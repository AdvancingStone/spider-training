def pie_base():
    from pyecharts import options as opts
    from pyecharts.charts import Page, Pie
    v1 = ["啤酒", "可乐", "雪碧", "咖啡", "奶茶"]
    v2 = [30, 19, 21, 12, 18]

    c = (
        Pie()
            .add("", [list(z) for z in zip(v1, v2)])
            .set_global_opts(title_opts=opts.TitleOpts(title="销售收入占比"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))  # 格式化标签输出内容
    )
    return c


pie_base().render_notebook()