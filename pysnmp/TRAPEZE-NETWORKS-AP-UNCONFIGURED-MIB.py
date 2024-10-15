# SNMP MIB module (TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:28 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(TrpzApSerialNum,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzApSerialNum")

(TrpzPhysPortNumber,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzPhysPortNumber")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzApUnconfiguredMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15)
)
trpzApUnconfiguredMib.setRevisions(
        ("2011-06-15 00:11",
         "2008-11-14 00:04")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzApUnconfiguredOrphanReason(Integer32, TextualConvention):
    status = "current"
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
        *(("ap-license-exceeded", 3),
          ("ap-model-mismatch", 5),
          ("controller-behind-nat", 4),
          ("no-configuration", 2),
          ("no-macs", 6),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzApUnconfMibObjects_ObjectIdentity = ObjectIdentity
trpzApUnconfMibObjects = _TrpzApUnconfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1)
)
_TrpzApUnconfOrphanTable_Object = MibTable
trpzApUnconfOrphanTable = _TrpzApUnconfOrphanTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2)
)
if mibBuilder.loadTexts:
    trpzApUnconfOrphanTable.setStatus("current")
_TrpzApUnconfOrphanEntry_Object = MibTableRow
trpzApUnconfOrphanEntry = _TrpzApUnconfOrphanEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1)
)
trpzApUnconfOrphanEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApSerialNum"),
)
if mibBuilder.loadTexts:
    trpzApUnconfOrphanEntry.setStatus("current")
_TrpzApUnconfOrphanApSerialNum_Type = TrpzApSerialNum
_TrpzApUnconfOrphanApSerialNum_Object = MibTableColumn
trpzApUnconfOrphanApSerialNum = _TrpzApUnconfOrphanApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 1),
    _TrpzApUnconfOrphanApSerialNum_Type()
)
trpzApUnconfOrphanApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanApSerialNum.setStatus("current")


class _TrpzApUnconfOrphanApModelName_Type(DisplayString):
    """Custom type trpzApUnconfOrphanApModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_TrpzApUnconfOrphanApModelName_Type.__name__ = "DisplayString"
_TrpzApUnconfOrphanApModelName_Object = MibTableColumn
trpzApUnconfOrphanApModelName = _TrpzApUnconfOrphanApModelName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 2),
    _TrpzApUnconfOrphanApModelName_Type()
)
trpzApUnconfOrphanApModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanApModelName.setStatus("current")
_TrpzApUnconfOrphanIpAddress_Type = IpAddress
_TrpzApUnconfOrphanIpAddress_Object = MibTableColumn
trpzApUnconfOrphanIpAddress = _TrpzApUnconfOrphanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 5),
    _TrpzApUnconfOrphanIpAddress_Type()
)
trpzApUnconfOrphanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanIpAddress.setStatus("current")
_TrpzApUnconfOrphanPhysPortNum_Type = TrpzPhysPortNumber
_TrpzApUnconfOrphanPhysPortNum_Object = MibTableColumn
trpzApUnconfOrphanPhysPortNum = _TrpzApUnconfOrphanPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 6),
    _TrpzApUnconfOrphanPhysPortNum_Type()
)
trpzApUnconfOrphanPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanPhysPortNum.setStatus("current")


class _TrpzApUnconfOrphanVLANName_Type(DisplayString):
    """Custom type trpzApUnconfOrphanVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrpzApUnconfOrphanVLANName_Type.__name__ = "DisplayString"
_TrpzApUnconfOrphanVLANName_Object = MibTableColumn
trpzApUnconfOrphanVLANName = _TrpzApUnconfOrphanVLANName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 7),
    _TrpzApUnconfOrphanVLANName_Type()
)
trpzApUnconfOrphanVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanVLANName.setStatus("current")
_TrpzApUnconfOrphanReason_Type = TrpzApUnconfiguredOrphanReason
_TrpzApUnconfOrphanReason_Object = MibTableColumn
trpzApUnconfOrphanReason = _TrpzApUnconfOrphanReason_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 8),
    _TrpzApUnconfOrphanReason_Type()
)
trpzApUnconfOrphanReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzApUnconfOrphanReason.setStatus("current")
_TrpzApUnconfConformance_ObjectIdentity = ObjectIdentity
trpzApUnconfConformance = _TrpzApUnconfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2)
)
_TrpzApUnconfCompliances_ObjectIdentity = ObjectIdentity
trpzApUnconfCompliances = _TrpzApUnconfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1)
)
_TrpzApUnconfGroups_ObjectIdentity = ObjectIdentity
trpzApUnconfGroups = _TrpzApUnconfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2)
)

# Managed Objects groups

trpzApUnconfOrphanBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2, 1)
)
trpzApUnconfOrphanBasicGroup.setObjects(
      *(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApModelName"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanIpAddress"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanPhysPortNum"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanVLANName"),
        ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanReason"))
)
if mibBuilder.loadTexts:
    trpzApUnconfOrphanBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzApUnconfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzApUnconfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB",
    **{"TrpzApUnconfiguredOrphanReason": TrpzApUnconfiguredOrphanReason,
       "trpzApUnconfiguredMib": trpzApUnconfiguredMib,
       "trpzApUnconfMibObjects": trpzApUnconfMibObjects,
       "trpzApUnconfOrphanTable": trpzApUnconfOrphanTable,
       "trpzApUnconfOrphanEntry": trpzApUnconfOrphanEntry,
       "trpzApUnconfOrphanApSerialNum": trpzApUnconfOrphanApSerialNum,
       "trpzApUnconfOrphanApModelName": trpzApUnconfOrphanApModelName,
       "trpzApUnconfOrphanIpAddress": trpzApUnconfOrphanIpAddress,
       "trpzApUnconfOrphanPhysPortNum": trpzApUnconfOrphanPhysPortNum,
       "trpzApUnconfOrphanVLANName": trpzApUnconfOrphanVLANName,
       "trpzApUnconfOrphanReason": trpzApUnconfOrphanReason,
       "trpzApUnconfConformance": trpzApUnconfConformance,
       "trpzApUnconfCompliances": trpzApUnconfCompliances,
       "trpzApUnconfCompliance": trpzApUnconfCompliance,
       "trpzApUnconfGroups": trpzApUnconfGroups,
       "trpzApUnconfOrphanBasicGroup": trpzApUnconfOrphanBasicGroup}
)
