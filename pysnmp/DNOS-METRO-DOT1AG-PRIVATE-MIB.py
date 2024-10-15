# SNMP MIB module (DNOS-METRO-DOT1AG-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-METRO-DOT1AG-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:05 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(DisplayString,
 MacAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathDot1agPrivateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45)
)
fastPathDot1agPrivateMIB.setRevisions(
        ("2011-01-26 00:00",
         "2008-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot1agGlobalConfigGroup_ObjectIdentity = ObjectIdentity
dot1agGlobalConfigGroup = _Dot1agGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1)
)
_AgentDot1agGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1agGlobalConfigGroup = _AgentDot1agGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1)
)


class _AgentDot1agCfmStatus_Type(Integer32):
    """Custom type agentDot1agCfmStatus based on Integer32"""
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


_AgentDot1agCfmStatus_Type.__name__ = "Integer32"
_AgentDot1agCfmStatus_Object = MibScalar
agentDot1agCfmStatus = _AgentDot1agCfmStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 1),
    _AgentDot1agCfmStatus_Type()
)
agentDot1agCfmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1agCfmStatus.setStatus("current")


class _AgentDot1agCfmArchieveHoldTime_Type(Integer32):
    """Custom type agentDot1agCfmArchieveHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentDot1agCfmArchieveHoldTime_Type.__name__ = "Integer32"
_AgentDot1agCfmArchieveHoldTime_Object = MibScalar
agentDot1agCfmArchieveHoldTime = _AgentDot1agCfmArchieveHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 2),
    _AgentDot1agCfmArchieveHoldTime_Type()
)
agentDot1agCfmArchieveHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1agCfmArchieveHoldTime.setStatus("current")


class _AgentDot1agCfmClearRemoteMEPs_Type(Integer32):
    """Custom type agentDot1agCfmClearRemoteMEPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AgentDot1agCfmClearRemoteMEPs_Type.__name__ = "Integer32"
_AgentDot1agCfmClearRemoteMEPs_Object = MibScalar
agentDot1agCfmClearRemoteMEPs = _AgentDot1agCfmClearRemoteMEPs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 3),
    _AgentDot1agCfmClearRemoteMEPs_Type()
)
agentDot1agCfmClearRemoteMEPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1agCfmClearRemoteMEPs.setStatus("current")


class _AgentDot1agCfmClearTraceRouteCache_Type(Integer32):
    """Custom type agentDot1agCfmClearTraceRouteCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AgentDot1agCfmClearTraceRouteCache_Type.__name__ = "Integer32"
_AgentDot1agCfmClearTraceRouteCache_Object = MibScalar
agentDot1agCfmClearTraceRouteCache = _AgentDot1agCfmClearTraceRouteCache_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 1, 1, 4),
    _AgentDot1agCfmClearTraceRouteCache_Type()
)
agentDot1agCfmClearTraceRouteCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1agCfmClearTraceRouteCache.setStatus("current")
_Dot1agMipConfigGroup_ObjectIdentity = ObjectIdentity
dot1agMipConfigGroup = _Dot1agMipConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2)
)
_AgentDot1agMipConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1agMipConfigGroup = _AgentDot1agMipConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1)
)
_AgentDot1agMipTable_Object = MibTable
agentDot1agMipTable = _AgentDot1agMipTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentDot1agMipTable.setStatus("current")
_AgentDot1agMipEntry_Object = MibTableRow
agentDot1agMipEntry = _AgentDot1agMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1)
)
agentDot1agMipEntry.setIndexNames(
    (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agMipMdIndex"),
    (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agMipIfIndex"),
)
if mibBuilder.loadTexts:
    agentDot1agMipEntry.setStatus("current")


class _AgentDot1agMipMdIndex_Type(Unsigned32):
    """Custom type agentDot1agMipMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AgentDot1agMipMdIndex_Type.__name__ = "Unsigned32"
_AgentDot1agMipMdIndex_Object = MibTableColumn
agentDot1agMipMdIndex = _AgentDot1agMipMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1, 1),
    _AgentDot1agMipMdIndex_Type()
)
agentDot1agMipMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1agMipMdIndex.setStatus("current")
_AgentDot1agMipIfIndex_Type = InterfaceIndex
_AgentDot1agMipIfIndex_Object = MibTableColumn
agentDot1agMipIfIndex = _AgentDot1agMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1, 2),
    _AgentDot1agMipIfIndex_Type()
)
agentDot1agMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1agMipIfIndex.setStatus("current")


class _AgentDot1agMipMode_Type(Integer32):
    """Custom type agentDot1agMipMode based on Integer32"""
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


_AgentDot1agMipMode_Type.__name__ = "Integer32"
_AgentDot1agMipMode_Object = MibTableColumn
agentDot1agMipMode = _AgentDot1agMipMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 2, 1, 1, 1, 3),
    _AgentDot1agMipMode_Type()
)
agentDot1agMipMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDot1agMipMode.setStatus("current")
_Dot1agRMepConfigGroup_ObjectIdentity = ObjectIdentity
dot1agRMepConfigGroup = _Dot1agRMepConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3)
)
_AgentDot1agRMepConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1agRMepConfigGroup = _AgentDot1agRMepConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1)
)
_AgentDot1agRMepTable_Object = MibTable
agentDot1agRMepTable = _AgentDot1agRMepTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1)
)
if mibBuilder.loadTexts:
    agentDot1agRMepTable.setStatus("current")
_AgentDot1agRMepEntry_Object = MibTableRow
agentDot1agRMepEntry = _AgentDot1agRMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1)
)
agentDot1agRMepEntry.setIndexNames(
    (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepMdIndex"),
    (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepMaIndex"),
    (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepMepIdIndex"),
    (0, "DNOS-METRO-DOT1AG-PRIVATE-MIB", "agentDot1agRMepIdentifier"),
)
if mibBuilder.loadTexts:
    agentDot1agRMepEntry.setStatus("current")
_AgentDot1agRMepMdIndex_Type = Unsigned32
_AgentDot1agRMepMdIndex_Object = MibTableColumn
agentDot1agRMepMdIndex = _AgentDot1agRMepMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 1),
    _AgentDot1agRMepMdIndex_Type()
)
agentDot1agRMepMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1agRMepMdIndex.setStatus("current")
_AgentDot1agRMepMaIndex_Type = Unsigned32
_AgentDot1agRMepMaIndex_Object = MibTableColumn
agentDot1agRMepMaIndex = _AgentDot1agRMepMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 2),
    _AgentDot1agRMepMaIndex_Type()
)
agentDot1agRMepMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1agRMepMaIndex.setStatus("current")


class _AgentDot1agRMepMepIdIndex_Type(Unsigned32):
    """Custom type agentDot1agRMepMepIdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_AgentDot1agRMepMepIdIndex_Type.__name__ = "Unsigned32"
_AgentDot1agRMepMepIdIndex_Object = MibTableColumn
agentDot1agRMepMepIdIndex = _AgentDot1agRMepMepIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 3),
    _AgentDot1agRMepMepIdIndex_Type()
)
agentDot1agRMepMepIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1agRMepMepIdIndex.setStatus("current")


class _AgentDot1agRMepIdentifier_Type(Unsigned32):
    """Custom type agentDot1agRMepIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_AgentDot1agRMepIdentifier_Type.__name__ = "Unsigned32"
_AgentDot1agRMepIdentifier_Object = MibTableColumn
agentDot1agRMepIdentifier = _AgentDot1agRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 4),
    _AgentDot1agRMepIdentifier_Type()
)
agentDot1agRMepIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDot1agRMepIdentifier.setStatus("current")
_AgentDot1agRMepIfIndex_Type = InterfaceIndex
_AgentDot1agRMepIfIndex_Object = MibTableColumn
agentDot1agRMepIfIndex = _AgentDot1agRMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 5),
    _AgentDot1agRMepIfIndex_Type()
)
agentDot1agRMepIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1agRMepIfIndex.setStatus("current")
_AgentDot1agRMepMacAddress_Type = MacAddress
_AgentDot1agRMepMacAddress_Object = MibTableColumn
agentDot1agRMepMacAddress = _AgentDot1agRMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 6),
    _AgentDot1agRMepMacAddress_Type()
)
agentDot1agRMepMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1agRMepMacAddress.setStatus("current")
_AgentDot1agRMepRowStatus_Type = RowStatus
_AgentDot1agRMepRowStatus_Object = MibTableColumn
agentDot1agRMepRowStatus = _AgentDot1agRMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 45, 3, 1, 1, 1, 7),
    _AgentDot1agRMepRowStatus_Type()
)
agentDot1agRMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDot1agRMepRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-METRO-DOT1AG-PRIVATE-MIB",
    **{"fastPathDot1agPrivateMIB": fastPathDot1agPrivateMIB,
       "dot1agGlobalConfigGroup": dot1agGlobalConfigGroup,
       "agentDot1agGlobalConfigGroup": agentDot1agGlobalConfigGroup,
       "agentDot1agCfmStatus": agentDot1agCfmStatus,
       "agentDot1agCfmArchieveHoldTime": agentDot1agCfmArchieveHoldTime,
       "agentDot1agCfmClearRemoteMEPs": agentDot1agCfmClearRemoteMEPs,
       "agentDot1agCfmClearTraceRouteCache": agentDot1agCfmClearTraceRouteCache,
       "dot1agMipConfigGroup": dot1agMipConfigGroup,
       "agentDot1agMipConfigGroup": agentDot1agMipConfigGroup,
       "agentDot1agMipTable": agentDot1agMipTable,
       "agentDot1agMipEntry": agentDot1agMipEntry,
       "agentDot1agMipMdIndex": agentDot1agMipMdIndex,
       "agentDot1agMipIfIndex": agentDot1agMipIfIndex,
       "agentDot1agMipMode": agentDot1agMipMode,
       "dot1agRMepConfigGroup": dot1agRMepConfigGroup,
       "agentDot1agRMepConfigGroup": agentDot1agRMepConfigGroup,
       "agentDot1agRMepTable": agentDot1agRMepTable,
       "agentDot1agRMepEntry": agentDot1agRMepEntry,
       "agentDot1agRMepMdIndex": agentDot1agRMepMdIndex,
       "agentDot1agRMepMaIndex": agentDot1agRMepMaIndex,
       "agentDot1agRMepMepIdIndex": agentDot1agRMepMepIdIndex,
       "agentDot1agRMepIdentifier": agentDot1agRMepIdentifier,
       "agentDot1agRMepIfIndex": agentDot1agRMepIfIndex,
       "agentDot1agRMepMacAddress": agentDot1agRMepMacAddress,
       "agentDot1agRMepRowStatus": agentDot1agRMepRowStatus}
)
