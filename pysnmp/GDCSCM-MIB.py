# SNMP MIB module (GDCSCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCSCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:21 2024
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

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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
 NotificationType,
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
    "NotificationType",
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

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Sc_ObjectIdentity = ObjectIdentity
sc = _Sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3)
)
_ScmSystem_ObjectIdentity = ObjectIdentity
scmSystem = _ScmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 6)
)
_ScmVersion_ObjectIdentity = ObjectIdentity
scmVersion = _ScmVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 1)
)


class _ScmMIBVersion_Type(DisplayString):
    """Custom type scmMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_ScmMIBVersion_Type.__name__ = "DisplayString"
_ScmMIBVersion_Object = MibScalar
scmMIBVersion = _ScmMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 1, 1),
    _ScmMIBVersion_Type()
)
scmMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmMIBVersion.setStatus("mandatory")


class _ScmBootVersion_Type(DisplayString):
    """Custom type scmBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_ScmBootVersion_Type.__name__ = "DisplayString"
_ScmBootVersion_Object = MibScalar
scmBootVersion = _ScmBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 1, 2),
    _ScmBootVersion_Type()
)
scmBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmBootVersion.setStatus("mandatory")


class _ScmApplVersion_Type(DisplayString):
    """Custom type scmApplVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_ScmApplVersion_Type.__name__ = "DisplayString"
_ScmApplVersion_Object = MibScalar
scmApplVersion = _ScmApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 1, 3),
    _ScmApplVersion_Type()
)
scmApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmApplVersion.setStatus("mandatory")
_ScmMaster_ObjectIdentity = ObjectIdentity
scmMaster = _ScmMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2)
)


class _ScmMasterTimeout_Type(Integer32):
    """Custom type scmMasterTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 100),
    )


_ScmMasterTimeout_Type.__name__ = "Integer32"
_ScmMasterTimeout_Object = MibScalar
scmMasterTimeout = _ScmMasterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 1),
    _ScmMasterTimeout_Type()
)
scmMasterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmMasterTimeout.setStatus("mandatory")


class _ScmAlarmScan_Type(Integer32):
    """Custom type scmAlarmScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmScanOff", 2),
          ("alarmScanOn", 1))
    )


_ScmAlarmScan_Type.__name__ = "Integer32"
_ScmAlarmScan_Object = MibScalar
scmAlarmScan = _ScmAlarmScan_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 2),
    _ScmAlarmScan_Type()
)
scmAlarmScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmAlarmScan.setStatus("mandatory")


class _ScmTime_Type(DisplayString):
    """Custom type scmTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ScmTime_Type.__name__ = "DisplayString"
_ScmTime_Object = MibScalar
scmTime = _ScmTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 3),
    _ScmTime_Type()
)
scmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmTime.setStatus("obsolete")


class _ScmDate_Type(DisplayString):
    """Custom type scmDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ScmDate_Type.__name__ = "DisplayString"
_ScmDate_Object = MibScalar
scmDate = _ScmDate_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 4),
    _ScmDate_Type()
)
scmDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmDate.setStatus("obsolete")


class _ScmRedundant_Type(Integer32):
    """Custom type scmRedundant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("redundant", 1))
    )


_ScmRedundant_Type.__name__ = "Integer32"
_ScmRedundant_Object = MibScalar
scmRedundant = _ScmRedundant_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 5),
    _ScmRedundant_Type()
)
scmRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmRedundant.setStatus("mandatory")


class _ScmShelfNumber_Type(Integer32):
    """Custom type scmShelfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneShelf", 1),
          ("twoShelf", 2))
    )


_ScmShelfNumber_Type.__name__ = "Integer32"
_ScmShelfNumber_Object = MibScalar
scmShelfNumber = _ScmShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 6),
    _ScmShelfNumber_Type()
)
scmShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmShelfNumber.setStatus("mandatory")


class _ScmReset_Type(Integer32):
    """Custom type scmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_ScmReset_Type.__name__ = "Integer32"
_ScmReset_Object = MibScalar
scmReset = _ScmReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 7),
    _ScmReset_Type()
)
scmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmReset.setStatus("mandatory")
_ScmPowerAvail_Type = Gauge32
_ScmPowerAvail_Object = MibScalar
scmPowerAvail = _ScmPowerAvail_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 8),
    _ScmPowerAvail_Type()
)
scmPowerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPowerAvail.setStatus("mandatory")


class _ScmDefaultConfig_Type(Integer32):
    """Custom type scmDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryApplDefault", 2),
          ("normal", 1))
    )


_ScmDefaultConfig_Type.__name__ = "Integer32"
_ScmDefaultConfig_Object = MibScalar
scmDefaultConfig = _ScmDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 9),
    _ScmDefaultConfig_Type()
)
scmDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmDefaultConfig.setStatus("mandatory")
_ScmPowerConsum_Type = Gauge32
_ScmPowerConsum_Object = MibScalar
scmPowerConsum = _ScmPowerConsum_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 10),
    _ScmPowerConsum_Type()
)
scmPowerConsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPowerConsum.setStatus("mandatory")


class _ScmCannedConfig_Type(Integer32):
    """Custom type scmCannedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cannedConfig1", 2),
          ("cannedConfig2", 3),
          ("cannedConfig3", 4),
          ("cannedConfig4", 5),
          ("cannedConfig5", 6),
          ("cannedConfig6", 7),
          ("cannedConfig7", 8),
          ("cannedConfigNone", 1))
    )


_ScmCannedConfig_Type.__name__ = "Integer32"
_ScmCannedConfig_Object = MibScalar
scmCannedConfig = _ScmCannedConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 11),
    _ScmCannedConfig_Type()
)
scmCannedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmCannedConfig.setStatus("mandatory")


class _ScmSetNetworkElementRealTime_Type(Integer32):
    """Custom type scmSetNetworkElementRealTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScmSetNetworkElementRealTime_Type.__name__ = "Integer32"
_ScmSetNetworkElementRealTime_Object = MibScalar
scmSetNetworkElementRealTime = _ScmSetNetworkElementRealTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 12),
    _ScmSetNetworkElementRealTime_Type()
)
scmSetNetworkElementRealTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmSetNetworkElementRealTime.setStatus("mandatory")


class _ScmDownLoadCode_Type(Integer32):
    """Custom type scmDownLoadCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ScmDownLoadCode_Type.__name__ = "Integer32"
_ScmDownLoadCode_Object = MibScalar
scmDownLoadCode = _ScmDownLoadCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 13),
    _ScmDownLoadCode_Type()
)
scmDownLoadCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmDownLoadCode.setStatus("mandatory")


class _ScmOperatingMode_Type(Integer32):
    """Custom type scmOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("sleep", 3),
          ("standby", 2))
    )


_ScmOperatingMode_Type.__name__ = "Integer32"
_ScmOperatingMode_Object = MibScalar
scmOperatingMode = _ScmOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 14),
    _ScmOperatingMode_Type()
)
scmOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmOperatingMode.setStatus("mandatory")


class _ScmAliveTrapInterval_Type(Integer32):
    """Custom type scmAliveTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ScmAliveTrapInterval_Type.__name__ = "Integer32"
_ScmAliveTrapInterval_Object = MibScalar
scmAliveTrapInterval = _ScmAliveTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 15),
    _ScmAliveTrapInterval_Type()
)
scmAliveTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmAliveTrapInterval.setStatus("mandatory")


class _ScmRedundantTimeOut_Type(Integer32):
    """Custom type scmRedundantTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ScmRedundantTimeOut_Type.__name__ = "Integer32"
_ScmRedundantTimeOut_Object = MibScalar
scmRedundantTimeOut = _ScmRedundantTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 16),
    _ScmRedundantTimeOut_Type()
)
scmRedundantTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmRedundantTimeOut.setStatus("mandatory")


class _ScmTelnet_Type(Integer32):
    """Custom type scmTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ScmTelnet_Type.__name__ = "Integer32"
_ScmTelnet_Object = MibScalar
scmTelnet = _ScmTelnet_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 17),
    _ScmTelnet_Type()
)
scmTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmTelnet.setStatus("mandatory")


class _ScmTextAlarmTraps_Type(Integer32):
    """Custom type scmTextAlarmTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ScmTextAlarmTraps_Type.__name__ = "Integer32"
_ScmTextAlarmTraps_Object = MibScalar
scmTextAlarmTraps = _ScmTextAlarmTraps_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 2, 18),
    _ScmTextAlarmTraps_Type()
)
scmTextAlarmTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmTextAlarmTraps.setStatus("mandatory")
_ScmNode_ObjectIdentity = ObjectIdentity
scmNode = _ScmNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3)
)
_ScmNodeTable_Object = MibTable
scmNodeTable = _ScmNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2)
)
if mibBuilder.loadTexts:
    scmNodeTable.setStatus("mandatory")
_ScmNodeEntry_Object = MibTableRow
scmNodeEntry = _ScmNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1)
)
scmNodeEntry.setIndexNames(
    (0, "GDCSCM-MIB", "scmNodeIndex"),
)
if mibBuilder.loadTexts:
    scmNodeEntry.setStatus("mandatory")
_ScmNodeIndex_Type = SCinstance
_ScmNodeIndex_Object = MibTableColumn
scmNodeIndex = _ScmNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 1),
    _ScmNodeIndex_Type()
)
scmNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNodeIndex.setStatus("mandatory")


class _ScmNodeType_Type(Integer32):
    """Custom type scmNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72)
        )
    )
    namedValues = NamedValues(
        *(("datx2011", 4),
          ("dc610", 13),
          ("dc610NZ", 34),
          ("dc612", 14),
          ("dc621", 22),
          ("dc720G1", 10),
          ("dc720G2", 11),
          ("dc720g2rp", 27),
          ("dc721T1", 38),
          ("dc721T2", 39),
          ("dc721T2RP", 40),
          ("dc730D1", 8),
          ("dc730D2", 9),
          ("dc730d2rp", 28),
          ("dc731D1", 41),
          ("dc731D2", 42),
          ("dc731D2RP", 43),
          ("gt1020", 62),
          ("gt1030", 57),
          ("gt1030xr", 68),
          ("gt128", 54),
          ("gt128NZ", 55),
          ("gt1830", 70),
          ("gt2020", 63),
          ("gt2030", 58),
          ("hdsl700AG2", 49),
          ("hdsl700AG2NZ", 50),
          ("mp7001", 35),
          ("mp7002", 29),
          ("nms510", 16),
          ("nms520", 5),
          ("nms553", 25),
          ("notlocallymanaged", 47),
          ("ntu2m", 52),
          ("sc202", 65),
          ("sc5001", 2),
          ("sc5002", 33),
          ("sc5034", 17),
          ("sc5034A", 61),
          ("sc5090", 56),
          ("sc521", 32),
          ("sc521A", 66),
          ("sc5506", 71),
          ("sc5516", 72),
          ("sc5520", 3),
          ("sc553", 46),
          ("sc5553", 20),
          ("sc611", 21),
          ("sc613", 19),
          ("sc616", 12),
          ("sc700G2", 6),
          ("sc700G3", 7),
          ("sc700g2RP", 24),
          ("sc701T2", 36),
          ("sc701T2RP", 37),
          ("sc702G2", 15),
          ("sc710d2", 23),
          ("sc710d2rp", 26),
          ("sc711D2", 64),
          ("sc800T3", 59),
          ("scdualV34", 18),
          ("scm", 31),
          ("uas7022", 53),
          ("uas7616", 45),
          ("uas7616NZ", 30),
          ("uas7616TA", 44),
          ("uas7624", 48),
          ("uas7626", 51),
          ("uas7722", 60),
          ("uas7722xr", 67),
          ("uas780g2", 69),
          ("vf288", 1))
    )


_ScmNodeType_Type.__name__ = "Integer32"
_ScmNodeType_Object = MibTableColumn
scmNodeType = _ScmNodeType_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 2),
    _ScmNodeType_Type()
)
scmNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmNodeType.setStatus("mandatory")


class _ScmNodeConfigCs_Type(OctetString):
    """Custom type scmNodeConfigCs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ScmNodeConfigCs_Type.__name__ = "OctetString"
_ScmNodeConfigCs_Object = MibTableColumn
scmNodeConfigCs = _ScmNodeConfigCs_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 3),
    _ScmNodeConfigCs_Type()
)
scmNodeConfigCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNodeConfigCs.setStatus("mandatory")


class _ScmNodeStatus_Type(Integer32):
    """Custom type scmNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ScmNodeStatus_Type.__name__ = "Integer32"
_ScmNodeStatus_Object = MibTableColumn
scmNodeStatus = _ScmNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 4),
    _ScmNodeStatus_Type()
)
scmNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmNodeStatus.setStatus("mandatory")


class _ScmNodeAlarmScan_Type(Integer32):
    """Custom type scmNodeAlarmScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ScmNodeAlarmScan_Type.__name__ = "Integer32"
_ScmNodeAlarmScan_Object = MibTableColumn
scmNodeAlarmScan = _ScmNodeAlarmScan_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 5),
    _ScmNodeAlarmScan_Type()
)
scmNodeAlarmScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmNodeAlarmScan.setStatus("mandatory")


class _ScmNodeLevel_Type(Integer32):
    """Custom type scmNodeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ScmNodeLevel_Type.__name__ = "Integer32"
_ScmNodeLevel_Object = MibTableColumn
scmNodeLevel = _ScmNodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 6),
    _ScmNodeLevel_Type()
)
scmNodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmNodeLevel.setStatus("mandatory")


class _ScmNodeConfigChecksumStatus_Type(Integer32):
    """Custom type scmNodeConfigChecksumStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("correct", 1),
          ("incorrect", 2))
    )


_ScmNodeConfigChecksumStatus_Type.__name__ = "Integer32"
_ScmNodeConfigChecksumStatus_Object = MibTableColumn
scmNodeConfigChecksumStatus = _ScmNodeConfigChecksumStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 7),
    _ScmNodeConfigChecksumStatus_Type()
)
scmNodeConfigChecksumStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNodeConfigChecksumStatus.setStatus("mandatory")


class _ScmNodeCurrentAlarms_Type(OctetString):
    """Custom type scmNodeCurrentAlarms based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ScmNodeCurrentAlarms_Type.__name__ = "OctetString"
_ScmNodeCurrentAlarms_Object = MibTableColumn
scmNodeCurrentAlarms = _ScmNodeCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 8),
    _ScmNodeCurrentAlarms_Type()
)
scmNodeCurrentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNodeCurrentAlarms.setStatus("mandatory")


class _ScmNodeSerialNumber_Type(DisplayString):
    """Custom type scmNodeSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ScmNodeSerialNumber_Type.__name__ = "DisplayString"
_ScmNodeSerialNumber_Object = MibTableColumn
scmNodeSerialNumber = _ScmNodeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 9),
    _ScmNodeSerialNumber_Type()
)
scmNodeSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmNodeSerialNumber.setStatus("mandatory")


class _ScmNodeAdminStatus_Type(Integer32):
    """Custom type scmNodeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ScmNodeAdminStatus_Type.__name__ = "Integer32"
_ScmNodeAdminStatus_Object = MibTableColumn
scmNodeAdminStatus = _ScmNodeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 10),
    _ScmNodeAdminStatus_Type()
)
scmNodeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmNodeAdminStatus.setStatus("mandatory")


class _ScmNodeOperStatus_Type(Integer32):
    """Custom type scmNodeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ScmNodeOperStatus_Type.__name__ = "Integer32"
_ScmNodeOperStatus_Object = MibTableColumn
scmNodeOperStatus = _ScmNodeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 3, 2, 1, 11),
    _ScmNodeOperStatus_Type()
)
scmNodeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmNodeOperStatus.setStatus("mandatory")
_ScmShelf_ObjectIdentity = ObjectIdentity
scmShelf = _ScmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 4)
)
_ScmSlotTable_Object = MibTable
scmSlotTable = _ScmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    scmSlotTable.setStatus("mandatory")
_ScmSlotEntry_Object = MibTableRow
scmSlotEntry = _ScmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 4, 1, 1)
)
scmSlotEntry.setIndexNames(
    (0, "GDCSCM-MIB", "scmSlotNumber"),
)
if mibBuilder.loadTexts:
    scmSlotEntry.setStatus("mandatory")


class _ScmSlotNumber_Type(Integer32):
    """Custom type scmSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ScmSlotNumber_Type.__name__ = "Integer32"
_ScmSlotNumber_Object = MibTableColumn
scmSlotNumber = _ScmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 4, 1, 1, 1),
    _ScmSlotNumber_Type()
)
scmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmSlotNumber.setStatus("mandatory")


class _ScmSlotState_Type(Integer32):
    """Custom type scmSlotState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeerrorstate", 3),
          ("activestate", 1),
          ("inactivestate", 2))
    )


_ScmSlotState_Type.__name__ = "Integer32"
_ScmSlotState_Object = MibTableColumn
scmSlotState = _ScmSlotState_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 4, 1, 1, 2),
    _ScmSlotState_Type()
)
scmSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmSlotState.setStatus("mandatory")
_ScmAlmTrap_ObjectIdentity = ObjectIdentity
scmAlmTrap = _ScmAlmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 5)
)
_ScmRedundancy_ObjectIdentity = ObjectIdentity
scmRedundancy = _ScmRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 6)
)
_ScmRedundancyTable_Object = MibTable
scmRedundancyTable = _ScmRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 6, 2)
)
if mibBuilder.loadTexts:
    scmRedundancyTable.setStatus("mandatory")
_ScmRedundancyEntry_Object = MibTableRow
scmRedundancyEntry = _ScmRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 6, 2, 1)
)
scmRedundancyEntry.setIndexNames(
    (0, "GDCSCM-MIB", "scmRedundancyIndex"),
)
if mibBuilder.loadTexts:
    scmRedundancyEntry.setStatus("mandatory")
_ScmRedundancyIndex_Type = SCinstance
_ScmRedundancyIndex_Object = MibTableColumn
scmRedundancyIndex = _ScmRedundancyIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 6, 2, 1, 1),
    _ScmRedundancyIndex_Type()
)
scmRedundancyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmRedundancyIndex.setStatus("mandatory")
_ScmEtherIPAddress_Type = IpAddress
_ScmEtherIPAddress_Object = MibTableColumn
scmEtherIPAddress = _ScmEtherIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 6, 2, 1, 2),
    _ScmEtherIPAddress_Type()
)
scmEtherIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmEtherIPAddress.setStatus("mandatory")
_ScmPPPIPAddress_Type = IpAddress
_ScmPPPIPAddress_Object = MibTableColumn
scmPPPIPAddress = _ScmPPPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 6, 2, 1, 3),
    _ScmPPPIPAddress_Type()
)
scmPPPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmPPPIPAddress.setStatus("mandatory")


class _ScmRedundancySwitch_Type(Integer32):
    """Custom type scmRedundancySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("redundant", 1))
    )


_ScmRedundancySwitch_Type.__name__ = "Integer32"
_ScmRedundancySwitch_Object = MibTableColumn
scmRedundancySwitch = _ScmRedundancySwitch_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 6, 2, 1, 4),
    _ScmRedundancySwitch_Type()
)
scmRedundancySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmRedundancySwitch.setStatus("mandatory")


class _ScmAlarmText_Type(DisplayString):
    """Custom type scmAlarmText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_ScmAlarmText_Type.__name__ = "DisplayString"
_ScmAlarmText_Object = MibScalar
scmAlarmText = _ScmAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 7),
    _ScmAlarmText_Type()
)
scmAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmAlarmText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

scmAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 0, 1)
)
scmAlarmTrap.setObjects(
    ("GDCSCM-MIB", "scmNodeCurrentAlarms")
)
if mibBuilder.loadTexts:
    scmAlarmTrap.setStatus(
        ""
    )

scmExpressPollTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 0, 2)
)
scmExpressPollTrap.setObjects(
    ("GDCSCM-MIB", "scmSlotState")
)
if mibBuilder.loadTexts:
    scmExpressPollTrap.setStatus(
        ""
    )

scmPowerSupplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 0, 3)
)
scmPowerSupplyTrap.setObjects(
    ("GDCSCM-MIB", "scmPowerAvail")
)
if mibBuilder.loadTexts:
    scmPowerSupplyTrap.setStatus(
        ""
    )

scmAliveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 0, 4)
)
scmAliveTrap.setObjects(
      *(("GDCSCM-MIB", "scmOperatingMode"),
        ("GDCSCM-MIB", "scmAliveTrapInterval"))
)
if mibBuilder.loadTexts:
    scmAliveTrap.setStatus(
        ""
    )

scmConfigChksumTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 0, 5)
)
scmConfigChksumTrap.setObjects(
    ("GDCSCM-MIB", "scmNodeIndex")
)
if mibBuilder.loadTexts:
    scmConfigChksumTrap.setStatus(
        ""
    )

scmAlarmTextTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 6, 0, 6)
)
scmAlarmTextTrap.setObjects(
    ("GDCSCM-MIB", "scmAlarmText")
)
if mibBuilder.loadTexts:
    scmAlarmTextTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCSCM-MIB",
    **{"gdc": gdc,
       "sc": sc,
       "scmSystem": scmSystem,
       "scmAlarmTrap": scmAlarmTrap,
       "scmExpressPollTrap": scmExpressPollTrap,
       "scmPowerSupplyTrap": scmPowerSupplyTrap,
       "scmAliveTrap": scmAliveTrap,
       "scmConfigChksumTrap": scmConfigChksumTrap,
       "scmAlarmTextTrap": scmAlarmTextTrap,
       "scmVersion": scmVersion,
       "scmMIBVersion": scmMIBVersion,
       "scmBootVersion": scmBootVersion,
       "scmApplVersion": scmApplVersion,
       "scmMaster": scmMaster,
       "scmMasterTimeout": scmMasterTimeout,
       "scmAlarmScan": scmAlarmScan,
       "scmTime": scmTime,
       "scmDate": scmDate,
       "scmRedundant": scmRedundant,
       "scmShelfNumber": scmShelfNumber,
       "scmReset": scmReset,
       "scmPowerAvail": scmPowerAvail,
       "scmDefaultConfig": scmDefaultConfig,
       "scmPowerConsum": scmPowerConsum,
       "scmCannedConfig": scmCannedConfig,
       "scmSetNetworkElementRealTime": scmSetNetworkElementRealTime,
       "scmDownLoadCode": scmDownLoadCode,
       "scmOperatingMode": scmOperatingMode,
       "scmAliveTrapInterval": scmAliveTrapInterval,
       "scmRedundantTimeOut": scmRedundantTimeOut,
       "scmTelnet": scmTelnet,
       "scmTextAlarmTraps": scmTextAlarmTraps,
       "scmNode": scmNode,
       "scmNodeTable": scmNodeTable,
       "scmNodeEntry": scmNodeEntry,
       "scmNodeIndex": scmNodeIndex,
       "scmNodeType": scmNodeType,
       "scmNodeConfigCs": scmNodeConfigCs,
       "scmNodeStatus": scmNodeStatus,
       "scmNodeAlarmScan": scmNodeAlarmScan,
       "scmNodeLevel": scmNodeLevel,
       "scmNodeConfigChecksumStatus": scmNodeConfigChecksumStatus,
       "scmNodeCurrentAlarms": scmNodeCurrentAlarms,
       "scmNodeSerialNumber": scmNodeSerialNumber,
       "scmNodeAdminStatus": scmNodeAdminStatus,
       "scmNodeOperStatus": scmNodeOperStatus,
       "scmShelf": scmShelf,
       "scmSlotTable": scmSlotTable,
       "scmSlotEntry": scmSlotEntry,
       "scmSlotNumber": scmSlotNumber,
       "scmSlotState": scmSlotState,
       "scmAlmTrap": scmAlmTrap,
       "scmRedundancy": scmRedundancy,
       "scmRedundancyTable": scmRedundancyTable,
       "scmRedundancyEntry": scmRedundancyEntry,
       "scmRedundancyIndex": scmRedundancyIndex,
       "scmEtherIPAddress": scmEtherIPAddress,
       "scmPPPIPAddress": scmPPPIPAddress,
       "scmRedundancySwitch": scmRedundancySwitch,
       "scmAlarmText": scmAlarmText}
)
