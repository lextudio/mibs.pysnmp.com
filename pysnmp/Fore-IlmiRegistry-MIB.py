# SNMP MIB module (Fore-IlmiRegistry-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-IlmiRegistry-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:05 2024
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

(AtmAddress,
 ilmiRegistry) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "AtmAddress",
    "ilmiRegistry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ilmiRegistryModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdminIlmiRegTable_Object = MibTable
adminIlmiRegTable = _AdminIlmiRegTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1)
)
if mibBuilder.loadTexts:
    adminIlmiRegTable.setStatus("current")
_AdminIlmiRegEntry_Object = MibTableRow
adminIlmiRegEntry = _AdminIlmiRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1, 1)
)
adminIlmiRegEntry.setIndexNames(
    (0, "Fore-IlmiRegistry-MIB", "adminIlmiRegPort"),
    (0, "Fore-IlmiRegistry-MIB", "adminIlmiRegServiceID"),
    (0, "Fore-IlmiRegistry-MIB", "adminIlmiRegAddressIndex"),
)
if mibBuilder.loadTexts:
    adminIlmiRegEntry.setStatus("current")


class _AdminIlmiRegPort_Type(Integer32):
    """Custom type adminIlmiRegPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdminIlmiRegPort_Type.__name__ = "Integer32"
_AdminIlmiRegPort_Object = MibTableColumn
adminIlmiRegPort = _AdminIlmiRegPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1, 1, 1),
    _AdminIlmiRegPort_Type()
)
adminIlmiRegPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminIlmiRegPort.setStatus("current")
_AdminIlmiRegServiceID_Type = ObjectIdentifier
_AdminIlmiRegServiceID_Object = MibTableColumn
adminIlmiRegServiceID = _AdminIlmiRegServiceID_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1, 1, 2),
    _AdminIlmiRegServiceID_Type()
)
adminIlmiRegServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminIlmiRegServiceID.setStatus("current")
_AdminIlmiRegATMAddress_Type = AtmAddress
_AdminIlmiRegATMAddress_Object = MibTableColumn
adminIlmiRegATMAddress = _AdminIlmiRegATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1, 1, 3),
    _AdminIlmiRegATMAddress_Type()
)
adminIlmiRegATMAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminIlmiRegATMAddress.setStatus("current")


class _AdminIlmiRegAddressIndex_Type(Integer32):
    """Custom type adminIlmiRegAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdminIlmiRegAddressIndex_Type.__name__ = "Integer32"
_AdminIlmiRegAddressIndex_Object = MibTableColumn
adminIlmiRegAddressIndex = _AdminIlmiRegAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1, 1, 4),
    _AdminIlmiRegAddressIndex_Type()
)
adminIlmiRegAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminIlmiRegAddressIndex.setStatus("current")


class _AdminIlmiRegParm1_Type(OctetString):
    """Custom type adminIlmiRegParm1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AdminIlmiRegParm1_Type.__name__ = "OctetString"
_AdminIlmiRegParm1_Object = MibTableColumn
adminIlmiRegParm1 = _AdminIlmiRegParm1_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1, 1, 5),
    _AdminIlmiRegParm1_Type()
)
adminIlmiRegParm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminIlmiRegParm1.setStatus("current")
_AdminIlmiRegRowStatus_Type = RowStatus
_AdminIlmiRegRowStatus_Object = MibTableColumn
adminIlmiRegRowStatus = _AdminIlmiRegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 14, 1, 1, 6),
    _AdminIlmiRegRowStatus_Type()
)
adminIlmiRegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adminIlmiRegRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-IlmiRegistry-MIB",
    **{"adminIlmiRegTable": adminIlmiRegTable,
       "adminIlmiRegEntry": adminIlmiRegEntry,
       "adminIlmiRegPort": adminIlmiRegPort,
       "adminIlmiRegServiceID": adminIlmiRegServiceID,
       "adminIlmiRegATMAddress": adminIlmiRegATMAddress,
       "adminIlmiRegAddressIndex": adminIlmiRegAddressIndex,
       "adminIlmiRegParm1": adminIlmiRegParm1,
       "adminIlmiRegRowStatus": adminIlmiRegRowStatus,
       "ilmiRegistryModule": ilmiRegistryModule}
)
