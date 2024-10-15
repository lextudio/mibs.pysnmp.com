# SNMP MIB module (RND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:05 2024
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
              45)
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
    (0, "RND-MIB", "rndCommunityMngStationAddr"),
    (1, "RND-MIB", "rndCommunityString"),
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
    (0, "RND-MIB", "rndIfIndex"),
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
_RndIPXdriver_ObjectIdentity = ObjectIdentity
rndIPXdriver = _RndIPXdriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 1)
)
_RndIPXRip_ObjectIdentity = ObjectIdentity
rndIPXRip = _RndIPXRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 2)
)
_RndIPXRipFilterGlbTable_Object = MibTable
rndIPXRipFilterGlbTable = _RndIPXRipFilterGlbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10)
)
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbTable.setStatus("mandatory")
_RndIPXRipFilterGlbEntry_Object = MibTableRow
rndIPXRipFilterGlbEntry = _RndIPXRipFilterGlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1)
)
rndIPXRipFilterGlbEntry.setIndexNames(
    (0, "RND-MIB", "rndIPXRipFilterGlbFLtype"),
    (0, "RND-MIB", "rndIPXRipFilterGlbFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbEntry.setStatus("mandatory")


class _RndIPXRipFilterGlbFLtype_Type(Integer32):
    """Custom type rndIPXRipFilterGlbFLtype based on Integer32"""
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


_RndIPXRipFilterGlbFLtype_Type.__name__ = "Integer32"
_RndIPXRipFilterGlbFLtype_Object = MibTableColumn
rndIPXRipFilterGlbFLtype = _RndIPXRipFilterGlbFLtype_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 1),
    _RndIPXRipFilterGlbFLtype_Type()
)
rndIPXRipFilterGlbFLtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLtype.setStatus("mandatory")
_RndIPXRipFilterGlbFLnumber_Type = Integer32
_RndIPXRipFilterGlbFLnumber_Object = MibTableColumn
rndIPXRipFilterGlbFLnumber = _RndIPXRipFilterGlbFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 2),
    _RndIPXRipFilterGlbFLnumber_Type()
)
rndIPXRipFilterGlbFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLnumber.setStatus("mandatory")


class _RndIPXRipFilterGlbFLStatus_Type(Integer32):
    """Custom type rndIPXRipFilterGlbFLStatus based on Integer32"""
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


_RndIPXRipFilterGlbFLStatus_Type.__name__ = "Integer32"
_RndIPXRipFilterGlbFLStatus_Object = MibTableColumn
rndIPXRipFilterGlbFLStatus = _RndIPXRipFilterGlbFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 3),
    _RndIPXRipFilterGlbFLStatus_Type()
)
rndIPXRipFilterGlbFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLStatus.setStatus("mandatory")


class _RndIPXRipFilterGlbFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXRipFilterGlbFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXRipFilterGlbFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXRipFilterGlbFLnetworkPatern_Object = MibTableColumn
rndIPXRipFilterGlbFLnetworkPatern = _RndIPXRipFilterGlbFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 4),
    _RndIPXRipFilterGlbFLnetworkPatern_Type()
)
rndIPXRipFilterGlbFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLnetworkPatern.setStatus("mandatory")


class _RndIPXRipFilterGlbFLnetworkMask_Type(OctetString):
    """Custom type rndIPXRipFilterGlbFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXRipFilterGlbFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXRipFilterGlbFLnetworkMask_Object = MibTableColumn
rndIPXRipFilterGlbFLnetworkMask = _RndIPXRipFilterGlbFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 5),
    _RndIPXRipFilterGlbFLnetworkMask_Type()
)
rndIPXRipFilterGlbFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLnetworkMask.setStatus("mandatory")


class _RndIPXRipFilterGlbFLaction_Type(Integer32):
    """Custom type rndIPXRipFilterGlbFLaction based on Integer32"""
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


_RndIPXRipFilterGlbFLaction_Type.__name__ = "Integer32"
_RndIPXRipFilterGlbFLaction_Object = MibTableColumn
rndIPXRipFilterGlbFLaction = _RndIPXRipFilterGlbFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 6),
    _RndIPXRipFilterGlbFLaction_Type()
)
rndIPXRipFilterGlbFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLaction.setStatus("mandatory")
_RndIPXRipFilterCircuitTable_Object = MibTable
rndIPXRipFilterCircuitTable = _RndIPXRipFilterCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11)
)
if mibBuilder.loadTexts:
    rndIPXRipFilterCircuitTable.setStatus("mandatory")
_RndIPXRipFilterCircuitEntry_Object = MibTableRow
rndIPXRipFilterCircuitEntry = _RndIPXRipFilterCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1)
)
rndIPXRipFilterCircuitEntry.setIndexNames(
    (0, "RND-MIB", "rndIPXRipFilterCircFLIfIndex"),
    (0, "RND-MIB", "rndIPXRipFilterCircFLType"),
    (0, "RND-MIB", "rndIPXRipFilterCircFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXRipFilterCircuitEntry.setStatus("mandatory")
_RndIPXRipFilterCircFLIfIndex_Type = Integer32
_RndIPXRipFilterCircFLIfIndex_Object = MibTableColumn
rndIPXRipFilterCircFLIfIndex = _RndIPXRipFilterCircFLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 1),
    _RndIPXRipFilterCircFLIfIndex_Type()
)
rndIPXRipFilterCircFLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLIfIndex.setStatus("mandatory")


class _RndIPXRipFilterCircFLType_Type(Integer32):
    """Custom type rndIPXRipFilterCircFLType based on Integer32"""
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


_RndIPXRipFilterCircFLType_Type.__name__ = "Integer32"
_RndIPXRipFilterCircFLType_Object = MibTableColumn
rndIPXRipFilterCircFLType = _RndIPXRipFilterCircFLType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 2),
    _RndIPXRipFilterCircFLType_Type()
)
rndIPXRipFilterCircFLType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLType.setStatus("mandatory")
_RndIPXRipFilterCircFLnumber_Type = Integer32
_RndIPXRipFilterCircFLnumber_Object = MibTableColumn
rndIPXRipFilterCircFLnumber = _RndIPXRipFilterCircFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 3),
    _RndIPXRipFilterCircFLnumber_Type()
)
rndIPXRipFilterCircFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLnumber.setStatus("mandatory")


class _RndIPXRipFilterCircFLStatus_Type(Integer32):
    """Custom type rndIPXRipFilterCircFLStatus based on Integer32"""
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


_RndIPXRipFilterCircFLStatus_Type.__name__ = "Integer32"
_RndIPXRipFilterCircFLStatus_Object = MibTableColumn
rndIPXRipFilterCircFLStatus = _RndIPXRipFilterCircFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 4),
    _RndIPXRipFilterCircFLStatus_Type()
)
rndIPXRipFilterCircFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLStatus.setStatus("mandatory")


class _RndIPXRipFilterCircFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXRipFilterCircFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXRipFilterCircFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXRipFilterCircFLnetworkPatern_Object = MibTableColumn
rndIPXRipFilterCircFLnetworkPatern = _RndIPXRipFilterCircFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 5),
    _RndIPXRipFilterCircFLnetworkPatern_Type()
)
rndIPXRipFilterCircFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLnetworkPatern.setStatus("mandatory")


class _RndIPXRipFilterCircFLnetworkMask_Type(OctetString):
    """Custom type rndIPXRipFilterCircFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXRipFilterCircFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXRipFilterCircFLnetworkMask_Object = MibTableColumn
rndIPXRipFilterCircFLnetworkMask = _RndIPXRipFilterCircFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 6),
    _RndIPXRipFilterCircFLnetworkMask_Type()
)
rndIPXRipFilterCircFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLnetworkMask.setStatus("mandatory")


class _RndIPXRipFilterCircFLaction_Type(Integer32):
    """Custom type rndIPXRipFilterCircFLaction based on Integer32"""
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


_RndIPXRipFilterCircFLaction_Type.__name__ = "Integer32"
_RndIPXRipFilterCircFLaction_Object = MibTableColumn
rndIPXRipFilterCircFLaction = _RndIPXRipFilterCircFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 7),
    _RndIPXRipFilterCircFLaction_Type()
)
rndIPXRipFilterCircFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLaction.setStatus("mandatory")
_RndIPXSap_ObjectIdentity = ObjectIdentity
rndIPXSap = _RndIPXSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 3)
)
_RndIPXSapFilterGlbTable_Object = MibTable
rndIPXSapFilterGlbTable = _RndIPXSapFilterGlbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10)
)
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbTable.setStatus("mandatory")
_RndIPXSapFilterGlbEntry_Object = MibTableRow
rndIPXSapFilterGlbEntry = _RndIPXSapFilterGlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1)
)
rndIPXSapFilterGlbEntry.setIndexNames(
    (0, "RND-MIB", "rndIPXSapFilterGlbFLtype"),
    (0, "RND-MIB", "rndIPXSapFilterGlbFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbEntry.setStatus("mandatory")


class _RndIPXSapFilterGlbFLtype_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLtype based on Integer32"""
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


_RndIPXSapFilterGlbFLtype_Type.__name__ = "Integer32"
_RndIPXSapFilterGlbFLtype_Object = MibTableColumn
rndIPXSapFilterGlbFLtype = _RndIPXSapFilterGlbFLtype_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 1),
    _RndIPXSapFilterGlbFLtype_Type()
)
rndIPXSapFilterGlbFLtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLtype.setStatus("mandatory")
_RndIPXSapFilterGlbFLnumber_Type = Integer32
_RndIPXSapFilterGlbFLnumber_Object = MibTableColumn
rndIPXSapFilterGlbFLnumber = _RndIPXSapFilterGlbFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 2),
    _RndIPXSapFilterGlbFLnumber_Type()
)
rndIPXSapFilterGlbFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLnumber.setStatus("mandatory")


class _RndIPXSapFilterGlbFLStatus_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLStatus based on Integer32"""
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


_RndIPXSapFilterGlbFLStatus_Type.__name__ = "Integer32"
_RndIPXSapFilterGlbFLStatus_Object = MibTableColumn
rndIPXSapFilterGlbFLStatus = _RndIPXSapFilterGlbFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 3),
    _RndIPXSapFilterGlbFLStatus_Type()
)
rndIPXSapFilterGlbFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLStatus.setStatus("mandatory")


class _RndIPXSapFilterGlbFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXSapFilterGlbFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXSapFilterGlbFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXSapFilterGlbFLnetworkPatern_Object = MibTableColumn
rndIPXSapFilterGlbFLnetworkPatern = _RndIPXSapFilterGlbFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 4),
    _RndIPXSapFilterGlbFLnetworkPatern_Type()
)
rndIPXSapFilterGlbFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLnetworkPatern.setStatus("mandatory")


class _RndIPXSapFilterGlbFLnetworkMask_Type(OctetString):
    """Custom type rndIPXSapFilterGlbFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXSapFilterGlbFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXSapFilterGlbFLnetworkMask_Object = MibTableColumn
rndIPXSapFilterGlbFLnetworkMask = _RndIPXSapFilterGlbFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 5),
    _RndIPXSapFilterGlbFLnetworkMask_Type()
)
rndIPXSapFilterGlbFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLnetworkMask.setStatus("mandatory")


class _RndIPXSapFilterGlbFLserviceType_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLserviceType based on Integer32"""
    defaultHexValue = 65535


_RndIPXSapFilterGlbFLserviceType_Object = MibTableColumn
rndIPXSapFilterGlbFLserviceType = _RndIPXSapFilterGlbFLserviceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 6),
    _RndIPXSapFilterGlbFLserviceType_Type()
)
rndIPXSapFilterGlbFLserviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLserviceType.setStatus("mandatory")


class _RndIPXSapFilterGlbFLserviceName_Type(OctetString):
    """Custom type rndIPXSapFilterGlbFLserviceName based on OctetString"""
    defaultValue = OctetString("*")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RndIPXSapFilterGlbFLserviceName_Type.__name__ = "OctetString"
_RndIPXSapFilterGlbFLserviceName_Object = MibTableColumn
rndIPXSapFilterGlbFLserviceName = _RndIPXSapFilterGlbFLserviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 7),
    _RndIPXSapFilterGlbFLserviceName_Type()
)
rndIPXSapFilterGlbFLserviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLserviceName.setStatus("mandatory")


class _RndIPXSapFilterGlbFLaction_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLaction based on Integer32"""
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


_RndIPXSapFilterGlbFLaction_Type.__name__ = "Integer32"
_RndIPXSapFilterGlbFLaction_Object = MibTableColumn
rndIPXSapFilterGlbFLaction = _RndIPXSapFilterGlbFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 8),
    _RndIPXSapFilterGlbFLaction_Type()
)
rndIPXSapFilterGlbFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLaction.setStatus("mandatory")
_RndIPXSapFilterCircuitTable_Object = MibTable
rndIPXSapFilterCircuitTable = _RndIPXSapFilterCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11)
)
if mibBuilder.loadTexts:
    rndIPXSapFilterCircuitTable.setStatus("mandatory")
_RndIPXSapFilterCircuitEntry_Object = MibTableRow
rndIPXSapFilterCircuitEntry = _RndIPXSapFilterCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1)
)
rndIPXSapFilterCircuitEntry.setIndexNames(
    (0, "RND-MIB", "rndIPXSapFilterCircFLIfIndex"),
    (0, "RND-MIB", "rndIPXSapFilterCircFLtype"),
    (0, "RND-MIB", "rndIPXSapFilterCircFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXSapFilterCircuitEntry.setStatus("mandatory")
_RndIPXSapFilterCircFLIfIndex_Type = Integer32
_RndIPXSapFilterCircFLIfIndex_Object = MibTableColumn
rndIPXSapFilterCircFLIfIndex = _RndIPXSapFilterCircFLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 1),
    _RndIPXSapFilterCircFLIfIndex_Type()
)
rndIPXSapFilterCircFLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLIfIndex.setStatus("mandatory")


class _RndIPXSapFilterCircFLtype_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLtype based on Integer32"""
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


_RndIPXSapFilterCircFLtype_Type.__name__ = "Integer32"
_RndIPXSapFilterCircFLtype_Object = MibTableColumn
rndIPXSapFilterCircFLtype = _RndIPXSapFilterCircFLtype_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 2),
    _RndIPXSapFilterCircFLtype_Type()
)
rndIPXSapFilterCircFLtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLtype.setStatus("mandatory")
_RndIPXSapFilterCircFLnumber_Type = Integer32
_RndIPXSapFilterCircFLnumber_Object = MibTableColumn
rndIPXSapFilterCircFLnumber = _RndIPXSapFilterCircFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 3),
    _RndIPXSapFilterCircFLnumber_Type()
)
rndIPXSapFilterCircFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLnumber.setStatus("mandatory")


class _RndIPXSapFilterCircFLStatus_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLStatus based on Integer32"""
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


_RndIPXSapFilterCircFLStatus_Type.__name__ = "Integer32"
_RndIPXSapFilterCircFLStatus_Object = MibTableColumn
rndIPXSapFilterCircFLStatus = _RndIPXSapFilterCircFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 4),
    _RndIPXSapFilterCircFLStatus_Type()
)
rndIPXSapFilterCircFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLStatus.setStatus("mandatory")


class _RndIPXSapFilterCircFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXSapFilterCircFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXSapFilterCircFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXSapFilterCircFLnetworkPatern_Object = MibTableColumn
rndIPXSapFilterCircFLnetworkPatern = _RndIPXSapFilterCircFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 5),
    _RndIPXSapFilterCircFLnetworkPatern_Type()
)
rndIPXSapFilterCircFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLnetworkPatern.setStatus("mandatory")


class _RndIPXSapFilterCircFLnetworkMask_Type(OctetString):
    """Custom type rndIPXSapFilterCircFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RndIPXSapFilterCircFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXSapFilterCircFLnetworkMask_Object = MibTableColumn
rndIPXSapFilterCircFLnetworkMask = _RndIPXSapFilterCircFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 6),
    _RndIPXSapFilterCircFLnetworkMask_Type()
)
rndIPXSapFilterCircFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLnetworkMask.setStatus("mandatory")


class _RndIPXSapFilterCircFLserviceType_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLserviceType based on Integer32"""
    defaultHexValue = 65535


_RndIPXSapFilterCircFLserviceType_Object = MibTableColumn
rndIPXSapFilterCircFLserviceType = _RndIPXSapFilterCircFLserviceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 7),
    _RndIPXSapFilterCircFLserviceType_Type()
)
rndIPXSapFilterCircFLserviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLserviceType.setStatus("mandatory")


class _RndIPXSapFilterCircFLserviceName_Type(OctetString):
    """Custom type rndIPXSapFilterCircFLserviceName based on OctetString"""
    defaultValue = OctetString("*")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RndIPXSapFilterCircFLserviceName_Type.__name__ = "OctetString"
_RndIPXSapFilterCircFLserviceName_Object = MibTableColumn
rndIPXSapFilterCircFLserviceName = _RndIPXSapFilterCircFLserviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 8),
    _RndIPXSapFilterCircFLserviceName_Type()
)
rndIPXSapFilterCircFLserviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLserviceName.setStatus("mandatory")


class _RndIPXSapFilterCircFLaction_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLaction based on Integer32"""
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


_RndIPXSapFilterCircFLaction_Type.__name__ = "Integer32"
_RndIPXSapFilterCircFLaction_Object = MibTableColumn
rndIPXSapFilterCircFLaction = _RndIPXSapFilterCircFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 9),
    _RndIPXSapFilterCircFLaction_Type()
)
rndIPXSapFilterCircFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLaction.setStatus("mandatory")
_IpxSystem_ObjectIdentity = ObjectIdentity
ipxSystem = _IpxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 4)
)
_IpxBasicSysTable_Object = MibTable
ipxBasicSysTable = _IpxBasicSysTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1)
)
if mibBuilder.loadTexts:
    ipxBasicSysTable.setStatus("mandatory")
_IpxBasicSysEntry_Object = MibTableRow
ipxBasicSysEntry = _IpxBasicSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1)
)
ipxBasicSysEntry.setIndexNames(
    (0, "RND-MIB", "ipxBasicSysInstance"),
)
if mibBuilder.loadTexts:
    ipxBasicSysEntry.setStatus("mandatory")
_IpxBasicSysInstance_Type = Integer32
_IpxBasicSysInstance_Object = MibTableColumn
ipxBasicSysInstance = _IpxBasicSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 1),
    _IpxBasicSysInstance_Type()
)
ipxBasicSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysInstance.setStatus("mandatory")


class _IpxBasicSysExistState_Type(Integer32):
    """Custom type ipxBasicSysExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxBasicSysExistState_Type.__name__ = "Integer32"
_IpxBasicSysExistState_Object = MibTableColumn
ipxBasicSysExistState = _IpxBasicSysExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 2),
    _IpxBasicSysExistState_Type()
)
ipxBasicSysExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysExistState.setStatus("mandatory")
_IpxBasicSysInReceives_Type = Counter32
_IpxBasicSysInReceives_Object = MibTableColumn
ipxBasicSysInReceives = _IpxBasicSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 3),
    _IpxBasicSysInReceives_Type()
)
ipxBasicSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInReceives.setStatus("mandatory")
_IpxBasicSysInHdrErrors_Type = Counter32
_IpxBasicSysInHdrErrors_Object = MibTableColumn
ipxBasicSysInHdrErrors = _IpxBasicSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 4),
    _IpxBasicSysInHdrErrors_Type()
)
ipxBasicSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInHdrErrors.setStatus("mandatory")
_IpxBasicSysInUnknownSockets_Type = Counter32
_IpxBasicSysInUnknownSockets_Object = MibTableColumn
ipxBasicSysInUnknownSockets = _IpxBasicSysInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 5),
    _IpxBasicSysInUnknownSockets_Type()
)
ipxBasicSysInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInUnknownSockets.setStatus("mandatory")
_IpxBasicSysInDiscards_Type = Counter32
_IpxBasicSysInDiscards_Object = MibTableColumn
ipxBasicSysInDiscards = _IpxBasicSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 6),
    _IpxBasicSysInDiscards_Type()
)
ipxBasicSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDiscards.setStatus("mandatory")
_IpxBasicSysInDelivers_Type = Counter32
_IpxBasicSysInDelivers_Object = MibTableColumn
ipxBasicSysInDelivers = _IpxBasicSysInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 7),
    _IpxBasicSysInDelivers_Type()
)
ipxBasicSysInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDelivers.setStatus("mandatory")
_IpxBasicSysNoRoutes_Type = Counter32
_IpxBasicSysNoRoutes_Object = MibTableColumn
ipxBasicSysNoRoutes = _IpxBasicSysNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 8),
    _IpxBasicSysNoRoutes_Type()
)
ipxBasicSysNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysNoRoutes.setStatus("mandatory")
_IpxBasicSysOutRequests_Type = Counter32
_IpxBasicSysOutRequests_Object = MibTableColumn
ipxBasicSysOutRequests = _IpxBasicSysOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 9),
    _IpxBasicSysOutRequests_Type()
)
ipxBasicSysOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutRequests.setStatus("mandatory")
_IpxBasicSysOutMalformedRequests_Type = Counter32
_IpxBasicSysOutMalformedRequests_Object = MibTableColumn
ipxBasicSysOutMalformedRequests = _IpxBasicSysOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 10),
    _IpxBasicSysOutMalformedRequests_Type()
)
ipxBasicSysOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutMalformedRequests.setStatus("mandatory")
_IpxBasicSysOutDiscards_Type = Counter32
_IpxBasicSysOutDiscards_Object = MibTableColumn
ipxBasicSysOutDiscards = _IpxBasicSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 11),
    _IpxBasicSysOutDiscards_Type()
)
ipxBasicSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutDiscards.setStatus("mandatory")
_IpxBasicSysOutPackets_Type = Counter32
_IpxBasicSysOutPackets_Object = MibTableColumn
ipxBasicSysOutPackets = _IpxBasicSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 12),
    _IpxBasicSysOutPackets_Type()
)
ipxBasicSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutPackets.setStatus("mandatory")
_IpxCircuit_ObjectIdentity = ObjectIdentity
ipxCircuit = _IpxCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 5)
)
_IpxCircTable_Object = MibTable
ipxCircTable = _IpxCircTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1)
)
if mibBuilder.loadTexts:
    ipxCircTable.setStatus("mandatory")
_IpxCircEntry_Object = MibTableRow
ipxCircEntry = _IpxCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1)
)
ipxCircEntry.setIndexNames(
    (0, "RND-MIB", "ipxCircSysInstance"),
    (0, "RND-MIB", "ipxCircIndex"),
)
if mibBuilder.loadTexts:
    ipxCircEntry.setStatus("mandatory")
_IpxCircSysInstance_Type = Integer32
_IpxCircSysInstance_Object = MibTableColumn
ipxCircSysInstance = _IpxCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 1),
    _IpxCircSysInstance_Type()
)
ipxCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSysInstance.setStatus("mandatory")
_IpxCircIndex_Type = Integer32
_IpxCircIndex_Object = MibTableColumn
ipxCircIndex = _IpxCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 2),
    _IpxCircIndex_Type()
)
ipxCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIndex.setStatus("mandatory")


class _IpxCircExistState_Type(Integer32):
    """Custom type ipxCircExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("sleeping", 3))
    )


_IpxCircExistState_Type.__name__ = "Integer32"
_IpxCircExistState_Object = MibTableColumn
ipxCircExistState = _IpxCircExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 3),
    _IpxCircExistState_Type()
)
ipxCircExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircExistState.setStatus("mandatory")


class _IpxCircOperState_Type(Integer32):
    """Custom type ipxCircOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_IpxCircOperState_Type.__name__ = "Integer32"
_IpxCircOperState_Object = MibTableColumn
ipxCircOperState = _IpxCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 4),
    _IpxCircOperState_Type()
)
ipxCircOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircOperState.setStatus("mandatory")
_IpxCircIfIndex_Type = Integer32
_IpxCircIfIndex_Object = MibTableColumn
ipxCircIfIndex = _IpxCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 5),
    _IpxCircIfIndex_Type()
)
ipxCircIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIfIndex.setStatus("mandatory")
_IpxCircNetNumber_Type = NetNumber
_IpxCircNetNumber_Object = MibTableColumn
ipxCircNetNumber = _IpxCircNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 6),
    _IpxCircNetNumber_Type()
)
ipxCircNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetNumber.setStatus("mandatory")


class _IpxCircTimeToNet_Type(Integer32):
    """Custom type ipxCircTimeToNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpxCircTimeToNet_Type.__name__ = "Integer32"
_IpxCircTimeToNet_Object = MibTableColumn
ipxCircTimeToNet = _IpxCircTimeToNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 7),
    _IpxCircTimeToNet_Type()
)
ipxCircTimeToNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircTimeToNet.setStatus("mandatory")


class _IpxCircEncaps_Type(Integer32):
    """Custom type ipxCircEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("llc", 3),
          ("none", 10),
          ("novell", 1),
          ("snap", 4))
    )


_IpxCircEncaps_Type.__name__ = "Integer32"
_IpxCircEncaps_Object = MibTableColumn
ipxCircEncaps = _IpxCircEncaps_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 8),
    _IpxCircEncaps_Type()
)
ipxCircEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircEncaps.setStatus("mandatory")


class _IpxCircNetbiosDeliver_Type(Integer32):
    """Custom type ipxCircNetbiosDeliver based on Integer32"""
    defaultValue = 1

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


_IpxCircNetbiosDeliver_Type.__name__ = "Integer32"
_IpxCircNetbiosDeliver_Object = MibTableColumn
ipxCircNetbiosDeliver = _IpxCircNetbiosDeliver_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 9),
    _IpxCircNetbiosDeliver_Type()
)
ipxCircNetbiosDeliver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetbiosDeliver.setStatus("mandatory")
_IpxForwarding_ObjectIdentity = ObjectIdentity
ipxForwarding = _IpxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 6)
)
_IpxDestTable_Object = MibTable
ipxDestTable = _IpxDestTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1)
)
if mibBuilder.loadTexts:
    ipxDestTable.setStatus("mandatory")
_IpxDestEntry_Object = MibTableRow
ipxDestEntry = _IpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1)
)
ipxDestEntry.setIndexNames(
    (0, "RND-MIB", "ipxDestSysInstance"),
    (0, "RND-MIB", "ipxDestNetNum"),
    (0, "RND-MIB", "ipxDestNextHopCircIndex"),
)
if mibBuilder.loadTexts:
    ipxDestEntry.setStatus("mandatory")
_IpxDestSysInstance_Type = Integer32
_IpxDestSysInstance_Object = MibTableColumn
ipxDestSysInstance = _IpxDestSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 1),
    _IpxDestSysInstance_Type()
)
ipxDestSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestSysInstance.setStatus("mandatory")
_IpxDestNetNum_Type = NetNumber
_IpxDestNetNum_Object = MibTableColumn
ipxDestNetNum = _IpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 2),
    _IpxDestNetNum_Type()
)
ipxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNetNum.setStatus("mandatory")
_IpxDestNextHopCircIndex_Type = Integer32
_IpxDestNextHopCircIndex_Object = MibTableColumn
ipxDestNextHopCircIndex = _IpxDestNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 3),
    _IpxDestNextHopCircIndex_Type()
)
ipxDestNextHopCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopCircIndex.setStatus("mandatory")


class _IpxDestProtocol_Type(Integer32):
    """Custom type ipxDestProtocol based on Integer32"""
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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5))
    )


_IpxDestProtocol_Type.__name__ = "Integer32"
_IpxDestProtocol_Object = MibTableColumn
ipxDestProtocol = _IpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 4),
    _IpxDestProtocol_Type()
)
ipxDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestProtocol.setStatus("mandatory")
_IpxDestTicks_Type = Integer32
_IpxDestTicks_Object = MibTableColumn
ipxDestTicks = _IpxDestTicks_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 5),
    _IpxDestTicks_Type()
)
ipxDestTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestTicks.setStatus("mandatory")
_IpxDestHopCount_Type = Integer32
_IpxDestHopCount_Object = MibTableColumn
ipxDestHopCount = _IpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 6),
    _IpxDestHopCount_Type()
)
ipxDestHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestHopCount.setStatus("mandatory")


class _IpxDestNextHopNICAddress_Type(PhysAddress):
    """Custom type ipxDestNextHopNICAddress based on PhysAddress"""
    defaultHexValue = "A102B304C506"


_IpxDestNextHopNICAddress_Object = MibTableColumn
ipxDestNextHopNICAddress = _IpxDestNextHopNICAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 7),
    _IpxDestNextHopNICAddress_Type()
)
ipxDestNextHopNICAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNICAddress.setStatus("mandatory")
_IpxDestNextHopNetNum_Type = NetNumber
_IpxDestNextHopNetNum_Object = MibTableColumn
ipxDestNextHopNetNum = _IpxDestNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 8),
    _IpxDestNextHopNetNum_Type()
)
ipxDestNextHopNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNetNum.setStatus("mandatory")


class _IpxDestExistState_Type(Integer32):
    """Custom type ipxDestExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxDestExistState_Type.__name__ = "Integer32"
_IpxDestExistState_Object = MibTableColumn
ipxDestExistState = _IpxDestExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 9),
    _IpxDestExistState_Type()
)
ipxDestExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestExistState.setStatus("mandatory")
_IpxServices_ObjectIdentity = ObjectIdentity
ipxServices = _IpxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 7)
)
_IpxServTable_Object = MibTable
ipxServTable = _IpxServTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1)
)
if mibBuilder.loadTexts:
    ipxServTable.setStatus("mandatory")
_IpxServEntry_Object = MibTableRow
ipxServEntry = _IpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1)
)
ipxServEntry.setIndexNames(
    (0, "RND-MIB", "ipxServSysInstance"),
    (0, "RND-MIB", "ipxServType"),
    (1, "RND-MIB", "ipxServName"),
)
if mibBuilder.loadTexts:
    ipxServEntry.setStatus("mandatory")
_IpxServSysInstance_Type = Integer32
_IpxServSysInstance_Object = MibTableColumn
ipxServSysInstance = _IpxServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 1),
    _IpxServSysInstance_Type()
)
ipxServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServSysInstance.setStatus("mandatory")


class _IpxServType_Type(OctetString):
    """Custom type ipxServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxServType_Type.__name__ = "OctetString"
_IpxServType_Object = MibTableColumn
ipxServType = _IpxServType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 2),
    _IpxServType_Type()
)
ipxServType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServType.setStatus("mandatory")


class _IpxServName_Type(OctetString):
    """Custom type ipxServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServName_Type.__name__ = "OctetString"
_IpxServName_Object = MibTableColumn
ipxServName = _IpxServName_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 3),
    _IpxServName_Type()
)
ipxServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServName.setStatus("mandatory")


class _IpxServProtocol_Type(Integer32):
    """Custom type ipxServProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("sap", 6),
          ("static", 5))
    )


_IpxServProtocol_Type.__name__ = "Integer32"
_IpxServProtocol_Object = MibTableColumn
ipxServProtocol = _IpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 4),
    _IpxServProtocol_Type()
)
ipxServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServProtocol.setStatus("mandatory")
_IpxServNetNum_Type = NetNumber
_IpxServNetNum_Object = MibTableColumn
ipxServNetNum = _IpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 5),
    _IpxServNetNum_Type()
)
ipxServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNetNum.setStatus("mandatory")


class _IpxServNode_Type(OctetString):
    """Custom type ipxServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxServNode_Type.__name__ = "OctetString"
_IpxServNode_Object = MibTableColumn
ipxServNode = _IpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 6),
    _IpxServNode_Type()
)
ipxServNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNode.setStatus("mandatory")


class _IpxServSocket_Type(OctetString):
    """Custom type ipxServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxServSocket_Type.__name__ = "OctetString"
_IpxServSocket_Object = MibTableColumn
ipxServSocket = _IpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 7),
    _IpxServSocket_Type()
)
ipxServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServSocket.setStatus("mandatory")
_IpxServHopCount_Type = Integer32
_IpxServHopCount_Object = MibTableColumn
ipxServHopCount = _IpxServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 8),
    _IpxServHopCount_Type()
)
ipxServHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServHopCount.setStatus("mandatory")


class _IpxServExistState_Type(Integer32):
    """Custom type ipxServExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxServExistState_Type.__name__ = "Integer32"
_IpxServExistState_Object = MibTableColumn
ipxServExistState = _IpxServExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 9),
    _IpxServExistState_Type()
)
ipxServExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServExistState.setStatus("mandatory")
_Ripsap_ObjectIdentity = ObjectIdentity
ripsap = _Ripsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 8)
)
_RipsapSystem_ObjectIdentity = ObjectIdentity
ripsapSystem = _RipsapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1)
)
_RipSysTable_Object = MibTable
ripSysTable = _RipSysTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ripSysTable.setStatus("mandatory")
_RipSysEntry_Object = MibTableRow
ripSysEntry = _RipSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1)
)
ripSysEntry.setIndexNames(
    (0, "RND-MIB", "ripSysInstance"),
)
if mibBuilder.loadTexts:
    ripSysEntry.setStatus("mandatory")
_RipSysInstance_Type = Integer32
_RipSysInstance_Object = MibTableColumn
ripSysInstance = _RipSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1, 1),
    _RipSysInstance_Type()
)
ripSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripSysInstance.setStatus("mandatory")


class _RipSysState_Type(Integer32):
    """Custom type ripSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RipSysState_Type.__name__ = "Integer32"
_RipSysState_Object = MibTableColumn
ripSysState = _RipSysState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1, 2),
    _RipSysState_Type()
)
ripSysState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripSysState.setStatus("mandatory")
_RipSysIncorrectPackets_Type = Counter32
_RipSysIncorrectPackets_Object = MibTableColumn
ripSysIncorrectPackets = _RipSysIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1, 3),
    _RipSysIncorrectPackets_Type()
)
ripSysIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripSysIncorrectPackets.setStatus("mandatory")
_SapSysTable_Object = MibTable
sapSysTable = _SapSysTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2)
)
if mibBuilder.loadTexts:
    sapSysTable.setStatus("mandatory")
_SapSysEntry_Object = MibTableRow
sapSysEntry = _SapSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1)
)
sapSysEntry.setIndexNames(
    (0, "RND-MIB", "sapSysInstance"),
)
if mibBuilder.loadTexts:
    sapSysEntry.setStatus("mandatory")
_SapSysInstance_Type = Integer32
_SapSysInstance_Object = MibTableColumn
sapSysInstance = _SapSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1, 1),
    _SapSysInstance_Type()
)
sapSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapSysInstance.setStatus("mandatory")


class _SapSysState_Type(Integer32):
    """Custom type sapSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SapSysState_Type.__name__ = "Integer32"
_SapSysState_Object = MibTableColumn
sapSysState = _SapSysState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1, 2),
    _SapSysState_Type()
)
sapSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapSysState.setStatus("mandatory")
_SapSysIncorrectPackets_Type = Counter32
_SapSysIncorrectPackets_Object = MibTableColumn
sapSysIncorrectPackets = _SapSysIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1, 3),
    _SapSysIncorrectPackets_Type()
)
sapSysIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapSysIncorrectPackets.setStatus("mandatory")
_RipsapCircuit_ObjectIdentity = ObjectIdentity
ripsapCircuit = _RipsapCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2)
)
_RipCircTable_Object = MibTable
ripCircTable = _RipCircTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1)
)
if mibBuilder.loadTexts:
    ripCircTable.setStatus("mandatory")
_RipCircEntry_Object = MibTableRow
ripCircEntry = _RipCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1)
)
ripCircEntry.setIndexNames(
    (0, "RND-MIB", "ripCircSysInstance"),
    (0, "RND-MIB", "ripCircIndex"),
)
if mibBuilder.loadTexts:
    ripCircEntry.setStatus("mandatory")
_RipCircSysInstance_Type = Integer32
_RipCircSysInstance_Object = MibTableColumn
ripCircSysInstance = _RipCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 1),
    _RipCircSysInstance_Type()
)
ripCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircSysInstance.setStatus("mandatory")
_RipCircIndex_Type = Integer32
_RipCircIndex_Object = MibTableColumn
ripCircIndex = _RipCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 2),
    _RipCircIndex_Type()
)
ripCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircIndex.setStatus("mandatory")


class _RipCircState_Type(Integer32):
    """Custom type ripCircState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RipCircState_Type.__name__ = "Integer32"
_RipCircState_Object = MibTableColumn
ripCircState = _RipCircState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 3),
    _RipCircState_Type()
)
ripCircState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircState.setStatus("mandatory")


class _RipCircUpdate_Type(Integer32):
    """Custom type ripCircUpdate based on Integer32"""
    defaultValue = 60


_RipCircUpdate_Object = MibTableColumn
ripCircUpdate = _RipCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 4),
    _RipCircUpdate_Type()
)
ripCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircUpdate.setStatus("mandatory")


class _RipCircAgeMultiplier_Type(Integer32):
    """Custom type ripCircAgeMultiplier based on Integer32"""
    defaultValue = 4


_RipCircAgeMultiplier_Object = MibTableColumn
ripCircAgeMultiplier = _RipCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 5),
    _RipCircAgeMultiplier_Type()
)
ripCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircAgeMultiplier.setStatus("mandatory")
_RipCircOutPackets_Type = Counter32
_RipCircOutPackets_Object = MibTableColumn
ripCircOutPackets = _RipCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 6),
    _RipCircOutPackets_Type()
)
ripCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCircOutPackets.setStatus("mandatory")
_RipCircInPackets_Type = Counter32
_RipCircInPackets_Object = MibTableColumn
ripCircInPackets = _RipCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 7),
    _RipCircInPackets_Type()
)
ripCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCircInPackets.setStatus("mandatory")
_SapCircTable_Object = MibTable
sapCircTable = _SapCircTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2)
)
if mibBuilder.loadTexts:
    sapCircTable.setStatus("mandatory")
_SapCircEntry_Object = MibTableRow
sapCircEntry = _SapCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1)
)
sapCircEntry.setIndexNames(
    (0, "RND-MIB", "sapCircSysInstance"),
    (0, "RND-MIB", "sapCircIndex"),
)
if mibBuilder.loadTexts:
    sapCircEntry.setStatus("mandatory")
_SapCircSysInstance_Type = Integer32
_SapCircSysInstance_Object = MibTableColumn
sapCircSysInstance = _SapCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 1),
    _SapCircSysInstance_Type()
)
sapCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircSysInstance.setStatus("mandatory")
_SapCircIndex_Type = Integer32
_SapCircIndex_Object = MibTableColumn
sapCircIndex = _SapCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 2),
    _SapCircIndex_Type()
)
sapCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircIndex.setStatus("mandatory")


class _SapCircState_Type(Integer32):
    """Custom type sapCircState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SapCircState_Type.__name__ = "Integer32"
_SapCircState_Object = MibTableColumn
sapCircState = _SapCircState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 3),
    _SapCircState_Type()
)
sapCircState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircState.setStatus("mandatory")


class _SapCircUpdate_Type(Integer32):
    """Custom type sapCircUpdate based on Integer32"""
    defaultValue = 60


_SapCircUpdate_Object = MibTableColumn
sapCircUpdate = _SapCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 4),
    _SapCircUpdate_Type()
)
sapCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircUpdate.setStatus("mandatory")


class _SapCircAgeMultiplier_Type(Integer32):
    """Custom type sapCircAgeMultiplier based on Integer32"""
    defaultValue = 4


_SapCircAgeMultiplier_Object = MibTableColumn
sapCircAgeMultiplier = _SapCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 5),
    _SapCircAgeMultiplier_Type()
)
sapCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircAgeMultiplier.setStatus("mandatory")


class _SapCircGetNearestServerReply_Type(Integer32):
    """Custom type sapCircGetNearestServerReply based on Integer32"""
    defaultValue = 2

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


_SapCircGetNearestServerReply_Type.__name__ = "Integer32"
_SapCircGetNearestServerReply_Object = MibTableColumn
sapCircGetNearestServerReply = _SapCircGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 6),
    _SapCircGetNearestServerReply_Type()
)
sapCircGetNearestServerReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircGetNearestServerReply.setStatus("mandatory")
_SapCircOutPackets_Type = Counter32
_SapCircOutPackets_Object = MibTableColumn
sapCircOutPackets = _SapCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 7),
    _SapCircOutPackets_Type()
)
sapCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCircOutPackets.setStatus("mandatory")
_SapCircInPackets_Type = Counter32
_SapCircInPackets_Object = MibTableColumn
sapCircInPackets = _SapCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 8),
    _SapCircInPackets_Type()
)
sapCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCircInPackets.setStatus("mandatory")
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
    (0, "RND-MIB", "rndFACSActType"),
    (0, "RND-MIB", "rndFACSActIfIndex"),
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
    (0, "RND-MIB", "rndFACSIfIndex"),
    (0, "RND-MIB", "rndFACSProtocolType"),
    (0, "RND-MIB", "rndFACSType"),
    (0, "RND-MIB", "rndFACSIndex"),
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
    (0, "RND-MIB", "rsIpAdEntAddr"),
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
_RsIpAdEntBackupAddr_Type = IpAddress
_RsIpAdEntBackupAddr_Object = MibTableColumn
rsIpAdEntBackupAddr = _RsIpAdEntBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 1, 1, 5),
    _RsIpAdEntBackupAddr_Type()
)
rsIpAdEntBackupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpAdEntBackupAddr.setStatus("mandatory")


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
    (0, "RND-MIB", "rsIcmpRdIpAddr"),
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
    (0, "RND-MIB", "rsRip2IfConfAddress"),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
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
    (0, "RND-MIB", "ipRedundRoutersIfAddr"),
    (0, "RND-MIB", "ipRedundRoutersMainRouterAddr"),
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
    (0, "RND-MIB", "rsIpRipFilterGlbType"),
    (0, "RND-MIB", "rsIpRipFilterGlbNumber"),
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
    (0, "RND-MIB", "rsIpRipFilterLclIpIntf"),
    (0, "RND-MIB", "rsIpRipFilterLclType"),
    (0, "RND-MIB", "rsIpRipFilterLclNumber"),
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
    (0, "RND-MIB", "vlIfIndex"),
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
    (0, "RND-MIB", "vLIfIndex"),
    (0, "RND-MIB", "vLPortIfIndex"),
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
    (0, "RND-MIB", "vlAutoConfPortIfIndex"),
    (0, "RND-MIB", "vlAutoConfProto"),
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
    (0, "RND-MIB", "rsIfConfIndex"),
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
    (0, "RND-MIB", "eventNum"),
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
    (0, "RND-MIB", "reaBrgFftEntryNum"),
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
    (0, "RND-MIB", "reaIpFftEntryNum"),
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
    (0, "RND-MIB", "reaIpxFftEntryNum"),
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
    (0, "RND-MIB", "lreVnRespVn"),
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
_RndApplications_ObjectIdentity = ObjectIdentity
rndApplications = _RndApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35)
)
_RsServerDispatcher_ObjectIdentity = ObjectIdentity
rsServerDispatcher = _RsServerDispatcher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1)
)
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
    (0, "RND-MIB", "rndMonitoredElementAddress"),
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
    (0, "RND-MIB", "rndMonitoredElement"),
    (0, "RND-MIB", "rndMonitoredObjectInstanceLabel"),
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
    (0, "RND-MIB", "rndMibFileIndex"),
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
    (1, "RND-MIB", "rndRowStatusVariableName"),
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
    (0, "RND-MIB", "rsIpZhrStatusIpIntf"),
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
    (0, "RND-MIB", "rsIpZhrVirtAddressIpIntf"),
    (0, "RND-MIB", "rsIpZhrVirtAddressTo"),
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
    (0, "RND-MIB", "rsIpZhrConnectionIpIntf"),
    (0, "RND-MIB", "rsIpZhrConnectionSrcIp"),
    (0, "RND-MIB", "rsIpZhrConnectionDestIp"),
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
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    routeTableOverflow.setStatus(
        ""
    )

resetRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 10)
)
resetRequired.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    resetRequired.setStatus(
        ""
    )

endTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 12)
)
endTftp.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    endTftp.setStatus(
        ""
    )

abortTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 13)
)
abortTftp.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    abortTftp.setStatus(
        ""
    )

startTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 14)
)
startTftp.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    startTftp.setStatus(
        ""
    )

ipxRipTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 36)
)
ipxRipTblOverflow.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxRipTblOverflow.setStatus(
        ""
    )

ipxSapTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 37)
)
ipxSapTblOverflow.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxSapTblOverflow.setStatus(
        ""
    )

facsAccessVoilation = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 49)
)
facsAccessVoilation.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    facsAccessVoilation.setStatus(
        ""
    )

autoConfigurationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 50)
)
autoConfigurationCompleted.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    autoConfigurationCompleted.setStatus(
        ""
    )

forwardingTabOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 51)
)
forwardingTabOverflow.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    forwardingTabOverflow.setStatus(
        ""
    )

errorsDuringInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 61)
)
errorsDuringInit.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    errorsDuringInit.setStatus(
        ""
    )

vlanDynPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 66)
)
vlanDynPortAdded.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortAdded.setStatus(
        ""
    )

vlanDynPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 67)
)
vlanDynPortRemoved.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortRemoved.setStatus(
        ""
    )

rsSDclientsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 68)
)
rsSDclientsTableOverflow.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDclientsTableOverflow.setStatus(
        ""
    )

rsSDinactiveServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 69)
)
rsSDinactiveServer.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDinactiveServer.setStatus(
        ""
    )

rsIpZhrConnectionsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 70)
)
rsIpZhrConnectionsTableOverflow.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionsTableOverflow.setStatus(
        ""
    )

rsIpZhrReqStaticConnNotAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 71)
)
rsIpZhrReqStaticConnNotAccepted.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrReqStaticConnNotAccepted.setStatus(
        ""
    )

rsIpZhrVirtualIpAsSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 72)
)
rsIpZhrVirtualIpAsSource.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrVirtualIpAsSource.setStatus(
        ""
    )

rsIpZhrNotAllocVirtualIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 73)
)
rsIpZhrNotAllocVirtualIp.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrNotAllocVirtualIp.setStatus(
        ""
    )

rsSnmpSetRequestInSpecialCfgState = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 74)
)
rsSnmpSetRequestInSpecialCfgState.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSnmpSetRequestInSpecialCfgState.setStatus(
        ""
    )

rsWSDRedundancySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 141)
)
rsWSDRedundancySwitch.setObjects(
      *(("RND-MIB", "rndErrorDesc"),
        ("RND-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDRedundancySwitch.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RND-MIB",
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
       "rndIPXdriver": rndIPXdriver,
       "rndIPXRip": rndIPXRip,
       "rndIPXRipFilterGlbTable": rndIPXRipFilterGlbTable,
       "rndIPXRipFilterGlbEntry": rndIPXRipFilterGlbEntry,
       "rndIPXRipFilterGlbFLtype": rndIPXRipFilterGlbFLtype,
       "rndIPXRipFilterGlbFLnumber": rndIPXRipFilterGlbFLnumber,
       "rndIPXRipFilterGlbFLStatus": rndIPXRipFilterGlbFLStatus,
       "rndIPXRipFilterGlbFLnetworkPatern": rndIPXRipFilterGlbFLnetworkPatern,
       "rndIPXRipFilterGlbFLnetworkMask": rndIPXRipFilterGlbFLnetworkMask,
       "rndIPXRipFilterGlbFLaction": rndIPXRipFilterGlbFLaction,
       "rndIPXRipFilterCircuitTable": rndIPXRipFilterCircuitTable,
       "rndIPXRipFilterCircuitEntry": rndIPXRipFilterCircuitEntry,
       "rndIPXRipFilterCircFLIfIndex": rndIPXRipFilterCircFLIfIndex,
       "rndIPXRipFilterCircFLType": rndIPXRipFilterCircFLType,
       "rndIPXRipFilterCircFLnumber": rndIPXRipFilterCircFLnumber,
       "rndIPXRipFilterCircFLStatus": rndIPXRipFilterCircFLStatus,
       "rndIPXRipFilterCircFLnetworkPatern": rndIPXRipFilterCircFLnetworkPatern,
       "rndIPXRipFilterCircFLnetworkMask": rndIPXRipFilterCircFLnetworkMask,
       "rndIPXRipFilterCircFLaction": rndIPXRipFilterCircFLaction,
       "rndIPXSap": rndIPXSap,
       "rndIPXSapFilterGlbTable": rndIPXSapFilterGlbTable,
       "rndIPXSapFilterGlbEntry": rndIPXSapFilterGlbEntry,
       "rndIPXSapFilterGlbFLtype": rndIPXSapFilterGlbFLtype,
       "rndIPXSapFilterGlbFLnumber": rndIPXSapFilterGlbFLnumber,
       "rndIPXSapFilterGlbFLStatus": rndIPXSapFilterGlbFLStatus,
       "rndIPXSapFilterGlbFLnetworkPatern": rndIPXSapFilterGlbFLnetworkPatern,
       "rndIPXSapFilterGlbFLnetworkMask": rndIPXSapFilterGlbFLnetworkMask,
       "rndIPXSapFilterGlbFLserviceType": rndIPXSapFilterGlbFLserviceType,
       "rndIPXSapFilterGlbFLserviceName": rndIPXSapFilterGlbFLserviceName,
       "rndIPXSapFilterGlbFLaction": rndIPXSapFilterGlbFLaction,
       "rndIPXSapFilterCircuitTable": rndIPXSapFilterCircuitTable,
       "rndIPXSapFilterCircuitEntry": rndIPXSapFilterCircuitEntry,
       "rndIPXSapFilterCircFLIfIndex": rndIPXSapFilterCircFLIfIndex,
       "rndIPXSapFilterCircFLtype": rndIPXSapFilterCircFLtype,
       "rndIPXSapFilterCircFLnumber": rndIPXSapFilterCircFLnumber,
       "rndIPXSapFilterCircFLStatus": rndIPXSapFilterCircFLStatus,
       "rndIPXSapFilterCircFLnetworkPatern": rndIPXSapFilterCircFLnetworkPatern,
       "rndIPXSapFilterCircFLnetworkMask": rndIPXSapFilterCircFLnetworkMask,
       "rndIPXSapFilterCircFLserviceType": rndIPXSapFilterCircFLserviceType,
       "rndIPXSapFilterCircFLserviceName": rndIPXSapFilterCircFLserviceName,
       "rndIPXSapFilterCircFLaction": rndIPXSapFilterCircFLaction,
       "ipxSystem": ipxSystem,
       "ipxBasicSysTable": ipxBasicSysTable,
       "ipxBasicSysEntry": ipxBasicSysEntry,
       "ipxBasicSysInstance": ipxBasicSysInstance,
       "ipxBasicSysExistState": ipxBasicSysExistState,
       "ipxBasicSysInReceives": ipxBasicSysInReceives,
       "ipxBasicSysInHdrErrors": ipxBasicSysInHdrErrors,
       "ipxBasicSysInUnknownSockets": ipxBasicSysInUnknownSockets,
       "ipxBasicSysInDiscards": ipxBasicSysInDiscards,
       "ipxBasicSysInDelivers": ipxBasicSysInDelivers,
       "ipxBasicSysNoRoutes": ipxBasicSysNoRoutes,
       "ipxBasicSysOutRequests": ipxBasicSysOutRequests,
       "ipxBasicSysOutMalformedRequests": ipxBasicSysOutMalformedRequests,
       "ipxBasicSysOutDiscards": ipxBasicSysOutDiscards,
       "ipxBasicSysOutPackets": ipxBasicSysOutPackets,
       "ipxCircuit": ipxCircuit,
       "ipxCircTable": ipxCircTable,
       "ipxCircEntry": ipxCircEntry,
       "ipxCircSysInstance": ipxCircSysInstance,
       "ipxCircIndex": ipxCircIndex,
       "ipxCircExistState": ipxCircExistState,
       "ipxCircOperState": ipxCircOperState,
       "ipxCircIfIndex": ipxCircIfIndex,
       "ipxCircNetNumber": ipxCircNetNumber,
       "ipxCircTimeToNet": ipxCircTimeToNet,
       "ipxCircEncaps": ipxCircEncaps,
       "ipxCircNetbiosDeliver": ipxCircNetbiosDeliver,
       "ipxForwarding": ipxForwarding,
       "ipxDestTable": ipxDestTable,
       "ipxDestEntry": ipxDestEntry,
       "ipxDestSysInstance": ipxDestSysInstance,
       "ipxDestNetNum": ipxDestNetNum,
       "ipxDestNextHopCircIndex": ipxDestNextHopCircIndex,
       "ipxDestProtocol": ipxDestProtocol,
       "ipxDestTicks": ipxDestTicks,
       "ipxDestHopCount": ipxDestHopCount,
       "ipxDestNextHopNICAddress": ipxDestNextHopNICAddress,
       "ipxDestNextHopNetNum": ipxDestNextHopNetNum,
       "ipxDestExistState": ipxDestExistState,
       "ipxServices": ipxServices,
       "ipxServTable": ipxServTable,
       "ipxServEntry": ipxServEntry,
       "ipxServSysInstance": ipxServSysInstance,
       "ipxServType": ipxServType,
       "ipxServName": ipxServName,
       "ipxServProtocol": ipxServProtocol,
       "ipxServNetNum": ipxServNetNum,
       "ipxServNode": ipxServNode,
       "ipxServSocket": ipxServSocket,
       "ipxServHopCount": ipxServHopCount,
       "ipxServExistState": ipxServExistState,
       "ripsap": ripsap,
       "ripsapSystem": ripsapSystem,
       "ripSysTable": ripSysTable,
       "ripSysEntry": ripSysEntry,
       "ripSysInstance": ripSysInstance,
       "ripSysState": ripSysState,
       "ripSysIncorrectPackets": ripSysIncorrectPackets,
       "sapSysTable": sapSysTable,
       "sapSysEntry": sapSysEntry,
       "sapSysInstance": sapSysInstance,
       "sapSysState": sapSysState,
       "sapSysIncorrectPackets": sapSysIncorrectPackets,
       "ripsapCircuit": ripsapCircuit,
       "ripCircTable": ripCircTable,
       "ripCircEntry": ripCircEntry,
       "ripCircSysInstance": ripCircSysInstance,
       "ripCircIndex": ripCircIndex,
       "ripCircState": ripCircState,
       "ripCircUpdate": ripCircUpdate,
       "ripCircAgeMultiplier": ripCircAgeMultiplier,
       "ripCircOutPackets": ripCircOutPackets,
       "ripCircInPackets": ripCircInPackets,
       "sapCircTable": sapCircTable,
       "sapCircEntry": sapCircEntry,
       "sapCircSysInstance": sapCircSysInstance,
       "sapCircIndex": sapCircIndex,
       "sapCircState": sapCircState,
       "sapCircUpdate": sapCircUpdate,
       "sapCircAgeMultiplier": sapCircAgeMultiplier,
       "sapCircGetNearestServerReply": sapCircGetNearestServerReply,
       "sapCircOutPackets": sapCircOutPackets,
       "sapCircInPackets": sapCircInPackets,
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
       "rsIpAdEntBackupAddr": rsIpAdEntBackupAddr,
       "rsIpAdEntStatus": rsIpAdEntStatus,
       "rsIpAdEntBcastAddr": rsIpAdEntBcastAddr,
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
       "rndApplications": rndApplications,
       "rsServerDispatcher": rsServerDispatcher,
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
