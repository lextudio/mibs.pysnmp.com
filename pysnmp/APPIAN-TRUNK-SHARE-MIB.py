# SNMP MIB module (APPIAN-TRUNK-SHARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-TRUNK-SHARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:48 2024
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

(AcAdminStatus,
 acTrunks) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "acTrunks")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

acTrunksShare = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1)
)
acTrunksShare.setRevisions(
        ("1900-02-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcTrunkTimeSlots(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )



# MIB Managed Objects in the order of their OIDs

_AcTrunkSharedTable_Object = MibTable
acTrunkSharedTable = _AcTrunkSharedTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    acTrunkSharedTable.setStatus("current")
_AcTrunkSharedEntry_Object = MibTableRow
acTrunkSharedEntry = _AcTrunkSharedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1)
)
acTrunkSharedEntry.setIndexNames(
    (0, "APPIAN-TRUNK-SHARE-MIB", "acTrunkSharedIndex"),
)
if mibBuilder.loadTexts:
    acTrunkSharedEntry.setStatus("current")
_AcTrunkSharedIndex_Type = Integer32
_AcTrunkSharedIndex_Object = MibTableColumn
acTrunkSharedIndex = _AcTrunkSharedIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 1),
    _AcTrunkSharedIndex_Type()
)
acTrunkSharedIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrunkSharedIndex.setStatus("current")


class _AcTrunkSharedAdminStatus_Type(AcAdminStatus):
    """Custom type acTrunkSharedAdminStatus based on AcAdminStatus"""


_AcTrunkSharedAdminStatus_Object = MibTableColumn
acTrunkSharedAdminStatus = _AcTrunkSharedAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 2),
    _AcTrunkSharedAdminStatus_Type()
)
acTrunkSharedAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrunkSharedAdminStatus.setStatus("current")


class _AcTrunkSharedName_Type(DisplayString):
    """Custom type acTrunkSharedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcTrunkSharedName_Type.__name__ = "DisplayString"
_AcTrunkSharedName_Object = MibTableColumn
acTrunkSharedName = _AcTrunkSharedName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 3),
    _AcTrunkSharedName_Type()
)
acTrunkSharedName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrunkSharedName.setStatus("current")


class _AcTrunkSharedIdentifier_Type(Integer32):
    """Custom type acTrunkSharedIdentifier based on Integer32"""
    defaultValue = 0


_AcTrunkSharedIdentifier_Object = MibTableColumn
acTrunkSharedIdentifier = _AcTrunkSharedIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 4),
    _AcTrunkSharedIdentifier_Type()
)
acTrunkSharedIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrunkSharedIdentifier.setStatus("current")


class _AcTrunkSharedDataProtocol_Type(Integer32):
    """Custom type acTrunkSharedDataProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 1),
          ("mfr", 2),
          ("mlppp", 4),
          ("ppp", 3),
          ("tls", 5),
          ("unknown", 0))
    )


_AcTrunkSharedDataProtocol_Type.__name__ = "Integer32"
_AcTrunkSharedDataProtocol_Object = MibTableColumn
acTrunkSharedDataProtocol = _AcTrunkSharedDataProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 5),
    _AcTrunkSharedDataProtocol_Type()
)
acTrunkSharedDataProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrunkSharedDataProtocol.setStatus("current")
_AcTrunkSharedTimeslotList_Type = AcTrunkTimeSlots
_AcTrunkSharedTimeslotList_Object = MibTableColumn
acTrunkSharedTimeslotList = _AcTrunkSharedTimeslotList_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 1, 1, 1, 6),
    _AcTrunkSharedTimeslotList_Type()
)
acTrunkSharedTimeslotList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrunkSharedTimeslotList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-TRUNK-SHARE-MIB",
    **{"AcTrunkTimeSlots": AcTrunkTimeSlots,
       "acTrunksShare": acTrunksShare,
       "acTrunkSharedTable": acTrunkSharedTable,
       "acTrunkSharedEntry": acTrunkSharedEntry,
       "acTrunkSharedIndex": acTrunkSharedIndex,
       "acTrunkSharedAdminStatus": acTrunkSharedAdminStatus,
       "acTrunkSharedName": acTrunkSharedName,
       "acTrunkSharedIdentifier": acTrunkSharedIdentifier,
       "acTrunkSharedDataProtocol": acTrunkSharedDataProtocol,
       "acTrunkSharedTimeslotList": acTrunkSharedTimeslotList}
)
