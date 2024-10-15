# SNMP MIB module (INTEL-ES480-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-ES480-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:37 2024
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

(es480tAgent,) = mibBuilder.importSymbols(
    "INTEL-ES480-MIB",
    "es480tAgent")

(es480tVlanIfIndex,) = mibBuilder.importSymbols(
    "INTEL-ES480-VLAN-MIB",
    "es480tVlanIfIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

es480tQos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Es480tQosCommon_ObjectIdentity = ObjectIdentity
es480tQosCommon = _Es480tQosCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1)
)


class _Es480tQosMode_Type(Integer32):
    """Custom type es480tQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_Es480tQosMode_Type.__name__ = "Integer32"
_Es480tQosMode_Object = MibScalar
es480tQosMode = _Es480tQosMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 4),
    _Es480tQosMode_Type()
)
es480tQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosMode.setStatus("mandatory")
_Es480tQosUnconfigure_Type = TruthValue
_Es480tQosUnconfigure_Object = MibScalar
es480tQosUnconfigure = _Es480tQosUnconfigure_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 5),
    _Es480tQosUnconfigure_Type()
)
es480tQosUnconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosUnconfigure.setStatus("mandatory")
_Es480tQosProfileTable_Object = MibTable
es480tQosProfileTable = _Es480tQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6)
)
if mibBuilder.loadTexts:
    es480tQosProfileTable.setStatus("mandatory")
_Es480tQosProfileEntry_Object = MibTableRow
es480tQosProfileEntry = _Es480tQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1)
)
es480tQosProfileEntry.setIndexNames(
    (0, "INTEL-ES480-QOS-MIB", "es480tQosProfileIndex"),
)
if mibBuilder.loadTexts:
    es480tQosProfileEntry.setStatus("mandatory")


class _Es480tQosProfileIndex_Type(Integer32):
    """Custom type es480tQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es480tQosProfileIndex_Type.__name__ = "Integer32"
_Es480tQosProfileIndex_Object = MibTableColumn
es480tQosProfileIndex = _Es480tQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 1),
    _Es480tQosProfileIndex_Type()
)
es480tQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosProfileIndex.setStatus("mandatory")


class _Es480tQosProfileName_Type(DisplayString):
    """Custom type es480tQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Es480tQosProfileName_Type.__name__ = "DisplayString"
_Es480tQosProfileName_Object = MibTableColumn
es480tQosProfileName = _Es480tQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 2),
    _Es480tQosProfileName_Type()
)
es480tQosProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosProfileName.setStatus("mandatory")
_Es480tQosProfileMinBw_Type = Integer32
_Es480tQosProfileMinBw_Object = MibTableColumn
es480tQosProfileMinBw = _Es480tQosProfileMinBw_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 3),
    _Es480tQosProfileMinBw_Type()
)
es480tQosProfileMinBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosProfileMinBw.setStatus("mandatory")
_Es480tQosProfileMaxBw_Type = Integer32
_Es480tQosProfileMaxBw_Object = MibTableColumn
es480tQosProfileMaxBw = _Es480tQosProfileMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 4),
    _Es480tQosProfileMaxBw_Type()
)
es480tQosProfileMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosProfileMaxBw.setStatus("mandatory")


class _Es480tQosProfilePriority_Type(Integer32):
    """Custom type es480tQosProfilePriority based on Integer32"""
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
        *(("high", 7),
          ("highHi", 8),
          ("low", 1),
          ("lowNormal", 2),
          ("medium", 5),
          ("mediumHi", 6),
          ("normal", 3),
          ("normalMedium", 4))
    )


_Es480tQosProfilePriority_Type.__name__ = "Integer32"
_Es480tQosProfilePriority_Object = MibTableColumn
es480tQosProfilePriority = _Es480tQosProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 5),
    _Es480tQosProfilePriority_Type()
)
es480tQosProfilePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosProfilePriority.setStatus("mandatory")
_Es480tQosProfileRowStatus_Type = RowStatus
_Es480tQosProfileRowStatus_Object = MibTableColumn
es480tQosProfileRowStatus = _Es480tQosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 6),
    _Es480tQosProfileRowStatus_Type()
)
es480tQosProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosProfileRowStatus.setStatus("mandatory")
_Es480tQosByVlanMappingTable_Object = MibTable
es480tQosByVlanMappingTable = _Es480tQosByVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 7)
)
if mibBuilder.loadTexts:
    es480tQosByVlanMappingTable.setStatus("mandatory")
_Es480tQosByVlanMappingEntry_Object = MibTableRow
es480tQosByVlanMappingEntry = _Es480tQosByVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 7, 1)
)
es480tQosByVlanMappingEntry.setIndexNames(
    (0, "INTEL-ES480-VLAN-MIB", "es480tVlanIfIndex"),
)
if mibBuilder.loadTexts:
    es480tQosByVlanMappingEntry.setStatus("mandatory")


class _Es480tQosByVlanMappingQosProfileIndex_Type(Integer32):
    """Custom type es480tQosByVlanMappingQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Es480tQosByVlanMappingQosProfileIndex_Type.__name__ = "Integer32"
_Es480tQosByVlanMappingQosProfileIndex_Object = MibTableColumn
es480tQosByVlanMappingQosProfileIndex = _Es480tQosByVlanMappingQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 7, 1, 1),
    _Es480tQosByVlanMappingQosProfileIndex_Type()
)
es480tQosByVlanMappingQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tQosByVlanMappingQosProfileIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-ES480-QOS-MIB",
    **{"es480tQos": es480tQos,
       "es480tQosCommon": es480tQosCommon,
       "es480tQosMode": es480tQosMode,
       "es480tQosUnconfigure": es480tQosUnconfigure,
       "es480tQosProfileTable": es480tQosProfileTable,
       "es480tQosProfileEntry": es480tQosProfileEntry,
       "es480tQosProfileIndex": es480tQosProfileIndex,
       "es480tQosProfileName": es480tQosProfileName,
       "es480tQosProfileMinBw": es480tQosProfileMinBw,
       "es480tQosProfileMaxBw": es480tQosProfileMaxBw,
       "es480tQosProfilePriority": es480tQosProfilePriority,
       "es480tQosProfileRowStatus": es480tQosProfileRowStatus,
       "es480tQosByVlanMappingTable": es480tQosByVlanMappingTable,
       "es480tQosByVlanMappingEntry": es480tQosByVlanMappingEntry,
       "es480tQosByVlanMappingQosProfileIndex": es480tQosByVlanMappingQosProfileIndex}
)
