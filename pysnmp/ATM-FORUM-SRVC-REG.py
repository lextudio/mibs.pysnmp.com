# SNMP MIB module (ATM-FORUM-SRVC-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-FORUM-SRVC-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:56 2024
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

(atmForumAdmin,
 atmForumUni) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "atmForumAdmin",
    "atmForumUni")

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


# Types definitions



class AtmAddress(OctetString):
    """Custom type AtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmfSrvcRegTypes_ObjectIdentity = ObjectIdentity
atmfSrvcRegTypes = _AtmfSrvcRegTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 5)
)
_AtmfSrvcRegLecs_ObjectIdentity = ObjectIdentity
atmfSrvcRegLecs = _AtmfSrvcRegLecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 1, 5, 1)
)
_AtmfSrvcRegistryGroup_ObjectIdentity = ObjectIdentity
atmfSrvcRegistryGroup = _AtmfSrvcRegistryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 8)
)
_AtmfSrvcRegTable_Object = MibTable
atmfSrvcRegTable = _AtmfSrvcRegTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1)
)
if mibBuilder.loadTexts:
    atmfSrvcRegTable.setStatus("mandatory")
_AtmfSrvcRegEntry_Object = MibTableRow
atmfSrvcRegEntry = _AtmfSrvcRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1)
)
atmfSrvcRegEntry.setIndexNames(
    (0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegPort"),
    (0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegServiceID"),
    (0, "ATM-FORUM-SRVC-REG", "atmfSrvcAddressIndex"),
)
if mibBuilder.loadTexts:
    atmfSrvcRegEntry.setStatus("mandatory")


class _AtmfSrvcRegPort_Type(Integer32):
    """Custom type atmfSrvcRegPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfSrvcRegPort_Type.__name__ = "Integer32"
_AtmfSrvcRegPort_Object = MibTableColumn
atmfSrvcRegPort = _AtmfSrvcRegPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 1),
    _AtmfSrvcRegPort_Type()
)
atmfSrvcRegPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfSrvcRegPort.setStatus("mandatory")
_AtmfSrvcRegServiceID_Type = ObjectIdentifier
_AtmfSrvcRegServiceID_Object = MibTableColumn
atmfSrvcRegServiceID = _AtmfSrvcRegServiceID_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 2),
    _AtmfSrvcRegServiceID_Type()
)
atmfSrvcRegServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfSrvcRegServiceID.setStatus("mandatory")
_AtmfSrvcRegATMAddress_Type = AtmAddress
_AtmfSrvcRegATMAddress_Object = MibTableColumn
atmfSrvcRegATMAddress = _AtmfSrvcRegATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 3),
    _AtmfSrvcRegATMAddress_Type()
)
atmfSrvcRegATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfSrvcRegATMAddress.setStatus("mandatory")
_AtmfSrvcRegAddressIndex_Type = Integer32
_AtmfSrvcRegAddressIndex_Object = MibTableColumn
atmfSrvcRegAddressIndex = _AtmfSrvcRegAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 4),
    _AtmfSrvcRegAddressIndex_Type()
)
atmfSrvcRegAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfSrvcRegAddressIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-FORUM-SRVC-REG",
    **{"AtmAddress": AtmAddress,
       "atmfSrvcRegTypes": atmfSrvcRegTypes,
       "atmfSrvcRegLecs": atmfSrvcRegLecs,
       "atmfSrvcRegistryGroup": atmfSrvcRegistryGroup,
       "atmfSrvcRegTable": atmfSrvcRegTable,
       "atmfSrvcRegEntry": atmfSrvcRegEntry,
       "atmfSrvcRegPort": atmfSrvcRegPort,
       "atmfSrvcRegServiceID": atmfSrvcRegServiceID,
       "atmfSrvcRegATMAddress": atmfSrvcRegATMAddress,
       "atmfSrvcRegAddressIndex": atmfSrvcRegAddressIndex}
)
