# SNMP MIB module (ELTEX-MES-IpRouter) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-IpRouter
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:48 2024
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

(eltMesOspf,) = mibBuilder.importSymbols(
    "ELTEX-MES-IP",
    "eltMesOspf")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltOspfAuthTable_Object = MibTable
eltOspfAuthTable = _EltOspfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1)
)
if mibBuilder.loadTexts:
    eltOspfAuthTable.setStatus("current")
_EltOspfAuthEntry_Object = MibTableRow
eltOspfAuthEntry = _EltOspfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1)
)
eltOspfAuthEntry.setIndexNames(
    (0, "ELTEX-MES-IpRouter", "eltOspfIfIpAddress"),
    (0, "ELTEX-MES-IpRouter", "eltOspfAuthKeyId"),
)
if mibBuilder.loadTexts:
    eltOspfAuthEntry.setStatus("current")
_EltOspfIfIpAddress_Type = IpAddress
_EltOspfIfIpAddress_Object = MibTableColumn
eltOspfIfIpAddress = _EltOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 1),
    _EltOspfIfIpAddress_Type()
)
eltOspfIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltOspfIfIpAddress.setStatus("current")
_EltOspfAuthKeyId_Type = Unsigned32
_EltOspfAuthKeyId_Object = MibTableColumn
eltOspfAuthKeyId = _EltOspfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 2),
    _EltOspfAuthKeyId_Type()
)
eltOspfAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltOspfAuthKeyId.setStatus("current")


class _EltOspfAuthKey_Type(OctetString):
    """Custom type eltOspfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EltOspfAuthKey_Type.__name__ = "OctetString"
_EltOspfAuthKey_Object = MibTableColumn
eltOspfAuthKey = _EltOspfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 3),
    _EltOspfAuthKey_Type()
)
eltOspfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltOspfAuthKey.setStatus("current")
_EltOspfAuthStatus_Type = RowStatus
_EltOspfAuthStatus_Object = MibTableColumn
eltOspfAuthStatus = _EltOspfAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 1, 1, 4),
    _EltOspfAuthStatus_Type()
)
eltOspfAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltOspfAuthStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IpRouter",
    **{"eltOspfAuthTable": eltOspfAuthTable,
       "eltOspfAuthEntry": eltOspfAuthEntry,
       "eltOspfIfIpAddress": eltOspfIfIpAddress,
       "eltOspfAuthKeyId": eltOspfAuthKeyId,
       "eltOspfAuthKey": eltOspfAuthKey,
       "eltOspfAuthStatus": eltOspfAuthStatus}
)
