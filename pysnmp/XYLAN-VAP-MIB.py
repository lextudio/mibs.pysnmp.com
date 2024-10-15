# SNMP MIB module (XYLAN-VAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-VAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:16 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

(xylanVapArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanVapArch")


# MODULE-IDENTITY


# Types definitions



class XylanVapAdminStatCodes(Integer32):
    """Custom type XylanVapAdminStatCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("partial", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XVapInfo_ObjectIdentity = ObjectIdentity
xVapInfo = _XVapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1)
)
_XVapAdmStatus_Type = XylanVapAdminStatCodes
_XVapAdmStatus_Object = MibScalar
xVapAdmStatus = _XVapAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 1),
    _XVapAdmStatus_Type()
)
xVapAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xVapAdmStatus.setStatus("mandatory")
_XVapTable_Object = MibTable
xVapTable = _XVapTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    xVapTable.setStatus("mandatory")
_XVapEntry_Object = MibTableRow
xVapEntry = _XVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1)
)
xVapEntry.setIndexNames(
    (0, "XYLAN-VAP-MIB", "xVapMACAddress"),
    (0, "XYLAN-VAP-MIB", "xVapSlot"),
    (0, "XYLAN-VAP-MIB", "xVapPort"),
)
if mibBuilder.loadTexts:
    xVapEntry.setStatus("mandatory")
_XVapPrimaryAddress_Type = IpAddress
_XVapPrimaryAddress_Object = MibTableColumn
xVapPrimaryAddress = _XVapPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 1),
    _XVapPrimaryAddress_Type()
)
xVapPrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xVapPrimaryAddress.setStatus("mandatory")
_XVapSecondaryAddress_Type = IpAddress
_XVapSecondaryAddress_Object = MibTableColumn
xVapSecondaryAddress = _XVapSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 2),
    _XVapSecondaryAddress_Type()
)
xVapSecondaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xVapSecondaryAddress.setStatus("mandatory")


class _XVapSlot_Type(Integer32):
    """Custom type xVapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XVapSlot_Type.__name__ = "Integer32"
_XVapSlot_Object = MibTableColumn
xVapSlot = _XVapSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 3),
    _XVapSlot_Type()
)
xVapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xVapSlot.setStatus("mandatory")


class _XVapPort_Type(Integer32):
    """Custom type xVapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_XVapPort_Type.__name__ = "Integer32"
_XVapPort_Object = MibTableColumn
xVapPort = _XVapPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 4),
    _XVapPort_Type()
)
xVapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xVapPort.setStatus("mandatory")
_XVapMACAddress_Type = MacAddress
_XVapMACAddress_Object = MibTableColumn
xVapMACAddress = _XVapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 5),
    _XVapMACAddress_Type()
)
xVapMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xVapMACAddress.setStatus("mandatory")
_XVapGroupId_Type = Integer32
_XVapGroupId_Object = MibTableColumn
xVapGroupId = _XVapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 6),
    _XVapGroupId_Type()
)
xVapGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xVapGroupId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-VAP-MIB",
    **{"XylanVapAdminStatCodes": XylanVapAdminStatCodes,
       "xVapInfo": xVapInfo,
       "xVapAdmStatus": xVapAdmStatus,
       "xVapTable": xVapTable,
       "xVapEntry": xVapEntry,
       "xVapPrimaryAddress": xVapPrimaryAddress,
       "xVapSecondaryAddress": xVapSecondaryAddress,
       "xVapSlot": xVapSlot,
       "xVapPort": xVapPort,
       "xVapMACAddress": xVapMACAddress,
       "xVapGroupId": xVapGroupId}
)
