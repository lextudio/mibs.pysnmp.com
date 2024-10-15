# SNMP MIB module (RADLAN-SMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-SMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:22 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 84)
)
rlSmon.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CopyModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor-only", 1),
          ("network", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlPortCopyMibVersion_Type = Integer32
_RlPortCopyMibVersion_Object = MibScalar
rlPortCopyMibVersion = _RlPortCopyMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 1),
    _RlPortCopyMibVersion_Type()
)
rlPortCopyMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortCopyMibVersion.setStatus("current")


class _RlPortCopySupport_Type(Integer32):
    """Custom type rlPortCopySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_RlPortCopySupport_Type.__name__ = "Integer32"
_RlPortCopySupport_Object = MibScalar
rlPortCopySupport = _RlPortCopySupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 2),
    _RlPortCopySupport_Type()
)
rlPortCopySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortCopySupport.setStatus("current")
_RlPortCopyVlanTaggingTable_Object = MibTable
rlPortCopyVlanTaggingTable = _RlPortCopyVlanTaggingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 3)
)
if mibBuilder.loadTexts:
    rlPortCopyVlanTaggingTable.setStatus("current")
_RlPortCopyVlanTaggingEntry_Object = MibTableRow
rlPortCopyVlanTaggingEntry = _RlPortCopyVlanTaggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 3, 1)
)
rlPortCopyVlanTaggingEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortCopyVlanTaggingEntry.setStatus("current")


class _RlPortCopyVlanTagging_Type(TruthValue):
    """Custom type rlPortCopyVlanTagging based on TruthValue"""


_RlPortCopyVlanTagging_Object = MibTableColumn
rlPortCopyVlanTagging = _RlPortCopyVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 3, 1, 1),
    _RlPortCopyVlanTagging_Type()
)
rlPortCopyVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortCopyVlanTagging.setStatus("current")
_RlPortCopyMode_Type = CopyModeType
_RlPortCopyMode_Object = MibScalar
rlPortCopyMode = _RlPortCopyMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 4),
    _RlPortCopyMode_Type()
)
rlPortCopyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortCopyMode.setStatus("current")


class _RlPortCopySessionsEnabled_Type(TruthValue):
    """Custom type rlPortCopySessionsEnabled based on TruthValue"""


_RlPortCopySessionsEnabled_Object = MibScalar
rlPortCopySessionsEnabled = _RlPortCopySessionsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 84, 5),
    _RlPortCopySessionsEnabled_Type()
)
rlPortCopySessionsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortCopySessionsEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SMON-MIB",
    **{"CopyModeType": CopyModeType,
       "rlSmon": rlSmon,
       "rlPortCopyMibVersion": rlPortCopyMibVersion,
       "rlPortCopySupport": rlPortCopySupport,
       "rlPortCopyVlanTaggingTable": rlPortCopyVlanTaggingTable,
       "rlPortCopyVlanTaggingEntry": rlPortCopyVlanTaggingEntry,
       "rlPortCopyVlanTagging": rlPortCopyVlanTagging,
       "rlPortCopyMode": rlPortCopyMode,
       "rlPortCopySessionsEnabled": rlPortCopySessionsEnabled}
)
