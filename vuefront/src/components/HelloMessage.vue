<template>
  <div class="container">
    <h1>CP短打生成器 V2</h1>
    <br />
    <br />
    <el-row :gutter="18">
      <el-col :xs="24" :sm="12" :md="12" :lg="12" style="margin-top:15px;">
        <el-input placeholder="攻め" v-model="gong">
          <template slot="prepend">攻</template>
        </el-input>
      </el-col>
      <el-col :xs="24" :sm="12" :md="12" :lg="12" style="margin-top:15px;">
        <el-input placeholder="受け" v-model="shou">
          <template slot="prepend">受</template>
        </el-input>
      </el-col>
    </el-row>
    <br />
    <br />
    <el-row type="flex" class="row-bg" justify="center">
      <el-button
        type="success"
        @click="writeStory"
        :disabled="gong === '' || shou === ''"
      >{{btnText}}</el-button>

      <el-button type="primary" icon="el-icon-plus" @click="dialogAdd = true">投稿</el-button>
    </el-row>

    <el-divider></el-divider>

    <el-main>
      <p id="story" v-html="story">{{story}}</p>
    </el-main>

    <!-- Add Messages -->
    <el-dialog title="投稿(需审核)" :visible.sync="dialogAdd" :width="dialogWidth">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="作者*">
          <el-input v-model="form.author"></el-input>
        </el-form-item>

        <el-form-item label="创意*">
          <el-input
            type="textarea"
            :autosize="{ minRows: 1, maxRows: 5}"
            v-model="form.content"
            placeholder="投稿格式 e.g. 都说<攻>的眼里藏了长驻的冰雪。<受>阖眸前迷迷糊糊地笑——你看，这不是化了吗？"
          ></el-input>
        </el-form-item>

        <el-form-item label="标签">
          <el-tag
            :key="tag"
            v-for="tag in form.tags"
            effect="dark"
            closable
            :disable-transitions="false"
            type="success"
            @close="handleClose(tag)"
          >{{tag}}</el-tag>
          <el-input
            class="input-new-tag"
            v-if="form.inputVisible"
            v-model="form.inputValue"
            ref="saveTagInput"
            size="small"
            @keyup.enter.native="handleInputConfirm"
            @blur="handleInputConfirm"
          ></el-input>
          <el-button
            v-else
            class="button-new-tag"
            size="small"
            @click="showInput"
            icon="el-icon-plus"
            circle
          ></el-button>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button
          type="primary"
          @click="addMessage({ author: form.author, content: form.content, is_public: form.is_public,tags:form.tags})"
          :disabled="!form.content || !form.author "
        >Submit</el-button>
      </span>
    </el-dialog>

    <!-- Edit Messages -->
    <el-dialog title="编辑" :visible.sync="dialogEdit" width="50%">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="作者">
          <el-input v-model="form.author"></el-input>
        </el-form-item>
        <el-form-item label="Content">
          <el-input type="textarea" autosize v-model="form.content"></el-input>
        </el-form-item>
        <el-form-item label="Tags">
          <el-tag
            :key="tag"
            v-for="tag in form.tags "
            closable
            :disable-transitions="false"
            @close="handleClose(tag)"
          >{{tag}}</el-tag>
          <el-input
            class="input-new-tag"
            v-if="form.inputVisible"
            v-model="form.inputValue"
            ref="saveTagInput"
            size="small"
            @keyup.enter.native="handleInputConfirm"
            @blur="handleInputConfirm"
          ></el-input>
          <el-button
            v-else
            class="button-new-tag"
            size="small"
            @click="showInput"
            icon="el-icon-plus"
            circle
          ></el-button>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button
          type="primary"
          @click="putMessage({id: form.id, author: form.author,content: form.content, tags:form.tags})"
          :disabled="!form.content"
        >Submit</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Messages",
  data() {
    return {
      gong: "",
      shou: "",
      story: "",
      btnText: "生成故事",
      dialogAdd: false,
      dialogEdit: false,
      dialogWidth: 0
    };
  },
  computed: mapState({
    messages: state => state.messages,
    form: state => state.form
  }),
  methods: {
    writeStory: function() {
      let index;
      if (this.story === "") {
        index = 0;
      } else {
        index = Math.floor(Math.random() * this.messages.length);
      }
      this.shuffle(this.messages);

      if (this.story !== '') {
          this.btnText = "再生一个";
        } else {
          this.btnText = "生成故事";
        }

      this.story = this.messages[index].content
        .replace(
          new RegExp("<攻>", "g"),
          '<span class="e-brown">' + this.gong + "</span>"
        )
        .replace(
          new RegExp("<受>", "g"),
          '<span class="e-pink">' + this.shou + "</span>"
        );
      this.story =
        this.story +
        "<br><br><span> By " +
        this.messages[index].author +
        "</span>";
    },
    shuffle: function(array) {
      for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    },
    openVn() {
      const h = this.$createElement;
      this.$message({
        message: h("p", null, [
          h("span", null, "提交成功"),
          h("strong", { style: "color: #FFBF00" }, "!!!")
        ])
      });
    },
    addMessage(item) {
      this.$store.dispatch("addMessage", item);
      this.openVn();
    },
    getMessage(pk) {
      this.$store.dispatch("getMessage", pk)
      this.dialogEdit = true;
    },
    patchMessage(item) {
      // anyway, yes - store.dispatch() only accepts one argument, and your action function will only receive one
      // this.$store.dispatch("patchMessage", pk, item) would not work !!!
      this.$store.dispatch("patchMessage", item);
    },
    putMessage(item) {
      this.$store.dispatch("putMessage", item);
    },
    deleteMessage(pk) {
      this.$store.dispatch("deleteMessage", pk);
    },
    handleClose(tag) {
      this.form.tags.splice(this.form.tags.indexOf(tag), 1);
    },

    showInput() {
      this.form.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.form.inputValue;
      if (inputValue) {
        this.form.tags.push(inputValue);
      }
      this.form.inputVisible = false;
      this.form.inputValue = "";
    },
    setDialogWidth() {
      let width = document.body.clientWidth;
      const margin = 640; // 默认宽度
      if (width < margin) {
        this.dialogWidth = "90%";
      } else {
        this.dialogWidth = margin + "px";
      }
    }
  },
  created() {
    this.$store.dispatch("getMessages");
    this.setDialogWidth();
  }
};
</script>

<style>
.box-card {
  margin-top: 20px;
  margin-bottom: 20px;
}

.time {
  font-size: 13px;
  color: #999;
}

.tags {
  margin-right: 10px;
  margin-bottom: 5px;
}

.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
}
.e-pink {
  border-bottom: 2px solid #f56c6c;
}
.e-brown {
  border-bottom: 2px solid #303133;
}
</style>


