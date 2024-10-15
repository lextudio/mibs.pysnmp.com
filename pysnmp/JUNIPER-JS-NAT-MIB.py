# SNMP MIB module (JUNIPER-JS-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:19 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(jnxJsNAT,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsNAT")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxJsNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1)
)
jnxJsNatMIB.setRevisions(
        ("2007-04-13 20:22",
         "2012-03-01 11:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsNatNotifications_ObjectIdentity = ObjectIdentity
jnxJsNatNotifications = _JnxJsNatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 0)
)
_JnxJsNatObjects_ObjectIdentity = ObjectIdentity
jnxJsNatObjects = _JnxJsNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1)
)
_JnxJsSrcNatNumOfEntries_Type = Gauge32
_JnxJsSrcNatNumOfEntries_Object = MibScalar
jnxJsSrcNatNumOfEntries = _JnxJsSrcNatNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 1),
    _JnxJsSrcNatNumOfEntries_Type()
)
jnxJsSrcNatNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSrcNatNumOfEntries.setStatus("current")
_JnxJsSrcNatTable_Object = MibTable
jnxJsSrcNatTable = _JnxJsSrcNatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxJsSrcNatTable.setStatus("deprecated")
_JnxJsSrcNatEntry_Object = MibTableRow
jnxJsSrcNatEntry = _JnxJsSrcNatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1)
)
jnxJsSrcNatEntry.setIndexNames(
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcIpPoolName"),
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcGlobalAddr"),
)
if mibBuilder.loadTexts:
    jnxJsSrcNatEntry.setStatus("deprecated")


class _JnxJsNatSrcIpPoolName_Type(DisplayString):
    """Custom type jnxJsNatSrcIpPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJsNatSrcIpPoolName_Type.__name__ = "DisplayString"
_JnxJsNatSrcIpPoolName_Object = MibTableColumn
jnxJsNatSrcIpPoolName = _JnxJsNatSrcIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 1),
    _JnxJsNatSrcIpPoolName_Type()
)
jnxJsNatSrcIpPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsNatSrcIpPoolName.setStatus("deprecated")
_JnxJsNatSrcGlobalAddr_Type = InetAddressIPv4
_JnxJsNatSrcGlobalAddr_Object = MibTableColumn
jnxJsNatSrcGlobalAddr = _JnxJsNatSrcGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 2),
    _JnxJsNatSrcGlobalAddr_Type()
)
jnxJsNatSrcGlobalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsNatSrcGlobalAddr.setStatus("deprecated")


class _JnxJsNatSrcPortPoolType_Type(Integer32):
    """Custom type jnxJsNatSrcPortPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 3),
          ("withPAT", 1),
          ("withoutPAT", 2))
    )


_JnxJsNatSrcPortPoolType_Type.__name__ = "Integer32"
_JnxJsNatSrcPortPoolType_Object = MibTableColumn
jnxJsNatSrcPortPoolType = _JnxJsNatSrcPortPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 3),
    _JnxJsNatSrcPortPoolType_Type()
)
jnxJsNatSrcPortPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatSrcPortPoolType.setStatus("deprecated")
_JnxJsNatSrcNumOfPortInuse_Type = Integer32
_JnxJsNatSrcNumOfPortInuse_Object = MibTableColumn
jnxJsNatSrcNumOfPortInuse = _JnxJsNatSrcNumOfPortInuse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 4),
    _JnxJsNatSrcNumOfPortInuse_Type()
)
jnxJsNatSrcNumOfPortInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatSrcNumOfPortInuse.setStatus("deprecated")
_JnxJsNatSrcNumOfSessions_Type = Integer32
_JnxJsNatSrcNumOfSessions_Object = MibTableColumn
jnxJsNatSrcNumOfSessions = _JnxJsNatSrcNumOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 5),
    _JnxJsNatSrcNumOfSessions_Type()
)
jnxJsNatSrcNumOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatSrcNumOfSessions.setStatus("deprecated")
_JnxJsNatSrcAssocatedIf_Type = InterfaceIndex
_JnxJsNatSrcAssocatedIf_Object = MibTableColumn
jnxJsNatSrcAssocatedIf = _JnxJsNatSrcAssocatedIf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 2, 1, 6),
    _JnxJsNatSrcAssocatedIf_Type()
)
jnxJsNatSrcAssocatedIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatSrcAssocatedIf.setStatus("deprecated")
_JnxJsNatIfSrcPoolPortTable_Object = MibTable
jnxJsNatIfSrcPoolPortTable = _JnxJsNatIfSrcPoolPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxJsNatIfSrcPoolPortTable.setStatus("current")
_JnxJsNatIfSrcPoolPortEntry_Object = MibTableRow
jnxJsNatIfSrcPoolPortEntry = _JnxJsNatIfSrcPoolPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1)
)
jnxJsNatIfSrcPoolPortEntry.setIndexNames(
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatIfSrcPoolIndex"),
)
if mibBuilder.loadTexts:
    jnxJsNatIfSrcPoolPortEntry.setStatus("current")


class _JnxJsNatIfSrcPoolIndex_Type(Integer32):
    """Custom type jnxJsNatIfSrcPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxJsNatIfSrcPoolIndex_Type.__name__ = "Integer32"
_JnxJsNatIfSrcPoolIndex_Object = MibTableColumn
jnxJsNatIfSrcPoolIndex = _JnxJsNatIfSrcPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 1),
    _JnxJsNatIfSrcPoolIndex_Type()
)
jnxJsNatIfSrcPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsNatIfSrcPoolIndex.setStatus("current")
_JnxJsNatIfSrcPoolTotalSinglePorts_Type = Integer32
_JnxJsNatIfSrcPoolTotalSinglePorts_Object = MibTableColumn
jnxJsNatIfSrcPoolTotalSinglePorts = _JnxJsNatIfSrcPoolTotalSinglePorts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 2),
    _JnxJsNatIfSrcPoolTotalSinglePorts_Type()
)
jnxJsNatIfSrcPoolTotalSinglePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatIfSrcPoolTotalSinglePorts.setStatus("current")
_JnxJsNatIfSrcPoolAllocSinglePorts_Type = Integer32
_JnxJsNatIfSrcPoolAllocSinglePorts_Object = MibTableColumn
jnxJsNatIfSrcPoolAllocSinglePorts = _JnxJsNatIfSrcPoolAllocSinglePorts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 3),
    _JnxJsNatIfSrcPoolAllocSinglePorts_Type()
)
jnxJsNatIfSrcPoolAllocSinglePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatIfSrcPoolAllocSinglePorts.setStatus("current")
_JnxJsNatIfSrcPoolTotalTwinPorts_Type = Integer32
_JnxJsNatIfSrcPoolTotalTwinPorts_Object = MibTableColumn
jnxJsNatIfSrcPoolTotalTwinPorts = _JnxJsNatIfSrcPoolTotalTwinPorts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 4),
    _JnxJsNatIfSrcPoolTotalTwinPorts_Type()
)
jnxJsNatIfSrcPoolTotalTwinPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatIfSrcPoolTotalTwinPorts.setStatus("current")
_JnxJsNatIfSrcPoolAllocTwinPorts_Type = Integer32
_JnxJsNatIfSrcPoolAllocTwinPorts_Object = MibTableColumn
jnxJsNatIfSrcPoolAllocTwinPorts = _JnxJsNatIfSrcPoolAllocTwinPorts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 3, 1, 5),
    _JnxJsNatIfSrcPoolAllocTwinPorts_Type()
)
jnxJsNatIfSrcPoolAllocTwinPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatIfSrcPoolAllocTwinPorts.setStatus("current")
_JnxJsSrcNatStatsTable_Object = MibTable
jnxJsSrcNatStatsTable = _JnxJsSrcNatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxJsSrcNatStatsTable.setStatus("current")
_JnxJsSrcNatStatsEntry_Object = MibTableRow
jnxJsSrcNatStatsEntry = _JnxJsSrcNatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1)
)
jnxJsSrcNatStatsEntry.setIndexNames(
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcPoolName"),
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcXlatedAddrType"),
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatSrcXlatedAddr"),
)
if mibBuilder.loadTexts:
    jnxJsSrcNatStatsEntry.setStatus("current")


class _JnxJsNatSrcPoolName_Type(DisplayString):
    """Custom type jnxJsNatSrcPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJsNatSrcPoolName_Type.__name__ = "DisplayString"
_JnxJsNatSrcPoolName_Object = MibTableColumn
jnxJsNatSrcPoolName = _JnxJsNatSrcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 1),
    _JnxJsNatSrcPoolName_Type()
)
jnxJsNatSrcPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsNatSrcPoolName.setStatus("current")
_JnxJsNatSrcXlatedAddrType_Type = InetAddressType
_JnxJsNatSrcXlatedAddrType_Object = MibTableColumn
jnxJsNatSrcXlatedAddrType = _JnxJsNatSrcXlatedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 2),
    _JnxJsNatSrcXlatedAddrType_Type()
)
jnxJsNatSrcXlatedAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsNatSrcXlatedAddrType.setStatus("current")
_JnxJsNatSrcXlatedAddr_Type = InetAddress
_JnxJsNatSrcXlatedAddr_Object = MibTableColumn
jnxJsNatSrcXlatedAddr = _JnxJsNatSrcXlatedAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 3),
    _JnxJsNatSrcXlatedAddr_Type()
)
jnxJsNatSrcXlatedAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsNatSrcXlatedAddr.setStatus("current")


class _JnxJsNatSrcPoolType_Type(Integer32):
    """Custom type jnxJsNatSrcPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 3),
          ("withPAT", 1),
          ("withoutPAT", 2))
    )


_JnxJsNatSrcPoolType_Type.__name__ = "Integer32"
_JnxJsNatSrcPoolType_Object = MibTableColumn
jnxJsNatSrcPoolType = _JnxJsNatSrcPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 4),
    _JnxJsNatSrcPoolType_Type()
)
jnxJsNatSrcPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatSrcPoolType.setStatus("current")
_JnxJsNatSrcNumPortInuse_Type = Integer32
_JnxJsNatSrcNumPortInuse_Object = MibTableColumn
jnxJsNatSrcNumPortInuse = _JnxJsNatSrcNumPortInuse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 5),
    _JnxJsNatSrcNumPortInuse_Type()
)
jnxJsNatSrcNumPortInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatSrcNumPortInuse.setStatus("current")
_JnxJsNatSrcNumSessions_Type = Integer32
_JnxJsNatSrcNumSessions_Object = MibTableColumn
jnxJsNatSrcNumSessions = _JnxJsNatSrcNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 4, 1, 6),
    _JnxJsNatSrcNumSessions_Type()
)
jnxJsNatSrcNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatSrcNumSessions.setStatus("current")
_JnxJsNatRuleTable_Object = MibTable
jnxJsNatRuleTable = _JnxJsNatRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxJsNatRuleTable.setStatus("current")
_JnxJsNatRuleEntry_Object = MibTableRow
jnxJsNatRuleEntry = _JnxJsNatRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1)
)
jnxJsNatRuleEntry.setIndexNames(
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatRuleName"),
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatRuleType"),
)
if mibBuilder.loadTexts:
    jnxJsNatRuleEntry.setStatus("current")


class _JnxJsNatRuleName_Type(DisplayString):
    """Custom type jnxJsNatRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJsNatRuleName_Type.__name__ = "DisplayString"
_JnxJsNatRuleName_Object = MibTableColumn
jnxJsNatRuleName = _JnxJsNatRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 1),
    _JnxJsNatRuleName_Type()
)
jnxJsNatRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatRuleName.setStatus("current")


class _JnxJsNatRuleType_Type(Integer32):
    """Custom type jnxJsNatRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1),
          ("static", 3))
    )


_JnxJsNatRuleType_Type.__name__ = "Integer32"
_JnxJsNatRuleType_Object = MibTableColumn
jnxJsNatRuleType = _JnxJsNatRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 2),
    _JnxJsNatRuleType_Type()
)
jnxJsNatRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatRuleType.setStatus("current")
_JnxJsNatRuleTransHits_Type = Integer32
_JnxJsNatRuleTransHits_Object = MibTableColumn
jnxJsNatRuleTransHits = _JnxJsNatRuleTransHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 3),
    _JnxJsNatRuleTransHits_Type()
)
jnxJsNatRuleTransHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatRuleTransHits.setStatus("deprecated")
_JnxJsNatRuleHits_Type = Counter32
_JnxJsNatRuleHits_Object = MibTableColumn
jnxJsNatRuleHits = _JnxJsNatRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 5, 1, 4),
    _JnxJsNatRuleHits_Type()
)
jnxJsNatRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatRuleHits.setStatus("current")
_JnxJsNatPoolTable_Object = MibTable
jnxJsNatPoolTable = _JnxJsNatPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxJsNatPoolTable.setStatus("current")
_JnxJsNatPoolEntry_Object = MibTableRow
jnxJsNatPoolEntry = _JnxJsNatPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1)
)
jnxJsNatPoolEntry.setIndexNames(
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatPoolName"),
    (0, "JUNIPER-JS-NAT-MIB", "jnxJsNatPoolType"),
)
if mibBuilder.loadTexts:
    jnxJsNatPoolEntry.setStatus("current")


class _JnxJsNatPoolName_Type(DisplayString):
    """Custom type jnxJsNatPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJsNatPoolName_Type.__name__ = "DisplayString"
_JnxJsNatPoolName_Object = MibTableColumn
jnxJsNatPoolName = _JnxJsNatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 1),
    _JnxJsNatPoolName_Type()
)
jnxJsNatPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatPoolName.setStatus("current")


class _JnxJsNatPoolType_Type(Integer32):
    """Custom type jnxJsNatPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1),
          ("static", 3))
    )


_JnxJsNatPoolType_Type.__name__ = "Integer32"
_JnxJsNatPoolType_Object = MibTableColumn
jnxJsNatPoolType = _JnxJsNatPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 2),
    _JnxJsNatPoolType_Type()
)
jnxJsNatPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatPoolType.setStatus("current")
_JnxJsNatPoolTransHits_Type = Integer32
_JnxJsNatPoolTransHits_Object = MibTableColumn
jnxJsNatPoolTransHits = _JnxJsNatPoolTransHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 3),
    _JnxJsNatPoolTransHits_Type()
)
jnxJsNatPoolTransHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatPoolTransHits.setStatus("deprecated")
_JnxJsNatPoolHits_Type = Counter32
_JnxJsNatPoolHits_Object = MibTableColumn
jnxJsNatPoolHits = _JnxJsNatPoolHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 1, 6, 1, 4),
    _JnxJsNatPoolHits_Type()
)
jnxJsNatPoolHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNatPoolHits.setStatus("current")
_JnxJsNatTrapVars_ObjectIdentity = ObjectIdentity
jnxJsNatTrapVars = _JnxJsNatTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 2)
)


class _JnxJsNatAddrPoolUtil_Type(Integer32):
    """Custom type jnxJsNatAddrPoolUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxJsNatAddrPoolUtil_Type.__name__ = "Integer32"
_JnxJsNatAddrPoolUtil_Object = MibScalar
jnxJsNatAddrPoolUtil = _JnxJsNatAddrPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 2, 1),
    _JnxJsNatAddrPoolUtil_Type()
)
jnxJsNatAddrPoolUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsNatAddrPoolUtil.setStatus("current")


class _JnxJsNatTrapPoolName_Type(DisplayString):
    """Custom type jnxJsNatTrapPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxJsNatTrapPoolName_Type.__name__ = "DisplayString"
_JnxJsNatTrapPoolName_Object = MibScalar
jnxJsNatTrapPoolName = _JnxJsNatTrapPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 2, 2),
    _JnxJsNatTrapPoolName_Type()
)
jnxJsNatTrapPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsNatTrapPoolName.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsNatAddrPoolThresholdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 0, 1)
)
jnxJsNatAddrPoolThresholdStatus.setObjects(
      *(("JUNIPER-JS-NAT-MIB", "jnxJsNatSrcIpPoolName"),
        ("JUNIPER-JS-NAT-MIB", "jnxJsNatAddrPoolUtil"))
)
if mibBuilder.loadTexts:
    jnxJsNatAddrPoolThresholdStatus.setStatus(
        "deprecated"
    )

jnxJsSrcNatPoolThresholdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7, 1, 0, 2)
)
jnxJsSrcNatPoolThresholdStatus.setObjects(
      *(("JUNIPER-JS-NAT-MIB", "jnxJsNatTrapPoolName"),
        ("JUNIPER-JS-NAT-MIB", "jnxJsNatAddrPoolUtil"))
)
if mibBuilder.loadTexts:
    jnxJsSrcNatPoolThresholdStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-NAT-MIB",
    **{"jnxJsNatMIB": jnxJsNatMIB,
       "jnxJsNatNotifications": jnxJsNatNotifications,
       "jnxJsNatAddrPoolThresholdStatus": jnxJsNatAddrPoolThresholdStatus,
       "jnxJsSrcNatPoolThresholdStatus": jnxJsSrcNatPoolThresholdStatus,
       "jnxJsNatObjects": jnxJsNatObjects,
       "jnxJsSrcNatNumOfEntries": jnxJsSrcNatNumOfEntries,
       "jnxJsSrcNatTable": jnxJsSrcNatTable,
       "jnxJsSrcNatEntry": jnxJsSrcNatEntry,
       "jnxJsNatSrcIpPoolName": jnxJsNatSrcIpPoolName,
       "jnxJsNatSrcGlobalAddr": jnxJsNatSrcGlobalAddr,
       "jnxJsNatSrcPortPoolType": jnxJsNatSrcPortPoolType,
       "jnxJsNatSrcNumOfPortInuse": jnxJsNatSrcNumOfPortInuse,
       "jnxJsNatSrcNumOfSessions": jnxJsNatSrcNumOfSessions,
       "jnxJsNatSrcAssocatedIf": jnxJsNatSrcAssocatedIf,
       "jnxJsNatIfSrcPoolPortTable": jnxJsNatIfSrcPoolPortTable,
       "jnxJsNatIfSrcPoolPortEntry": jnxJsNatIfSrcPoolPortEntry,
       "jnxJsNatIfSrcPoolIndex": jnxJsNatIfSrcPoolIndex,
       "jnxJsNatIfSrcPoolTotalSinglePorts": jnxJsNatIfSrcPoolTotalSinglePorts,
       "jnxJsNatIfSrcPoolAllocSinglePorts": jnxJsNatIfSrcPoolAllocSinglePorts,
       "jnxJsNatIfSrcPoolTotalTwinPorts": jnxJsNatIfSrcPoolTotalTwinPorts,
       "jnxJsNatIfSrcPoolAllocTwinPorts": jnxJsNatIfSrcPoolAllocTwinPorts,
       "jnxJsSrcNatStatsTable": jnxJsSrcNatStatsTable,
       "jnxJsSrcNatStatsEntry": jnxJsSrcNatStatsEntry,
       "jnxJsNatSrcPoolName": jnxJsNatSrcPoolName,
       "jnxJsNatSrcXlatedAddrType": jnxJsNatSrcXlatedAddrType,
       "jnxJsNatSrcXlatedAddr": jnxJsNatSrcXlatedAddr,
       "jnxJsNatSrcPoolType": jnxJsNatSrcPoolType,
       "jnxJsNatSrcNumPortInuse": jnxJsNatSrcNumPortInuse,
       "jnxJsNatSrcNumSessions": jnxJsNatSrcNumSessions,
       "jnxJsNatRuleTable": jnxJsNatRuleTable,
       "jnxJsNatRuleEntry": jnxJsNatRuleEntry,
       "jnxJsNatRuleName": jnxJsNatRuleName,
       "jnxJsNatRuleType": jnxJsNatRuleType,
       "jnxJsNatRuleTransHits": jnxJsNatRuleTransHits,
       "jnxJsNatRuleHits": jnxJsNatRuleHits,
       "jnxJsNatPoolTable": jnxJsNatPoolTable,
       "jnxJsNatPoolEntry": jnxJsNatPoolEntry,
       "jnxJsNatPoolName": jnxJsNatPoolName,
       "jnxJsNatPoolType": jnxJsNatPoolType,
       "jnxJsNatPoolTransHits": jnxJsNatPoolTransHits,
       "jnxJsNatPoolHits": jnxJsNatPoolHits,
       "jnxJsNatTrapVars": jnxJsNatTrapVars,
       "jnxJsNatAddrPoolUtil": jnxJsNatAddrPoolUtil,
       "jnxJsNatTrapPoolName": jnxJsNatTrapPoolName}
)
