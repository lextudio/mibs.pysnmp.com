# SNMP MIB module (BAY-STACK-ERROR-MESSAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-ERROR-MESSAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:57 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackErrorMessageMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 19)
)
bayStackErrorMessageMib.setRevisions(
        ("2013-10-11 00:00",
         "2006-11-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsemObjects_ObjectIdentity = ObjectIdentity
bsemObjects = _BsemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 19, 1)
)
_BsemErrorMessageTable_Object = MibTable
bsemErrorMessageTable = _BsemErrorMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1)
)
if mibBuilder.loadTexts:
    bsemErrorMessageTable.setStatus("current")
_BsemErrorMessageEntry_Object = MibTableRow
bsemErrorMessageEntry = _BsemErrorMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1)
)
bsemErrorMessageEntry.setIndexNames(
    (0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageAddressType"),
    (0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageAddress"),
    (0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageRequestId"),
)
if mibBuilder.loadTexts:
    bsemErrorMessageEntry.setStatus("current")
_BsemErrorMessageAddressType_Type = InetAddressType
_BsemErrorMessageAddressType_Object = MibTableColumn
bsemErrorMessageAddressType = _BsemErrorMessageAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 1),
    _BsemErrorMessageAddressType_Type()
)
bsemErrorMessageAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsemErrorMessageAddressType.setStatus("current")
_BsemErrorMessageAddress_Type = InetAddress
_BsemErrorMessageAddress_Object = MibTableColumn
bsemErrorMessageAddress = _BsemErrorMessageAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 2),
    _BsemErrorMessageAddress_Type()
)
bsemErrorMessageAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsemErrorMessageAddress.setStatus("current")
_BsemErrorMessageRequestId_Type = Unsigned32
_BsemErrorMessageRequestId_Object = MibTableColumn
bsemErrorMessageRequestId = _BsemErrorMessageRequestId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 3),
    _BsemErrorMessageRequestId_Type()
)
bsemErrorMessageRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsemErrorMessageRequestId.setStatus("current")
_BsemErrorMessageString_Type = DisplayString
_BsemErrorMessageString_Object = MibTableColumn
bsemErrorMessageString = _BsemErrorMessageString_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 4),
    _BsemErrorMessageString_Type()
)
bsemErrorMessageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsemErrorMessageString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-ERROR-MESSAGE-MIB",
    **{"bayStackErrorMessageMib": bayStackErrorMessageMib,
       "bsemObjects": bsemObjects,
       "bsemErrorMessageTable": bsemErrorMessageTable,
       "bsemErrorMessageEntry": bsemErrorMessageEntry,
       "bsemErrorMessageAddressType": bsemErrorMessageAddressType,
       "bsemErrorMessageAddress": bsemErrorMessageAddress,
       "bsemErrorMessageRequestId": bsemErrorMessageRequestId,
       "bsemErrorMessageString": bsemErrorMessageString}
)
