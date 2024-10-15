# SNMP MIB module (UB-MIB-SUPRV) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UB-MIB-SUPRV
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PhysAddress,) = mibBuilder.importSymbols(
    "RFC1213",
    "PhysAddress")

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

_UbNode_ObjectIdentity = ObjectIdentity
ubNode = _UbNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75)
)
_UbEquip_ObjectIdentity = ObjectIdentity
ubEquip = _UbEquip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1)
)
_UbSuprv_ObjectIdentity = ObjectIdentity
ubSuprv = _UbSuprv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 1)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1)
)
_HubId_Type = PhysAddress
_HubId_Object = MibScalar
hubId = _HubId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 1),
    _HubId_Type()
)
hubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubId.setStatus("mandatory")


class _HubType_Type(Integer32):
    """Custom type hubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("elevenSlot-ASE7000", 11),
          ("fiveSlot-ASE3000", 5),
          ("oneSlot-ASE1000", 1),
          ("twoSlot-ASE2000", 3))
    )


_HubType_Type.__name__ = "Integer32"
_HubType_Object = MibScalar
hubType = _HubType_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 2),
    _HubType_Type()
)
hubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubType.setStatus("mandatory")
_HubName_Type = DisplayString
_HubName_Object = MibScalar
hubName = _HubName_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 3),
    _HubName_Type()
)
hubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubName.setStatus("mandatory")
_HubSerNumber_Type = DisplayString
_HubSerNumber_Object = MibScalar
hubSerNumber = _HubSerNumber_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 4),
    _HubSerNumber_Type()
)
hubSerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSerNumber.setStatus("mandatory")
_HubIPAddr_Type = IpAddress
_HubIPAddr_Object = MibScalar
hubIPAddr = _HubIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 5),
    _HubIPAddr_Type()
)
hubIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIPAddr.setStatus("mandatory")


class _HubPowerSupplyStatus_Type(Integer32):
    """Custom type hubPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acPowerAbnormal", 3),
          ("highTemp", 4),
          ("normalPower", 2),
          ("notApplicable", 1),
          ("onePsModuleFailed", 5))
    )


_HubPowerSupplyStatus_Type.__name__ = "Integer32"
_HubPowerSupplyStatus_Object = MibScalar
hubPowerSupplyStatus = _HubPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 6),
    _HubPowerSupplyStatus_Type()
)
hubPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPowerSupplyStatus.setStatus("mandatory")


class _HubTempStatus_Type(Integer32):
    """Custom type hubTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abnormalTemperature", 2),
          ("normalTemperature", 3),
          ("notApplicable", 1))
    )


_HubTempStatus_Type.__name__ = "Integer32"
_HubTempStatus_Object = MibScalar
hubTempStatus = _HubTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 7),
    _HubTempStatus_Type()
)
hubTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubTempStatus.setStatus("mandatory")


class _HubPollTime_Type(Integer32):
    """Custom type hubPollTime based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("fiveSecs", 12),
          ("fourPt5secs", 11),
          ("fourSecs", 10),
          ("no-polling-requested", 2),
          ("notApplicable", 1),
          ("oneHalfSec", 3),
          ("onePt5secs", 5),
          ("oneSec", 4),
          ("threePt5secs", 9),
          ("threeSecs", 8),
          ("twoPt5secs", 7),
          ("twoSecs", 6))
    )


_HubPollTime_Type.__name__ = "Integer32"
_HubPollTime_Object = MibScalar
hubPollTime = _HubPollTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 8),
    _HubPollTime_Type()
)
hubPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPollTime.setStatus("mandatory")


class _HubResetAction_Type(Integer32):
    """Custom type hubResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("forceLoad", 5),
          ("not-requested", 2),
          ("resetAllCards", 3))
    )


_HubResetAction_Type.__name__ = "Integer32"
_HubResetAction_Object = MibScalar
hubResetAction = _HubResetAction_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 9),
    _HubResetAction_Type()
)
hubResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubResetAction.setStatus("mandatory")


class _HubAFS_Type(Integer32):
    """Custom type hubAFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abnormalAirflow", 3),
          ("normalAirflow", 2),
          ("notApplicable", 1))
    )


_HubAFS_Type.__name__ = "Integer32"
_HubAFS_Object = MibScalar
hubAFS = _HubAFS_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 1, 10),
    _HubAFS_Type()
)
hubAFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAFS.setStatus("mandatory")
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2)
)


class _EnsupStaticNetConfig_Type(Integer32):
    """Custom type ensupStaticNetConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("netAndSupDirect", 2),
          ("netOnly", 4),
          ("supElseBridge", 5),
          ("supOnly", 3))
    )


_EnsupStaticNetConfig_Type.__name__ = "Integer32"
_EnsupStaticNetConfig_Object = MibScalar
ensupStaticNetConfig = _EnsupStaticNetConfig_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 1),
    _EnsupStaticNetConfig_Type()
)
ensupStaticNetConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ensupStaticNetConfig.setStatus("mandatory")


class _EnsupDynamicNetStatus_Type(Integer32):
    """Custom type ensupDynamicNetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bridgeOnly", 5),
          ("netAndSupDirect", 2),
          ("netOnly", 4),
          ("netOrSupLoopback", 6),
          ("notApplicable", 1),
          ("supOnly", 3))
    )


_EnsupDynamicNetStatus_Type.__name__ = "Integer32"
_EnsupDynamicNetStatus_Object = MibScalar
ensupDynamicNetStatus = _EnsupDynamicNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 2),
    _EnsupDynamicNetStatus_Type()
)
ensupDynamicNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ensupDynamicNetStatus.setStatus("mandatory")


class _EnsupNetBridgeSlot_Type(Integer32):
    """Custom type ensupNetBridgeSlot based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("slot-1", 2),
          ("slot-10", 11),
          ("slot-11", 12),
          ("slot-2", 3),
          ("slot-3", 4),
          ("slot-4", 5),
          ("slot-5", 6),
          ("slot-6", 7),
          ("slot-7", 8),
          ("slot-8", 9),
          ("slot-9", 10))
    )


_EnsupNetBridgeSlot_Type.__name__ = "Integer32"
_EnsupNetBridgeSlot_Object = MibScalar
ensupNetBridgeSlot = _EnsupNetBridgeSlot_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 3),
    _EnsupNetBridgeSlot_Type()
)
ensupNetBridgeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ensupNetBridgeSlot.setStatus("mandatory")
_EnsupCarrierCounter_Type = Counter32
_EnsupCarrierCounter_Object = MibScalar
ensupCarrierCounter = _EnsupCarrierCounter_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 4),
    _EnsupCarrierCounter_Type()
)
ensupCarrierCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ensupCarrierCounter.setStatus("mandatory")
_EnsupNetUtilization_Type = DisplayString
_EnsupNetUtilization_Object = MibScalar
ensupNetUtilization = _EnsupNetUtilization_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 5),
    _EnsupNetUtilization_Type()
)
ensupNetUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ensupNetUtilization.setStatus("mandatory")
_EnsupNetUtilThreshold_Type = Integer32
_EnsupNetUtilThreshold_Object = MibScalar
ensupNetUtilThreshold = _EnsupNetUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 6),
    _EnsupNetUtilThreshold_Type()
)
ensupNetUtilThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ensupNetUtilThreshold.setStatus("mandatory")
_A1gTable_Object = MibTable
a1gTable = _A1gTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    a1gTable.setStatus("mandatory")
_A1gEntry_Object = MibTableRow
a1gEntry = _A1gEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1)
)
a1gEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "a1gSlotId"),
)
if mibBuilder.loadTexts:
    a1gEntry.setStatus("mandatory")
_A1gSlotId_Type = Integer32
_A1gSlotId_Object = MibTableColumn
a1gSlotId = _A1gSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 1),
    _A1gSlotId_Type()
)
a1gSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gSlotId.setStatus("mandatory")
_A1gPorts_Type = Integer32
_A1gPorts_Object = MibTableColumn
a1gPorts = _A1gPorts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 2),
    _A1gPorts_Type()
)
a1gPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gPorts.setStatus("mandatory")


class _A1gOperStatus_Type(Integer32):
    """Custom type a1gOperStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("active", 15),
          ("cbLoading", 9),
          ("debugMode", 4),
          ("inactive", 14),
          ("initializing", 2),
          ("moduleFault", 6),
          ("netBooting", 7),
          ("netLoading", 8),
          ("notApplicable", 1),
          ("notResponding", 16),
          ("onlineDiagnostics", 5),
          ("powerOnDiagnostics", 3),
          ("reset", 13),
          ("softwareDisabled", 12),
          ("standby", 11),
          ("up", 10))
    )


_A1gOperStatus_Type.__name__ = "Integer32"
_A1gOperStatus_Object = MibTableColumn
a1gOperStatus = _A1gOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 3),
    _A1gOperStatus_Type()
)
a1gOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gOperStatus.setStatus("mandatory")


class _A1gTempStatus_Type(Integer32):
    """Custom type a1gTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abnormalTemperature", 2),
          ("normalTemperature", 3),
          ("notApplicable", 1))
    )


_A1gTempStatus_Type.__name__ = "Integer32"
_A1gTempStatus_Object = MibTableColumn
a1gTempStatus = _A1gTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 4),
    _A1gTempStatus_Type()
)
a1gTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gTempStatus.setStatus("mandatory")


class _A1gEthBusAdmAction_Type(Integer32):
    """Custom type a1gEthBusAdmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 3),
          ("notApplicable", 1),
          ("unlock", 2))
    )


_A1gEthBusAdmAction_Type.__name__ = "Integer32"
_A1gEthBusAdmAction_Object = MibTableColumn
a1gEthBusAdmAction = _A1gEthBusAdmAction_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 5),
    _A1gEthBusAdmAction_Type()
)
a1gEthBusAdmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1gEthBusAdmAction.setStatus("mandatory")


class _A1gEthBusMgmtStatus_Type(Integer32):
    """Custom type a1gEthBusMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autosegmented", 5),
          ("hardwareFault", 6),
          ("locked", 3),
          ("lockedByJumper", 7),
          ("notApplicable", 1),
          ("notResponding", 4),
          ("unlocked", 2))
    )


_A1gEthBusMgmtStatus_Type.__name__ = "Integer32"
_A1gEthBusMgmtStatus_Object = MibTableColumn
a1gEthBusMgmtStatus = _A1gEthBusMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 6),
    _A1gEthBusMgmtStatus_Type()
)
a1gEthBusMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gEthBusMgmtStatus.setStatus("mandatory")


class _A1gNetMgmtBusOperStatus_Type(Integer32):
    """Custom type a1gNetMgmtBusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("notApplicable", 1),
          ("notResponding", 3))
    )


_A1gNetMgmtBusOperStatus_Type.__name__ = "Integer32"
_A1gNetMgmtBusOperStatus_Object = MibTableColumn
a1gNetMgmtBusOperStatus = _A1gNetMgmtBusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 7),
    _A1gNetMgmtBusOperStatus_Type()
)
a1gNetMgmtBusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gNetMgmtBusOperStatus.setStatus("mandatory")


class _A1gProductType_Type(Integer32):
    """Custom type a1gProductType based on Integer32"""
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
              46)
        )
    )
    namedValues = NamedValues(
        *(("async-100", 15),
          ("ausup-700s", 31),
          ("brnet-510", 9),
          ("brnet-560", 8),
          ("brsuprv-710", 5),
          ("brsuprv-760", 4),
          ("eBrR-5330", 45),
          ("eTBrR-5530", 44),
          ("ecm-300", 11),
          ("ecm-310", 14),
          ("ecm-320-1", 26),
          ("ecm-320-2", 27),
          ("fBrR-5361", 43),
          ("fec-800", 13),
          ("fosup-700s", 34),
          ("lebr-5300", 18),
          ("lebr-5340", 25),
          ("lfebr-5360", 24),
          ("lftbr-5560", 23),
          ("ltebr-5500", 19),
          ("lttbr-5550", 20),
          ("m3270", 17),
          ("mtm-7100", 16),
          ("net-500", 6),
          ("net-500s", 36),
          ("net-550", 7),
          ("notApplicable", 1),
          ("rr-8300", 37),
          ("rr-8310", 38),
          ("rr-8320", 39),
          ("rr-8500", 40),
          ("rr-8510", 41),
          ("rr-8520", 42),
          ("suprv-700", 3),
          ("suprv-700s", 35),
          ("suprv-780", 2),
          ("suprv-790", 30),
          ("suprv-790s16", 33),
          ("suprv-790s4", 46),
          ("t1ebr-6300", 21),
          ("t1tbr-6500", 22),
          ("tec-900", 12),
          ("tpsup-700s", 32),
          ("trc-400", 10),
          ("trc-410-1", 28),
          ("trc-410-2", 29))
    )


_A1gProductType_Type.__name__ = "Integer32"
_A1gProductType_Object = MibTableColumn
a1gProductType = _A1gProductType_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 8),
    _A1gProductType_Type()
)
a1gProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gProductType.setStatus("mandatory")
_A1gUpTime_Type = TimeTicks
_A1gUpTime_Object = MibTableColumn
a1gUpTime = _A1gUpTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 9),
    _A1gUpTime_Type()
)
a1gUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gUpTime.setStatus("mandatory")
_A1gResets_Type = Counter32
_A1gResets_Object = MibTableColumn
a1gResets = _A1gResets_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 10),
    _A1gResets_Type()
)
a1gResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1gResets.setStatus("mandatory")


class _A1gResetAction_Type(Integer32):
    """Custom type a1gResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enterDebugMode", 2),
          ("noResetRequested", 1),
          ("podThenDebug", 3),
          ("podThenNetdownload", 4))
    )


_A1gResetAction_Type.__name__ = "Integer32"
_A1gResetAction_Object = MibTableColumn
a1gResetAction = _A1gResetAction_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 7, 1, 11),
    _A1gResetAction_Type()
)
a1gResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1gResetAction.setStatus("mandatory")
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    configTable.setStatus("mandatory")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 8, 1)
)
configEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "configSlotId"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("mandatory")
_ConfigSlotId_Type = Integer32
_ConfigSlotId_Object = MibTableColumn
configSlotId = _ConfigSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 8, 1, 1),
    _ConfigSlotId_Type()
)
configSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configSlotId.setStatus("mandatory")


class _ConfigFaultActionType_Type(Integer32):
    """Custom type configFaultActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noSupvAction", 4),
          ("reset", 2),
          ("stayInReset", 3))
    )


_ConfigFaultActionType_Type.__name__ = "Integer32"
_ConfigFaultActionType_Object = MibTableColumn
configFaultActionType = _ConfigFaultActionType_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 8, 1, 2),
    _ConfigFaultActionType_Type()
)
configFaultActionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFaultActionType.setStatus("mandatory")
_ConfigRetries_Type = Integer32
_ConfigRetries_Object = MibTableColumn
configRetries = _ConfigRetries_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 8, 1, 3),
    _ConfigRetries_Type()
)
configRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRetries.setStatus("mandatory")


class _ConfigPowerUpMode_Type(Integer32):
    """Custom type configPowerUpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("debug", 2),
          ("notApplicable", 1),
          ("pod-CopyDefaults-Run", 6),
          ("pod-CopyUserMem-Run", 5),
          ("podThenDebug", 3),
          ("podThenNetdownload", 4))
    )


_ConfigPowerUpMode_Type.__name__ = "Integer32"
_ConfigPowerUpMode_Object = MibTableColumn
configPowerUpMode = _ConfigPowerUpMode_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 8, 1, 4),
    _ConfigPowerUpMode_Type()
)
configPowerUpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPowerUpMode.setStatus("mandatory")
_A1imTable_Object = MibTable
a1imTable = _A1imTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    a1imTable.setStatus("mandatory")
_A1imEntry_Object = MibTableRow
a1imEntry = _A1imEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9, 1)
)
a1imEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "a1imSlotId"),
)
if mibBuilder.loadTexts:
    a1imEntry.setStatus("mandatory")
_A1imSlotId_Type = Integer32
_A1imSlotId_Object = MibTableColumn
a1imSlotId = _A1imSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9, 1, 1),
    _A1imSlotId_Type()
)
a1imSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1imSlotId.setStatus("mandatory")
_A1imMACAddr_Type = PhysAddress
_A1imMACAddr_Object = MibTableColumn
a1imMACAddr = _A1imMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9, 1, 2),
    _A1imMACAddr_Type()
)
a1imMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1imMACAddr.setStatus("mandatory")
_A1imPodDiagnosticMsg_Type = DisplayString
_A1imPodDiagnosticMsg_Object = MibTableColumn
a1imPodDiagnosticMsg = _A1imPodDiagnosticMsg_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9, 1, 3),
    _A1imPodDiagnosticMsg_Type()
)
a1imPodDiagnosticMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1imPodDiagnosticMsg.setStatus("mandatory")


class _A1imModuleFault_Type(Integer32):
    """Custom type a1imModuleFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("diagosticError", 5),
          ("networkError", 4),
          ("noFault", 2),
          ("notApplicable", 1),
          ("operationalError", 6),
          ("parityError", 3))
    )


_A1imModuleFault_Type.__name__ = "Integer32"
_A1imModuleFault_Object = MibTableColumn
a1imModuleFault = _A1imModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9, 1, 4),
    _A1imModuleFault_Type()
)
a1imModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1imModuleFault.setStatus("mandatory")


class _A1imHaltReason_Type(Integer32):
    """Custom type a1imHaltReason based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("arithmeticOverflow", 10),
          ("badBreakpoint", 9),
          ("badSingleStep", 7),
          ("breakpoint", 5),
          ("dma-0Interrupt", 16),
          ("dma-1Interrupt", 17),
          ("errorDivideByZero", 6),
          ("exceededArrayBounds", 11),
          ("halted", 3),
          ("int-0Interrupt", 18),
          ("int-1Interrupt", 19),
          ("int-2Interrupt", 20),
          ("invalidEscapeOpcode", 13),
          ("invalidOpcode", 12),
          ("nonMaskableInterrupt", 8),
          ("notAvailable", 1),
          ("parityError", 23),
          ("reservedInterrupt", 15),
          ("singleStepped", 4),
          ("timer-0Interrupt", 14),
          ("timer-1Interrupt", 21),
          ("timer-2Interrupt", 22),
          ("unexpectedSoftInterrupt", 2),
          ("watchDogTimeout", 24))
    )


_A1imHaltReason_Type.__name__ = "Integer32"
_A1imHaltReason_Object = MibTableColumn
a1imHaltReason = _A1imHaltReason_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9, 1, 5),
    _A1imHaltReason_Type()
)
a1imHaltReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1imHaltReason.setStatus("mandatory")
_A1imDebugRegisters_Type = OctetString
_A1imDebugRegisters_Object = MibTableColumn
a1imDebugRegisters = _A1imDebugRegisters_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 9, 1, 6),
    _A1imDebugRegisters_Type()
)
a1imDebugRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1imDebugRegisters.setStatus("mandatory")
_TplTable_Object = MibTable
tplTable = _TplTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    tplTable.setStatus("mandatory")
_TplEntry_Object = MibTableRow
tplEntry = _TplEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 10, 1)
)
tplEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "tplSlotId"),
)
if mibBuilder.loadTexts:
    tplEntry.setStatus("mandatory")
_TplSlotId_Type = Integer32
_TplSlotId_Object = MibTableColumn
tplSlotId = _TplSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 10, 1, 1),
    _TplSlotId_Type()
)
tplSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tplSlotId.setStatus("mandatory")
_TplIPAddress_Type = IpAddress
_TplIPAddress_Object = MibTableColumn
tplIPAddress = _TplIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 10, 1, 2),
    _TplIPAddress_Type()
)
tplIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tplIPAddress.setStatus("mandatory")
_TplNiuName_Type = DisplayString
_TplNiuName_Object = MibTableColumn
tplNiuName = _TplNiuName_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 10, 1, 3),
    _TplNiuName_Type()
)
tplNiuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tplNiuName.setStatus("mandatory")


class _TplProtocolType_Type(Integer32):
    """Custom type tplProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("any", 5),
          ("iso", 4),
          ("tcpIp", 3),
          ("unknown", 1),
          ("xns", 2))
    )


_TplProtocolType_Type.__name__ = "Integer32"
_TplProtocolType_Object = MibTableColumn
tplProtocolType = _TplProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 10, 1, 4),
    _TplProtocolType_Type()
)
tplProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tplProtocolType.setStatus("mandatory")


class _TplSuprvPollStatus_Type(Integer32):
    """Custom type tplSuprvPollStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cannotPoll", 5),
          ("notApplicable", 1),
          ("notResponding", 3),
          ("pollingSuspended", 4),
          ("responding", 2))
    )


_TplSuprvPollStatus_Type.__name__ = "Integer32"
_TplSuprvPollStatus_Object = MibTableColumn
tplSuprvPollStatus = _TplSuprvPollStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 10, 1, 5),
    _TplSuprvPollStatus_Type()
)
tplSuprvPollStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tplSuprvPollStatus.setStatus("mandatory")
_ImenEthBusTable_Object = MibTable
imenEthBusTable = _ImenEthBusTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    imenEthBusTable.setStatus("mandatory")
_ImenEthBusEntry_Object = MibTableRow
imenEthBusEntry = _ImenEthBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 11, 1)
)
imenEthBusEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "imenSlotId"),
)
if mibBuilder.loadTexts:
    imenEthBusEntry.setStatus("mandatory")
_ImenSlotId_Type = Integer32
_ImenSlotId_Object = MibTableColumn
imenSlotId = _ImenSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 11, 1, 1),
    _ImenSlotId_Type()
)
imenSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imenSlotId.setStatus("mandatory")
_ImenTransmitPkts_Type = Counter32
_ImenTransmitPkts_Object = MibTableColumn
imenTransmitPkts = _ImenTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 11, 1, 2),
    _ImenTransmitPkts_Type()
)
imenTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imenTransmitPkts.setStatus("mandatory")
_ImenReceivePkts_Type = Counter32
_ImenReceivePkts_Object = MibTableColumn
imenReceivePkts = _ImenReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 11, 1, 3),
    _ImenReceivePkts_Type()
)
imenReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imenReceivePkts.setStatus("mandatory")
_ImenCRCErrors_Type = Counter32
_ImenCRCErrors_Object = MibTableColumn
imenCRCErrors = _ImenCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 11, 1, 4),
    _ImenCRCErrors_Type()
)
imenCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imenCRCErrors.setStatus("mandatory")
_ImenCollisions_Type = Counter32
_ImenCollisions_Object = MibTableColumn
imenCollisions = _ImenCollisions_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 11, 1, 5),
    _ImenCollisions_Type()
)
imenCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imenCollisions.setStatus("mandatory")
_BrdgTable_Object = MibTable
brdgTable = _BrdgTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    brdgTable.setStatus("mandatory")
_BrdgEntry_Object = MibTableRow
brdgEntry = _BrdgEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 12, 1)
)
brdgEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "brdgSlotId"),
    (0, "UB-MIB-SUPRV", "brdgIfId"),
)
if mibBuilder.loadTexts:
    brdgEntry.setStatus("mandatory")
_BrdgSlotId_Type = Integer32
_BrdgSlotId_Object = MibTableColumn
brdgSlotId = _BrdgSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 12, 1, 1),
    _BrdgSlotId_Type()
)
brdgSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdgSlotId.setStatus("mandatory")
_BrdgIfId_Type = Integer32
_BrdgIfId_Object = MibTableColumn
brdgIfId = _BrdgIfId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 12, 1, 2),
    _BrdgIfId_Type()
)
brdgIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdgIfId.setStatus("mandatory")


class _BrdgIfType_Type(Integer32):
    """Custom type brdgIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("baseband802-3", 3),
          ("broadband802-3", 7),
          ("ethernetBus", 2),
          ("fddi", 5),
          ("fourMbps802-5", 4),
          ("sixteenMbps802-5", 8),
          ("t1", 6))
    )


_BrdgIfType_Type.__name__ = "Integer32"
_BrdgIfType_Object = MibTableColumn
brdgIfType = _BrdgIfType_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 12, 1, 3),
    _BrdgIfType_Type()
)
brdgIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdgIfType.setStatus("mandatory")


class _BrdgIfFault_Type(Integer32):
    """Custom type brdgIfFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkLoopbackTest", 4),
          ("linkUp", 3),
          ("notApplicable", 1))
    )


_BrdgIfFault_Type.__name__ = "Integer32"
_BrdgIfFault_Object = MibTableColumn
brdgIfFault = _BrdgIfFault_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 12, 1, 4),
    _BrdgIfFault_Type()
)
brdgIfFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdgIfFault.setStatus("mandatory")
_BrdgIfMACAddr_Type = PhysAddress
_BrdgIfMACAddr_Object = MibTableColumn
brdgIfMACAddr = _BrdgIfMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 12, 1, 5),
    _BrdgIfMACAddr_Type()
)
brdgIfMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdgIfMACAddr.setStatus("mandatory")
_EcTable_Object = MibTable
ecTable = _EcTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    ecTable.setStatus("mandatory")
_EcEntry_Object = MibTableRow
ecEntry = _EcEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 13, 1)
)
ecEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "ecSlotId"),
)
if mibBuilder.loadTexts:
    ecEntry.setStatus("mandatory")
_EcSlotId_Type = Integer32
_EcSlotId_Object = MibTableColumn
ecSlotId = _EcSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 13, 1, 1),
    _EcSlotId_Type()
)
ecSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecSlotId.setStatus("mandatory")
_EcCarrierCounter_Type = Counter32
_EcCarrierCounter_Object = MibTableColumn
ecCarrierCounter = _EcCarrierCounter_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 13, 1, 2),
    _EcCarrierCounter_Type()
)
ecCarrierCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecCarrierCounter.setStatus("mandatory")


class _EcFanStatus_Type(Integer32):
    """Custom type ecFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abnormalFan", 3),
          ("normalFan", 2),
          ("notApplicable", 1))
    )


_EcFanStatus_Type.__name__ = "Integer32"
_EcFanStatus_Object = MibTableColumn
ecFanStatus = _EcFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 13, 1, 3),
    _EcFanStatus_Type()
)
ecFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecFanStatus.setStatus("mandatory")
_NetTable_Object = MibTable
netTable = _NetTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    netTable.setStatus("mandatory")
_NetEntry_Object = MibTableRow
netEntry = _NetEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 14, 1)
)
netEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "netSlotId"),
)
if mibBuilder.loadTexts:
    netEntry.setStatus("mandatory")
_NetSlotId_Type = Integer32
_NetSlotId_Object = MibTableColumn
netSlotId = _NetSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 14, 1, 1),
    _NetSlotId_Type()
)
netSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSlotId.setStatus("mandatory")


class _NetBackboneType_Type(Integer32):
    """Custom type netBackboneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("baseband", 2),
          ("broadband", 3))
    )


_NetBackboneType_Type.__name__ = "Integer32"
_NetBackboneType_Object = MibTableColumn
netBackboneType = _NetBackboneType_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 14, 1, 2),
    _NetBackboneType_Type()
)
netBackboneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBackboneType.setStatus("mandatory")


class _NetFault_Type(Integer32):
    """Custom type netFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auiBad", 3),
          ("bufferedRepeaterBad", 5),
          ("internalFault", 2),
          ("mdiBad", 4),
          ("normal", 6),
          ("notApplicable", 1))
    )


_NetFault_Type.__name__ = "Integer32"
_NetFault_Object = MibTableColumn
netFault = _NetFault_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 14, 1, 3),
    _NetFault_Type()
)
netFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netFault.setStatus("mandatory")


class _NetBackboneStatus_Type(Integer32):
    """Custom type netBackboneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bridgeOnly", 5),
          ("loopback", 4),
          ("netAndSupDirect", 3),
          ("netOnly", 2),
          ("notApplicable", 1),
          ("standby", 6))
    )


_NetBackboneStatus_Type.__name__ = "Integer32"
_NetBackboneStatus_Object = MibTableColumn
netBackboneStatus = _NetBackboneStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 14, 1, 4),
    _NetBackboneStatus_Type()
)
netBackboneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBackboneStatus.setStatus("mandatory")
_BrnTable_Object = MibTable
brnTable = _BrnTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    brnTable.setStatus("mandatory")
_BrnEntry_Object = MibTableRow
brnEntry = _BrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1)
)
brnEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "brnSlotId"),
    (0, "UB-MIB-SUPRV", "brnIfId"),
)
if mibBuilder.loadTexts:
    brnEntry.setStatus("mandatory")
_BrnSlotId_Type = Integer32
_BrnSlotId_Object = MibTableColumn
brnSlotId = _BrnSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 1),
    _BrnSlotId_Type()
)
brnSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnSlotId.setStatus("mandatory")


class _BrnIfId_Type(Integer32):
    """Custom type brnIfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("if-1", 1),
          ("if-ETHBUS", 2))
    )


_BrnIfId_Type.__name__ = "Integer32"
_BrnIfId_Object = MibTableColumn
brnIfId = _BrnIfId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 2),
    _BrnIfId_Type()
)
brnIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnIfId.setStatus("mandatory")


class _BrnIfEthDLCStatus_Type(Integer32):
    """Custom type brnIfEthDLCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("collision", 5),
          ("collisions-16", 4),
          ("normal", 2),
          ("notApplicable", 1),
          ("parityError", 3),
          ("underflow", 6))
    )


_BrnIfEthDLCStatus_Type.__name__ = "Integer32"
_BrnIfEthDLCStatus_Object = MibTableColumn
brnIfEthDLCStatus = _BrnIfEthDLCStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 3),
    _BrnIfEthDLCStatus_Type()
)
brnIfEthDLCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnIfEthDLCStatus.setStatus("mandatory")
_BrnCarrierCounter_Type = Counter32
_BrnCarrierCounter_Object = MibTableColumn
brnCarrierCounter = _BrnCarrierCounter_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 4),
    _BrnCarrierCounter_Type()
)
brnCarrierCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnCarrierCounter.setStatus("mandatory")
_BrnCarrierTimeInterval_Type = TimeTicks
_BrnCarrierTimeInterval_Object = MibTableColumn
brnCarrierTimeInterval = _BrnCarrierTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 5),
    _BrnCarrierTimeInterval_Type()
)
brnCarrierTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnCarrierTimeInterval.setStatus("mandatory")
_BrnTransmitPkts_Type = Counter32
_BrnTransmitPkts_Object = MibTableColumn
brnTransmitPkts = _BrnTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 6),
    _BrnTransmitPkts_Type()
)
brnTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnTransmitPkts.setStatus("mandatory")
_BrnReceivePkts_Type = Counter32
_BrnReceivePkts_Object = MibTableColumn
brnReceivePkts = _BrnReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 7),
    _BrnReceivePkts_Type()
)
brnReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnReceivePkts.setStatus("mandatory")
_BrnCRCErrors_Type = Counter32
_BrnCRCErrors_Object = MibTableColumn
brnCRCErrors = _BrnCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 8),
    _BrnCRCErrors_Type()
)
brnCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnCRCErrors.setStatus("mandatory")
_BrnCollisions_Type = Counter32
_BrnCollisions_Object = MibTableColumn
brnCollisions = _BrnCollisions_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 9),
    _BrnCollisions_Type()
)
brnCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnCollisions.setStatus("mandatory")
_BrnPktsAborted16Colls_Type = Counter32
_BrnPktsAborted16Colls_Object = MibTableColumn
brnPktsAborted16Colls = _BrnPktsAborted16Colls_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 10),
    _BrnPktsAborted16Colls_Type()
)
brnPktsAborted16Colls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnPktsAborted16Colls.setStatus("mandatory")
_BrnShortPkts_Type = Counter32
_BrnShortPkts_Object = MibTableColumn
brnShortPkts = _BrnShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 11),
    _BrnShortPkts_Type()
)
brnShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnShortPkts.setStatus("mandatory")
_BrnAlignmentErrors_Type = Counter32
_BrnAlignmentErrors_Object = MibTableColumn
brnAlignmentErrors = _BrnAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 12),
    _BrnAlignmentErrors_Type()
)
brnAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnAlignmentErrors.setStatus("mandatory")
_BrnOverflows_Type = Counter32
_BrnOverflows_Object = MibTableColumn
brnOverflows = _BrnOverflows_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 13),
    _BrnOverflows_Type()
)
brnOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnOverflows.setStatus("mandatory")
_BrnUnderflows_Type = Counter32
_BrnUnderflows_Object = MibTableColumn
brnUnderflows = _BrnUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 15, 1, 14),
    _BrnUnderflows_Type()
)
brnUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brnUnderflows.setStatus("mandatory")
_Tr16cTable_Object = MibTable
tr16cTable = _Tr16cTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    tr16cTable.setStatus("mandatory")
_Tr16cEntry_Object = MibTableRow
tr16cEntry = _Tr16cEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1)
)
tr16cEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "tr16cSlotId"),
)
if mibBuilder.loadTexts:
    tr16cEntry.setStatus("mandatory")
_Tr16cSlotId_Type = Integer32
_Tr16cSlotId_Object = MibTableColumn
tr16cSlotId = _Tr16cSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 1),
    _Tr16cSlotId_Type()
)
tr16cSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cSlotId.setStatus("mandatory")


class _Tr16cTier_Type(Integer32):
    """Custom type tr16cTier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tier-1", 1),
          ("tier-2", 2),
          ("tier-3", 3))
    )


_Tr16cTier_Type.__name__ = "Integer32"
_Tr16cTier_Object = MibTableColumn
tr16cTier = _Tr16cTier_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 2),
    _Tr16cTier_Type()
)
tr16cTier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cTier.setStatus("mandatory")


class _Tr16cOperState_Type(Integer32):
    """Custom type tr16cOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("beaconDetectInProgress", 3),
          ("normal", 2),
          ("notApplicable", 1))
    )


_Tr16cOperState_Type.__name__ = "Integer32"
_Tr16cOperState_Object = MibTableColumn
tr16cOperState = _Tr16cOperState_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 3),
    _Tr16cOperState_Type()
)
tr16cOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cOperState.setStatus("mandatory")
_Tr16cRingNumber_Type = Integer32
_Tr16cRingNumber_Object = MibTableColumn
tr16cRingNumber = _Tr16cRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 4),
    _Tr16cRingNumber_Type()
)
tr16cRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cRingNumber.setStatus("mandatory")
_Tr16cManufacturerID_Type = OctetString
_Tr16cManufacturerID_Object = MibTableColumn
tr16cManufacturerID = _Tr16cManufacturerID_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 5),
    _Tr16cManufacturerID_Type()
)
tr16cManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cManufacturerID.setStatus("mandatory")
_Tr16cManufacturerProductID_Type = DisplayString
_Tr16cManufacturerProductID_Object = MibTableColumn
tr16cManufacturerProductID = _Tr16cManufacturerProductID_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 6),
    _Tr16cManufacturerProductID_Type()
)
tr16cManufacturerProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cManufacturerProductID.setStatus("mandatory")
_Tr16cManufProductVers_Type = OctetString
_Tr16cManufProductVers_Object = MibTableColumn
tr16cManufProductVers = _Tr16cManufProductVers_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 7),
    _Tr16cManufProductVers_Type()
)
tr16cManufProductVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cManufProductVers.setStatus("mandatory")
_Tr16cActiveMonitorPortNumber_Type = Integer32
_Tr16cActiveMonitorPortNumber_Object = MibTableColumn
tr16cActiveMonitorPortNumber = _Tr16cActiveMonitorPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 8),
    _Tr16cActiveMonitorPortNumber_Type()
)
tr16cActiveMonitorPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cActiveMonitorPortNumber.setStatus("mandatory")


class _Tr16cRingSpeed_Type(Integer32):
    """Custom type tr16cRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourMbps", 2),
          ("notApplicable", 1),
          ("sixteenMbps", 3))
    )


_Tr16cRingSpeed_Type.__name__ = "Integer32"
_Tr16cRingSpeed_Object = MibTableColumn
tr16cRingSpeed = _Tr16cRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 9),
    _Tr16cRingSpeed_Type()
)
tr16cRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cRingSpeed.setStatus("mandatory")
_Tr16cLLCFrames_Type = Counter32
_Tr16cLLCFrames_Object = MibTableColumn
tr16cLLCFrames = _Tr16cLLCFrames_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 10),
    _Tr16cLLCFrames_Type()
)
tr16cLLCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cLLCFrames.setStatus("mandatory")
_Tr16cMACFrames_Type = Counter32
_Tr16cMACFrames_Object = MibTableColumn
tr16cMACFrames = _Tr16cMACFrames_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 11),
    _Tr16cMACFrames_Type()
)
tr16cMACFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cMACFrames.setStatus("mandatory")
_Tr16cOctets_Type = Counter32
_Tr16cOctets_Object = MibTableColumn
tr16cOctets = _Tr16cOctets_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 12),
    _Tr16cOctets_Type()
)
tr16cOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cOctets.setStatus("mandatory")
_Tr16cMulticastFrames_Type = Counter32
_Tr16cMulticastFrames_Object = MibTableColumn
tr16cMulticastFrames = _Tr16cMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 13),
    _Tr16cMulticastFrames_Type()
)
tr16cMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cMulticastFrames.setStatus("mandatory")
_Tr16cBroadcastFrames_Type = Counter32
_Tr16cBroadcastFrames_Object = MibTableColumn
tr16cBroadcastFrames = _Tr16cBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 14),
    _Tr16cBroadcastFrames_Type()
)
tr16cBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cBroadcastFrames.setStatus("mandatory")
_Tr16cFrameCheckSequences_Type = Counter32
_Tr16cFrameCheckSequences_Object = MibTableColumn
tr16cFrameCheckSequences = _Tr16cFrameCheckSequences_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 15),
    _Tr16cFrameCheckSequences_Type()
)
tr16cFrameCheckSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cFrameCheckSequences.setStatus("mandatory")
_Tr16cAutoPartitionEnableTimer_Type = TimeTicks
_Tr16cAutoPartitionEnableTimer_Object = MibTableColumn
tr16cAutoPartitionEnableTimer = _Tr16cAutoPartitionEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 16),
    _Tr16cAutoPartitionEnableTimer_Type()
)
tr16cAutoPartitionEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr16cAutoPartitionEnableTimer.setStatus("mandatory")
_Tr16cAutoPartitionHoldTimer_Type = TimeTicks
_Tr16cAutoPartitionHoldTimer_Object = MibTableColumn
tr16cAutoPartitionHoldTimer = _Tr16cAutoPartitionHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 17),
    _Tr16cAutoPartitionHoldTimer_Type()
)
tr16cAutoPartitionHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr16cAutoPartitionHoldTimer.setStatus("mandatory")
_Tr16cAutoPartitionRetries_Type = Integer32
_Tr16cAutoPartitionRetries_Object = MibTableColumn
tr16cAutoPartitionRetries = _Tr16cAutoPartitionRetries_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 18),
    _Tr16cAutoPartitionRetries_Type()
)
tr16cAutoPartitionRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr16cAutoPartitionRetries.setStatus("mandatory")
_Tr16cLLCSamples_Type = Counter32
_Tr16cLLCSamples_Object = MibTableColumn
tr16cLLCSamples = _Tr16cLLCSamples_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 19),
    _Tr16cLLCSamples_Type()
)
tr16cLLCSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cLLCSamples.setStatus("mandatory")
_Tr16cMACSamples_Type = Counter32
_Tr16cMACSamples_Object = MibTableColumn
tr16cMACSamples = _Tr16cMACSamples_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 20),
    _Tr16cMACSamples_Type()
)
tr16cMACSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cMACSamples.setStatus("mandatory")
_Tr16cUpTimeMS_Type = Counter32
_Tr16cUpTimeMS_Object = MibTableColumn
tr16cUpTimeMS = _Tr16cUpTimeMS_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 21),
    _Tr16cUpTimeMS_Type()
)
tr16cUpTimeMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16cUpTimeMS.setStatus("mandatory")


class _Tr16cResetDurableUserAttrs_Type(Integer32):
    """Custom type tr16cResetDurableUserAttrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetComplete", 1),
          ("setToDefaults", 2))
    )


_Tr16cResetDurableUserAttrs_Type.__name__ = "Integer32"
_Tr16cResetDurableUserAttrs_Object = MibTableColumn
tr16cResetDurableUserAttrs = _Tr16cResetDurableUserAttrs_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 16, 1, 22),
    _Tr16cResetDurableUserAttrs_Type()
)
tr16cResetDurableUserAttrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr16cResetDurableUserAttrs.setStatus("mandatory")
_Tr16reTable_Object = MibTable
tr16reTable = _Tr16reTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17)
)
if mibBuilder.loadTexts:
    tr16reTable.setStatus("mandatory")
_Tr16reEntry_Object = MibTableRow
tr16reEntry = _Tr16reEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17, 1)
)
tr16reEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "tr16reSlotId"),
)
if mibBuilder.loadTexts:
    tr16reEntry.setStatus("mandatory")
_Tr16reSlotId_Type = Integer32
_Tr16reSlotId_Object = MibTableColumn
tr16reSlotId = _Tr16reSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17, 1, 1),
    _Tr16reSlotId_Type()
)
tr16reSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16reSlotId.setStatus("mandatory")
_Tr16reLostFrames_Type = Counter32
_Tr16reLostFrames_Object = MibTableColumn
tr16reLostFrames = _Tr16reLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17, 1, 2),
    _Tr16reLostFrames_Type()
)
tr16reLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16reLostFrames.setStatus("mandatory")
_Tr16reRcvCongestionErrors_Type = Counter32
_Tr16reRcvCongestionErrors_Object = MibTableColumn
tr16reRcvCongestionErrors = _Tr16reRcvCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17, 1, 3),
    _Tr16reRcvCongestionErrors_Type()
)
tr16reRcvCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16reRcvCongestionErrors.setStatus("mandatory")
_Tr16reFrequencyErrors_Type = Counter32
_Tr16reFrequencyErrors_Object = MibTableColumn
tr16reFrequencyErrors = _Tr16reFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17, 1, 4),
    _Tr16reFrequencyErrors_Type()
)
tr16reFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16reFrequencyErrors.setStatus("mandatory")
_Tr16reFrameCopyErrors_Type = Counter32
_Tr16reFrameCopyErrors_Object = MibTableColumn
tr16reFrameCopyErrors = _Tr16reFrameCopyErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17, 1, 5),
    _Tr16reFrameCopyErrors_Type()
)
tr16reFrameCopyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16reFrameCopyErrors.setStatus("mandatory")
_Tr16reTokenErrors_Type = Counter32
_Tr16reTokenErrors_Object = MibTableColumn
tr16reTokenErrors = _Tr16reTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 2, 17, 1, 6),
    _Tr16reTokenErrors_Type()
)
tr16reTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16reTokenErrors.setStatus("mandatory")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3)
)
_EcpTable_Object = MibTable
ecpTable = _EcpTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ecpTable.setStatus("mandatory")
_EcpEntry_Object = MibTableRow
ecpEntry = _EcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 1, 1)
)
ecpEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "ecpSlotId"),
    (0, "UB-MIB-SUPRV", "ecpPortId"),
)
if mibBuilder.loadTexts:
    ecpEntry.setStatus("mandatory")
_EcpSlotId_Type = Integer32
_EcpSlotId_Object = MibTableColumn
ecpSlotId = _EcpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 1, 1, 1),
    _EcpSlotId_Type()
)
ecpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSlotId.setStatus("mandatory")
_EcpPortId_Type = Integer32
_EcpPortId_Object = MibTableColumn
ecpPortId = _EcpPortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 1, 1, 2),
    _EcpPortId_Type()
)
ecpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpPortId.setStatus("mandatory")


class _EcpMgmtStatus_Type(Integer32):
    """Custom type ecpMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("autosegmented", 4),
          ("enabled", 2),
          ("faultyLockedBySuprv", 5),
          ("lockedByNMC", 3),
          ("lowLight", 6),
          ("notApplicable", 1))
    )


_EcpMgmtStatus_Type.__name__ = "Integer32"
_EcpMgmtStatus_Object = MibTableColumn
ecpMgmtStatus = _EcpMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 1, 1, 3),
    _EcpMgmtStatus_Type()
)
ecpMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpMgmtStatus.setStatus("mandatory")


class _EcpAdmAction_Type(Integer32):
    """Custom type ecpAdmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 3),
          ("notApplicable", 1),
          ("unlocked", 2))
    )


_EcpAdmAction_Type.__name__ = "Integer32"
_EcpAdmAction_Object = MibTableColumn
ecpAdmAction = _EcpAdmAction_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 1, 1, 4),
    _EcpAdmAction_Type()
)
ecpAdmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpAdmAction.setStatus("mandatory")
_EcpCarrierCounter_Type = Counter32
_EcpCarrierCounter_Object = MibTableColumn
ecpCarrierCounter = _EcpCarrierCounter_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 1, 1, 5),
    _EcpCarrierCounter_Type()
)
ecpCarrierCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpCarrierCounter.setStatus("mandatory")
_EcfpTable_Object = MibTable
ecfpTable = _EcfpTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ecfpTable.setStatus("mandatory")
_EcfpEntry_Object = MibTableRow
ecfpEntry = _EcfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 2, 1)
)
ecfpEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "ecfpSlotId"),
    (0, "UB-MIB-SUPRV", "ecfpPortId"),
)
if mibBuilder.loadTexts:
    ecfpEntry.setStatus("mandatory")
_EcfpSlotId_Type = Integer32
_EcfpSlotId_Object = MibTableColumn
ecfpSlotId = _EcfpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 2, 1, 1),
    _EcfpSlotId_Type()
)
ecfpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecfpSlotId.setStatus("mandatory")
_EcfpPortId_Type = Integer32
_EcfpPortId_Object = MibTableColumn
ecfpPortId = _EcfpPortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 2, 1, 2),
    _EcfpPortId_Type()
)
ecfpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecfpPortId.setStatus("mandatory")
_EcfpMACAddr_Type = PhysAddress
_EcfpMACAddr_Object = MibTableColumn
ecfpMACAddr = _EcfpMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 2, 1, 3),
    _EcfpMACAddr_Type()
)
ecfpMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecfpMACAddr.setStatus("mandatory")
_EcfpTxIdleTime_Type = TimeTicks
_EcfpTxIdleTime_Object = MibTableColumn
ecfpTxIdleTime = _EcfpTxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 2, 1, 4),
    _EcfpTxIdleTime_Type()
)
ecfpTxIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecfpTxIdleTime.setStatus("mandatory")
_Ec10btpTable_Object = MibTable
ec10btpTable = _Ec10btpTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ec10btpTable.setStatus("mandatory")
_Ec10btpEntry_Object = MibTableRow
ec10btpEntry = _Ec10btpEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 3, 1)
)
ec10btpEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "ec10btpSlotId"),
    (0, "UB-MIB-SUPRV", "ec10btpPortId"),
)
if mibBuilder.loadTexts:
    ec10btpEntry.setStatus("mandatory")
_Ec10btpSlotId_Type = Integer32
_Ec10btpSlotId_Object = MibTableColumn
ec10btpSlotId = _Ec10btpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 3, 1, 1),
    _Ec10btpSlotId_Type()
)
ec10btpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ec10btpSlotId.setStatus("mandatory")
_Ec10btpPortId_Type = Integer32
_Ec10btpPortId_Object = MibTableColumn
ec10btpPortId = _Ec10btpPortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 3, 1, 2),
    _Ec10btpPortId_Type()
)
ec10btpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ec10btpPortId.setStatus("mandatory")


class _Ec10btpLinkTestStatus_Type(Integer32):
    """Custom type ec10btpLinkTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 3),
          ("testLocked", 2),
          ("testPassed", 4))
    )


_Ec10btpLinkTestStatus_Type.__name__ = "Integer32"
_Ec10btpLinkTestStatus_Object = MibTableColumn
ec10btpLinkTestStatus = _Ec10btpLinkTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 3, 1, 3),
    _Ec10btpLinkTestStatus_Type()
)
ec10btpLinkTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ec10btpLinkTestStatus.setStatus("mandatory")


class _Ec10btpLinkTestAction_Type(Integer32):
    """Custom type ec10btpLinkTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lockIntegrityTest", 3),
          ("unlockIntegrityTest", 2))
    )


_Ec10btpLinkTestAction_Type.__name__ = "Integer32"
_Ec10btpLinkTestAction_Object = MibTableColumn
ec10btpLinkTestAction = _Ec10btpLinkTestAction_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 3, 1, 4),
    _Ec10btpLinkTestAction_Type()
)
ec10btpLinkTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ec10btpLinkTestAction.setStatus("mandatory")
_TrcpTable_Object = MibTable
trcpTable = _TrcpTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    trcpTable.setStatus("mandatory")
_TrcpEntry_Object = MibTableRow
trcpEntry = _TrcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 4, 1)
)
trcpEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "trcpSlotId"),
    (0, "UB-MIB-SUPRV", "trcpPortId"),
)
if mibBuilder.loadTexts:
    trcpEntry.setStatus("mandatory")
_TrcpSlotId_Type = Integer32
_TrcpSlotId_Object = MibTableColumn
trcpSlotId = _TrcpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 4, 1, 1),
    _TrcpSlotId_Type()
)
trcpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcpSlotId.setStatus("mandatory")


class _TrcpPortId_Type(Integer32):
    """Custom type trcpPortId based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("in", 21),
          ("out", 22),
          ("rs1", 1),
          ("rs10", 10),
          ("rs11", 11),
          ("rs12", 12),
          ("rs13", 13),
          ("rs14", 14),
          ("rs15", 15),
          ("rs16", 16),
          ("rs17", 17),
          ("rs18", 18),
          ("rs19", 19),
          ("rs2", 2),
          ("rs20", 20),
          ("rs3", 3),
          ("rs4", 4),
          ("rs5", 5),
          ("rs6", 6),
          ("rs7", 7),
          ("rs8", 8),
          ("rs9", 9))
    )


_TrcpPortId_Type.__name__ = "Integer32"
_TrcpPortId_Object = MibTableColumn
trcpPortId = _TrcpPortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 4, 1, 2),
    _TrcpPortId_Type()
)
trcpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcpPortId.setStatus("mandatory")


class _TrcpAdmAction_Type(Integer32):
    """Custom type trcpAdmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 3),
          ("notApplicable", 1),
          ("unlock", 2))
    )


_TrcpAdmAction_Type.__name__ = "Integer32"
_TrcpAdmAction_Object = MibTableColumn
trcpAdmAction = _TrcpAdmAction_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 4, 1, 3),
    _TrcpAdmAction_Type()
)
trcpAdmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trcpAdmAction.setStatus("mandatory")


class _TrcpOperStatus_Type(Integer32):
    """Custom type trcpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("portError", 4),
          ("selfBypass", 3),
          ("stationInserted", 2))
    )


_TrcpOperStatus_Type.__name__ = "Integer32"
_TrcpOperStatus_Object = MibTableColumn
trcpOperStatus = _TrcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 4, 1, 4),
    _TrcpOperStatus_Type()
)
trcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trcpOperStatus.setStatus("mandatory")
_Tr16p1Table_Object = MibTable
tr16p1Table = _Tr16p1Table_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tr16p1Table.setStatus("mandatory")
_Tr16p1Entry_Object = MibTableRow
tr16p1Entry = _Tr16p1Entry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5, 1)
)
tr16p1Entry.setIndexNames(
    (0, "UB-MIB-SUPRV", "tr16p1SlotId"),
    (0, "UB-MIB-SUPRV", "tr16p1PortId"),
)
if mibBuilder.loadTexts:
    tr16p1Entry.setStatus("mandatory")
_Tr16p1SlotId_Type = Integer32
_Tr16p1SlotId_Object = MibTableColumn
tr16p1SlotId = _Tr16p1SlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5, 1, 1),
    _Tr16p1SlotId_Type()
)
tr16p1SlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p1SlotId.setStatus("mandatory")


class _Tr16p1PortId_Type(Integer32):
    """Custom type tr16p1PortId based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("in", 13),
          ("out", 14),
          ("rs1", 1),
          ("rs10", 10),
          ("rs11", 11),
          ("rs12", 12),
          ("rs2", 2),
          ("rs3", 3),
          ("rs4", 4),
          ("rs5", 5),
          ("rs6", 6),
          ("rs7", 7),
          ("rs8", 8),
          ("rs9", 9))
    )


_Tr16p1PortId_Type.__name__ = "Integer32"
_Tr16p1PortId_Object = MibTableColumn
tr16p1PortId = _Tr16p1PortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5, 1, 2),
    _Tr16p1PortId_Type()
)
tr16p1PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p1PortId.setStatus("mandatory")


class _Tr16p1InsertionState_Type(Integer32):
    """Custom type tr16p1InsertionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 3),
          ("inserted", 2),
          ("notApplicable", 1))
    )


_Tr16p1InsertionState_Type.__name__ = "Integer32"
_Tr16p1InsertionState_Object = MibTableColumn
tr16p1InsertionState = _Tr16p1InsertionState_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5, 1, 3),
    _Tr16p1InsertionState_Type()
)
tr16p1InsertionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p1InsertionState.setStatus("mandatory")


class _Tr16p1AllowInsert_Type(Integer32):
    """Custom type tr16p1AllowInsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insertionAllowed", 3),
          ("insertionNotAllowed", 2),
          ("notApplicable", 1))
    )


_Tr16p1AllowInsert_Type.__name__ = "Integer32"
_Tr16p1AllowInsert_Object = MibTableColumn
tr16p1AllowInsert = _Tr16p1AllowInsert_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5, 1, 4),
    _Tr16p1AllowInsert_Type()
)
tr16p1AllowInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr16p1AllowInsert.setStatus("mandatory")


class _Tr16p1ForceInsert_Type(Integer32):
    """Custom type tr16p1ForceInsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcedInsertion", 3),
          ("noForcedInsertion", 2),
          ("notApplicable", 1))
    )


_Tr16p1ForceInsert_Type.__name__ = "Integer32"
_Tr16p1ForceInsert_Object = MibTableColumn
tr16p1ForceInsert = _Tr16p1ForceInsert_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5, 1, 5),
    _Tr16p1ForceInsert_Type()
)
tr16p1ForceInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tr16p1ForceInsert.setStatus("mandatory")


class _Tr16p1PhantomState_Type(Integer32):
    """Custom type tr16p1PhantomState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("phantomVoltageAbsent", 3),
          ("phantomVoltagePresent", 2),
          ("wiringFault", 4))
    )


_Tr16p1PhantomState_Type.__name__ = "Integer32"
_Tr16p1PhantomState_Object = MibTableColumn
tr16p1PhantomState = _Tr16p1PhantomState_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 5, 1, 6),
    _Tr16p1PhantomState_Type()
)
tr16p1PhantomState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p1PhantomState.setStatus("mandatory")
_Tr16p2Table_Object = MibTable
tr16p2Table = _Tr16p2Table_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tr16p2Table.setStatus("mandatory")
_Tr16p2Entry_Object = MibTableRow
tr16p2Entry = _Tr16p2Entry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1)
)
tr16p2Entry.setIndexNames(
    (0, "UB-MIB-SUPRV", "tr16p2SlotId"),
    (0, "UB-MIB-SUPRV", "tr16p2PortId"),
)
if mibBuilder.loadTexts:
    tr16p2Entry.setStatus("mandatory")
_Tr16p2SlotId_Type = Integer32
_Tr16p2SlotId_Object = MibTableColumn
tr16p2SlotId = _Tr16p2SlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 1),
    _Tr16p2SlotId_Type()
)
tr16p2SlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2SlotId.setStatus("mandatory")


class _Tr16p2PortId_Type(Integer32):
    """Custom type tr16p2PortId based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("in", 13),
          ("out", 14),
          ("rs1", 1),
          ("rs10", 10),
          ("rs11", 11),
          ("rs12", 12),
          ("rs2", 2),
          ("rs3", 3),
          ("rs4", 4),
          ("rs5", 5),
          ("rs6", 6),
          ("rs7", 7),
          ("rs8", 8),
          ("rs9", 9))
    )


_Tr16p2PortId_Type.__name__ = "Integer32"
_Tr16p2PortId_Object = MibTableColumn
tr16p2PortId = _Tr16p2PortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 2),
    _Tr16p2PortId_Type()
)
tr16p2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2PortId.setStatus("mandatory")


class _Tr16p2OperState_Type(Integer32):
    """Custom type tr16p2OperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 3),
          ("notApplicable", 1),
          ("portOperational", 2))
    )


_Tr16p2OperState_Type.__name__ = "Integer32"
_Tr16p2OperState_Object = MibTableColumn
tr16p2OperState = _Tr16p2OperState_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 3),
    _Tr16p2OperState_Type()
)
tr16p2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2OperState.setStatus("mandatory")
_Tr16p2BeaconDetects_Type = Counter32
_Tr16p2BeaconDetects_Object = MibTableColumn
tr16p2BeaconDetects = _Tr16p2BeaconDetects_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 4),
    _Tr16p2BeaconDetects_Type()
)
tr16p2BeaconDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2BeaconDetects.setStatus("mandatory")
_Tr16p2LastSourceAddress_Type = PhysAddress
_Tr16p2LastSourceAddress_Object = MibTableColumn
tr16p2LastSourceAddress = _Tr16p2LastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 5),
    _Tr16p2LastSourceAddress_Type()
)
tr16p2LastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2LastSourceAddress.setStatus("mandatory")
_Tr16p2LLCFramesTransmitted_Type = Counter32
_Tr16p2LLCFramesTransmitted_Object = MibTableColumn
tr16p2LLCFramesTransmitted = _Tr16p2LLCFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 6),
    _Tr16p2LLCFramesTransmitted_Type()
)
tr16p2LLCFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2LLCFramesTransmitted.setStatus("mandatory")
_Tr16p2LLCFramesReceived_Type = Counter32
_Tr16p2LLCFramesReceived_Object = MibTableColumn
tr16p2LLCFramesReceived = _Tr16p2LLCFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 7),
    _Tr16p2LLCFramesReceived_Type()
)
tr16p2LLCFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2LLCFramesReceived.setStatus("mandatory")
_Tr16p2MACFramesTransmitted_Type = Counter32
_Tr16p2MACFramesTransmitted_Object = MibTableColumn
tr16p2MACFramesTransmitted = _Tr16p2MACFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 8),
    _Tr16p2MACFramesTransmitted_Type()
)
tr16p2MACFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2MACFramesTransmitted.setStatus("mandatory")
_Tr16p2MACFramesReceived_Type = Counter32
_Tr16p2MACFramesReceived_Object = MibTableColumn
tr16p2MACFramesReceived = _Tr16p2MACFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 9),
    _Tr16p2MACFramesReceived_Type()
)
tr16p2MACFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2MACFramesReceived.setStatus("mandatory")
_Tr16p2OctetsTransmitted_Type = Counter32
_Tr16p2OctetsTransmitted_Object = MibTableColumn
tr16p2OctetsTransmitted = _Tr16p2OctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 10),
    _Tr16p2OctetsTransmitted_Type()
)
tr16p2OctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2OctetsTransmitted.setStatus("mandatory")
_Tr16p2OctetsReceived_Type = Counter32
_Tr16p2OctetsReceived_Object = MibTableColumn
tr16p2OctetsReceived = _Tr16p2OctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 11),
    _Tr16p2OctetsReceived_Type()
)
tr16p2OctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2OctetsReceived.setStatus("mandatory")
_Tr16p2MulticastsTransmitted_Type = Counter32
_Tr16p2MulticastsTransmitted_Object = MibTableColumn
tr16p2MulticastsTransmitted = _Tr16p2MulticastsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 12),
    _Tr16p2MulticastsTransmitted_Type()
)
tr16p2MulticastsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2MulticastsTransmitted.setStatus("mandatory")
_Tr16p2BroadcastsTransmitted_Type = Counter32
_Tr16p2BroadcastsTransmitted_Object = MibTableColumn
tr16p2BroadcastsTransmitted = _Tr16p2BroadcastsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 13),
    _Tr16p2BroadcastsTransmitted_Type()
)
tr16p2BroadcastsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2BroadcastsTransmitted.setStatus("mandatory")
_Tr16p2FCSErrorsTransmitted_Type = Counter32
_Tr16p2FCSErrorsTransmitted_Object = MibTableColumn
tr16p2FCSErrorsTransmitted = _Tr16p2FCSErrorsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 14),
    _Tr16p2FCSErrorsTransmitted_Type()
)
tr16p2FCSErrorsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2FCSErrorsTransmitted.setStatus("mandatory")
_Tr16p2FCSErrorsReceived_Type = Counter32
_Tr16p2FCSErrorsReceived_Object = MibTableColumn
tr16p2FCSErrorsReceived = _Tr16p2FCSErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 15),
    _Tr16p2FCSErrorsReceived_Type()
)
tr16p2FCSErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2FCSErrorsReceived.setStatus("mandatory")
_Tr16p2LastSourceAddressUptime_Type = TimeTicks
_Tr16p2LastSourceAddressUptime_Object = MibTableColumn
tr16p2LastSourceAddressUptime = _Tr16p2LastSourceAddressUptime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 6, 1, 16),
    _Tr16p2LastSourceAddressUptime_Type()
)
tr16p2LastSourceAddressUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p2LastSourceAddressUptime.setStatus("mandatory")
_Tr16p3Table_Object = MibTable
tr16p3Table = _Tr16p3Table_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tr16p3Table.setStatus("mandatory")
_Tr16p3Entry_Object = MibTableRow
tr16p3Entry = _Tr16p3Entry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1)
)
tr16p3Entry.setIndexNames(
    (0, "UB-MIB-SUPRV", "tr16p3SlotId"),
    (0, "UB-MIB-SUPRV", "tr16p3PortId"),
)
if mibBuilder.loadTexts:
    tr16p3Entry.setStatus("mandatory")
_Tr16p3SlotId_Type = Integer32
_Tr16p3SlotId_Object = MibTableColumn
tr16p3SlotId = _Tr16p3SlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1, 1),
    _Tr16p3SlotId_Type()
)
tr16p3SlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p3SlotId.setStatus("mandatory")


class _Tr16p3PortId_Type(Integer32):
    """Custom type tr16p3PortId based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("in", 13),
          ("out", 14),
          ("rs1", 1),
          ("rs10", 10),
          ("rs11", 11),
          ("rs12", 12),
          ("rs2", 2),
          ("rs3", 3),
          ("rs4", 4),
          ("rs5", 5),
          ("rs6", 6),
          ("rs7", 7),
          ("rs8", 8),
          ("rs9", 9))
    )


_Tr16p3PortId_Type.__name__ = "Integer32"
_Tr16p3PortId_Object = MibTableColumn
tr16p3PortId = _Tr16p3PortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1, 2),
    _Tr16p3PortId_Type()
)
tr16p3PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p3PortId.setStatus("mandatory")
_Tr16p3LineErrors_Type = Counter32
_Tr16p3LineErrors_Object = MibTableColumn
tr16p3LineErrors = _Tr16p3LineErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1, 3),
    _Tr16p3LineErrors_Type()
)
tr16p3LineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p3LineErrors.setStatus("mandatory")
_Tr16p3InternalErrors_Type = Counter32
_Tr16p3InternalErrors_Object = MibTableColumn
tr16p3InternalErrors = _Tr16p3InternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1, 4),
    _Tr16p3InternalErrors_Type()
)
tr16p3InternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p3InternalErrors.setStatus("mandatory")
_Tr16p3Burst5Errors_Type = Counter32
_Tr16p3Burst5Errors_Object = MibTableColumn
tr16p3Burst5Errors = _Tr16p3Burst5Errors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1, 5),
    _Tr16p3Burst5Errors_Type()
)
tr16p3Burst5Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p3Burst5Errors.setStatus("mandatory")
_Tr16p3AcErrors_Type = Counter32
_Tr16p3AcErrors_Object = MibTableColumn
tr16p3AcErrors = _Tr16p3AcErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1, 6),
    _Tr16p3AcErrors_Type()
)
tr16p3AcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p3AcErrors.setStatus("mandatory")
_Tr16p3AbortDelimiters_Type = Counter32
_Tr16p3AbortDelimiters_Object = MibTableColumn
tr16p3AbortDelimiters = _Tr16p3AbortDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 1, 3, 7, 1, 7),
    _Tr16p3AbortDelimiters_Type()
)
tr16p3AbortDelimiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tr16p3AbortDelimiters.setStatus("mandatory")
_UbTrapAttrs_ObjectIdentity = ObjectIdentity
ubTrapAttrs = _UbTrapAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 3)
)
_TrapInstanceId_Type = Integer32
_TrapInstanceId_Object = MibScalar
trapInstanceId = _TrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 75, 3, 1),
    _TrapInstanceId_Type()
)
trapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapInstanceId.setStatus("mandatory")
_TrapSlotId_Type = Integer32
_TrapSlotId_Object = MibScalar
trapSlotId = _TrapSlotId_Object(
    (1, 3, 6, 1, 4, 1, 75, 3, 2),
    _TrapSlotId_Type()
)
trapSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSlotId.setStatus("optional")
_TrapProductType_Type = Integer32
_TrapProductType_Object = MibScalar
trapProductType = _TrapProductType_Object(
    (1, 3, 6, 1, 4, 1, 75, 3, 3),
    _TrapProductType_Type()
)
trapProductType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapProductType.setStatus("mandatory")
_TrapPortID_Type = Integer32
_TrapPortID_Object = MibScalar
trapPortID = _TrapPortID_Object(
    (1, 3, 6, 1, 4, 1, 75, 3, 4),
    _TrapPortID_Type()
)
trapPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapPortID.setStatus("optional")
_TrapPortCount_Type = Integer32
_TrapPortCount_Object = MibScalar
trapPortCount = _TrapPortCount_Object(
    (1, 3, 6, 1, 4, 1, 75, 3, 15),
    _TrapPortCount_Type()
)
trapPortCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapPortCount.setStatus("optional")
_TrapPortMask_Type = OctetString
_TrapPortMask_Object = MibScalar
trapPortMask = _TrapPortMask_Object(
    (1, 3, 6, 1, 4, 1, 75, 3, 16),
    _TrapPortMask_Type()
)
trapPortMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapPortMask.setStatus("optional")
_UbSystem_ObjectIdentity = ObjectIdentity
ubSystem = _UbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 4)
)
_UbSecurity_ObjectIdentity = ObjectIdentity
ubSecurity = _UbSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 4, 1)
)
_TrpsbTable_Object = MibTable
trpsbTable = _TrpsbTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 4, 1, 2)
)
if mibBuilder.loadTexts:
    trpsbTable.setStatus("mandatory")
_TrpsbEntry_Object = MibTableRow
trpsbEntry = _TrpsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 4, 1, 2, 1)
)
trpsbEntry.setIndexNames(
    (0, "UB-MIB-SUPRV", "trpsbIpAddress"),
)
if mibBuilder.loadTexts:
    trpsbEntry.setStatus("mandatory")
_TrpsbIpAddress_Type = IpAddress
_TrpsbIpAddress_Object = MibTableColumn
trpsbIpAddress = _TrpsbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 75, 4, 1, 2, 1, 1),
    _TrpsbIpAddress_Type()
)
trpsbIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trpsbIpAddress.setStatus("mandatory")
_TrpsbCommunity_Type = OctetString
_TrpsbCommunity_Object = MibTableColumn
trpsbCommunity = _TrpsbCommunity_Object(
    (1, 3, 6, 1, 4, 1, 75, 4, 1, 2, 1, 2),
    _TrpsbCommunity_Type()
)
trpsbCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trpsbCommunity.setStatus("mandatory")


class _TrpsbActions_Type(Integer32):
    """Custom type trpsbActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("subscribeToTraps", 2),
          ("subscriptionToTrapsCancelled", 3))
    )


_TrpsbActions_Type.__name__ = "Integer32"
_TrpsbActions_Object = MibTableColumn
trpsbActions = _TrpsbActions_Object(
    (1, 3, 6, 1, 4, 1, 75, 4, 1, 2, 1, 3),
    _TrpsbActions_Type()
)
trpsbActions.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    trpsbActions.setStatus("mandatory")

# Managed Objects groups


# Notification objects

moduleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 1)
)
moduleInserted.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleInserted.setStatus(
        ""
    )

moduleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 2)
)
moduleRemoved.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleRemoved.setStatus(
        ""
    )

moduleFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 3)
)
moduleFaulty.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleFaulty.setStatus(
        ""
    )

moduleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 4)
)
moduleDown.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleDown.setStatus(
        ""
    )

moduleReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 5)
)
moduleReset.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleReset.setStatus(
        ""
    )

moduleDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 6)
)
moduleDebug.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleDebug.setStatus(
        ""
    )

moduleHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 7)
)
moduleHighTemperature.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleHighTemperature.setStatus(
        ""
    )

ethBusUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 8)
)
ethBusUnlocked.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    ethBusUnlocked.setStatus(
        ""
    )

ethBusLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 9)
)
ethBusLocked.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    ethBusLocked.setStatus(
        ""
    )

moduleNetIfEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 16)
)
moduleNetIfEnabled.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleNetIfEnabled.setStatus(
        ""
    )

moduleNetIfDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 17)
)
moduleNetIfDisabled.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleNetIfDisabled.setStatus(
        ""
    )

moduleNetIfLoopBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 18)
)
moduleNetIfLoopBack.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleNetIfLoopBack.setStatus(
        ""
    )

moduleNetIfInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 19)
)
moduleNetIfInternalError.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleNetIfInternalError.setStatus(
        ""
    )

moduleNetIfExternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 20)
)
moduleNetIfExternalError.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleNetIfExternalError.setStatus(
        ""
    )

moduleParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 21)
)
moduleParityError.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleParityError.setStatus(
        ""
    )

moduleFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 22)
)
moduleFanBad.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleFanBad.setStatus(
        ""
    )

beaconDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 23)
)
beaconDetected.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    beaconDetected.setStatus(
        ""
    )

moduleTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 24)
)
moduleTemperatureNormal.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    moduleTemperatureNormal.setStatus(
        ""
    )

portUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 32)
)
portUnlocked.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portUnlocked.setStatus(
        ""
    )

portLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 33)
)
portLocked.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portLocked.setStatus(
        ""
    )

portAutoSegmented = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 34)
)
portAutoSegmented.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portAutoSegmented.setStatus(
        ""
    )

portFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 35)
)
portFault.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portFault.setStatus(
        ""
    )

portForced = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 36)
)
portForced.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portForced.setStatus(
        ""
    )

portNotForced = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 37)
)
portNotForced.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portNotForced.setStatus(
        ""
    )

portLobeFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 38)
)
portLobeFault.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portLobeFault.setStatus(
        ""
    )

portLobeFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 39)
)
portLobeFaultCleared.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"))
)
if mibBuilder.loadTexts:
    portLobeFaultCleared.setStatus(
        ""
    )

portLinkTestUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 40)
)
portLinkTestUnlocked.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portLinkTestUnlocked.setStatus(
        ""
    )

portLinkTestLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 41)
)
portLinkTestLocked.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    portLinkTestLocked.setStatus(
        ""
    )

badPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 48)
)
badPowerSupply.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    badPowerSupply.setStatus(
        ""
    )

powerSupplyHiTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 49)
)
powerSupplyHiTemp.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    powerSupplyHiTemp.setStatus(
        ""
    )

networkIfError = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 50)
)
networkIfError.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    networkIfError.setStatus(
        ""
    )

networkIfOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 51)
)
networkIfOK.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    networkIfOK.setStatus(
        ""
    )

tempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 52)
)
if mibBuilder.loadTexts:
    tempBad.setStatus(
        ""
    )

tempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 53)
)
tempOK.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    tempOK.setStatus(
        ""
    )

fTPSBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 54)
)
fTPSBad.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    fTPSBad.setStatus(
        ""
    )

netUtilThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 55)
)
netUtilThreshold.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    netUtilThreshold.setStatus(
        ""
    )

enclosureFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 56)
)
enclosureFanBad.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    enclosureFanBad.setStatus(
        ""
    )

servicePortLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 64)
)
servicePortLogin.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    servicePortLogin.setStatus(
        ""
    )

servicePortLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 75, 0, 65)
)
servicePortLogout.setObjects(
      *(("UB-MIB-SUPRV", "trapInstanceId"),
        ("UB-MIB-SUPRV", "trapSlotId"),
        ("UB-MIB-SUPRV", "trapProductType"),
        ("UB-MIB-SUPRV", "trapPortID"),
        ("UB-MIB-SUPRV", "trapPortCount"),
        ("UB-MIB-SUPRV", "trapPortMask"))
)
if mibBuilder.loadTexts:
    servicePortLogout.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UB-MIB-SUPRV",
    **{"ubNode": ubNode,
       "moduleInserted": moduleInserted,
       "moduleRemoved": moduleRemoved,
       "moduleFaulty": moduleFaulty,
       "moduleDown": moduleDown,
       "moduleReset": moduleReset,
       "moduleDebug": moduleDebug,
       "moduleHighTemperature": moduleHighTemperature,
       "ethBusUnlocked": ethBusUnlocked,
       "ethBusLocked": ethBusLocked,
       "moduleNetIfEnabled": moduleNetIfEnabled,
       "moduleNetIfDisabled": moduleNetIfDisabled,
       "moduleNetIfLoopBack": moduleNetIfLoopBack,
       "moduleNetIfInternalError": moduleNetIfInternalError,
       "moduleNetIfExternalError": moduleNetIfExternalError,
       "moduleParityError": moduleParityError,
       "moduleFanBad": moduleFanBad,
       "beaconDetected": beaconDetected,
       "moduleTemperatureNormal": moduleTemperatureNormal,
       "portUnlocked": portUnlocked,
       "portLocked": portLocked,
       "portAutoSegmented": portAutoSegmented,
       "portFault": portFault,
       "portForced": portForced,
       "portNotForced": portNotForced,
       "portLobeFault": portLobeFault,
       "portLobeFaultCleared": portLobeFaultCleared,
       "portLinkTestUnlocked": portLinkTestUnlocked,
       "portLinkTestLocked": portLinkTestLocked,
       "badPowerSupply": badPowerSupply,
       "powerSupplyHiTemp": powerSupplyHiTemp,
       "networkIfError": networkIfError,
       "networkIfOK": networkIfOK,
       "tempBad": tempBad,
       "tempOK": tempOK,
       "fTPSBad": fTPSBad,
       "netUtilThreshold": netUtilThreshold,
       "enclosureFanBad": enclosureFanBad,
       "servicePortLogin": servicePortLogin,
       "servicePortLogout": servicePortLogout,
       "ubEquip": ubEquip,
       "ubSuprv": ubSuprv,
       "hub": hub,
       "hubId": hubId,
       "hubType": hubType,
       "hubName": hubName,
       "hubSerNumber": hubSerNumber,
       "hubIPAddr": hubIPAddr,
       "hubPowerSupplyStatus": hubPowerSupplyStatus,
       "hubTempStatus": hubTempStatus,
       "hubPollTime": hubPollTime,
       "hubResetAction": hubResetAction,
       "hubAFS": hubAFS,
       "card": card,
       "ensupStaticNetConfig": ensupStaticNetConfig,
       "ensupDynamicNetStatus": ensupDynamicNetStatus,
       "ensupNetBridgeSlot": ensupNetBridgeSlot,
       "ensupCarrierCounter": ensupCarrierCounter,
       "ensupNetUtilization": ensupNetUtilization,
       "ensupNetUtilThreshold": ensupNetUtilThreshold,
       "a1gTable": a1gTable,
       "a1gEntry": a1gEntry,
       "a1gSlotId": a1gSlotId,
       "a1gPorts": a1gPorts,
       "a1gOperStatus": a1gOperStatus,
       "a1gTempStatus": a1gTempStatus,
       "a1gEthBusAdmAction": a1gEthBusAdmAction,
       "a1gEthBusMgmtStatus": a1gEthBusMgmtStatus,
       "a1gNetMgmtBusOperStatus": a1gNetMgmtBusOperStatus,
       "a1gProductType": a1gProductType,
       "a1gUpTime": a1gUpTime,
       "a1gResets": a1gResets,
       "a1gResetAction": a1gResetAction,
       "configTable": configTable,
       "configEntry": configEntry,
       "configSlotId": configSlotId,
       "configFaultActionType": configFaultActionType,
       "configRetries": configRetries,
       "configPowerUpMode": configPowerUpMode,
       "a1imTable": a1imTable,
       "a1imEntry": a1imEntry,
       "a1imSlotId": a1imSlotId,
       "a1imMACAddr": a1imMACAddr,
       "a1imPodDiagnosticMsg": a1imPodDiagnosticMsg,
       "a1imModuleFault": a1imModuleFault,
       "a1imHaltReason": a1imHaltReason,
       "a1imDebugRegisters": a1imDebugRegisters,
       "tplTable": tplTable,
       "tplEntry": tplEntry,
       "tplSlotId": tplSlotId,
       "tplIPAddress": tplIPAddress,
       "tplNiuName": tplNiuName,
       "tplProtocolType": tplProtocolType,
       "tplSuprvPollStatus": tplSuprvPollStatus,
       "imenEthBusTable": imenEthBusTable,
       "imenEthBusEntry": imenEthBusEntry,
       "imenSlotId": imenSlotId,
       "imenTransmitPkts": imenTransmitPkts,
       "imenReceivePkts": imenReceivePkts,
       "imenCRCErrors": imenCRCErrors,
       "imenCollisions": imenCollisions,
       "brdgTable": brdgTable,
       "brdgEntry": brdgEntry,
       "brdgSlotId": brdgSlotId,
       "brdgIfId": brdgIfId,
       "brdgIfType": brdgIfType,
       "brdgIfFault": brdgIfFault,
       "brdgIfMACAddr": brdgIfMACAddr,
       "ecTable": ecTable,
       "ecEntry": ecEntry,
       "ecSlotId": ecSlotId,
       "ecCarrierCounter": ecCarrierCounter,
       "ecFanStatus": ecFanStatus,
       "netTable": netTable,
       "netEntry": netEntry,
       "netSlotId": netSlotId,
       "netBackboneType": netBackboneType,
       "netFault": netFault,
       "netBackboneStatus": netBackboneStatus,
       "brnTable": brnTable,
       "brnEntry": brnEntry,
       "brnSlotId": brnSlotId,
       "brnIfId": brnIfId,
       "brnIfEthDLCStatus": brnIfEthDLCStatus,
       "brnCarrierCounter": brnCarrierCounter,
       "brnCarrierTimeInterval": brnCarrierTimeInterval,
       "brnTransmitPkts": brnTransmitPkts,
       "brnReceivePkts": brnReceivePkts,
       "brnCRCErrors": brnCRCErrors,
       "brnCollisions": brnCollisions,
       "brnPktsAborted16Colls": brnPktsAborted16Colls,
       "brnShortPkts": brnShortPkts,
       "brnAlignmentErrors": brnAlignmentErrors,
       "brnOverflows": brnOverflows,
       "brnUnderflows": brnUnderflows,
       "tr16cTable": tr16cTable,
       "tr16cEntry": tr16cEntry,
       "tr16cSlotId": tr16cSlotId,
       "tr16cTier": tr16cTier,
       "tr16cOperState": tr16cOperState,
       "tr16cRingNumber": tr16cRingNumber,
       "tr16cManufacturerID": tr16cManufacturerID,
       "tr16cManufacturerProductID": tr16cManufacturerProductID,
       "tr16cManufProductVers": tr16cManufProductVers,
       "tr16cActiveMonitorPortNumber": tr16cActiveMonitorPortNumber,
       "tr16cRingSpeed": tr16cRingSpeed,
       "tr16cLLCFrames": tr16cLLCFrames,
       "tr16cMACFrames": tr16cMACFrames,
       "tr16cOctets": tr16cOctets,
       "tr16cMulticastFrames": tr16cMulticastFrames,
       "tr16cBroadcastFrames": tr16cBroadcastFrames,
       "tr16cFrameCheckSequences": tr16cFrameCheckSequences,
       "tr16cAutoPartitionEnableTimer": tr16cAutoPartitionEnableTimer,
       "tr16cAutoPartitionHoldTimer": tr16cAutoPartitionHoldTimer,
       "tr16cAutoPartitionRetries": tr16cAutoPartitionRetries,
       "tr16cLLCSamples": tr16cLLCSamples,
       "tr16cMACSamples": tr16cMACSamples,
       "tr16cUpTimeMS": tr16cUpTimeMS,
       "tr16cResetDurableUserAttrs": tr16cResetDurableUserAttrs,
       "tr16reTable": tr16reTable,
       "tr16reEntry": tr16reEntry,
       "tr16reSlotId": tr16reSlotId,
       "tr16reLostFrames": tr16reLostFrames,
       "tr16reRcvCongestionErrors": tr16reRcvCongestionErrors,
       "tr16reFrequencyErrors": tr16reFrequencyErrors,
       "tr16reFrameCopyErrors": tr16reFrameCopyErrors,
       "tr16reTokenErrors": tr16reTokenErrors,
       "port": port,
       "ecpTable": ecpTable,
       "ecpEntry": ecpEntry,
       "ecpSlotId": ecpSlotId,
       "ecpPortId": ecpPortId,
       "ecpMgmtStatus": ecpMgmtStatus,
       "ecpAdmAction": ecpAdmAction,
       "ecpCarrierCounter": ecpCarrierCounter,
       "ecfpTable": ecfpTable,
       "ecfpEntry": ecfpEntry,
       "ecfpSlotId": ecfpSlotId,
       "ecfpPortId": ecfpPortId,
       "ecfpMACAddr": ecfpMACAddr,
       "ecfpTxIdleTime": ecfpTxIdleTime,
       "ec10btpTable": ec10btpTable,
       "ec10btpEntry": ec10btpEntry,
       "ec10btpSlotId": ec10btpSlotId,
       "ec10btpPortId": ec10btpPortId,
       "ec10btpLinkTestStatus": ec10btpLinkTestStatus,
       "ec10btpLinkTestAction": ec10btpLinkTestAction,
       "trcpTable": trcpTable,
       "trcpEntry": trcpEntry,
       "trcpSlotId": trcpSlotId,
       "trcpPortId": trcpPortId,
       "trcpAdmAction": trcpAdmAction,
       "trcpOperStatus": trcpOperStatus,
       "tr16p1Table": tr16p1Table,
       "tr16p1Entry": tr16p1Entry,
       "tr16p1SlotId": tr16p1SlotId,
       "tr16p1PortId": tr16p1PortId,
       "tr16p1InsertionState": tr16p1InsertionState,
       "tr16p1AllowInsert": tr16p1AllowInsert,
       "tr16p1ForceInsert": tr16p1ForceInsert,
       "tr16p1PhantomState": tr16p1PhantomState,
       "tr16p2Table": tr16p2Table,
       "tr16p2Entry": tr16p2Entry,
       "tr16p2SlotId": tr16p2SlotId,
       "tr16p2PortId": tr16p2PortId,
       "tr16p2OperState": tr16p2OperState,
       "tr16p2BeaconDetects": tr16p2BeaconDetects,
       "tr16p2LastSourceAddress": tr16p2LastSourceAddress,
       "tr16p2LLCFramesTransmitted": tr16p2LLCFramesTransmitted,
       "tr16p2LLCFramesReceived": tr16p2LLCFramesReceived,
       "tr16p2MACFramesTransmitted": tr16p2MACFramesTransmitted,
       "tr16p2MACFramesReceived": tr16p2MACFramesReceived,
       "tr16p2OctetsTransmitted": tr16p2OctetsTransmitted,
       "tr16p2OctetsReceived": tr16p2OctetsReceived,
       "tr16p2MulticastsTransmitted": tr16p2MulticastsTransmitted,
       "tr16p2BroadcastsTransmitted": tr16p2BroadcastsTransmitted,
       "tr16p2FCSErrorsTransmitted": tr16p2FCSErrorsTransmitted,
       "tr16p2FCSErrorsReceived": tr16p2FCSErrorsReceived,
       "tr16p2LastSourceAddressUptime": tr16p2LastSourceAddressUptime,
       "tr16p3Table": tr16p3Table,
       "tr16p3Entry": tr16p3Entry,
       "tr16p3SlotId": tr16p3SlotId,
       "tr16p3PortId": tr16p3PortId,
       "tr16p3LineErrors": tr16p3LineErrors,
       "tr16p3InternalErrors": tr16p3InternalErrors,
       "tr16p3Burst5Errors": tr16p3Burst5Errors,
       "tr16p3AcErrors": tr16p3AcErrors,
       "tr16p3AbortDelimiters": tr16p3AbortDelimiters,
       "ubTrapAttrs": ubTrapAttrs,
       "trapInstanceId": trapInstanceId,
       "trapSlotId": trapSlotId,
       "trapProductType": trapProductType,
       "trapPortID": trapPortID,
       "trapPortCount": trapPortCount,
       "trapPortMask": trapPortMask,
       "ubSystem": ubSystem,
       "ubSecurity": ubSecurity,
       "trpsbTable": trpsbTable,
       "trpsbEntry": trpsbEntry,
       "trpsbIpAddress": trpsbIpAddress,
       "trpsbCommunity": trpsbCommunity,
       "trpsbActions": trpsbActions}
)
