# SNMP MIB module (RADWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:12 2024
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class RsIfType(Integer32):
    """Custom type RsIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(23,
              32,
              500,
              1000,
              1001,
              1002,
              1003,
              1010,
              1011,
              1100)
        )
    )
    namedValues = NamedValues(
        *(("b1isdn", 1010),
          ("b2isdn", 1011),
          ("backup", 1002),
          ("cod", 1001),
          ("fr1490", 1003),
          ("frameRelay", 32),
          ("ppp", 23),
          ("rndWan", 1000),
          ("unknown", 1100),
          ("virtualNet", 500))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rnd_ObjectIdentity = ObjectIdentity
rnd = _Rnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89)
)
_RndMng_ObjectIdentity = ObjectIdentity
rndMng = _RndMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 1)
)


class _RndSysId_Type(Integer32):
    """Custom type rndSysId based on Integer32"""
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
              62)
        )
    )
    namedValues = NamedValues(
        *(("apollo", 45),
          ("armon", 22),
          ("ceb", 2),
          ("ceblb", 3),
          ("elX", 30),
          ("fccs1004", 23),
          ("fccs1012", 24),
          ("ftc", 21),
          ("gatelinx", 17),
          ("ielb", 11),
          ("iprouter", 10),
          ("itlb", 16),
          ("leb", 12),
          ("lre", 35),
          ("ltb", 8),
          ("lte", 9),
          ("mlm", 42),
          ("mrt", 32),
          ("ogRanTR", 19),
          ("ogRubE", 28),
          ("ogRubT", 29),
          ("ogSrubET", 33),
          ("ogvan", 26),
          ("openGate12", 13),
          ("openGate2", 18),
          ("openGate4", 14),
          ("prt", 41),
          ("prt11", 43),
          ("quickOffice", 44),
          ("radware", 62),
          ("ran", 15),
          ("rdapter", 25),
          ("reb", 1),
          ("rebsx", 6),
          ("rtb", 7),
          ("serverDispatcher2", 38),
          ("serverDispatcher2Fast", 40),
          ("serverDispatcher4", 37),
          ("stc", 20),
          ("vGate2", 36),
          ("vGate2Fast", 39),
          ("vGate4", 31),
          ("vanXS", 34),
          ("wanGate", 27),
          ("xeb", 4),
          ("xeb1", 5))
    )


_RndSysId_Type.__name__ = "Integer32"
_RndSysId_Object = MibScalar
rndSysId = _RndSysId_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 1),
    _RndSysId_Type()
)
rndSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndSysId.setStatus("mandatory")


class _RndAction_Type(Integer32):
    """Custom type rndAction based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("backupArpTab", 16),
          ("backupIPRoutingTab", 13),
          ("backupIPXRipTab", 17),
          ("backupIPXSAPTab", 18),
          ("backupLanTab", 15),
          ("backupNetworkTab", 14),
          ("backupSPFRoutingTab", 12),
          ("deleteArpTab", 8),
          ("deleteLanTab", 7),
          ("deleteNetworkTab", 3),
          ("deleteRouteTab", 10),
          ("deleteRoutingTab", 5),
          ("deleteZeroHopRoutingAllocTab", 21),
          ("eraseCDB", 20),
          ("reset", 1),
          ("resetCDB", 19),
          ("sendArpTab", 9),
          ("sendLanTab", 6),
          ("sendNetworkTab", 2),
          ("sendRouteTab", 11),
          ("sendRoutingTab", 4))
    )


_RndAction_Type.__name__ = "Integer32"
_RndAction_Object = MibScalar
rndAction = _RndAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 2),
    _RndAction_Type()
)
rndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAction.setStatus("mandatory")
_RndFileName_Type = OctetString
_RndFileName_Object = MibScalar
rndFileName = _RndFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 1, 3),
    _RndFileName_Type()
)
rndFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFileName.setStatus("mandatory")
_RndDeviceParams_ObjectIdentity = ObjectIdentity
rndDeviceParams = _RndDeviceParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2)
)


class _RndBridgeType_Type(Integer32):
    """Custom type rndBridgeType based on Integer32"""
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
              48)
        )
    )
    namedValues = NamedValues(
        *(("ceb", 2),
          ("ceblb", 3),
          ("ete", 12),
          ("gatelinx", 36),
          ("ielb", 30),
          ("itlb", 35),
          ("leb", 31),
          ("lre", 46),
          ("ltb", 8),
          ("mrt", 47),
          ("ogRanTR", 38),
          ("ogRubE", 42),
          ("ogRubT", 43),
          ("ogVan", 40),
          ("openGate12", 32),
          ("openGate2", 37),
          ("openGate4", 33),
          ("ran", 34),
          ("rdapter", 39),
          ("reb", 1),
          ("rebsx", 6),
          ("rete", 13),
          ("rtb", 7),
          ("rtre", 10),
          ("tre", 9),
          ("vGate2", 48),
          ("vGate4", 45),
          ("wanGate", 41),
          ("wanGateI", 44),
          ("xeb", 4),
          ("xeb1", 5),
          ("xtb", 11))
    )


_RndBridgeType_Type.__name__ = "Integer32"
_RndBridgeType_Object = MibScalar
rndBridgeType = _RndBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 1),
    _RndBridgeType_Type()
)
rndBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBridgeType.setStatus("mandatory")
_RndInactiveArpTimeOut_Type = Integer32
_RndInactiveArpTimeOut_Object = MibScalar
rndInactiveArpTimeOut = _RndInactiveArpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 2),
    _RndInactiveArpTimeOut_Type()
)
rndInactiveArpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndInactiveArpTimeOut.setStatus("mandatory")
_RndBridgeAlarm_ObjectIdentity = ObjectIdentity
rndBridgeAlarm = _RndBridgeAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 3)
)
_RndErrorDesc_Type = DisplayString
_RndErrorDesc_Object = MibScalar
rndErrorDesc = _RndErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 1),
    _RndErrorDesc_Type()
)
rndErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorDesc.setStatus("mandatory")
_RndErrorSeverity_Type = Integer32
_RndErrorSeverity_Object = MibScalar
rndErrorSeverity = _RndErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 2),
    _RndErrorSeverity_Type()
)
rndErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorSeverity.setStatus("mandatory")
_RndBrgVersion_Type = DisplayString
_RndBrgVersion_Object = MibScalar
rndBrgVersion = _RndBrgVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 4),
    _RndBrgVersion_Type()
)
rndBrgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBrgVersion.setStatus("mandatory")
_RndBrgFeatures_Type = OctetString
_RndBrgFeatures_Object = MibScalar
rndBrgFeatures = _RndBrgFeatures_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 5),
    _RndBrgFeatures_Type()
)
rndBrgFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBrgFeatures.setStatus("mandatory")
_RndBrgLicense_Type = OctetString
_RndBrgLicense_Object = MibScalar
rndBrgLicense = _RndBrgLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 6),
    _RndBrgLicense_Type()
)
rndBrgLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBrgLicense.setStatus("mandatory")
_RndIpHost_ObjectIdentity = ObjectIdentity
rndIpHost = _RndIpHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 7)
)


class _RndICMPTransmitionEnable_Type(Integer32):
    """Custom type rndICMPTransmitionEnable based on Integer32"""
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


_RndICMPTransmitionEnable_Type.__name__ = "Integer32"
_RndICMPTransmitionEnable_Object = MibScalar
rndICMPTransmitionEnable = _RndICMPTransmitionEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 1),
    _RndICMPTransmitionEnable_Type()
)
rndICMPTransmitionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndICMPTransmitionEnable.setStatus("mandatory")
_RndCommunityTable_Object = MibTable
rndCommunityTable = _RndCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2)
)
if mibBuilder.loadTexts:
    rndCommunityTable.setStatus("mandatory")
_RndCommunityEntry_Object = MibTableRow
rndCommunityEntry = _RndCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1)
)
rndCommunityEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndCommunityMngStationAddr"),
    (1, "RADWARE-MIB", "rndCommunityString"),
)
if mibBuilder.loadTexts:
    rndCommunityEntry.setStatus("mandatory")
_RndCommunityMngStationAddr_Type = IpAddress
_RndCommunityMngStationAddr_Object = MibTableColumn
rndCommunityMngStationAddr = _RndCommunityMngStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 1),
    _RndCommunityMngStationAddr_Type()
)
rndCommunityMngStationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityMngStationAddr.setStatus("mandatory")


class _RndCommunityString_Type(DisplayString):
    """Custom type rndCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndCommunityString_Type.__name__ = "DisplayString"
_RndCommunityString_Object = MibTableColumn
rndCommunityString = _RndCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 2),
    _RndCommunityString_Type()
)
rndCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityString.setStatus("mandatory")


class _RndCommunityAccess_Type(Integer32):
    """Custom type rndCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("super", 3))
    )


_RndCommunityAccess_Type.__name__ = "Integer32"
_RndCommunityAccess_Object = MibTableColumn
rndCommunityAccess = _RndCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 3),
    _RndCommunityAccess_Type()
)
rndCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityAccess.setStatus("mandatory")


class _RndCommunityTrapsEnable_Type(Integer32):
    """Custom type rndCommunityTrapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapsDisable", 2),
          ("trapsEnable", 1))
    )


_RndCommunityTrapsEnable_Type.__name__ = "Integer32"
_RndCommunityTrapsEnable_Object = MibTableColumn
rndCommunityTrapsEnable = _RndCommunityTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 4),
    _RndCommunityTrapsEnable_Type()
)
rndCommunityTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityTrapsEnable.setStatus("mandatory")


class _RndCommunityStatus_Type(Integer32):
    """Custom type rndCommunityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("invalid", 2))
    )


_RndCommunityStatus_Type.__name__ = "Integer32"
_RndCommunityStatus_Object = MibTableColumn
rndCommunityStatus = _RndCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 5),
    _RndCommunityStatus_Type()
)
rndCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndCommunityStatus.setStatus("mandatory")


class _RndManagedTime_Type(DisplayString):
    """Custom type rndManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RndManagedTime_Type.__name__ = "DisplayString"
_RndManagedTime_Object = MibScalar
rndManagedTime = _RndManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 8),
    _RndManagedTime_Type()
)
rndManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedTime.setStatus("mandatory")


class _RndManagedDate_Type(DisplayString):
    """Custom type rndManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 8),
    )


_RndManagedDate_Type.__name__ = "DisplayString"
_RndManagedDate_Object = MibScalar
rndManagedDate = _RndManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 9),
    _RndManagedDate_Type()
)
rndManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedDate.setStatus("mandatory")
_GenGroup_ObjectIdentity = ObjectIdentity
genGroup = _GenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 11)
)
_GenGroupHWVersion_Type = DisplayString
_GenGroupHWVersion_Object = MibScalar
genGroupHWVersion = _GenGroupHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 1),
    _GenGroupHWVersion_Type()
)
genGroupHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWVersion.setStatus("mandatory")


class _GenGroupConfigurationSymbol_Type(DisplayString):
    """Custom type genGroupConfigurationSymbol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GenGroupConfigurationSymbol_Type.__name__ = "DisplayString"
_GenGroupConfigurationSymbol_Object = MibScalar
genGroupConfigurationSymbol = _GenGroupConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 2),
    _GenGroupConfigurationSymbol_Type()
)
genGroupConfigurationSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupConfigurationSymbol.setStatus("mandatory")


class _GenGroupHWStatus_Type(Integer32):
    """Custom type genGroupHWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hardwareProblems", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_GenGroupHWStatus_Type.__name__ = "Integer32"
_GenGroupHWStatus_Object = MibScalar
genGroupHWStatus = _GenGroupHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 3),
    _GenGroupHWStatus_Type()
)
genGroupHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWStatus.setStatus("mandatory")
_RndInterface_ObjectIdentity = ObjectIdentity
rndInterface = _RndInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 4)
)
_RndIfTable_Object = MibTable
rndIfTable = _RndIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1)
)
if mibBuilder.loadTexts:
    rndIfTable.setStatus("mandatory")
_RndIfEntry_Object = MibTableRow
rndIfEntry = _RndIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1)
)
rndIfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndIfIndex"),
)
if mibBuilder.loadTexts:
    rndIfEntry.setStatus("mandatory")
_RndIfIndex_Type = Integer32
_RndIfIndex_Object = MibTableColumn
rndIfIndex = _RndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 1),
    _RndIfIndex_Type()
)
rndIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfIndex.setStatus("mandatory")
_RndIfBoardNum_Type = Integer32
_RndIfBoardNum_Object = MibTableColumn
rndIfBoardNum = _RndIfBoardNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 2),
    _RndIfBoardNum_Type()
)
rndIfBoardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfBoardNum.setStatus("mandatory")
_RndIfNetAddress_Type = IpAddress
_RndIfNetAddress_Object = MibTableColumn
rndIfNetAddress = _RndIfNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 3),
    _RndIfNetAddress_Type()
)
rndIfNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfNetAddress.setStatus("mandatory")


class _RndIfStatus_Type(Integer32):
    """Custom type rndIfStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("channelLoopback", 7),
          ("connctFault", 4),
          ("ok", 1),
          ("okMultiBrg", 3),
          ("okSingleBrg", 2),
          ("rxClockFault", 8),
          ("rxFault", 5),
          ("t1Alarm", 9),
          ("txFault", 6))
    )


_RndIfStatus_Type.__name__ = "Integer32"
_RndIfStatus_Object = MibTableColumn
rndIfStatus = _RndIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 4),
    _RndIfStatus_Type()
)
rndIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfStatus.setStatus("mandatory")


class _RndIfClockType_Type(Integer32):
    """Custom type rndIfClockType based on Integer32"""
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
        *(("external", 1),
          ("g703", 4),
          ("internal", 2),
          ("t1", 3))
    )


_RndIfClockType_Type.__name__ = "Integer32"
_RndIfClockType_Object = MibTableColumn
rndIfClockType = _RndIfClockType_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 5),
    _RndIfClockType_Type()
)
rndIfClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfClockType.setStatus("mandatory")
_RndIfBaudRate_Type = Integer32
_RndIfBaudRate_Object = MibTableColumn
rndIfBaudRate = _RndIfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 6),
    _RndIfBaudRate_Type()
)
rndIfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfBaudRate.setStatus("mandatory")
_RndIfCost_Type = Integer32
_RndIfCost_Object = MibTableColumn
rndIfCost = _RndIfCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 7),
    _RndIfCost_Type()
)
rndIfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfCost.setStatus("mandatory")


class _RndIfCompression_Type(Integer32):
    """Custom type rndIfCompression based on Integer32"""
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


_RndIfCompression_Type.__name__ = "Integer32"
_RndIfCompression_Object = MibTableColumn
rndIfCompression = _RndIfCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 8),
    _RndIfCompression_Type()
)
rndIfCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfCompression.setStatus("mandatory")


class _RndIfCompressionStatus_Type(Integer32):
    """Custom type rndIfCompressionStatus based on Integer32"""
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
        *(("active", 2),
          ("disable", 4),
          ("not-active", 3),
          ("not-inserted", 1))
    )


_RndIfCompressionStatus_Type.__name__ = "Integer32"
_RndIfCompressionStatus_Object = MibTableColumn
rndIfCompressionStatus = _RndIfCompressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 9),
    _RndIfCompressionStatus_Type()
)
rndIfCompressionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfCompressionStatus.setStatus("mandatory")
_RndIfCompressionRate_Type = Integer32
_RndIfCompressionRate_Object = MibTableColumn
rndIfCompressionRate = _RndIfCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 10),
    _RndIfCompressionRate_Type()
)
rndIfCompressionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfCompressionRate.setStatus("mandatory")


class _RndIfLATCompression_Type(Integer32):
    """Custom type rndIfLATCompression based on Integer32"""
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


_RndIfLATCompression_Type.__name__ = "Integer32"
_RndIfLATCompression_Object = MibTableColumn
rndIfLATCompression = _RndIfLATCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 11),
    _RndIfLATCompression_Type()
)
rndIfLATCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfLATCompression.setStatus("mandatory")


class _RndIfCompressionType_Type(Integer32):
    """Custom type rndIfCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highSpeed", 3),
          ("lowSpeed", 2),
          ("none", 1))
    )


_RndIfCompressionType_Type.__name__ = "Integer32"
_RndIfCompressionType_Object = MibTableColumn
rndIfCompressionType = _RndIfCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 12),
    _RndIfCompressionType_Type()
)
rndIfCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIfCompressionType.setStatus("mandatory")


class _RndIfFilterMode_Type(Integer32):
    """Custom type rndIfFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destinationOnly", 1),
          ("none", 3),
          ("sourceAndDestination", 2))
    )


_RndIfFilterMode_Type.__name__ = "Integer32"
_RndIfFilterMode_Object = MibTableColumn
rndIfFilterMode = _RndIfFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 13),
    _RndIfFilterMode_Type()
)
rndIfFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfFilterMode.setStatus("mandatory")


class _RndIfChannelType_Type(Integer32):
    """Custom type rndIfChannelType based on Integer32"""
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
        *(("dialBackup", 5),
          ("frameRelay1490", 9),
          ("frameRelay1490CAR", 10),
          ("frameRelayCAR", 11),
          ("lan", 7),
          ("ogRanPort", 2),
          ("ppp", 12),
          ("routerToBridge", 3),
          ("snar", 6),
          ("spsFramRelay", 4),
          ("spsX25", 8),
          ("wanChannel", 1))
    )


_RndIfChannelType_Type.__name__ = "Integer32"
_RndIfChannelType_Object = MibTableColumn
rndIfChannelType = _RndIfChannelType_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 14),
    _RndIfChannelType_Type()
)
rndIfChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfChannelType.setStatus("mandatory")


class _RndIfBridge_Type(Integer32):
    """Custom type rndIfBridge based on Integer32"""
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


_RndIfBridge_Type.__name__ = "Integer32"
_RndIfBridge_Object = MibTableColumn
rndIfBridge = _RndIfBridge_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 15),
    _RndIfBridge_Type()
)
rndIfBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIfBridge.setStatus("mandatory")


class _RndHighPriorityIf_Type(Integer32):
    """Custom type rndHighPriorityIf based on Integer32"""
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


_RndHighPriorityIf_Type.__name__ = "Integer32"
_RndHighPriorityIf_Object = MibTableColumn
rndHighPriorityIf = _RndHighPriorityIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 16),
    _RndHighPriorityIf_Type()
)
rndHighPriorityIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndHighPriorityIf.setStatus("mandatory")


class _RndWanHeader_Type(Integer32):
    """Custom type rndWanHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("short", 2))
    )


_RndWanHeader_Type.__name__ = "Integer32"
_RndWanHeader_Object = MibTableColumn
rndWanHeader = _RndWanHeader_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 17),
    _RndWanHeader_Type()
)
rndWanHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndWanHeader.setStatus("mandatory")


class _RndDuplexMode_Type(Integer32):
    """Custom type rndDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_RndDuplexMode_Type.__name__ = "Integer32"
_RndDuplexMode_Object = MibTableColumn
rndDuplexMode = _RndDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 4, 1, 1, 18),
    _RndDuplexMode_Type()
)
rndDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDuplexMode.setStatus("mandatory")
_RndIPX_ObjectIdentity = ObjectIdentity
rndIPX = _RndIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12)
)
_RndFACS_ObjectIdentity = ObjectIdentity
rndFACS = _RndFACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 16)
)


class _RndFACSDefaultAction_Type(Integer32):
    """Custom type rndFACSDefaultAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              129)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("blockAndReport", 129),
          ("disable", 4),
          ("enable", 3),
          ("forward", 2))
    )


_RndFACSDefaultAction_Type.__name__ = "Integer32"
_RndFACSDefaultAction_Object = MibScalar
rndFACSDefaultAction = _RndFACSDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 1),
    _RndFACSDefaultAction_Type()
)
rndFACSDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSDefaultAction.setStatus("mandatory")
_RndFACSActTable_Object = MibTable
rndFACSActTable = _RndFACSActTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2)
)
if mibBuilder.loadTexts:
    rndFACSActTable.setStatus("mandatory")
_RndFACSActEntry_Object = MibTableRow
rndFACSActEntry = _RndFACSActEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1)
)
rndFACSActEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndFACSActType"),
    (0, "RADWARE-MIB", "rndFACSActIfIndex"),
)
if mibBuilder.loadTexts:
    rndFACSActEntry.setStatus("mandatory")


class _RndFACSActType_Type(Integer32):
    """Custom type rndFACSActType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activeDB", 4),
          ("rx", 2),
          ("tempDB", 5),
          ("tx", 1))
    )


_RndFACSActType_Type.__name__ = "Integer32"
_RndFACSActType_Object = MibTableColumn
rndFACSActType = _RndFACSActType_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1, 1),
    _RndFACSActType_Type()
)
rndFACSActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSActType.setStatus("mandatory")
_RndFACSActIfIndex_Type = Integer32
_RndFACSActIfIndex_Object = MibTableColumn
rndFACSActIfIndex = _RndFACSActIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1, 2),
    _RndFACSActIfIndex_Type()
)
rndFACSActIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSActIfIndex.setStatus("mandatory")


class _RndFACSAction_Type(Integer32):
    """Custom type rndFACSAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("backupBrg", 13),
          ("backupIP", 10),
          ("backupIPX", 12),
          ("eraseBrg", 5),
          ("eraseDECnet", 3),
          ("eraseIP", 2),
          ("eraseIPX", 4),
          ("none", 1),
          ("replaceBrg", 9),
          ("replaceIP", 6),
          ("replaceIPX", 8))
    )


_RndFACSAction_Type.__name__ = "Integer32"
_RndFACSAction_Object = MibTableColumn
rndFACSAction = _RndFACSAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 2, 1, 3),
    _RndFACSAction_Type()
)
rndFACSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSAction.setStatus("mandatory")
_RndFACSTable_Object = MibTable
rndFACSTable = _RndFACSTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3)
)
if mibBuilder.loadTexts:
    rndFACSTable.setStatus("mandatory")
_RndFACSEntry_Object = MibTableRow
rndFACSEntry = _RndFACSEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1)
)
rndFACSEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndFACSIfIndex"),
    (0, "RADWARE-MIB", "rndFACSProtocolType"),
    (0, "RADWARE-MIB", "rndFACSType"),
    (0, "RADWARE-MIB", "rndFACSIndex"),
)
if mibBuilder.loadTexts:
    rndFACSEntry.setStatus("mandatory")
_RndFACSIfIndex_Type = Integer32
_RndFACSIfIndex_Object = MibTableColumn
rndFACSIfIndex = _RndFACSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 1),
    _RndFACSIfIndex_Type()
)
rndFACSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSIfIndex.setStatus("mandatory")


class _RndFACSProtocolType_Type(Integer32):
    """Custom type rndFACSProtocolType based on Integer32"""
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
        *(("bridge", 4),
          ("dec", 3),
          ("ip", 1),
          ("ipx", 2))
    )


_RndFACSProtocolType_Type.__name__ = "Integer32"
_RndFACSProtocolType_Object = MibTableColumn
rndFACSProtocolType = _RndFACSProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 2),
    _RndFACSProtocolType_Type()
)
rndFACSProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSProtocolType.setStatus("mandatory")


class _RndFACSType_Type(Integer32):
    """Custom type rndFACSType based on Integer32"""
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
        *(("activeDB", 4),
          ("cod", 3),
          ("rx", 2),
          ("tempDB", 5),
          ("tx", 1))
    )


_RndFACSType_Type.__name__ = "Integer32"
_RndFACSType_Object = MibTableColumn
rndFACSType = _RndFACSType_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 3),
    _RndFACSType_Type()
)
rndFACSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSType.setStatus("mandatory")
_RndFACSIndex_Type = Integer32
_RndFACSIndex_Object = MibTableColumn
rndFACSIndex = _RndFACSIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 4),
    _RndFACSIndex_Type()
)
rndFACSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndFACSIndex.setStatus("mandatory")
_RndFACSSrcAdd_Type = OctetString
_RndFACSSrcAdd_Object = MibTableColumn
rndFACSSrcAdd = _RndFACSSrcAdd_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 5),
    _RndFACSSrcAdd_Type()
)
rndFACSSrcAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSSrcAdd.setStatus("mandatory")
_RndFACSSrcAddMask_Type = OctetString
_RndFACSSrcAddMask_Object = MibTableColumn
rndFACSSrcAddMask = _RndFACSSrcAddMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 6),
    _RndFACSSrcAddMask_Type()
)
rndFACSSrcAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSSrcAddMask.setStatus("mandatory")
_RndFACSDesAdd_Type = OctetString
_RndFACSDesAdd_Object = MibTableColumn
rndFACSDesAdd = _RndFACSDesAdd_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 7),
    _RndFACSDesAdd_Type()
)
rndFACSDesAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSDesAdd.setStatus("mandatory")
_RndFACSDesAddMask_Type = OctetString
_RndFACSDesAddMask_Object = MibTableColumn
rndFACSDesAddMask = _RndFACSDesAddMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 8),
    _RndFACSDesAddMask_Type()
)
rndFACSDesAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSDesAddMask.setStatus("mandatory")


class _RndFACSOperation_Type(Integer32):
    """Custom type rndFACSOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              129)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("blockAndReport", 129),
          ("blockZHRP", 5),
          ("deny", 4),
          ("forward", 2),
          ("permit", 3))
    )


_RndFACSOperation_Type.__name__ = "Integer32"
_RndFACSOperation_Object = MibTableColumn
rndFACSOperation = _RndFACSOperation_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 9),
    _RndFACSOperation_Type()
)
rndFACSOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSOperation.setStatus("mandatory")


class _RndFACSNetFiltering_Type(Integer32):
    """Custom type rndFACSNetFiltering based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("arp", 3),
          ("decnet", 8),
          ("icmp", 4),
          ("ip", 5),
          ("ipx", 9),
          ("l2multicast", 2),
          ("none", 1),
          ("tcp", 7),
          ("udp", 6))
    )


_RndFACSNetFiltering_Type.__name__ = "Integer32"
_RndFACSNetFiltering_Object = MibTableColumn
rndFACSNetFiltering = _RndFACSNetFiltering_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 10),
    _RndFACSNetFiltering_Type()
)
rndFACSNetFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSNetFiltering.setStatus("mandatory")
_RndFACSSoketNum_Type = Integer32
_RndFACSSoketNum_Object = MibTableColumn
rndFACSSoketNum = _RndFACSSoketNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 11),
    _RndFACSSoketNum_Type()
)
rndFACSSoketNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSSoketNum.setStatus("mandatory")
_RndFACSMask1Id_Type = Integer32
_RndFACSMask1Id_Object = MibTableColumn
rndFACSMask1Id = _RndFACSMask1Id_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 12),
    _RndFACSMask1Id_Type()
)
rndFACSMask1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSMask1Id.setStatus("mandatory")
_RndFACSMask2Id_Type = Integer32
_RndFACSMask2Id_Object = MibTableColumn
rndFACSMask2Id = _RndFACSMask2Id_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 13),
    _RndFACSMask2Id_Type()
)
rndFACSMask2Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSMask2Id.setStatus("mandatory")


class _RndFACSStatus_Type(Integer32):
    """Custom type rndFACSStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_RndFACSStatus_Type.__name__ = "Integer32"
_RndFACSStatus_Object = MibTableColumn
rndFACSStatus = _RndFACSStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 16, 3, 1, 14),
    _RndFACSStatus_Type()
)
rndFACSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndFACSStatus.setStatus("mandatory")
_RndBootP_ObjectIdentity = ObjectIdentity
rndBootP = _RndBootP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 24)
)


class _RndBootPServerAddress_Type(IpAddress):
    """Custom type rndBootPServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_RndBootPServerAddress_Object = MibScalar
rndBootPServerAddress = _RndBootPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 24, 1),
    _RndBootPServerAddress_Type()
)
rndBootPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPServerAddress.setStatus("mandatory")
_RndBootPRelaySecThreshold_Type = Integer32
_RndBootPRelaySecThreshold_Object = MibScalar
rndBootPRelaySecThreshold = _RndBootPRelaySecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 24, 2),
    _RndBootPRelaySecThreshold_Type()
)
rndBootPRelaySecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBootPRelaySecThreshold.setStatus("mandatory")
_IpSpec_ObjectIdentity = ObjectIdentity
ipSpec = _IpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26)
)
_RsIpAddrTable_Object = MibTable
rsIpAddrTable = _RsIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1)
)
if mibBuilder.loadTexts:
    rsIpAddrTable.setStatus("mandatory")
_RsIpAddrEntry_Object = MibTableRow
rsIpAddrEntry = _RsIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1)
)
rsIpAddrEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    rsIpAddrEntry.setStatus("mandatory")
_RsIpAdEntAddr_Type = IpAddress
_RsIpAdEntAddr_Object = MibTableColumn
rsIpAdEntAddr = _RsIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 1),
    _RsIpAdEntAddr_Type()
)
rsIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntAddr.setStatus("mandatory")
_RsIpAdEntIfIndex_Type = Integer32
_RsIpAdEntIfIndex_Object = MibTableColumn
rsIpAdEntIfIndex = _RsIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 2),
    _RsIpAdEntIfIndex_Type()
)
rsIpAdEntIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntIfIndex.setStatus("mandatory")
_RsIpAdEntNetMask_Type = IpAddress
_RsIpAdEntNetMask_Object = MibTableColumn
rsIpAdEntNetMask = _RsIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 3),
    _RsIpAdEntNetMask_Type()
)
rsIpAdEntNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntNetMask.setStatus("mandatory")


class _RsIpAdEntForwardIpBroadcast_Type(Integer32):
    """Custom type rsIpAdEntForwardIpBroadcast based on Integer32"""
    defaultValue = 1

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


_RsIpAdEntForwardIpBroadcast_Type.__name__ = "Integer32"
_RsIpAdEntForwardIpBroadcast_Object = MibTableColumn
rsIpAdEntForwardIpBroadcast = _RsIpAdEntForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 4),
    _RsIpAdEntForwardIpBroadcast_Type()
)
rsIpAdEntForwardIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntForwardIpBroadcast.setStatus("mandatory")


class _RsIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type rsIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_RsIpAdEntReasmMaxSize_Object = MibTableColumn
rsIpAdEntReasmMaxSize = _RsIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 5),
    _RsIpAdEntReasmMaxSize_Type()
)
rsIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpAdEntReasmMaxSize.setStatus("mandatory")


class _RsIpAdEntStatus_Type(Integer32):
    """Custom type rsIpAdEntStatus based on Integer32"""
    defaultValue = 1

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


_RsIpAdEntStatus_Type.__name__ = "Integer32"
_RsIpAdEntStatus_Object = MibTableColumn
rsIpAdEntStatus = _RsIpAdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 6),
    _RsIpAdEntStatus_Type()
)
rsIpAdEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntStatus.setStatus("mandatory")


class _RsIpAdEntBcastAddr_Type(Integer32):
    """Custom type rsIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RsIpAdEntBcastAddr_Type.__name__ = "Integer32"
_RsIpAdEntBcastAddr_Object = MibTableColumn
rsIpAdEntBcastAddr = _RsIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 7),
    _RsIpAdEntBcastAddr_Type()
)
rsIpAdEntBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntBcastAddr.setStatus("mandatory")
_RsIpAdEntVlanTag_Type = Integer32
_RsIpAdEntVlanTag_Object = MibTableColumn
rsIpAdEntVlanTag = _RsIpAdEntVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 8),
    _RsIpAdEntVlanTag_Type()
)
rsIpAdEntVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntVlanTag.setStatus("mandatory")
_IcmpSpec_ObjectIdentity = ObjectIdentity
icmpSpec = _IcmpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 2)
)


class _RsIcmpGenErrMsgEnable_Type(Integer32):
    """Custom type rsIcmpGenErrMsgEnable based on Integer32"""
    defaultValue = 1

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


_RsIcmpGenErrMsgEnable_Type.__name__ = "Integer32"
_RsIcmpGenErrMsgEnable_Object = MibScalar
rsIcmpGenErrMsgEnable = _RsIcmpGenErrMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 1),
    _RsIcmpGenErrMsgEnable_Type()
)
rsIcmpGenErrMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpGenErrMsgEnable.setStatus("mandatory")
_RsIcmpRdTable_Object = MibTable
rsIcmpRdTable = _RsIcmpRdTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2)
)
if mibBuilder.loadTexts:
    rsIcmpRdTable.setStatus("mandatory")
_RsIcmpRdEntry_Object = MibTableRow
rsIcmpRdEntry = _RsIcmpRdEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1)
)
rsIcmpRdEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIcmpRdIpAddr"),
)
if mibBuilder.loadTexts:
    rsIcmpRdEntry.setStatus("mandatory")
_RsIcmpRdIpAddr_Type = IpAddress
_RsIcmpRdIpAddr_Object = MibTableColumn
rsIcmpRdIpAddr = _RsIcmpRdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 1),
    _RsIcmpRdIpAddr_Type()
)
rsIcmpRdIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIcmpRdIpAddr.setStatus("mandatory")


class _RsIcmpRdIpAdvertAddr_Type(IpAddress):
    """Custom type rsIcmpRdIpAdvertAddr based on IpAddress"""
    defaultHexValue = "E0000001"


_RsIcmpRdIpAdvertAddr_Object = MibTableColumn
rsIcmpRdIpAdvertAddr = _RsIcmpRdIpAdvertAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 2),
    _RsIcmpRdIpAdvertAddr_Type()
)
rsIcmpRdIpAdvertAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdIpAdvertAddr.setStatus("mandatory")


class _RsIcmpRdMaxAdvertInterval_Type(Integer32):
    """Custom type rsIcmpRdMaxAdvertInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_RsIcmpRdMaxAdvertInterval_Type.__name__ = "Integer32"
_RsIcmpRdMaxAdvertInterval_Object = MibTableColumn
rsIcmpRdMaxAdvertInterval = _RsIcmpRdMaxAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 3),
    _RsIcmpRdMaxAdvertInterval_Type()
)
rsIcmpRdMaxAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdMaxAdvertInterval.setStatus("mandatory")


class _RsIcmpRdMinAdvertInterval_Type(Integer32):
    """Custom type rsIcmpRdMinAdvertInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_RsIcmpRdMinAdvertInterval_Type.__name__ = "Integer32"
_RsIcmpRdMinAdvertInterval_Object = MibTableColumn
rsIcmpRdMinAdvertInterval = _RsIcmpRdMinAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 4),
    _RsIcmpRdMinAdvertInterval_Type()
)
rsIcmpRdMinAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdMinAdvertInterval.setStatus("mandatory")


class _RsIcmpRdAdvertLifetime_Type(Integer32):
    """Custom type rsIcmpRdAdvertLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_RsIcmpRdAdvertLifetime_Type.__name__ = "Integer32"
_RsIcmpRdAdvertLifetime_Object = MibTableColumn
rsIcmpRdAdvertLifetime = _RsIcmpRdAdvertLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 5),
    _RsIcmpRdAdvertLifetime_Type()
)
rsIcmpRdAdvertLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdAdvertLifetime.setStatus("mandatory")


class _RsIcmpRdAdvertise_Type(Integer32):
    """Custom type rsIcmpRdAdvertise based on Integer32"""
    defaultValue = 1

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


_RsIcmpRdAdvertise_Type.__name__ = "Integer32"
_RsIcmpRdAdvertise_Object = MibTableColumn
rsIcmpRdAdvertise = _RsIcmpRdAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 6),
    _RsIcmpRdAdvertise_Type()
)
rsIcmpRdAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdAdvertise.setStatus("mandatory")


class _RsIcmpRdPreferenceLevel_Type(Integer32):
    """Custom type rsIcmpRdPreferenceLevel based on Integer32"""
    defaultValue = 0


_RsIcmpRdPreferenceLevel_Object = MibTableColumn
rsIcmpRdPreferenceLevel = _RsIcmpRdPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 7),
    _RsIcmpRdPreferenceLevel_Type()
)
rsIcmpRdPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdPreferenceLevel.setStatus("mandatory")
_RsIcmpRdEntStatus_Type = Integer32
_RsIcmpRdEntStatus_Object = MibTableColumn
rsIcmpRdEntStatus = _RsIcmpRdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 2, 2, 1, 8),
    _RsIcmpRdEntStatus_Type()
)
rsIcmpRdEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIcmpRdEntStatus.setStatus("mandatory")
_Rip2Spec_ObjectIdentity = ObjectIdentity
rip2Spec = _Rip2Spec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 3)
)
_RsRip2IfConfTable_Object = MibTable
rsRip2IfConfTable = _RsRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1)
)
if mibBuilder.loadTexts:
    rsRip2IfConfTable.setStatus("mandatory")
_RsRip2IfConfEntry_Object = MibTableRow
rsRip2IfConfEntry = _RsRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1)
)
rsRip2IfConfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    rsRip2IfConfEntry.setStatus("mandatory")
_RsRip2IfConfAddress_Type = IpAddress
_RsRip2IfConfAddress_Object = MibTableColumn
rsRip2IfConfAddress = _RsRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 1),
    _RsRip2IfConfAddress_Type()
)
rsRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRip2IfConfAddress.setStatus("mandatory")


class _RsRip2IfConfVirtualDis_Type(Integer32):
    """Custom type rsRip2IfConfVirtualDis based on Integer32"""
    defaultValue = 1


_RsRip2IfConfVirtualDis_Object = MibTableColumn
rsRip2IfConfVirtualDis = _RsRip2IfConfVirtualDis_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 2),
    _RsRip2IfConfVirtualDis_Type()
)
rsRip2IfConfVirtualDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRip2IfConfVirtualDis.setStatus("mandatory")


class _RsRip2IfConfAutoSend_Type(Integer32):
    """Custom type rsRip2IfConfAutoSend based on Integer32"""
    defaultValue = 1

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


_RsRip2IfConfAutoSend_Type.__name__ = "Integer32"
_RsRip2IfConfAutoSend_Object = MibTableColumn
rsRip2IfConfAutoSend = _RsRip2IfConfAutoSend_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 3, 1, 1, 3),
    _RsRip2IfConfAutoSend_Type()
)
rsRip2IfConfAutoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRip2IfConfAutoSend.setStatus("mandatory")
_ArpSpec_ObjectIdentity = ObjectIdentity
arpSpec = _ArpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 4)
)
_RsArpDeleteTable_Type = Integer32
_RsArpDeleteTable_Object = MibScalar
rsArpDeleteTable = _RsArpDeleteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 1),
    _RsArpDeleteTable_Type()
)
rsArpDeleteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpDeleteTable.setStatus("mandatory")


class _RsArpInactiveTimeOut_Type(Integer32):
    """Custom type rsArpInactiveTimeOut based on Integer32"""
    defaultValue = 60000


_RsArpInactiveTimeOut_Object = MibScalar
rsArpInactiveTimeOut = _RsArpInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 2),
    _RsArpInactiveTimeOut_Type()
)
rsArpInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpInactiveTimeOut.setStatus("mandatory")


class _RsArpProxy_Type(Integer32):
    """Custom type rsArpProxy based on Integer32"""
    defaultValue = 2

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


_RsArpProxy_Type.__name__ = "Integer32"
_RsArpProxy_Object = MibScalar
rsArpProxy = _RsArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 4, 3),
    _RsArpProxy_Type()
)
rsArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsArpProxy.setStatus("mandatory")
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 5)
)


class _RsTftpRetryTimeOut_Type(Integer32):
    """Custom type rsTftpRetryTimeOut based on Integer32"""
    defaultValue = 15


_RsTftpRetryTimeOut_Object = MibScalar
rsTftpRetryTimeOut = _RsTftpRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 1),
    _RsTftpRetryTimeOut_Type()
)
rsTftpRetryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTftpRetryTimeOut.setStatus("mandatory")


class _RsTftpTotalTimeOut_Type(Integer32):
    """Custom type rsTftpTotalTimeOut based on Integer32"""
    defaultValue = 60


_RsTftpTotalTimeOut_Object = MibScalar
rsTftpTotalTimeOut = _RsTftpTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 2),
    _RsTftpTotalTimeOut_Type()
)
rsTftpTotalTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTftpTotalTimeOut.setStatus("mandatory")
_RsSendConfigFile_Type = DisplayString
_RsSendConfigFile_Object = MibScalar
rsSendConfigFile = _RsSendConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 3),
    _RsSendConfigFile_Type()
)
rsSendConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSendConfigFile.setStatus("mandatory")
_RsGetConfigFile_Type = DisplayString
_RsGetConfigFile_Object = MibScalar
rsGetConfigFile = _RsGetConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 4),
    _RsGetConfigFile_Type()
)
rsGetConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsGetConfigFile.setStatus("mandatory")
_RsLoadSoftware_Type = DisplayString
_RsLoadSoftware_Object = MibScalar
rsLoadSoftware = _RsLoadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 5),
    _RsLoadSoftware_Type()
)
rsLoadSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLoadSoftware.setStatus("mandatory")
_RsFileServerAddress_Type = IpAddress
_RsFileServerAddress_Object = MibScalar
rsFileServerAddress = _RsFileServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 6),
    _RsFileServerAddress_Type()
)
rsFileServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsFileServerAddress.setStatus("mandatory")
_IpRedundancy_ObjectIdentity = ObjectIdentity
ipRedundancy = _IpRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 6)
)


class _IpRedundAdminStatus_Type(Integer32):
    """Custom type ipRedundAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("vrrp", 3))
    )


_IpRedundAdminStatus_Type.__name__ = "Integer32"
_IpRedundAdminStatus_Object = MibScalar
ipRedundAdminStatus = _IpRedundAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 1),
    _IpRedundAdminStatus_Type()
)
ipRedundAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundAdminStatus.setStatus("mandatory")


class _IpRedundOperStatus_Type(Integer32):
    """Custom type ipRedundOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpRedundOperStatus_Type.__name__ = "Integer32"
_IpRedundOperStatus_Object = MibScalar
ipRedundOperStatus = _IpRedundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 2),
    _IpRedundOperStatus_Type()
)
ipRedundOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundOperStatus.setStatus("mandatory")
_IpRedundRoutersTable_Object = MibTable
ipRedundRoutersTable = _IpRedundRoutersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3)
)
if mibBuilder.loadTexts:
    ipRedundRoutersTable.setStatus("mandatory")
_IpRedundRoutersEntry_Object = MibTableRow
ipRedundRoutersEntry = _IpRedundRoutersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1)
)
ipRedundRoutersEntry.setIndexNames(
    (0, "RADWARE-MIB", "ipRedundRoutersIfAddr"),
    (0, "RADWARE-MIB", "ipRedundRoutersMainRouterAddr"),
)
if mibBuilder.loadTexts:
    ipRedundRoutersEntry.setStatus("mandatory")
_IpRedundRoutersIfAddr_Type = IpAddress
_IpRedundRoutersIfAddr_Object = MibTableColumn
ipRedundRoutersIfAddr = _IpRedundRoutersIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 1),
    _IpRedundRoutersIfAddr_Type()
)
ipRedundRoutersIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersIfAddr.setStatus("mandatory")
_IpRedundRoutersMainRouterAddr_Type = IpAddress
_IpRedundRoutersMainRouterAddr_Object = MibTableColumn
ipRedundRoutersMainRouterAddr = _IpRedundRoutersMainRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 2),
    _IpRedundRoutersMainRouterAddr_Type()
)
ipRedundRoutersMainRouterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersMainRouterAddr.setStatus("mandatory")


class _IpRedundRoutersOperStatus_Type(Integer32):
    """Custom type ipRedundRoutersOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpRedundRoutersOperStatus_Type.__name__ = "Integer32"
_IpRedundRoutersOperStatus_Object = MibTableColumn
ipRedundRoutersOperStatus = _IpRedundRoutersOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 3),
    _IpRedundRoutersOperStatus_Type()
)
ipRedundRoutersOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersOperStatus.setStatus("mandatory")


class _IpRedundRoutersPollInterval_Type(Integer32):
    """Custom type ipRedundRoutersPollInterval based on Integer32"""
    defaultValue = 3


_IpRedundRoutersPollInterval_Object = MibTableColumn
ipRedundRoutersPollInterval = _IpRedundRoutersPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 4),
    _IpRedundRoutersPollInterval_Type()
)
ipRedundRoutersPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersPollInterval.setStatus("mandatory")


class _IpRedundRoutersTimeout_Type(Integer32):
    """Custom type ipRedundRoutersTimeout based on Integer32"""
    defaultValue = 12


_IpRedundRoutersTimeout_Object = MibTableColumn
ipRedundRoutersTimeout = _IpRedundRoutersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 5),
    _IpRedundRoutersTimeout_Type()
)
ipRedundRoutersTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersTimeout.setStatus("mandatory")


class _IpRedundRoutersStatus_Type(Integer32):
    """Custom type ipRedundRoutersStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_IpRedundRoutersStatus_Type.__name__ = "Integer32"
_IpRedundRoutersStatus_Object = MibTableColumn
ipRedundRoutersStatus = _IpRedundRoutersStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 6, 3, 1, 6),
    _IpRedundRoutersStatus_Type()
)
ipRedundRoutersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersStatus.setStatus("mandatory")
_IpRouteLeaking_ObjectIdentity = ObjectIdentity
ipRouteLeaking = _IpRouteLeaking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 7)
)


class _IpLeakStaticToRip_Type(Integer32):
    """Custom type ipLeakStaticToRip based on Integer32"""
    defaultValue = 1

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


_IpLeakStaticToRip_Type.__name__ = "Integer32"
_IpLeakStaticToRip_Object = MibScalar
ipLeakStaticToRip = _IpLeakStaticToRip_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 1),
    _IpLeakStaticToRip_Type()
)
ipLeakStaticToRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakStaticToRip.setStatus("mandatory")


class _IpLeakStaticToOspf_Type(Integer32):
    """Custom type ipLeakStaticToOspf based on Integer32"""
    defaultValue = 1

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


_IpLeakStaticToOspf_Type.__name__ = "Integer32"
_IpLeakStaticToOspf_Object = MibScalar
ipLeakStaticToOspf = _IpLeakStaticToOspf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 2),
    _IpLeakStaticToOspf_Type()
)
ipLeakStaticToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakStaticToOspf.setStatus("mandatory")


class _IpLeakOspfToRip_Type(Integer32):
    """Custom type ipLeakOspfToRip based on Integer32"""
    defaultValue = 2

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


_IpLeakOspfToRip_Type.__name__ = "Integer32"
_IpLeakOspfToRip_Object = MibScalar
ipLeakOspfToRip = _IpLeakOspfToRip_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 3),
    _IpLeakOspfToRip_Type()
)
ipLeakOspfToRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakOspfToRip.setStatus("mandatory")


class _IpLeakRipToOspf_Type(Integer32):
    """Custom type ipLeakRipToOspf based on Integer32"""
    defaultValue = 2

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


_IpLeakRipToOspf_Type.__name__ = "Integer32"
_IpLeakRipToOspf_Object = MibScalar
ipLeakRipToOspf = _IpLeakRipToOspf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 4),
    _IpLeakRipToOspf_Type()
)
ipLeakRipToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakRipToOspf.setStatus("mandatory")


class _IpLeakExtDirectToOspf_Type(Integer32):
    """Custom type ipLeakExtDirectToOspf based on Integer32"""
    defaultValue = 1

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


_IpLeakExtDirectToOspf_Type.__name__ = "Integer32"
_IpLeakExtDirectToOspf_Object = MibScalar
ipLeakExtDirectToOspf = _IpLeakExtDirectToOspf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 7, 5),
    _IpLeakExtDirectToOspf_Type()
)
ipLeakExtDirectToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakExtDirectToOspf.setStatus("mandatory")
_IpRipFilter_ObjectIdentity = ObjectIdentity
ipRipFilter = _IpRipFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 26, 8)
)
_RsIpRipFilterGlbTable_Object = MibTable
rsIpRipFilterGlbTable = _RsIpRipFilterGlbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1)
)
if mibBuilder.loadTexts:
    rsIpRipFilterGlbTable.setStatus("mandatory")
_RsIpRipFilterGlbEntry_Object = MibTableRow
rsIpRipFilterGlbEntry = _RsIpRipFilterGlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1)
)
rsIpRipFilterGlbEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpRipFilterGlbType"),
    (0, "RADWARE-MIB", "rsIpRipFilterGlbNumber"),
)
if mibBuilder.loadTexts:
    rsIpRipFilterGlbEntry.setStatus("mandatory")


class _RsIpRipFilterGlbType_Type(Integer32):
    """Custom type rsIpRipFilterGlbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RsIpRipFilterGlbType_Type.__name__ = "Integer32"
_RsIpRipFilterGlbType_Object = MibTableColumn
rsIpRipFilterGlbType = _RsIpRipFilterGlbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 1),
    _RsIpRipFilterGlbType_Type()
)
rsIpRipFilterGlbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbType.setStatus("mandatory")
_RsIpRipFilterGlbNumber_Type = Integer32
_RsIpRipFilterGlbNumber_Object = MibTableColumn
rsIpRipFilterGlbNumber = _RsIpRipFilterGlbNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 2),
    _RsIpRipFilterGlbNumber_Type()
)
rsIpRipFilterGlbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbNumber.setStatus("mandatory")


class _RsIpRipFilterGlbStatus_Type(Integer32):
    """Custom type rsIpRipFilterGlbStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("underCreation", 3),
          ("valid", 1))
    )


_RsIpRipFilterGlbStatus_Type.__name__ = "Integer32"
_RsIpRipFilterGlbStatus_Object = MibTableColumn
rsIpRipFilterGlbStatus = _RsIpRipFilterGlbStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 3),
    _RsIpRipFilterGlbStatus_Type()
)
rsIpRipFilterGlbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbStatus.setStatus("mandatory")


class _RsIpRipFilterGlbIpAddr_Type(IpAddress):
    """Custom type rsIpRipFilterGlbIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpRipFilterGlbIpAddr_Object = MibTableColumn
rsIpRipFilterGlbIpAddr = _RsIpRipFilterGlbIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 4),
    _RsIpRipFilterGlbIpAddr_Type()
)
rsIpRipFilterGlbIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbIpAddr.setStatus("mandatory")


class _RsIpRipFilterGlbNetworkMaskBits_Type(Integer32):
    """Custom type rsIpRipFilterGlbNetworkMaskBits based on Integer32"""
    defaultValue = 0


_RsIpRipFilterGlbNetworkMaskBits_Object = MibTableColumn
rsIpRipFilterGlbNetworkMaskBits = _RsIpRipFilterGlbNetworkMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 5),
    _RsIpRipFilterGlbNetworkMaskBits_Type()
)
rsIpRipFilterGlbNetworkMaskBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbNetworkMaskBits.setStatus("mandatory")


class _RsIpRipFilterGlbMatchBits_Type(Integer32):
    """Custom type rsIpRipFilterGlbMatchBits based on Integer32"""
    defaultValue = 32


_RsIpRipFilterGlbMatchBits_Object = MibTableColumn
rsIpRipFilterGlbMatchBits = _RsIpRipFilterGlbMatchBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 6),
    _RsIpRipFilterGlbMatchBits_Type()
)
rsIpRipFilterGlbMatchBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbMatchBits.setStatus("mandatory")


class _RsIpRipFilterGlbAction_Type(Integer32):
    """Custom type rsIpRipFilterGlbAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RsIpRipFilterGlbAction_Type.__name__ = "Integer32"
_RsIpRipFilterGlbAction_Object = MibTableColumn
rsIpRipFilterGlbAction = _RsIpRipFilterGlbAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 1, 1, 7),
    _RsIpRipFilterGlbAction_Type()
)
rsIpRipFilterGlbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbAction.setStatus("mandatory")
_RsIpRipFilterLclTable_Object = MibTable
rsIpRipFilterLclTable = _RsIpRipFilterLclTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2)
)
if mibBuilder.loadTexts:
    rsIpRipFilterLclTable.setStatus("mandatory")
_RsIpRipFilterLclEntry_Object = MibTableRow
rsIpRipFilterLclEntry = _RsIpRipFilterLclEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1)
)
rsIpRipFilterLclEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpRipFilterLclIpIntf"),
    (0, "RADWARE-MIB", "rsIpRipFilterLclType"),
    (0, "RADWARE-MIB", "rsIpRipFilterLclNumber"),
)
if mibBuilder.loadTexts:
    rsIpRipFilterLclEntry.setStatus("mandatory")
_RsIpRipFilterLclIpIntf_Type = IpAddress
_RsIpRipFilterLclIpIntf_Object = MibTableColumn
rsIpRipFilterLclIpIntf = _RsIpRipFilterLclIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 1),
    _RsIpRipFilterLclIpIntf_Type()
)
rsIpRipFilterLclIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclIpIntf.setStatus("mandatory")


class _RsIpRipFilterLclType_Type(Integer32):
    """Custom type rsIpRipFilterLclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RsIpRipFilterLclType_Type.__name__ = "Integer32"
_RsIpRipFilterLclType_Object = MibTableColumn
rsIpRipFilterLclType = _RsIpRipFilterLclType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 2),
    _RsIpRipFilterLclType_Type()
)
rsIpRipFilterLclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclType.setStatus("mandatory")
_RsIpRipFilterLclNumber_Type = Integer32
_RsIpRipFilterLclNumber_Object = MibTableColumn
rsIpRipFilterLclNumber = _RsIpRipFilterLclNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 3),
    _RsIpRipFilterLclNumber_Type()
)
rsIpRipFilterLclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclNumber.setStatus("mandatory")


class _RsIpRipFilterLclStatus_Type(Integer32):
    """Custom type rsIpRipFilterLclStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("underCreation", 3),
          ("valid", 1))
    )


_RsIpRipFilterLclStatus_Type.__name__ = "Integer32"
_RsIpRipFilterLclStatus_Object = MibTableColumn
rsIpRipFilterLclStatus = _RsIpRipFilterLclStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 4),
    _RsIpRipFilterLclStatus_Type()
)
rsIpRipFilterLclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclStatus.setStatus("mandatory")


class _RsIpRipFilterLclIpAddr_Type(IpAddress):
    """Custom type rsIpRipFilterLclIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpRipFilterLclIpAddr_Object = MibTableColumn
rsIpRipFilterLclIpAddr = _RsIpRipFilterLclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 5),
    _RsIpRipFilterLclIpAddr_Type()
)
rsIpRipFilterLclIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclIpAddr.setStatus("mandatory")


class _RsIpRipFilterLclNetworkMaskBits_Type(Integer32):
    """Custom type rsIpRipFilterLclNetworkMaskBits based on Integer32"""
    defaultValue = 0


_RsIpRipFilterLclNetworkMaskBits_Object = MibTableColumn
rsIpRipFilterLclNetworkMaskBits = _RsIpRipFilterLclNetworkMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 6),
    _RsIpRipFilterLclNetworkMaskBits_Type()
)
rsIpRipFilterLclNetworkMaskBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclNetworkMaskBits.setStatus("mandatory")


class _RsIpRipFilterLclMatchBits_Type(Integer32):
    """Custom type rsIpRipFilterLclMatchBits based on Integer32"""
    defaultValue = 32


_RsIpRipFilterLclMatchBits_Object = MibTableColumn
rsIpRipFilterLclMatchBits = _RsIpRipFilterLclMatchBits_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 7),
    _RsIpRipFilterLclMatchBits_Type()
)
rsIpRipFilterLclMatchBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclMatchBits.setStatus("mandatory")


class _RsIpRipFilterLclAction_Type(Integer32):
    """Custom type rsIpRipFilterLclAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RsIpRipFilterLclAction_Type.__name__ = "Integer32"
_RsIpRipFilterLclAction_Object = MibTableColumn
rsIpRipFilterLclAction = _RsIpRipFilterLclAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 8, 2, 1, 8),
    _RsIpRipFilterLclAction_Type()
)
rsIpRipFilterLclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclAction.setStatus("mandatory")


class _RsRipEnable_Type(Integer32):
    """Custom type rsRipEnable based on Integer32"""
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


_RsRipEnable_Type.__name__ = "Integer32"
_RsRipEnable_Object = MibScalar
rsRipEnable = _RsRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 9),
    _RsRipEnable_Type()
)
rsRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRipEnable.setStatus("mandatory")
_LreBoxAgentIP_Type = IpAddress
_LreBoxAgentIP_Object = MibScalar
lreBoxAgentIP = _LreBoxAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 10),
    _LreBoxAgentIP_Type()
)
lreBoxAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreBoxAgentIP.setStatus("mandatory")
_VirtualLan_ObjectIdentity = ObjectIdentity
virtualLan = _VirtualLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 27)
)
_VirtualLanTable_Object = MibTable
virtualLanTable = _VirtualLanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1)
)
if mibBuilder.loadTexts:
    virtualLanTable.setStatus("mandatory")
_VirtualLanEntry_Object = MibTableRow
virtualLanEntry = _VirtualLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1)
)
virtualLanEntry.setIndexNames(
    (0, "RADWARE-MIB", "vlIfIndex"),
)
if mibBuilder.loadTexts:
    virtualLanEntry.setStatus("mandatory")
_VlIfIndex_Type = Integer32
_VlIfIndex_Object = MibTableColumn
vlIfIndex = _VlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 1),
    _VlIfIndex_Type()
)
vlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlIfIndex.setStatus("mandatory")


class _VlProto_Type(Integer32):
    """Custom type vlProto based on Integer32"""
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
        *(("appleTalk", 11),
          ("decLAT", 9),
          ("decNET", 8),
          ("ip", 2),
          ("ipmulticast", 3),
          ("ipxET", 5),
          ("ipxLLC", 6),
          ("ipxRaw", 4),
          ("ipxSNAP", 7),
          ("netBios", 10),
          ("other", 1),
          ("sna", 13),
          ("userDefined", 14),
          ("xns", 12))
    )


_VlProto_Type.__name__ = "Integer32"
_VlProto_Object = MibTableColumn
vlProto = _VlProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 2),
    _VlProto_Type()
)
vlProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlProto.setStatus("mandatory")
_VlAutoConfigEnable_Type = TruthValue
_VlAutoConfigEnable_Object = MibTableColumn
vlAutoConfigEnable = _VlAutoConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 3),
    _VlAutoConfigEnable_Type()
)
vlAutoConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlAutoConfigEnable.setStatus("mandatory")
_VlStatus_Type = RowStatus
_VlStatus_Object = MibTableColumn
vlStatus = _VlStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 4),
    _VlStatus_Type()
)
vlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlStatus.setStatus("mandatory")


class _VlType_Type(Integer32):
    """Custom type vlType based on Integer32"""
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
        *(("regular", 1),
          ("specArpReq", 3),
          ("specArpReqAndUnicast", 5),
          ("specBroadcast", 2),
          ("specBroadcastAndUnicast", 4))
    )


_VlType_Type.__name__ = "Integer32"
_VlType_Object = MibTableColumn
vlType = _VlType_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 1, 1, 5),
    _VlType_Type()
)
vlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlType.setStatus("mandatory")
_VirtualLanPortsTable_Object = MibTable
virtualLanPortsTable = _VirtualLanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2)
)
if mibBuilder.loadTexts:
    virtualLanPortsTable.setStatus("mandatory")
_VirtualLanPortEntry_Object = MibTableRow
virtualLanPortEntry = _VirtualLanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1)
)
virtualLanPortEntry.setIndexNames(
    (0, "RADWARE-MIB", "vLIfIndex"),
    (0, "RADWARE-MIB", "vLPortIfIndex"),
)
if mibBuilder.loadTexts:
    virtualLanPortEntry.setStatus("mandatory")
_VLIfIndex_Type = Integer32
_VLIfIndex_Object = MibTableColumn
vLIfIndex = _VLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 1),
    _VLIfIndex_Type()
)
vLIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLIfIndex.setStatus("mandatory")
_VLPortIfIndex_Type = Integer32
_VLPortIfIndex_Object = MibTableColumn
vLPortIfIndex = _VLPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 2),
    _VLPortIfIndex_Type()
)
vLPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLPortIfIndex.setStatus("mandatory")


class _VLPortType_Type(Integer32):
    """Custom type vLPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_VLPortType_Type.__name__ = "Integer32"
_VLPortType_Object = MibTableColumn
vLPortType = _VLPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 3),
    _VLPortType_Type()
)
vLPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLPortType.setStatus("mandatory")
_VLPortStatus_Type = RowStatus
_VLPortStatus_Object = MibTableColumn
vLPortStatus = _VLPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 2, 1, 4),
    _VLPortStatus_Type()
)
vLPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLPortStatus.setStatus("mandatory")
_VirtualLanAutoConfTable_Object = MibTable
virtualLanAutoConfTable = _VirtualLanAutoConfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3)
)
if mibBuilder.loadTexts:
    virtualLanAutoConfTable.setStatus("mandatory")
_VirtualLanAutoConfEntry_Object = MibTableRow
virtualLanAutoConfEntry = _VirtualLanAutoConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1)
)
virtualLanAutoConfEntry.setIndexNames(
    (0, "RADWARE-MIB", "vlAutoConfPortIfIndex"),
    (0, "RADWARE-MIB", "vlAutoConfProto"),
)
if mibBuilder.loadTexts:
    virtualLanAutoConfEntry.setStatus("mandatory")
_VlAutoConfPortIfIndex_Type = Integer32
_VlAutoConfPortIfIndex_Object = MibTableColumn
vlAutoConfPortIfIndex = _VlAutoConfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1, 1),
    _VlAutoConfPortIfIndex_Type()
)
vlAutoConfPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlAutoConfPortIfIndex.setStatus("mandatory")


class _VlAutoConfProto_Type(Integer32):
    """Custom type vlAutoConfProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ip", 2)
    )


_VlAutoConfProto_Type.__name__ = "Integer32"
_VlAutoConfProto_Object = MibTableColumn
vlAutoConfProto = _VlAutoConfProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1, 2),
    _VlAutoConfProto_Type()
)
vlAutoConfProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlAutoConfProto.setStatus("mandatory")
_VlAutoConfStatus_Type = RowStatus
_VlAutoConfStatus_Object = MibTableColumn
vlAutoConfStatus = _VlAutoConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 3, 1, 3),
    _VlAutoConfStatus_Type()
)
vlAutoConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlAutoConfStatus.setStatus("mandatory")


class _VirtualLanAutoConfAgingTimeout_Type(Integer32):
    """Custom type virtualLanAutoConfAgingTimeout based on Integer32"""
    defaultValue = 3600


_VirtualLanAutoConfAgingTimeout_Object = MibScalar
virtualLanAutoConfAgingTimeout = _VirtualLanAutoConfAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 4),
    _VirtualLanAutoConfAgingTimeout_Type()
)
virtualLanAutoConfAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualLanAutoConfAgingTimeout.setStatus("mandatory")
_VirtualLanProtocolVlan_ObjectIdentity = ObjectIdentity
virtualLanProtocolVlan = _VirtualLanProtocolVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 27, 5)
)


class _VirtualLanUserEtherType_Type(OctetString):
    """Custom type virtualLanUserEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VirtualLanUserEtherType_Type.__name__ = "OctetString"
_VirtualLanUserEtherType_Object = MibScalar
virtualLanUserEtherType = _VirtualLanUserEtherType_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 5, 1),
    _VirtualLanUserEtherType_Type()
)
virtualLanUserEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualLanUserEtherType.setStatus("mandatory")


class _VirtualLanUserMask_Type(OctetString):
    """Custom type virtualLanUserMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VirtualLanUserMask_Type.__name__ = "OctetString"
_VirtualLanUserMask_Object = MibScalar
virtualLanUserMask = _VirtualLanUserMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 27, 5, 2),
    _VirtualLanUserMask_Type()
)
virtualLanUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualLanUserMask.setStatus("mandatory")
_RsConf_ObjectIdentity = ObjectIdentity
rsConf = _RsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 28)
)
_RsIfConfTable_Object = MibTable
rsIfConfTable = _RsIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1)
)
if mibBuilder.loadTexts:
    rsIfConfTable.setStatus("mandatory")
_RsIfConfEntry_Object = MibTableRow
rsIfConfEntry = _RsIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1)
)
rsIfConfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIfConfIndex"),
)
if mibBuilder.loadTexts:
    rsIfConfEntry.setStatus("mandatory")
_RsIfConfIndex_Type = Integer32
_RsIfConfIndex_Object = MibTableColumn
rsIfConfIndex = _RsIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 1),
    _RsIfConfIndex_Type()
)
rsIfConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfConfIndex.setStatus("mandatory")
_RsIfConfType_Type = RsIfType
_RsIfConfType_Object = MibTableColumn
rsIfConfType = _RsIfConfType_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 2),
    _RsIfConfType_Type()
)
rsIfConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfConfType.setStatus("mandatory")
_RsIfConfName_Type = DisplayString
_RsIfConfName_Object = MibTableColumn
rsIfConfName = _RsIfConfName_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 3),
    _RsIfConfName_Type()
)
rsIfConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfConfName.setStatus("mandatory")
_RsIfConfStatus_Type = RowStatus
_RsIfConfStatus_Object = MibTableColumn
rsIfConfStatus = _RsIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 28, 1, 1, 4),
    _RsIfConfStatus_Type()
)
rsIfConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfConfStatus.setStatus("mandatory")
_RsTunning_ObjectIdentity = ObjectIdentity
rsTunning = _RsTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29)
)
_RsHighPriority_Type = Integer32
_RsHighPriority_Object = MibScalar
rsHighPriority = _RsHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 1),
    _RsHighPriority_Type()
)
rsHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsHighPriority.setStatus("mandatory")
_RsLowPriority_Type = Integer32
_RsLowPriority_Object = MibScalar
rsLowPriority = _RsLowPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 2),
    _RsLowPriority_Type()
)
rsLowPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsLowPriority.setStatus("mandatory")
_RsDbgLevel_Type = Integer32
_RsDbgLevel_Object = MibScalar
rsDbgLevel = _RsDbgLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 3),
    _RsDbgLevel_Type()
)
rsDbgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDbgLevel.setStatus("mandatory")
_RsDiagnostic_Type = DisplayString
_RsDiagnostic_Object = MibScalar
rsDiagnostic = _RsDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 4),
    _RsDiagnostic_Type()
)
rsDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiagnostic.setStatus("mandatory")
_RsConfirmMessagTab_Type = Integer32
_RsConfirmMessagTab_Object = MibScalar
rsConfirmMessagTab = _RsConfirmMessagTab_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 5),
    _RsConfirmMessagTab_Type()
)
rsConfirmMessagTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsConfirmMessagTab.setStatus("mandatory")
_EventMessageTable_Object = MibTable
eventMessageTable = _EventMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6)
)
if mibBuilder.loadTexts:
    eventMessageTable.setStatus("mandatory")
_EventMessageEntry_Object = MibTableRow
eventMessageEntry = _EventMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1)
)
eventMessageEntry.setIndexNames(
    (0, "RADWARE-MIB", "eventNum"),
)
if mibBuilder.loadTexts:
    eventMessageEntry.setStatus("mandatory")
_EventNum_Type = Integer32
_EventNum_Object = MibTableColumn
eventNum = _EventNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1, 1),
    _EventNum_Type()
)
eventNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNum.setStatus("mandatory")
_EventDesc_Type = DisplayString
_EventDesc_Object = MibTableColumn
eventDesc = _EventDesc_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 6, 1, 2),
    _EventDesc_Type()
)
eventDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDesc.setStatus("mandatory")
_ReaTunning_ObjectIdentity = ObjectIdentity
reaTunning = _ReaTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 7)
)
_ReaIpRemoteAgingTime_Type = Integer32
_ReaIpRemoteAgingTime_Object = MibScalar
reaIpRemoteAgingTime = _ReaIpRemoteAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 1),
    _ReaIpRemoteAgingTime_Type()
)
reaIpRemoteAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpRemoteAgingTime.setStatus("mandatory")
_ReaFftHashMaxChain_Type = Integer32
_ReaFftHashMaxChain_Object = MibScalar
reaFftHashMaxChain = _ReaFftHashMaxChain_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 2),
    _ReaFftHashMaxChain_Type()
)
reaFftHashMaxChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaFftHashMaxChain.setStatus("mandatory")


class _ReaMltcstBitOn_Type(Integer32):
    """Custom type reaMltcstBitOn based on Integer32"""
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


_ReaMltcstBitOn_Type.__name__ = "Integer32"
_ReaMltcstBitOn_Object = MibScalar
reaMltcstBitOn = _ReaMltcstBitOn_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 3),
    _ReaMltcstBitOn_Type()
)
reaMltcstBitOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaMltcstBitOn.setStatus("mandatory")


class _ReaIpForwardEnable_Type(Integer32):
    """Custom type reaIpForwardEnable based on Integer32"""
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


_ReaIpForwardEnable_Type.__name__ = "Integer32"
_ReaIpForwardEnable_Object = MibScalar
reaIpForwardEnable = _ReaIpForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 4),
    _ReaIpForwardEnable_Type()
)
reaIpForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpForwardEnable.setStatus("mandatory")


class _ReaIpxForwardEnable_Type(Integer32):
    """Custom type reaIpxForwardEnable based on Integer32"""
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


_ReaIpxForwardEnable_Type.__name__ = "Integer32"
_ReaIpxForwardEnable_Object = MibScalar
reaIpxForwardEnable = _ReaIpxForwardEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 5),
    _ReaIpxForwardEnable_Type()
)
reaIpxForwardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaIpxForwardEnable.setStatus("mandatory")


class _ReaBridgeEnable_Type(Integer32):
    """Custom type reaBridgeEnable based on Integer32"""
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


_ReaBridgeEnable_Type.__name__ = "Integer32"
_ReaBridgeEnable_Object = MibScalar
reaBridgeEnable = _ReaBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 6),
    _ReaBridgeEnable_Type()
)
reaBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaBridgeEnable.setStatus("mandatory")


class _ReaFacsEnable_Type(Integer32):
    """Custom type reaFacsEnable based on Integer32"""
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


_ReaFacsEnable_Type.__name__ = "Integer32"
_ReaFacsEnable_Object = MibScalar
reaFacsEnable = _ReaFacsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 7),
    _ReaFacsEnable_Type()
)
reaFacsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaFacsEnable.setStatus("mandatory")
_ReaIpForwardDatagrams_Type = Counter32
_ReaIpForwardDatagrams_Object = MibScalar
reaIpForwardDatagrams = _ReaIpForwardDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 8),
    _ReaIpForwardDatagrams_Type()
)
reaIpForwardDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpForwardDatagrams.setStatus("mandatory")
_ReaIpInDiscards_Type = Counter32
_ReaIpInDiscards_Object = MibScalar
reaIpInDiscards = _ReaIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 9),
    _ReaIpInDiscards_Type()
)
reaIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpInDiscards.setStatus("mandatory")
_ReaIpxForwardDatagrams_Type = Counter32
_ReaIpxForwardDatagrams_Object = MibScalar
reaIpxForwardDatagrams = _ReaIpxForwardDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 10),
    _ReaIpxForwardDatagrams_Type()
)
reaIpxForwardDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxForwardDatagrams.setStatus("mandatory")
_ReaIpxInDiscards_Type = Counter32
_ReaIpxInDiscards_Object = MibScalar
reaIpxInDiscards = _ReaIpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 11),
    _ReaIpxInDiscards_Type()
)
reaIpxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxInDiscards.setStatus("mandatory")
_ReaBridgeFftTable_Object = MibTable
reaBridgeFftTable = _ReaBridgeFftTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12)
)
if mibBuilder.loadTexts:
    reaBridgeFftTable.setStatus("mandatory")
_ReaBridgeFftEntry_Object = MibTableRow
reaBridgeFftEntry = _ReaBridgeFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1)
)
reaBridgeFftEntry.setIndexNames(
    (0, "RADWARE-MIB", "reaBrgFftEntryNum"),
)
if mibBuilder.loadTexts:
    reaBridgeFftEntry.setStatus("mandatory")
_ReaBrgFftEntryNum_Type = Integer32
_ReaBrgFftEntryNum_Object = MibTableColumn
reaBrgFftEntryNum = _ReaBrgFftEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 1),
    _ReaBrgFftEntryNum_Type()
)
reaBrgFftEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftEntryNum.setStatus("mandatory")
_ReaBrgFftMacAddr_Type = PhysAddress
_ReaBrgFftMacAddr_Object = MibTableColumn
reaBrgFftMacAddr = _ReaBrgFftMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 2),
    _ReaBrgFftMacAddr_Type()
)
reaBrgFftMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftMacAddr.setStatus("mandatory")
_ReaBrgFftReNum_Type = Integer32
_ReaBrgFftReNum_Object = MibTableColumn
reaBrgFftReNum = _ReaBrgFftReNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 3),
    _ReaBrgFftReNum_Type()
)
reaBrgFftReNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftReNum.setStatus("mandatory")
_ReaBrgFftPortNum_Type = Integer32
_ReaBrgFftPortNum_Object = MibTableColumn
reaBrgFftPortNum = _ReaBrgFftPortNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 4),
    _ReaBrgFftPortNum_Type()
)
reaBrgFftPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftPortNum.setStatus("mandatory")
_ReaBrgFftFacsSrcIndex_Type = Integer32
_ReaBrgFftFacsSrcIndex_Object = MibTableColumn
reaBrgFftFacsSrcIndex = _ReaBrgFftFacsSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 5),
    _ReaBrgFftFacsSrcIndex_Type()
)
reaBrgFftFacsSrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftFacsSrcIndex.setStatus("mandatory")
_ReaBrgFftFacsDstIndex_Type = Integer32
_ReaBrgFftFacsDstIndex_Object = MibTableColumn
reaBrgFftFacsDstIndex = _ReaBrgFftFacsDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 12, 1, 6),
    _ReaBrgFftFacsDstIndex_Type()
)
reaBrgFftFacsDstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgFftFacsDstIndex.setStatus("mandatory")
_ReaBrgDiscards_Type = Counter32
_ReaBrgDiscards_Object = MibScalar
reaBrgDiscards = _ReaBrgDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 13),
    _ReaBrgDiscards_Type()
)
reaBrgDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgDiscards.setStatus("mandatory")
_ReaBrgForwards_Type = Counter32
_ReaBrgForwards_Object = MibScalar
reaBrgForwards = _ReaBrgForwards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 14),
    _ReaBrgForwards_Type()
)
reaBrgForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBrgForwards.setStatus("mandatory")
_ReaIpFftTable_Object = MibTable
reaIpFftTable = _ReaIpFftTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15)
)
if mibBuilder.loadTexts:
    reaIpFftTable.setStatus("mandatory")
_ReaIpFftEntry_Object = MibTableRow
reaIpFftEntry = _ReaIpFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1)
)
reaIpFftEntry.setIndexNames(
    (0, "RADWARE-MIB", "reaIpFftEntryNum"),
)
if mibBuilder.loadTexts:
    reaIpFftEntry.setStatus("mandatory")
_ReaIpFftEntryNum_Type = Integer32
_ReaIpFftEntryNum_Object = MibTableColumn
reaIpFftEntryNum = _ReaIpFftEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 1),
    _ReaIpFftEntryNum_Type()
)
reaIpFftEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftEntryNum.setStatus("mandatory")
_ReaIpFftDstIpAddr_Type = IpAddress
_ReaIpFftDstIpAddr_Object = MibTableColumn
reaIpFftDstIpAddr = _ReaIpFftDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 2),
    _ReaIpFftDstIpAddr_Type()
)
reaIpFftDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftDstIpAddr.setStatus("mandatory")
_ReaIpFftDstIpMask_Type = IpAddress
_ReaIpFftDstIpMask_Object = MibTableColumn
reaIpFftDstIpMask = _ReaIpFftDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 3),
    _ReaIpFftDstIpMask_Type()
)
reaIpFftDstIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftDstIpMask.setStatus("mandatory")


class _ReaIpFftRangeType_Type(Integer32):
    """Custom type reaIpFftRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("remote", 2))
    )


_ReaIpFftRangeType_Type.__name__ = "Integer32"
_ReaIpFftRangeType_Object = MibTableColumn
reaIpFftRangeType = _ReaIpFftRangeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 4),
    _ReaIpFftRangeType_Type()
)
reaIpFftRangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftRangeType.setStatus("mandatory")
_ReaIpFftSrcMacAddr_Type = PhysAddress
_ReaIpFftSrcMacAddr_Object = MibTableColumn
reaIpFftSrcMacAddr = _ReaIpFftSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 5),
    _ReaIpFftSrcMacAddr_Type()
)
reaIpFftSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftSrcMacAddr.setStatus("mandatory")
_ReaIpFftDstMacAddr_Type = PhysAddress
_ReaIpFftDstMacAddr_Object = MibTableColumn
reaIpFftDstMacAddr = _ReaIpFftDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 6),
    _ReaIpFftDstMacAddr_Type()
)
reaIpFftDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftDstMacAddr.setStatus("mandatory")
_ReaIpFftReNum_Type = Integer32
_ReaIpFftReNum_Object = MibTableColumn
reaIpFftReNum = _ReaIpFftReNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 7),
    _ReaIpFftReNum_Type()
)
reaIpFftReNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftReNum.setStatus("mandatory")
_ReaIpFftPortNum_Type = Integer32
_ReaIpFftPortNum_Object = MibTableColumn
reaIpFftPortNum = _ReaIpFftPortNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 8),
    _ReaIpFftPortNum_Type()
)
reaIpFftPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftPortNum.setStatus("mandatory")
_ReaIpFftFacsSrcIndex_Type = Integer32
_ReaIpFftFacsSrcIndex_Object = MibTableColumn
reaIpFftFacsSrcIndex = _ReaIpFftFacsSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 9),
    _ReaIpFftFacsSrcIndex_Type()
)
reaIpFftFacsSrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftFacsSrcIndex.setStatus("mandatory")
_ReaIpFftFacsDstIndex_Type = Integer32
_ReaIpFftFacsDstIndex_Object = MibTableColumn
reaIpFftFacsDstIndex = _ReaIpFftFacsDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 10),
    _ReaIpFftFacsDstIndex_Type()
)
reaIpFftFacsDstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftFacsDstIndex.setStatus("mandatory")


class _ReaIpFftApplFlags_Type(OctetString):
    """Custom type reaIpFftApplFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ReaIpFftApplFlags_Type.__name__ = "OctetString"
_ReaIpFftApplFlags_Object = MibTableColumn
reaIpFftApplFlags = _ReaIpFftApplFlags_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 15, 1, 11),
    _ReaIpFftApplFlags_Type()
)
reaIpFftApplFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpFftApplFlags.setStatus("mandatory")
_ReaIpxFftTable_Object = MibTable
reaIpxFftTable = _ReaIpxFftTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16)
)
if mibBuilder.loadTexts:
    reaIpxFftTable.setStatus("mandatory")
_ReaIpxFftEntry_Object = MibTableRow
reaIpxFftEntry = _ReaIpxFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1)
)
reaIpxFftEntry.setIndexNames(
    (0, "RADWARE-MIB", "reaIpxFftEntryNum"),
)
if mibBuilder.loadTexts:
    reaIpxFftEntry.setStatus("mandatory")
_ReaIpxFftEntryNum_Type = Integer32
_ReaIpxFftEntryNum_Object = MibTableColumn
reaIpxFftEntryNum = _ReaIpxFftEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 1),
    _ReaIpxFftEntryNum_Type()
)
reaIpxFftEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftEntryNum.setStatus("mandatory")
_ReaIpxFftDstNetid_Type = Integer32
_ReaIpxFftDstNetid_Object = MibTableColumn
reaIpxFftDstNetid = _ReaIpxFftDstNetid_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 2),
    _ReaIpxFftDstNetid_Type()
)
reaIpxFftDstNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftDstNetid.setStatus("mandatory")


class _ReaIpxFftRangeType_Type(Integer32):
    """Custom type reaIpxFftRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("remote", 2))
    )


_ReaIpxFftRangeType_Type.__name__ = "Integer32"
_ReaIpxFftRangeType_Object = MibTableColumn
reaIpxFftRangeType = _ReaIpxFftRangeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 3),
    _ReaIpxFftRangeType_Type()
)
reaIpxFftRangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftRangeType.setStatus("mandatory")
_ReaIpxFftSrcMacAddr_Type = PhysAddress
_ReaIpxFftSrcMacAddr_Object = MibTableColumn
reaIpxFftSrcMacAddr = _ReaIpxFftSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 4),
    _ReaIpxFftSrcMacAddr_Type()
)
reaIpxFftSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftSrcMacAddr.setStatus("mandatory")
_ReaIpxFftDstMacAddr_Type = PhysAddress
_ReaIpxFftDstMacAddr_Object = MibTableColumn
reaIpxFftDstMacAddr = _ReaIpxFftDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 5),
    _ReaIpxFftDstMacAddr_Type()
)
reaIpxFftDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftDstMacAddr.setStatus("mandatory")
_ReaIpxFftReNum_Type = Integer32
_ReaIpxFftReNum_Object = MibTableColumn
reaIpxFftReNum = _ReaIpxFftReNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 6),
    _ReaIpxFftReNum_Type()
)
reaIpxFftReNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftReNum.setStatus("mandatory")
_ReaIpxFftPortNum_Type = Integer32
_ReaIpxFftPortNum_Object = MibTableColumn
reaIpxFftPortNum = _ReaIpxFftPortNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 7),
    _ReaIpxFftPortNum_Type()
)
reaIpxFftPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftPortNum.setStatus("mandatory")
_ReaIpxFftFacsSrcIndex_Type = Integer32
_ReaIpxFftFacsSrcIndex_Object = MibTableColumn
reaIpxFftFacsSrcIndex = _ReaIpxFftFacsSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 8),
    _ReaIpxFftFacsSrcIndex_Type()
)
reaIpxFftFacsSrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftFacsSrcIndex.setStatus("mandatory")
_ReaIpxFftFacsDstIndex_Type = Integer32
_ReaIpxFftFacsDstIndex_Object = MibTableColumn
reaIpxFftFacsDstIndex = _ReaIpxFftFacsDstIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 16, 1, 9),
    _ReaIpxFftFacsDstIndex_Type()
)
reaIpxFftFacsDstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaIpxFftFacsDstIndex.setStatus("mandatory")
_LreVnResposibilityTable_Object = MibTable
lreVnResposibilityTable = _LreVnResposibilityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17)
)
if mibBuilder.loadTexts:
    lreVnResposibilityTable.setStatus("mandatory")
_LreVnResposibilityEntry_Object = MibTableRow
lreVnResposibilityEntry = _LreVnResposibilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17, 1)
)
lreVnResposibilityEntry.setIndexNames(
    (0, "RADWARE-MIB", "lreVnRespVn"),
)
if mibBuilder.loadTexts:
    lreVnResposibilityEntry.setStatus("mandatory")
_LreVnRespVn_Type = Integer32
_LreVnRespVn_Object = MibTableColumn
lreVnRespVn = _LreVnRespVn_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17, 1, 1),
    _LreVnRespVn_Type()
)
lreVnRespVn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreVnRespVn.setStatus("mandatory")
_LreVnRespStatus_Type = RowStatus
_LreVnRespStatus_Object = MibTableColumn
lreVnRespStatus = _LreVnRespStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 17, 1, 2),
    _LreVnRespStatus_Type()
)
lreVnRespStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreVnRespStatus.setStatus("mandatory")


class _ReaSrcViolationEnable_Type(Integer32):
    """Custom type reaSrcViolationEnable based on Integer32"""
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


_ReaSrcViolationEnable_Type.__name__ = "Integer32"
_ReaSrcViolationEnable_Object = MibScalar
reaSrcViolationEnable = _ReaSrcViolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 18),
    _ReaSrcViolationEnable_Type()
)
reaSrcViolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaSrcViolationEnable.setStatus("mandatory")


class _ReaSrcViolationTrapEnable_Type(Integer32):
    """Custom type reaSrcViolationTrapEnable based on Integer32"""
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


_ReaSrcViolationTrapEnable_Type.__name__ = "Integer32"
_ReaSrcViolationTrapEnable_Object = MibScalar
reaSrcViolationTrapEnable = _ReaSrcViolationTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 19),
    _ReaSrcViolationTrapEnable_Type()
)
reaSrcViolationTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaSrcViolationTrapEnable.setStatus("mandatory")


class _ReaSrcAddrValidationEnable_Type(Integer32):
    """Custom type reaSrcAddrValidationEnable based on Integer32"""
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


_ReaSrcAddrValidationEnable_Type.__name__ = "Integer32"
_ReaSrcAddrValidationEnable_Object = MibScalar
reaSrcAddrValidationEnable = _ReaSrcAddrValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 20),
    _ReaSrcAddrValidationEnable_Type()
)
reaSrcAddrValidationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reaSrcAddrValidationEnable.setStatus("mandatory")
_ReaRsQueueDiscards_Type = Counter32
_ReaRsQueueDiscards_Object = MibScalar
reaRsQueueDiscards = _ReaRsQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 21),
    _ReaRsQueueDiscards_Type()
)
reaRsQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaRsQueueDiscards.setStatus("mandatory")
_ReaBufFree_Type = Integer32
_ReaBufFree_Object = MibScalar
reaBufFree = _ReaBufFree_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 22),
    _ReaBufFree_Type()
)
reaBufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reaBufFree.setStatus("mandatory")


class _LreResetDstMacBit46_Type(Integer32):
    """Custom type lreResetDstMacBit46 based on Integer32"""
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


_LreResetDstMacBit46_Type.__name__ = "Integer32"
_LreResetDstMacBit46_Object = MibScalar
lreResetDstMacBit46 = _LreResetDstMacBit46_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 23),
    _LreResetDstMacBit46_Type()
)
lreResetDstMacBit46.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreResetDstMacBit46.setStatus("mandatory")


class _LreQueSourceSelect_Type(Integer32):
    """Custom type lreQueSourceSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dstMac", 2),
          ("vNET", 1))
    )


_LreQueSourceSelect_Type.__name__ = "Integer32"
_LreQueSourceSelect_Object = MibScalar
lreQueSourceSelect = _LreQueSourceSelect_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 24),
    _LreQueSourceSelect_Type()
)
lreQueSourceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreQueSourceSelect.setStatus("mandatory")


class _LreResetDstMacBit47_Type(Integer32):
    """Custom type lreResetDstMacBit47 based on Integer32"""
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


_LreResetDstMacBit47_Type.__name__ = "Integer32"
_LreResetDstMacBit47_Object = MibScalar
lreResetDstMacBit47 = _LreResetDstMacBit47_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 7, 25),
    _LreResetDstMacBit47_Type()
)
lreResetDstMacBit47.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lreResetDstMacBit47.setStatus("mandatory")
_RsMaxEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxEntriesTuning = _RsMaxEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8)
)
_RsMaxBridgeForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxBridgeForwardingEntriesTuning = _RsMaxBridgeForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1)
)
_RsMaxBrgFrwEntries_Type = Integer32
_RsMaxBrgFrwEntries_Object = MibScalar
rsMaxBrgFrwEntries = _RsMaxBrgFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1, 1),
    _RsMaxBrgFrwEntries_Type()
)
rsMaxBrgFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxBrgFrwEntries.setStatus("mandatory")
_RsMaxBrgFrwEntriesAfterReset_Type = Integer32
_RsMaxBrgFrwEntriesAfterReset_Object = MibScalar
rsMaxBrgFrwEntriesAfterReset = _RsMaxBrgFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 1, 2),
    _RsMaxBrgFrwEntriesAfterReset_Type()
)
rsMaxBrgFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxBrgFrwEntriesAfterReset.setStatus("mandatory")
_RsMaxIpForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpForwardingEntriesTuning = _RsMaxIpForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2)
)
_RsMaxIpFrwEntries_Type = Integer32
_RsMaxIpFrwEntries_Object = MibScalar
rsMaxIpFrwEntries = _RsMaxIpFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2, 1),
    _RsMaxIpFrwEntries_Type()
)
rsMaxIpFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpFrwEntries.setStatus("mandatory")
_RsMaxIpFrwEntriesAfterReset_Type = Integer32
_RsMaxIpFrwEntriesAfterReset_Object = MibScalar
rsMaxIpFrwEntriesAfterReset = _RsMaxIpFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 2, 2),
    _RsMaxIpFrwEntriesAfterReset_Type()
)
rsMaxIpFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpFrwEntriesAfterReset.setStatus("mandatory")
_RsMaxArpEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxArpEntriesTuning = _RsMaxArpEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3)
)
_RsMaxArpEntries_Type = Integer32
_RsMaxArpEntries_Object = MibScalar
rsMaxArpEntries = _RsMaxArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3, 1),
    _RsMaxArpEntries_Type()
)
rsMaxArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxArpEntries.setStatus("mandatory")
_RsMaxArpEntriesAfterReset_Type = Integer32
_RsMaxArpEntriesAfterReset_Object = MibScalar
rsMaxArpEntriesAfterReset = _RsMaxArpEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 3, 2),
    _RsMaxArpEntriesAfterReset_Type()
)
rsMaxArpEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxArpEntriesAfterReset.setStatus("mandatory")
_RsMaxIpxForwardingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpxForwardingEntriesTuning = _RsMaxIpxForwardingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4)
)
_RsMaxIpxFrwEntries_Type = Integer32
_RsMaxIpxFrwEntries_Object = MibScalar
rsMaxIpxFrwEntries = _RsMaxIpxFrwEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4, 1),
    _RsMaxIpxFrwEntries_Type()
)
rsMaxIpxFrwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxFrwEntries.setStatus("mandatory")
_RsMaxIpxFrwEntriesAfterReset_Type = Integer32
_RsMaxIpxFrwEntriesAfterReset_Object = MibScalar
rsMaxIpxFrwEntriesAfterReset = _RsMaxIpxFrwEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 4, 2),
    _RsMaxIpxFrwEntriesAfterReset_Type()
)
rsMaxIpxFrwEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxFrwEntriesAfterReset.setStatus("mandatory")
_RsMaxIpxSapEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxIpxSapEntriesTuning = _RsMaxIpxSapEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5)
)
_RsMaxIpxSapEntries_Type = Integer32
_RsMaxIpxSapEntries_Object = MibScalar
rsMaxIpxSapEntries = _RsMaxIpxSapEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5, 1),
    _RsMaxIpxSapEntries_Type()
)
rsMaxIpxSapEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxIpxSapEntries.setStatus("mandatory")
_RsMaxIpxSapEntriesAfterReset_Type = Integer32
_RsMaxIpxSapEntriesAfterReset_Object = MibScalar
rsMaxIpxSapEntriesAfterReset = _RsMaxIpxSapEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 5, 2),
    _RsMaxIpxSapEntriesAfterReset_Type()
)
rsMaxIpxSapEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxIpxSapEntriesAfterReset.setStatus("mandatory")
_RsMaxDspClntEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxDspClntEntriesTuning = _RsMaxDspClntEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6)
)
_RsMaxDspClntEntries_Type = Integer32
_RsMaxDspClntEntries_Object = MibScalar
rsMaxDspClntEntries = _RsMaxDspClntEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6, 1),
    _RsMaxDspClntEntries_Type()
)
rsMaxDspClntEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDspClntEntries.setStatus("mandatory")
_RsMaxDspClntEntriesAfterReset_Type = Integer32
_RsMaxDspClntEntriesAfterReset_Object = MibScalar
rsMaxDspClntEntriesAfterReset = _RsMaxDspClntEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 6, 2),
    _RsMaxDspClntEntriesAfterReset_Type()
)
rsMaxDspClntEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDspClntEntriesAfterReset.setStatus("mandatory")
_RsMaxZeroHopRoutEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxZeroHopRoutEntriesTuning = _RsMaxZeroHopRoutEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 7)
)
_RsMaxZhrConns_Type = Integer32
_RsMaxZhrConns_Object = MibScalar
rsMaxZhrConns = _RsMaxZhrConns_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 7, 1),
    _RsMaxZhrConns_Type()
)
rsMaxZhrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxZhrConns.setStatus("mandatory")
_RsMaxZhrConnsAfterReset_Type = Integer32
_RsMaxZhrConnsAfterReset_Object = MibScalar
rsMaxZhrConnsAfterReset = _RsMaxZhrConnsAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 7, 2),
    _RsMaxZhrConnsAfterReset_Type()
)
rsMaxZhrConnsAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxZhrConnsAfterReset.setStatus("mandatory")
_RsMaxDspFrmEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxDspFrmEntriesTuning = _RsMaxDspFrmEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 8)
)
_RsMaxDspFrmEntries_Type = Integer32
_RsMaxDspFrmEntries_Object = MibScalar
rsMaxDspFrmEntries = _RsMaxDspFrmEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 8, 1),
    _RsMaxDspFrmEntries_Type()
)
rsMaxDspFrmEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxDspFrmEntries.setStatus("mandatory")
_RsMaxDspFrmEntriesAfterReset_Type = Integer32
_RsMaxDspFrmEntriesAfterReset_Object = MibScalar
rsMaxDspFrmEntriesAfterReset = _RsMaxDspFrmEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 8, 2),
    _RsMaxDspFrmEntriesAfterReset_Type()
)
rsMaxDspFrmEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxDspFrmEntriesAfterReset.setStatus("mandatory")
_RsMaxRoutingEntriesTuning_ObjectIdentity = ObjectIdentity
rsMaxRoutingEntriesTuning = _RsMaxRoutingEntriesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9)
)
_RsMaxRoutingEntries_Type = Integer32
_RsMaxRoutingEntries_Object = MibScalar
rsMaxRoutingEntries = _RsMaxRoutingEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 1),
    _RsMaxRoutingEntries_Type()
)
rsMaxRoutingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMaxRoutingEntries.setStatus("mandatory")
_RsMaxRoutingEntriesAfterReset_Type = Integer32
_RsMaxRoutingEntriesAfterReset_Object = MibScalar
rsMaxRoutingEntriesAfterReset = _RsMaxRoutingEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 29, 8, 9, 2),
    _RsMaxRoutingEntriesAfterReset_Type()
)
rsMaxRoutingEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMaxRoutingEntriesAfterReset.setStatus("mandatory")
_RndApplications_ObjectIdentity = ObjectIdentity
rndApplications = _RndApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35)
)
_RsServerDispatcher_ObjectIdentity = ObjectIdentity
rsServerDispatcher = _RsServerDispatcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1)
)
_RsWSDServerStatTable_Object = MibTable
rsWSDServerStatTable = _RsWSDServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12)
)
if mibBuilder.loadTexts:
    rsWSDServerStatTable.setStatus("mandatory")
_RsWSDServerStatEntry_Object = MibTableRow
rsWSDServerStatEntry = _RsWSDServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1)
)
rsWSDServerStatEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDSerStatName"),
)
if mibBuilder.loadTexts:
    rsWSDServerStatEntry.setStatus("mandatory")


class _RsWSDSerStatName_Type(DisplayString):
    """Custom type rsWSDSerStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsWSDSerStatName_Type.__name__ = "DisplayString"
_RsWSDSerStatName_Object = MibTableColumn
rsWSDSerStatName = _RsWSDSerStatName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 1),
    _RsWSDSerStatName_Type()
)
rsWSDSerStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatName.setStatus("mandatory")
_RsWSDSerStatAttUsersNum_Type = Integer32
_RsWSDSerStatAttUsersNum_Object = MibTableColumn
rsWSDSerStatAttUsersNum = _RsWSDSerStatAttUsersNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 2),
    _RsWSDSerStatAttUsersNum_Type()
)
rsWSDSerStatAttUsersNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatAttUsersNum.setStatus("mandatory")
_RsWSDSerStatPeakLoad_Type = Integer32
_RsWSDSerStatPeakLoad_Object = MibTableColumn
rsWSDSerStatPeakLoad = _RsWSDSerStatPeakLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 3),
    _RsWSDSerStatPeakLoad_Type()
)
rsWSDSerStatPeakLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatPeakLoad.setStatus("mandatory")
_RsWSDSerStatFramesRate_Type = Integer32
_RsWSDSerStatFramesRate_Object = MibTableColumn
rsWSDSerStatFramesRate = _RsWSDSerStatFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 4),
    _RsWSDSerStatFramesRate_Type()
)
rsWSDSerStatFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatFramesRate.setStatus("mandatory")
_RsWSDSerStatFramesLoad_Type = Counter32
_RsWSDSerStatFramesLoad_Object = MibTableColumn
rsWSDSerStatFramesLoad = _RsWSDSerStatFramesLoad_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 5),
    _RsWSDSerStatFramesLoad_Type()
)
rsWSDSerStatFramesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatFramesLoad.setStatus("mandatory")
_RsWSDSerStatRecoveryTime_Type = Integer32
_RsWSDSerStatRecoveryTime_Object = MibTableColumn
rsWSDSerStatRecoveryTime = _RsWSDSerStatRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 6),
    _RsWSDSerStatRecoveryTime_Type()
)
rsWSDSerStatRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatRecoveryTime.setStatus("mandatory")
_RsWSDSerStatWarmUpTime_Type = Integer32
_RsWSDSerStatWarmUpTime_Object = MibTableColumn
rsWSDSerStatWarmUpTime = _RsWSDSerStatWarmUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 7),
    _RsWSDSerStatWarmUpTime_Type()
)
rsWSDSerStatWarmUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatWarmUpTime.setStatus("mandatory")
_RsWSDSerStatConnectionLimit_Type = Integer32
_RsWSDSerStatConnectionLimit_Object = MibTableColumn
rsWSDSerStatConnectionLimit = _RsWSDSerStatConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 8),
    _RsWSDSerStatConnectionLimit_Type()
)
rsWSDSerStatConnectionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatConnectionLimit.setStatus("mandatory")


class _RsWSDSerStatAdminStatus_Type(Integer32):
    """Custom type rsWSDSerStatAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("shutdown", 2))
    )


_RsWSDSerStatAdminStatus_Type.__name__ = "Integer32"
_RsWSDSerStatAdminStatus_Object = MibTableColumn
rsWSDSerStatAdminStatus = _RsWSDSerStatAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 9),
    _RsWSDSerStatAdminStatus_Type()
)
rsWSDSerStatAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSerStatAdminStatus.setStatus("mandatory")
_RsWSDSerStatConnectionLimitReached_Type = Integer32
_RsWSDSerStatConnectionLimitReached_Object = MibTableColumn
rsWSDSerStatConnectionLimitReached = _RsWSDSerStatConnectionLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 1, 10),
    _RsWSDSerStatConnectionLimitReached_Type()
)
rsWSDSerStatConnectionLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSerStatConnectionLimitReached.setStatus("mandatory")
_RsWSDdummy2_Type = Integer32
_RsWSDdummy2_Object = MibScalar
rsWSDdummy2 = _RsWSDdummy2_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 12, 2),
    _RsWSDdummy2_Type()
)
rsWSDdummy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy2.setStatus("mandatory")
_WsdRedundTable_Object = MibTable
wsdRedundTable = _WsdRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16)
)
if mibBuilder.loadTexts:
    wsdRedundTable.setStatus("mandatory")
_WsdRedundEntry_Object = MibTableRow
wsdRedundEntry = _WsdRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1)
)
wsdRedundEntry.setIndexNames(
    (0, "RADWARE-MIB", "wsdRedundFarmAddr"),
    (0, "RADWARE-MIB", "wsdRedundMainWsdAddr"),
)
if mibBuilder.loadTexts:
    wsdRedundEntry.setStatus("mandatory")
_WsdRedundFarmAddr_Type = IpAddress
_WsdRedundFarmAddr_Object = MibTableColumn
wsdRedundFarmAddr = _WsdRedundFarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 1),
    _WsdRedundFarmAddr_Type()
)
wsdRedundFarmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsdRedundFarmAddr.setStatus("mandatory")
_WsdRedundMainWsdAddr_Type = IpAddress
_WsdRedundMainWsdAddr_Object = MibTableColumn
wsdRedundMainWsdAddr = _WsdRedundMainWsdAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 2),
    _WsdRedundMainWsdAddr_Type()
)
wsdRedundMainWsdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsdRedundMainWsdAddr.setStatus("mandatory")


class _WsdRedundOperStatus_Type(Integer32):
    """Custom type wsdRedundOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WsdRedundOperStatus_Type.__name__ = "Integer32"
_WsdRedundOperStatus_Object = MibTableColumn
wsdRedundOperStatus = _WsdRedundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 3),
    _WsdRedundOperStatus_Type()
)
wsdRedundOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsdRedundOperStatus.setStatus("mandatory")
_WsdRedundPollInterval_Type = Integer32
_WsdRedundPollInterval_Object = MibTableColumn
wsdRedundPollInterval = _WsdRedundPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 4),
    _WsdRedundPollInterval_Type()
)
wsdRedundPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsdRedundPollInterval.setStatus("mandatory")
_WsdRedundTimeout_Type = Integer32
_WsdRedundTimeout_Object = MibTableColumn
wsdRedundTimeout = _WsdRedundTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 5),
    _WsdRedundTimeout_Type()
)
wsdRedundTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsdRedundTimeout.setStatus("mandatory")


class _WsdRedundStatus_Type(Integer32):
    """Custom type wsdRedundStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_WsdRedundStatus_Type.__name__ = "Integer32"
_WsdRedundStatus_Object = MibTableColumn
wsdRedundStatus = _WsdRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 1, 6),
    _WsdRedundStatus_Type()
)
wsdRedundStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsdRedundStatus.setStatus("mandatory")
_RsWSDdummy5_Type = Integer32
_RsWSDdummy5_Object = MibScalar
rsWSDdummy5 = _RsWSDdummy5_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 16, 2),
    _RsWSDdummy5_Type()
)
rsWSDdummy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy5.setStatus("mandatory")


class _RsWSDNewEntryOnSourcePort_Type(Integer32):
    """Custom type rsWSDNewEntryOnSourcePort based on Integer32"""
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


_RsWSDNewEntryOnSourcePort_Type.__name__ = "Integer32"
_RsWSDNewEntryOnSourcePort_Object = MibScalar
rsWSDNewEntryOnSourcePort = _RsWSDNewEntryOnSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 19),
    _RsWSDNewEntryOnSourcePort_Type()
)
rsWSDNewEntryOnSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNewEntryOnSourcePort.setStatus("mandatory")


class _RsWSDSelectServerOnSourcePort_Type(Integer32):
    """Custom type rsWSDSelectServerOnSourcePort based on Integer32"""
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


_RsWSDSelectServerOnSourcePort_Type.__name__ = "Integer32"
_RsWSDSelectServerOnSourcePort_Object = MibScalar
rsWSDSelectServerOnSourcePort = _RsWSDSelectServerOnSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 20),
    _RsWSDSelectServerOnSourcePort_Type()
)
rsWSDSelectServerOnSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSelectServerOnSourcePort.setStatus("mandatory")


class _RsWSDRedundancyMode_Type(Integer32):
    """Custom type rsWSDRedundancyMode based on Integer32"""
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


_RsWSDRedundancyMode_Type.__name__ = "Integer32"
_RsWSDRedundancyMode_Object = MibScalar
rsWSDRedundancyMode = _RsWSDRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 21),
    _RsWSDRedundancyMode_Type()
)
rsWSDRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDRedundancyMode.setStatus("mandatory")


class _RsNsdMode_Type(Integer32):
    """Custom type rsNsdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastMode", 2),
          ("slowMode", 1))
    )


_RsNsdMode_Type.__name__ = "Integer32"
_RsNsdMode_Object = MibScalar
rsNsdMode = _RsNsdMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 22),
    _RsNsdMode_Type()
)
rsNsdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsNsdMode.setStatus("mandatory")
_RsNsdWINSAddr_Type = IpAddress
_RsNsdWINSAddr_Object = MibScalar
rsNsdWINSAddr = _RsNsdWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 23),
    _RsNsdWINSAddr_Type()
)
rsNsdWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsNsdWINSAddr.setStatus("mandatory")


class _RsWSDSyslogStatus_Type(Integer32):
    """Custom type rsWSDSyslogStatus based on Integer32"""
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


_RsWSDSyslogStatus_Type.__name__ = "Integer32"
_RsWSDSyslogStatus_Object = MibScalar
rsWSDSyslogStatus = _RsWSDSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 26),
    _RsWSDSyslogStatus_Type()
)
rsWSDSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogStatus.setStatus("mandatory")
_RsWSDSyslogAddress_Type = IpAddress
_RsWSDSyslogAddress_Object = MibScalar
rsWSDSyslogAddress = _RsWSDSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 27),
    _RsWSDSyslogAddress_Type()
)
rsWSDSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSyslogAddress.setStatus("mandatory")
_RsWSDNTCheckTable_Object = MibTable
rsWSDNTCheckTable = _RsWSDNTCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28)
)
if mibBuilder.loadTexts:
    rsWSDNTCheckTable.setStatus("mandatory")
_RsWSDNTCheckEntry_Object = MibTableRow
rsWSDNTCheckEntry = _RsWSDNTCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1)
)
rsWSDNTCheckEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDNTSerialNum"),
)
if mibBuilder.loadTexts:
    rsWSDNTCheckEntry.setStatus("mandatory")
_RsWSDNTSerialNum_Type = Integer32
_RsWSDNTSerialNum_Object = MibTableColumn
rsWSDNTSerialNum = _RsWSDNTSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 1),
    _RsWSDNTSerialNum_Type()
)
rsWSDNTSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDNTSerialNum.setStatus("mandatory")
_RsWSDNTFrequentCheckPeriod_Type = Integer32
_RsWSDNTFrequentCheckPeriod_Object = MibTableColumn
rsWSDNTFrequentCheckPeriod = _RsWSDNTFrequentCheckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 2),
    _RsWSDNTFrequentCheckPeriod_Type()
)
rsWSDNTFrequentCheckPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTFrequentCheckPeriod.setStatus("mandatory")
_RsWSDNTOpenSessionsWeight_Type = Integer32
_RsWSDNTOpenSessionsWeight_Object = MibTableColumn
rsWSDNTOpenSessionsWeight = _RsWSDNTOpenSessionsWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 3),
    _RsWSDNTOpenSessionsWeight_Type()
)
rsWSDNTOpenSessionsWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTOpenSessionsWeight.setStatus("mandatory")
_RsWSDNTIncomingTrafficWeight_Type = Integer32
_RsWSDNTIncomingTrafficWeight_Object = MibTableColumn
rsWSDNTIncomingTrafficWeight = _RsWSDNTIncomingTrafficWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 4),
    _RsWSDNTIncomingTrafficWeight_Type()
)
rsWSDNTIncomingTrafficWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTIncomingTrafficWeight.setStatus("mandatory")
_RsWSDNTOutgoingTrafficWeight_Type = Integer32
_RsWSDNTOutgoingTrafficWeight_Object = MibTableColumn
rsWSDNTOutgoingTrafficWeight = _RsWSDNTOutgoingTrafficWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 5),
    _RsWSDNTOutgoingTrafficWeight_Type()
)
rsWSDNTOutgoingTrafficWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTOutgoingTrafficWeight.setStatus("mandatory")
_RsWSDNTRegularCheckPeriod_Type = Integer32
_RsWSDNTRegularCheckPeriod_Object = MibTableColumn
rsWSDNTRegularCheckPeriod = _RsWSDNTRegularCheckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 6),
    _RsWSDNTRegularCheckPeriod_Type()
)
rsWSDNTRegularCheckPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTRegularCheckPeriod.setStatus("mandatory")
_RsWSDNTAvResponseWeight_Type = Integer32
_RsWSDNTAvResponseWeight_Object = MibTableColumn
rsWSDNTAvResponseWeight = _RsWSDNTAvResponseWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 7),
    _RsWSDNTAvResponseWeight_Type()
)
rsWSDNTAvResponseWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTAvResponseWeight.setStatus("mandatory")
_RsWSDNTUsersLimitWeight_Type = Integer32
_RsWSDNTUsersLimitWeight_Object = MibTableColumn
rsWSDNTUsersLimitWeight = _RsWSDNTUsersLimitWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 8),
    _RsWSDNTUsersLimitWeight_Type()
)
rsWSDNTUsersLimitWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTUsersLimitWeight.setStatus("mandatory")
_RsWSDNTTCPLimitWeight_Type = Integer32
_RsWSDNTTCPLimitWeight_Object = MibTableColumn
rsWSDNTTCPLimitWeight = _RsWSDNTTCPLimitWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 9),
    _RsWSDNTTCPLimitWeight_Type()
)
rsWSDNTTCPLimitWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTTCPLimitWeight.setStatus("mandatory")
_RsWSDNTRetries_Type = Integer32
_RsWSDNTRetries_Object = MibTableColumn
rsWSDNTRetries = _RsWSDNTRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 10),
    _RsWSDNTRetries_Type()
)
rsWSDNTRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTRetries.setStatus("mandatory")


class _RsWSDNTCommunity_Type(DisplayString):
    """Custom type rsWSDNTCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsWSDNTCommunity_Type.__name__ = "DisplayString"
_RsWSDNTCommunity_Object = MibTableColumn
rsWSDNTCommunity = _RsWSDNTCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 1, 11),
    _RsWSDNTCommunity_Type()
)
rsWSDNTCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTCommunity.setStatus("mandatory")
_RsWSDdummy8_Type = Integer32
_RsWSDdummy8_Object = MibScalar
rsWSDdummy8 = _RsWSDdummy8_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 28, 2),
    _RsWSDdummy8_Type()
)
rsWSDdummy8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy8.setStatus("mandatory")
_RsWSDPrivateCheckTable_Object = MibTable
rsWSDPrivateCheckTable = _RsWSDPrivateCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29)
)
if mibBuilder.loadTexts:
    rsWSDPrivateCheckTable.setStatus("mandatory")
_RsWSDPrivateCheckEntry_Object = MibTableRow
rsWSDPrivateCheckEntry = _RsWSDPrivateCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1)
)
rsWSDPrivateCheckEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDPrivateSerialNum"),
)
if mibBuilder.loadTexts:
    rsWSDPrivateCheckEntry.setStatus("mandatory")
_RsWSDPrivateSerialNum_Type = Integer32
_RsWSDPrivateSerialNum_Object = MibTableColumn
rsWSDPrivateSerialNum = _RsWSDPrivateSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 1),
    _RsWSDPrivateSerialNum_Type()
)
rsWSDPrivateSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPrivateSerialNum.setStatus("mandatory")
_RsWSDPrivateSpecialCheckPeriod_Type = Integer32
_RsWSDPrivateSpecialCheckPeriod_Object = MibTableColumn
rsWSDPrivateSpecialCheckPeriod = _RsWSDPrivateSpecialCheckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 2),
    _RsWSDPrivateSpecialCheckPeriod_Type()
)
rsWSDPrivateSpecialCheckPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateSpecialCheckPeriod.setStatus("mandatory")
_RsWSDPrivateExtraVar1ID_Type = ObjectIdentifier
_RsWSDPrivateExtraVar1ID_Object = MibTableColumn
rsWSDPrivateExtraVar1ID = _RsWSDPrivateExtraVar1ID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 3),
    _RsWSDPrivateExtraVar1ID_Type()
)
rsWSDPrivateExtraVar1ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar1ID.setStatus("mandatory")
_RsWSDPrivateExtraVar1Weight_Type = Integer32
_RsWSDPrivateExtraVar1Weight_Object = MibTableColumn
rsWSDPrivateExtraVar1Weight = _RsWSDPrivateExtraVar1Weight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 4),
    _RsWSDPrivateExtraVar1Weight_Type()
)
rsWSDPrivateExtraVar1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar1Weight.setStatus("mandatory")
_RsWSDPrivateExtraVar2ID_Type = ObjectIdentifier
_RsWSDPrivateExtraVar2ID_Object = MibTableColumn
rsWSDPrivateExtraVar2ID = _RsWSDPrivateExtraVar2ID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 5),
    _RsWSDPrivateExtraVar2ID_Type()
)
rsWSDPrivateExtraVar2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar2ID.setStatus("mandatory")
_RsWSDPrivateExtraVar2Weight_Type = Integer32
_RsWSDPrivateExtraVar2Weight_Object = MibTableColumn
rsWSDPrivateExtraVar2Weight = _RsWSDPrivateExtraVar2Weight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 6),
    _RsWSDPrivateExtraVar2Weight_Type()
)
rsWSDPrivateExtraVar2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar2Weight.setStatus("mandatory")
_RsWSDPrivateRetries_Type = Integer32
_RsWSDPrivateRetries_Object = MibTableColumn
rsWSDPrivateRetries = _RsWSDPrivateRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 7),
    _RsWSDPrivateRetries_Type()
)
rsWSDPrivateRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateRetries.setStatus("mandatory")


class _RsWSDPrivateCommunity_Type(DisplayString):
    """Custom type rsWSDPrivateCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RsWSDPrivateCommunity_Type.__name__ = "DisplayString"
_RsWSDPrivateCommunity_Object = MibTableColumn
rsWSDPrivateCommunity = _RsWSDPrivateCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 8),
    _RsWSDPrivateCommunity_Type()
)
rsWSDPrivateCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateCommunity.setStatus("mandatory")


class _RsWSDPrivateExtraVar1Mode_Type(Integer32):
    """Custom type rsWSDPrivateExtraVar1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 1),
          ("descending", 2))
    )


_RsWSDPrivateExtraVar1Mode_Type.__name__ = "Integer32"
_RsWSDPrivateExtraVar1Mode_Object = MibTableColumn
rsWSDPrivateExtraVar1Mode = _RsWSDPrivateExtraVar1Mode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 9),
    _RsWSDPrivateExtraVar1Mode_Type()
)
rsWSDPrivateExtraVar1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar1Mode.setStatus("mandatory")


class _RsWSDPrivateExtraVar2Mode_Type(Integer32):
    """Custom type rsWSDPrivateExtraVar2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 1),
          ("descending", 2))
    )


_RsWSDPrivateExtraVar2Mode_Type.__name__ = "Integer32"
_RsWSDPrivateExtraVar2Mode_Object = MibTableColumn
rsWSDPrivateExtraVar2Mode = _RsWSDPrivateExtraVar2Mode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 1, 10),
    _RsWSDPrivateExtraVar2Mode_Type()
)
rsWSDPrivateExtraVar2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDPrivateExtraVar2Mode.setStatus("mandatory")
_RsWSDdummy9_Type = Integer32
_RsWSDdummy9_Object = MibScalar
rsWSDdummy9 = _RsWSDdummy9_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 29, 2),
    _RsWSDdummy9_Type()
)
rsWSDdummy9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy9.setStatus("mandatory")


class _RsWSDDNSResolution_Type(Integer32):
    """Custom type rsWSDDNSResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("proximity", 3))
    )


_RsWSDDNSResolution_Type.__name__ = "Integer32"
_RsWSDDNSResolution_Object = MibScalar
rsWSDDNSResolution = _RsWSDDNSResolution_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 31),
    _RsWSDDNSResolution_Type()
)
rsWSDDNSResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDNSResolution.setStatus("mandatory")


class _RsWSDUserPassword_Type(DisplayString):
    """Custom type rsWSDUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RsWSDUserPassword_Type.__name__ = "DisplayString"
_RsWSDUserPassword_Object = MibScalar
rsWSDUserPassword = _RsWSDUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 33),
    _RsWSDUserPassword_Type()
)
rsWSDUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDUserPassword.setStatus("mandatory")


class _RsWSDUserVersion_Type(DisplayString):
    """Custom type rsWSDUserVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RsWSDUserVersion_Type.__name__ = "DisplayString"
_RsWSDUserVersion_Object = MibScalar
rsWSDUserVersion = _RsWSDUserVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 34),
    _RsWSDUserVersion_Type()
)
rsWSDUserVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDUserVersion.setStatus("mandatory")


class _RsWSDNatStatus_Type(Integer32):
    """Custom type rsWSDNatStatus based on Integer32"""
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


_RsWSDNatStatus_Type.__name__ = "Integer32"
_RsWSDNatStatus_Object = MibScalar
rsWSDNatStatus = _RsWSDNatStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 35),
    _RsWSDNatStatus_Type()
)
rsWSDNatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNatStatus.setStatus("mandatory")


class _RsWSDRedundancyTakeback_Type(Integer32):
    """Custom type rsWSDRedundancyTakeback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_RsWSDRedundancyTakeback_Type.__name__ = "Integer32"
_RsWSDRedundancyTakeback_Object = MibScalar
rsWSDRedundancyTakeback = _RsWSDRedundancyTakeback_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 37),
    _RsWSDRedundancyTakeback_Type()
)
rsWSDRedundancyTakeback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDRedundancyTakeback.setStatus("mandatory")
_RsMLB_ObjectIdentity = ObjectIdentity
rsMLB = _RsMLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 38)
)
_RsCSD_ObjectIdentity = ObjectIdentity
rsCSD = _RsCSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 39)
)
_RsNWSD_ObjectIdentity = ObjectIdentity
rsNWSD = _RsNWSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40)
)
_RsWSDIfTable_Object = MibTable
rsWSDIfTable = _RsWSDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41)
)
if mibBuilder.loadTexts:
    rsWSDIfTable.setStatus("mandatory")
_RsWSDIfEntry_Object = MibTableRow
rsWSDIfEntry = _RsWSDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1)
)
rsWSDIfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDIfIndex"),
)
if mibBuilder.loadTexts:
    rsWSDIfEntry.setStatus("mandatory")
_RsWSDIfIndex_Type = Integer32
_RsWSDIfIndex_Object = MibTableColumn
rsWSDIfIndex = _RsWSDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 1),
    _RsWSDIfIndex_Type()
)
rsWSDIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfIndex.setStatus("mandatory")
_RsWSDIfBoardNum_Type = Integer32
_RsWSDIfBoardNum_Object = MibTableColumn
rsWSDIfBoardNum = _RsWSDIfBoardNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 2),
    _RsWSDIfBoardNum_Type()
)
rsWSDIfBoardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfBoardNum.setStatus("mandatory")
_RsWSDIfNetAddress_Type = IpAddress
_RsWSDIfNetAddress_Object = MibTableColumn
rsWSDIfNetAddress = _RsWSDIfNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 3),
    _RsWSDIfNetAddress_Type()
)
rsWSDIfNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfNetAddress.setStatus("mandatory")


class _RsWSDIfStatus_Type(Integer32):
    """Custom type rsWSDIfStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("channelLoopback", 7),
          ("connctFault", 4),
          ("ok", 1),
          ("okMultiBrg", 3),
          ("okSingleBrg", 2),
          ("rxClockFault", 8),
          ("rxFault", 5),
          ("t1Alarm", 9),
          ("txFault", 6))
    )


_RsWSDIfStatus_Type.__name__ = "Integer32"
_RsWSDIfStatus_Object = MibTableColumn
rsWSDIfStatus = _RsWSDIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 4),
    _RsWSDIfStatus_Type()
)
rsWSDIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfStatus.setStatus("mandatory")


class _RsWSDIfClockType_Type(Integer32):
    """Custom type rsWSDIfClockType based on Integer32"""
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
        *(("external", 1),
          ("g703", 4),
          ("internal", 2),
          ("t1", 3))
    )


_RsWSDIfClockType_Type.__name__ = "Integer32"
_RsWSDIfClockType_Object = MibTableColumn
rsWSDIfClockType = _RsWSDIfClockType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 5),
    _RsWSDIfClockType_Type()
)
rsWSDIfClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfClockType.setStatus("mandatory")
_RsWSDIfBaudRate_Type = Integer32
_RsWSDIfBaudRate_Object = MibTableColumn
rsWSDIfBaudRate = _RsWSDIfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 6),
    _RsWSDIfBaudRate_Type()
)
rsWSDIfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfBaudRate.setStatus("mandatory")
_RsWSDIfCost_Type = Integer32
_RsWSDIfCost_Object = MibTableColumn
rsWSDIfCost = _RsWSDIfCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 7),
    _RsWSDIfCost_Type()
)
rsWSDIfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfCost.setStatus("mandatory")


class _RsWSDIfCompression_Type(Integer32):
    """Custom type rsWSDIfCompression based on Integer32"""
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


_RsWSDIfCompression_Type.__name__ = "Integer32"
_RsWSDIfCompression_Object = MibTableColumn
rsWSDIfCompression = _RsWSDIfCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 8),
    _RsWSDIfCompression_Type()
)
rsWSDIfCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfCompression.setStatus("mandatory")


class _RsWSDIfCompressionStatus_Type(Integer32):
    """Custom type rsWSDIfCompressionStatus based on Integer32"""
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
        *(("active", 2),
          ("disable", 4),
          ("not-active", 3),
          ("not-inserted", 1))
    )


_RsWSDIfCompressionStatus_Type.__name__ = "Integer32"
_RsWSDIfCompressionStatus_Object = MibTableColumn
rsWSDIfCompressionStatus = _RsWSDIfCompressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 9),
    _RsWSDIfCompressionStatus_Type()
)
rsWSDIfCompressionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfCompressionStatus.setStatus("mandatory")
_RsWSDIfCompressionRate_Type = Integer32
_RsWSDIfCompressionRate_Object = MibTableColumn
rsWSDIfCompressionRate = _RsWSDIfCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 10),
    _RsWSDIfCompressionRate_Type()
)
rsWSDIfCompressionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfCompressionRate.setStatus("mandatory")


class _RsWSDIfLATCompression_Type(Integer32):
    """Custom type rsWSDIfLATCompression based on Integer32"""
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


_RsWSDIfLATCompression_Type.__name__ = "Integer32"
_RsWSDIfLATCompression_Object = MibTableColumn
rsWSDIfLATCompression = _RsWSDIfLATCompression_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 11),
    _RsWSDIfLATCompression_Type()
)
rsWSDIfLATCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfLATCompression.setStatus("mandatory")


class _RsWSDIfCompressionType_Type(Integer32):
    """Custom type rsWSDIfCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highSpeed", 3),
          ("lowSpeed", 2),
          ("none", 1))
    )


_RsWSDIfCompressionType_Type.__name__ = "Integer32"
_RsWSDIfCompressionType_Object = MibTableColumn
rsWSDIfCompressionType = _RsWSDIfCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 12),
    _RsWSDIfCompressionType_Type()
)
rsWSDIfCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDIfCompressionType.setStatus("mandatory")


class _RsWSDIfFilterMode_Type(Integer32):
    """Custom type rsWSDIfFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destinationOnly", 1),
          ("none", 3),
          ("sourceAndDestination", 2))
    )


_RsWSDIfFilterMode_Type.__name__ = "Integer32"
_RsWSDIfFilterMode_Object = MibTableColumn
rsWSDIfFilterMode = _RsWSDIfFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 13),
    _RsWSDIfFilterMode_Type()
)
rsWSDIfFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfFilterMode.setStatus("mandatory")


class _RsWSDIfChannelType_Type(Integer32):
    """Custom type rsWSDIfChannelType based on Integer32"""
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
        *(("dialBackup", 5),
          ("frameRelay1490", 9),
          ("frameRelay1490CAR", 10),
          ("frameRelayCAR", 11),
          ("lan", 7),
          ("ogRanPort", 2),
          ("ppp", 12),
          ("routerToBridge", 3),
          ("snar", 6),
          ("spsFramRelay", 4),
          ("spsX25", 8),
          ("wanChannel", 1))
    )


_RsWSDIfChannelType_Type.__name__ = "Integer32"
_RsWSDIfChannelType_Object = MibTableColumn
rsWSDIfChannelType = _RsWSDIfChannelType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 14),
    _RsWSDIfChannelType_Type()
)
rsWSDIfChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfChannelType.setStatus("mandatory")


class _RsWSDIfBridge_Type(Integer32):
    """Custom type rsWSDIfBridge based on Integer32"""
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


_RsWSDIfBridge_Type.__name__ = "Integer32"
_RsWSDIfBridge_Object = MibTableColumn
rsWSDIfBridge = _RsWSDIfBridge_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 15),
    _RsWSDIfBridge_Type()
)
rsWSDIfBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDIfBridge.setStatus("mandatory")


class _RsWSDHighPriorityIf_Type(Integer32):
    """Custom type rsWSDHighPriorityIf based on Integer32"""
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


_RsWSDHighPriorityIf_Type.__name__ = "Integer32"
_RsWSDHighPriorityIf_Object = MibTableColumn
rsWSDHighPriorityIf = _RsWSDHighPriorityIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 16),
    _RsWSDHighPriorityIf_Type()
)
rsWSDHighPriorityIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHighPriorityIf.setStatus("mandatory")


class _RsWSDWanHeader_Type(Integer32):
    """Custom type rsWSDWanHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("short", 2))
    )


_RsWSDWanHeader_Type.__name__ = "Integer32"
_RsWSDWanHeader_Object = MibTableColumn
rsWSDWanHeader = _RsWSDWanHeader_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 17),
    _RsWSDWanHeader_Type()
)
rsWSDWanHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWanHeader.setStatus("mandatory")


class _RsWSDDuplexMode_Type(Integer32):
    """Custom type rsWSDDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 2),
          ("half", 1))
    )


_RsWSDDuplexMode_Type.__name__ = "Integer32"
_RsWSDDuplexMode_Object = MibTableColumn
rsWSDDuplexMode = _RsWSDDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 41, 1, 18),
    _RsWSDDuplexMode_Type()
)
rsWSDDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDuplexMode.setStatus("mandatory")


class _RsWSDClientMirrorPercentage_Type(Integer32):
    """Custom type rsWSDClientMirrorPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDClientMirrorPercentage_Type.__name__ = "Integer32"
_RsWSDClientMirrorPercentage_Object = MibScalar
rsWSDClientMirrorPercentage = _RsWSDClientMirrorPercentage_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 42),
    _RsWSDClientMirrorPercentage_Type()
)
rsWSDClientMirrorPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientMirrorPercentage.setStatus("mandatory")


class _RsWSDMirrorStatus_Type(Integer32):
    """Custom type rsWSDMirrorStatus based on Integer32"""
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


_RsWSDMirrorStatus_Type.__name__ = "Integer32"
_RsWSDMirrorStatus_Object = MibScalar
rsWSDMirrorStatus = _RsWSDMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 43),
    _RsWSDMirrorStatus_Type()
)
rsWSDMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMirrorStatus.setStatus("mandatory")


class _RsWSDMirrorProtocolMode_Type(Integer32):
    """Custom type rsWSDMirrorProtocolMode based on Integer32"""
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


_RsWSDMirrorProtocolMode_Type.__name__ = "Integer32"
_RsWSDMirrorProtocolMode_Object = MibScalar
rsWSDMirrorProtocolMode = _RsWSDMirrorProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 44),
    _RsWSDMirrorProtocolMode_Type()
)
rsWSDMirrorProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMirrorProtocolMode.setStatus("mandatory")
_RsWSDApplicationMirrorTable_Object = MibTable
rsWSDApplicationMirrorTable = _RsWSDApplicationMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45)
)
if mibBuilder.loadTexts:
    rsWSDApplicationMirrorTable.setStatus("mandatory")
_RsWSDApplicationMirrorEntry_Object = MibTableRow
rsWSDApplicationMirrorEntry = _RsWSDApplicationMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45, 1)
)
rsWSDApplicationMirrorEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDMirrorActiveAddress"),
)
if mibBuilder.loadTexts:
    rsWSDApplicationMirrorEntry.setStatus("mandatory")
_RsWSDMirrorActiveAddress_Type = IpAddress
_RsWSDMirrorActiveAddress_Object = MibTableColumn
rsWSDMirrorActiveAddress = _RsWSDMirrorActiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45, 1, 1),
    _RsWSDMirrorActiveAddress_Type()
)
rsWSDMirrorActiveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDMirrorActiveAddress.setStatus("mandatory")


class _RsWSDMirrorActiveStatus_Type(Integer32):
    """Custom type rsWSDMirrorActiveStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RsWSDMirrorActiveStatus_Type.__name__ = "Integer32"
_RsWSDMirrorActiveStatus_Object = MibTableColumn
rsWSDMirrorActiveStatus = _RsWSDMirrorActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45, 1, 2),
    _RsWSDMirrorActiveStatus_Type()
)
rsWSDMirrorActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDMirrorActiveStatus.setStatus("mandatory")
_RsWSDdummy11_Type = Integer32
_RsWSDdummy11_Object = MibScalar
rsWSDdummy11 = _RsWSDdummy11_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 45, 2),
    _RsWSDdummy11_Type()
)
rsWSDdummy11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDdummy11.setStatus("mandatory")
_RsWSDClientMirrorPollingTime_Type = Integer32
_RsWSDClientMirrorPollingTime_Object = MibScalar
rsWSDClientMirrorPollingTime = _RsWSDClientMirrorPollingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 46),
    _RsWSDClientMirrorPollingTime_Type()
)
rsWSDClientMirrorPollingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientMirrorPollingTime.setStatus("mandatory")


class _RsPlatformIdentifier_Type(Integer32):
    """Custom type rsPlatformIdentifier based on Integer32"""
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
        *(("boomer", 5),
          ("cougar", 6),
          ("onecpu", 3),
          ("onecpuh", 4),
          ("vgate", 1),
          ("vgfe", 2))
    )


_RsPlatformIdentifier_Type.__name__ = "Integer32"
_RsPlatformIdentifier_Object = MibScalar
rsPlatformIdentifier = _RsPlatformIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 47),
    _RsPlatformIdentifier_Type()
)
rsPlatformIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPlatformIdentifier.setStatus("mandatory")


class _RsConfigurationIdentifier_Type(Integer32):
    """Custom type rsConfigurationIdentifier based on Integer32"""
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
        *(("chassis", 7),
          ("fixed-16-5", 6),
          ("fixed-2", 3),
          ("fixed-7", 8),
          ("fixed-8", 4),
          ("fixed-8-2", 5),
          ("fourPorts", 2),
          ("twoPorts", 1))
    )


_RsConfigurationIdentifier_Type.__name__ = "Integer32"
_RsConfigurationIdentifier_Object = MibScalar
rsConfigurationIdentifier = _RsConfigurationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 48),
    _RsConfigurationIdentifier_Type()
)
rsConfigurationIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsConfigurationIdentifier.setStatus("mandatory")


class _RsSWPasswordStatus_Type(Integer32):
    """Custom type rsSWPasswordStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passwordOK", 2),
          ("statusUnset", 1),
          ("wrongPassword", 3))
    )


_RsSWPasswordStatus_Type.__name__ = "Integer32"
_RsSWPasswordStatus_Object = MibScalar
rsSWPasswordStatus = _RsSWPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 49),
    _RsSWPasswordStatus_Type()
)
rsSWPasswordStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSWPasswordStatus.setStatus("mandatory")
_RsWSDFlashSize_Type = Integer32
_RsWSDFlashSize_Object = MibScalar
rsWSDFlashSize = _RsWSDFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 50),
    _RsWSDFlashSize_Type()
)
rsWSDFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDFlashSize.setStatus("mandatory")
_RsWSDDRAMSize_Type = Integer32
_RsWSDDRAMSize_Object = MibScalar
rsWSDDRAMSize = _RsWSDDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 51),
    _RsWSDDRAMSize_Type()
)
rsWSDDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDDRAMSize.setStatus("mandatory")


class _RsWSDVLANRedundOperStatus_Type(Integer32):
    """Custom type rsWSDVLANRedundOperStatus based on Integer32"""
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


_RsWSDVLANRedundOperStatus_Type.__name__ = "Integer32"
_RsWSDVLANRedundOperStatus_Object = MibScalar
rsWSDVLANRedundOperStatus = _RsWSDVLANRedundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 52),
    _RsWSDVLANRedundOperStatus_Type()
)
rsWSDVLANRedundOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDVLANRedundOperStatus.setStatus("mandatory")


class _RsWSDResourceUtilization_Type(Integer32):
    """Custom type rsWSDResourceUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDResourceUtilization_Type.__name__ = "Integer32"
_RsWSDResourceUtilization_Object = MibScalar
rsWSDResourceUtilization = _RsWSDResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 53),
    _RsWSDResourceUtilization_Type()
)
rsWSDResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDResourceUtilization.setStatus("mandatory")


class _RsWSDRSResourceUtilization_Type(Integer32):
    """Custom type rsWSDRSResourceUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDRSResourceUtilization_Type.__name__ = "Integer32"
_RsWSDRSResourceUtilization_Object = MibScalar
rsWSDRSResourceUtilization = _RsWSDRSResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 54),
    _RsWSDRSResourceUtilization_Type()
)
rsWSDRSResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDRSResourceUtilization.setStatus("mandatory")


class _RsWSDREResourceUtilization_Type(Integer32):
    """Custom type rsWSDREResourceUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsWSDREResourceUtilization_Type.__name__ = "Integer32"
_RsWSDREResourceUtilization_Object = MibScalar
rsWSDREResourceUtilization = _RsWSDREResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 55),
    _RsWSDREResourceUtilization_Type()
)
rsWSDREResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDREResourceUtilization.setStatus("mandatory")
_RsWSDBuildNumber_Type = DisplayString
_RsWSDBuildNumber_Object = MibScalar
rsWSDBuildNumber = _RsWSDBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 56),
    _RsWSDBuildNumber_Type()
)
rsWSDBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDBuildNumber.setStatus("mandatory")


class _RsWSDUseOneTrap_Type(Integer32):
    """Custom type rsWSDUseOneTrap based on Integer32"""
    defaultValue = 2

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


_RsWSDUseOneTrap_Type.__name__ = "Integer32"
_RsWSDUseOneTrap_Object = MibScalar
rsWSDUseOneTrap = _RsWSDUseOneTrap_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 57),
    _RsWSDUseOneTrap_Type()
)
rsWSDUseOneTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDUseOneTrap.setStatus("mandatory")
_RsWSDSecuredComm_ObjectIdentity = ObjectIdentity
rsWSDSecuredComm = _RsWSDSecuredComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58)
)
_RsWSDSCProtcolsTable_Object = MibTable
rsWSDSCProtcolsTable = _RsWSDSCProtcolsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1)
)
if mibBuilder.loadTexts:
    rsWSDSCProtcolsTable.setStatus("mandatory")
_RsWSDSCProtcolsEntry_Object = MibTableRow
rsWSDSCProtcolsEntry = _RsWSDSCProtcolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1, 1)
)
rsWSDSCProtcolsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDSCProtocol"),
)
if mibBuilder.loadTexts:
    rsWSDSCProtcolsEntry.setStatus("mandatory")


class _RsWSDSCProtocol_Type(Integer32):
    """Custom type rsWSDSCProtocol based on Integer32"""
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
        *(("lrp", 3),
          ("mirror", 6),
          ("prp", 4),
          ("snmp", 1),
          ("srp", 5),
          ("tftp", 2))
    )


_RsWSDSCProtocol_Type.__name__ = "Integer32"
_RsWSDSCProtocol_Object = MibTableColumn
rsWSDSCProtocol = _RsWSDSCProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1, 1, 1),
    _RsWSDSCProtocol_Type()
)
rsWSDSCProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSCProtocol.setStatus("mandatory")


class _RsWSDSCProtocolStatus_Type(Integer32):
    """Custom type rsWSDSCProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 1),
          ("notEncrypted", 2))
    )


_RsWSDSCProtocolStatus_Type.__name__ = "Integer32"
_RsWSDSCProtocolStatus_Object = MibTableColumn
rsWSDSCProtocolStatus = _RsWSDSCProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 58, 1, 1, 2),
    _RsWSDSCProtocolStatus_Type()
)
rsWSDSCProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSCProtocolStatus.setStatus("mandatory")
_RsWSDSNMPPortsTable_Object = MibTable
rsWSDSNMPPortsTable = _RsWSDSNMPPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59)
)
if mibBuilder.loadTexts:
    rsWSDSNMPPortsTable.setStatus("mandatory")
_RsWSDSNMPPortsEntry_Object = MibTableRow
rsWSDSNMPPortsEntry = _RsWSDSNMPPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1)
)
rsWSDSNMPPortsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDSNMPPhysicalPortNumber"),
)
if mibBuilder.loadTexts:
    rsWSDSNMPPortsEntry.setStatus("mandatory")
_RsWSDSNMPPhysicalPortNumber_Type = Integer32
_RsWSDSNMPPhysicalPortNumber_Object = MibTableColumn
rsWSDSNMPPhysicalPortNumber = _RsWSDSNMPPhysicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 1),
    _RsWSDSNMPPhysicalPortNumber_Type()
)
rsWSDSNMPPhysicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortNumber.setStatus("mandatory")


class _RsWSDSNMPPhysicalPortState_Type(Integer32):
    """Custom type rsWSDSNMPPhysicalPortState based on Integer32"""
    defaultValue = 1

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


_RsWSDSNMPPhysicalPortState_Type.__name__ = "Integer32"
_RsWSDSNMPPhysicalPortState_Object = MibTableColumn
rsWSDSNMPPhysicalPortState = _RsWSDSNMPPhysicalPortState_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 59, 1, 2),
    _RsWSDSNMPPhysicalPortState_Type()
)
rsWSDSNMPPhysicalPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSNMPPhysicalPortState.setStatus("mandatory")
_RsBWM_ObjectIdentity = ObjectIdentity
rsBWM = _RsBWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60)
)
_RsWSDTelnetUserTable_Object = MibTable
rsWSDTelnetUserTable = _RsWSDTelnetUserTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61)
)
if mibBuilder.loadTexts:
    rsWSDTelnetUserTable.setStatus("mandatory")
_RsWSDTelnetUserEntry_Object = MibTableRow
rsWSDTelnetUserEntry = _RsWSDTelnetUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1)
)
rsWSDTelnetUserEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDTelnetUserName"),
)
if mibBuilder.loadTexts:
    rsWSDTelnetUserEntry.setStatus("mandatory")


class _RsWSDTelnetUserName_Type(DisplayString):
    """Custom type rsWSDTelnetUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsWSDTelnetUserName_Type.__name__ = "DisplayString"
_RsWSDTelnetUserName_Object = MibTableColumn
rsWSDTelnetUserName = _RsWSDTelnetUserName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 1),
    _RsWSDTelnetUserName_Type()
)
rsWSDTelnetUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserName.setStatus("mandatory")


class _RsWSDTelnetUserPassword_Type(DisplayString):
    """Custom type rsWSDTelnetUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsWSDTelnetUserPassword_Type.__name__ = "DisplayString"
_RsWSDTelnetUserPassword_Object = MibTableColumn
rsWSDTelnetUserPassword = _RsWSDTelnetUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 2),
    _RsWSDTelnetUserPassword_Type()
)
rsWSDTelnetUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserPassword.setStatus("mandatory")


class _RsWSDTelnetUserEAddr_Type(DisplayString):
    """Custom type rsWSDTelnetUserEAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsWSDTelnetUserEAddr_Type.__name__ = "DisplayString"
_RsWSDTelnetUserEAddr_Object = MibTableColumn
rsWSDTelnetUserEAddr = _RsWSDTelnetUserEAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 3),
    _RsWSDTelnetUserEAddr_Type()
)
rsWSDTelnetUserEAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserEAddr.setStatus("mandatory")


class _RsWSDTelnetUserSeverity_Type(Integer32):
    """Custom type rsWSDTelnetUserSeverity based on Integer32"""
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
        *(("error", 4),
          ("fatal", 5),
          ("info", 2),
          ("none", 1),
          ("warning", 3))
    )


_RsWSDTelnetUserSeverity_Type.__name__ = "Integer32"
_RsWSDTelnetUserSeverity_Object = MibTableColumn
rsWSDTelnetUserSeverity = _RsWSDTelnetUserSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 4),
    _RsWSDTelnetUserSeverity_Type()
)
rsWSDTelnetUserSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserSeverity.setStatus("mandatory")
_RsWSDTelnetUserStatus_Type = RowStatus
_RsWSDTelnetUserStatus_Object = MibTableColumn
rsWSDTelnetUserStatus = _RsWSDTelnetUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 5),
    _RsWSDTelnetUserStatus_Type()
)
rsWSDTelnetUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserStatus.setStatus("mandatory")


class _RsWSDTelnetUserGroup_Type(DisplayString):
    """Custom type rsWSDTelnetUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsWSDTelnetUserGroup_Type.__name__ = "DisplayString"
_RsWSDTelnetUserGroup_Object = MibTableColumn
rsWSDTelnetUserGroup = _RsWSDTelnetUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 61, 1, 6),
    _RsWSDTelnetUserGroup_Type()
)
rsWSDTelnetUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetUserGroup.setStatus("mandatory")
_RsWSDTelnetParams_ObjectIdentity = ObjectIdentity
rsWSDTelnetParams = _RsWSDTelnetParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62)
)
_RsWSDTelnetPort_Type = Integer32
_RsWSDTelnetPort_Object = MibScalar
rsWSDTelnetPort = _RsWSDTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62, 1),
    _RsWSDTelnetPort_Type()
)
rsWSDTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetPort.setStatus("mandatory")


class _RsWSDTelnetStatus_Type(Integer32):
    """Custom type rsWSDTelnetStatus based on Integer32"""
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


_RsWSDTelnetStatus_Type.__name__ = "Integer32"
_RsWSDTelnetStatus_Object = MibScalar
rsWSDTelnetStatus = _RsWSDTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62, 2),
    _RsWSDTelnetStatus_Type()
)
rsWSDTelnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetStatus.setStatus("mandatory")
_RsSSD_ObjectIdentity = ObjectIdentity
rsSSD = _RsSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63)
)
_RsSSDvirtualLan_ObjectIdentity = ObjectIdentity
rsSSDvirtualLan = _RsSSDvirtualLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1)
)
_RsSSDvirtualLanTable_Object = MibTable
rsSSDvirtualLanTable = _RsSSDvirtualLanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1)
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanTable.setStatus("mandatory")
_RsSSDvirtualLanEntry_Object = MibTableRow
rsSSDvirtualLanEntry = _RsSSDvirtualLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1)
)
rsSSDvirtualLanEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsSSDvlIfIndex"),
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanEntry.setStatus("mandatory")
_RsSSDvlIfIndex_Type = Integer32
_RsSSDvlIfIndex_Object = MibTableColumn
rsSSDvlIfIndex = _RsSSDvlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 1),
    _RsSSDvlIfIndex_Type()
)
rsSSDvlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlIfIndex.setStatus("mandatory")


class _RsSSDvlProto_Type(Integer32):
    """Custom type rsSSDvlProto based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 11),
          ("decLAT", 9),
          ("decNET", 8),
          ("ip", 2),
          ("ipmulticast", 3),
          ("ipxET", 5),
          ("ipxLLC", 6),
          ("ipxRaw", 4),
          ("ipxSNAP", 7),
          ("netBios", 10),
          ("other", 1),
          ("sna", 13),
          ("swVlan", 15),
          ("userDefined", 14),
          ("xns", 12))
    )


_RsSSDvlProto_Type.__name__ = "Integer32"
_RsSSDvlProto_Object = MibTableColumn
rsSSDvlProto = _RsSSDvlProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 2),
    _RsSSDvlProto_Type()
)
rsSSDvlProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlProto.setStatus("mandatory")
_RsSSDvlAutoConfigEnable_Type = TruthValue
_RsSSDvlAutoConfigEnable_Object = MibTableColumn
rsSSDvlAutoConfigEnable = _RsSSDvlAutoConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 3),
    _RsSSDvlAutoConfigEnable_Type()
)
rsSSDvlAutoConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlAutoConfigEnable.setStatus("mandatory")
_RsSSDvlStatus_Type = RowStatus
_RsSSDvlStatus_Object = MibTableColumn
rsSSDvlStatus = _RsSSDvlStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 4),
    _RsSSDvlStatus_Type()
)
rsSSDvlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlStatus.setStatus("mandatory")


class _RsSSDvlType_Type(Integer32):
    """Custom type rsSSDvlType based on Integer32"""
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
        *(("regular", 1),
          ("specArpReq", 3),
          ("specArpReqAndUnicast", 5),
          ("specBroadcast", 2),
          ("specBroadcastAndUnicast", 4),
          ("specSwitch", 6))
    )


_RsSSDvlType_Type.__name__ = "Integer32"
_RsSSDvlType_Object = MibTableColumn
rsSSDvlType = _RsSSDvlType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 5),
    _RsSSDvlType_Type()
)
rsSSDvlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlType.setStatus("mandatory")


class _RsSSDvlTag_Type(Integer32):
    """Custom type rsSSDvlTag based on Integer32"""
    defaultValue = 0


_RsSSDvlTag_Object = MibTableColumn
rsSSDvlTag = _RsSSDvlTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 6),
    _RsSSDvlTag_Type()
)
rsSSDvlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlTag.setStatus("mandatory")


class _RsSSDvlPriority_Type(Integer32):
    """Custom type rsSSDvlPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_RsSSDvlPriority_Type.__name__ = "Integer32"
_RsSSDvlPriority_Object = MibTableColumn
rsSSDvlPriority = _RsSSDvlPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 1, 1, 7),
    _RsSSDvlPriority_Type()
)
rsSSDvlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvlPriority.setStatus("mandatory")
_RsSSDvirtualLanPortsTable_Object = MibTable
rsSSDvirtualLanPortsTable = _RsSSDvirtualLanPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2)
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanPortsTable.setStatus("mandatory")
_RsSSDvirtualLanPortEntry_Object = MibTableRow
rsSSDvirtualLanPortEntry = _RsSSDvirtualLanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1)
)
rsSSDvirtualLanPortEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsSSDvLIfIndex"),
    (0, "RADWARE-MIB", "rsSSDvLPortIfIndex"),
)
if mibBuilder.loadTexts:
    rsSSDvirtualLanPortEntry.setStatus("mandatory")
_RsSSDvLIfIndex_Type = Integer32
_RsSSDvLIfIndex_Object = MibTableColumn
rsSSDvLIfIndex = _RsSSDvLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 1),
    _RsSSDvLIfIndex_Type()
)
rsSSDvLIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLIfIndex.setStatus("mandatory")
_RsSSDvLPortIfIndex_Type = Integer32
_RsSSDvLPortIfIndex_Object = MibTableColumn
rsSSDvLPortIfIndex = _RsSSDvLPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 2),
    _RsSSDvLPortIfIndex_Type()
)
rsSSDvLPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLPortIfIndex.setStatus("mandatory")


class _RsSSDvLPortType_Type(Integer32):
    """Custom type rsSSDvLPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_RsSSDvLPortType_Type.__name__ = "Integer32"
_RsSSDvLPortType_Object = MibTableColumn
rsSSDvLPortType = _RsSSDvLPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 3),
    _RsSSDvLPortType_Type()
)
rsSSDvLPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSSDvLPortType.setStatus("mandatory")
_RsSSDvLPortStatus_Type = RowStatus
_RsSSDvLPortStatus_Object = MibTableColumn
rsSSDvLPortStatus = _RsSSDvLPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 4),
    _RsSSDvLPortStatus_Type()
)
rsSSDvLPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLPortStatus.setStatus("mandatory")


class _RsSSDvLPortTag_Type(Integer32):
    """Custom type rsSSDvLPortTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 2),
          ("untag", 1))
    )


_RsSSDvLPortTag_Type.__name__ = "Integer32"
_RsSSDvLPortTag_Object = MibTableColumn
rsSSDvLPortTag = _RsSSDvLPortTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 63, 1, 2, 1, 5),
    _RsSSDvLPortTag_Type()
)
rsSSDvLPortTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSSDvLPortTag.setStatus("mandatory")
_RsWSDThresholdWarnings_ObjectIdentity = ObjectIdentity
rsWSDThresholdWarnings = _RsWSDThresholdWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64)
)


class _RsWSDThreshTrapFloodDelay_Type(Integer32):
    """Custom type rsWSDThreshTrapFloodDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RsWSDThreshTrapFloodDelay_Type.__name__ = "Integer32"
_RsWSDThreshTrapFloodDelay_Object = MibScalar
rsWSDThreshTrapFloodDelay = _RsWSDThreshTrapFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 1),
    _RsWSDThreshTrapFloodDelay_Type()
)
rsWSDThreshTrapFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDThreshTrapFloodDelay.setStatus("mandatory")


class _RsWSDCriticalTrapFloodDelay_Type(Integer32):
    """Custom type rsWSDCriticalTrapFloodDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RsWSDCriticalTrapFloodDelay_Type.__name__ = "Integer32"
_RsWSDCriticalTrapFloodDelay_Object = MibScalar
rsWSDCriticalTrapFloodDelay = _RsWSDCriticalTrapFloodDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 64, 2),
    _RsWSDCriticalTrapFloodDelay_Type()
)
rsWSDCriticalTrapFloodDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDCriticalTrapFloodDelay.setStatus("mandatory")
_RsIDS_ObjectIdentity = ObjectIdentity
rsIDS = _RsIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 65)
)


class _RsWSDLicense_Type(DisplayString):
    """Custom type rsWSDLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDLicense_Type.__name__ = "DisplayString"
_RsWSDLicense_Object = MibScalar
rsWSDLicense = _RsWSDLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 66),
    _RsWSDLicense_Type()
)
rsWSDLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDLicense.setStatus("mandatory")
_RsErrMailParams_ObjectIdentity = ObjectIdentity
rsErrMailParams = _RsErrMailParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67)
)


class _RsErrMailEnable_Type(Integer32):
    """Custom type rsErrMailEnable based on Integer32"""
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


_RsErrMailEnable_Type.__name__ = "Integer32"
_RsErrMailEnable_Object = MibScalar
rsErrMailEnable = _RsErrMailEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67, 1),
    _RsErrMailEnable_Type()
)
rsErrMailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsErrMailEnable.setStatus("mandatory")
_RsErrMailGateway_Type = IpAddress
_RsErrMailGateway_Object = MibScalar
rsErrMailGateway = _RsErrMailGateway_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67, 2),
    _RsErrMailGateway_Type()
)
rsErrMailGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsErrMailGateway.setStatus("mandatory")


class _RsErrMailSrcAddress_Type(DisplayString):
    """Custom type rsErrMailSrcAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RsErrMailSrcAddress_Type.__name__ = "DisplayString"
_RsErrMailSrcAddress_Object = MibScalar
rsErrMailSrcAddress = _RsErrMailSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 67, 3),
    _RsErrMailSrcAddress_Type()
)
rsErrMailSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsErrMailSrcAddress.setStatus("mandatory")
_RsWSDWebParams_ObjectIdentity = ObjectIdentity
rsWSDWebParams = _RsWSDWebParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68)
)
_RsWSDWebPort_Type = Integer32
_RsWSDWebPort_Object = MibScalar
rsWSDWebPort = _RsWSDWebPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 1),
    _RsWSDWebPort_Type()
)
rsWSDWebPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebPort.setStatus("mandatory")


class _RsWSDWebStatus_Type(Integer32):
    """Custom type rsWSDWebStatus based on Integer32"""
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


_RsWSDWebStatus_Type.__name__ = "Integer32"
_RsWSDWebStatus_Object = MibScalar
rsWSDWebStatus = _RsWSDWebStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 2),
    _RsWSDWebStatus_Type()
)
rsWSDWebStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebStatus.setStatus("mandatory")


class _RsWSDWebHelpLocation_Type(DisplayString):
    """Custom type rsWSDWebHelpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDWebHelpLocation_Type.__name__ = "DisplayString"
_RsWSDWebHelpLocation_Object = MibScalar
rsWSDWebHelpLocation = _RsWSDWebHelpLocation_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 68, 3),
    _RsWSDWebHelpLocation_Type()
)
rsWSDWebHelpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDWebHelpLocation.setStatus("mandatory")
_RsWSDSysParams_ObjectIdentity = ObjectIdentity
rsWSDSysParams = _RsWSDSysParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69)
)
_RsWSDSysFlashSize_Type = Integer32
_RsWSDSysFlashSize_Object = MibScalar
rsWSDSysFlashSize = _RsWSDSysFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 1),
    _RsWSDSysFlashSize_Type()
)
rsWSDSysFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSysFlashSize.setStatus("mandatory")
_RsWSDSysUpTime_Type = DisplayString
_RsWSDSysUpTime_Object = MibScalar
rsWSDSysUpTime = _RsWSDSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 2),
    _RsWSDSysUpTime_Type()
)
rsWSDSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDSysUpTime.setStatus("mandatory")


class _RsWSDSysManagedTime_Type(DisplayString):
    """Custom type rsWSDSysManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDSysManagedTime_Type.__name__ = "DisplayString"
_RsWSDSysManagedTime_Object = MibScalar
rsWSDSysManagedTime = _RsWSDSysManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 3),
    _RsWSDSysManagedTime_Type()
)
rsWSDSysManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSysManagedTime.setStatus("mandatory")


class _RsWSDSysManagedDate_Type(DisplayString):
    """Custom type rsWSDSysManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RsWSDSysManagedDate_Type.__name__ = "DisplayString"
_RsWSDSysManagedDate_Object = MibScalar
rsWSDSysManagedDate = _RsWSDSysManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 69, 4),
    _RsWSDSysManagedDate_Type()
)
rsWSDSysManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSysManagedDate.setStatus("mandatory")


class _RsWSDLicenseID_Type(DisplayString):
    """Custom type rsWSDLicenseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsWSDLicenseID_Type.__name__ = "DisplayString"
_RsWSDLicenseID_Object = MibScalar
rsWSDLicenseID = _RsWSDLicenseID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 70),
    _RsWSDLicenseID_Type()
)
rsWSDLicenseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDLicenseID.setStatus("mandatory")


class _RsWSDSendFakeArp_Type(Integer32):
    """Custom type rsWSDSendFakeArp based on Integer32"""
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


_RsWSDSendFakeArp_Type.__name__ = "Integer32"
_RsWSDSendFakeArp_Object = MibScalar
rsWSDSendFakeArp = _RsWSDSendFakeArp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 71),
    _RsWSDSendFakeArp_Type()
)
rsWSDSendFakeArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSendFakeArp.setStatus("mandatory")
_RsWSDNTP_ObjectIdentity = ObjectIdentity
rsWSDNTP = _RsWSDNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72)
)
_RsWSDNTPServerAddr_Type = IpAddress
_RsWSDNTPServerAddr_Object = MibScalar
rsWSDNTPServerAddr = _RsWSDNTPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 1),
    _RsWSDNTPServerAddr_Type()
)
rsWSDNTPServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPServerAddr.setStatus("mandatory")
_RsWSDNTPInterval_Type = Integer32
_RsWSDNTPInterval_Object = MibScalar
rsWSDNTPInterval = _RsWSDNTPInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 2),
    _RsWSDNTPInterval_Type()
)
rsWSDNTPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPInterval.setStatus("mandatory")


class _RsWSDNTPStatus_Type(Integer32):
    """Custom type rsWSDNTPStatus based on Integer32"""
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


_RsWSDNTPStatus_Type.__name__ = "Integer32"
_RsWSDNTPStatus_Object = MibScalar
rsWSDNTPStatus = _RsWSDNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 3),
    _RsWSDNTPStatus_Type()
)
rsWSDNTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPStatus.setStatus("mandatory")


class _RsWSDNTPTimeZone_Type(DisplayString):
    """Custom type rsWSDNTPTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RsWSDNTPTimeZone_Type.__name__ = "DisplayString"
_RsWSDNTPTimeZone_Object = MibScalar
rsWSDNTPTimeZone = _RsWSDNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 4),
    _RsWSDNTPTimeZone_Type()
)
rsWSDNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPTimeZone.setStatus("mandatory")
_RsWSDNTPPort_Type = Integer32
_RsWSDNTPPort_Object = MibScalar
rsWSDNTPPort = _RsWSDNTPPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 72, 5),
    _RsWSDNTPPort_Type()
)
rsWSDNTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDNTPPort.setStatus("mandatory")
_RsStatistics_ObjectIdentity = ObjectIdentity
rsStatistics = _RsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 73)
)
_RsPhysPortMirrorTable_Object = MibTable
rsPhysPortMirrorTable = _RsPhysPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74)
)
if mibBuilder.loadTexts:
    rsPhysPortMirrorTable.setStatus("mandatory")
_RsPhysPortMirrorEntry_Object = MibTableRow
rsPhysPortMirrorEntry = _RsPhysPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1)
)
rsPhysPortMirrorEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsPhysPortMirrorSrcInf"),
    (0, "RADWARE-MIB", "rsPhysPortMirrorDstPort"),
)
if mibBuilder.loadTexts:
    rsPhysPortMirrorEntry.setStatus("mandatory")
_RsPhysPortMirrorSrcInf_Type = Integer32
_RsPhysPortMirrorSrcInf_Object = MibTableColumn
rsPhysPortMirrorSrcInf = _RsPhysPortMirrorSrcInf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 1),
    _RsPhysPortMirrorSrcInf_Type()
)
rsPhysPortMirrorSrcInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorSrcInf.setStatus("mandatory")
_RsPhysPortMirrorDstPort_Type = Integer32
_RsPhysPortMirrorDstPort_Object = MibTableColumn
rsPhysPortMirrorDstPort = _RsPhysPortMirrorDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 2),
    _RsPhysPortMirrorDstPort_Type()
)
rsPhysPortMirrorDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorDstPort.setStatus("mandatory")


class _RsPhysPortMirrorRxTx_Type(Integer32):
    """Custom type rsPhysPortMirrorRxTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copyRxOnly", 2),
          ("copyRxTx", 1),
          ("copyTxOnly", 3))
    )


_RsPhysPortMirrorRxTx_Type.__name__ = "Integer32"
_RsPhysPortMirrorRxTx_Object = MibTableColumn
rsPhysPortMirrorRxTx = _RsPhysPortMirrorRxTx_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 3),
    _RsPhysPortMirrorRxTx_Type()
)
rsPhysPortMirrorRxTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorRxTx.setStatus("mandatory")


class _RsPhysPortMirrorRxBroadCast_Type(Integer32):
    """Custom type rsPhysPortMirrorRxBroadCast based on Integer32"""
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


_RsPhysPortMirrorRxBroadCast_Type.__name__ = "Integer32"
_RsPhysPortMirrorRxBroadCast_Object = MibTableColumn
rsPhysPortMirrorRxBroadCast = _RsPhysPortMirrorRxBroadCast_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 4),
    _RsPhysPortMirrorRxBroadCast_Type()
)
rsPhysPortMirrorRxBroadCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorRxBroadCast.setStatus("mandatory")
_RsPhysPortMirrorStatus_Type = RowStatus
_RsPhysPortMirrorStatus_Object = MibTableColumn
rsPhysPortMirrorStatus = _RsPhysPortMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 5),
    _RsPhysPortMirrorStatus_Type()
)
rsPhysPortMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorStatus.setStatus("mandatory")
_RsPhysPortMirrorBackupDstPort_Type = Integer32
_RsPhysPortMirrorBackupDstPort_Object = MibTableColumn
rsPhysPortMirrorBackupDstPort = _RsPhysPortMirrorBackupDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 6),
    _RsPhysPortMirrorBackupDstPort_Type()
)
rsPhysPortMirrorBackupDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPhysPortMirrorBackupDstPort.setStatus("mandatory")


class _RsPhysPortMirrorDstStatus_Type(Integer32):
    """Custom type rsPhysPortMirrorDstStatus based on Integer32"""
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
        *(("active", 1),
          ("checkIDSFail", 3),
          ("checkIDSFailAndPortDown", 4),
          ("portDown", 2))
    )


_RsPhysPortMirrorDstStatus_Type.__name__ = "Integer32"
_RsPhysPortMirrorDstStatus_Object = MibTableColumn
rsPhysPortMirrorDstStatus = _RsPhysPortMirrorDstStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 7),
    _RsPhysPortMirrorDstStatus_Type()
)
rsPhysPortMirrorDstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorDstStatus.setStatus("mandatory")


class _RsPhysPortMirrorBackupStatus_Type(Integer32):
    """Custom type rsPhysPortMirrorBackupStatus based on Integer32"""
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
        *(("active", 1),
          ("checkIDSFail", 3),
          ("checkIDSFailAndPortDown", 4),
          ("none", 5),
          ("portDown", 2))
    )


_RsPhysPortMirrorBackupStatus_Type.__name__ = "Integer32"
_RsPhysPortMirrorBackupStatus_Object = MibTableColumn
rsPhysPortMirrorBackupStatus = _RsPhysPortMirrorBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 8),
    _RsPhysPortMirrorBackupStatus_Type()
)
rsPhysPortMirrorBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorBackupStatus.setStatus("mandatory")


class _RsPhysPortMirrorActiveDstPort_Type(Integer32):
    """Custom type rsPhysPortMirrorActiveDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupPort", 2),
          ("dstPort", 1),
          ("none", 3))
    )


_RsPhysPortMirrorActiveDstPort_Type.__name__ = "Integer32"
_RsPhysPortMirrorActiveDstPort_Object = MibTableColumn
rsPhysPortMirrorActiveDstPort = _RsPhysPortMirrorActiveDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 74, 1, 9),
    _RsPhysPortMirrorActiveDstPort_Type()
)
rsPhysPortMirrorActiveDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPhysPortMirrorActiveDstPort.setStatus("mandatory")
_RsCP_ObjectIdentity = ObjectIdentity
rsCP = _RsCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 75)
)
_RsVWSD_ObjectIdentity = ObjectIdentity
rsVWSD = _RsVWSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76)
)
_RsVWSDDataPermissionsTable_Object = MibTable
rsVWSDDataPermissionsTable = _RsVWSDDataPermissionsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1)
)
if mibBuilder.loadTexts:
    rsVWSDDataPermissionsTable.setStatus("mandatory")
_RsVWSDDataPermissionsTableEntry_Object = MibTableRow
rsVWSDDataPermissionsTableEntry = _RsVWSDDataPermissionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1)
)
rsVWSDDataPermissionsTableEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsVWSDUserGroup"),
    (0, "RADWARE-MIB", "rsVWSDDataType"),
    (0, "RADWARE-MIB", "rsVWSDDataItems"),
)
if mibBuilder.loadTexts:
    rsVWSDDataPermissionsTableEntry.setStatus("mandatory")


class _RsVWSDUserGroup_Type(DisplayString):
    """Custom type rsVWSDUserGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RsVWSDUserGroup_Type.__name__ = "DisplayString"
_RsVWSDUserGroup_Object = MibTableColumn
rsVWSDUserGroup = _RsVWSDUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 1),
    _RsVWSDUserGroup_Type()
)
rsVWSDUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVWSDUserGroup.setStatus("mandatory")


class _RsVWSDDataType_Type(OctetString):
    """Custom type rsVWSDDataType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsVWSDDataType_Type.__name__ = "OctetString"
_RsVWSDDataType_Object = MibTableColumn
rsVWSDDataType = _RsVWSDDataType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 2),
    _RsVWSDDataType_Type()
)
rsVWSDDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVWSDDataType.setStatus("mandatory")


class _RsVWSDDataItems_Type(OctetString):
    """Custom type rsVWSDDataItems based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsVWSDDataItems_Type.__name__ = "OctetString"
_RsVWSDDataItems_Object = MibTableColumn
rsVWSDDataItems = _RsVWSDDataItems_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 3),
    _RsVWSDDataItems_Type()
)
rsVWSDDataItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVWSDDataItems.setStatus("mandatory")
_RsVWSDDataStatus_Type = RowStatus
_RsVWSDDataStatus_Object = MibTableColumn
rsVWSDDataStatus = _RsVWSDDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 76, 1, 1, 4),
    _RsVWSDDataStatus_Type()
)
rsVWSDDataStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsVWSDDataStatus.setStatus("mandatory")


class _RsWSDManagementPorts_Type(Integer32):
    """Custom type rsWSDManagementPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("outOfPath", 1),
          ("promiscuous", 3),
          ("switch", 2))
    )


_RsWSDManagementPorts_Type.__name__ = "Integer32"
_RsWSDManagementPorts_Object = MibScalar
rsWSDManagementPorts = _RsWSDManagementPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 77),
    _RsWSDManagementPorts_Type()
)
rsWSDManagementPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDManagementPorts.setStatus("mandatory")
_RsWSDManagementPortsTable_Object = MibTable
rsWSDManagementPortsTable = _RsWSDManagementPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78)
)
if mibBuilder.loadTexts:
    rsWSDManagementPortsTable.setStatus("mandatory")
_RsWSDManagementPortsEntry_Object = MibTableRow
rsWSDManagementPortsEntry = _RsWSDManagementPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78, 1)
)
rsWSDManagementPortsEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDPortIndex"),
)
if mibBuilder.loadTexts:
    rsWSDManagementPortsEntry.setStatus("mandatory")
_RsWSDPortIndex_Type = Integer32
_RsWSDPortIndex_Object = MibTableColumn
rsWSDPortIndex = _RsWSDPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78, 1, 1),
    _RsWSDPortIndex_Type()
)
rsWSDPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPortIndex.setStatus("mandatory")


class _RsWSDPortOperation_Type(Integer32):
    """Custom type rsWSDPortOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("management", 1),
          ("sniffer", 2))
    )


_RsWSDPortOperation_Type.__name__ = "Integer32"
_RsWSDPortOperation_Object = MibTableColumn
rsWSDPortOperation = _RsWSDPortOperation_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 78, 1, 2),
    _RsWSDPortOperation_Type()
)
rsWSDPortOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDPortOperation.setStatus("mandatory")
_RsCCK_ObjectIdentity = ObjectIdentity
rsCCK = _RsCCK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 79)
)
_RsWSDSshParams_ObjectIdentity = ObjectIdentity
rsWSDSshParams = _RsWSDSshParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80)
)
_RsWSDSshPort_Type = Integer32
_RsWSDSshPort_Object = MibScalar
rsWSDSshPort = _RsWSDSshPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 1),
    _RsWSDSshPort_Type()
)
rsWSDSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshPort.setStatus("mandatory")


class _RsWSDSshStatus_Type(Integer32):
    """Custom type rsWSDSshStatus based on Integer32"""
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


_RsWSDSshStatus_Type.__name__ = "Integer32"
_RsWSDSshStatus_Object = MibScalar
rsWSDSshStatus = _RsWSDSshStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 2),
    _RsWSDSshStatus_Type()
)
rsWSDSshStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshStatus.setStatus("mandatory")
_RsWSDHttpsParams_ObjectIdentity = ObjectIdentity
rsWSDHttpsParams = _RsWSDHttpsParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 81)
)
_RsWSDHttpsPort_Type = Integer32
_RsWSDHttpsPort_Object = MibScalar
rsWSDHttpsPort = _RsWSDHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 81, 1),
    _RsWSDHttpsPort_Type()
)
rsWSDHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHttpsPort.setStatus("mandatory")


class _RsWSDHttpsStatus_Type(Integer32):
    """Custom type rsWSDHttpsStatus based on Integer32"""
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


_RsWSDHttpsStatus_Type.__name__ = "Integer32"
_RsWSDHttpsStatus_Object = MibScalar
rsWSDHttpsStatus = _RsWSDHttpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 81, 2),
    _RsWSDHttpsStatus_Type()
)
rsWSDHttpsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDHttpsStatus.setStatus("mandatory")
_RsWSDStaticForwardingTable_Object = MibTable
rsWSDStaticForwardingTable = _RsWSDStaticForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82)
)
if mibBuilder.loadTexts:
    rsWSDStaticForwardingTable.setStatus("mandatory")
_RsWSDStaticForwardingEntry_Object = MibTableRow
rsWSDStaticForwardingEntry = _RsWSDStaticForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1)
)
rsWSDStaticForwardingEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsWSDStaticSourcePort"),
)
if mibBuilder.loadTexts:
    rsWSDStaticForwardingEntry.setStatus("mandatory")
_RsWSDStaticSourcePort_Type = Integer32
_RsWSDStaticSourcePort_Object = MibTableColumn
rsWSDStaticSourcePort = _RsWSDStaticSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 1),
    _RsWSDStaticSourcePort_Type()
)
rsWSDStaticSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDStaticSourcePort.setStatus("mandatory")
_RsWSDStaticDestinationPort_Type = Integer32
_RsWSDStaticDestinationPort_Object = MibTableColumn
rsWSDStaticDestinationPort = _RsWSDStaticDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 2),
    _RsWSDStaticDestinationPort_Type()
)
rsWSDStaticDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticDestinationPort.setStatus("mandatory")


class _RsWSDStaticPortOperation_Type(Integer32):
    """Custom type rsWSDStaticPortOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 2),
          ("process", 1))
    )


_RsWSDStaticPortOperation_Type.__name__ = "Integer32"
_RsWSDStaticPortOperation_Object = MibTableColumn
rsWSDStaticPortOperation = _RsWSDStaticPortOperation_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 3),
    _RsWSDStaticPortOperation_Type()
)
rsWSDStaticPortOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticPortOperation.setStatus("mandatory")
_RsWSDStaticStatus_Type = RowStatus
_RsWSDStaticStatus_Object = MibTableColumn
rsWSDStaticStatus = _RsWSDStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 82, 1, 4),
    _RsWSDStaticStatus_Type()
)
rsWSDStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDStaticStatus.setStatus("mandatory")
_RsRadiusServer_ObjectIdentity = ObjectIdentity
rsRadiusServer = _RsRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83)
)
_RsRadiusMainServerAddr_Type = IpAddress
_RsRadiusMainServerAddr_Object = MibScalar
rsRadiusMainServerAddr = _RsRadiusMainServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 1),
    _RsRadiusMainServerAddr_Type()
)
rsRadiusMainServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMainServerAddr.setStatus("mandatory")
_RsRadiusMainServerPort_Type = Integer32
_RsRadiusMainServerPort_Object = MibScalar
rsRadiusMainServerPort = _RsRadiusMainServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 2),
    _RsRadiusMainServerPort_Type()
)
rsRadiusMainServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMainServerPort.setStatus("mandatory")


class _RsRadiusMainServerSecret_Type(DisplayString):
    """Custom type rsRadiusMainServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsRadiusMainServerSecret_Type.__name__ = "DisplayString"
_RsRadiusMainServerSecret_Object = MibScalar
rsRadiusMainServerSecret = _RsRadiusMainServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 3),
    _RsRadiusMainServerSecret_Type()
)
rsRadiusMainServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusMainServerSecret.setStatus("mandatory")
_RsRadiusBackupServerAddr_Type = IpAddress
_RsRadiusBackupServerAddr_Object = MibScalar
rsRadiusBackupServerAddr = _RsRadiusBackupServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 4),
    _RsRadiusBackupServerAddr_Type()
)
rsRadiusBackupServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusBackupServerAddr.setStatus("mandatory")
_RsRadiusBackupServerPort_Type = Integer32
_RsRadiusBackupServerPort_Object = MibScalar
rsRadiusBackupServerPort = _RsRadiusBackupServerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 5),
    _RsRadiusBackupServerPort_Type()
)
rsRadiusBackupServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusBackupServerPort.setStatus("mandatory")


class _RsRadiusBackupServerSecret_Type(DisplayString):
    """Custom type rsRadiusBackupServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsRadiusBackupServerSecret_Type.__name__ = "DisplayString"
_RsRadiusBackupServerSecret_Object = MibScalar
rsRadiusBackupServerSecret = _RsRadiusBackupServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 6),
    _RsRadiusBackupServerSecret_Type()
)
rsRadiusBackupServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusBackupServerSecret.setStatus("mandatory")


class _RsAuthenticationMethod_Type(Integer32):
    """Custom type rsAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("combined", 3),
          ("radius", 2),
          ("userTable", 1))
    )


_RsAuthenticationMethod_Type.__name__ = "Integer32"
_RsAuthenticationMethod_Object = MibScalar
rsAuthenticationMethod = _RsAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 7),
    _RsAuthenticationMethod_Type()
)
rsAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAuthenticationMethod.setStatus("mandatory")


class _RsRadiusServerTimeout_Type(Integer32):
    """Custom type rsRadiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsRadiusServerTimeout_Type.__name__ = "Integer32"
_RsRadiusServerTimeout_Object = MibScalar
rsRadiusServerTimeout = _RsRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 8),
    _RsRadiusServerTimeout_Type()
)
rsRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusServerTimeout.setStatus("mandatory")


class _RsRadiusServerRetries_Type(Integer32):
    """Custom type rsRadiusServerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RsRadiusServerRetries_Type.__name__ = "Integer32"
_RsRadiusServerRetries_Object = MibScalar
rsRadiusServerRetries = _RsRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 83, 9),
    _RsRadiusServerRetries_Type()
)
rsRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusServerRetries.setStatus("mandatory")
_RsIfTable_Object = MibTable
rsIfTable = _RsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84)
)
if mibBuilder.loadTexts:
    rsIfTable.setStatus("mandatory")
_RsIfEntry_Object = MibTableRow
rsIfEntry = _RsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1)
)
rsIfEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIfIndex"),
)
if mibBuilder.loadTexts:
    rsIfEntry.setStatus("mandatory")
_RsIfIndex_Type = Integer32
_RsIfIndex_Object = MibTableColumn
rsIfIndex = _RsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 1),
    _RsIfIndex_Type()
)
rsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfIndex.setStatus("mandatory")


class _RsIfSpeed_Type(Integer32):
    """Custom type rsIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eth10", 1),
          ("fe100", 2),
          ("ge1000", 3))
    )


_RsIfSpeed_Type.__name__ = "Integer32"
_RsIfSpeed_Object = MibTableColumn
rsIfSpeed = _RsIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 2),
    _RsIfSpeed_Type()
)
rsIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfSpeed.setStatus("mandatory")


class _RsIfDuplex_Type(Integer32):
    """Custom type rsIfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_RsIfDuplex_Type.__name__ = "Integer32"
_RsIfDuplex_Object = MibTableColumn
rsIfDuplex = _RsIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 3),
    _RsIfDuplex_Type()
)
rsIfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfDuplex.setStatus("mandatory")


class _RsIfAutoNegotiate_Type(Integer32):
    """Custom type rsIfAutoNegotiate based on Integer32"""
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


_RsIfAutoNegotiate_Type.__name__ = "Integer32"
_RsIfAutoNegotiate_Object = MibTableColumn
rsIfAutoNegotiate = _RsIfAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 4),
    _RsIfAutoNegotiate_Type()
)
rsIfAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfAutoNegotiate.setStatus("mandatory")
_RsIfRowStatus_Type = RowStatus
_RsIfRowStatus_Object = MibTableColumn
rsIfRowStatus = _RsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 84, 1, 5),
    _RsIfRowStatus_Type()
)
rsIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIfRowStatus.setStatus("mandatory")


class _RsWSDDeviceOperationMode_Type(Integer32):
    """Custom type rsWSDDeviceOperationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("staticForwarding", 2),
          ("trafficRedirection", 1))
    )


_RsWSDDeviceOperationMode_Type.__name__ = "Integer32"
_RsWSDDeviceOperationMode_Object = MibScalar
rsWSDDeviceOperationMode = _RsWSDDeviceOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 85),
    _RsWSDDeviceOperationMode_Type()
)
rsWSDDeviceOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDeviceOperationMode.setStatus("mandatory")


class _RsWSDVersionStatus_Type(Integer32):
    """Custom type rsWSDVersionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("final", 2),
          ("open", 1))
    )


_RsWSDVersionStatus_Type.__name__ = "Integer32"
_RsWSDVersionStatus_Object = MibScalar
rsWSDVersionStatus = _RsWSDVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 86),
    _RsWSDVersionStatus_Type()
)
rsWSDVersionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsWSDVersionStatus.setStatus("mandatory")
_RndMidLevelManagement_ObjectIdentity = ObjectIdentity
rndMidLevelManagement = _RndMidLevelManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 2)
)
_RndAlarmOptions_ObjectIdentity = ObjectIdentity
rndAlarmOptions = _RndAlarmOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 2)
)


class _RndAlarmEnabling_Type(Integer32):
    """Custom type rndAlarmEnabling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RndAlarmEnabling_Type.__name__ = "Integer32"
_RndAlarmEnabling_Object = MibScalar
rndAlarmEnabling = _RndAlarmEnabling_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 2, 1),
    _RndAlarmEnabling_Type()
)
rndAlarmEnabling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmEnabling.setStatus("mandatory")
_RndAlarmInterval_Type = Integer32
_RndAlarmInterval_Object = MibScalar
rndAlarmInterval = _RndAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 2, 2),
    _RndAlarmInterval_Type()
)
rndAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmInterval.setStatus("mandatory")
_RndMonitoredElementsTable_Object = MibTable
rndMonitoredElementsTable = _RndMonitoredElementsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3)
)
if mibBuilder.loadTexts:
    rndMonitoredElementsTable.setStatus("mandatory")
_RndMonitoredElementEntry_Object = MibTableRow
rndMonitoredElementEntry = _RndMonitoredElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1)
)
rndMonitoredElementEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndMonitoredElementAddress"),
)
if mibBuilder.loadTexts:
    rndMonitoredElementEntry.setStatus("mandatory")
_RndMonitoredElementAddress_Type = IpAddress
_RndMonitoredElementAddress_Object = MibTableColumn
rndMonitoredElementAddress = _RndMonitoredElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 1),
    _RndMonitoredElementAddress_Type()
)
rndMonitoredElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredElementAddress.setStatus("mandatory")


class _RndMonitoredElementCommunity_Type(DisplayString):
    """Custom type rndMonitoredElementCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElementCommunity_Type.__name__ = "DisplayString"
_RndMonitoredElementCommunity_Object = MibTableColumn
rndMonitoredElementCommunity = _RndMonitoredElementCommunity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 2),
    _RndMonitoredElementCommunity_Type()
)
rndMonitoredElementCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementCommunity.setStatus("mandatory")


class _RndMonitoredElementLabel_Type(DisplayString):
    """Custom type rndMonitoredElementLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElementLabel_Type.__name__ = "DisplayString"
_RndMonitoredElementLabel_Object = MibTableColumn
rndMonitoredElementLabel = _RndMonitoredElementLabel_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 3),
    _RndMonitoredElementLabel_Type()
)
rndMonitoredElementLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementLabel.setStatus("mandatory")
_RndDefaultPollingInterval_Type = Integer32
_RndDefaultPollingInterval_Object = MibTableColumn
rndDefaultPollingInterval = _RndDefaultPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 4),
    _RndDefaultPollingInterval_Type()
)
rndDefaultPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDefaultPollingInterval.setStatus("mandatory")
_RndDefaultLogFile_Type = DisplayString
_RndDefaultLogFile_Object = MibTableColumn
rndDefaultLogFile = _RndDefaultLogFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 5),
    _RndDefaultLogFile_Type()
)
rndDefaultLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDefaultLogFile.setStatus("mandatory")
_RndMonitoredElementStatus_Type = RowStatus
_RndMonitoredElementStatus_Object = MibTableColumn
rndMonitoredElementStatus = _RndMonitoredElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 3, 1, 6),
    _RndMonitoredElementStatus_Type()
)
rndMonitoredElementStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementStatus.setStatus("mandatory")
_RndMonitoringTable_Object = MibTable
rndMonitoringTable = _RndMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4)
)
if mibBuilder.loadTexts:
    rndMonitoringTable.setStatus("mandatory")
_RndMonitoringEntry_Object = MibTableRow
rndMonitoringEntry = _RndMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1)
)
rndMonitoringEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndMonitoredElement"),
    (0, "RADWARE-MIB", "rndMonitoredObjectInstanceLabel"),
)
if mibBuilder.loadTexts:
    rndMonitoringEntry.setStatus("mandatory")


class _RndMonitoredElement_Type(DisplayString):
    """Custom type rndMonitoredElement based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElement_Type.__name__ = "DisplayString"
_RndMonitoredElement_Object = MibTableColumn
rndMonitoredElement = _RndMonitoredElement_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 1),
    _RndMonitoredElement_Type()
)
rndMonitoredElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredElement.setStatus("mandatory")


class _RndMonitoredObjectInstanceLabel_Type(DisplayString):
    """Custom type rndMonitoredObjectInstanceLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredObjectInstanceLabel_Type.__name__ = "DisplayString"
_RndMonitoredObjectInstanceLabel_Object = MibTableColumn
rndMonitoredObjectInstanceLabel = _RndMonitoredObjectInstanceLabel_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 2),
    _RndMonitoredObjectInstanceLabel_Type()
)
rndMonitoredObjectInstanceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredObjectInstanceLabel.setStatus("mandatory")


class _RndMonitoredObjectName_Type(DisplayString):
    """Custom type rndMonitoredObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RndMonitoredObjectName_Type.__name__ = "DisplayString"
_RndMonitoredObjectName_Object = MibTableColumn
rndMonitoredObjectName = _RndMonitoredObjectName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 3),
    _RndMonitoredObjectName_Type()
)
rndMonitoredObjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectName.setStatus("mandatory")
_RndMonitoredObjectIdentifier_Type = ObjectIdentifier
_RndMonitoredObjectIdentifier_Object = MibTableColumn
rndMonitoredObjectIdentifier = _RndMonitoredObjectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 4),
    _RndMonitoredObjectIdentifier_Type()
)
rndMonitoredObjectIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectIdentifier.setStatus("mandatory")
_RndMonitoredObjectInstance_Type = ObjectIdentifier
_RndMonitoredObjectInstance_Object = MibTableColumn
rndMonitoredObjectInstance = _RndMonitoredObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 5),
    _RndMonitoredObjectInstance_Type()
)
rndMonitoredObjectInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectInstance.setStatus("mandatory")


class _RndMonitoredObjectSyntax_Type(Integer32):
    """Custom type rndMonitoredObjectSyntax based on Integer32"""
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
        *(("integer", 1),
          ("ip-address", 3),
          ("object-identifier", 4),
          ("octet-string", 2))
    )


_RndMonitoredObjectSyntax_Type.__name__ = "Integer32"
_RndMonitoredObjectSyntax_Object = MibTableColumn
rndMonitoredObjectSyntax = _RndMonitoredObjectSyntax_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 6),
    _RndMonitoredObjectSyntax_Type()
)
rndMonitoredObjectSyntax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectSyntax.setStatus("mandatory")
_RndMonitoringInterval_Type = Integer32
_RndMonitoringInterval_Object = MibTableColumn
rndMonitoringInterval = _RndMonitoringInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 7),
    _RndMonitoringInterval_Type()
)
rndMonitoringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringInterval.setStatus("mandatory")
_RndAlarmMaxTreshold_Type = Integer32
_RndAlarmMaxTreshold_Object = MibTableColumn
rndAlarmMaxTreshold = _RndAlarmMaxTreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 8),
    _RndAlarmMaxTreshold_Type()
)
rndAlarmMaxTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmMaxTreshold.setStatus("mandatory")
_RndAlarmMinTreshold_Type = Integer32
_RndAlarmMinTreshold_Object = MibTableColumn
rndAlarmMinTreshold = _RndAlarmMinTreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 9),
    _RndAlarmMinTreshold_Type()
)
rndAlarmMinTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmMinTreshold.setStatus("mandatory")
_RndMonitoringLogfile_Type = DisplayString
_RndMonitoringLogfile_Object = MibTableColumn
rndMonitoringLogfile = _RndMonitoringLogfile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 10),
    _RndMonitoringLogfile_Type()
)
rndMonitoringLogfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringLogfile.setStatus("mandatory")
_RndMonitoringEntryStatus_Type = RowStatus
_RndMonitoringEntryStatus_Object = MibTableColumn
rndMonitoringEntryStatus = _RndMonitoringEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 4, 1, 11),
    _RndMonitoringEntryStatus_Type()
)
rndMonitoringEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringEntryStatus.setStatus("mandatory")
_RndMibFilesTable_Object = MibTable
rndMibFilesTable = _RndMibFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5)
)
if mibBuilder.loadTexts:
    rndMibFilesTable.setStatus("mandatory")
_RndMibFileEntry_Object = MibTableRow
rndMibFileEntry = _RndMibFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1)
)
rndMibFileEntry.setIndexNames(
    (0, "RADWARE-MIB", "rndMibFileIndex"),
)
if mibBuilder.loadTexts:
    rndMibFileEntry.setStatus("mandatory")
_RndMibFileIndex_Type = Integer32
_RndMibFileIndex_Object = MibTableColumn
rndMibFileIndex = _RndMibFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 1),
    _RndMibFileIndex_Type()
)
rndMibFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMibFileIndex.setStatus("mandatory")
_RndMibFilePath_Type = DisplayString
_RndMibFilePath_Object = MibTableColumn
rndMibFilePath = _RndMibFilePath_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 2),
    _RndMibFilePath_Type()
)
rndMibFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFilePath.setStatus("mandatory")


class _RndMibFileRefresh_Type(Integer32):
    """Custom type rndMibFileRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RndMibFileRefresh_Type.__name__ = "Integer32"
_RndMibFileRefresh_Object = MibTableColumn
rndMibFileRefresh = _RndMibFileRefresh_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 3),
    _RndMibFileRefresh_Type()
)
rndMibFileRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFileRefresh.setStatus("mandatory")
_RndMibFileEntryStatus_Type = RowStatus
_RndMibFileEntryStatus_Object = MibTableColumn
rndMibFileEntryStatus = _RndMibFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 5, 1, 4),
    _RndMibFileEntryStatus_Type()
)
rndMibFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFileEntryStatus.setStatus("mandatory")
_RndHardwareConfiguration_Type = TruthValue
_RndHardwareConfiguration_Object = MibScalar
rndHardwareConfiguration = _RndHardwareConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 6),
    _RndHardwareConfiguration_Type()
)
rndHardwareConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndHardwareConfiguration.setStatus("mandatory")


class _RndEraseSimulatedConfiguration_Type(Integer32):
    """Custom type rndEraseSimulatedConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eraseSimulatedConfiguration", 1),
          ("simulatedConfigurationErased", 3),
          ("simulatedConfigurationPresent", 2))
    )


_RndEraseSimulatedConfiguration_Type.__name__ = "Integer32"
_RndEraseSimulatedConfiguration_Object = MibScalar
rndEraseSimulatedConfiguration = _RndEraseSimulatedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 7),
    _RndEraseSimulatedConfiguration_Type()
)
rndEraseSimulatedConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndEraseSimulatedConfiguration.setStatus("mandatory")
_RndDeleteValuesTable_Object = MibTable
rndDeleteValuesTable = _RndDeleteValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8)
)
if mibBuilder.loadTexts:
    rndDeleteValuesTable.setStatus("mandatory")
_RndDeleteValuesEntry_Object = MibTableRow
rndDeleteValuesEntry = _RndDeleteValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1)
)
rndDeleteValuesEntry.setIndexNames(
    (1, "RADWARE-MIB", "rndRowStatusVariableName"),
)
if mibBuilder.loadTexts:
    rndDeleteValuesEntry.setStatus("mandatory")


class _RndRowStatusVariableName_Type(DisplayString):
    """Custom type rndRowStatusVariableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RndRowStatusVariableName_Type.__name__ = "DisplayString"
_RndRowStatusVariableName_Object = MibTableColumn
rndRowStatusVariableName = _RndRowStatusVariableName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 1),
    _RndRowStatusVariableName_Type()
)
rndRowStatusVariableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowStatusVariableName.setStatus("mandatory")
_RndRowStatusObjectId_Type = ObjectIdentifier
_RndRowStatusObjectId_Object = MibTableColumn
rndRowStatusObjectId = _RndRowStatusObjectId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 2),
    _RndRowStatusObjectId_Type()
)
rndRowStatusObjectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowStatusObjectId.setStatus("mandatory")
_RndRowDeleteValue_Type = Integer32
_RndRowDeleteValue_Object = MibTableColumn
rndRowDeleteValue = _RndRowDeleteValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 3),
    _RndRowDeleteValue_Type()
)
rndRowDeleteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowDeleteValue.setStatus("mandatory")
_RndDeleteValueEntryStatus_Type = RowStatus
_RndDeleteValueEntryStatus_Object = MibTableColumn
rndDeleteValueEntryStatus = _RndDeleteValueEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 8, 1, 4),
    _RndDeleteValueEntryStatus_Type()
)
rndDeleteValueEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDeleteValueEntryStatus.setStatus("mandatory")
_RsIpZeroHopRouting_ObjectIdentity = ObjectIdentity
rsIpZeroHopRouting = _RsIpZeroHopRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 3)
)


class _RsIpZhrGeneralStatus_Type(Integer32):
    """Custom type rsIpZhrGeneralStatus based on Integer32"""
    defaultValue = 2

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


_RsIpZhrGeneralStatus_Type.__name__ = "Integer32"
_RsIpZhrGeneralStatus_Object = MibScalar
rsIpZhrGeneralStatus = _RsIpZhrGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 1),
    _RsIpZhrGeneralStatus_Type()
)
rsIpZhrGeneralStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrGeneralStatus.setStatus("mandatory")


class _RsIpZhrAgingTimeout_Type(Integer32):
    """Custom type rsIpZhrAgingTimeout based on Integer32"""
    defaultValue = 600


_RsIpZhrAgingTimeout_Object = MibScalar
rsIpZhrAgingTimeout = _RsIpZhrAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 2),
    _RsIpZhrAgingTimeout_Type()
)
rsIpZhrAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrAgingTimeout.setStatus("mandatory")
_RsIpZhrStatusTable_Object = MibTable
rsIpZhrStatusTable = _RsIpZhrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3)
)
if mibBuilder.loadTexts:
    rsIpZhrStatusTable.setStatus("mandatory")
_RsIpZhrStatusEntry_Object = MibTableRow
rsIpZhrStatusEntry = _RsIpZhrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3, 1)
)
rsIpZhrStatusEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpZhrStatusIpIntf"),
)
if mibBuilder.loadTexts:
    rsIpZhrStatusEntry.setStatus("mandatory")
_RsIpZhrStatusIpIntf_Type = IpAddress
_RsIpZhrStatusIpIntf_Object = MibTableColumn
rsIpZhrStatusIpIntf = _RsIpZhrStatusIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3, 1, 1),
    _RsIpZhrStatusIpIntf_Type()
)
rsIpZhrStatusIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrStatusIpIntf.setStatus("mandatory")


class _RsIpZhrAdminStatus_Type(Integer32):
    """Custom type rsIpZhrAdminStatus based on Integer32"""
    defaultValue = 1

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


_RsIpZhrAdminStatus_Type.__name__ = "Integer32"
_RsIpZhrAdminStatus_Object = MibTableColumn
rsIpZhrAdminStatus = _RsIpZhrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 3, 1, 2),
    _RsIpZhrAdminStatus_Type()
)
rsIpZhrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrAdminStatus.setStatus("mandatory")
_RsIpZhrVirtAddressTable_Object = MibTable
rsIpZhrVirtAddressTable = _RsIpZhrVirtAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4)
)
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressTable.setStatus("mandatory")
_RsIpZhrVirtAddressEntry_Object = MibTableRow
rsIpZhrVirtAddressEntry = _RsIpZhrVirtAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1)
)
rsIpZhrVirtAddressEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpZhrVirtAddressIpIntf"),
    (0, "RADWARE-MIB", "rsIpZhrVirtAddressTo"),
)
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressEntry.setStatus("mandatory")
_RsIpZhrVirtAddressIpIntf_Type = IpAddress
_RsIpZhrVirtAddressIpIntf_Object = MibTableColumn
rsIpZhrVirtAddressIpIntf = _RsIpZhrVirtAddressIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 1),
    _RsIpZhrVirtAddressIpIntf_Type()
)
rsIpZhrVirtAddressIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressIpIntf.setStatus("mandatory")
_RsIpZhrVirtAddressTo_Type = IpAddress
_RsIpZhrVirtAddressTo_Object = MibTableColumn
rsIpZhrVirtAddressTo = _RsIpZhrVirtAddressTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 2),
    _RsIpZhrVirtAddressTo_Type()
)
rsIpZhrVirtAddressTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressTo.setStatus("mandatory")
_RsIpZhrVirtAddressFrom_Type = IpAddress
_RsIpZhrVirtAddressFrom_Object = MibTableColumn
rsIpZhrVirtAddressFrom = _RsIpZhrVirtAddressFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 3),
    _RsIpZhrVirtAddressFrom_Type()
)
rsIpZhrVirtAddressFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressFrom.setStatus("mandatory")
_RsIpZhrVirtAddressStatus_Type = RowStatus
_RsIpZhrVirtAddressStatus_Object = MibTableColumn
rsIpZhrVirtAddressStatus = _RsIpZhrVirtAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 4, 1, 4),
    _RsIpZhrVirtAddressStatus_Type()
)
rsIpZhrVirtAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrVirtAddressStatus.setStatus("mandatory")
_RsIpZhrConnectionsTable_Object = MibTable
rsIpZhrConnectionsTable = _RsIpZhrConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5)
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionsTable.setStatus("mandatory")
_RsIpZhrConnectionEntry_Object = MibTableRow
rsIpZhrConnectionEntry = _RsIpZhrConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1)
)
rsIpZhrConnectionEntry.setIndexNames(
    (0, "RADWARE-MIB", "rsIpZhrConnectionIpIntf"),
    (0, "RADWARE-MIB", "rsIpZhrConnectionSrcIp"),
    (0, "RADWARE-MIB", "rsIpZhrConnectionDestIp"),
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionEntry.setStatus("mandatory")
_RsIpZhrConnectionIpIntf_Type = IpAddress
_RsIpZhrConnectionIpIntf_Object = MibTableColumn
rsIpZhrConnectionIpIntf = _RsIpZhrConnectionIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 1),
    _RsIpZhrConnectionIpIntf_Type()
)
rsIpZhrConnectionIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionIpIntf.setStatus("mandatory")
_RsIpZhrConnectionSrcIp_Type = IpAddress
_RsIpZhrConnectionSrcIp_Object = MibTableColumn
rsIpZhrConnectionSrcIp = _RsIpZhrConnectionSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 2),
    _RsIpZhrConnectionSrcIp_Type()
)
rsIpZhrConnectionSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionSrcIp.setStatus("mandatory")
_RsIpZhrConnectionDestIp_Type = IpAddress
_RsIpZhrConnectionDestIp_Object = MibTableColumn
rsIpZhrConnectionDestIp = _RsIpZhrConnectionDestIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 3),
    _RsIpZhrConnectionDestIp_Type()
)
rsIpZhrConnectionDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionDestIp.setStatus("mandatory")
_RsIpZhrConnectionVirtualIp_Type = IpAddress
_RsIpZhrConnectionVirtualIp_Object = MibTableColumn
rsIpZhrConnectionVirtualIp = _RsIpZhrConnectionVirtualIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 4),
    _RsIpZhrConnectionVirtualIp_Type()
)
rsIpZhrConnectionVirtualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionVirtualIp.setStatus("mandatory")


class _RsIpZhrConnectionType_Type(Integer32):
    """Custom type rsIpZhrConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("dynamic", 2),
          ("static", 1))
    )


_RsIpZhrConnectionType_Type.__name__ = "Integer32"
_RsIpZhrConnectionType_Object = MibTableColumn
rsIpZhrConnectionType = _RsIpZhrConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 5),
    _RsIpZhrConnectionType_Type()
)
rsIpZhrConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionType.setStatus("mandatory")
_RsIpZhrConnectionAge_Type = Integer32
_RsIpZhrConnectionAge_Object = MibTableColumn
rsIpZhrConnectionAge = _RsIpZhrConnectionAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 6),
    _RsIpZhrConnectionAge_Type()
)
rsIpZhrConnectionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpZhrConnectionAge.setStatus("mandatory")
_RsIpZhrConnectionStatus_Type = RowStatus
_RsIpZhrConnectionStatus_Object = MibTableColumn
rsIpZhrConnectionStatus = _RsIpZhrConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 3, 5, 1, 7),
    _RsIpZhrConnectionStatus_Type()
)
rsIpZhrConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpZhrConnectionStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

routeTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 5)
)
routeTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    routeTableOverflow.setStatus(
        ""
    )

resetRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 10)
)
resetRequired.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    resetRequired.setStatus(
        ""
    )

endTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 12)
)
endTftp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    endTftp.setStatus(
        ""
    )

abortTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 13)
)
abortTftp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    abortTftp.setStatus(
        ""
    )

startTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 14)
)
startTftp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    startTftp.setStatus(
        ""
    )

ipxRipTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 36)
)
ipxRipTblOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxRipTblOverflow.setStatus(
        ""
    )

ipxSapTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 37)
)
ipxSapTblOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxSapTblOverflow.setStatus(
        ""
    )

facsAccessVoilation = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 49)
)
facsAccessVoilation.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    facsAccessVoilation.setStatus(
        ""
    )

autoConfigurationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 50)
)
autoConfigurationCompleted.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    autoConfigurationCompleted.setStatus(
        ""
    )

forwardingTabOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 51)
)
forwardingTabOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    forwardingTabOverflow.setStatus(
        ""
    )

errorsDuringInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 61)
)
errorsDuringInit.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    errorsDuringInit.setStatus(
        ""
    )

vlanDynPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 66)
)
vlanDynPortAdded.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortAdded.setStatus(
        ""
    )

vlanDynPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 67)
)
vlanDynPortRemoved.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortRemoved.setStatus(
        ""
    )

rsSDclientsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 68)
)
rsSDclientsTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDclientsTableOverflow.setStatus(
        ""
    )

rsSDinactiveServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 69)
)
rsSDinactiveServer.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDinactiveServer.setStatus(
        ""
    )

rsIpZhrConnectionsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 70)
)
rsIpZhrConnectionsTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionsTableOverflow.setStatus(
        ""
    )

rsIpZhrReqStaticConnNotAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 71)
)
rsIpZhrReqStaticConnNotAccepted.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrReqStaticConnNotAccepted.setStatus(
        ""
    )

rsIpZhrVirtualIpAsSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 72)
)
rsIpZhrVirtualIpAsSource.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrVirtualIpAsSource.setStatus(
        ""
    )

rsIpZhrNotAllocVirtualIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 73)
)
rsIpZhrNotAllocVirtualIp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrNotAllocVirtualIp.setStatus(
        ""
    )

rsSnmpSetRequestInSpecialCfgState = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 74)
)
rsSnmpSetRequestInSpecialCfgState.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSnmpSetRequestInSpecialCfgState.setStatus(
        ""
    )

rsWSDRedundancySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 141)
)
rsWSDRedundancySwitch.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDRedundancySwitch.setStatus(
        ""
    )

rsWSDConnectionLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 1)
)
rsWSDConnectionLimitReached.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDConnectionLimitReached.setStatus(
        ""
    )

rsWSDReadyForShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 2)
)
rsWSDReadyForShutDown.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDReadyForShutDown.setStatus(
        ""
    )

rsWSDIllegalReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 3)
)
rsWSDIllegalReport.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDIllegalReport.setStatus(
        ""
    )

rsWSDRemoteWSDUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 4)
)
rsWSDRemoteWSDUnavailable.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDRemoteWSDUnavailable.setStatus(
        ""
    )

rsWSDCapacityLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 5)
)
rsWSDCapacityLimitReached.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDCapacityLimitReached.setStatus(
        ""
    )

rsWSDStatusMonitoring = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 6)
)
rsWSDStatusMonitoring.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDStatusMonitoring.setStatus(
        ""
    )

rsWSDWrongPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 7)
)
rsWSDWrongPassword.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDWrongPassword.setStatus(
        ""
    )

rsWSDInternalTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 8)
)
rsWSDInternalTableOverflow.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDInternalTableOverflow.setStatus(
        ""
    )

rsWSDServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 9)
)
rsWSDServerUp.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDServerUp.setStatus(
        ""
    )

rsWSDPoliciesUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 10)
)
rsWSDPoliciesUpdated.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDPoliciesUpdated.setStatus(
        ""
    )

rsWSDIntrusionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 0, 11)
)
rsWSDIntrusionDetected.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDIntrusionDetected.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADWARE-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "NetNumber": NetNumber,
       "RsIfType": RsIfType,
       "rnd": rnd,
       "routeTableOverflow": routeTableOverflow,
       "resetRequired": resetRequired,
       "endTftp": endTftp,
       "abortTftp": abortTftp,
       "startTftp": startTftp,
       "ipxRipTblOverflow": ipxRipTblOverflow,
       "ipxSapTblOverflow": ipxSapTblOverflow,
       "facsAccessVoilation": facsAccessVoilation,
       "autoConfigurationCompleted": autoConfigurationCompleted,
       "forwardingTabOverflow": forwardingTabOverflow,
       "errorsDuringInit": errorsDuringInit,
       "vlanDynPortAdded": vlanDynPortAdded,
       "vlanDynPortRemoved": vlanDynPortRemoved,
       "rsSDclientsTableOverflow": rsSDclientsTableOverflow,
       "rsSDinactiveServer": rsSDinactiveServer,
       "rsIpZhrConnectionsTableOverflow": rsIpZhrConnectionsTableOverflow,
       "rsIpZhrReqStaticConnNotAccepted": rsIpZhrReqStaticConnNotAccepted,
       "rsIpZhrVirtualIpAsSource": rsIpZhrVirtualIpAsSource,
       "rsIpZhrNotAllocVirtualIp": rsIpZhrNotAllocVirtualIp,
       "rsSnmpSetRequestInSpecialCfgState": rsSnmpSetRequestInSpecialCfgState,
       "rsWSDRedundancySwitch": rsWSDRedundancySwitch,
       "rndMng": rndMng,
       "rndSysId": rndSysId,
       "rndAction": rndAction,
       "rndFileName": rndFileName,
       "rndDeviceParams": rndDeviceParams,
       "rndBridgeType": rndBridgeType,
       "rndInactiveArpTimeOut": rndInactiveArpTimeOut,
       "rndBridgeAlarm": rndBridgeAlarm,
       "rndErrorDesc": rndErrorDesc,
       "rndErrorSeverity": rndErrorSeverity,
       "rndBrgVersion": rndBrgVersion,
       "rndBrgFeatures": rndBrgFeatures,
       "rndBrgLicense": rndBrgLicense,
       "rndIpHost": rndIpHost,
       "rndICMPTransmitionEnable": rndICMPTransmitionEnable,
       "rndCommunityTable": rndCommunityTable,
       "rndCommunityEntry": rndCommunityEntry,
       "rndCommunityMngStationAddr": rndCommunityMngStationAddr,
       "rndCommunityString": rndCommunityString,
       "rndCommunityAccess": rndCommunityAccess,
       "rndCommunityTrapsEnable": rndCommunityTrapsEnable,
       "rndCommunityStatus": rndCommunityStatus,
       "rndManagedTime": rndManagedTime,
       "rndManagedDate": rndManagedDate,
       "genGroup": genGroup,
       "genGroupHWVersion": genGroupHWVersion,
       "genGroupConfigurationSymbol": genGroupConfigurationSymbol,
       "genGroupHWStatus": genGroupHWStatus,
       "rndInterface": rndInterface,
       "rndIfTable": rndIfTable,
       "rndIfEntry": rndIfEntry,
       "rndIfIndex": rndIfIndex,
       "rndIfBoardNum": rndIfBoardNum,
       "rndIfNetAddress": rndIfNetAddress,
       "rndIfStatus": rndIfStatus,
       "rndIfClockType": rndIfClockType,
       "rndIfBaudRate": rndIfBaudRate,
       "rndIfCost": rndIfCost,
       "rndIfCompression": rndIfCompression,
       "rndIfCompressionStatus": rndIfCompressionStatus,
       "rndIfCompressionRate": rndIfCompressionRate,
       "rndIfLATCompression": rndIfLATCompression,
       "rndIfCompressionType": rndIfCompressionType,
       "rndIfFilterMode": rndIfFilterMode,
       "rndIfChannelType": rndIfChannelType,
       "rndIfBridge": rndIfBridge,
       "rndHighPriorityIf": rndHighPriorityIf,
       "rndWanHeader": rndWanHeader,
       "rndDuplexMode": rndDuplexMode,
       "rndIPX": rndIPX,
       "rndFACS": rndFACS,
       "rndFACSDefaultAction": rndFACSDefaultAction,
       "rndFACSActTable": rndFACSActTable,
       "rndFACSActEntry": rndFACSActEntry,
       "rndFACSActType": rndFACSActType,
       "rndFACSActIfIndex": rndFACSActIfIndex,
       "rndFACSAction": rndFACSAction,
       "rndFACSTable": rndFACSTable,
       "rndFACSEntry": rndFACSEntry,
       "rndFACSIfIndex": rndFACSIfIndex,
       "rndFACSProtocolType": rndFACSProtocolType,
       "rndFACSType": rndFACSType,
       "rndFACSIndex": rndFACSIndex,
       "rndFACSSrcAdd": rndFACSSrcAdd,
       "rndFACSSrcAddMask": rndFACSSrcAddMask,
       "rndFACSDesAdd": rndFACSDesAdd,
       "rndFACSDesAddMask": rndFACSDesAddMask,
       "rndFACSOperation": rndFACSOperation,
       "rndFACSNetFiltering": rndFACSNetFiltering,
       "rndFACSSoketNum": rndFACSSoketNum,
       "rndFACSMask1Id": rndFACSMask1Id,
       "rndFACSMask2Id": rndFACSMask2Id,
       "rndFACSStatus": rndFACSStatus,
       "rndBootP": rndBootP,
       "rndBootPServerAddress": rndBootPServerAddress,
       "rndBootPRelaySecThreshold": rndBootPRelaySecThreshold,
       "ipSpec": ipSpec,
       "rsIpAddrTable": rsIpAddrTable,
       "rsIpAddrEntry": rsIpAddrEntry,
       "rsIpAdEntAddr": rsIpAdEntAddr,
       "rsIpAdEntIfIndex": rsIpAdEntIfIndex,
       "rsIpAdEntNetMask": rsIpAdEntNetMask,
       "rsIpAdEntForwardIpBroadcast": rsIpAdEntForwardIpBroadcast,
       "rsIpAdEntReasmMaxSize": rsIpAdEntReasmMaxSize,
       "rsIpAdEntStatus": rsIpAdEntStatus,
       "rsIpAdEntBcastAddr": rsIpAdEntBcastAddr,
       "rsIpAdEntVlanTag": rsIpAdEntVlanTag,
       "icmpSpec": icmpSpec,
       "rsIcmpGenErrMsgEnable": rsIcmpGenErrMsgEnable,
       "rsIcmpRdTable": rsIcmpRdTable,
       "rsIcmpRdEntry": rsIcmpRdEntry,
       "rsIcmpRdIpAddr": rsIcmpRdIpAddr,
       "rsIcmpRdIpAdvertAddr": rsIcmpRdIpAdvertAddr,
       "rsIcmpRdMaxAdvertInterval": rsIcmpRdMaxAdvertInterval,
       "rsIcmpRdMinAdvertInterval": rsIcmpRdMinAdvertInterval,
       "rsIcmpRdAdvertLifetime": rsIcmpRdAdvertLifetime,
       "rsIcmpRdAdvertise": rsIcmpRdAdvertise,
       "rsIcmpRdPreferenceLevel": rsIcmpRdPreferenceLevel,
       "rsIcmpRdEntStatus": rsIcmpRdEntStatus,
       "rip2Spec": rip2Spec,
       "rsRip2IfConfTable": rsRip2IfConfTable,
       "rsRip2IfConfEntry": rsRip2IfConfEntry,
       "rsRip2IfConfAddress": rsRip2IfConfAddress,
       "rsRip2IfConfVirtualDis": rsRip2IfConfVirtualDis,
       "rsRip2IfConfAutoSend": rsRip2IfConfAutoSend,
       "arpSpec": arpSpec,
       "rsArpDeleteTable": rsArpDeleteTable,
       "rsArpInactiveTimeOut": rsArpInactiveTimeOut,
       "rsArpProxy": rsArpProxy,
       "tftp": tftp,
       "rsTftpRetryTimeOut": rsTftpRetryTimeOut,
       "rsTftpTotalTimeOut": rsTftpTotalTimeOut,
       "rsSendConfigFile": rsSendConfigFile,
       "rsGetConfigFile": rsGetConfigFile,
       "rsLoadSoftware": rsLoadSoftware,
       "rsFileServerAddress": rsFileServerAddress,
       "ipRedundancy": ipRedundancy,
       "ipRedundAdminStatus": ipRedundAdminStatus,
       "ipRedundOperStatus": ipRedundOperStatus,
       "ipRedundRoutersTable": ipRedundRoutersTable,
       "ipRedundRoutersEntry": ipRedundRoutersEntry,
       "ipRedundRoutersIfAddr": ipRedundRoutersIfAddr,
       "ipRedundRoutersMainRouterAddr": ipRedundRoutersMainRouterAddr,
       "ipRedundRoutersOperStatus": ipRedundRoutersOperStatus,
       "ipRedundRoutersPollInterval": ipRedundRoutersPollInterval,
       "ipRedundRoutersTimeout": ipRedundRoutersTimeout,
       "ipRedundRoutersStatus": ipRedundRoutersStatus,
       "ipRouteLeaking": ipRouteLeaking,
       "ipLeakStaticToRip": ipLeakStaticToRip,
       "ipLeakStaticToOspf": ipLeakStaticToOspf,
       "ipLeakOspfToRip": ipLeakOspfToRip,
       "ipLeakRipToOspf": ipLeakRipToOspf,
       "ipLeakExtDirectToOspf": ipLeakExtDirectToOspf,
       "ipRipFilter": ipRipFilter,
       "rsIpRipFilterGlbTable": rsIpRipFilterGlbTable,
       "rsIpRipFilterGlbEntry": rsIpRipFilterGlbEntry,
       "rsIpRipFilterGlbType": rsIpRipFilterGlbType,
       "rsIpRipFilterGlbNumber": rsIpRipFilterGlbNumber,
       "rsIpRipFilterGlbStatus": rsIpRipFilterGlbStatus,
       "rsIpRipFilterGlbIpAddr": rsIpRipFilterGlbIpAddr,
       "rsIpRipFilterGlbNetworkMaskBits": rsIpRipFilterGlbNetworkMaskBits,
       "rsIpRipFilterGlbMatchBits": rsIpRipFilterGlbMatchBits,
       "rsIpRipFilterGlbAction": rsIpRipFilterGlbAction,
       "rsIpRipFilterLclTable": rsIpRipFilterLclTable,
       "rsIpRipFilterLclEntry": rsIpRipFilterLclEntry,
       "rsIpRipFilterLclIpIntf": rsIpRipFilterLclIpIntf,
       "rsIpRipFilterLclType": rsIpRipFilterLclType,
       "rsIpRipFilterLclNumber": rsIpRipFilterLclNumber,
       "rsIpRipFilterLclStatus": rsIpRipFilterLclStatus,
       "rsIpRipFilterLclIpAddr": rsIpRipFilterLclIpAddr,
       "rsIpRipFilterLclNetworkMaskBits": rsIpRipFilterLclNetworkMaskBits,
       "rsIpRipFilterLclMatchBits": rsIpRipFilterLclMatchBits,
       "rsIpRipFilterLclAction": rsIpRipFilterLclAction,
       "rsRipEnable": rsRipEnable,
       "lreBoxAgentIP": lreBoxAgentIP,
       "virtualLan": virtualLan,
       "virtualLanTable": virtualLanTable,
       "virtualLanEntry": virtualLanEntry,
       "vlIfIndex": vlIfIndex,
       "vlProto": vlProto,
       "vlAutoConfigEnable": vlAutoConfigEnable,
       "vlStatus": vlStatus,
       "vlType": vlType,
       "virtualLanPortsTable": virtualLanPortsTable,
       "virtualLanPortEntry": virtualLanPortEntry,
       "vLIfIndex": vLIfIndex,
       "vLPortIfIndex": vLPortIfIndex,
       "vLPortType": vLPortType,
       "vLPortStatus": vLPortStatus,
       "virtualLanAutoConfTable": virtualLanAutoConfTable,
       "virtualLanAutoConfEntry": virtualLanAutoConfEntry,
       "vlAutoConfPortIfIndex": vlAutoConfPortIfIndex,
       "vlAutoConfProto": vlAutoConfProto,
       "vlAutoConfStatus": vlAutoConfStatus,
       "virtualLanAutoConfAgingTimeout": virtualLanAutoConfAgingTimeout,
       "virtualLanProtocolVlan": virtualLanProtocolVlan,
       "virtualLanUserEtherType": virtualLanUserEtherType,
       "virtualLanUserMask": virtualLanUserMask,
       "rsConf": rsConf,
       "rsIfConfTable": rsIfConfTable,
       "rsIfConfEntry": rsIfConfEntry,
       "rsIfConfIndex": rsIfConfIndex,
       "rsIfConfType": rsIfConfType,
       "rsIfConfName": rsIfConfName,
       "rsIfConfStatus": rsIfConfStatus,
       "rsTunning": rsTunning,
       "rsHighPriority": rsHighPriority,
       "rsLowPriority": rsLowPriority,
       "rsDbgLevel": rsDbgLevel,
       "rsDiagnostic": rsDiagnostic,
       "rsConfirmMessagTab": rsConfirmMessagTab,
       "eventMessageTable": eventMessageTable,
       "eventMessageEntry": eventMessageEntry,
       "eventNum": eventNum,
       "eventDesc": eventDesc,
       "reaTunning": reaTunning,
       "reaIpRemoteAgingTime": reaIpRemoteAgingTime,
       "reaFftHashMaxChain": reaFftHashMaxChain,
       "reaMltcstBitOn": reaMltcstBitOn,
       "reaIpForwardEnable": reaIpForwardEnable,
       "reaIpxForwardEnable": reaIpxForwardEnable,
       "reaBridgeEnable": reaBridgeEnable,
       "reaFacsEnable": reaFacsEnable,
       "reaIpForwardDatagrams": reaIpForwardDatagrams,
       "reaIpInDiscards": reaIpInDiscards,
       "reaIpxForwardDatagrams": reaIpxForwardDatagrams,
       "reaIpxInDiscards": reaIpxInDiscards,
       "reaBridgeFftTable": reaBridgeFftTable,
       "reaBridgeFftEntry": reaBridgeFftEntry,
       "reaBrgFftEntryNum": reaBrgFftEntryNum,
       "reaBrgFftMacAddr": reaBrgFftMacAddr,
       "reaBrgFftReNum": reaBrgFftReNum,
       "reaBrgFftPortNum": reaBrgFftPortNum,
       "reaBrgFftFacsSrcIndex": reaBrgFftFacsSrcIndex,
       "reaBrgFftFacsDstIndex": reaBrgFftFacsDstIndex,
       "reaBrgDiscards": reaBrgDiscards,
       "reaBrgForwards": reaBrgForwards,
       "reaIpFftTable": reaIpFftTable,
       "reaIpFftEntry": reaIpFftEntry,
       "reaIpFftEntryNum": reaIpFftEntryNum,
       "reaIpFftDstIpAddr": reaIpFftDstIpAddr,
       "reaIpFftDstIpMask": reaIpFftDstIpMask,
       "reaIpFftRangeType": reaIpFftRangeType,
       "reaIpFftSrcMacAddr": reaIpFftSrcMacAddr,
       "reaIpFftDstMacAddr": reaIpFftDstMacAddr,
       "reaIpFftReNum": reaIpFftReNum,
       "reaIpFftPortNum": reaIpFftPortNum,
       "reaIpFftFacsSrcIndex": reaIpFftFacsSrcIndex,
       "reaIpFftFacsDstIndex": reaIpFftFacsDstIndex,
       "reaIpFftApplFlags": reaIpFftApplFlags,
       "reaIpxFftTable": reaIpxFftTable,
       "reaIpxFftEntry": reaIpxFftEntry,
       "reaIpxFftEntryNum": reaIpxFftEntryNum,
       "reaIpxFftDstNetid": reaIpxFftDstNetid,
       "reaIpxFftRangeType": reaIpxFftRangeType,
       "reaIpxFftSrcMacAddr": reaIpxFftSrcMacAddr,
       "reaIpxFftDstMacAddr": reaIpxFftDstMacAddr,
       "reaIpxFftReNum": reaIpxFftReNum,
       "reaIpxFftPortNum": reaIpxFftPortNum,
       "reaIpxFftFacsSrcIndex": reaIpxFftFacsSrcIndex,
       "reaIpxFftFacsDstIndex": reaIpxFftFacsDstIndex,
       "lreVnResposibilityTable": lreVnResposibilityTable,
       "lreVnResposibilityEntry": lreVnResposibilityEntry,
       "lreVnRespVn": lreVnRespVn,
       "lreVnRespStatus": lreVnRespStatus,
       "reaSrcViolationEnable": reaSrcViolationEnable,
       "reaSrcViolationTrapEnable": reaSrcViolationTrapEnable,
       "reaSrcAddrValidationEnable": reaSrcAddrValidationEnable,
       "reaRsQueueDiscards": reaRsQueueDiscards,
       "reaBufFree": reaBufFree,
       "lreResetDstMacBit46": lreResetDstMacBit46,
       "lreQueSourceSelect": lreQueSourceSelect,
       "lreResetDstMacBit47": lreResetDstMacBit47,
       "rsMaxEntriesTuning": rsMaxEntriesTuning,
       "rsMaxBridgeForwardingEntriesTuning": rsMaxBridgeForwardingEntriesTuning,
       "rsMaxBrgFrwEntries": rsMaxBrgFrwEntries,
       "rsMaxBrgFrwEntriesAfterReset": rsMaxBrgFrwEntriesAfterReset,
       "rsMaxIpForwardingEntriesTuning": rsMaxIpForwardingEntriesTuning,
       "rsMaxIpFrwEntries": rsMaxIpFrwEntries,
       "rsMaxIpFrwEntriesAfterReset": rsMaxIpFrwEntriesAfterReset,
       "rsMaxArpEntriesTuning": rsMaxArpEntriesTuning,
       "rsMaxArpEntries": rsMaxArpEntries,
       "rsMaxArpEntriesAfterReset": rsMaxArpEntriesAfterReset,
       "rsMaxIpxForwardingEntriesTuning": rsMaxIpxForwardingEntriesTuning,
       "rsMaxIpxFrwEntries": rsMaxIpxFrwEntries,
       "rsMaxIpxFrwEntriesAfterReset": rsMaxIpxFrwEntriesAfterReset,
       "rsMaxIpxSapEntriesTuning": rsMaxIpxSapEntriesTuning,
       "rsMaxIpxSapEntries": rsMaxIpxSapEntries,
       "rsMaxIpxSapEntriesAfterReset": rsMaxIpxSapEntriesAfterReset,
       "rsMaxDspClntEntriesTuning": rsMaxDspClntEntriesTuning,
       "rsMaxDspClntEntries": rsMaxDspClntEntries,
       "rsMaxDspClntEntriesAfterReset": rsMaxDspClntEntriesAfterReset,
       "rsMaxZeroHopRoutEntriesTuning": rsMaxZeroHopRoutEntriesTuning,
       "rsMaxZhrConns": rsMaxZhrConns,
       "rsMaxZhrConnsAfterReset": rsMaxZhrConnsAfterReset,
       "rsMaxDspFrmEntriesTuning": rsMaxDspFrmEntriesTuning,
       "rsMaxDspFrmEntries": rsMaxDspFrmEntries,
       "rsMaxDspFrmEntriesAfterReset": rsMaxDspFrmEntriesAfterReset,
       "rsMaxRoutingEntriesTuning": rsMaxRoutingEntriesTuning,
       "rsMaxRoutingEntries": rsMaxRoutingEntries,
       "rsMaxRoutingEntriesAfterReset": rsMaxRoutingEntriesAfterReset,
       "rndApplications": rndApplications,
       "rsServerDispatcher": rsServerDispatcher,
       "rsWSDConnectionLimitReached": rsWSDConnectionLimitReached,
       "rsWSDReadyForShutDown": rsWSDReadyForShutDown,
       "rsWSDIllegalReport": rsWSDIllegalReport,
       "rsWSDRemoteWSDUnavailable": rsWSDRemoteWSDUnavailable,
       "rsWSDCapacityLimitReached": rsWSDCapacityLimitReached,
       "rsWSDStatusMonitoring": rsWSDStatusMonitoring,
       "rsWSDWrongPassword": rsWSDWrongPassword,
       "rsWSDInternalTableOverflow": rsWSDInternalTableOverflow,
       "rsWSDServerUp": rsWSDServerUp,
       "rsWSDPoliciesUpdated": rsWSDPoliciesUpdated,
       "rsWSDIntrusionDetected": rsWSDIntrusionDetected,
       "rsWSDServerStatTable": rsWSDServerStatTable,
       "rsWSDServerStatEntry": rsWSDServerStatEntry,
       "rsWSDSerStatName": rsWSDSerStatName,
       "rsWSDSerStatAttUsersNum": rsWSDSerStatAttUsersNum,
       "rsWSDSerStatPeakLoad": rsWSDSerStatPeakLoad,
       "rsWSDSerStatFramesRate": rsWSDSerStatFramesRate,
       "rsWSDSerStatFramesLoad": rsWSDSerStatFramesLoad,
       "rsWSDSerStatRecoveryTime": rsWSDSerStatRecoveryTime,
       "rsWSDSerStatWarmUpTime": rsWSDSerStatWarmUpTime,
       "rsWSDSerStatConnectionLimit": rsWSDSerStatConnectionLimit,
       "rsWSDSerStatAdminStatus": rsWSDSerStatAdminStatus,
       "rsWSDSerStatConnectionLimitReached": rsWSDSerStatConnectionLimitReached,
       "rsWSDdummy2": rsWSDdummy2,
       "wsdRedundTable": wsdRedundTable,
       "wsdRedundEntry": wsdRedundEntry,
       "wsdRedundFarmAddr": wsdRedundFarmAddr,
       "wsdRedundMainWsdAddr": wsdRedundMainWsdAddr,
       "wsdRedundOperStatus": wsdRedundOperStatus,
       "wsdRedundPollInterval": wsdRedundPollInterval,
       "wsdRedundTimeout": wsdRedundTimeout,
       "wsdRedundStatus": wsdRedundStatus,
       "rsWSDdummy5": rsWSDdummy5,
       "rsWSDNewEntryOnSourcePort": rsWSDNewEntryOnSourcePort,
       "rsWSDSelectServerOnSourcePort": rsWSDSelectServerOnSourcePort,
       "rsWSDRedundancyMode": rsWSDRedundancyMode,
       "rsNsdMode": rsNsdMode,
       "rsNsdWINSAddr": rsNsdWINSAddr,
       "rsWSDSyslogStatus": rsWSDSyslogStatus,
       "rsWSDSyslogAddress": rsWSDSyslogAddress,
       "rsWSDNTCheckTable": rsWSDNTCheckTable,
       "rsWSDNTCheckEntry": rsWSDNTCheckEntry,
       "rsWSDNTSerialNum": rsWSDNTSerialNum,
       "rsWSDNTFrequentCheckPeriod": rsWSDNTFrequentCheckPeriod,
       "rsWSDNTOpenSessionsWeight": rsWSDNTOpenSessionsWeight,
       "rsWSDNTIncomingTrafficWeight": rsWSDNTIncomingTrafficWeight,
       "rsWSDNTOutgoingTrafficWeight": rsWSDNTOutgoingTrafficWeight,
       "rsWSDNTRegularCheckPeriod": rsWSDNTRegularCheckPeriod,
       "rsWSDNTAvResponseWeight": rsWSDNTAvResponseWeight,
       "rsWSDNTUsersLimitWeight": rsWSDNTUsersLimitWeight,
       "rsWSDNTTCPLimitWeight": rsWSDNTTCPLimitWeight,
       "rsWSDNTRetries": rsWSDNTRetries,
       "rsWSDNTCommunity": rsWSDNTCommunity,
       "rsWSDdummy8": rsWSDdummy8,
       "rsWSDPrivateCheckTable": rsWSDPrivateCheckTable,
       "rsWSDPrivateCheckEntry": rsWSDPrivateCheckEntry,
       "rsWSDPrivateSerialNum": rsWSDPrivateSerialNum,
       "rsWSDPrivateSpecialCheckPeriod": rsWSDPrivateSpecialCheckPeriod,
       "rsWSDPrivateExtraVar1ID": rsWSDPrivateExtraVar1ID,
       "rsWSDPrivateExtraVar1Weight": rsWSDPrivateExtraVar1Weight,
       "rsWSDPrivateExtraVar2ID": rsWSDPrivateExtraVar2ID,
       "rsWSDPrivateExtraVar2Weight": rsWSDPrivateExtraVar2Weight,
       "rsWSDPrivateRetries": rsWSDPrivateRetries,
       "rsWSDPrivateCommunity": rsWSDPrivateCommunity,
       "rsWSDPrivateExtraVar1Mode": rsWSDPrivateExtraVar1Mode,
       "rsWSDPrivateExtraVar2Mode": rsWSDPrivateExtraVar2Mode,
       "rsWSDdummy9": rsWSDdummy9,
       "rsWSDDNSResolution": rsWSDDNSResolution,
       "rsWSDUserPassword": rsWSDUserPassword,
       "rsWSDUserVersion": rsWSDUserVersion,
       "rsWSDNatStatus": rsWSDNatStatus,
       "rsWSDRedundancyTakeback": rsWSDRedundancyTakeback,
       "rsMLB": rsMLB,
       "rsCSD": rsCSD,
       "rsNWSD": rsNWSD,
       "rsWSDIfTable": rsWSDIfTable,
       "rsWSDIfEntry": rsWSDIfEntry,
       "rsWSDIfIndex": rsWSDIfIndex,
       "rsWSDIfBoardNum": rsWSDIfBoardNum,
       "rsWSDIfNetAddress": rsWSDIfNetAddress,
       "rsWSDIfStatus": rsWSDIfStatus,
       "rsWSDIfClockType": rsWSDIfClockType,
       "rsWSDIfBaudRate": rsWSDIfBaudRate,
       "rsWSDIfCost": rsWSDIfCost,
       "rsWSDIfCompression": rsWSDIfCompression,
       "rsWSDIfCompressionStatus": rsWSDIfCompressionStatus,
       "rsWSDIfCompressionRate": rsWSDIfCompressionRate,
       "rsWSDIfLATCompression": rsWSDIfLATCompression,
       "rsWSDIfCompressionType": rsWSDIfCompressionType,
       "rsWSDIfFilterMode": rsWSDIfFilterMode,
       "rsWSDIfChannelType": rsWSDIfChannelType,
       "rsWSDIfBridge": rsWSDIfBridge,
       "rsWSDHighPriorityIf": rsWSDHighPriorityIf,
       "rsWSDWanHeader": rsWSDWanHeader,
       "rsWSDDuplexMode": rsWSDDuplexMode,
       "rsWSDClientMirrorPercentage": rsWSDClientMirrorPercentage,
       "rsWSDMirrorStatus": rsWSDMirrorStatus,
       "rsWSDMirrorProtocolMode": rsWSDMirrorProtocolMode,
       "rsWSDApplicationMirrorTable": rsWSDApplicationMirrorTable,
       "rsWSDApplicationMirrorEntry": rsWSDApplicationMirrorEntry,
       "rsWSDMirrorActiveAddress": rsWSDMirrorActiveAddress,
       "rsWSDMirrorActiveStatus": rsWSDMirrorActiveStatus,
       "rsWSDdummy11": rsWSDdummy11,
       "rsWSDClientMirrorPollingTime": rsWSDClientMirrorPollingTime,
       "rsPlatformIdentifier": rsPlatformIdentifier,
       "rsConfigurationIdentifier": rsConfigurationIdentifier,
       "rsSWPasswordStatus": rsSWPasswordStatus,
       "rsWSDFlashSize": rsWSDFlashSize,
       "rsWSDDRAMSize": rsWSDDRAMSize,
       "rsWSDVLANRedundOperStatus": rsWSDVLANRedundOperStatus,
       "rsWSDResourceUtilization": rsWSDResourceUtilization,
       "rsWSDRSResourceUtilization": rsWSDRSResourceUtilization,
       "rsWSDREResourceUtilization": rsWSDREResourceUtilization,
       "rsWSDBuildNumber": rsWSDBuildNumber,
       "rsWSDUseOneTrap": rsWSDUseOneTrap,
       "rsWSDSecuredComm": rsWSDSecuredComm,
       "rsWSDSCProtcolsTable": rsWSDSCProtcolsTable,
       "rsWSDSCProtcolsEntry": rsWSDSCProtcolsEntry,
       "rsWSDSCProtocol": rsWSDSCProtocol,
       "rsWSDSCProtocolStatus": rsWSDSCProtocolStatus,
       "rsWSDSNMPPortsTable": rsWSDSNMPPortsTable,
       "rsWSDSNMPPortsEntry": rsWSDSNMPPortsEntry,
       "rsWSDSNMPPhysicalPortNumber": rsWSDSNMPPhysicalPortNumber,
       "rsWSDSNMPPhysicalPortState": rsWSDSNMPPhysicalPortState,
       "rsBWM": rsBWM,
       "rsWSDTelnetUserTable": rsWSDTelnetUserTable,
       "rsWSDTelnetUserEntry": rsWSDTelnetUserEntry,
       "rsWSDTelnetUserName": rsWSDTelnetUserName,
       "rsWSDTelnetUserPassword": rsWSDTelnetUserPassword,
       "rsWSDTelnetUserEAddr": rsWSDTelnetUserEAddr,
       "rsWSDTelnetUserSeverity": rsWSDTelnetUserSeverity,
       "rsWSDTelnetUserStatus": rsWSDTelnetUserStatus,
       "rsWSDTelnetUserGroup": rsWSDTelnetUserGroup,
       "rsWSDTelnetParams": rsWSDTelnetParams,
       "rsWSDTelnetPort": rsWSDTelnetPort,
       "rsWSDTelnetStatus": rsWSDTelnetStatus,
       "rsSSD": rsSSD,
       "rsSSDvirtualLan": rsSSDvirtualLan,
       "rsSSDvirtualLanTable": rsSSDvirtualLanTable,
       "rsSSDvirtualLanEntry": rsSSDvirtualLanEntry,
       "rsSSDvlIfIndex": rsSSDvlIfIndex,
       "rsSSDvlProto": rsSSDvlProto,
       "rsSSDvlAutoConfigEnable": rsSSDvlAutoConfigEnable,
       "rsSSDvlStatus": rsSSDvlStatus,
       "rsSSDvlType": rsSSDvlType,
       "rsSSDvlTag": rsSSDvlTag,
       "rsSSDvlPriority": rsSSDvlPriority,
       "rsSSDvirtualLanPortsTable": rsSSDvirtualLanPortsTable,
       "rsSSDvirtualLanPortEntry": rsSSDvirtualLanPortEntry,
       "rsSSDvLIfIndex": rsSSDvLIfIndex,
       "rsSSDvLPortIfIndex": rsSSDvLPortIfIndex,
       "rsSSDvLPortType": rsSSDvLPortType,
       "rsSSDvLPortStatus": rsSSDvLPortStatus,
       "rsSSDvLPortTag": rsSSDvLPortTag,
       "rsWSDThresholdWarnings": rsWSDThresholdWarnings,
       "rsWSDThreshTrapFloodDelay": rsWSDThreshTrapFloodDelay,
       "rsWSDCriticalTrapFloodDelay": rsWSDCriticalTrapFloodDelay,
       "rsIDS": rsIDS,
       "rsWSDLicense": rsWSDLicense,
       "rsErrMailParams": rsErrMailParams,
       "rsErrMailEnable": rsErrMailEnable,
       "rsErrMailGateway": rsErrMailGateway,
       "rsErrMailSrcAddress": rsErrMailSrcAddress,
       "rsWSDWebParams": rsWSDWebParams,
       "rsWSDWebPort": rsWSDWebPort,
       "rsWSDWebStatus": rsWSDWebStatus,
       "rsWSDWebHelpLocation": rsWSDWebHelpLocation,
       "rsWSDSysParams": rsWSDSysParams,
       "rsWSDSysFlashSize": rsWSDSysFlashSize,
       "rsWSDSysUpTime": rsWSDSysUpTime,
       "rsWSDSysManagedTime": rsWSDSysManagedTime,
       "rsWSDSysManagedDate": rsWSDSysManagedDate,
       "rsWSDLicenseID": rsWSDLicenseID,
       "rsWSDSendFakeArp": rsWSDSendFakeArp,
       "rsWSDNTP": rsWSDNTP,
       "rsWSDNTPServerAddr": rsWSDNTPServerAddr,
       "rsWSDNTPInterval": rsWSDNTPInterval,
       "rsWSDNTPStatus": rsWSDNTPStatus,
       "rsWSDNTPTimeZone": rsWSDNTPTimeZone,
       "rsWSDNTPPort": rsWSDNTPPort,
       "rsStatistics": rsStatistics,
       "rsPhysPortMirrorTable": rsPhysPortMirrorTable,
       "rsPhysPortMirrorEntry": rsPhysPortMirrorEntry,
       "rsPhysPortMirrorSrcInf": rsPhysPortMirrorSrcInf,
       "rsPhysPortMirrorDstPort": rsPhysPortMirrorDstPort,
       "rsPhysPortMirrorRxTx": rsPhysPortMirrorRxTx,
       "rsPhysPortMirrorRxBroadCast": rsPhysPortMirrorRxBroadCast,
       "rsPhysPortMirrorStatus": rsPhysPortMirrorStatus,
       "rsPhysPortMirrorBackupDstPort": rsPhysPortMirrorBackupDstPort,
       "rsPhysPortMirrorDstStatus": rsPhysPortMirrorDstStatus,
       "rsPhysPortMirrorBackupStatus": rsPhysPortMirrorBackupStatus,
       "rsPhysPortMirrorActiveDstPort": rsPhysPortMirrorActiveDstPort,
       "rsCP": rsCP,
       "rsVWSD": rsVWSD,
       "rsVWSDDataPermissionsTable": rsVWSDDataPermissionsTable,
       "rsVWSDDataPermissionsTableEntry": rsVWSDDataPermissionsTableEntry,
       "rsVWSDUserGroup": rsVWSDUserGroup,
       "rsVWSDDataType": rsVWSDDataType,
       "rsVWSDDataItems": rsVWSDDataItems,
       "rsVWSDDataStatus": rsVWSDDataStatus,
       "rsWSDManagementPorts": rsWSDManagementPorts,
       "rsWSDManagementPortsTable": rsWSDManagementPortsTable,
       "rsWSDManagementPortsEntry": rsWSDManagementPortsEntry,
       "rsWSDPortIndex": rsWSDPortIndex,
       "rsWSDPortOperation": rsWSDPortOperation,
       "rsCCK": rsCCK,
       "rsWSDSshParams": rsWSDSshParams,
       "rsWSDSshPort": rsWSDSshPort,
       "rsWSDSshStatus": rsWSDSshStatus,
       "rsWSDHttpsParams": rsWSDHttpsParams,
       "rsWSDHttpsPort": rsWSDHttpsPort,
       "rsWSDHttpsStatus": rsWSDHttpsStatus,
       "rsWSDStaticForwardingTable": rsWSDStaticForwardingTable,
       "rsWSDStaticForwardingEntry": rsWSDStaticForwardingEntry,
       "rsWSDStaticSourcePort": rsWSDStaticSourcePort,
       "rsWSDStaticDestinationPort": rsWSDStaticDestinationPort,
       "rsWSDStaticPortOperation": rsWSDStaticPortOperation,
       "rsWSDStaticStatus": rsWSDStaticStatus,
       "rsRadiusServer": rsRadiusServer,
       "rsRadiusMainServerAddr": rsRadiusMainServerAddr,
       "rsRadiusMainServerPort": rsRadiusMainServerPort,
       "rsRadiusMainServerSecret": rsRadiusMainServerSecret,
       "rsRadiusBackupServerAddr": rsRadiusBackupServerAddr,
       "rsRadiusBackupServerPort": rsRadiusBackupServerPort,
       "rsRadiusBackupServerSecret": rsRadiusBackupServerSecret,
       "rsAuthenticationMethod": rsAuthenticationMethod,
       "rsRadiusServerTimeout": rsRadiusServerTimeout,
       "rsRadiusServerRetries": rsRadiusServerRetries,
       "rsIfTable": rsIfTable,
       "rsIfEntry": rsIfEntry,
       "rsIfIndex": rsIfIndex,
       "rsIfSpeed": rsIfSpeed,
       "rsIfDuplex": rsIfDuplex,
       "rsIfAutoNegotiate": rsIfAutoNegotiate,
       "rsIfRowStatus": rsIfRowStatus,
       "rsWSDDeviceOperationMode": rsWSDDeviceOperationMode,
       "rsWSDVersionStatus": rsWSDVersionStatus,
       "rndMidLevelManagement": rndMidLevelManagement,
       "rndAlarmOptions": rndAlarmOptions,
       "rndAlarmEnabling": rndAlarmEnabling,
       "rndAlarmInterval": rndAlarmInterval,
       "rndMonitoredElementsTable": rndMonitoredElementsTable,
       "rndMonitoredElementEntry": rndMonitoredElementEntry,
       "rndMonitoredElementAddress": rndMonitoredElementAddress,
       "rndMonitoredElementCommunity": rndMonitoredElementCommunity,
       "rndMonitoredElementLabel": rndMonitoredElementLabel,
       "rndDefaultPollingInterval": rndDefaultPollingInterval,
       "rndDefaultLogFile": rndDefaultLogFile,
       "rndMonitoredElementStatus": rndMonitoredElementStatus,
       "rndMonitoringTable": rndMonitoringTable,
       "rndMonitoringEntry": rndMonitoringEntry,
       "rndMonitoredElement": rndMonitoredElement,
       "rndMonitoredObjectInstanceLabel": rndMonitoredObjectInstanceLabel,
       "rndMonitoredObjectName": rndMonitoredObjectName,
       "rndMonitoredObjectIdentifier": rndMonitoredObjectIdentifier,
       "rndMonitoredObjectInstance": rndMonitoredObjectInstance,
       "rndMonitoredObjectSyntax": rndMonitoredObjectSyntax,
       "rndMonitoringInterval": rndMonitoringInterval,
       "rndAlarmMaxTreshold": rndAlarmMaxTreshold,
       "rndAlarmMinTreshold": rndAlarmMinTreshold,
       "rndMonitoringLogfile": rndMonitoringLogfile,
       "rndMonitoringEntryStatus": rndMonitoringEntryStatus,
       "rndMibFilesTable": rndMibFilesTable,
       "rndMibFileEntry": rndMibFileEntry,
       "rndMibFileIndex": rndMibFileIndex,
       "rndMibFilePath": rndMibFilePath,
       "rndMibFileRefresh": rndMibFileRefresh,
       "rndMibFileEntryStatus": rndMibFileEntryStatus,
       "rndHardwareConfiguration": rndHardwareConfiguration,
       "rndEraseSimulatedConfiguration": rndEraseSimulatedConfiguration,
       "rndDeleteValuesTable": rndDeleteValuesTable,
       "rndDeleteValuesEntry": rndDeleteValuesEntry,
       "rndRowStatusVariableName": rndRowStatusVariableName,
       "rndRowStatusObjectId": rndRowStatusObjectId,
       "rndRowDeleteValue": rndRowDeleteValue,
       "rndDeleteValueEntryStatus": rndDeleteValueEntryStatus,
       "rsIpZeroHopRouting": rsIpZeroHopRouting,
       "rsIpZhrGeneralStatus": rsIpZhrGeneralStatus,
       "rsIpZhrAgingTimeout": rsIpZhrAgingTimeout,
       "rsIpZhrStatusTable": rsIpZhrStatusTable,
       "rsIpZhrStatusEntry": rsIpZhrStatusEntry,
       "rsIpZhrStatusIpIntf": rsIpZhrStatusIpIntf,
       "rsIpZhrAdminStatus": rsIpZhrAdminStatus,
       "rsIpZhrVirtAddressTable": rsIpZhrVirtAddressTable,
       "rsIpZhrVirtAddressEntry": rsIpZhrVirtAddressEntry,
       "rsIpZhrVirtAddressIpIntf": rsIpZhrVirtAddressIpIntf,
       "rsIpZhrVirtAddressTo": rsIpZhrVirtAddressTo,
       "rsIpZhrVirtAddressFrom": rsIpZhrVirtAddressFrom,
       "rsIpZhrVirtAddressStatus": rsIpZhrVirtAddressStatus,
       "rsIpZhrConnectionsTable": rsIpZhrConnectionsTable,
       "rsIpZhrConnectionEntry": rsIpZhrConnectionEntry,
       "rsIpZhrConnectionIpIntf": rsIpZhrConnectionIpIntf,
       "rsIpZhrConnectionSrcIp": rsIpZhrConnectionSrcIp,
       "rsIpZhrConnectionDestIp": rsIpZhrConnectionDestIp,
       "rsIpZhrConnectionVirtualIp": rsIpZhrConnectionVirtualIp,
       "rsIpZhrConnectionType": rsIpZhrConnectionType,
       "rsIpZhrConnectionAge": rsIpZhrConnectionAge,
       "rsIpZhrConnectionStatus": rsIpZhrConnectionStatus}
)
