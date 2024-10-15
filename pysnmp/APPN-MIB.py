# SNMP MIB module (APPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:53 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(snanauMIB,) = mibBuilder.importSymbols(
    "SNA-NAU-MIB",
    "snanauMIB")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DateAndTime,
 DisplayString,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

appnMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4)
)
appnMIB.setRevisions(
        ("1998-07-15 18:00",
         "1998-05-26 18:00",
         "1997-07-31 18:00",
         "1997-03-31 18:00",
         "1997-03-20 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnaNodeIdentification(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class SnaControlPointName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )



class SnaClassOfServiceName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class SnaModeName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class SnaSenseData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class DisplayableDlcAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class AppnNodeCounter(Counter32, TextualConvention):
    status = "current"


class AppnPortCounter(Counter32, TextualConvention):
    status = "current"


class AppnLinkStationCounter(Counter32, TextualConvention):
    status = "current"


class AppnTopologyEntryTimeLeft(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class AppnTgDlcData(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class AppnTgEffectiveCapacity(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class AppnTgSecurity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )



class AppnTgDelay(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



# MIB Managed Objects in the order of their OIDs

_AppnObjects_ObjectIdentity = ObjectIdentity
appnObjects = _AppnObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1)
)
_AppnNode_ObjectIdentity = ObjectIdentity
appnNode = _AppnNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1)
)
_AppnGeneralInfoAndCaps_ObjectIdentity = ObjectIdentity
appnGeneralInfoAndCaps = _AppnGeneralInfoAndCaps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1)
)
_AppnNodeCpName_Type = SnaControlPointName
_AppnNodeCpName_Object = MibScalar
appnNodeCpName = _AppnNodeCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 1),
    _AppnNodeCpName_Type()
)
appnNodeCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeCpName.setStatus("current")


class _AppnNodeMibVersion_Type(DisplayString):
    """Custom type appnNodeMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_AppnNodeMibVersion_Type.__name__ = "DisplayString"
_AppnNodeMibVersion_Object = MibScalar
appnNodeMibVersion = _AppnNodeMibVersion_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 2),
    _AppnNodeMibVersion_Type()
)
appnNodeMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeMibVersion.setStatus("deprecated")
_AppnNodeId_Type = SnaNodeIdentification
_AppnNodeId_Object = MibScalar
appnNodeId = _AppnNodeId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 3),
    _AppnNodeId_Type()
)
appnNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeId.setStatus("current")


class _AppnNodeType_Type(Integer32):
    """Custom type appnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endNode", 2),
          ("networkNode", 1),
          ("t21len", 4))
    )


_AppnNodeType_Type.__name__ = "Integer32"
_AppnNodeType_Object = MibScalar
appnNodeType = _AppnNodeType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 4),
    _AppnNodeType_Type()
)
appnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeType.setStatus("current")
_AppnNodeUpTime_Type = TimeTicks
_AppnNodeUpTime_Object = MibScalar
appnNodeUpTime = _AppnNodeUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 5),
    _AppnNodeUpTime_Type()
)
appnNodeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeUpTime.setStatus("current")
if mibBuilder.loadTexts:
    appnNodeUpTime.setUnits("hundredths of a second")
_AppnNodeParallelTg_Type = TruthValue
_AppnNodeParallelTg_Object = MibScalar
appnNodeParallelTg = _AppnNodeParallelTg_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 6),
    _AppnNodeParallelTg_Type()
)
appnNodeParallelTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeParallelTg.setStatus("current")
_AppnNodeAdaptiveBindPacing_Type = TruthValue
_AppnNodeAdaptiveBindPacing_Object = MibScalar
appnNodeAdaptiveBindPacing = _AppnNodeAdaptiveBindPacing_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 7),
    _AppnNodeAdaptiveBindPacing_Type()
)
appnNodeAdaptiveBindPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeAdaptiveBindPacing.setStatus("current")


class _AppnNodeHprSupport_Type(Integer32):
    """Custom type appnNodeHprSupport based on Integer32"""
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
        *(("controlFlowsOverRtpTower", 4),
          ("hprBaseOnly", 2),
          ("noHprSupport", 1),
          ("rtpTower", 3))
    )


_AppnNodeHprSupport_Type.__name__ = "Integer32"
_AppnNodeHprSupport_Object = MibScalar
appnNodeHprSupport = _AppnNodeHprSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 8),
    _AppnNodeHprSupport_Type()
)
appnNodeHprSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeHprSupport.setStatus("current")
_AppnNodeMaxSessPerRtpConn_Type = Gauge32
_AppnNodeMaxSessPerRtpConn_Object = MibScalar
appnNodeMaxSessPerRtpConn = _AppnNodeMaxSessPerRtpConn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 9),
    _AppnNodeMaxSessPerRtpConn_Type()
)
appnNodeMaxSessPerRtpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeMaxSessPerRtpConn.setStatus("current")
_AppnNodeHprIntRteSetups_Type = AppnNodeCounter
_AppnNodeHprIntRteSetups_Object = MibScalar
appnNodeHprIntRteSetups = _AppnNodeHprIntRteSetups_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 10),
    _AppnNodeHprIntRteSetups_Type()
)
appnNodeHprIntRteSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeHprIntRteSetups.setStatus("current")
_AppnNodeHprIntRteRejects_Type = AppnNodeCounter
_AppnNodeHprIntRteRejects_Object = MibScalar
appnNodeHprIntRteRejects = _AppnNodeHprIntRteRejects_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 11),
    _AppnNodeHprIntRteRejects_Type()
)
appnNodeHprIntRteRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeHprIntRteRejects.setStatus("current")
_AppnNodeHprOrgRteSetups_Type = AppnNodeCounter
_AppnNodeHprOrgRteSetups_Object = MibScalar
appnNodeHprOrgRteSetups = _AppnNodeHprOrgRteSetups_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 12),
    _AppnNodeHprOrgRteSetups_Type()
)
appnNodeHprOrgRteSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeHprOrgRteSetups.setStatus("current")
_AppnNodeHprOrgRteRejects_Type = AppnNodeCounter
_AppnNodeHprOrgRteRejects_Object = MibScalar
appnNodeHprOrgRteRejects = _AppnNodeHprOrgRteRejects_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 13),
    _AppnNodeHprOrgRteRejects_Type()
)
appnNodeHprOrgRteRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeHprOrgRteRejects.setStatus("current")
_AppnNodeHprEndRteSetups_Type = AppnNodeCounter
_AppnNodeHprEndRteSetups_Object = MibScalar
appnNodeHprEndRteSetups = _AppnNodeHprEndRteSetups_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 14),
    _AppnNodeHprEndRteSetups_Type()
)
appnNodeHprEndRteSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeHprEndRteSetups.setStatus("current")
_AppnNodeHprEndRteRejects_Type = AppnNodeCounter
_AppnNodeHprEndRteRejects_Object = MibScalar
appnNodeHprEndRteRejects = _AppnNodeHprEndRteRejects_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 15),
    _AppnNodeHprEndRteRejects_Type()
)
appnNodeHprEndRteRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeHprEndRteRejects.setStatus("current")
_AppnNodeCounterDisconTime_Type = TimeStamp
_AppnNodeCounterDisconTime_Object = MibScalar
appnNodeCounterDisconTime = _AppnNodeCounterDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 16),
    _AppnNodeCounterDisconTime_Type()
)
appnNodeCounterDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeCounterDisconTime.setStatus("current")


class _AppnNodeLsCounterType_Type(Integer32):
    """Custom type appnNodeLsCounterType based on Integer32"""
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
        *(("allAnr", 4),
          ("anrForLocalNces", 3),
          ("noAnr", 2),
          ("other", 1))
    )


_AppnNodeLsCounterType_Type.__name__ = "Integer32"
_AppnNodeLsCounterType_Object = MibScalar
appnNodeLsCounterType = _AppnNodeLsCounterType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 17),
    _AppnNodeLsCounterType_Type()
)
appnNodeLsCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeLsCounterType.setStatus("current")
_AppnNodeBrNn_Type = TruthValue
_AppnNodeBrNn_Object = MibScalar
appnNodeBrNn = _AppnNodeBrNn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 1, 18),
    _AppnNodeBrNn_Type()
)
appnNodeBrNn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeBrNn.setStatus("current")
_AppnNnUniqueInfoAndCaps_ObjectIdentity = ObjectIdentity
appnNnUniqueInfoAndCaps = _AppnNnUniqueInfoAndCaps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2)
)
_AppnNodeNnCentralDirectory_Type = TruthValue
_AppnNodeNnCentralDirectory_Object = MibScalar
appnNodeNnCentralDirectory = _AppnNodeNnCentralDirectory_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 1),
    _AppnNodeNnCentralDirectory_Type()
)
appnNodeNnCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnCentralDirectory.setStatus("current")


class _AppnNodeNnTreeCache_Type(Integer32):
    """Custom type appnNodeNnTreeCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cacheNoIncrUpdate", 2),
          ("cacheWithIncrUpdate", 3),
          ("noCache", 1))
    )


_AppnNodeNnTreeCache_Type.__name__ = "Integer32"
_AppnNodeNnTreeCache_Object = MibScalar
appnNodeNnTreeCache = _AppnNodeNnTreeCache_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 2),
    _AppnNodeNnTreeCache_Type()
)
appnNodeNnTreeCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnTreeCache.setStatus("current")


class _AppnNodeNnRouteAddResist_Type(Integer32):
    """Custom type appnNodeNnRouteAddResist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNodeNnRouteAddResist_Type.__name__ = "Integer32"
_AppnNodeNnRouteAddResist_Object = MibScalar
appnNodeNnRouteAddResist = _AppnNodeNnRouteAddResist_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 3),
    _AppnNodeNnRouteAddResist_Type()
)
appnNodeNnRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnRouteAddResist.setStatus("current")
_AppnNodeNnIsr_Type = TruthValue
_AppnNodeNnIsr_Object = MibScalar
appnNodeNnIsr = _AppnNodeNnIsr_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 4),
    _AppnNodeNnIsr_Type()
)
appnNodeNnIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnIsr.setStatus("current")
_AppnNodeNnFrsn_Type = Unsigned32
_AppnNodeNnFrsn_Object = MibScalar
appnNodeNnFrsn = _AppnNodeNnFrsn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 5),
    _AppnNodeNnFrsn_Type()
)
appnNodeNnFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnFrsn.setStatus("current")
_AppnNodeNnPeriBorderSup_Type = TruthValue
_AppnNodeNnPeriBorderSup_Object = MibScalar
appnNodeNnPeriBorderSup = _AppnNodeNnPeriBorderSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 6),
    _AppnNodeNnPeriBorderSup_Type()
)
appnNodeNnPeriBorderSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnPeriBorderSup.setStatus("current")
_AppnNodeNnInterchangeSup_Type = TruthValue
_AppnNodeNnInterchangeSup_Object = MibScalar
appnNodeNnInterchangeSup = _AppnNodeNnInterchangeSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 7),
    _AppnNodeNnInterchangeSup_Type()
)
appnNodeNnInterchangeSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnInterchangeSup.setStatus("current")
_AppnNodeNnExteBorderSup_Type = TruthValue
_AppnNodeNnExteBorderSup_Object = MibScalar
appnNodeNnExteBorderSup = _AppnNodeNnExteBorderSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 8),
    _AppnNodeNnExteBorderSup_Type()
)
appnNodeNnExteBorderSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnExteBorderSup.setStatus("current")


class _AppnNodeNnSafeStoreFreq_Type(Integer32):
    """Custom type appnNodeNnSafeStoreFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AppnNodeNnSafeStoreFreq_Type.__name__ = "Integer32"
_AppnNodeNnSafeStoreFreq_Object = MibScalar
appnNodeNnSafeStoreFreq = _AppnNodeNnSafeStoreFreq_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 9),
    _AppnNodeNnSafeStoreFreq_Type()
)
appnNodeNnSafeStoreFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnNodeNnSafeStoreFreq.setStatus("current")
if mibBuilder.loadTexts:
    appnNodeNnSafeStoreFreq.setUnits("TDUs")
_AppnNodeNnRsn_Type = Unsigned32
_AppnNodeNnRsn_Object = MibScalar
appnNodeNnRsn = _AppnNodeNnRsn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 10),
    _AppnNodeNnRsn_Type()
)
appnNodeNnRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnRsn.setStatus("current")
_AppnNodeNnCongested_Type = TruthValue
_AppnNodeNnCongested_Object = MibScalar
appnNodeNnCongested = _AppnNodeNnCongested_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 11),
    _AppnNodeNnCongested_Type()
)
appnNodeNnCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnCongested.setStatus("current")
_AppnNodeNnIsrDepleted_Type = TruthValue
_AppnNodeNnIsrDepleted_Object = MibScalar
appnNodeNnIsrDepleted = _AppnNodeNnIsrDepleted_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 12),
    _AppnNodeNnIsrDepleted_Type()
)
appnNodeNnIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnIsrDepleted.setStatus("current")
_AppnNodeNnQuiescing_Type = TruthValue
_AppnNodeNnQuiescing_Object = MibScalar
appnNodeNnQuiescing = _AppnNodeNnQuiescing_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 13),
    _AppnNodeNnQuiescing_Type()
)
appnNodeNnQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnQuiescing.setStatus("current")
_AppnNodeNnGateway_Type = TruthValue
_AppnNodeNnGateway_Object = MibScalar
appnNodeNnGateway = _AppnNodeNnGateway_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 2, 14),
    _AppnNodeNnGateway_Type()
)
appnNodeNnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeNnGateway.setStatus("current")
_AppnEnUniqueCaps_ObjectIdentity = ObjectIdentity
appnEnUniqueCaps = _AppnEnUniqueCaps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 3)
)
_AppnNodeEnModeCosMap_Type = TruthValue
_AppnNodeEnModeCosMap_Object = MibScalar
appnNodeEnModeCosMap = _AppnNodeEnModeCosMap_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 3, 1),
    _AppnNodeEnModeCosMap_Type()
)
appnNodeEnModeCosMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeEnModeCosMap.setStatus("current")


class _AppnNodeEnNnServer_Type(OctetString):
    """Custom type appnNodeEnNnServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_AppnNodeEnNnServer_Type.__name__ = "OctetString"
_AppnNodeEnNnServer_Object = MibScalar
appnNodeEnNnServer = _AppnNodeEnNnServer_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 3, 2),
    _AppnNodeEnNnServer_Type()
)
appnNodeEnNnServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeEnNnServer.setStatus("current")
_AppnNodeEnLuSearch_Type = TruthValue
_AppnNodeEnLuSearch_Object = MibScalar
appnNodeEnLuSearch = _AppnNodeEnLuSearch_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 3, 3),
    _AppnNodeEnLuSearch_Type()
)
appnNodeEnLuSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNodeEnLuSearch.setStatus("current")
_AppnPortInformation_ObjectIdentity = ObjectIdentity
appnPortInformation = _AppnPortInformation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4)
)
_AppnPortTable_Object = MibTable
appnPortTable = _AppnPortTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    appnPortTable.setStatus("current")
_AppnPortEntry_Object = MibTableRow
appnPortEntry = _AppnPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1)
)
appnPortEntry.setIndexNames(
    (0, "APPN-MIB", "appnPortName"),
)
if mibBuilder.loadTexts:
    appnPortEntry.setStatus("current")


class _AppnPortName_Type(DisplayString):
    """Custom type appnPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AppnPortName_Type.__name__ = "DisplayString"
_AppnPortName_Object = MibTableColumn
appnPortName = _AppnPortName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 1),
    _AppnPortName_Type()
)
appnPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnPortName.setStatus("current")


class _AppnPortCommand_Type(Integer32):
    """Custom type appnPortCommand based on Integer32"""
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
        *(("activate", 2),
          ("deactivate", 1),
          ("ready", 4),
          ("recycle", 3))
    )


_AppnPortCommand_Type.__name__ = "Integer32"
_AppnPortCommand_Object = MibTableColumn
appnPortCommand = _AppnPortCommand_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 2),
    _AppnPortCommand_Type()
)
appnPortCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnPortCommand.setStatus("current")


class _AppnPortOperState_Type(Integer32):
    """Custom type appnPortOperState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_AppnPortOperState_Type.__name__ = "Integer32"
_AppnPortOperState_Object = MibTableColumn
appnPortOperState = _AppnPortOperState_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 3),
    _AppnPortOperState_Type()
)
appnPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortOperState.setStatus("current")
_AppnPortDlcType_Type = IANAifType
_AppnPortDlcType_Object = MibTableColumn
appnPortDlcType = _AppnPortDlcType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 4),
    _AppnPortDlcType_Type()
)
appnPortDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDlcType.setStatus("current")


class _AppnPortPortType_Type(Integer32):
    """Custom type appnPortPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("sharedAccessFacilities", 3),
          ("switched", 2))
    )


_AppnPortPortType_Type.__name__ = "Integer32"
_AppnPortPortType_Object = MibTableColumn
appnPortPortType = _AppnPortPortType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 5),
    _AppnPortPortType_Type()
)
appnPortPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortPortType.setStatus("current")
_AppnPortSIMRIM_Type = TruthValue
_AppnPortSIMRIM_Object = MibTableColumn
appnPortSIMRIM = _AppnPortSIMRIM_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 6),
    _AppnPortSIMRIM_Type()
)
appnPortSIMRIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortSIMRIM.setStatus("current")


class _AppnPortLsRole_Type(Integer32):
    """Custom type appnPortLsRole based on Integer32"""
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
        *(("abm", 4),
          ("negotiable", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_AppnPortLsRole_Type.__name__ = "Integer32"
_AppnPortLsRole_Object = MibTableColumn
appnPortLsRole = _AppnPortLsRole_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 7),
    _AppnPortLsRole_Type()
)
appnPortLsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortLsRole.setStatus("current")
_AppnPortNegotLs_Type = TruthValue
_AppnPortNegotLs_Object = MibTableColumn
appnPortNegotLs = _AppnPortNegotLs_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 8),
    _AppnPortNegotLs_Type()
)
appnPortNegotLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortNegotLs.setStatus("current")
_AppnPortDynamicLinkSupport_Type = TruthValue
_AppnPortDynamicLinkSupport_Object = MibTableColumn
appnPortDynamicLinkSupport = _AppnPortDynamicLinkSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 9),
    _AppnPortDynamicLinkSupport_Type()
)
appnPortDynamicLinkSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDynamicLinkSupport.setStatus("current")


class _AppnPortMaxRcvBtuSize_Type(Integer32):
    """Custom type appnPortMaxRcvBtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32767),
    )


_AppnPortMaxRcvBtuSize_Type.__name__ = "Integer32"
_AppnPortMaxRcvBtuSize_Object = MibTableColumn
appnPortMaxRcvBtuSize = _AppnPortMaxRcvBtuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 10),
    _AppnPortMaxRcvBtuSize_Type()
)
appnPortMaxRcvBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortMaxRcvBtuSize.setStatus("current")
if mibBuilder.loadTexts:
    appnPortMaxRcvBtuSize.setUnits("bytes")
_AppnPortMaxIframeWindow_Type = Gauge32
_AppnPortMaxIframeWindow_Object = MibTableColumn
appnPortMaxIframeWindow = _AppnPortMaxIframeWindow_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 11),
    _AppnPortMaxIframeWindow_Type()
)
appnPortMaxIframeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortMaxIframeWindow.setStatus("current")
if mibBuilder.loadTexts:
    appnPortMaxIframeWindow.setUnits("I-frames")
_AppnPortDefLsGoodXids_Type = AppnPortCounter
_AppnPortDefLsGoodXids_Object = MibTableColumn
appnPortDefLsGoodXids = _AppnPortDefLsGoodXids_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 12),
    _AppnPortDefLsGoodXids_Type()
)
appnPortDefLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDefLsGoodXids.setStatus("current")
if mibBuilder.loadTexts:
    appnPortDefLsGoodXids.setUnits("XID exchanges")
_AppnPortDefLsBadXids_Type = AppnPortCounter
_AppnPortDefLsBadXids_Object = MibTableColumn
appnPortDefLsBadXids = _AppnPortDefLsBadXids_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 13),
    _AppnPortDefLsBadXids_Type()
)
appnPortDefLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDefLsBadXids.setStatus("current")
if mibBuilder.loadTexts:
    appnPortDefLsBadXids.setUnits("XID exchanges")
_AppnPortDynLsGoodXids_Type = AppnPortCounter
_AppnPortDynLsGoodXids_Object = MibTableColumn
appnPortDynLsGoodXids = _AppnPortDynLsGoodXids_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 14),
    _AppnPortDynLsGoodXids_Type()
)
appnPortDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDynLsGoodXids.setStatus("current")
if mibBuilder.loadTexts:
    appnPortDynLsGoodXids.setUnits("XID exchanges")
_AppnPortDynLsBadXids_Type = AppnPortCounter
_AppnPortDynLsBadXids_Object = MibTableColumn
appnPortDynLsBadXids = _AppnPortDynLsBadXids_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 15),
    _AppnPortDynLsBadXids_Type()
)
appnPortDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDynLsBadXids.setStatus("current")
if mibBuilder.loadTexts:
    appnPortDynLsBadXids.setUnits("XID exchanges")
_AppnPortSpecific_Type = RowPointer
_AppnPortSpecific_Object = MibTableColumn
appnPortSpecific = _AppnPortSpecific_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 16),
    _AppnPortSpecific_Type()
)
appnPortSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortSpecific.setStatus("current")
_AppnPortDlcLocalAddr_Type = DisplayableDlcAddress
_AppnPortDlcLocalAddr_Object = MibTableColumn
appnPortDlcLocalAddr = _AppnPortDlcLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 17),
    _AppnPortDlcLocalAddr_Type()
)
appnPortDlcLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortDlcLocalAddr.setStatus("current")
_AppnPortCounterDisconTime_Type = TimeStamp
_AppnPortCounterDisconTime_Object = MibTableColumn
appnPortCounterDisconTime = _AppnPortCounterDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 4, 1, 1, 18),
    _AppnPortCounterDisconTime_Type()
)
appnPortCounterDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnPortCounterDisconTime.setStatus("current")
_AppnLinkStationInformation_ObjectIdentity = ObjectIdentity
appnLinkStationInformation = _AppnLinkStationInformation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5)
)
_AppnLsTable_Object = MibTable
appnLsTable = _AppnLsTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    appnLsTable.setStatus("current")
_AppnLsEntry_Object = MibTableRow
appnLsEntry = _AppnLsEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1)
)
appnLsEntry.setIndexNames(
    (0, "APPN-MIB", "appnLsName"),
)
if mibBuilder.loadTexts:
    appnLsEntry.setStatus("current")


class _AppnLsName_Type(DisplayString):
    """Custom type appnLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AppnLsName_Type.__name__ = "DisplayString"
_AppnLsName_Object = MibTableColumn
appnLsName = _AppnLsName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 1),
    _AppnLsName_Type()
)
appnLsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLsName.setStatus("current")


class _AppnLsCommand_Type(Integer32):
    """Custom type appnLsCommand based on Integer32"""
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
        *(("activate", 2),
          ("deactivate", 1),
          ("ready", 4),
          ("recycle", 3))
    )


_AppnLsCommand_Type.__name__ = "Integer32"
_AppnLsCommand_Object = MibTableColumn
appnLsCommand = _AppnLsCommand_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 2),
    _AppnLsCommand_Type()
)
appnLsCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnLsCommand.setStatus("current")


class _AppnLsOperState_Type(Integer32):
    """Custom type appnLsOperState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("active", 7),
          ("inactive", 1),
          ("otherPendingActive", 6),
          ("otherPendingInact", 11),
          ("pendXidExch", 3),
          ("sendActAs", 4),
          ("sendSetMode", 5),
          ("sentConnectOut", 2),
          ("sentDeactAsOrd", 8),
          ("sentDiscImmed", 10),
          ("sentDiscOrd", 9))
    )


_AppnLsOperState_Type.__name__ = "Integer32"
_AppnLsOperState_Object = MibTableColumn
appnLsOperState = _AppnLsOperState_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 3),
    _AppnLsOperState_Type()
)
appnLsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOperState.setStatus("current")


class _AppnLsPortName_Type(DisplayString):
    """Custom type appnLsPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AppnLsPortName_Type.__name__ = "DisplayString"
_AppnLsPortName_Object = MibTableColumn
appnLsPortName = _AppnLsPortName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 4),
    _AppnLsPortName_Type()
)
appnLsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsPortName.setStatus("current")
_AppnLsDlcType_Type = IANAifType
_AppnLsDlcType_Object = MibTableColumn
appnLsDlcType = _AppnLsDlcType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 5),
    _AppnLsDlcType_Type()
)
appnLsDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsDlcType.setStatus("current")
_AppnLsDynamic_Type = TruthValue
_AppnLsDynamic_Object = MibTableColumn
appnLsDynamic = _AppnLsDynamic_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 6),
    _AppnLsDynamic_Type()
)
appnLsDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsDynamic.setStatus("current")


class _AppnLsAdjCpName_Type(OctetString):
    """Custom type appnLsAdjCpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_AppnLsAdjCpName_Type.__name__ = "OctetString"
_AppnLsAdjCpName_Object = MibTableColumn
appnLsAdjCpName = _AppnLsAdjCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 7),
    _AppnLsAdjCpName_Type()
)
appnLsAdjCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsAdjCpName.setStatus("current")


class _AppnLsAdjNodeType_Type(Integer32):
    """Custom type appnLsAdjNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("endNode", 2),
          ("networkNode", 1),
          ("t21len", 4),
          ("unknown", 255))
    )


_AppnLsAdjNodeType_Type.__name__ = "Integer32"
_AppnLsAdjNodeType_Object = MibTableColumn
appnLsAdjNodeType = _AppnLsAdjNodeType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 8),
    _AppnLsAdjNodeType_Type()
)
appnLsAdjNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsAdjNodeType.setStatus("current")


class _AppnLsTgNum_Type(Integer32):
    """Custom type appnLsTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AppnLsTgNum_Type.__name__ = "Integer32"
_AppnLsTgNum_Object = MibTableColumn
appnLsTgNum = _AppnLsTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 9),
    _AppnLsTgNum_Type()
)
appnLsTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsTgNum.setStatus("current")
_AppnLsLimResource_Type = TruthValue
_AppnLsLimResource_Object = MibTableColumn
appnLsLimResource = _AppnLsLimResource_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 10),
    _AppnLsLimResource_Type()
)
appnLsLimResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsLimResource.setStatus("current")
_AppnLsActOnDemand_Type = TruthValue
_AppnLsActOnDemand_Object = MibTableColumn
appnLsActOnDemand = _AppnLsActOnDemand_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 11),
    _AppnLsActOnDemand_Type()
)
appnLsActOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsActOnDemand.setStatus("current")
_AppnLsMigration_Type = TruthValue
_AppnLsMigration_Object = MibTableColumn
appnLsMigration = _AppnLsMigration_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 12),
    _AppnLsMigration_Type()
)
appnLsMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMigration.setStatus("current")
_AppnLsPartnerNodeId_Type = SnaNodeIdentification
_AppnLsPartnerNodeId_Object = MibTableColumn
appnLsPartnerNodeId = _AppnLsPartnerNodeId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 13),
    _AppnLsPartnerNodeId_Type()
)
appnLsPartnerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsPartnerNodeId.setStatus("current")
_AppnLsCpCpSessionSupport_Type = TruthValue
_AppnLsCpCpSessionSupport_Object = MibTableColumn
appnLsCpCpSessionSupport = _AppnLsCpCpSessionSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 14),
    _AppnLsCpCpSessionSupport_Type()
)
appnLsCpCpSessionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsCpCpSessionSupport.setStatus("current")


class _AppnLsMaxSendBtuSize_Type(Integer32):
    """Custom type appnLsMaxSendBtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32767),
    )


_AppnLsMaxSendBtuSize_Type.__name__ = "Integer32"
_AppnLsMaxSendBtuSize_Object = MibTableColumn
appnLsMaxSendBtuSize = _AppnLsMaxSendBtuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 15),
    _AppnLsMaxSendBtuSize_Type()
)
appnLsMaxSendBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMaxSendBtuSize.setStatus("current")
if mibBuilder.loadTexts:
    appnLsMaxSendBtuSize.setUnits("bytes")
_AppnLsInXidBytes_Type = AppnLinkStationCounter
_AppnLsInXidBytes_Object = MibTableColumn
appnLsInXidBytes = _AppnLsInXidBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 16),
    _AppnLsInXidBytes_Type()
)
appnLsInXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInXidBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnLsInXidBytes.setUnits("bytes")
_AppnLsInMsgBytes_Type = AppnLinkStationCounter
_AppnLsInMsgBytes_Object = MibTableColumn
appnLsInMsgBytes = _AppnLsInMsgBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 17),
    _AppnLsInMsgBytes_Type()
)
appnLsInMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInMsgBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnLsInMsgBytes.setUnits("bytes")
_AppnLsInXidFrames_Type = AppnLinkStationCounter
_AppnLsInXidFrames_Object = MibTableColumn
appnLsInXidFrames = _AppnLsInXidFrames_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 18),
    _AppnLsInXidFrames_Type()
)
appnLsInXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInXidFrames.setStatus("current")
if mibBuilder.loadTexts:
    appnLsInXidFrames.setUnits("XID frames")
_AppnLsInMsgFrames_Type = AppnLinkStationCounter
_AppnLsInMsgFrames_Object = MibTableColumn
appnLsInMsgFrames = _AppnLsInMsgFrames_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 19),
    _AppnLsInMsgFrames_Type()
)
appnLsInMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsInMsgFrames.setStatus("current")
if mibBuilder.loadTexts:
    appnLsInMsgFrames.setUnits("I-frames")
_AppnLsOutXidBytes_Type = AppnLinkStationCounter
_AppnLsOutXidBytes_Object = MibTableColumn
appnLsOutXidBytes = _AppnLsOutXidBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 20),
    _AppnLsOutXidBytes_Type()
)
appnLsOutXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutXidBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnLsOutXidBytes.setUnits("bytes")
_AppnLsOutMsgBytes_Type = AppnLinkStationCounter
_AppnLsOutMsgBytes_Object = MibTableColumn
appnLsOutMsgBytes = _AppnLsOutMsgBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 21),
    _AppnLsOutMsgBytes_Type()
)
appnLsOutMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutMsgBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnLsOutMsgBytes.setUnits("bytes")
_AppnLsOutXidFrames_Type = AppnLinkStationCounter
_AppnLsOutXidFrames_Object = MibTableColumn
appnLsOutXidFrames = _AppnLsOutXidFrames_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 22),
    _AppnLsOutXidFrames_Type()
)
appnLsOutXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutXidFrames.setStatus("current")
if mibBuilder.loadTexts:
    appnLsOutXidFrames.setUnits("XID frames")
_AppnLsOutMsgFrames_Type = AppnLinkStationCounter
_AppnLsOutMsgFrames_Object = MibTableColumn
appnLsOutMsgFrames = _AppnLsOutMsgFrames_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 23),
    _AppnLsOutMsgFrames_Type()
)
appnLsOutMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsOutMsgFrames.setStatus("current")
if mibBuilder.loadTexts:
    appnLsOutMsgFrames.setUnits("I-frames")
_AppnLsEchoRsps_Type = AppnLinkStationCounter
_AppnLsEchoRsps_Object = MibTableColumn
appnLsEchoRsps = _AppnLsEchoRsps_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 24),
    _AppnLsEchoRsps_Type()
)
appnLsEchoRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsEchoRsps.setStatus("current")
if mibBuilder.loadTexts:
    appnLsEchoRsps.setUnits("echo responses")
_AppnLsCurrentDelay_Type = Gauge32
_AppnLsCurrentDelay_Object = MibTableColumn
appnLsCurrentDelay = _AppnLsCurrentDelay_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 25),
    _AppnLsCurrentDelay_Type()
)
appnLsCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsCurrentDelay.setStatus("current")
if mibBuilder.loadTexts:
    appnLsCurrentDelay.setUnits("milliseconds")
_AppnLsMaxDelay_Type = Gauge32
_AppnLsMaxDelay_Object = MibTableColumn
appnLsMaxDelay = _AppnLsMaxDelay_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 26),
    _AppnLsMaxDelay_Type()
)
appnLsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    appnLsMaxDelay.setUnits("milliseconds")
_AppnLsMinDelay_Type = Gauge32
_AppnLsMinDelay_Object = MibTableColumn
appnLsMinDelay = _AppnLsMinDelay_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 27),
    _AppnLsMinDelay_Type()
)
appnLsMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    appnLsMinDelay.setUnits("milliseconds")
_AppnLsMaxDelayTime_Type = DateAndTime
_AppnLsMaxDelayTime_Object = MibTableColumn
appnLsMaxDelayTime = _AppnLsMaxDelayTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 28),
    _AppnLsMaxDelayTime_Type()
)
appnLsMaxDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMaxDelayTime.setStatus("current")
_AppnLsGoodXids_Type = AppnLinkStationCounter
_AppnLsGoodXids_Object = MibTableColumn
appnLsGoodXids = _AppnLsGoodXids_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 29),
    _AppnLsGoodXids_Type()
)
appnLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsGoodXids.setStatus("current")
if mibBuilder.loadTexts:
    appnLsGoodXids.setUnits("XID exchanges")
_AppnLsBadXids_Type = AppnLinkStationCounter
_AppnLsBadXids_Object = MibTableColumn
appnLsBadXids = _AppnLsBadXids_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 30),
    _AppnLsBadXids_Type()
)
appnLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsBadXids.setStatus("current")
if mibBuilder.loadTexts:
    appnLsBadXids.setUnits("XID exchanges")
_AppnLsSpecific_Type = RowPointer
_AppnLsSpecific_Object = MibTableColumn
appnLsSpecific = _AppnLsSpecific_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 31),
    _AppnLsSpecific_Type()
)
appnLsSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsSpecific.setStatus("current")
_AppnLsActiveTime_Type = Unsigned32
_AppnLsActiveTime_Object = MibTableColumn
appnLsActiveTime = _AppnLsActiveTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 32),
    _AppnLsActiveTime_Type()
)
appnLsActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    appnLsActiveTime.setUnits("hundredths of a second")
_AppnLsCurrentStateTime_Type = TimeTicks
_AppnLsCurrentStateTime_Object = MibTableColumn
appnLsCurrentStateTime = _AppnLsCurrentStateTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 33),
    _AppnLsCurrentStateTime_Type()
)
appnLsCurrentStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsCurrentStateTime.setStatus("current")
if mibBuilder.loadTexts:
    appnLsCurrentStateTime.setUnits("hundredths of a second")


class _AppnLsHprSup_Type(Integer32):
    """Custom type appnLsHprSup based on Integer32"""
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
        *(("controlFlowsOverRtpTower", 4),
          ("hprBaseOnly", 2),
          ("noHprSupport", 1),
          ("rtpTower", 3))
    )


_AppnLsHprSup_Type.__name__ = "Integer32"
_AppnLsHprSup_Object = MibTableColumn
appnLsHprSup = _AppnLsHprSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 34),
    _AppnLsHprSup_Type()
)
appnLsHprSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsHprSup.setStatus("current")
_AppnLsErrRecoSup_Type = TruthValue
_AppnLsErrRecoSup_Object = MibTableColumn
appnLsErrRecoSup = _AppnLsErrRecoSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 35),
    _AppnLsErrRecoSup_Type()
)
appnLsErrRecoSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsErrRecoSup.setStatus("current")


class _AppnLsForAnrLabel_Type(OctetString):
    """Custom type appnLsForAnrLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppnLsForAnrLabel_Type.__name__ = "OctetString"
_AppnLsForAnrLabel_Object = MibTableColumn
appnLsForAnrLabel = _AppnLsForAnrLabel_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 36),
    _AppnLsForAnrLabel_Type()
)
appnLsForAnrLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsForAnrLabel.setStatus("current")


class _AppnLsRevAnrLabel_Type(OctetString):
    """Custom type appnLsRevAnrLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppnLsRevAnrLabel_Type.__name__ = "OctetString"
_AppnLsRevAnrLabel_Object = MibTableColumn
appnLsRevAnrLabel = _AppnLsRevAnrLabel_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 37),
    _AppnLsRevAnrLabel_Type()
)
appnLsRevAnrLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsRevAnrLabel.setStatus("current")


class _AppnLsCpCpNceId_Type(OctetString):
    """Custom type appnLsCpCpNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppnLsCpCpNceId_Type.__name__ = "OctetString"
_AppnLsCpCpNceId_Object = MibTableColumn
appnLsCpCpNceId = _AppnLsCpCpNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 38),
    _AppnLsCpCpNceId_Type()
)
appnLsCpCpNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsCpCpNceId.setStatus("current")


class _AppnLsRouteNceId_Type(OctetString):
    """Custom type appnLsRouteNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppnLsRouteNceId_Type.__name__ = "OctetString"
_AppnLsRouteNceId_Object = MibTableColumn
appnLsRouteNceId = _AppnLsRouteNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 39),
    _AppnLsRouteNceId_Type()
)
appnLsRouteNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsRouteNceId.setStatus("current")


class _AppnLsBfNceId_Type(OctetString):
    """Custom type appnLsBfNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AppnLsBfNceId_Type.__name__ = "OctetString"
_AppnLsBfNceId_Object = MibTableColumn
appnLsBfNceId = _AppnLsBfNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 40),
    _AppnLsBfNceId_Type()
)
appnLsBfNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsBfNceId.setStatus("current")
_AppnLsLocalAddr_Type = DisplayableDlcAddress
_AppnLsLocalAddr_Object = MibTableColumn
appnLsLocalAddr = _AppnLsLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 41),
    _AppnLsLocalAddr_Type()
)
appnLsLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsLocalAddr.setStatus("current")
_AppnLsRemoteAddr_Type = DisplayableDlcAddress
_AppnLsRemoteAddr_Object = MibTableColumn
appnLsRemoteAddr = _AppnLsRemoteAddr_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 42),
    _AppnLsRemoteAddr_Type()
)
appnLsRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsRemoteAddr.setStatus("current")


class _AppnLsRemoteLsName_Type(DisplayString):
    """Custom type appnLsRemoteLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AppnLsRemoteLsName_Type.__name__ = "DisplayString"
_AppnLsRemoteLsName_Object = MibTableColumn
appnLsRemoteLsName = _AppnLsRemoteLsName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 43),
    _AppnLsRemoteLsName_Type()
)
appnLsRemoteLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsRemoteLsName.setStatus("current")
_AppnLsCounterDisconTime_Type = TimeStamp
_AppnLsCounterDisconTime_Object = MibTableColumn
appnLsCounterDisconTime = _AppnLsCounterDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 44),
    _AppnLsCounterDisconTime_Type()
)
appnLsCounterDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsCounterDisconTime.setStatus("current")
_AppnLsMltgMember_Type = TruthValue
_AppnLsMltgMember_Object = MibTableColumn
appnLsMltgMember = _AppnLsMltgMember_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 1, 1, 45),
    _AppnLsMltgMember_Type()
)
appnLsMltgMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsMltgMember.setStatus("current")
_AppnLsStatusTable_Object = MibTable
appnLsStatusTable = _AppnLsStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    appnLsStatusTable.setStatus("current")
_AppnLsStatusEntry_Object = MibTableRow
appnLsStatusEntry = _AppnLsStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1)
)
appnLsStatusEntry.setIndexNames(
    (0, "APPN-MIB", "appnLsStatusIndex"),
)
if mibBuilder.loadTexts:
    appnLsStatusEntry.setStatus("current")


class _AppnLsStatusIndex_Type(Integer32):
    """Custom type appnLsStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AppnLsStatusIndex_Type.__name__ = "Integer32"
_AppnLsStatusIndex_Object = MibTableColumn
appnLsStatusIndex = _AppnLsStatusIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 1),
    _AppnLsStatusIndex_Type()
)
appnLsStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLsStatusIndex.setStatus("current")
_AppnLsStatusTime_Type = DateAndTime
_AppnLsStatusTime_Object = MibTableColumn
appnLsStatusTime = _AppnLsStatusTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 2),
    _AppnLsStatusTime_Type()
)
appnLsStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusTime.setStatus("current")


class _AppnLsStatusLsName_Type(DisplayString):
    """Custom type appnLsStatusLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AppnLsStatusLsName_Type.__name__ = "DisplayString"
_AppnLsStatusLsName_Object = MibTableColumn
appnLsStatusLsName = _AppnLsStatusLsName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 3),
    _AppnLsStatusLsName_Type()
)
appnLsStatusLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusLsName.setStatus("current")


class _AppnLsStatusCpName_Type(DisplayString):
    """Custom type appnLsStatusCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_AppnLsStatusCpName_Type.__name__ = "DisplayString"
_AppnLsStatusCpName_Object = MibTableColumn
appnLsStatusCpName = _AppnLsStatusCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 4),
    _AppnLsStatusCpName_Type()
)
appnLsStatusCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusCpName.setStatus("current")
_AppnLsStatusPartnerId_Type = SnaNodeIdentification
_AppnLsStatusPartnerId_Object = MibTableColumn
appnLsStatusPartnerId = _AppnLsStatusPartnerId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 5),
    _AppnLsStatusPartnerId_Type()
)
appnLsStatusPartnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusPartnerId.setStatus("current")


class _AppnLsStatusTgNum_Type(Integer32):
    """Custom type appnLsStatusTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AppnLsStatusTgNum_Type.__name__ = "Integer32"
_AppnLsStatusTgNum_Object = MibTableColumn
appnLsStatusTgNum = _AppnLsStatusTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 6),
    _AppnLsStatusTgNum_Type()
)
appnLsStatusTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusTgNum.setStatus("current")
_AppnLsStatusGeneralSense_Type = SnaSenseData
_AppnLsStatusGeneralSense_Object = MibTableColumn
appnLsStatusGeneralSense = _AppnLsStatusGeneralSense_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 7),
    _AppnLsStatusGeneralSense_Type()
)
appnLsStatusGeneralSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusGeneralSense.setStatus("current")
_AppnLsStatusRetry_Type = TruthValue
_AppnLsStatusRetry_Object = MibTableColumn
appnLsStatusRetry = _AppnLsStatusRetry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 8),
    _AppnLsStatusRetry_Type()
)
appnLsStatusRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusRetry.setStatus("current")
_AppnLsStatusEndSense_Type = SnaSenseData
_AppnLsStatusEndSense_Object = MibTableColumn
appnLsStatusEndSense = _AppnLsStatusEndSense_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 9),
    _AppnLsStatusEndSense_Type()
)
appnLsStatusEndSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusEndSense.setStatus("current")
_AppnLsStatusXidLocalSense_Type = SnaSenseData
_AppnLsStatusXidLocalSense_Object = MibTableColumn
appnLsStatusXidLocalSense = _AppnLsStatusXidLocalSense_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 10),
    _AppnLsStatusXidLocalSense_Type()
)
appnLsStatusXidLocalSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusXidLocalSense.setStatus("current")
_AppnLsStatusXidRemoteSense_Type = SnaSenseData
_AppnLsStatusXidRemoteSense_Object = MibTableColumn
appnLsStatusXidRemoteSense = _AppnLsStatusXidRemoteSense_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 11),
    _AppnLsStatusXidRemoteSense_Type()
)
appnLsStatusXidRemoteSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusXidRemoteSense.setStatus("current")


class _AppnLsStatusXidByteInError_Type(Integer32):
    """Custom type appnLsStatusXidByteInError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AppnLsStatusXidByteInError_Type.__name__ = "Integer32"
_AppnLsStatusXidByteInError_Object = MibTableColumn
appnLsStatusXidByteInError = _AppnLsStatusXidByteInError_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 12),
    _AppnLsStatusXidByteInError_Type()
)
appnLsStatusXidByteInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusXidByteInError.setStatus("current")


class _AppnLsStatusXidBitInError_Type(Integer32):
    """Custom type appnLsStatusXidBitInError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AppnLsStatusXidBitInError_Type.__name__ = "Integer32"
_AppnLsStatusXidBitInError_Object = MibTableColumn
appnLsStatusXidBitInError = _AppnLsStatusXidBitInError_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 13),
    _AppnLsStatusXidBitInError_Type()
)
appnLsStatusXidBitInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusXidBitInError.setStatus("current")
_AppnLsStatusDlcType_Type = IANAifType
_AppnLsStatusDlcType_Object = MibTableColumn
appnLsStatusDlcType = _AppnLsStatusDlcType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 14),
    _AppnLsStatusDlcType_Type()
)
appnLsStatusDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusDlcType.setStatus("current")
_AppnLsStatusLocalAddr_Type = DisplayableDlcAddress
_AppnLsStatusLocalAddr_Object = MibTableColumn
appnLsStatusLocalAddr = _AppnLsStatusLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 15),
    _AppnLsStatusLocalAddr_Type()
)
appnLsStatusLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusLocalAddr.setStatus("current")
_AppnLsStatusRemoteAddr_Type = DisplayableDlcAddress
_AppnLsStatusRemoteAddr_Object = MibTableColumn
appnLsStatusRemoteAddr = _AppnLsStatusRemoteAddr_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 5, 2, 1, 16),
    _AppnLsStatusRemoteAddr_Type()
)
appnLsStatusRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLsStatusRemoteAddr.setStatus("current")
_AppnVrnInfo_ObjectIdentity = ObjectIdentity
appnVrnInfo = _AppnVrnInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 6)
)
_AppnVrnTable_Object = MibTable
appnVrnTable = _AppnVrnTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    appnVrnTable.setStatus("current")
_AppnVrnEntry_Object = MibTableRow
appnVrnEntry = _AppnVrnEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 6, 1, 1)
)
appnVrnEntry.setIndexNames(
    (0, "APPN-MIB", "appnVrnName"),
    (0, "APPN-MIB", "appnVrnTgNum"),
    (0, "APPN-MIB", "appnVrnPortName"),
)
if mibBuilder.loadTexts:
    appnVrnEntry.setStatus("current")
_AppnVrnName_Type = SnaControlPointName
_AppnVrnName_Object = MibTableColumn
appnVrnName = _AppnVrnName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 6, 1, 1, 1),
    _AppnVrnName_Type()
)
appnVrnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnVrnName.setStatus("current")


class _AppnVrnTgNum_Type(Integer32):
    """Custom type appnVrnTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnVrnTgNum_Type.__name__ = "Integer32"
_AppnVrnTgNum_Object = MibTableColumn
appnVrnTgNum = _AppnVrnTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 6, 1, 1, 2),
    _AppnVrnTgNum_Type()
)
appnVrnTgNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnVrnTgNum.setStatus("current")


class _AppnVrnPortName_Type(DisplayString):
    """Custom type appnVrnPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AppnVrnPortName_Type.__name__ = "DisplayString"
_AppnVrnPortName_Object = MibTableColumn
appnVrnPortName = _AppnVrnPortName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 1, 6, 1, 1, 3),
    _AppnVrnPortName_Type()
)
appnVrnPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnVrnPortName.setStatus("current")
_AppnNn_ObjectIdentity = ObjectIdentity
appnNn = _AppnNn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2)
)
_AppnNnTopo_ObjectIdentity = ObjectIdentity
appnNnTopo = _AppnNnTopo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 1)
)
_AppnNnTopoMaxNodes_Type = Gauge32
_AppnNnTopoMaxNodes_Object = MibScalar
appnNnTopoMaxNodes = _AppnNnTopoMaxNodes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 1, 1),
    _AppnNnTopoMaxNodes_Type()
)
appnNnTopoMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTopoMaxNodes.setStatus("current")
if mibBuilder.loadTexts:
    appnNnTopoMaxNodes.setUnits("node entries")
_AppnNnTopoCurNumNodes_Type = Gauge32
_AppnNnTopoCurNumNodes_Object = MibScalar
appnNnTopoCurNumNodes = _AppnNnTopoCurNumNodes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 1, 2),
    _AppnNnTopoCurNumNodes_Type()
)
appnNnTopoCurNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTopoCurNumNodes.setStatus("current")
if mibBuilder.loadTexts:
    appnNnTopoCurNumNodes.setUnits("node entries")
_AppnNnTopoNodePurges_Type = AppnNodeCounter
_AppnNnTopoNodePurges_Object = MibScalar
appnNnTopoNodePurges = _AppnNnTopoNodePurges_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 1, 3),
    _AppnNnTopoNodePurges_Type()
)
appnNnTopoNodePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTopoNodePurges.setStatus("current")
if mibBuilder.loadTexts:
    appnNnTopoNodePurges.setUnits("node entries")
_AppnNnTopoTgPurges_Type = AppnNodeCounter
_AppnNnTopoTgPurges_Object = MibScalar
appnNnTopoTgPurges = _AppnNnTopoTgPurges_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 1, 4),
    _AppnNnTopoTgPurges_Type()
)
appnNnTopoTgPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTopoTgPurges.setStatus("current")
if mibBuilder.loadTexts:
    appnNnTopoTgPurges.setUnits("TG entries")
_AppnNnTopoTotalTduWars_Type = AppnNodeCounter
_AppnNnTopoTotalTduWars_Object = MibScalar
appnNnTopoTotalTduWars = _AppnNnTopoTotalTduWars_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 1, 5),
    _AppnNnTopoTotalTduWars_Type()
)
appnNnTopoTotalTduWars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTopoTotalTduWars.setStatus("current")
if mibBuilder.loadTexts:
    appnNnTopoTotalTduWars.setUnits("TDU wars")
_AppnNnTopology_ObjectIdentity = ObjectIdentity
appnNnTopology = _AppnNnTopology_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2)
)
_AppnNnTopologyFRTable_Object = MibTable
appnNnTopologyFRTable = _AppnNnTopologyFRTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    appnNnTopologyFRTable.setStatus("current")
_AppnNnTopologyFREntry_Object = MibTableRow
appnNnTopologyFREntry = _AppnNnTopologyFREntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1)
)
appnNnTopologyFREntry.setIndexNames(
    (0, "APPN-MIB", "appnNnNodeFRFrsn"),
    (0, "APPN-MIB", "appnNnNodeFRName"),
)
if mibBuilder.loadTexts:
    appnNnTopologyFREntry.setStatus("current")
_AppnNnNodeFRFrsn_Type = Unsigned32
_AppnNnNodeFRFrsn_Object = MibTableColumn
appnNnNodeFRFrsn = _AppnNnNodeFRFrsn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 1),
    _AppnNnNodeFRFrsn_Type()
)
appnNnNodeFRFrsn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnNodeFRFrsn.setStatus("current")
_AppnNnNodeFRName_Type = SnaControlPointName
_AppnNnNodeFRName_Object = MibTableColumn
appnNnNodeFRName = _AppnNnNodeFRName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 2),
    _AppnNnNodeFRName_Type()
)
appnNnNodeFRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnNodeFRName.setStatus("current")
_AppnNnNodeFREntryTimeLeft_Type = AppnTopologyEntryTimeLeft
_AppnNnNodeFREntryTimeLeft_Object = MibTableColumn
appnNnNodeFREntryTimeLeft = _AppnNnNodeFREntryTimeLeft_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 3),
    _AppnNnNodeFREntryTimeLeft_Type()
)
appnNnNodeFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFREntryTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    appnNnNodeFREntryTimeLeft.setUnits("days")


class _AppnNnNodeFRType_Type(Integer32):
    """Custom type appnNnNodeFRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkNode", 1),
          ("virtualRoutingNode", 3))
    )


_AppnNnNodeFRType_Type.__name__ = "Integer32"
_AppnNnNodeFRType_Object = MibTableColumn
appnNnNodeFRType = _AppnNnNodeFRType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 4),
    _AppnNnNodeFRType_Type()
)
appnNnNodeFRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRType.setStatus("current")
_AppnNnNodeFRRsn_Type = Unsigned32
_AppnNnNodeFRRsn_Object = MibTableColumn
appnNnNodeFRRsn = _AppnNnNodeFRRsn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 5),
    _AppnNnNodeFRRsn_Type()
)
appnNnNodeFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRRsn.setStatus("current")


class _AppnNnNodeFRRouteAddResist_Type(Integer32):
    """Custom type appnNnNodeFRRouteAddResist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnNodeFRRouteAddResist_Type.__name__ = "Integer32"
_AppnNnNodeFRRouteAddResist_Object = MibTableColumn
appnNnNodeFRRouteAddResist = _AppnNnNodeFRRouteAddResist_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 6),
    _AppnNnNodeFRRouteAddResist_Type()
)
appnNnNodeFRRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRRouteAddResist.setStatus("current")
_AppnNnNodeFRCongested_Type = TruthValue
_AppnNnNodeFRCongested_Object = MibTableColumn
appnNnNodeFRCongested = _AppnNnNodeFRCongested_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 7),
    _AppnNnNodeFRCongested_Type()
)
appnNnNodeFRCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRCongested.setStatus("current")
_AppnNnNodeFRIsrDepleted_Type = TruthValue
_AppnNnNodeFRIsrDepleted_Object = MibTableColumn
appnNnNodeFRIsrDepleted = _AppnNnNodeFRIsrDepleted_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 8),
    _AppnNnNodeFRIsrDepleted_Type()
)
appnNnNodeFRIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRIsrDepleted.setStatus("current")
_AppnNnNodeFRQuiescing_Type = TruthValue
_AppnNnNodeFRQuiescing_Object = MibTableColumn
appnNnNodeFRQuiescing = _AppnNnNodeFRQuiescing_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 9),
    _AppnNnNodeFRQuiescing_Type()
)
appnNnNodeFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRQuiescing.setStatus("current")
_AppnNnNodeFRGateway_Type = TruthValue
_AppnNnNodeFRGateway_Object = MibTableColumn
appnNnNodeFRGateway = _AppnNnNodeFRGateway_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 10),
    _AppnNnNodeFRGateway_Type()
)
appnNnNodeFRGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRGateway.setStatus("current")
_AppnNnNodeFRCentralDirectory_Type = TruthValue
_AppnNnNodeFRCentralDirectory_Object = MibTableColumn
appnNnNodeFRCentralDirectory = _AppnNnNodeFRCentralDirectory_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 11),
    _AppnNnNodeFRCentralDirectory_Type()
)
appnNnNodeFRCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRCentralDirectory.setStatus("current")
_AppnNnNodeFRIsr_Type = TruthValue
_AppnNnNodeFRIsr_Object = MibTableColumn
appnNnNodeFRIsr = _AppnNnNodeFRIsr_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 12),
    _AppnNnNodeFRIsr_Type()
)
appnNnNodeFRIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRIsr.setStatus("current")
_AppnNnNodeFRGarbageCollect_Type = TruthValue
_AppnNnNodeFRGarbageCollect_Object = MibTableColumn
appnNnNodeFRGarbageCollect = _AppnNnNodeFRGarbageCollect_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 13),
    _AppnNnNodeFRGarbageCollect_Type()
)
appnNnNodeFRGarbageCollect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRGarbageCollect.setStatus("current")


class _AppnNnNodeFRHprSupport_Type(Integer32):
    """Custom type appnNnNodeFRHprSupport based on Integer32"""
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
        *(("controlFlowsOverRtpTower", 4),
          ("hprBaseOnly", 2),
          ("noHprSupport", 1),
          ("rtpTower", 3))
    )


_AppnNnNodeFRHprSupport_Type.__name__ = "Integer32"
_AppnNnNodeFRHprSupport_Object = MibTableColumn
appnNnNodeFRHprSupport = _AppnNnNodeFRHprSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 14),
    _AppnNnNodeFRHprSupport_Type()
)
appnNnNodeFRHprSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRHprSupport.setStatus("current")
_AppnNnNodeFRPeriBorderSup_Type = TruthValue
_AppnNnNodeFRPeriBorderSup_Object = MibTableColumn
appnNnNodeFRPeriBorderSup = _AppnNnNodeFRPeriBorderSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 15),
    _AppnNnNodeFRPeriBorderSup_Type()
)
appnNnNodeFRPeriBorderSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRPeriBorderSup.setStatus("current")
_AppnNnNodeFRInterchangeSup_Type = TruthValue
_AppnNnNodeFRInterchangeSup_Object = MibTableColumn
appnNnNodeFRInterchangeSup = _AppnNnNodeFRInterchangeSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 16),
    _AppnNnNodeFRInterchangeSup_Type()
)
appnNnNodeFRInterchangeSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRInterchangeSup.setStatus("current")
_AppnNnNodeFRExteBorderSup_Type = TruthValue
_AppnNnNodeFRExteBorderSup_Object = MibTableColumn
appnNnNodeFRExteBorderSup = _AppnNnNodeFRExteBorderSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 17),
    _AppnNnNodeFRExteBorderSup_Type()
)
appnNnNodeFRExteBorderSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRExteBorderSup.setStatus("current")
_AppnNnNodeFRBranchAwareness_Type = TruthValue
_AppnNnNodeFRBranchAwareness_Object = MibTableColumn
appnNnNodeFRBranchAwareness = _AppnNnNodeFRBranchAwareness_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 3, 1, 18),
    _AppnNnNodeFRBranchAwareness_Type()
)
appnNnNodeFRBranchAwareness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnNodeFRBranchAwareness.setStatus("current")
_AppnNnTgTopologyFRTable_Object = MibTable
appnNnTgTopologyFRTable = _AppnNnTgTopologyFRTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    appnNnTgTopologyFRTable.setStatus("current")
_AppnNnTgTopologyFREntry_Object = MibTableRow
appnNnTgTopologyFREntry = _AppnNnTgTopologyFREntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1)
)
appnNnTgTopologyFREntry.setIndexNames(
    (0, "APPN-MIB", "appnNnTgFRFrsn"),
    (0, "APPN-MIB", "appnNnTgFROwner"),
    (0, "APPN-MIB", "appnNnTgFRDest"),
    (0, "APPN-MIB", "appnNnTgFRNum"),
)
if mibBuilder.loadTexts:
    appnNnTgTopologyFREntry.setStatus("current")
_AppnNnTgFRFrsn_Type = Unsigned32
_AppnNnTgFRFrsn_Object = MibTableColumn
appnNnTgFRFrsn = _AppnNnTgFRFrsn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 1),
    _AppnNnTgFRFrsn_Type()
)
appnNnTgFRFrsn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnTgFRFrsn.setStatus("current")
_AppnNnTgFROwner_Type = SnaControlPointName
_AppnNnTgFROwner_Object = MibTableColumn
appnNnTgFROwner = _AppnNnTgFROwner_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 2),
    _AppnNnTgFROwner_Type()
)
appnNnTgFROwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnTgFROwner.setStatus("current")
_AppnNnTgFRDest_Type = SnaControlPointName
_AppnNnTgFRDest_Object = MibTableColumn
appnNnTgFRDest = _AppnNnTgFRDest_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 3),
    _AppnNnTgFRDest_Type()
)
appnNnTgFRDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnTgFRDest.setStatus("current")


class _AppnNnTgFRNum_Type(Integer32):
    """Custom type appnNnTgFRNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgFRNum_Type.__name__ = "Integer32"
_AppnNnTgFRNum_Object = MibTableColumn
appnNnTgFRNum = _AppnNnTgFRNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 4),
    _AppnNnTgFRNum_Type()
)
appnNnTgFRNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnNnTgFRNum.setStatus("current")
_AppnNnTgFREntryTimeLeft_Type = AppnTopologyEntryTimeLeft
_AppnNnTgFREntryTimeLeft_Object = MibTableColumn
appnNnTgFREntryTimeLeft = _AppnNnTgFREntryTimeLeft_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 5),
    _AppnNnTgFREntryTimeLeft_Type()
)
appnNnTgFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFREntryTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    appnNnTgFREntryTimeLeft.setUnits("days")
_AppnNnTgFRDestVirtual_Type = TruthValue
_AppnNnTgFRDestVirtual_Object = MibTableColumn
appnNnTgFRDestVirtual = _AppnNnTgFRDestVirtual_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 6),
    _AppnNnTgFRDestVirtual_Type()
)
appnNnTgFRDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRDestVirtual.setStatus("current")
_AppnNnTgFRDlcData_Type = AppnTgDlcData
_AppnNnTgFRDlcData_Object = MibTableColumn
appnNnTgFRDlcData = _AppnNnTgFRDlcData_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 7),
    _AppnNnTgFRDlcData_Type()
)
appnNnTgFRDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRDlcData.setStatus("current")
_AppnNnTgFRRsn_Type = Unsigned32
_AppnNnTgFRRsn_Object = MibTableColumn
appnNnTgFRRsn = _AppnNnTgFRRsn_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 8),
    _AppnNnTgFRRsn_Type()
)
appnNnTgFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRRsn.setStatus("current")
_AppnNnTgFROperational_Type = TruthValue
_AppnNnTgFROperational_Object = MibTableColumn
appnNnTgFROperational = _AppnNnTgFROperational_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 9),
    _AppnNnTgFROperational_Type()
)
appnNnTgFROperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFROperational.setStatus("current")
_AppnNnTgFRQuiescing_Type = TruthValue
_AppnNnTgFRQuiescing_Object = MibTableColumn
appnNnTgFRQuiescing = _AppnNnTgFRQuiescing_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 10),
    _AppnNnTgFRQuiescing_Type()
)
appnNnTgFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRQuiescing.setStatus("current")


class _AppnNnTgFRCpCpSession_Type(Integer32):
    """Custom type appnNnTgFRCpCpSession based on Integer32"""
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
        *(("notSupported", 3),
          ("supportedActive", 2),
          ("supportedNotActive", 4),
          ("supportedUnknownStatus", 1))
    )


_AppnNnTgFRCpCpSession_Type.__name__ = "Integer32"
_AppnNnTgFRCpCpSession_Object = MibTableColumn
appnNnTgFRCpCpSession = _AppnNnTgFRCpCpSession_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 11),
    _AppnNnTgFRCpCpSession_Type()
)
appnNnTgFRCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRCpCpSession.setStatus("current")
_AppnNnTgFREffCap_Type = AppnTgEffectiveCapacity
_AppnNnTgFREffCap_Object = MibTableColumn
appnNnTgFREffCap = _AppnNnTgFREffCap_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 12),
    _AppnNnTgFREffCap_Type()
)
appnNnTgFREffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFREffCap.setStatus("current")


class _AppnNnTgFRConnCost_Type(Integer32):
    """Custom type appnNnTgFRConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgFRConnCost_Type.__name__ = "Integer32"
_AppnNnTgFRConnCost_Object = MibTableColumn
appnNnTgFRConnCost = _AppnNnTgFRConnCost_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 13),
    _AppnNnTgFRConnCost_Type()
)
appnNnTgFRConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRConnCost.setStatus("current")


class _AppnNnTgFRByteCost_Type(Integer32):
    """Custom type appnNnTgFRByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgFRByteCost_Type.__name__ = "Integer32"
_AppnNnTgFRByteCost_Object = MibTableColumn
appnNnTgFRByteCost = _AppnNnTgFRByteCost_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 14),
    _AppnNnTgFRByteCost_Type()
)
appnNnTgFRByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRByteCost.setStatus("current")
_AppnNnTgFRSecurity_Type = AppnTgSecurity
_AppnNnTgFRSecurity_Object = MibTableColumn
appnNnTgFRSecurity = _AppnNnTgFRSecurity_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 15),
    _AppnNnTgFRSecurity_Type()
)
appnNnTgFRSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRSecurity.setStatus("current")
_AppnNnTgFRDelay_Type = AppnTgDelay
_AppnNnTgFRDelay_Object = MibTableColumn
appnNnTgFRDelay = _AppnNnTgFRDelay_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 16),
    _AppnNnTgFRDelay_Type()
)
appnNnTgFRDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRDelay.setStatus("current")


class _AppnNnTgFRUsr1_Type(Integer32):
    """Custom type appnNnTgFRUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgFRUsr1_Type.__name__ = "Integer32"
_AppnNnTgFRUsr1_Object = MibTableColumn
appnNnTgFRUsr1 = _AppnNnTgFRUsr1_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 17),
    _AppnNnTgFRUsr1_Type()
)
appnNnTgFRUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRUsr1.setStatus("current")


class _AppnNnTgFRUsr2_Type(Integer32):
    """Custom type appnNnTgFRUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgFRUsr2_Type.__name__ = "Integer32"
_AppnNnTgFRUsr2_Object = MibTableColumn
appnNnTgFRUsr2 = _AppnNnTgFRUsr2_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 18),
    _AppnNnTgFRUsr2_Type()
)
appnNnTgFRUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRUsr2.setStatus("current")


class _AppnNnTgFRUsr3_Type(Integer32):
    """Custom type appnNnTgFRUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnNnTgFRUsr3_Type.__name__ = "Integer32"
_AppnNnTgFRUsr3_Object = MibTableColumn
appnNnTgFRUsr3 = _AppnNnTgFRUsr3_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 19),
    _AppnNnTgFRUsr3_Type()
)
appnNnTgFRUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRUsr3.setStatus("current")
_AppnNnTgFRGarbageCollect_Type = TruthValue
_AppnNnTgFRGarbageCollect_Object = MibTableColumn
appnNnTgFRGarbageCollect = _AppnNnTgFRGarbageCollect_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 20),
    _AppnNnTgFRGarbageCollect_Type()
)
appnNnTgFRGarbageCollect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRGarbageCollect.setStatus("current")
_AppnNnTgFRSubareaNum_Type = Unsigned32
_AppnNnTgFRSubareaNum_Object = MibTableColumn
appnNnTgFRSubareaNum = _AppnNnTgFRSubareaNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 21),
    _AppnNnTgFRSubareaNum_Type()
)
appnNnTgFRSubareaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRSubareaNum.setStatus("current")
_AppnNnTgFRHprSup_Type = TruthValue
_AppnNnTgFRHprSup_Object = MibTableColumn
appnNnTgFRHprSup = _AppnNnTgFRHprSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 22),
    _AppnNnTgFRHprSup_Type()
)
appnNnTgFRHprSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRHprSup.setStatus("current")
_AppnNnTgFRDestHprTrans_Type = TruthValue
_AppnNnTgFRDestHprTrans_Object = MibTableColumn
appnNnTgFRDestHprTrans = _AppnNnTgFRDestHprTrans_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 23),
    _AppnNnTgFRDestHprTrans_Type()
)
appnNnTgFRDestHprTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRDestHprTrans.setStatus("current")


class _AppnNnTgFRTypeIndicator_Type(Integer32):
    """Custom type appnNnTgFRTypeIndicator based on Integer32"""
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
        *(("appnOrBfTg", 2),
          ("interchangeTg", 3),
          ("unknown", 1),
          ("virtualRouteTg", 4))
    )


_AppnNnTgFRTypeIndicator_Type.__name__ = "Integer32"
_AppnNnTgFRTypeIndicator_Object = MibTableColumn
appnNnTgFRTypeIndicator = _AppnNnTgFRTypeIndicator_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 24),
    _AppnNnTgFRTypeIndicator_Type()
)
appnNnTgFRTypeIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRTypeIndicator.setStatus("current")
_AppnNnTgFRIntersubnet_Type = TruthValue
_AppnNnTgFRIntersubnet_Object = MibTableColumn
appnNnTgFRIntersubnet = _AppnNnTgFRIntersubnet_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 25),
    _AppnNnTgFRIntersubnet_Type()
)
appnNnTgFRIntersubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRIntersubnet.setStatus("current")
_AppnNnTgFRMltgLinkType_Type = TruthValue
_AppnNnTgFRMltgLinkType_Object = MibTableColumn
appnNnTgFRMltgLinkType = _AppnNnTgFRMltgLinkType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 26),
    _AppnNnTgFRMltgLinkType_Type()
)
appnNnTgFRMltgLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRMltgLinkType.setStatus("current")
_AppnNnTgFRBranchTg_Type = TruthValue
_AppnNnTgFRBranchTg_Object = MibTableColumn
appnNnTgFRBranchTg = _AppnNnTgFRBranchTg_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 2, 2, 4, 1, 27),
    _AppnNnTgFRBranchTg_Type()
)
appnNnTgFRBranchTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnNnTgFRBranchTg.setStatus("current")
_AppnLocalTopology_ObjectIdentity = ObjectIdentity
appnLocalTopology = _AppnLocalTopology_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3)
)
_AppnLocalTgTable_Object = MibTable
appnLocalTgTable = _AppnLocalTgTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    appnLocalTgTable.setStatus("current")
_AppnLocalTgEntry_Object = MibTableRow
appnLocalTgEntry = _AppnLocalTgEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1)
)
appnLocalTgEntry.setIndexNames(
    (0, "APPN-MIB", "appnLocalTgDest"),
    (0, "APPN-MIB", "appnLocalTgNum"),
)
if mibBuilder.loadTexts:
    appnLocalTgEntry.setStatus("current")
_AppnLocalTgDest_Type = SnaControlPointName
_AppnLocalTgDest_Object = MibTableColumn
appnLocalTgDest = _AppnLocalTgDest_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 1),
    _AppnLocalTgDest_Type()
)
appnLocalTgDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLocalTgDest.setStatus("current")


class _AppnLocalTgNum_Type(Integer32):
    """Custom type appnLocalTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalTgNum_Type.__name__ = "Integer32"
_AppnLocalTgNum_Object = MibTableColumn
appnLocalTgNum = _AppnLocalTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 2),
    _AppnLocalTgNum_Type()
)
appnLocalTgNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLocalTgNum.setStatus("current")
_AppnLocalTgDestVirtual_Type = TruthValue
_AppnLocalTgDestVirtual_Object = MibTableColumn
appnLocalTgDestVirtual = _AppnLocalTgDestVirtual_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 3),
    _AppnLocalTgDestVirtual_Type()
)
appnLocalTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgDestVirtual.setStatus("current")
_AppnLocalTgDlcData_Type = AppnTgDlcData
_AppnLocalTgDlcData_Object = MibTableColumn
appnLocalTgDlcData = _AppnLocalTgDlcData_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 4),
    _AppnLocalTgDlcData_Type()
)
appnLocalTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgDlcData.setStatus("current")


class _AppnLocalTgPortName_Type(DisplayString):
    """Custom type appnLocalTgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AppnLocalTgPortName_Type.__name__ = "DisplayString"
_AppnLocalTgPortName_Object = MibTableColumn
appnLocalTgPortName = _AppnLocalTgPortName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 5),
    _AppnLocalTgPortName_Type()
)
appnLocalTgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgPortName.setStatus("current")
_AppnLocalTgQuiescing_Type = TruthValue
_AppnLocalTgQuiescing_Object = MibTableColumn
appnLocalTgQuiescing = _AppnLocalTgQuiescing_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 6),
    _AppnLocalTgQuiescing_Type()
)
appnLocalTgQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgQuiescing.setStatus("current")
_AppnLocalTgOperational_Type = TruthValue
_AppnLocalTgOperational_Object = MibTableColumn
appnLocalTgOperational = _AppnLocalTgOperational_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 7),
    _AppnLocalTgOperational_Type()
)
appnLocalTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgOperational.setStatus("current")


class _AppnLocalTgCpCpSession_Type(Integer32):
    """Custom type appnLocalTgCpCpSession based on Integer32"""
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
        *(("notSupported", 3),
          ("supportedActive", 2),
          ("supportedNotActive", 4),
          ("supportedUnknownStatus", 1))
    )


_AppnLocalTgCpCpSession_Type.__name__ = "Integer32"
_AppnLocalTgCpCpSession_Object = MibTableColumn
appnLocalTgCpCpSession = _AppnLocalTgCpCpSession_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 8),
    _AppnLocalTgCpCpSession_Type()
)
appnLocalTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgCpCpSession.setStatus("current")
_AppnLocalTgEffCap_Type = AppnTgEffectiveCapacity
_AppnLocalTgEffCap_Object = MibTableColumn
appnLocalTgEffCap = _AppnLocalTgEffCap_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 9),
    _AppnLocalTgEffCap_Type()
)
appnLocalTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgEffCap.setStatus("current")


class _AppnLocalTgConnCost_Type(Integer32):
    """Custom type appnLocalTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalTgConnCost_Type.__name__ = "Integer32"
_AppnLocalTgConnCost_Object = MibTableColumn
appnLocalTgConnCost = _AppnLocalTgConnCost_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 10),
    _AppnLocalTgConnCost_Type()
)
appnLocalTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgConnCost.setStatus("current")


class _AppnLocalTgByteCost_Type(Integer32):
    """Custom type appnLocalTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalTgByteCost_Type.__name__ = "Integer32"
_AppnLocalTgByteCost_Object = MibTableColumn
appnLocalTgByteCost = _AppnLocalTgByteCost_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 11),
    _AppnLocalTgByteCost_Type()
)
appnLocalTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgByteCost.setStatus("current")
_AppnLocalTgSecurity_Type = AppnTgSecurity
_AppnLocalTgSecurity_Object = MibTableColumn
appnLocalTgSecurity = _AppnLocalTgSecurity_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 12),
    _AppnLocalTgSecurity_Type()
)
appnLocalTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgSecurity.setStatus("current")
_AppnLocalTgDelay_Type = AppnTgDelay
_AppnLocalTgDelay_Object = MibTableColumn
appnLocalTgDelay = _AppnLocalTgDelay_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 13),
    _AppnLocalTgDelay_Type()
)
appnLocalTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgDelay.setStatus("current")


class _AppnLocalTgUsr1_Type(Integer32):
    """Custom type appnLocalTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalTgUsr1_Type.__name__ = "Integer32"
_AppnLocalTgUsr1_Object = MibTableColumn
appnLocalTgUsr1 = _AppnLocalTgUsr1_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 14),
    _AppnLocalTgUsr1_Type()
)
appnLocalTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgUsr1.setStatus("current")


class _AppnLocalTgUsr2_Type(Integer32):
    """Custom type appnLocalTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalTgUsr2_Type.__name__ = "Integer32"
_AppnLocalTgUsr2_Object = MibTableColumn
appnLocalTgUsr2 = _AppnLocalTgUsr2_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 15),
    _AppnLocalTgUsr2_Type()
)
appnLocalTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgUsr2.setStatus("current")


class _AppnLocalTgUsr3_Type(Integer32):
    """Custom type appnLocalTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalTgUsr3_Type.__name__ = "Integer32"
_AppnLocalTgUsr3_Object = MibTableColumn
appnLocalTgUsr3 = _AppnLocalTgUsr3_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 16),
    _AppnLocalTgUsr3_Type()
)
appnLocalTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgUsr3.setStatus("current")


class _AppnLocalTgHprSup_Type(Integer32):
    """Custom type appnLocalTgHprSup based on Integer32"""
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
        *(("controlFlowsOverRtpTower", 4),
          ("hprBaseOnly", 2),
          ("noHprSupport", 1),
          ("rtpTower", 3))
    )


_AppnLocalTgHprSup_Type.__name__ = "Integer32"
_AppnLocalTgHprSup_Object = MibTableColumn
appnLocalTgHprSup = _AppnLocalTgHprSup_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 17),
    _AppnLocalTgHprSup_Type()
)
appnLocalTgHprSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgHprSup.setStatus("current")
_AppnLocalTgIntersubnet_Type = TruthValue
_AppnLocalTgIntersubnet_Object = MibTableColumn
appnLocalTgIntersubnet = _AppnLocalTgIntersubnet_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 18),
    _AppnLocalTgIntersubnet_Type()
)
appnLocalTgIntersubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgIntersubnet.setStatus("current")
_AppnLocalTgMltgLinkType_Type = TruthValue
_AppnLocalTgMltgLinkType_Object = MibTableColumn
appnLocalTgMltgLinkType = _AppnLocalTgMltgLinkType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 19),
    _AppnLocalTgMltgLinkType_Type()
)
appnLocalTgMltgLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgMltgLinkType.setStatus("current")


class _AppnLocalTgBranchLinkType_Type(Integer32):
    """Custom type appnLocalTgBranchLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 3),
          ("downlinkToBranchNetworkNode", 4),
          ("none", 5),
          ("other", 1),
          ("unknown", 255),
          ("uplink", 2))
    )


_AppnLocalTgBranchLinkType_Type.__name__ = "Integer32"
_AppnLocalTgBranchLinkType_Object = MibTableColumn
appnLocalTgBranchLinkType = _AppnLocalTgBranchLinkType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 1, 1, 20),
    _AppnLocalTgBranchLinkType_Type()
)
appnLocalTgBranchLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalTgBranchLinkType.setStatus("current")
_AppnLocalEnTgTable_Object = MibTable
appnLocalEnTgTable = _AppnLocalEnTgTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    appnLocalEnTgTable.setStatus("current")
_AppnLocalEnTgEntry_Object = MibTableRow
appnLocalEnTgEntry = _AppnLocalEnTgEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1)
)
appnLocalEnTgEntry.setIndexNames(
    (0, "APPN-MIB", "appnLocalEnTgOrigin"),
    (0, "APPN-MIB", "appnLocalEnTgDest"),
    (0, "APPN-MIB", "appnLocalEnTgNum"),
)
if mibBuilder.loadTexts:
    appnLocalEnTgEntry.setStatus("current")
_AppnLocalEnTgOrigin_Type = SnaControlPointName
_AppnLocalEnTgOrigin_Object = MibTableColumn
appnLocalEnTgOrigin = _AppnLocalEnTgOrigin_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 1),
    _AppnLocalEnTgOrigin_Type()
)
appnLocalEnTgOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLocalEnTgOrigin.setStatus("current")
_AppnLocalEnTgDest_Type = SnaControlPointName
_AppnLocalEnTgDest_Object = MibTableColumn
appnLocalEnTgDest = _AppnLocalEnTgDest_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 2),
    _AppnLocalEnTgDest_Type()
)
appnLocalEnTgDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLocalEnTgDest.setStatus("current")


class _AppnLocalEnTgNum_Type(Integer32):
    """Custom type appnLocalEnTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalEnTgNum_Type.__name__ = "Integer32"
_AppnLocalEnTgNum_Object = MibTableColumn
appnLocalEnTgNum = _AppnLocalEnTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 3),
    _AppnLocalEnTgNum_Type()
)
appnLocalEnTgNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnLocalEnTgNum.setStatus("current")
_AppnLocalEnTgEntryTimeLeft_Type = AppnTopologyEntryTimeLeft
_AppnLocalEnTgEntryTimeLeft_Object = MibTableColumn
appnLocalEnTgEntryTimeLeft = _AppnLocalEnTgEntryTimeLeft_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 4),
    _AppnLocalEnTgEntryTimeLeft_Type()
)
appnLocalEnTgEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgEntryTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    appnLocalEnTgEntryTimeLeft.setUnits("days")
_AppnLocalEnTgDestVirtual_Type = TruthValue
_AppnLocalEnTgDestVirtual_Object = MibTableColumn
appnLocalEnTgDestVirtual = _AppnLocalEnTgDestVirtual_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 5),
    _AppnLocalEnTgDestVirtual_Type()
)
appnLocalEnTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgDestVirtual.setStatus("current")
_AppnLocalEnTgDlcData_Type = AppnTgDlcData
_AppnLocalEnTgDlcData_Object = MibTableColumn
appnLocalEnTgDlcData = _AppnLocalEnTgDlcData_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 6),
    _AppnLocalEnTgDlcData_Type()
)
appnLocalEnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgDlcData.setStatus("current")
_AppnLocalEnTgOperational_Type = TruthValue
_AppnLocalEnTgOperational_Object = MibTableColumn
appnLocalEnTgOperational = _AppnLocalEnTgOperational_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 7),
    _AppnLocalEnTgOperational_Type()
)
appnLocalEnTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgOperational.setStatus("current")


class _AppnLocalEnTgCpCpSession_Type(Integer32):
    """Custom type appnLocalEnTgCpCpSession based on Integer32"""
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
        *(("notSupported", 3),
          ("supportedActive", 2),
          ("supportedNotActive", 4),
          ("supportedUnknownStatus", 1))
    )


_AppnLocalEnTgCpCpSession_Type.__name__ = "Integer32"
_AppnLocalEnTgCpCpSession_Object = MibTableColumn
appnLocalEnTgCpCpSession = _AppnLocalEnTgCpCpSession_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 8),
    _AppnLocalEnTgCpCpSession_Type()
)
appnLocalEnTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgCpCpSession.setStatus("current")
_AppnLocalEnTgEffCap_Type = AppnTgEffectiveCapacity
_AppnLocalEnTgEffCap_Object = MibTableColumn
appnLocalEnTgEffCap = _AppnLocalEnTgEffCap_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 9),
    _AppnLocalEnTgEffCap_Type()
)
appnLocalEnTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgEffCap.setStatus("current")


class _AppnLocalEnTgConnCost_Type(Integer32):
    """Custom type appnLocalEnTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalEnTgConnCost_Type.__name__ = "Integer32"
_AppnLocalEnTgConnCost_Object = MibTableColumn
appnLocalEnTgConnCost = _AppnLocalEnTgConnCost_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 10),
    _AppnLocalEnTgConnCost_Type()
)
appnLocalEnTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgConnCost.setStatus("current")


class _AppnLocalEnTgByteCost_Type(Integer32):
    """Custom type appnLocalEnTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalEnTgByteCost_Type.__name__ = "Integer32"
_AppnLocalEnTgByteCost_Object = MibTableColumn
appnLocalEnTgByteCost = _AppnLocalEnTgByteCost_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 11),
    _AppnLocalEnTgByteCost_Type()
)
appnLocalEnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgByteCost.setStatus("current")
_AppnLocalEnTgSecurity_Type = AppnTgSecurity
_AppnLocalEnTgSecurity_Object = MibTableColumn
appnLocalEnTgSecurity = _AppnLocalEnTgSecurity_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 12),
    _AppnLocalEnTgSecurity_Type()
)
appnLocalEnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgSecurity.setStatus("current")
_AppnLocalEnTgDelay_Type = AppnTgDelay
_AppnLocalEnTgDelay_Object = MibTableColumn
appnLocalEnTgDelay = _AppnLocalEnTgDelay_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 13),
    _AppnLocalEnTgDelay_Type()
)
appnLocalEnTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgDelay.setStatus("current")


class _AppnLocalEnTgUsr1_Type(Integer32):
    """Custom type appnLocalEnTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalEnTgUsr1_Type.__name__ = "Integer32"
_AppnLocalEnTgUsr1_Object = MibTableColumn
appnLocalEnTgUsr1 = _AppnLocalEnTgUsr1_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 14),
    _AppnLocalEnTgUsr1_Type()
)
appnLocalEnTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgUsr1.setStatus("current")


class _AppnLocalEnTgUsr2_Type(Integer32):
    """Custom type appnLocalEnTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalEnTgUsr2_Type.__name__ = "Integer32"
_AppnLocalEnTgUsr2_Object = MibTableColumn
appnLocalEnTgUsr2 = _AppnLocalEnTgUsr2_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 15),
    _AppnLocalEnTgUsr2_Type()
)
appnLocalEnTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgUsr2.setStatus("current")


class _AppnLocalEnTgUsr3_Type(Integer32):
    """Custom type appnLocalEnTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnLocalEnTgUsr3_Type.__name__ = "Integer32"
_AppnLocalEnTgUsr3_Object = MibTableColumn
appnLocalEnTgUsr3 = _AppnLocalEnTgUsr3_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 16),
    _AppnLocalEnTgUsr3_Type()
)
appnLocalEnTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgUsr3.setStatus("current")
_AppnLocalEnTgMltgLinkType_Type = TruthValue
_AppnLocalEnTgMltgLinkType_Object = MibTableColumn
appnLocalEnTgMltgLinkType = _AppnLocalEnTgMltgLinkType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 3, 2, 1, 17),
    _AppnLocalEnTgMltgLinkType_Type()
)
appnLocalEnTgMltgLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnLocalEnTgMltgLinkType.setStatus("current")
_AppnDir_ObjectIdentity = ObjectIdentity
appnDir = _AppnDir_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4)
)
_AppnDirPerf_ObjectIdentity = ObjectIdentity
appnDirPerf = _AppnDirPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1)
)
_AppnDirMaxCaches_Type = Unsigned32
_AppnDirMaxCaches_Object = MibScalar
appnDirMaxCaches = _AppnDirMaxCaches_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 1),
    _AppnDirMaxCaches_Type()
)
appnDirMaxCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirMaxCaches.setStatus("current")
if mibBuilder.loadTexts:
    appnDirMaxCaches.setUnits("directory entries")
_AppnDirCurCaches_Type = Gauge32
_AppnDirCurCaches_Object = MibScalar
appnDirCurCaches = _AppnDirCurCaches_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 2),
    _AppnDirCurCaches_Type()
)
appnDirCurCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirCurCaches.setStatus("current")
if mibBuilder.loadTexts:
    appnDirCurCaches.setUnits("directory entries")
_AppnDirCurHomeEntries_Type = Gauge32
_AppnDirCurHomeEntries_Object = MibScalar
appnDirCurHomeEntries = _AppnDirCurHomeEntries_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 3),
    _AppnDirCurHomeEntries_Type()
)
appnDirCurHomeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirCurHomeEntries.setStatus("current")
if mibBuilder.loadTexts:
    appnDirCurHomeEntries.setUnits("directory entries")
_AppnDirRegEntries_Type = Gauge32
_AppnDirRegEntries_Object = MibScalar
appnDirRegEntries = _AppnDirRegEntries_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 4),
    _AppnDirRegEntries_Type()
)
appnDirRegEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirRegEntries.setStatus("current")
if mibBuilder.loadTexts:
    appnDirRegEntries.setUnits("directory entries")
_AppnDirInLocates_Type = AppnNodeCounter
_AppnDirInLocates_Object = MibScalar
appnDirInLocates = _AppnDirInLocates_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 5),
    _AppnDirInLocates_Type()
)
appnDirInLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirInLocates.setStatus("current")
if mibBuilder.loadTexts:
    appnDirInLocates.setUnits("Locate messages")
_AppnDirInBcastLocates_Type = AppnNodeCounter
_AppnDirInBcastLocates_Object = MibScalar
appnDirInBcastLocates = _AppnDirInBcastLocates_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 6),
    _AppnDirInBcastLocates_Type()
)
appnDirInBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirInBcastLocates.setStatus("current")
if mibBuilder.loadTexts:
    appnDirInBcastLocates.setUnits("Locate messages")
_AppnDirOutLocates_Type = AppnNodeCounter
_AppnDirOutLocates_Object = MibScalar
appnDirOutLocates = _AppnDirOutLocates_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 7),
    _AppnDirOutLocates_Type()
)
appnDirOutLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirOutLocates.setStatus("current")
if mibBuilder.loadTexts:
    appnDirOutLocates.setUnits("Locate messages")
_AppnDirOutBcastLocates_Type = AppnNodeCounter
_AppnDirOutBcastLocates_Object = MibScalar
appnDirOutBcastLocates = _AppnDirOutBcastLocates_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 8),
    _AppnDirOutBcastLocates_Type()
)
appnDirOutBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirOutBcastLocates.setStatus("current")
if mibBuilder.loadTexts:
    appnDirOutBcastLocates.setUnits("Locate messages")
_AppnDirNotFoundLocates_Type = AppnNodeCounter
_AppnDirNotFoundLocates_Object = MibScalar
appnDirNotFoundLocates = _AppnDirNotFoundLocates_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 9),
    _AppnDirNotFoundLocates_Type()
)
appnDirNotFoundLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirNotFoundLocates.setStatus("current")
if mibBuilder.loadTexts:
    appnDirNotFoundLocates.setUnits("Locate messages")
_AppnDirNotFoundBcastLocates_Type = AppnNodeCounter
_AppnDirNotFoundBcastLocates_Object = MibScalar
appnDirNotFoundBcastLocates = _AppnDirNotFoundBcastLocates_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 10),
    _AppnDirNotFoundBcastLocates_Type()
)
appnDirNotFoundBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirNotFoundBcastLocates.setStatus("current")
if mibBuilder.loadTexts:
    appnDirNotFoundBcastLocates.setUnits("Locate messages")
_AppnDirLocateOutstands_Type = Gauge32
_AppnDirLocateOutstands_Object = MibScalar
appnDirLocateOutstands = _AppnDirLocateOutstands_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 1, 11),
    _AppnDirLocateOutstands_Type()
)
appnDirLocateOutstands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirLocateOutstands.setStatus("current")
if mibBuilder.loadTexts:
    appnDirLocateOutstands.setUnits("Locate messages")
_AppnDirTable_Object = MibTable
appnDirTable = _AppnDirTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    appnDirTable.setStatus("current")
_AppnDirEntry_Object = MibTableRow
appnDirEntry = _AppnDirEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2, 1)
)
appnDirEntry.setIndexNames(
    (0, "APPN-MIB", "appnDirLuName"),
)
if mibBuilder.loadTexts:
    appnDirEntry.setStatus("current")


class _AppnDirLuName_Type(DisplayString):
    """Custom type appnDirLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_AppnDirLuName_Type.__name__ = "DisplayString"
_AppnDirLuName_Object = MibTableColumn
appnDirLuName = _AppnDirLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2, 1, 1),
    _AppnDirLuName_Type()
)
appnDirLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnDirLuName.setStatus("current")
_AppnDirNnServerName_Type = SnaControlPointName
_AppnDirNnServerName_Object = MibTableColumn
appnDirNnServerName = _AppnDirNnServerName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2, 1, 2),
    _AppnDirNnServerName_Type()
)
appnDirNnServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirNnServerName.setStatus("current")
_AppnDirLuOwnerName_Type = SnaControlPointName
_AppnDirLuOwnerName_Object = MibTableColumn
appnDirLuOwnerName = _AppnDirLuOwnerName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2, 1, 3),
    _AppnDirLuOwnerName_Type()
)
appnDirLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirLuOwnerName.setStatus("current")


class _AppnDirLuLocation_Type(Integer32):
    """Custom type appnDirLuLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("local", 1),
          ("xdomain", 3))
    )


_AppnDirLuLocation_Type.__name__ = "Integer32"
_AppnDirLuLocation_Object = MibTableColumn
appnDirLuLocation = _AppnDirLuLocation_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2, 1, 4),
    _AppnDirLuLocation_Type()
)
appnDirLuLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirLuLocation.setStatus("current")


class _AppnDirType_Type(Integer32):
    """Custom type appnDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cache", 2),
          ("home", 1),
          ("registered", 3))
    )


_AppnDirType_Type.__name__ = "Integer32"
_AppnDirType_Object = MibTableColumn
appnDirType = _AppnDirType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2, 1, 5),
    _AppnDirType_Type()
)
appnDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirType.setStatus("current")


class _AppnDirApparentLuOwnerName_Type(DisplayString):
    """Custom type appnDirApparentLuOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_AppnDirApparentLuOwnerName_Type.__name__ = "DisplayString"
_AppnDirApparentLuOwnerName_Object = MibTableColumn
appnDirApparentLuOwnerName = _AppnDirApparentLuOwnerName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 4, 2, 1, 6),
    _AppnDirApparentLuOwnerName_Type()
)
appnDirApparentLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnDirApparentLuOwnerName.setStatus("current")
_AppnCos_ObjectIdentity = ObjectIdentity
appnCos = _AppnCos_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5)
)
_AppnCosModeTable_Object = MibTable
appnCosModeTable = _AppnCosModeTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    appnCosModeTable.setStatus("current")
_AppnCosModeEntry_Object = MibTableRow
appnCosModeEntry = _AppnCosModeEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 1, 1)
)
appnCosModeEntry.setIndexNames(
    (0, "APPN-MIB", "appnCosModeName"),
)
if mibBuilder.loadTexts:
    appnCosModeEntry.setStatus("current")
_AppnCosModeName_Type = SnaModeName
_AppnCosModeName_Object = MibTableColumn
appnCosModeName = _AppnCosModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 1, 1, 1),
    _AppnCosModeName_Type()
)
appnCosModeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosModeName.setStatus("current")
_AppnCosModeCosName_Type = SnaClassOfServiceName
_AppnCosModeCosName_Object = MibTableColumn
appnCosModeCosName = _AppnCosModeCosName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 1, 1, 2),
    _AppnCosModeCosName_Type()
)
appnCosModeCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosModeCosName.setStatus("current")
_AppnCosNameTable_Object = MibTable
appnCosNameTable = _AppnCosNameTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    appnCosNameTable.setStatus("current")
_AppnCosNameEntry_Object = MibTableRow
appnCosNameEntry = _AppnCosNameEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 2, 1)
)
appnCosNameEntry.setIndexNames(
    (0, "APPN-MIB", "appnCosName"),
)
if mibBuilder.loadTexts:
    appnCosNameEntry.setStatus("current")
_AppnCosName_Type = SnaClassOfServiceName
_AppnCosName_Object = MibTableColumn
appnCosName = _AppnCosName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 2, 1, 1),
    _AppnCosName_Type()
)
appnCosName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosName.setStatus("current")


class _AppnCosTransPriority_Type(Integer32):
    """Custom type appnCosTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_AppnCosTransPriority_Type.__name__ = "Integer32"
_AppnCosTransPriority_Object = MibTableColumn
appnCosTransPriority = _AppnCosTransPriority_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 2, 1, 2),
    _AppnCosTransPriority_Type()
)
appnCosTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTransPriority.setStatus("current")
_AppnCosNodeRowTable_Object = MibTable
appnCosNodeRowTable = _AppnCosNodeRowTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3)
)
if mibBuilder.loadTexts:
    appnCosNodeRowTable.setStatus("current")
_AppnCosNodeRowEntry_Object = MibTableRow
appnCosNodeRowEntry = _AppnCosNodeRowEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1)
)
appnCosNodeRowEntry.setIndexNames(
    (0, "APPN-MIB", "appnCosNodeRowName"),
    (0, "APPN-MIB", "appnCosNodeRowIndex"),
)
if mibBuilder.loadTexts:
    appnCosNodeRowEntry.setStatus("current")
_AppnCosNodeRowName_Type = SnaClassOfServiceName
_AppnCosNodeRowName_Object = MibTableColumn
appnCosNodeRowName = _AppnCosNodeRowName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1, 1),
    _AppnCosNodeRowName_Type()
)
appnCosNodeRowName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosNodeRowName.setStatus("current")


class _AppnCosNodeRowIndex_Type(Integer32):
    """Custom type appnCosNodeRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosNodeRowIndex_Type.__name__ = "Integer32"
_AppnCosNodeRowIndex_Object = MibTableColumn
appnCosNodeRowIndex = _AppnCosNodeRowIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1, 2),
    _AppnCosNodeRowIndex_Type()
)
appnCosNodeRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosNodeRowIndex.setStatus("current")


class _AppnCosNodeRowWgt_Type(DisplayString):
    """Custom type appnCosNodeRowWgt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AppnCosNodeRowWgt_Type.__name__ = "DisplayString"
_AppnCosNodeRowWgt_Object = MibTableColumn
appnCosNodeRowWgt = _AppnCosNodeRowWgt_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1, 3),
    _AppnCosNodeRowWgt_Type()
)
appnCosNodeRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosNodeRowWgt.setStatus("current")


class _AppnCosNodeRowResistMin_Type(Integer32):
    """Custom type appnCosNodeRowResistMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosNodeRowResistMin_Type.__name__ = "Integer32"
_AppnCosNodeRowResistMin_Object = MibTableColumn
appnCosNodeRowResistMin = _AppnCosNodeRowResistMin_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1, 4),
    _AppnCosNodeRowResistMin_Type()
)
appnCosNodeRowResistMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosNodeRowResistMin.setStatus("current")


class _AppnCosNodeRowResistMax_Type(Integer32):
    """Custom type appnCosNodeRowResistMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosNodeRowResistMax_Type.__name__ = "Integer32"
_AppnCosNodeRowResistMax_Object = MibTableColumn
appnCosNodeRowResistMax = _AppnCosNodeRowResistMax_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1, 5),
    _AppnCosNodeRowResistMax_Type()
)
appnCosNodeRowResistMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosNodeRowResistMax.setStatus("current")


class _AppnCosNodeRowMinCongestAllow_Type(Integer32):
    """Custom type appnCosNodeRowMinCongestAllow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AppnCosNodeRowMinCongestAllow_Type.__name__ = "Integer32"
_AppnCosNodeRowMinCongestAllow_Object = MibTableColumn
appnCosNodeRowMinCongestAllow = _AppnCosNodeRowMinCongestAllow_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1, 6),
    _AppnCosNodeRowMinCongestAllow_Type()
)
appnCosNodeRowMinCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosNodeRowMinCongestAllow.setStatus("current")


class _AppnCosNodeRowMaxCongestAllow_Type(Integer32):
    """Custom type appnCosNodeRowMaxCongestAllow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AppnCosNodeRowMaxCongestAllow_Type.__name__ = "Integer32"
_AppnCosNodeRowMaxCongestAllow_Object = MibTableColumn
appnCosNodeRowMaxCongestAllow = _AppnCosNodeRowMaxCongestAllow_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 3, 1, 7),
    _AppnCosNodeRowMaxCongestAllow_Type()
)
appnCosNodeRowMaxCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosNodeRowMaxCongestAllow.setStatus("current")
_AppnCosTgRowTable_Object = MibTable
appnCosTgRowTable = _AppnCosTgRowTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4)
)
if mibBuilder.loadTexts:
    appnCosTgRowTable.setStatus("current")
_AppnCosTgRowEntry_Object = MibTableRow
appnCosTgRowEntry = _AppnCosTgRowEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1)
)
appnCosTgRowEntry.setIndexNames(
    (0, "APPN-MIB", "appnCosTgRowName"),
    (0, "APPN-MIB", "appnCosTgRowIndex"),
)
if mibBuilder.loadTexts:
    appnCosTgRowEntry.setStatus("current")
_AppnCosTgRowName_Type = SnaClassOfServiceName
_AppnCosTgRowName_Object = MibTableColumn
appnCosTgRowName = _AppnCosTgRowName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 1),
    _AppnCosTgRowName_Type()
)
appnCosTgRowName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosTgRowName.setStatus("current")


class _AppnCosTgRowIndex_Type(Integer32):
    """Custom type appnCosTgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowIndex_Type.__name__ = "Integer32"
_AppnCosTgRowIndex_Object = MibTableColumn
appnCosTgRowIndex = _AppnCosTgRowIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 2),
    _AppnCosTgRowIndex_Type()
)
appnCosTgRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnCosTgRowIndex.setStatus("current")


class _AppnCosTgRowWgt_Type(DisplayString):
    """Custom type appnCosTgRowWgt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AppnCosTgRowWgt_Type.__name__ = "DisplayString"
_AppnCosTgRowWgt_Object = MibTableColumn
appnCosTgRowWgt = _AppnCosTgRowWgt_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 3),
    _AppnCosTgRowWgt_Type()
)
appnCosTgRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowWgt.setStatus("current")
_AppnCosTgRowEffCapMin_Type = AppnTgEffectiveCapacity
_AppnCosTgRowEffCapMin_Object = MibTableColumn
appnCosTgRowEffCapMin = _AppnCosTgRowEffCapMin_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 4),
    _AppnCosTgRowEffCapMin_Type()
)
appnCosTgRowEffCapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowEffCapMin.setStatus("current")
_AppnCosTgRowEffCapMax_Type = AppnTgEffectiveCapacity
_AppnCosTgRowEffCapMax_Object = MibTableColumn
appnCosTgRowEffCapMax = _AppnCosTgRowEffCapMax_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 5),
    _AppnCosTgRowEffCapMax_Type()
)
appnCosTgRowEffCapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowEffCapMax.setStatus("current")


class _AppnCosTgRowConnCostMin_Type(Integer32):
    """Custom type appnCosTgRowConnCostMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowConnCostMin_Type.__name__ = "Integer32"
_AppnCosTgRowConnCostMin_Object = MibTableColumn
appnCosTgRowConnCostMin = _AppnCosTgRowConnCostMin_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 6),
    _AppnCosTgRowConnCostMin_Type()
)
appnCosTgRowConnCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowConnCostMin.setStatus("current")


class _AppnCosTgRowConnCostMax_Type(Integer32):
    """Custom type appnCosTgRowConnCostMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowConnCostMax_Type.__name__ = "Integer32"
_AppnCosTgRowConnCostMax_Object = MibTableColumn
appnCosTgRowConnCostMax = _AppnCosTgRowConnCostMax_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 7),
    _AppnCosTgRowConnCostMax_Type()
)
appnCosTgRowConnCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowConnCostMax.setStatus("current")


class _AppnCosTgRowByteCostMin_Type(Integer32):
    """Custom type appnCosTgRowByteCostMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowByteCostMin_Type.__name__ = "Integer32"
_AppnCosTgRowByteCostMin_Object = MibTableColumn
appnCosTgRowByteCostMin = _AppnCosTgRowByteCostMin_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 8),
    _AppnCosTgRowByteCostMin_Type()
)
appnCosTgRowByteCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowByteCostMin.setStatus("current")


class _AppnCosTgRowByteCostMax_Type(Integer32):
    """Custom type appnCosTgRowByteCostMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowByteCostMax_Type.__name__ = "Integer32"
_AppnCosTgRowByteCostMax_Object = MibTableColumn
appnCosTgRowByteCostMax = _AppnCosTgRowByteCostMax_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 9),
    _AppnCosTgRowByteCostMax_Type()
)
appnCosTgRowByteCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowByteCostMax.setStatus("current")
_AppnCosTgRowSecurityMin_Type = AppnTgSecurity
_AppnCosTgRowSecurityMin_Object = MibTableColumn
appnCosTgRowSecurityMin = _AppnCosTgRowSecurityMin_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 10),
    _AppnCosTgRowSecurityMin_Type()
)
appnCosTgRowSecurityMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowSecurityMin.setStatus("current")
_AppnCosTgRowSecurityMax_Type = AppnTgSecurity
_AppnCosTgRowSecurityMax_Object = MibTableColumn
appnCosTgRowSecurityMax = _AppnCosTgRowSecurityMax_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 11),
    _AppnCosTgRowSecurityMax_Type()
)
appnCosTgRowSecurityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowSecurityMax.setStatus("current")
_AppnCosTgRowDelayMin_Type = AppnTgDelay
_AppnCosTgRowDelayMin_Object = MibTableColumn
appnCosTgRowDelayMin = _AppnCosTgRowDelayMin_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 12),
    _AppnCosTgRowDelayMin_Type()
)
appnCosTgRowDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowDelayMin.setStatus("current")
_AppnCosTgRowDelayMax_Type = AppnTgDelay
_AppnCosTgRowDelayMax_Object = MibTableColumn
appnCosTgRowDelayMax = _AppnCosTgRowDelayMax_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 13),
    _AppnCosTgRowDelayMax_Type()
)
appnCosTgRowDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowDelayMax.setStatus("current")


class _AppnCosTgRowUsr1Min_Type(Integer32):
    """Custom type appnCosTgRowUsr1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowUsr1Min_Type.__name__ = "Integer32"
_AppnCosTgRowUsr1Min_Object = MibTableColumn
appnCosTgRowUsr1Min = _AppnCosTgRowUsr1Min_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 14),
    _AppnCosTgRowUsr1Min_Type()
)
appnCosTgRowUsr1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowUsr1Min.setStatus("current")


class _AppnCosTgRowUsr1Max_Type(Integer32):
    """Custom type appnCosTgRowUsr1Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowUsr1Max_Type.__name__ = "Integer32"
_AppnCosTgRowUsr1Max_Object = MibTableColumn
appnCosTgRowUsr1Max = _AppnCosTgRowUsr1Max_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 15),
    _AppnCosTgRowUsr1Max_Type()
)
appnCosTgRowUsr1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowUsr1Max.setStatus("current")


class _AppnCosTgRowUsr2Min_Type(Integer32):
    """Custom type appnCosTgRowUsr2Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowUsr2Min_Type.__name__ = "Integer32"
_AppnCosTgRowUsr2Min_Object = MibTableColumn
appnCosTgRowUsr2Min = _AppnCosTgRowUsr2Min_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 16),
    _AppnCosTgRowUsr2Min_Type()
)
appnCosTgRowUsr2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowUsr2Min.setStatus("current")


class _AppnCosTgRowUsr2Max_Type(Integer32):
    """Custom type appnCosTgRowUsr2Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowUsr2Max_Type.__name__ = "Integer32"
_AppnCosTgRowUsr2Max_Object = MibTableColumn
appnCosTgRowUsr2Max = _AppnCosTgRowUsr2Max_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 17),
    _AppnCosTgRowUsr2Max_Type()
)
appnCosTgRowUsr2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowUsr2Max.setStatus("current")


class _AppnCosTgRowUsr3Min_Type(Integer32):
    """Custom type appnCosTgRowUsr3Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowUsr3Min_Type.__name__ = "Integer32"
_AppnCosTgRowUsr3Min_Object = MibTableColumn
appnCosTgRowUsr3Min = _AppnCosTgRowUsr3Min_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 18),
    _AppnCosTgRowUsr3Min_Type()
)
appnCosTgRowUsr3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowUsr3Min.setStatus("current")


class _AppnCosTgRowUsr3Max_Type(Integer32):
    """Custom type appnCosTgRowUsr3Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AppnCosTgRowUsr3Max_Type.__name__ = "Integer32"
_AppnCosTgRowUsr3Max_Object = MibTableColumn
appnCosTgRowUsr3Max = _AppnCosTgRowUsr3Max_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 5, 4, 1, 19),
    _AppnCosTgRowUsr3Max_Type()
)
appnCosTgRowUsr3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnCosTgRowUsr3Max.setStatus("current")
_AppnSessIntermediate_ObjectIdentity = ObjectIdentity
appnSessIntermediate = _AppnSessIntermediate_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6)
)
_AppnIsInGlobal_ObjectIdentity = ObjectIdentity
appnIsInGlobal = _AppnIsInGlobal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1)
)


class _AppnIsInGlobeCtrAdminStatus_Type(Integer32):
    """Custom type appnIsInGlobeCtrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1),
          ("ready", 3))
    )


_AppnIsInGlobeCtrAdminStatus_Type.__name__ = "Integer32"
_AppnIsInGlobeCtrAdminStatus_Object = MibScalar
appnIsInGlobeCtrAdminStatus = _AppnIsInGlobeCtrAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1, 1),
    _AppnIsInGlobeCtrAdminStatus_Type()
)
appnIsInGlobeCtrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIsInGlobeCtrAdminStatus.setStatus("current")


class _AppnIsInGlobeCtrOperStatus_Type(Integer32):
    """Custom type appnIsInGlobeCtrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppnIsInGlobeCtrOperStatus_Type.__name__ = "Integer32"
_AppnIsInGlobeCtrOperStatus_Object = MibScalar
appnIsInGlobeCtrOperStatus = _AppnIsInGlobeCtrOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1, 2),
    _AppnIsInGlobeCtrOperStatus_Type()
)
appnIsInGlobeCtrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInGlobeCtrOperStatus.setStatus("current")
_AppnIsInGlobeCtrStatusTime_Type = TimeTicks
_AppnIsInGlobeCtrStatusTime_Object = MibScalar
appnIsInGlobeCtrStatusTime = _AppnIsInGlobeCtrStatusTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1, 3),
    _AppnIsInGlobeCtrStatusTime_Type()
)
appnIsInGlobeCtrStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInGlobeCtrStatusTime.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInGlobeCtrStatusTime.setUnits("hundredths of a second")


class _AppnIsInGlobeRscv_Type(Integer32):
    """Custom type appnIsInGlobeRscv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AppnIsInGlobeRscv_Type.__name__ = "Integer32"
_AppnIsInGlobeRscv_Object = MibScalar
appnIsInGlobeRscv = _AppnIsInGlobeRscv_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1, 4),
    _AppnIsInGlobeRscv_Type()
)
appnIsInGlobeRscv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIsInGlobeRscv.setStatus("current")
_AppnIsInGlobeRscvTime_Type = TimeTicks
_AppnIsInGlobeRscvTime_Object = MibScalar
appnIsInGlobeRscvTime = _AppnIsInGlobeRscvTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1, 5),
    _AppnIsInGlobeRscvTime_Type()
)
appnIsInGlobeRscvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInGlobeRscvTime.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInGlobeRscvTime.setUnits("hundredths of a second")
_AppnIsInGlobeActSess_Type = Gauge32
_AppnIsInGlobeActSess_Object = MibScalar
appnIsInGlobeActSess = _AppnIsInGlobeActSess_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1, 6),
    _AppnIsInGlobeActSess_Type()
)
appnIsInGlobeActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInGlobeActSess.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInGlobeActSess.setUnits("sessions")
_AppnIsInGlobeHprBfActSess_Type = Gauge32
_AppnIsInGlobeHprBfActSess_Object = MibScalar
appnIsInGlobeHprBfActSess = _AppnIsInGlobeHprBfActSess_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 1, 7),
    _AppnIsInGlobeHprBfActSess_Type()
)
appnIsInGlobeHprBfActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInGlobeHprBfActSess.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInGlobeHprBfActSess.setUnits("sessions")
_AppnIsInTable_Object = MibTable
appnIsInTable = _AppnIsInTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    appnIsInTable.setStatus("current")
_AppnIsInEntry_Object = MibTableRow
appnIsInEntry = _AppnIsInEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1)
)
appnIsInEntry.setIndexNames(
    (0, "APPN-MIB", "appnIsInFqCpName"),
    (0, "APPN-MIB", "appnIsInPcid"),
)
if mibBuilder.loadTexts:
    appnIsInEntry.setStatus("current")
_AppnIsInFqCpName_Type = SnaControlPointName
_AppnIsInFqCpName_Object = MibTableColumn
appnIsInFqCpName = _AppnIsInFqCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 1),
    _AppnIsInFqCpName_Type()
)
appnIsInFqCpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsInFqCpName.setStatus("current")


class _AppnIsInPcid_Type(OctetString):
    """Custom type appnIsInPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AppnIsInPcid_Type.__name__ = "OctetString"
_AppnIsInPcid_Object = MibTableColumn
appnIsInPcid = _AppnIsInPcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 2),
    _AppnIsInPcid_Type()
)
appnIsInPcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsInPcid.setStatus("current")


class _AppnIsInSessState_Type(Integer32):
    """Custom type appnIsInSessState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_AppnIsInSessState_Type.__name__ = "Integer32"
_AppnIsInSessState_Object = MibTableColumn
appnIsInSessState = _AppnIsInSessState_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 3),
    _AppnIsInSessState_Type()
)
appnIsInSessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appnIsInSessState.setStatus("current")


class _AppnIsInPriLuName_Type(DisplayString):
    """Custom type appnIsInPriLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnIsInPriLuName_Type.__name__ = "DisplayString"
_AppnIsInPriLuName_Object = MibTableColumn
appnIsInPriLuName = _AppnIsInPriLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 4),
    _AppnIsInPriLuName_Type()
)
appnIsInPriLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPriLuName.setStatus("current")


class _AppnIsInSecLuName_Type(DisplayString):
    """Custom type appnIsInSecLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AppnIsInSecLuName_Type.__name__ = "DisplayString"
_AppnIsInSecLuName_Object = MibTableColumn
appnIsInSecLuName = _AppnIsInSecLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 5),
    _AppnIsInSecLuName_Type()
)
appnIsInSecLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSecLuName.setStatus("current")
_AppnIsInModeName_Type = SnaModeName
_AppnIsInModeName_Object = MibTableColumn
appnIsInModeName = _AppnIsInModeName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 6),
    _AppnIsInModeName_Type()
)
appnIsInModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInModeName.setStatus("current")
_AppnIsInCosName_Type = SnaClassOfServiceName
_AppnIsInCosName_Object = MibTableColumn
appnIsInCosName = _AppnIsInCosName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 7),
    _AppnIsInCosName_Type()
)
appnIsInCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInCosName.setStatus("current")


class _AppnIsInTransPriority_Type(Integer32):
    """Custom type appnIsInTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_AppnIsInTransPriority_Type.__name__ = "Integer32"
_AppnIsInTransPriority_Object = MibTableColumn
appnIsInTransPriority = _AppnIsInTransPriority_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 8),
    _AppnIsInTransPriority_Type()
)
appnIsInTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInTransPriority.setStatus("current")


class _AppnIsInSessType_Type(Integer32):
    """Custom type appnIsInSessType based on Integer32"""
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
        *(("lu0thru3", 3),
          ("lu0thru3dlur", 5),
          ("lu62", 2),
          ("lu62dlur", 4),
          ("unknown", 1))
    )


_AppnIsInSessType_Type.__name__ = "Integer32"
_AppnIsInSessType_Object = MibTableColumn
appnIsInSessType = _AppnIsInSessType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 9),
    _AppnIsInSessType_Type()
)
appnIsInSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSessType.setStatus("current")
_AppnIsInSessUpTime_Type = TimeTicks
_AppnIsInSessUpTime_Object = MibTableColumn
appnIsInSessUpTime = _AppnIsInSessUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 10),
    _AppnIsInSessUpTime_Type()
)
appnIsInSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSessUpTime.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInSessUpTime.setUnits("hundredths of a second")
_AppnIsInCtrUpTime_Type = TimeTicks
_AppnIsInCtrUpTime_Object = MibTableColumn
appnIsInCtrUpTime = _AppnIsInCtrUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 11),
    _AppnIsInCtrUpTime_Type()
)
appnIsInCtrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInCtrUpTime.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInCtrUpTime.setUnits("hundredths of a second")
_AppnIsInP2SFmdPius_Type = Unsigned32
_AppnIsInP2SFmdPius_Object = MibTableColumn
appnIsInP2SFmdPius = _AppnIsInP2SFmdPius_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 12),
    _AppnIsInP2SFmdPius_Type()
)
appnIsInP2SFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInP2SFmdPius.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInP2SFmdPius.setUnits("path information units (PIUs)")
_AppnIsInS2PFmdPius_Type = Unsigned32
_AppnIsInS2PFmdPius_Object = MibTableColumn
appnIsInS2PFmdPius = _AppnIsInS2PFmdPius_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 13),
    _AppnIsInS2PFmdPius_Type()
)
appnIsInS2PFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInS2PFmdPius.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInS2PFmdPius.setUnits("path information units (PIUs)")
_AppnIsInP2SNonFmdPius_Type = Unsigned32
_AppnIsInP2SNonFmdPius_Object = MibTableColumn
appnIsInP2SNonFmdPius = _AppnIsInP2SNonFmdPius_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 14),
    _AppnIsInP2SNonFmdPius_Type()
)
appnIsInP2SNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInP2SNonFmdPius.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInP2SNonFmdPius.setUnits("path information units (PIUs)")
_AppnIsInS2PNonFmdPius_Type = Unsigned32
_AppnIsInS2PNonFmdPius_Object = MibTableColumn
appnIsInS2PNonFmdPius = _AppnIsInS2PNonFmdPius_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 15),
    _AppnIsInS2PNonFmdPius_Type()
)
appnIsInS2PNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInS2PNonFmdPius.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInS2PNonFmdPius.setUnits("path information units (PIUs)")
_AppnIsInP2SFmdBytes_Type = Unsigned32
_AppnIsInP2SFmdBytes_Object = MibTableColumn
appnIsInP2SFmdBytes = _AppnIsInP2SFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 16),
    _AppnIsInP2SFmdBytes_Type()
)
appnIsInP2SFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInP2SFmdBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInP2SFmdBytes.setUnits("bytes")
_AppnIsInS2PFmdBytes_Type = Unsigned32
_AppnIsInS2PFmdBytes_Object = MibTableColumn
appnIsInS2PFmdBytes = _AppnIsInS2PFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 17),
    _AppnIsInS2PFmdBytes_Type()
)
appnIsInS2PFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInS2PFmdBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInS2PFmdBytes.setUnits("bytes")
_AppnIsInP2SNonFmdBytes_Type = Unsigned32
_AppnIsInP2SNonFmdBytes_Object = MibTableColumn
appnIsInP2SNonFmdBytes = _AppnIsInP2SNonFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 18),
    _AppnIsInP2SNonFmdBytes_Type()
)
appnIsInP2SNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInP2SNonFmdBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInP2SNonFmdBytes.setUnits("bytes")
_AppnIsInS2PNonFmdBytes_Type = Unsigned32
_AppnIsInS2PNonFmdBytes_Object = MibTableColumn
appnIsInS2PNonFmdBytes = _AppnIsInS2PNonFmdBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 19),
    _AppnIsInS2PNonFmdBytes_Type()
)
appnIsInS2PNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInS2PNonFmdBytes.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInS2PNonFmdBytes.setUnits("bytes")
_AppnIsInPsAdjCpName_Type = SnaControlPointName
_AppnIsInPsAdjCpName_Object = MibTableColumn
appnIsInPsAdjCpName = _AppnIsInPsAdjCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 20),
    _AppnIsInPsAdjCpName_Type()
)
appnIsInPsAdjCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsAdjCpName.setStatus("current")


class _AppnIsInPsAdjTgNum_Type(Integer32):
    """Custom type appnIsInPsAdjTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AppnIsInPsAdjTgNum_Type.__name__ = "Integer32"
_AppnIsInPsAdjTgNum_Object = MibTableColumn
appnIsInPsAdjTgNum = _AppnIsInPsAdjTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 21),
    _AppnIsInPsAdjTgNum_Type()
)
appnIsInPsAdjTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsAdjTgNum.setStatus("current")


class _AppnIsInPsSendMaxBtuSize_Type(Integer32):
    """Custom type appnIsInPsSendMaxBtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32767),
    )


_AppnIsInPsSendMaxBtuSize_Type.__name__ = "Integer32"
_AppnIsInPsSendMaxBtuSize_Object = MibTableColumn
appnIsInPsSendMaxBtuSize = _AppnIsInPsSendMaxBtuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 22),
    _AppnIsInPsSendMaxBtuSize_Type()
)
appnIsInPsSendMaxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsSendMaxBtuSize.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInPsSendMaxBtuSize.setUnits("bytes")


class _AppnIsInPsSendPacingType_Type(Integer32):
    """Custom type appnIsInPsSendPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_AppnIsInPsSendPacingType_Type.__name__ = "Integer32"
_AppnIsInPsSendPacingType_Object = MibTableColumn
appnIsInPsSendPacingType = _AppnIsInPsSendPacingType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 23),
    _AppnIsInPsSendPacingType_Type()
)
appnIsInPsSendPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsSendPacingType.setStatus("current")
_AppnIsInPsSendRpc_Type = Gauge32
_AppnIsInPsSendRpc_Object = MibTableColumn
appnIsInPsSendRpc = _AppnIsInPsSendRpc_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 24),
    _AppnIsInPsSendRpc_Type()
)
appnIsInPsSendRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsSendRpc.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInPsSendRpc.setUnits("message units (MUs)")
_AppnIsInPsSendNxWndwSize_Type = Gauge32
_AppnIsInPsSendNxWndwSize_Object = MibTableColumn
appnIsInPsSendNxWndwSize = _AppnIsInPsSendNxWndwSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 25),
    _AppnIsInPsSendNxWndwSize_Type()
)
appnIsInPsSendNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsSendNxWndwSize.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInPsSendNxWndwSize.setUnits("message units (MUs)")


class _AppnIsInPsRecvPacingType_Type(Integer32):
    """Custom type appnIsInPsRecvPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_AppnIsInPsRecvPacingType_Type.__name__ = "Integer32"
_AppnIsInPsRecvPacingType_Object = MibTableColumn
appnIsInPsRecvPacingType = _AppnIsInPsRecvPacingType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 26),
    _AppnIsInPsRecvPacingType_Type()
)
appnIsInPsRecvPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsRecvPacingType.setStatus("current")
_AppnIsInPsRecvRpc_Type = Gauge32
_AppnIsInPsRecvRpc_Object = MibTableColumn
appnIsInPsRecvRpc = _AppnIsInPsRecvRpc_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 27),
    _AppnIsInPsRecvRpc_Type()
)
appnIsInPsRecvRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsRecvRpc.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInPsRecvRpc.setUnits("message units (MUs)")
_AppnIsInPsRecvNxWndwSize_Type = Gauge32
_AppnIsInPsRecvNxWndwSize_Object = MibTableColumn
appnIsInPsRecvNxWndwSize = _AppnIsInPsRecvNxWndwSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 28),
    _AppnIsInPsRecvNxWndwSize_Type()
)
appnIsInPsRecvNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInPsRecvNxWndwSize.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInPsRecvNxWndwSize.setUnits("message units (MUs)")
_AppnIsInSsAdjCpName_Type = SnaControlPointName
_AppnIsInSsAdjCpName_Object = MibTableColumn
appnIsInSsAdjCpName = _AppnIsInSsAdjCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 29),
    _AppnIsInSsAdjCpName_Type()
)
appnIsInSsAdjCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsAdjCpName.setStatus("current")


class _AppnIsInSsAdjTgNum_Type(Integer32):
    """Custom type appnIsInSsAdjTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AppnIsInSsAdjTgNum_Type.__name__ = "Integer32"
_AppnIsInSsAdjTgNum_Object = MibTableColumn
appnIsInSsAdjTgNum = _AppnIsInSsAdjTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 30),
    _AppnIsInSsAdjTgNum_Type()
)
appnIsInSsAdjTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsAdjTgNum.setStatus("current")


class _AppnIsInSsSendMaxBtuSize_Type(Integer32):
    """Custom type appnIsInSsSendMaxBtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 32767),
    )


_AppnIsInSsSendMaxBtuSize_Type.__name__ = "Integer32"
_AppnIsInSsSendMaxBtuSize_Object = MibTableColumn
appnIsInSsSendMaxBtuSize = _AppnIsInSsSendMaxBtuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 31),
    _AppnIsInSsSendMaxBtuSize_Type()
)
appnIsInSsSendMaxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsSendMaxBtuSize.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInSsSendMaxBtuSize.setUnits("bytes")


class _AppnIsInSsSendPacingType_Type(Integer32):
    """Custom type appnIsInSsSendPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_AppnIsInSsSendPacingType_Type.__name__ = "Integer32"
_AppnIsInSsSendPacingType_Object = MibTableColumn
appnIsInSsSendPacingType = _AppnIsInSsSendPacingType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 32),
    _AppnIsInSsSendPacingType_Type()
)
appnIsInSsSendPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsSendPacingType.setStatus("current")
_AppnIsInSsSendRpc_Type = Gauge32
_AppnIsInSsSendRpc_Object = MibTableColumn
appnIsInSsSendRpc = _AppnIsInSsSendRpc_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 33),
    _AppnIsInSsSendRpc_Type()
)
appnIsInSsSendRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsSendRpc.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInSsSendRpc.setUnits("message units (MUs)")
_AppnIsInSsSendNxWndwSize_Type = Gauge32
_AppnIsInSsSendNxWndwSize_Object = MibTableColumn
appnIsInSsSendNxWndwSize = _AppnIsInSsSendNxWndwSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 34),
    _AppnIsInSsSendNxWndwSize_Type()
)
appnIsInSsSendNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsSendNxWndwSize.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInSsSendNxWndwSize.setUnits("message units (MUs)")


class _AppnIsInSsRecvPacingType_Type(Integer32):
    """Custom type appnIsInSsRecvPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_AppnIsInSsRecvPacingType_Type.__name__ = "Integer32"
_AppnIsInSsRecvPacingType_Object = MibTableColumn
appnIsInSsRecvPacingType = _AppnIsInSsRecvPacingType_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 35),
    _AppnIsInSsRecvPacingType_Type()
)
appnIsInSsRecvPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsRecvPacingType.setStatus("current")
_AppnIsInSsRecvRpc_Type = Gauge32
_AppnIsInSsRecvRpc_Object = MibTableColumn
appnIsInSsRecvRpc = _AppnIsInSsRecvRpc_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 36),
    _AppnIsInSsRecvRpc_Type()
)
appnIsInSsRecvRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsRecvRpc.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInSsRecvRpc.setUnits("message units (MUs)")
_AppnIsInSsRecvNxWndwSize_Type = Gauge32
_AppnIsInSsRecvNxWndwSize_Object = MibTableColumn
appnIsInSsRecvNxWndwSize = _AppnIsInSsRecvNxWndwSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 37),
    _AppnIsInSsRecvNxWndwSize_Type()
)
appnIsInSsRecvNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInSsRecvNxWndwSize.setStatus("current")
if mibBuilder.loadTexts:
    appnIsInSsRecvNxWndwSize.setUnits("message units (MUs)")


class _AppnIsInRouteInfo_Type(OctetString):
    """Custom type appnIsInRouteInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AppnIsInRouteInfo_Type.__name__ = "OctetString"
_AppnIsInRouteInfo_Object = MibTableColumn
appnIsInRouteInfo = _AppnIsInRouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 38),
    _AppnIsInRouteInfo_Type()
)
appnIsInRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInRouteInfo.setStatus("current")


class _AppnIsInRtpNceId_Type(OctetString):
    """Custom type appnIsInRtpNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnIsInRtpNceId_Type.__name__ = "OctetString"
_AppnIsInRtpNceId_Object = MibTableColumn
appnIsInRtpNceId = _AppnIsInRtpNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 39),
    _AppnIsInRtpNceId_Type()
)
appnIsInRtpNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInRtpNceId.setStatus("current")


class _AppnIsInRtpTcid_Type(OctetString):
    """Custom type appnIsInRtpTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AppnIsInRtpTcid_Type.__name__ = "OctetString"
_AppnIsInRtpTcid_Object = MibTableColumn
appnIsInRtpTcid = _AppnIsInRtpTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 2, 1, 40),
    _AppnIsInRtpTcid_Type()
)
appnIsInRtpTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsInRtpTcid.setStatus("current")
_AppnIsRtpTable_Object = MibTable
appnIsRtpTable = _AppnIsRtpTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    appnIsRtpTable.setStatus("current")
_AppnIsRtpEntry_Object = MibTableRow
appnIsRtpEntry = _AppnIsRtpEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 3, 1)
)
appnIsRtpEntry.setIndexNames(
    (0, "APPN-MIB", "appnIsRtpNceId"),
    (0, "APPN-MIB", "appnIsRtpTcid"),
)
if mibBuilder.loadTexts:
    appnIsRtpEntry.setStatus("current")


class _AppnIsRtpNceId_Type(OctetString):
    """Custom type appnIsRtpNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AppnIsRtpNceId_Type.__name__ = "OctetString"
_AppnIsRtpNceId_Object = MibTableColumn
appnIsRtpNceId = _AppnIsRtpNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 3, 1, 1),
    _AppnIsRtpNceId_Type()
)
appnIsRtpNceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsRtpNceId.setStatus("current")


class _AppnIsRtpTcid_Type(OctetString):
    """Custom type appnIsRtpTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AppnIsRtpTcid_Type.__name__ = "OctetString"
_AppnIsRtpTcid_Object = MibTableColumn
appnIsRtpTcid = _AppnIsRtpTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 3, 1, 2),
    _AppnIsRtpTcid_Type()
)
appnIsRtpTcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appnIsRtpTcid.setStatus("current")
_AppnIsRtpSessions_Type = Gauge32
_AppnIsRtpSessions_Object = MibTableColumn
appnIsRtpSessions = _AppnIsRtpSessions_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 1, 6, 3, 1, 3),
    _AppnIsRtpSessions_Type()
)
appnIsRtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appnIsRtpSessions.setStatus("current")
if mibBuilder.loadTexts:
    appnIsRtpSessions.setUnits("sessions")
_AppnTraps_ObjectIdentity = ObjectIdentity
appnTraps = _AppnTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 2)
)


class _AlertIdNumber_Type(OctetString):
    """Custom type alertIdNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AlertIdNumber_Type.__name__ = "OctetString"
_AlertIdNumber_Object = MibScalar
alertIdNumber = _AlertIdNumber_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 2, 2),
    _AlertIdNumber_Type()
)
alertIdNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertIdNumber.setStatus("current")
_AffectedObject_Type = VariablePointer
_AffectedObject_Object = MibScalar
affectedObject = _AffectedObject_Object(
    (1, 3, 6, 1, 2, 1, 34, 4, 2, 3),
    _AffectedObject_Type()
)
affectedObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    affectedObject.setStatus("current")
_AppnConformance_ObjectIdentity = ObjectIdentity
appnConformance = _AppnConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 3)
)
_AppnCompliances_ObjectIdentity = ObjectIdentity
appnCompliances = _AppnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 1)
)
_AppnGroups_ObjectIdentity = ObjectIdentity
appnGroups = _AppnGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2)
)

# Managed Objects groups

appnGeneralConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 1)
)
appnGeneralConfGroup.setObjects(
      *(("APPN-MIB", "appnNodeCpName"),
        ("APPN-MIB", "appnNodeMibVersion"),
        ("APPN-MIB", "appnNodeId"),
        ("APPN-MIB", "appnNodeType"),
        ("APPN-MIB", "appnNodeUpTime"),
        ("APPN-MIB", "appnNodeParallelTg"),
        ("APPN-MIB", "appnNodeAdaptiveBindPacing"),
        ("APPN-MIB", "appnNodeHprSupport"),
        ("APPN-MIB", "appnNodeCounterDisconTime"))
)
if mibBuilder.loadTexts:
    appnGeneralConfGroup.setStatus("deprecated")

appnPortConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 2)
)
appnPortConfGroup.setObjects(
      *(("APPN-MIB", "appnPortCommand"),
        ("APPN-MIB", "appnPortOperState"),
        ("APPN-MIB", "appnPortDlcType"),
        ("APPN-MIB", "appnPortPortType"),
        ("APPN-MIB", "appnPortSIMRIM"),
        ("APPN-MIB", "appnPortLsRole"),
        ("APPN-MIB", "appnPortNegotLs"),
        ("APPN-MIB", "appnPortDynamicLinkSupport"),
        ("APPN-MIB", "appnPortMaxRcvBtuSize"),
        ("APPN-MIB", "appnPortMaxIframeWindow"),
        ("APPN-MIB", "appnPortDefLsGoodXids"),
        ("APPN-MIB", "appnPortDefLsBadXids"),
        ("APPN-MIB", "appnPortDynLsGoodXids"),
        ("APPN-MIB", "appnPortDynLsBadXids"),
        ("APPN-MIB", "appnPortSpecific"),
        ("APPN-MIB", "appnPortDlcLocalAddr"),
        ("APPN-MIB", "appnPortCounterDisconTime"))
)
if mibBuilder.loadTexts:
    appnPortConfGroup.setStatus("current")

appnLinkConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 3)
)
appnLinkConfGroup.setObjects(
      *(("APPN-MIB", "appnLsCommand"),
        ("APPN-MIB", "appnLsOperState"),
        ("APPN-MIB", "appnLsPortName"),
        ("APPN-MIB", "appnLsDlcType"),
        ("APPN-MIB", "appnLsDynamic"),
        ("APPN-MIB", "appnLsAdjCpName"),
        ("APPN-MIB", "appnLsAdjNodeType"),
        ("APPN-MIB", "appnLsTgNum"),
        ("APPN-MIB", "appnLsLimResource"),
        ("APPN-MIB", "appnLsActOnDemand"),
        ("APPN-MIB", "appnLsMigration"),
        ("APPN-MIB", "appnLsPartnerNodeId"),
        ("APPN-MIB", "appnLsCpCpSessionSupport"),
        ("APPN-MIB", "appnLsMaxSendBtuSize"),
        ("APPN-MIB", "appnLsInXidBytes"),
        ("APPN-MIB", "appnLsInMsgBytes"),
        ("APPN-MIB", "appnLsInXidFrames"),
        ("APPN-MIB", "appnLsInMsgFrames"),
        ("APPN-MIB", "appnLsOutXidBytes"),
        ("APPN-MIB", "appnLsOutMsgBytes"),
        ("APPN-MIB", "appnLsOutXidFrames"),
        ("APPN-MIB", "appnLsOutMsgFrames"),
        ("APPN-MIB", "appnLsEchoRsps"),
        ("APPN-MIB", "appnLsCurrentDelay"),
        ("APPN-MIB", "appnLsMaxDelay"),
        ("APPN-MIB", "appnLsMinDelay"),
        ("APPN-MIB", "appnLsMaxDelayTime"),
        ("APPN-MIB", "appnLsGoodXids"),
        ("APPN-MIB", "appnLsBadXids"),
        ("APPN-MIB", "appnLsSpecific"),
        ("APPN-MIB", "appnLsActiveTime"),
        ("APPN-MIB", "appnLsCurrentStateTime"),
        ("APPN-MIB", "appnLsHprSup"),
        ("APPN-MIB", "appnLsLocalAddr"),
        ("APPN-MIB", "appnLsRemoteAddr"),
        ("APPN-MIB", "appnLsRemoteLsName"),
        ("APPN-MIB", "appnLsStatusTime"),
        ("APPN-MIB", "appnLsStatusLsName"),
        ("APPN-MIB", "appnLsStatusCpName"),
        ("APPN-MIB", "appnLsStatusPartnerId"),
        ("APPN-MIB", "appnLsStatusTgNum"),
        ("APPN-MIB", "appnLsStatusGeneralSense"),
        ("APPN-MIB", "appnLsStatusRetry"),
        ("APPN-MIB", "appnLsStatusEndSense"),
        ("APPN-MIB", "appnLsStatusXidLocalSense"),
        ("APPN-MIB", "appnLsStatusXidRemoteSense"),
        ("APPN-MIB", "appnLsStatusXidByteInError"),
        ("APPN-MIB", "appnLsStatusXidBitInError"),
        ("APPN-MIB", "appnLsStatusDlcType"),
        ("APPN-MIB", "appnLsStatusLocalAddr"),
        ("APPN-MIB", "appnLsStatusRemoteAddr"),
        ("APPN-MIB", "appnLsCounterDisconTime"))
)
if mibBuilder.loadTexts:
    appnLinkConfGroup.setStatus("deprecated")

appnLocalTgConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 4)
)
appnLocalTgConfGroup.setObjects(
      *(("APPN-MIB", "appnLocalTgDestVirtual"),
        ("APPN-MIB", "appnLocalTgDlcData"),
        ("APPN-MIB", "appnLocalTgPortName"),
        ("APPN-MIB", "appnLocalTgQuiescing"),
        ("APPN-MIB", "appnLocalTgOperational"),
        ("APPN-MIB", "appnLocalTgCpCpSession"),
        ("APPN-MIB", "appnLocalTgEffCap"),
        ("APPN-MIB", "appnLocalTgConnCost"),
        ("APPN-MIB", "appnLocalTgByteCost"),
        ("APPN-MIB", "appnLocalTgSecurity"),
        ("APPN-MIB", "appnLocalTgDelay"),
        ("APPN-MIB", "appnLocalTgUsr1"),
        ("APPN-MIB", "appnLocalTgUsr2"),
        ("APPN-MIB", "appnLocalTgUsr3"),
        ("APPN-MIB", "appnLocalTgHprSup"),
        ("APPN-MIB", "appnLocalTgIntersubnet"))
)
if mibBuilder.loadTexts:
    appnLocalTgConfGroup.setStatus("deprecated")

appnDirTableConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 5)
)
appnDirTableConfGroup.setObjects(
      *(("APPN-MIB", "appnDirNnServerName"),
        ("APPN-MIB", "appnDirLuOwnerName"),
        ("APPN-MIB", "appnDirLuLocation"),
        ("APPN-MIB", "appnDirType"))
)
if mibBuilder.loadTexts:
    appnDirTableConfGroup.setStatus("deprecated")

appnNnUniqueConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 6)
)
appnNnUniqueConfGroup.setObjects(
      *(("APPN-MIB", "appnNodeNnCentralDirectory"),
        ("APPN-MIB", "appnNodeNnTreeCache"),
        ("APPN-MIB", "appnNodeNnRouteAddResist"),
        ("APPN-MIB", "appnNodeNnIsr"),
        ("APPN-MIB", "appnNodeNnFrsn"),
        ("APPN-MIB", "appnNodeNnPeriBorderSup"),
        ("APPN-MIB", "appnNodeNnInterchangeSup"),
        ("APPN-MIB", "appnNodeNnExteBorderSup"),
        ("APPN-MIB", "appnNodeNnSafeStoreFreq"),
        ("APPN-MIB", "appnNodeNnRsn"),
        ("APPN-MIB", "appnNodeNnCongested"),
        ("APPN-MIB", "appnNodeNnIsrDepleted"),
        ("APPN-MIB", "appnNodeNnQuiescing"),
        ("APPN-MIB", "appnNodeNnGateway"))
)
if mibBuilder.loadTexts:
    appnNnUniqueConfGroup.setStatus("current")

appnEnUniqueConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 7)
)
appnEnUniqueConfGroup.setObjects(
      *(("APPN-MIB", "appnNodeEnModeCosMap"),
        ("APPN-MIB", "appnNodeEnNnServer"),
        ("APPN-MIB", "appnNodeEnLuSearch"))
)
if mibBuilder.loadTexts:
    appnEnUniqueConfGroup.setStatus("current")

appnVrnConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 8)
)
appnVrnConfGroup.setObjects(
    ("APPN-MIB", "appnVrnPortName")
)
if mibBuilder.loadTexts:
    appnVrnConfGroup.setStatus("current")

appnNnTopoConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 9)
)
appnNnTopoConfGroup.setObjects(
      *(("APPN-MIB", "appnNnTopoMaxNodes"),
        ("APPN-MIB", "appnNnTopoCurNumNodes"),
        ("APPN-MIB", "appnNnTopoNodePurges"),
        ("APPN-MIB", "appnNnTopoTgPurges"),
        ("APPN-MIB", "appnNnTopoTotalTduWars"),
        ("APPN-MIB", "appnNnNodeFREntryTimeLeft"),
        ("APPN-MIB", "appnNnNodeFRType"),
        ("APPN-MIB", "appnNnNodeFRRsn"),
        ("APPN-MIB", "appnNnNodeFRRouteAddResist"),
        ("APPN-MIB", "appnNnNodeFRCongested"),
        ("APPN-MIB", "appnNnNodeFRIsrDepleted"),
        ("APPN-MIB", "appnNnNodeFRQuiescing"),
        ("APPN-MIB", "appnNnNodeFRGateway"),
        ("APPN-MIB", "appnNnNodeFRCentralDirectory"),
        ("APPN-MIB", "appnNnNodeFRIsr"),
        ("APPN-MIB", "appnNnNodeFRGarbageCollect"),
        ("APPN-MIB", "appnNnNodeFRHprSupport"),
        ("APPN-MIB", "appnNnNodeFRPeriBorderSup"),
        ("APPN-MIB", "appnNnNodeFRInterchangeSup"),
        ("APPN-MIB", "appnNnNodeFRExteBorderSup"),
        ("APPN-MIB", "appnNnTgFREntryTimeLeft"),
        ("APPN-MIB", "appnNnTgFRDestVirtual"),
        ("APPN-MIB", "appnNnTgFRDlcData"),
        ("APPN-MIB", "appnNnTgFRRsn"),
        ("APPN-MIB", "appnNnTgFROperational"),
        ("APPN-MIB", "appnNnTgFRQuiescing"),
        ("APPN-MIB", "appnNnTgFRCpCpSession"),
        ("APPN-MIB", "appnNnTgFREffCap"),
        ("APPN-MIB", "appnNnTgFRConnCost"),
        ("APPN-MIB", "appnNnTgFRByteCost"),
        ("APPN-MIB", "appnNnTgFRSecurity"),
        ("APPN-MIB", "appnNnTgFRDelay"),
        ("APPN-MIB", "appnNnTgFRUsr1"),
        ("APPN-MIB", "appnNnTgFRUsr2"),
        ("APPN-MIB", "appnNnTgFRUsr3"),
        ("APPN-MIB", "appnNnTgFRGarbageCollect"),
        ("APPN-MIB", "appnNnTgFRSubareaNum"),
        ("APPN-MIB", "appnNnTgFRHprSup"),
        ("APPN-MIB", "appnNnTgFRDestHprTrans"),
        ("APPN-MIB", "appnNnTgFRTypeIndicator"),
        ("APPN-MIB", "appnNnTgFRIntersubnet"))
)
if mibBuilder.loadTexts:
    appnNnTopoConfGroup.setStatus("deprecated")

appnLocalEnTopoConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 10)
)
appnLocalEnTopoConfGroup.setObjects(
      *(("APPN-MIB", "appnLocalEnTgEntryTimeLeft"),
        ("APPN-MIB", "appnLocalEnTgDestVirtual"),
        ("APPN-MIB", "appnLocalEnTgDlcData"),
        ("APPN-MIB", "appnLocalEnTgOperational"),
        ("APPN-MIB", "appnLocalEnTgCpCpSession"),
        ("APPN-MIB", "appnLocalEnTgEffCap"),
        ("APPN-MIB", "appnLocalEnTgConnCost"),
        ("APPN-MIB", "appnLocalEnTgByteCost"),
        ("APPN-MIB", "appnLocalEnTgSecurity"),
        ("APPN-MIB", "appnLocalEnTgDelay"),
        ("APPN-MIB", "appnLocalEnTgUsr1"),
        ("APPN-MIB", "appnLocalEnTgUsr2"),
        ("APPN-MIB", "appnLocalEnTgUsr3"))
)
if mibBuilder.loadTexts:
    appnLocalEnTopoConfGroup.setStatus("deprecated")

appnLocalDirPerfConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 11)
)
appnLocalDirPerfConfGroup.setObjects(
      *(("APPN-MIB", "appnDirMaxCaches"),
        ("APPN-MIB", "appnDirCurCaches"),
        ("APPN-MIB", "appnDirCurHomeEntries"),
        ("APPN-MIB", "appnDirRegEntries"),
        ("APPN-MIB", "appnDirInLocates"),
        ("APPN-MIB", "appnDirInBcastLocates"),
        ("APPN-MIB", "appnDirOutLocates"),
        ("APPN-MIB", "appnDirOutBcastLocates"),
        ("APPN-MIB", "appnDirNotFoundLocates"),
        ("APPN-MIB", "appnDirNotFoundBcastLocates"),
        ("APPN-MIB", "appnDirLocateOutstands"))
)
if mibBuilder.loadTexts:
    appnLocalDirPerfConfGroup.setStatus("current")

appnCosConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 12)
)
appnCosConfGroup.setObjects(
      *(("APPN-MIB", "appnCosModeCosName"),
        ("APPN-MIB", "appnCosTransPriority"),
        ("APPN-MIB", "appnCosNodeRowWgt"),
        ("APPN-MIB", "appnCosNodeRowResistMin"),
        ("APPN-MIB", "appnCosNodeRowResistMax"),
        ("APPN-MIB", "appnCosNodeRowMinCongestAllow"),
        ("APPN-MIB", "appnCosNodeRowMaxCongestAllow"),
        ("APPN-MIB", "appnCosTgRowWgt"),
        ("APPN-MIB", "appnCosTgRowEffCapMin"),
        ("APPN-MIB", "appnCosTgRowEffCapMax"),
        ("APPN-MIB", "appnCosTgRowConnCostMin"),
        ("APPN-MIB", "appnCosTgRowConnCostMax"),
        ("APPN-MIB", "appnCosTgRowByteCostMin"),
        ("APPN-MIB", "appnCosTgRowByteCostMax"),
        ("APPN-MIB", "appnCosTgRowSecurityMin"),
        ("APPN-MIB", "appnCosTgRowSecurityMax"),
        ("APPN-MIB", "appnCosTgRowDelayMin"),
        ("APPN-MIB", "appnCosTgRowDelayMax"),
        ("APPN-MIB", "appnCosTgRowUsr1Min"),
        ("APPN-MIB", "appnCosTgRowUsr1Max"),
        ("APPN-MIB", "appnCosTgRowUsr2Min"),
        ("APPN-MIB", "appnCosTgRowUsr2Max"),
        ("APPN-MIB", "appnCosTgRowUsr3Min"),
        ("APPN-MIB", "appnCosTgRowUsr3Max"))
)
if mibBuilder.loadTexts:
    appnCosConfGroup.setStatus("current")

appnIntSessConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 13)
)
appnIntSessConfGroup.setObjects(
      *(("APPN-MIB", "appnIsInGlobeCtrAdminStatus"),
        ("APPN-MIB", "appnIsInGlobeCtrOperStatus"),
        ("APPN-MIB", "appnIsInGlobeCtrStatusTime"),
        ("APPN-MIB", "appnIsInGlobeRscv"),
        ("APPN-MIB", "appnIsInGlobeRscvTime"),
        ("APPN-MIB", "appnIsInGlobeActSess"),
        ("APPN-MIB", "appnIsInSessState"),
        ("APPN-MIB", "appnIsInPriLuName"),
        ("APPN-MIB", "appnIsInSecLuName"),
        ("APPN-MIB", "appnIsInModeName"),
        ("APPN-MIB", "appnIsInCosName"),
        ("APPN-MIB", "appnIsInTransPriority"),
        ("APPN-MIB", "appnIsInSessType"),
        ("APPN-MIB", "appnIsInSessUpTime"),
        ("APPN-MIB", "appnIsInCtrUpTime"),
        ("APPN-MIB", "appnIsInP2SFmdPius"),
        ("APPN-MIB", "appnIsInS2PFmdPius"),
        ("APPN-MIB", "appnIsInP2SNonFmdPius"),
        ("APPN-MIB", "appnIsInS2PNonFmdPius"),
        ("APPN-MIB", "appnIsInP2SFmdBytes"),
        ("APPN-MIB", "appnIsInS2PFmdBytes"),
        ("APPN-MIB", "appnIsInP2SNonFmdBytes"),
        ("APPN-MIB", "appnIsInS2PNonFmdBytes"),
        ("APPN-MIB", "appnIsInPsAdjCpName"),
        ("APPN-MIB", "appnIsInPsAdjTgNum"),
        ("APPN-MIB", "appnIsInPsSendMaxBtuSize"),
        ("APPN-MIB", "appnIsInPsSendPacingType"),
        ("APPN-MIB", "appnIsInPsSendRpc"),
        ("APPN-MIB", "appnIsInPsSendNxWndwSize"),
        ("APPN-MIB", "appnIsInPsRecvPacingType"),
        ("APPN-MIB", "appnIsInPsRecvRpc"),
        ("APPN-MIB", "appnIsInPsRecvNxWndwSize"),
        ("APPN-MIB", "appnIsInSsAdjCpName"),
        ("APPN-MIB", "appnIsInSsAdjTgNum"),
        ("APPN-MIB", "appnIsInSsSendMaxBtuSize"),
        ("APPN-MIB", "appnIsInSsSendPacingType"),
        ("APPN-MIB", "appnIsInSsSendRpc"),
        ("APPN-MIB", "appnIsInSsSendNxWndwSize"),
        ("APPN-MIB", "appnIsInSsRecvPacingType"),
        ("APPN-MIB", "appnIsInSsRecvRpc"),
        ("APPN-MIB", "appnIsInSsRecvNxWndwSize"),
        ("APPN-MIB", "appnIsInRouteInfo"))
)
if mibBuilder.loadTexts:
    appnIntSessConfGroup.setStatus("current")

appnHprBaseConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 14)
)
appnHprBaseConfGroup.setObjects(
      *(("APPN-MIB", "appnNodeHprIntRteSetups"),
        ("APPN-MIB", "appnNodeHprIntRteRejects"),
        ("APPN-MIB", "appnLsErrRecoSup"),
        ("APPN-MIB", "appnLsForAnrLabel"),
        ("APPN-MIB", "appnLsRevAnrLabel"))
)
if mibBuilder.loadTexts:
    appnHprBaseConfGroup.setStatus("current")

appnHprRtpConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 15)
)
appnHprRtpConfGroup.setObjects(
      *(("APPN-MIB", "appnNodeMaxSessPerRtpConn"),
        ("APPN-MIB", "appnNodeHprOrgRteSetups"),
        ("APPN-MIB", "appnNodeHprOrgRteRejects"),
        ("APPN-MIB", "appnNodeHprEndRteSetups"),
        ("APPN-MIB", "appnNodeHprEndRteRejects"),
        ("APPN-MIB", "appnLsBfNceId"))
)
if mibBuilder.loadTexts:
    appnHprRtpConfGroup.setStatus("current")

appnHprCtrlFlowsRtpConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 16)
)
appnHprCtrlFlowsRtpConfGroup.setObjects(
      *(("APPN-MIB", "appnLsCpCpNceId"),
        ("APPN-MIB", "appnLsRouteNceId"))
)
if mibBuilder.loadTexts:
    appnHprCtrlFlowsRtpConfGroup.setStatus("current")

appnHprBfConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 17)
)
appnHprBfConfGroup.setObjects(
      *(("APPN-MIB", "appnIsInGlobeHprBfActSess"),
        ("APPN-MIB", "appnIsInRtpNceId"),
        ("APPN-MIB", "appnIsInRtpTcid"),
        ("APPN-MIB", "appnIsRtpSessions"))
)
if mibBuilder.loadTexts:
    appnHprBfConfGroup.setStatus("current")

appnTrapConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 18)
)
appnTrapConfGroup.setObjects(
      *(("APPN-MIB", "alertIdNumber"),
        ("APPN-MIB", "affectedObject"))
)
if mibBuilder.loadTexts:
    appnTrapConfGroup.setStatus("current")

appnBrNnConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 20)
)
appnBrNnConfGroup.setObjects(
      *(("APPN-MIB", "appnNodeEnNnServer"),
        ("APPN-MIB", "appnNodeEnLuSearch"),
        ("APPN-MIB", "appnLocalTgBranchLinkType"))
)
if mibBuilder.loadTexts:
    appnBrNnConfGroup.setStatus("current")

appnGeneralConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 26)
)
appnGeneralConfGroup2.setObjects(
      *(("APPN-MIB", "appnNodeCpName"),
        ("APPN-MIB", "appnNodeId"),
        ("APPN-MIB", "appnNodeType"),
        ("APPN-MIB", "appnNodeUpTime"),
        ("APPN-MIB", "appnNodeParallelTg"),
        ("APPN-MIB", "appnNodeAdaptiveBindPacing"),
        ("APPN-MIB", "appnNodeHprSupport"),
        ("APPN-MIB", "appnNodeCounterDisconTime"),
        ("APPN-MIB", "appnNodeLsCounterType"),
        ("APPN-MIB", "appnNodeBrNn"))
)
if mibBuilder.loadTexts:
    appnGeneralConfGroup2.setStatus("current")

appnLinkConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 27)
)
appnLinkConfGroup2.setObjects(
      *(("APPN-MIB", "appnLsCommand"),
        ("APPN-MIB", "appnLsOperState"),
        ("APPN-MIB", "appnLsPortName"),
        ("APPN-MIB", "appnLsDlcType"),
        ("APPN-MIB", "appnLsDynamic"),
        ("APPN-MIB", "appnLsAdjCpName"),
        ("APPN-MIB", "appnLsAdjNodeType"),
        ("APPN-MIB", "appnLsTgNum"),
        ("APPN-MIB", "appnLsLimResource"),
        ("APPN-MIB", "appnLsActOnDemand"),
        ("APPN-MIB", "appnLsMigration"),
        ("APPN-MIB", "appnLsPartnerNodeId"),
        ("APPN-MIB", "appnLsCpCpSessionSupport"),
        ("APPN-MIB", "appnLsMaxSendBtuSize"),
        ("APPN-MIB", "appnLsInXidBytes"),
        ("APPN-MIB", "appnLsInMsgBytes"),
        ("APPN-MIB", "appnLsInXidFrames"),
        ("APPN-MIB", "appnLsInMsgFrames"),
        ("APPN-MIB", "appnLsOutXidBytes"),
        ("APPN-MIB", "appnLsOutMsgBytes"),
        ("APPN-MIB", "appnLsOutXidFrames"),
        ("APPN-MIB", "appnLsOutMsgFrames"),
        ("APPN-MIB", "appnLsEchoRsps"),
        ("APPN-MIB", "appnLsCurrentDelay"),
        ("APPN-MIB", "appnLsMaxDelay"),
        ("APPN-MIB", "appnLsMinDelay"),
        ("APPN-MIB", "appnLsMaxDelayTime"),
        ("APPN-MIB", "appnLsGoodXids"),
        ("APPN-MIB", "appnLsBadXids"),
        ("APPN-MIB", "appnLsSpecific"),
        ("APPN-MIB", "appnLsActiveTime"),
        ("APPN-MIB", "appnLsCurrentStateTime"),
        ("APPN-MIB", "appnLsHprSup"),
        ("APPN-MIB", "appnLsLocalAddr"),
        ("APPN-MIB", "appnLsRemoteAddr"),
        ("APPN-MIB", "appnLsRemoteLsName"),
        ("APPN-MIB", "appnLsStatusTime"),
        ("APPN-MIB", "appnLsStatusLsName"),
        ("APPN-MIB", "appnLsStatusCpName"),
        ("APPN-MIB", "appnLsStatusPartnerId"),
        ("APPN-MIB", "appnLsStatusTgNum"),
        ("APPN-MIB", "appnLsStatusGeneralSense"),
        ("APPN-MIB", "appnLsStatusRetry"),
        ("APPN-MIB", "appnLsStatusEndSense"),
        ("APPN-MIB", "appnLsStatusXidLocalSense"),
        ("APPN-MIB", "appnLsStatusXidRemoteSense"),
        ("APPN-MIB", "appnLsStatusXidByteInError"),
        ("APPN-MIB", "appnLsStatusXidBitInError"),
        ("APPN-MIB", "appnLsStatusDlcType"),
        ("APPN-MIB", "appnLsStatusLocalAddr"),
        ("APPN-MIB", "appnLsStatusRemoteAddr"),
        ("APPN-MIB", "appnLsCounterDisconTime"),
        ("APPN-MIB", "appnLsMltgMember"))
)
if mibBuilder.loadTexts:
    appnLinkConfGroup2.setStatus("current")

appnLocalTgConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 28)
)
appnLocalTgConfGroup2.setObjects(
      *(("APPN-MIB", "appnLocalTgDestVirtual"),
        ("APPN-MIB", "appnLocalTgDlcData"),
        ("APPN-MIB", "appnLocalTgPortName"),
        ("APPN-MIB", "appnLocalTgQuiescing"),
        ("APPN-MIB", "appnLocalTgOperational"),
        ("APPN-MIB", "appnLocalTgCpCpSession"),
        ("APPN-MIB", "appnLocalTgEffCap"),
        ("APPN-MIB", "appnLocalTgConnCost"),
        ("APPN-MIB", "appnLocalTgByteCost"),
        ("APPN-MIB", "appnLocalTgSecurity"),
        ("APPN-MIB", "appnLocalTgDelay"),
        ("APPN-MIB", "appnLocalTgUsr1"),
        ("APPN-MIB", "appnLocalTgUsr2"),
        ("APPN-MIB", "appnLocalTgUsr3"),
        ("APPN-MIB", "appnLocalTgHprSup"),
        ("APPN-MIB", "appnLocalTgIntersubnet"),
        ("APPN-MIB", "appnLocalTgMltgLinkType"))
)
if mibBuilder.loadTexts:
    appnLocalTgConfGroup2.setStatus("current")

appnDirTableConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 29)
)
appnDirTableConfGroup2.setObjects(
      *(("APPN-MIB", "appnDirNnServerName"),
        ("APPN-MIB", "appnDirLuOwnerName"),
        ("APPN-MIB", "appnDirLuLocation"),
        ("APPN-MIB", "appnDirType"),
        ("APPN-MIB", "appnDirApparentLuOwnerName"))
)
if mibBuilder.loadTexts:
    appnDirTableConfGroup2.setStatus("current")

appnNnTopoConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 30)
)
appnNnTopoConfGroup2.setObjects(
      *(("APPN-MIB", "appnNnTopoMaxNodes"),
        ("APPN-MIB", "appnNnTopoCurNumNodes"),
        ("APPN-MIB", "appnNnTopoNodePurges"),
        ("APPN-MIB", "appnNnTopoTgPurges"),
        ("APPN-MIB", "appnNnTopoTotalTduWars"),
        ("APPN-MIB", "appnNnNodeFREntryTimeLeft"),
        ("APPN-MIB", "appnNnNodeFRType"),
        ("APPN-MIB", "appnNnNodeFRRsn"),
        ("APPN-MIB", "appnNnNodeFRRouteAddResist"),
        ("APPN-MIB", "appnNnNodeFRCongested"),
        ("APPN-MIB", "appnNnNodeFRIsrDepleted"),
        ("APPN-MIB", "appnNnNodeFRQuiescing"),
        ("APPN-MIB", "appnNnNodeFRGateway"),
        ("APPN-MIB", "appnNnNodeFRCentralDirectory"),
        ("APPN-MIB", "appnNnNodeFRIsr"),
        ("APPN-MIB", "appnNnNodeFRGarbageCollect"),
        ("APPN-MIB", "appnNnNodeFRHprSupport"),
        ("APPN-MIB", "appnNnNodeFRPeriBorderSup"),
        ("APPN-MIB", "appnNnNodeFRInterchangeSup"),
        ("APPN-MIB", "appnNnNodeFRExteBorderSup"),
        ("APPN-MIB", "appnNnNodeFRBranchAwareness"),
        ("APPN-MIB", "appnNnTgFREntryTimeLeft"),
        ("APPN-MIB", "appnNnTgFRDestVirtual"),
        ("APPN-MIB", "appnNnTgFRDlcData"),
        ("APPN-MIB", "appnNnTgFRRsn"),
        ("APPN-MIB", "appnNnTgFROperational"),
        ("APPN-MIB", "appnNnTgFRQuiescing"),
        ("APPN-MIB", "appnNnTgFRCpCpSession"),
        ("APPN-MIB", "appnNnTgFREffCap"),
        ("APPN-MIB", "appnNnTgFRConnCost"),
        ("APPN-MIB", "appnNnTgFRByteCost"),
        ("APPN-MIB", "appnNnTgFRSecurity"),
        ("APPN-MIB", "appnNnTgFRDelay"),
        ("APPN-MIB", "appnNnTgFRUsr1"),
        ("APPN-MIB", "appnNnTgFRUsr2"),
        ("APPN-MIB", "appnNnTgFRUsr3"),
        ("APPN-MIB", "appnNnTgFRGarbageCollect"),
        ("APPN-MIB", "appnNnTgFRSubareaNum"),
        ("APPN-MIB", "appnNnTgFRHprSup"),
        ("APPN-MIB", "appnNnTgFRDestHprTrans"),
        ("APPN-MIB", "appnNnTgFRTypeIndicator"),
        ("APPN-MIB", "appnNnTgFRIntersubnet"),
        ("APPN-MIB", "appnNnTgFRMltgLinkType"),
        ("APPN-MIB", "appnNnTgFRBranchTg"))
)
if mibBuilder.loadTexts:
    appnNnTopoConfGroup2.setStatus("current")

appnLocalEnTopoConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 31)
)
appnLocalEnTopoConfGroup2.setObjects(
      *(("APPN-MIB", "appnLocalEnTgEntryTimeLeft"),
        ("APPN-MIB", "appnLocalEnTgDestVirtual"),
        ("APPN-MIB", "appnLocalEnTgDlcData"),
        ("APPN-MIB", "appnLocalEnTgOperational"),
        ("APPN-MIB", "appnLocalEnTgCpCpSession"),
        ("APPN-MIB", "appnLocalEnTgEffCap"),
        ("APPN-MIB", "appnLocalEnTgConnCost"),
        ("APPN-MIB", "appnLocalEnTgByteCost"),
        ("APPN-MIB", "appnLocalEnTgSecurity"),
        ("APPN-MIB", "appnLocalEnTgDelay"),
        ("APPN-MIB", "appnLocalEnTgUsr1"),
        ("APPN-MIB", "appnLocalEnTgUsr2"),
        ("APPN-MIB", "appnLocalEnTgUsr3"),
        ("APPN-MIB", "appnLocalEnTgMltgLinkType"))
)
if mibBuilder.loadTexts:
    appnLocalEnTopoConfGroup2.setStatus("current")


# Notification objects

alertTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 4, 2, 1)
)
alertTrap.setObjects(
      *(("APPN-MIB", "alertIdNumber"),
        ("APPN-MIB", "affectedObject"))
)
if mibBuilder.loadTexts:
    alertTrap.setStatus(
        "current"
    )


# Notifications groups

appnTrapNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 19)
)
appnTrapNotifGroup.setObjects(
    ("APPN-MIB", "alertTrap")
)
if mibBuilder.loadTexts:
    appnTrapNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

appnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    appnCompliance.setStatus(
        "deprecated"
    )

appnCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    appnCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPN-MIB",
    **{"SnaNodeIdentification": SnaNodeIdentification,
       "SnaControlPointName": SnaControlPointName,
       "SnaClassOfServiceName": SnaClassOfServiceName,
       "SnaModeName": SnaModeName,
       "SnaSenseData": SnaSenseData,
       "DisplayableDlcAddress": DisplayableDlcAddress,
       "AppnNodeCounter": AppnNodeCounter,
       "AppnPortCounter": AppnPortCounter,
       "AppnLinkStationCounter": AppnLinkStationCounter,
       "AppnTopologyEntryTimeLeft": AppnTopologyEntryTimeLeft,
       "AppnTgDlcData": AppnTgDlcData,
       "AppnTgEffectiveCapacity": AppnTgEffectiveCapacity,
       "AppnTgSecurity": AppnTgSecurity,
       "AppnTgDelay": AppnTgDelay,
       "appnMIB": appnMIB,
       "appnObjects": appnObjects,
       "appnNode": appnNode,
       "appnGeneralInfoAndCaps": appnGeneralInfoAndCaps,
       "appnNodeCpName": appnNodeCpName,
       "appnNodeMibVersion": appnNodeMibVersion,
       "appnNodeId": appnNodeId,
       "appnNodeType": appnNodeType,
       "appnNodeUpTime": appnNodeUpTime,
       "appnNodeParallelTg": appnNodeParallelTg,
       "appnNodeAdaptiveBindPacing": appnNodeAdaptiveBindPacing,
       "appnNodeHprSupport": appnNodeHprSupport,
       "appnNodeMaxSessPerRtpConn": appnNodeMaxSessPerRtpConn,
       "appnNodeHprIntRteSetups": appnNodeHprIntRteSetups,
       "appnNodeHprIntRteRejects": appnNodeHprIntRteRejects,
       "appnNodeHprOrgRteSetups": appnNodeHprOrgRteSetups,
       "appnNodeHprOrgRteRejects": appnNodeHprOrgRteRejects,
       "appnNodeHprEndRteSetups": appnNodeHprEndRteSetups,
       "appnNodeHprEndRteRejects": appnNodeHprEndRteRejects,
       "appnNodeCounterDisconTime": appnNodeCounterDisconTime,
       "appnNodeLsCounterType": appnNodeLsCounterType,
       "appnNodeBrNn": appnNodeBrNn,
       "appnNnUniqueInfoAndCaps": appnNnUniqueInfoAndCaps,
       "appnNodeNnCentralDirectory": appnNodeNnCentralDirectory,
       "appnNodeNnTreeCache": appnNodeNnTreeCache,
       "appnNodeNnRouteAddResist": appnNodeNnRouteAddResist,
       "appnNodeNnIsr": appnNodeNnIsr,
       "appnNodeNnFrsn": appnNodeNnFrsn,
       "appnNodeNnPeriBorderSup": appnNodeNnPeriBorderSup,
       "appnNodeNnInterchangeSup": appnNodeNnInterchangeSup,
       "appnNodeNnExteBorderSup": appnNodeNnExteBorderSup,
       "appnNodeNnSafeStoreFreq": appnNodeNnSafeStoreFreq,
       "appnNodeNnRsn": appnNodeNnRsn,
       "appnNodeNnCongested": appnNodeNnCongested,
       "appnNodeNnIsrDepleted": appnNodeNnIsrDepleted,
       "appnNodeNnQuiescing": appnNodeNnQuiescing,
       "appnNodeNnGateway": appnNodeNnGateway,
       "appnEnUniqueCaps": appnEnUniqueCaps,
       "appnNodeEnModeCosMap": appnNodeEnModeCosMap,
       "appnNodeEnNnServer": appnNodeEnNnServer,
       "appnNodeEnLuSearch": appnNodeEnLuSearch,
       "appnPortInformation": appnPortInformation,
       "appnPortTable": appnPortTable,
       "appnPortEntry": appnPortEntry,
       "appnPortName": appnPortName,
       "appnPortCommand": appnPortCommand,
       "appnPortOperState": appnPortOperState,
       "appnPortDlcType": appnPortDlcType,
       "appnPortPortType": appnPortPortType,
       "appnPortSIMRIM": appnPortSIMRIM,
       "appnPortLsRole": appnPortLsRole,
       "appnPortNegotLs": appnPortNegotLs,
       "appnPortDynamicLinkSupport": appnPortDynamicLinkSupport,
       "appnPortMaxRcvBtuSize": appnPortMaxRcvBtuSize,
       "appnPortMaxIframeWindow": appnPortMaxIframeWindow,
       "appnPortDefLsGoodXids": appnPortDefLsGoodXids,
       "appnPortDefLsBadXids": appnPortDefLsBadXids,
       "appnPortDynLsGoodXids": appnPortDynLsGoodXids,
       "appnPortDynLsBadXids": appnPortDynLsBadXids,
       "appnPortSpecific": appnPortSpecific,
       "appnPortDlcLocalAddr": appnPortDlcLocalAddr,
       "appnPortCounterDisconTime": appnPortCounterDisconTime,
       "appnLinkStationInformation": appnLinkStationInformation,
       "appnLsTable": appnLsTable,
       "appnLsEntry": appnLsEntry,
       "appnLsName": appnLsName,
       "appnLsCommand": appnLsCommand,
       "appnLsOperState": appnLsOperState,
       "appnLsPortName": appnLsPortName,
       "appnLsDlcType": appnLsDlcType,
       "appnLsDynamic": appnLsDynamic,
       "appnLsAdjCpName": appnLsAdjCpName,
       "appnLsAdjNodeType": appnLsAdjNodeType,
       "appnLsTgNum": appnLsTgNum,
       "appnLsLimResource": appnLsLimResource,
       "appnLsActOnDemand": appnLsActOnDemand,
       "appnLsMigration": appnLsMigration,
       "appnLsPartnerNodeId": appnLsPartnerNodeId,
       "appnLsCpCpSessionSupport": appnLsCpCpSessionSupport,
       "appnLsMaxSendBtuSize": appnLsMaxSendBtuSize,
       "appnLsInXidBytes": appnLsInXidBytes,
       "appnLsInMsgBytes": appnLsInMsgBytes,
       "appnLsInXidFrames": appnLsInXidFrames,
       "appnLsInMsgFrames": appnLsInMsgFrames,
       "appnLsOutXidBytes": appnLsOutXidBytes,
       "appnLsOutMsgBytes": appnLsOutMsgBytes,
       "appnLsOutXidFrames": appnLsOutXidFrames,
       "appnLsOutMsgFrames": appnLsOutMsgFrames,
       "appnLsEchoRsps": appnLsEchoRsps,
       "appnLsCurrentDelay": appnLsCurrentDelay,
       "appnLsMaxDelay": appnLsMaxDelay,
       "appnLsMinDelay": appnLsMinDelay,
       "appnLsMaxDelayTime": appnLsMaxDelayTime,
       "appnLsGoodXids": appnLsGoodXids,
       "appnLsBadXids": appnLsBadXids,
       "appnLsSpecific": appnLsSpecific,
       "appnLsActiveTime": appnLsActiveTime,
       "appnLsCurrentStateTime": appnLsCurrentStateTime,
       "appnLsHprSup": appnLsHprSup,
       "appnLsErrRecoSup": appnLsErrRecoSup,
       "appnLsForAnrLabel": appnLsForAnrLabel,
       "appnLsRevAnrLabel": appnLsRevAnrLabel,
       "appnLsCpCpNceId": appnLsCpCpNceId,
       "appnLsRouteNceId": appnLsRouteNceId,
       "appnLsBfNceId": appnLsBfNceId,
       "appnLsLocalAddr": appnLsLocalAddr,
       "appnLsRemoteAddr": appnLsRemoteAddr,
       "appnLsRemoteLsName": appnLsRemoteLsName,
       "appnLsCounterDisconTime": appnLsCounterDisconTime,
       "appnLsMltgMember": appnLsMltgMember,
       "appnLsStatusTable": appnLsStatusTable,
       "appnLsStatusEntry": appnLsStatusEntry,
       "appnLsStatusIndex": appnLsStatusIndex,
       "appnLsStatusTime": appnLsStatusTime,
       "appnLsStatusLsName": appnLsStatusLsName,
       "appnLsStatusCpName": appnLsStatusCpName,
       "appnLsStatusPartnerId": appnLsStatusPartnerId,
       "appnLsStatusTgNum": appnLsStatusTgNum,
       "appnLsStatusGeneralSense": appnLsStatusGeneralSense,
       "appnLsStatusRetry": appnLsStatusRetry,
       "appnLsStatusEndSense": appnLsStatusEndSense,
       "appnLsStatusXidLocalSense": appnLsStatusXidLocalSense,
       "appnLsStatusXidRemoteSense": appnLsStatusXidRemoteSense,
       "appnLsStatusXidByteInError": appnLsStatusXidByteInError,
       "appnLsStatusXidBitInError": appnLsStatusXidBitInError,
       "appnLsStatusDlcType": appnLsStatusDlcType,
       "appnLsStatusLocalAddr": appnLsStatusLocalAddr,
       "appnLsStatusRemoteAddr": appnLsStatusRemoteAddr,
       "appnVrnInfo": appnVrnInfo,
       "appnVrnTable": appnVrnTable,
       "appnVrnEntry": appnVrnEntry,
       "appnVrnName": appnVrnName,
       "appnVrnTgNum": appnVrnTgNum,
       "appnVrnPortName": appnVrnPortName,
       "appnNn": appnNn,
       "appnNnTopo": appnNnTopo,
       "appnNnTopoMaxNodes": appnNnTopoMaxNodes,
       "appnNnTopoCurNumNodes": appnNnTopoCurNumNodes,
       "appnNnTopoNodePurges": appnNnTopoNodePurges,
       "appnNnTopoTgPurges": appnNnTopoTgPurges,
       "appnNnTopoTotalTduWars": appnNnTopoTotalTduWars,
       "appnNnTopology": appnNnTopology,
       "appnNnTopologyFRTable": appnNnTopologyFRTable,
       "appnNnTopologyFREntry": appnNnTopologyFREntry,
       "appnNnNodeFRFrsn": appnNnNodeFRFrsn,
       "appnNnNodeFRName": appnNnNodeFRName,
       "appnNnNodeFREntryTimeLeft": appnNnNodeFREntryTimeLeft,
       "appnNnNodeFRType": appnNnNodeFRType,
       "appnNnNodeFRRsn": appnNnNodeFRRsn,
       "appnNnNodeFRRouteAddResist": appnNnNodeFRRouteAddResist,
       "appnNnNodeFRCongested": appnNnNodeFRCongested,
       "appnNnNodeFRIsrDepleted": appnNnNodeFRIsrDepleted,
       "appnNnNodeFRQuiescing": appnNnNodeFRQuiescing,
       "appnNnNodeFRGateway": appnNnNodeFRGateway,
       "appnNnNodeFRCentralDirectory": appnNnNodeFRCentralDirectory,
       "appnNnNodeFRIsr": appnNnNodeFRIsr,
       "appnNnNodeFRGarbageCollect": appnNnNodeFRGarbageCollect,
       "appnNnNodeFRHprSupport": appnNnNodeFRHprSupport,
       "appnNnNodeFRPeriBorderSup": appnNnNodeFRPeriBorderSup,
       "appnNnNodeFRInterchangeSup": appnNnNodeFRInterchangeSup,
       "appnNnNodeFRExteBorderSup": appnNnNodeFRExteBorderSup,
       "appnNnNodeFRBranchAwareness": appnNnNodeFRBranchAwareness,
       "appnNnTgTopologyFRTable": appnNnTgTopologyFRTable,
       "appnNnTgTopologyFREntry": appnNnTgTopologyFREntry,
       "appnNnTgFRFrsn": appnNnTgFRFrsn,
       "appnNnTgFROwner": appnNnTgFROwner,
       "appnNnTgFRDest": appnNnTgFRDest,
       "appnNnTgFRNum": appnNnTgFRNum,
       "appnNnTgFREntryTimeLeft": appnNnTgFREntryTimeLeft,
       "appnNnTgFRDestVirtual": appnNnTgFRDestVirtual,
       "appnNnTgFRDlcData": appnNnTgFRDlcData,
       "appnNnTgFRRsn": appnNnTgFRRsn,
       "appnNnTgFROperational": appnNnTgFROperational,
       "appnNnTgFRQuiescing": appnNnTgFRQuiescing,
       "appnNnTgFRCpCpSession": appnNnTgFRCpCpSession,
       "appnNnTgFREffCap": appnNnTgFREffCap,
       "appnNnTgFRConnCost": appnNnTgFRConnCost,
       "appnNnTgFRByteCost": appnNnTgFRByteCost,
       "appnNnTgFRSecurity": appnNnTgFRSecurity,
       "appnNnTgFRDelay": appnNnTgFRDelay,
       "appnNnTgFRUsr1": appnNnTgFRUsr1,
       "appnNnTgFRUsr2": appnNnTgFRUsr2,
       "appnNnTgFRUsr3": appnNnTgFRUsr3,
       "appnNnTgFRGarbageCollect": appnNnTgFRGarbageCollect,
       "appnNnTgFRSubareaNum": appnNnTgFRSubareaNum,
       "appnNnTgFRHprSup": appnNnTgFRHprSup,
       "appnNnTgFRDestHprTrans": appnNnTgFRDestHprTrans,
       "appnNnTgFRTypeIndicator": appnNnTgFRTypeIndicator,
       "appnNnTgFRIntersubnet": appnNnTgFRIntersubnet,
       "appnNnTgFRMltgLinkType": appnNnTgFRMltgLinkType,
       "appnNnTgFRBranchTg": appnNnTgFRBranchTg,
       "appnLocalTopology": appnLocalTopology,
       "appnLocalTgTable": appnLocalTgTable,
       "appnLocalTgEntry": appnLocalTgEntry,
       "appnLocalTgDest": appnLocalTgDest,
       "appnLocalTgNum": appnLocalTgNum,
       "appnLocalTgDestVirtual": appnLocalTgDestVirtual,
       "appnLocalTgDlcData": appnLocalTgDlcData,
       "appnLocalTgPortName": appnLocalTgPortName,
       "appnLocalTgQuiescing": appnLocalTgQuiescing,
       "appnLocalTgOperational": appnLocalTgOperational,
       "appnLocalTgCpCpSession": appnLocalTgCpCpSession,
       "appnLocalTgEffCap": appnLocalTgEffCap,
       "appnLocalTgConnCost": appnLocalTgConnCost,
       "appnLocalTgByteCost": appnLocalTgByteCost,
       "appnLocalTgSecurity": appnLocalTgSecurity,
       "appnLocalTgDelay": appnLocalTgDelay,
       "appnLocalTgUsr1": appnLocalTgUsr1,
       "appnLocalTgUsr2": appnLocalTgUsr2,
       "appnLocalTgUsr3": appnLocalTgUsr3,
       "appnLocalTgHprSup": appnLocalTgHprSup,
       "appnLocalTgIntersubnet": appnLocalTgIntersubnet,
       "appnLocalTgMltgLinkType": appnLocalTgMltgLinkType,
       "appnLocalTgBranchLinkType": appnLocalTgBranchLinkType,
       "appnLocalEnTgTable": appnLocalEnTgTable,
       "appnLocalEnTgEntry": appnLocalEnTgEntry,
       "appnLocalEnTgOrigin": appnLocalEnTgOrigin,
       "appnLocalEnTgDest": appnLocalEnTgDest,
       "appnLocalEnTgNum": appnLocalEnTgNum,
       "appnLocalEnTgEntryTimeLeft": appnLocalEnTgEntryTimeLeft,
       "appnLocalEnTgDestVirtual": appnLocalEnTgDestVirtual,
       "appnLocalEnTgDlcData": appnLocalEnTgDlcData,
       "appnLocalEnTgOperational": appnLocalEnTgOperational,
       "appnLocalEnTgCpCpSession": appnLocalEnTgCpCpSession,
       "appnLocalEnTgEffCap": appnLocalEnTgEffCap,
       "appnLocalEnTgConnCost": appnLocalEnTgConnCost,
       "appnLocalEnTgByteCost": appnLocalEnTgByteCost,
       "appnLocalEnTgSecurity": appnLocalEnTgSecurity,
       "appnLocalEnTgDelay": appnLocalEnTgDelay,
       "appnLocalEnTgUsr1": appnLocalEnTgUsr1,
       "appnLocalEnTgUsr2": appnLocalEnTgUsr2,
       "appnLocalEnTgUsr3": appnLocalEnTgUsr3,
       "appnLocalEnTgMltgLinkType": appnLocalEnTgMltgLinkType,
       "appnDir": appnDir,
       "appnDirPerf": appnDirPerf,
       "appnDirMaxCaches": appnDirMaxCaches,
       "appnDirCurCaches": appnDirCurCaches,
       "appnDirCurHomeEntries": appnDirCurHomeEntries,
       "appnDirRegEntries": appnDirRegEntries,
       "appnDirInLocates": appnDirInLocates,
       "appnDirInBcastLocates": appnDirInBcastLocates,
       "appnDirOutLocates": appnDirOutLocates,
       "appnDirOutBcastLocates": appnDirOutBcastLocates,
       "appnDirNotFoundLocates": appnDirNotFoundLocates,
       "appnDirNotFoundBcastLocates": appnDirNotFoundBcastLocates,
       "appnDirLocateOutstands": appnDirLocateOutstands,
       "appnDirTable": appnDirTable,
       "appnDirEntry": appnDirEntry,
       "appnDirLuName": appnDirLuName,
       "appnDirNnServerName": appnDirNnServerName,
       "appnDirLuOwnerName": appnDirLuOwnerName,
       "appnDirLuLocation": appnDirLuLocation,
       "appnDirType": appnDirType,
       "appnDirApparentLuOwnerName": appnDirApparentLuOwnerName,
       "appnCos": appnCos,
       "appnCosModeTable": appnCosModeTable,
       "appnCosModeEntry": appnCosModeEntry,
       "appnCosModeName": appnCosModeName,
       "appnCosModeCosName": appnCosModeCosName,
       "appnCosNameTable": appnCosNameTable,
       "appnCosNameEntry": appnCosNameEntry,
       "appnCosName": appnCosName,
       "appnCosTransPriority": appnCosTransPriority,
       "appnCosNodeRowTable": appnCosNodeRowTable,
       "appnCosNodeRowEntry": appnCosNodeRowEntry,
       "appnCosNodeRowName": appnCosNodeRowName,
       "appnCosNodeRowIndex": appnCosNodeRowIndex,
       "appnCosNodeRowWgt": appnCosNodeRowWgt,
       "appnCosNodeRowResistMin": appnCosNodeRowResistMin,
       "appnCosNodeRowResistMax": appnCosNodeRowResistMax,
       "appnCosNodeRowMinCongestAllow": appnCosNodeRowMinCongestAllow,
       "appnCosNodeRowMaxCongestAllow": appnCosNodeRowMaxCongestAllow,
       "appnCosTgRowTable": appnCosTgRowTable,
       "appnCosTgRowEntry": appnCosTgRowEntry,
       "appnCosTgRowName": appnCosTgRowName,
       "appnCosTgRowIndex": appnCosTgRowIndex,
       "appnCosTgRowWgt": appnCosTgRowWgt,
       "appnCosTgRowEffCapMin": appnCosTgRowEffCapMin,
       "appnCosTgRowEffCapMax": appnCosTgRowEffCapMax,
       "appnCosTgRowConnCostMin": appnCosTgRowConnCostMin,
       "appnCosTgRowConnCostMax": appnCosTgRowConnCostMax,
       "appnCosTgRowByteCostMin": appnCosTgRowByteCostMin,
       "appnCosTgRowByteCostMax": appnCosTgRowByteCostMax,
       "appnCosTgRowSecurityMin": appnCosTgRowSecurityMin,
       "appnCosTgRowSecurityMax": appnCosTgRowSecurityMax,
       "appnCosTgRowDelayMin": appnCosTgRowDelayMin,
       "appnCosTgRowDelayMax": appnCosTgRowDelayMax,
       "appnCosTgRowUsr1Min": appnCosTgRowUsr1Min,
       "appnCosTgRowUsr1Max": appnCosTgRowUsr1Max,
       "appnCosTgRowUsr2Min": appnCosTgRowUsr2Min,
       "appnCosTgRowUsr2Max": appnCosTgRowUsr2Max,
       "appnCosTgRowUsr3Min": appnCosTgRowUsr3Min,
       "appnCosTgRowUsr3Max": appnCosTgRowUsr3Max,
       "appnSessIntermediate": appnSessIntermediate,
       "appnIsInGlobal": appnIsInGlobal,
       "appnIsInGlobeCtrAdminStatus": appnIsInGlobeCtrAdminStatus,
       "appnIsInGlobeCtrOperStatus": appnIsInGlobeCtrOperStatus,
       "appnIsInGlobeCtrStatusTime": appnIsInGlobeCtrStatusTime,
       "appnIsInGlobeRscv": appnIsInGlobeRscv,
       "appnIsInGlobeRscvTime": appnIsInGlobeRscvTime,
       "appnIsInGlobeActSess": appnIsInGlobeActSess,
       "appnIsInGlobeHprBfActSess": appnIsInGlobeHprBfActSess,
       "appnIsInTable": appnIsInTable,
       "appnIsInEntry": appnIsInEntry,
       "appnIsInFqCpName": appnIsInFqCpName,
       "appnIsInPcid": appnIsInPcid,
       "appnIsInSessState": appnIsInSessState,
       "appnIsInPriLuName": appnIsInPriLuName,
       "appnIsInSecLuName": appnIsInSecLuName,
       "appnIsInModeName": appnIsInModeName,
       "appnIsInCosName": appnIsInCosName,
       "appnIsInTransPriority": appnIsInTransPriority,
       "appnIsInSessType": appnIsInSessType,
       "appnIsInSessUpTime": appnIsInSessUpTime,
       "appnIsInCtrUpTime": appnIsInCtrUpTime,
       "appnIsInP2SFmdPius": appnIsInP2SFmdPius,
       "appnIsInS2PFmdPius": appnIsInS2PFmdPius,
       "appnIsInP2SNonFmdPius": appnIsInP2SNonFmdPius,
       "appnIsInS2PNonFmdPius": appnIsInS2PNonFmdPius,
       "appnIsInP2SFmdBytes": appnIsInP2SFmdBytes,
       "appnIsInS2PFmdBytes": appnIsInS2PFmdBytes,
       "appnIsInP2SNonFmdBytes": appnIsInP2SNonFmdBytes,
       "appnIsInS2PNonFmdBytes": appnIsInS2PNonFmdBytes,
       "appnIsInPsAdjCpName": appnIsInPsAdjCpName,
       "appnIsInPsAdjTgNum": appnIsInPsAdjTgNum,
       "appnIsInPsSendMaxBtuSize": appnIsInPsSendMaxBtuSize,
       "appnIsInPsSendPacingType": appnIsInPsSendPacingType,
       "appnIsInPsSendRpc": appnIsInPsSendRpc,
       "appnIsInPsSendNxWndwSize": appnIsInPsSendNxWndwSize,
       "appnIsInPsRecvPacingType": appnIsInPsRecvPacingType,
       "appnIsInPsRecvRpc": appnIsInPsRecvRpc,
       "appnIsInPsRecvNxWndwSize": appnIsInPsRecvNxWndwSize,
       "appnIsInSsAdjCpName": appnIsInSsAdjCpName,
       "appnIsInSsAdjTgNum": appnIsInSsAdjTgNum,
       "appnIsInSsSendMaxBtuSize": appnIsInSsSendMaxBtuSize,
       "appnIsInSsSendPacingType": appnIsInSsSendPacingType,
       "appnIsInSsSendRpc": appnIsInSsSendRpc,
       "appnIsInSsSendNxWndwSize": appnIsInSsSendNxWndwSize,
       "appnIsInSsRecvPacingType": appnIsInSsRecvPacingType,
       "appnIsInSsRecvRpc": appnIsInSsRecvRpc,
       "appnIsInSsRecvNxWndwSize": appnIsInSsRecvNxWndwSize,
       "appnIsInRouteInfo": appnIsInRouteInfo,
       "appnIsInRtpNceId": appnIsInRtpNceId,
       "appnIsInRtpTcid": appnIsInRtpTcid,
       "appnIsRtpTable": appnIsRtpTable,
       "appnIsRtpEntry": appnIsRtpEntry,
       "appnIsRtpNceId": appnIsRtpNceId,
       "appnIsRtpTcid": appnIsRtpTcid,
       "appnIsRtpSessions": appnIsRtpSessions,
       "appnTraps": appnTraps,
       "alertTrap": alertTrap,
       "alertIdNumber": alertIdNumber,
       "affectedObject": affectedObject,
       "appnConformance": appnConformance,
       "appnCompliances": appnCompliances,
       "appnCompliance": appnCompliance,
       "appnCompliance2": appnCompliance2,
       "appnGroups": appnGroups,
       "appnGeneralConfGroup": appnGeneralConfGroup,
       "appnPortConfGroup": appnPortConfGroup,
       "appnLinkConfGroup": appnLinkConfGroup,
       "appnLocalTgConfGroup": appnLocalTgConfGroup,
       "appnDirTableConfGroup": appnDirTableConfGroup,
       "appnNnUniqueConfGroup": appnNnUniqueConfGroup,
       "appnEnUniqueConfGroup": appnEnUniqueConfGroup,
       "appnVrnConfGroup": appnVrnConfGroup,
       "appnNnTopoConfGroup": appnNnTopoConfGroup,
       "appnLocalEnTopoConfGroup": appnLocalEnTopoConfGroup,
       "appnLocalDirPerfConfGroup": appnLocalDirPerfConfGroup,
       "appnCosConfGroup": appnCosConfGroup,
       "appnIntSessConfGroup": appnIntSessConfGroup,
       "appnHprBaseConfGroup": appnHprBaseConfGroup,
       "appnHprRtpConfGroup": appnHprRtpConfGroup,
       "appnHprCtrlFlowsRtpConfGroup": appnHprCtrlFlowsRtpConfGroup,
       "appnHprBfConfGroup": appnHprBfConfGroup,
       "appnTrapConfGroup": appnTrapConfGroup,
       "appnTrapNotifGroup": appnTrapNotifGroup,
       "appnBrNnConfGroup": appnBrNnConfGroup,
       "appnGeneralConfGroup2": appnGeneralConfGroup2,
       "appnLinkConfGroup2": appnLinkConfGroup2,
       "appnLocalTgConfGroup2": appnLocalTgConfGroup2,
       "appnDirTableConfGroup2": appnDirTableConfGroup2,
       "appnNnTopoConfGroup2": appnNnTopoConfGroup2,
       "appnLocalEnTopoConfGroup2": appnLocalEnTopoConfGroup2}
)
