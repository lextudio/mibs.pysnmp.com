# SNMP MIB module (HPNSAPCI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAPCI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:23 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaPci_ObjectIdentity = ObjectIdentity
hpnsaPci = _HpnsaPci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10)
)
_HpnsaPciMibRev_ObjectIdentity = ObjectIdentity
hpnsaPciMibRev = _HpnsaPciMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 1)
)


class _HpnsaPciMibRevMajor_Type(Integer32):
    """Custom type hpnsaPciMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaPciMibRevMajor_Type.__name__ = "Integer32"
_HpnsaPciMibRevMajor_Object = MibScalar
hpnsaPciMibRevMajor = _HpnsaPciMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 1, 1),
    _HpnsaPciMibRevMajor_Type()
)
hpnsaPciMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciMibRevMajor.setStatus("mandatory")


class _HpnsaPciMibRevMinor_Type(Integer32):
    """Custom type hpnsaPciMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaPciMibRevMinor_Type.__name__ = "Integer32"
_HpnsaPciMibRevMinor_Object = MibScalar
hpnsaPciMibRevMinor = _HpnsaPciMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 1, 2),
    _HpnsaPciMibRevMinor_Type()
)
hpnsaPciMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciMibRevMinor.setStatus("mandatory")
_HpnsaPciAgent_ObjectIdentity = ObjectIdentity
hpnsaPciAgent = _HpnsaPciAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 2)
)
_HpnsaPciAgentTable_Object = MibTable
hpnsaPciAgentTable = _HpnsaPciAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaPciAgentTable.setStatus("mandatory")
_HpnsaPciAgentEntry_Object = MibTableRow
hpnsaPciAgentEntry = _HpnsaPciAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 2, 1, 1)
)
hpnsaPciAgentEntry.setIndexNames(
    (0, "HPNSAPCI-MIB", "hpnsaPciAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaPciAgentEntry.setStatus("mandatory")


class _HpnsaPciAgentIndex_Type(Integer32):
    """Custom type hpnsaPciAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciAgentIndex_Type.__name__ = "Integer32"
_HpnsaPciAgentIndex_Object = MibTableColumn
hpnsaPciAgentIndex = _HpnsaPciAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 2, 1, 1, 1),
    _HpnsaPciAgentIndex_Type()
)
hpnsaPciAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciAgentIndex.setStatus("mandatory")


class _HpnsaPciAgentName_Type(DisplayString):
    """Custom type hpnsaPciAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaPciAgentName_Type.__name__ = "DisplayString"
_HpnsaPciAgentName_Object = MibTableColumn
hpnsaPciAgentName = _HpnsaPciAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 2, 1, 1, 2),
    _HpnsaPciAgentName_Type()
)
hpnsaPciAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciAgentName.setStatus("mandatory")


class _HpnsaPciAgentVersion_Type(DisplayString):
    """Custom type hpnsaPciAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnsaPciAgentVersion_Type.__name__ = "DisplayString"
_HpnsaPciAgentVersion_Object = MibTableColumn
hpnsaPciAgentVersion = _HpnsaPciAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 2, 1, 1, 3),
    _HpnsaPciAgentVersion_Type()
)
hpnsaPciAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciAgentVersion.setStatus("mandatory")


class _HpnsaPciAgentDate_Type(OctetString):
    """Custom type hpnsaPciAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_HpnsaPciAgentDate_Type.__name__ = "OctetString"
_HpnsaPciAgentDate_Object = MibTableColumn
hpnsaPciAgentDate = _HpnsaPciAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 2, 1, 1, 4),
    _HpnsaPciAgentDate_Type()
)
hpnsaPciAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciAgentDate.setStatus("mandatory")
_HpnsaPciBios_ObjectIdentity = ObjectIdentity
hpnsaPciBios = _HpnsaPciBios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 3)
)


class _HpnsaPciBiosPresent_Type(Integer32):
    """Custom type hpnsaPciBiosPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("present", 1))
    )


_HpnsaPciBiosPresent_Type.__name__ = "Integer32"
_HpnsaPciBiosPresent_Object = MibScalar
hpnsaPciBiosPresent = _HpnsaPciBiosPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 3, 1),
    _HpnsaPciBiosPresent_Type()
)
hpnsaPciBiosPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciBiosPresent.setStatus("mandatory")
_HpnsaPciBiosVersion_Type = Integer32
_HpnsaPciBiosVersion_Object = MibScalar
hpnsaPciBiosVersion = _HpnsaPciBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 3, 2),
    _HpnsaPciBiosVersion_Type()
)
hpnsaPciBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciBiosVersion.setStatus("mandatory")


class _HpnsaPciBuses_Type(Integer32):
    """Custom type hpnsaPciBuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciBuses_Type.__name__ = "Integer32"
_HpnsaPciBuses_Object = MibScalar
hpnsaPciBuses = _HpnsaPciBuses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 3, 3),
    _HpnsaPciBuses_Type()
)
hpnsaPciBuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciBuses.setStatus("mandatory")
_HpnsaPciConfig_ObjectIdentity = ObjectIdentity
hpnsaPciConfig = _HpnsaPciConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4)
)
_HpnsaPciTable_Object = MibTable
hpnsaPciTable = _HpnsaPciTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaPciTable.setStatus("mandatory")
_HpnsaPciEntry_Object = MibTableRow
hpnsaPciEntry = _HpnsaPciEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1)
)
hpnsaPciEntry.setIndexNames(
    (0, "HPNSAPCI-MIB", "hpnsaPciBusIndex"),
    (0, "HPNSAPCI-MIB", "hpnsaPciDeviceIndex"),
    (0, "HPNSAPCI-MIB", "hpnsaPciFunctionIndex"),
)
if mibBuilder.loadTexts:
    hpnsaPciEntry.setStatus("mandatory")


class _HpnsaPciBusIndex_Type(Integer32):
    """Custom type hpnsaPciBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciBusIndex_Type.__name__ = "Integer32"
_HpnsaPciBusIndex_Object = MibTableColumn
hpnsaPciBusIndex = _HpnsaPciBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 1),
    _HpnsaPciBusIndex_Type()
)
hpnsaPciBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciBusIndex.setStatus("mandatory")


class _HpnsaPciDeviceIndex_Type(Integer32):
    """Custom type hpnsaPciDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HpnsaPciDeviceIndex_Type.__name__ = "Integer32"
_HpnsaPciDeviceIndex_Object = MibTableColumn
hpnsaPciDeviceIndex = _HpnsaPciDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 2),
    _HpnsaPciDeviceIndex_Type()
)
hpnsaPciDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciDeviceIndex.setStatus("mandatory")


class _HpnsaPciFunctionIndex_Type(Integer32):
    """Custom type hpnsaPciFunctionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnsaPciFunctionIndex_Type.__name__ = "Integer32"
_HpnsaPciFunctionIndex_Object = MibTableColumn
hpnsaPciFunctionIndex = _HpnsaPciFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 3),
    _HpnsaPciFunctionIndex_Type()
)
hpnsaPciFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciFunctionIndex.setStatus("mandatory")


class _HpnsaPciVendorId_Type(Integer32):
    """Custom type hpnsaPciVendorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4098,
              4099,
              4100,
              4101,
              4102,
              4103,
              4104,
              4106,
              4107,
              4108,
              4109,
              4110,
              4112,
              4113,
              4114,
              4115,
              4116,
              4118,
              4119,
              4120,
              4121,
              4122,
              4123,
              4124,
              4126,
              4127,
              4128,
              4129,
              4130,
              4131,
              4132,
              4133,
              4136,
              4137,
              4139,
              4140,
              4141,
              4142,
              4143,
              4144,
              4145,
              4146,
              4147,
              4148,
              4149,
              4150,
              4151,
              4152,
              4153,
              4154,
              4155,
              4156,
              4158,
              4159,
              4160,
              4161,
              4162,
              4163,
              4164,
              4165,
              4166,
              4167,
              4168,
              4169,
              4170,
              4171,
              4172,
              4173,
              4174,
              4175,
              4176,
              4177,
              4178,
              4180,
              4181,
              4182,
              4183,
              4184,
              4185,
              4186,
              4187,
              4188,
              4189,
              4190,
              4191,
              4192,
              4193,
              4194,
              4195,
              4196,
              4197,
              4198,
              4199,
              4200,
              4201,
              4202,
              4203,
              4203,
              4204,
              4205,
              4206,
              4207,
              4208,
              4209,
              4210,
              4211,
              4212,
              4213,
              4214,
              4215,
              4216,
              4217,
              4218,
              4219,
              4220,
              4221,
              4222,
              4223,
              4224,
              4225,
              4226,
              4227,
              4228,
              4229,
              4230,
              4231,
              4232,
              4233,
              4234,
              4236,
              4237,
              4239,
              4240,
              4241,
              4242,
              4243,
              4244,
              4245,
              4246,
              4247,
              4248,
              4249,
              4250,
              4251,
              4252,
              4253,
              4254,
              4255,
              4256,
              4257,
              4258,
              4259,
              4260,
              4261,
              4262,
              4263,
              4264,
              4265,
              4266,
              4267,
              4268,
              4269,
              4270,
              4271,
              4272,
              4273,
              4274,
              4275,
              4276,
              4277,
              4279,
              4280,
              4281,
              4282,
              4283,
              4284,
              4285,
              4286,
              4287,
              4288,
              4289,
              4290,
              4291,
              4292,
              4293,
              4294,
              4295,
              4296,
              4297,
              4298,
              4299,
              4300,
              4301,
              4302,
              4303,
              4304,
              4305,
              4306,
              4307,
              4308,
              4309,
              4310,
              4312,
              4313,
              4314,
              4315,
              4316,
              4317,
              4318,
              4319,
              4320,
              4321,
              4322,
              4323,
              4324,
              4325,
              4326,
              4327,
              4328,
              4329,
              4330,
              4331,
              4332,
              4333,
              4334,
              4335,
              4336,
              4337,
              4338,
              4339,
              4340,
              4341,
              4342,
              4343,
              4344,
              4345,
              4346,
              4347,
              4348,
              4349,
              4350,
              4351,
              4352,
              4353,
              4354,
              4355,
              4356,
              4357,
              4358,
              4359,
              4360,
              4361,
              4363,
              4364,
              4365,
              4366,
              4367,
              4368,
              4369,
              4370,
              4371,
              4372,
              4373,
              4374,
              4375,
              4376,
              4377,
              4378,
              4379,
              4380,
              4381,
              4382,
              4383,
              4384,
              4385,
              4386,
              4388,
              4389,
              4389,
              4393,
              4394,
              4395,
              4397,
              4398,
              4399,
              4400,
              4401,
              4402,
              4403,
              4404,
              4405,
              4406,
              4407,
              4408,
              4409,
              4410,
              4412,
              4413,
              4414,
              4415,
              4416,
              4417,
              4418,
              4419,
              4420,
              4421,
              4422,
              4423,
              4424,
              4425,
              4426,
              4427,
              4428,
              4429,
              4430,
              4431,
              4432,
              4433,
              4434,
              4435,
              4436,
              4437,
              4438,
              21299,
              22272)
        )
    )
    namedValues = NamedValues(
        *(("acc-microelectronics-corp", 4266),
          ("accton-technology-corporation", 4371),
          ("acer-incorporated", 4133),
          ("acer-labs", 4281),
          ("achme-computer-inc", 4338),
          ("advanced-integration-res", 4213),
          ("advanced-logic-research-inc", 4284),
          ("advanced-micro-devices", 4130),
          ("advanced-peripherals-labs", 4312),
          ("advanced-system-products", 4301),
          ("alacron", 4246),
          ("alaris-inc", 4339),
          ("alcatel-cit", 4196),
          ("alliance-semiconductor-corporation", 4418),
          ("alps-electric-co-ltd", 4329),
          ("altos-india-ltd", 4344),
          ("american-megatrends", 4126),
          ("amp-inc", 4152),
          ("anigma-inc", 4177),
          ("annabooks", 4428),
          ("appian-technology-inc", 4247),
          ("apple-computer-inc", 4203),
          ("applied-micro-circuits-corporation", 4328),
          ("aptix-corporation", 4322),
          ("artists-graphics", 4331),
          ("ascii-corporation", 4333),
          ("ast-research-inc", 4109),
          ("asustek-computer-inc", 4163),
          ("aten-research-inc", 4202),
          ("ati-technologies-inc", 4098),
          ("atmel-corp", 4372),
          ("auspex-systems-inc", 4290),
          ("autologic-inc", 4309),
          ("avance-logics-inc", 4101),
          ("award-software-intl-inc", 4292),
          ("benchmarq-microelectronics", 4263),
          ("berg-electronics", 4376),
          ("bit3-computer", 4234),
          ("boca-research-inc", 4288),
          ("brooktree-corporation", 4254),
          ("burndy-corporation", 4148),
          ("buslogic", 4171),
          ("cabletron-systems-inc", 4273),
          ("cache-computer", 4231),
          ("canopus-co-ltd", 4427),
          ("cardexpert-technology", 4272),
          ("cern-ecp-edu", 4316),
          ("cetia", 4310),
          ("chaintech-computer-co-ltd", 4214),
          ("chips-and-technologies", 4140),
          ("cincinnati-milacron", 4420),
          ("cirrus-logic", 4115),
          ("cisco-systems-inc", 4407),
          ("citicorp-tti", 4303),
          ("city-gate-development-ltd", 4207),
          ("cmd-technology-inc", 4245),
          ("co-time-computer-ltd", 4175),
          ("cogent-data-technologies", 4361),
          ("comp-comm-resh-lab", 4149),
          ("compaq", 4146),
          ("computervision", 4400),
          ("computrend", 4161),
          ("contaq-microsystems-inc", 4224),
          ("cornerstone-technology", 4270),
          ("cpu-technology", 4366),
          ("creative-electronic-systems-sa", 4342),
          ("creative-labs", 4354),
          ("crest-microsystem-inc", 4417),
          ("cyclone-micro", 4412),
          ("cyrix-corporation", 4216),
          ("daewoo-telecom-ltd", 4208),
          ("dapha-electronics-corporation", 4283),
          ("data-general-corporation", 4233),
          ("data-technology-corporation", 4223),
          ("data-translation", 4374),
          ("databook-inc", 4275),
          ("datacube-inc", 4375),
          ("dataexpert-corporation", 4297),
          ("dec", 4113),
          ("dell-computer-corporation", 4136),
          ("dfi-inc", 4206),
          ("diamond-computer-systems", 4242),
          ("digi-international", 4431),
          ("digicom", 4267),
          ("distributed-processing-technology", 4164),
          ("diversified-technology", 4200),
          ("dynamic-pictures-inc", 4409),
          ("efa-corporation-of-america", 4226),
          ("efar-microsystems", 4181),
          ("efficent-networks-inc", 4378),
          ("eicon-technology-corporation", 4403),
          ("eldec-corporaton", 4382),
          ("electronics-telec-rsh", 4184),
          ("elitegroup-computer-sys", 4121),
          ("elsa-gmbh", 4168),
          ("emc-corporation", 4384),
          ("emulex-corporation", 4319),
          ("encore-computer-corporation", 4240),
          ("epson", 4104),
          ("equinox-systems", 4415),
          ("eurocore", 4389),
          ("evans-sutherland", 4317),
          ("everex-systems-inc", 4259),
          ("fast-electronic-gmbh", 4350),
          ("firmworks", 4393),
          ("first-intl-computers", 4244),
          ("force-computers", 4422),
          ("forex-computer-corporation", 4227),
          ("fountain-technology", 4169),
          ("foxconn-international", 4187),
          ("fuji-xerox-co-ltd", 4405),
          ("fujitsu", 4298),
          ("fujitsu-limited", 4304),
          ("future-domain", 4150),
          ("future-systems", 4305),
          ("fwb-inc", 4410),
          ("gainbery-computer-products-inc", 4326),
          ("gateway-2000", 4219),
          ("gemlight-computer-ltd", 4251),
          ("genoa-systems-corp", 4167),
          ("git-co-ltd", 4210),
          ("globe-manufacturing-sales", 4260),
          ("goldstar-co-ltd", 4220),
          ("hermes-electronics-co-ltd", 4394),
          ("hewlett-packard", 4156),
          ("hitachi-computer-products", 4128),
          ("hitachi-ltd", 4180),
          ("hitachi-micro-systems", 4151),
          ("honeywell-iasd", 4268),
          ("hualon-microelectronics", 4308),
          ("hyundai-electronics-ameri", 4204),
          ("i-bus", 4217),
          ("i-o-data-device-inc", 4348),
          ("i-t-t", 4193),
          ("ibm", 4116),
          ("ic-corporation", 4429),
          ("icl", 4182),
          ("icl-personal-systems", 4118),
          ("icm-co-ltd", 4289),
          ("imaging-technology-inc", 4399),
          ("infomedia-microelectronics-inc", 4398),
          ("informtech-industrial-ltd", 4262),
          ("infotronic-america-inc", 4191),
          ("initio-corporation", 4353),
          ("integraphics-systems", 4330),
          ("integrated-device-tech", 4381),
          ("integrated-micro-solutions-inc", 4320),
          ("interface-corp", 4423),
          ("intergraph-corporation", 4241),
          ("interphase-corporation", 4222),
          ("intervoice-inc", 4416),
          ("ipc-corporation-ltd", 4166),
          ("j-bond-computer-systems", 4230),
          ("jabil-circuit-inc", 4307),
          ("jae-electronics-inc", 4433),
          ("jazz-multimedia", 4352),
          ("juko-electronics-ind-co-ltd", 4257),
          ("kubota-pacific-computer-inc", 4160),
          ("land-win-electronic-corp", 4435),
          ("leading-edge-products-inc", 4413),
          ("leadtek-research-inc", 4221),
          ("leutron-vision-ag", 4388),
          ("linotype-hell-ag", 4395),
          ("logic-modeling", 4159),
          ("macronix-international-co-ltd", 4313),
          ("madge-networks", 4203),
          ("maspar-computer-corp", 4194),
          ("matrox", 4139),
          ("matsushita-electric-industrial-co-ltd", 4343),
          ("media-vision", 4295),
          ("megachips-corporation", 4252),
          ("megatek", 4434),
          ("meidensha-corporation", 4256),
          ("melco-inc", 4436),
          ("mentor-arc-inc", 4300),
          ("mercury-computer-systems-inc", 4404),
          ("micro-computer-sysytems-inc", 4271),
          ("micro-industries-corporation", 4325),
          ("microcomputer-systems-m-son", 4232),
          ("micronics-computers-inc", 4114),
          ("mini-max-technology-inc", 4364),
          ("miro-computer-products-ag", 4145),
          ("mitac", 4209),
          ("mitel-corp", 4402),
          ("mitsubishi-electronics", 4199),
          ("mitsubishi-electronics-corp", 4282),
          ("molex-incorporated", 4306),
          ("momentum-data-systems", 4406),
          ("most-inc", 4287),
          ("motorola-computer", 4183),
          ("multi-tech-systems-inc", 4386),
          ("mylex-corporation", 4201),
          ("national-instruments", 4243),
          ("national-semiconductor", 4107),
          ("ncr", 4122),
          ("ncube", 4351),
          ("nec-corporation", 4147),
          ("neomagic-corporation", 4296),
          ("netframe-systems-inc", 4103),
          ("netpower", 22272),
          ("netpower-inc", 4419),
          ("networth", 4218),
          ("newbridge-microsystems", 4323),
          ("nexgen-microsysteme", 4212),
          ("nikon-systems-inc", 4430),
          ("nkk-corporation", 4341),
          ("number-9-computer-company", 4189),
          ("nvidia-corporation", 4318),
          ("oak-technology-inc", 4174),
          ("oakleigh-systems-inc", 4236),
          ("ocean-office-automation", 4195),
          ("oki-electric-industry", 4129),
          ("olicom", 4237),
          ("olivetti-advanced-technology", 4142),
          ("omron-corporation", 4299),
          ("opti", 4165),
          ("packard-bell", 4250),
          ("parador", 4228),
          ("pc-direct", 4345),
          ("pc-technology-inc", 4162),
          ("periscope-engineering", 4438),
          ("peritek-corporation", 4336),
          ("philips-semiconductors", 4401),
          ("phoenix-technologies", 4106),
          ("picopower-technology", 4198),
          ("picture-tel", 4127),
          ("pine-technology-ltd", 4437),
          ("plx-technology", 4277),
          ("powerhouse-systems", 4368),
          ("prescision-digital-images", 4383),
          ("promise-technology", 4186),
          ("proteon-inc", 4360),
          ("q-logic", 4215),
          ("quantum-corporation", 4258),
          ("quantum-designs-hk-ltd", 4248),
          ("racal-interlan", 4261),
          ("racore-computer-products-inc", 4335),
          ("radius-inc", 4302),
          ("rambus-inc", 4294),
          ("rasterops", 4356),
          ("ravicad", 4397),
          ("raytheon-company", 4274),
          ("realtek-semiconductor-co-ltd", 4332),
          ("reply-group", 4102),
          ("rockwell-network-systems", 4370),
          ("rohm-research", 4315),
          ("ross-technology", 4367),
          ("s-mos-systems", 4340),
          ("s3-inc", 21299),
          ("samsung-electronics-co-ltd", 4249),
          ("samsung-semiconductors", 4291),
          ("santa-cruz-operation", 4369),
          ("sanyo-electric-co", 4414),
          ("schneider-koch-co", 4424),
          ("seiko-epson-corporation", 4154),
          ("sequent", 4205),
          ("sgs-thomson-microelectric", 4170),
          ("siemens-nixdorf-is-ag", 4137),
          ("sierra-semiconductor", 4264),
          ("sigma-designs-inc", 4357),
          ("silicon-graphics", 4265),
          ("silicon-integrated-system", 4153),
          ("solliday-engineering", 4158),
          ("sony-corporation", 4173),
          ("soyo-technology-co-ltd", 4349),
          ("spea-software-ag", 4119),
          ("standard-microsystems-corporation", 4280),
          ("stb-systems-inc", 4276),
          ("stratus-computer", 4359),
          ("supermac-technology-inc", 4225),
          ("surecom-technology", 4285),
          ("symphony-labs", 4269),
          ("systemsoft-corporation", 4239),
          ("tandem-computers", 4324),
          ("tatung-co-of-america", 4155),
          ("teknor-microsystems", 4185),
          ("tekram-technology-co-ltd", 4321),
          ("teledyne-electronic-systems", 4379),
          ("texas-instruments", 4172),
          ("texas-microsystems", 4197),
          ("thesys-ges-f-mikroelektronik-mgh", 4347),
          ("thinking-machines-corp", 4432),
          ("thomas-conrad-corporation", 4314),
          ("three-3com-corporation", 4279),
          ("three-3dlabs", 4373),
          ("tmc-research", 4144),
          ("toshiba-america-elect", 4143),
          ("tricord-systems-inc", 4380),
          ("trident-microsystems", 4131),
          ("trigem-computer-inc", 4255),
          ("triones-technologies-inc", 4355),
          ("truevision", 4346),
          ("tseng-labs-inc", 4108),
          ("tsenglabs-international-co", 4286),
          ("tulip-computers-int-bv", 4229),
          ("tyan-computer", 4337),
          ("ulsi-systems", 4099),
          ("unisys-systems", 4120),
          ("united-microelectronics", 4192),
          ("vadem", 4327),
          ("via-technologies-inc", 4358),
          ("video-logic-ltd", 4112),
          ("vigra", 4389),
          ("vitesse-semiconductor", 4123),
          ("vlsi-technology-inc", 4100),
          ("vmic", 4426),
          ("vortex-computersysteme-gmbh", 4377),
          ("vtech-computers-limites", 4190),
          ("weitek", 4110),
          ("western-digital", 4124),
          ("win-system-corporation", 4425),
          ("winbond-electronics-corp", 4176),
          ("wipro-infotech-limited", 4188),
          ("workbit-corp", 4421),
          ("wyse-technology", 4141),
          ("xenon-microsystems", 4363),
          ("xerox-corporation", 4293),
          ("xilinx-corporation", 4334),
          ("yamaha-corporation", 4211),
          ("young-micro-systems", 4178),
          ("zenith-data-systems", 4132),
          ("ziatech-corporation", 4408),
          ("zida-technologies-ltd", 4253),
          ("zilog", 4385),
          ("znyx-advanced-systems", 4365))
    )


_HpnsaPciVendorId_Type.__name__ = "Integer32"
_HpnsaPciVendorId_Object = MibTableColumn
hpnsaPciVendorId = _HpnsaPciVendorId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 4),
    _HpnsaPciVendorId_Type()
)
hpnsaPciVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciVendorId.setStatus("mandatory")
_HpnsaPciDeviceId_Type = Integer32
_HpnsaPciDeviceId_Object = MibTableColumn
hpnsaPciDeviceId = _HpnsaPciDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 5),
    _HpnsaPciDeviceId_Type()
)
hpnsaPciDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciDeviceId.setStatus("mandatory")
_HpnsaPciRevisionId_Type = Integer32
_HpnsaPciRevisionId_Object = MibTableColumn
hpnsaPciRevisionId = _HpnsaPciRevisionId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 6),
    _HpnsaPciRevisionId_Type()
)
hpnsaPciRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciRevisionId.setStatus("mandatory")


class _HpnsaPciHeaderType_Type(Integer32):
    """Custom type hpnsaPciHeaderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciHeaderType_Type.__name__ = "Integer32"
_HpnsaPciHeaderType_Object = MibTableColumn
hpnsaPciHeaderType = _HpnsaPciHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 7),
    _HpnsaPciHeaderType_Type()
)
hpnsaPciHeaderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciHeaderType.setStatus("mandatory")


class _HpnsaPciClassCode_Type(OctetString):
    """Custom type hpnsaPciClassCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnsaPciClassCode_Type.__name__ = "OctetString"
_HpnsaPciClassCode_Object = MibTableColumn
hpnsaPciClassCode = _HpnsaPciClassCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 8),
    _HpnsaPciClassCode_Type()
)
hpnsaPciClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciClassCode.setStatus("mandatory")
_HpnsaPciCommand_Type = Integer32
_HpnsaPciCommand_Object = MibTableColumn
hpnsaPciCommand = _HpnsaPciCommand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 9),
    _HpnsaPciCommand_Type()
)
hpnsaPciCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciCommand.setStatus("mandatory")
_HpnsaPciStatus_Type = Integer32
_HpnsaPciStatus_Object = MibTableColumn
hpnsaPciStatus = _HpnsaPciStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 10),
    _HpnsaPciStatus_Type()
)
hpnsaPciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciStatus.setStatus("mandatory")


class _HpnsaPciCacheLineSize_Type(Integer32):
    """Custom type hpnsaPciCacheLineSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciCacheLineSize_Type.__name__ = "Integer32"
_HpnsaPciCacheLineSize_Object = MibTableColumn
hpnsaPciCacheLineSize = _HpnsaPciCacheLineSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 11),
    _HpnsaPciCacheLineSize_Type()
)
hpnsaPciCacheLineSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciCacheLineSize.setStatus("mandatory")


class _HpnsaPciLatencyTimer_Type(Integer32):
    """Custom type hpnsaPciLatencyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciLatencyTimer_Type.__name__ = "Integer32"
_HpnsaPciLatencyTimer_Object = MibTableColumn
hpnsaPciLatencyTimer = _HpnsaPciLatencyTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 12),
    _HpnsaPciLatencyTimer_Type()
)
hpnsaPciLatencyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciLatencyTimer.setStatus("mandatory")


class _HpnsaPciBist_Type(Integer32):
    """Custom type hpnsaPciBist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciBist_Type.__name__ = "Integer32"
_HpnsaPciBist_Object = MibTableColumn
hpnsaPciBist = _HpnsaPciBist_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 13),
    _HpnsaPciBist_Type()
)
hpnsaPciBist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciBist.setStatus("mandatory")


class _HpnsaPciInterruptLine_Type(Integer32):
    """Custom type hpnsaPciInterruptLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciInterruptLine_Type.__name__ = "Integer32"
_HpnsaPciInterruptLine_Object = MibTableColumn
hpnsaPciInterruptLine = _HpnsaPciInterruptLine_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 14),
    _HpnsaPciInterruptLine_Type()
)
hpnsaPciInterruptLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciInterruptLine.setStatus("mandatory")


class _HpnsaPciInterruptPin_Type(Integer32):
    """Custom type hpnsaPciInterruptPin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciInterruptPin_Type.__name__ = "Integer32"
_HpnsaPciInterruptPin_Object = MibTableColumn
hpnsaPciInterruptPin = _HpnsaPciInterruptPin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 15),
    _HpnsaPciInterruptPin_Type()
)
hpnsaPciInterruptPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciInterruptPin.setStatus("mandatory")


class _HpnsaPciMaxLat_Type(Integer32):
    """Custom type hpnsaPciMaxLat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciMaxLat_Type.__name__ = "Integer32"
_HpnsaPciMaxLat_Object = MibTableColumn
hpnsaPciMaxLat = _HpnsaPciMaxLat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 16),
    _HpnsaPciMaxLat_Type()
)
hpnsaPciMaxLat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciMaxLat.setStatus("mandatory")


class _HpnsaPciMinGnt_Type(Integer32):
    """Custom type hpnsaPciMinGnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaPciMinGnt_Type.__name__ = "Integer32"
_HpnsaPciMinGnt_Object = MibTableColumn
hpnsaPciMinGnt = _HpnsaPciMinGnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 17),
    _HpnsaPciMinGnt_Type()
)
hpnsaPciMinGnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciMinGnt.setStatus("mandatory")


class _HpnsaPciBaseAddrRegs_Type(OctetString):
    """Custom type hpnsaPciBaseAddrRegs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_HpnsaPciBaseAddrRegs_Type.__name__ = "OctetString"
_HpnsaPciBaseAddrRegs_Object = MibTableColumn
hpnsaPciBaseAddrRegs = _HpnsaPciBaseAddrRegs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 18),
    _HpnsaPciBaseAddrRegs_Type()
)
hpnsaPciBaseAddrRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciBaseAddrRegs.setStatus("mandatory")


class _HpnsaPciExpRomBaseAddr_Type(OctetString):
    """Custom type hpnsaPciExpRomBaseAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpnsaPciExpRomBaseAddr_Type.__name__ = "OctetString"
_HpnsaPciExpRomBaseAddr_Object = MibTableColumn
hpnsaPciExpRomBaseAddr = _HpnsaPciExpRomBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 19),
    _HpnsaPciExpRomBaseAddr_Type()
)
hpnsaPciExpRomBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciExpRomBaseAddr.setStatus("mandatory")


class _HpnsaPciDeviceSpecific_Type(OctetString):
    """Custom type hpnsaPciDeviceSpecific based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(192, 192),
    )


_HpnsaPciDeviceSpecific_Type.__name__ = "OctetString"
_HpnsaPciDeviceSpecific_Object = MibTableColumn
hpnsaPciDeviceSpecific = _HpnsaPciDeviceSpecific_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 10, 4, 1, 1, 20),
    _HpnsaPciDeviceSpecific_Type()
)
hpnsaPciDeviceSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaPciDeviceSpecific.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAPCI-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaPci": hpnsaPci,
       "hpnsaPciMibRev": hpnsaPciMibRev,
       "hpnsaPciMibRevMajor": hpnsaPciMibRevMajor,
       "hpnsaPciMibRevMinor": hpnsaPciMibRevMinor,
       "hpnsaPciAgent": hpnsaPciAgent,
       "hpnsaPciAgentTable": hpnsaPciAgentTable,
       "hpnsaPciAgentEntry": hpnsaPciAgentEntry,
       "hpnsaPciAgentIndex": hpnsaPciAgentIndex,
       "hpnsaPciAgentName": hpnsaPciAgentName,
       "hpnsaPciAgentVersion": hpnsaPciAgentVersion,
       "hpnsaPciAgentDate": hpnsaPciAgentDate,
       "hpnsaPciBios": hpnsaPciBios,
       "hpnsaPciBiosPresent": hpnsaPciBiosPresent,
       "hpnsaPciBiosVersion": hpnsaPciBiosVersion,
       "hpnsaPciBuses": hpnsaPciBuses,
       "hpnsaPciConfig": hpnsaPciConfig,
       "hpnsaPciTable": hpnsaPciTable,
       "hpnsaPciEntry": hpnsaPciEntry,
       "hpnsaPciBusIndex": hpnsaPciBusIndex,
       "hpnsaPciDeviceIndex": hpnsaPciDeviceIndex,
       "hpnsaPciFunctionIndex": hpnsaPciFunctionIndex,
       "hpnsaPciVendorId": hpnsaPciVendorId,
       "hpnsaPciDeviceId": hpnsaPciDeviceId,
       "hpnsaPciRevisionId": hpnsaPciRevisionId,
       "hpnsaPciHeaderType": hpnsaPciHeaderType,
       "hpnsaPciClassCode": hpnsaPciClassCode,
       "hpnsaPciCommand": hpnsaPciCommand,
       "hpnsaPciStatus": hpnsaPciStatus,
       "hpnsaPciCacheLineSize": hpnsaPciCacheLineSize,
       "hpnsaPciLatencyTimer": hpnsaPciLatencyTimer,
       "hpnsaPciBist": hpnsaPciBist,
       "hpnsaPciInterruptLine": hpnsaPciInterruptLine,
       "hpnsaPciInterruptPin": hpnsaPciInterruptPin,
       "hpnsaPciMaxLat": hpnsaPciMaxLat,
       "hpnsaPciMinGnt": hpnsaPciMinGnt,
       "hpnsaPciBaseAddrRegs": hpnsaPciBaseAddrRegs,
       "hpnsaPciExpRomBaseAddr": hpnsaPciExpRomBaseAddr,
       "hpnsaPciDeviceSpecific": hpnsaPciDeviceSpecific}
)
