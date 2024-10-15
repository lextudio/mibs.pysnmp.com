# SNMP MIB module (TERAWAVE-teraAccess-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraAccess-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:12 2024
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

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraAccess_ObjectIdentity = ObjectIdentity
teraAccess = _TeraAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 24)
)
_TeraUserProfilesTable_Object = MibTable
teraUserProfilesTable = _TeraUserProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1)
)
if mibBuilder.loadTexts:
    teraUserProfilesTable.setStatus("mandatory")
_TeraUserProfilesTableEntry_Object = MibTableRow
teraUserProfilesTableEntry = _TeraUserProfilesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1, 1)
)
teraUserProfilesTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAccess-MIB", "teraUserProfileIndex"),
)
if mibBuilder.loadTexts:
    teraUserProfilesTableEntry.setStatus("mandatory")
_TeraUserProfileIndex_Type = Integer32
_TeraUserProfileIndex_Object = MibTableColumn
teraUserProfileIndex = _TeraUserProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1, 1, 1),
    _TeraUserProfileIndex_Type()
)
teraUserProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUserProfileIndex.setStatus("mandatory")
_TeraUserProfileName_Type = OctetString
_TeraUserProfileName_Object = MibTableColumn
teraUserProfileName = _TeraUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1, 1, 2),
    _TeraUserProfileName_Type()
)
teraUserProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUserProfileName.setStatus("mandatory")
_TeraUserProfilePassword_Type = OctetString
_TeraUserProfilePassword_Object = MibTableColumn
teraUserProfilePassword = _TeraUserProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1, 1, 3),
    _TeraUserProfilePassword_Type()
)
teraUserProfilePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUserProfilePassword.setStatus("mandatory")


class _TeraUserProfileAccessLevel_Type(Integer32):
    """Custom type teraUserProfileAccessLevel based on Integer32"""
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
        *(("admin", 1),
          ("oper", 2),
          ("test", 3),
          ("view", 4))
    )


_TeraUserProfileAccessLevel_Type.__name__ = "Integer32"
_TeraUserProfileAccessLevel_Object = MibTableColumn
teraUserProfileAccessLevel = _TeraUserProfileAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1, 1, 4),
    _TeraUserProfileAccessLevel_Type()
)
teraUserProfileAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUserProfileAccessLevel.setStatus("mandatory")


class _TeraUserProfileStatus_Type(Integer32):
    """Custom type teraUserProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_TeraUserProfileStatus_Type.__name__ = "Integer32"
_TeraUserProfileStatus_Object = MibTableColumn
teraUserProfileStatus = _TeraUserProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1, 1, 5),
    _TeraUserProfileStatus_Type()
)
teraUserProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUserProfileStatus.setStatus("mandatory")
_TeraUserProfileClear_Type = Integer32
_TeraUserProfileClear_Object = MibScalar
teraUserProfileClear = _TeraUserProfileClear_Object(
    (1, 3, 6, 1, 4, 1, 4513, 24, 1, 2),
    _TeraUserProfileClear_Type()
)
teraUserProfileClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUserProfileClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraAccess-MIB",
    **{"terawave": terawave,
       "teraAccess": teraAccess,
       "teraUserProfilesTable": teraUserProfilesTable,
       "teraUserProfilesTableEntry": teraUserProfilesTableEntry,
       "teraUserProfileIndex": teraUserProfileIndex,
       "teraUserProfileName": teraUserProfileName,
       "teraUserProfilePassword": teraUserProfilePassword,
       "teraUserProfileAccessLevel": teraUserProfileAccessLevel,
       "teraUserProfileStatus": teraUserProfileStatus,
       "teraUserProfileClear": teraUserProfileClear}
)
