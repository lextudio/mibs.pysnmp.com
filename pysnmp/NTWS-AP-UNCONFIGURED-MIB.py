# SNMP MIB module (NTWS-AP-UNCONFIGURED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-AP-UNCONFIGURED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:53 2024
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

(NtwsApSerialNum,) = mibBuilder.importSymbols(
    "NTWS-AP-TC",
    "NtwsApSerialNum")

(NtwsPhysPortNumber,) = mibBuilder.importSymbols(
    "NTWS-BASIC-TC",
    "NtwsPhysPortNumber")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsApUnconfiguredMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15)
)
ntwsApUnconfiguredMib.setRevisions(
        ("2008-11-14 00:04",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsApUnconfiguredOrphanReason(Integer32, TextualConvention):
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

_NtwsApUnconfMibObjects_ObjectIdentity = ObjectIdentity
ntwsApUnconfMibObjects = _NtwsApUnconfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1)
)
_NtwsApUnconfOrphanTable_Object = MibTable
ntwsApUnconfOrphanTable = _NtwsApUnconfOrphanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2)
)
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanTable.setStatus("current")
_NtwsApUnconfOrphanEntry_Object = MibTableRow
ntwsApUnconfOrphanEntry = _NtwsApUnconfOrphanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1)
)
ntwsApUnconfOrphanEntry.setIndexNames(
    (0, "NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApSerialNum"),
)
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanEntry.setStatus("current")
_NtwsApUnconfOrphanApSerialNum_Type = NtwsApSerialNum
_NtwsApUnconfOrphanApSerialNum_Object = MibTableColumn
ntwsApUnconfOrphanApSerialNum = _NtwsApUnconfOrphanApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 1),
    _NtwsApUnconfOrphanApSerialNum_Type()
)
ntwsApUnconfOrphanApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanApSerialNum.setStatus("current")


class _NtwsApUnconfOrphanApModelName_Type(DisplayString):
    """Custom type ntwsApUnconfOrphanApModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NtwsApUnconfOrphanApModelName_Type.__name__ = "DisplayString"
_NtwsApUnconfOrphanApModelName_Object = MibTableColumn
ntwsApUnconfOrphanApModelName = _NtwsApUnconfOrphanApModelName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 2),
    _NtwsApUnconfOrphanApModelName_Type()
)
ntwsApUnconfOrphanApModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanApModelName.setStatus("current")
_NtwsApUnconfOrphanIpAddress_Type = IpAddress
_NtwsApUnconfOrphanIpAddress_Object = MibTableColumn
ntwsApUnconfOrphanIpAddress = _NtwsApUnconfOrphanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 5),
    _NtwsApUnconfOrphanIpAddress_Type()
)
ntwsApUnconfOrphanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanIpAddress.setStatus("current")
_NtwsApUnconfOrphanPhysPortNum_Type = NtwsPhysPortNumber
_NtwsApUnconfOrphanPhysPortNum_Object = MibTableColumn
ntwsApUnconfOrphanPhysPortNum = _NtwsApUnconfOrphanPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 6),
    _NtwsApUnconfOrphanPhysPortNum_Type()
)
ntwsApUnconfOrphanPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanPhysPortNum.setStatus("current")


class _NtwsApUnconfOrphanVLANName_Type(DisplayString):
    """Custom type ntwsApUnconfOrphanVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtwsApUnconfOrphanVLANName_Type.__name__ = "DisplayString"
_NtwsApUnconfOrphanVLANName_Object = MibTableColumn
ntwsApUnconfOrphanVLANName = _NtwsApUnconfOrphanVLANName_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 7),
    _NtwsApUnconfOrphanVLANName_Type()
)
ntwsApUnconfOrphanVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanVLANName.setStatus("current")
_NtwsApUnconfOrphanReason_Type = NtwsApUnconfiguredOrphanReason
_NtwsApUnconfOrphanReason_Object = MibTableColumn
ntwsApUnconfOrphanReason = _NtwsApUnconfOrphanReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 8),
    _NtwsApUnconfOrphanReason_Type()
)
ntwsApUnconfOrphanReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanReason.setStatus("current")
_NtwsApUnconfConformance_ObjectIdentity = ObjectIdentity
ntwsApUnconfConformance = _NtwsApUnconfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2)
)
_NtwsApUnconfCompliances_ObjectIdentity = ObjectIdentity
ntwsApUnconfCompliances = _NtwsApUnconfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1)
)
_NtwsApUnconfGroups_ObjectIdentity = ObjectIdentity
ntwsApUnconfGroups = _NtwsApUnconfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2)
)

# Managed Objects groups

ntwsApUnconfOrphanBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2, 1)
)
ntwsApUnconfOrphanBasicGroup.setObjects(
      *(("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApModelName"),
        ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanIpAddress"),
        ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanPhysPortNum"),
        ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanVLANName"),
        ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanReason"))
)
if mibBuilder.loadTexts:
    ntwsApUnconfOrphanBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsApUnconfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsApUnconfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-AP-UNCONFIGURED-MIB",
    **{"NtwsApUnconfiguredOrphanReason": NtwsApUnconfiguredOrphanReason,
       "ntwsApUnconfiguredMib": ntwsApUnconfiguredMib,
       "ntwsApUnconfMibObjects": ntwsApUnconfMibObjects,
       "ntwsApUnconfOrphanTable": ntwsApUnconfOrphanTable,
       "ntwsApUnconfOrphanEntry": ntwsApUnconfOrphanEntry,
       "ntwsApUnconfOrphanApSerialNum": ntwsApUnconfOrphanApSerialNum,
       "ntwsApUnconfOrphanApModelName": ntwsApUnconfOrphanApModelName,
       "ntwsApUnconfOrphanIpAddress": ntwsApUnconfOrphanIpAddress,
       "ntwsApUnconfOrphanPhysPortNum": ntwsApUnconfOrphanPhysPortNum,
       "ntwsApUnconfOrphanVLANName": ntwsApUnconfOrphanVLANName,
       "ntwsApUnconfOrphanReason": ntwsApUnconfOrphanReason,
       "ntwsApUnconfConformance": ntwsApUnconfConformance,
       "ntwsApUnconfCompliances": ntwsApUnconfCompliances,
       "ntwsApUnconfCompliance": ntwsApUnconfCompliance,
       "ntwsApUnconfGroups": ntwsApUnconfGroups,
       "ntwsApUnconfOrphanBasicGroup": ntwsApUnconfOrphanBasicGroup}
)
