# SNMP MIB module (CXVSHELL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXVSHELL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:01 2024
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

(cxMc600,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxMc600")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxVShell_ObjectIdentity = ObjectIdentity
cxVShell = _CxVShell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3)
)
_VoxCardsMapTable_Object = MibTable
voxCardsMapTable = _VoxCardsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    voxCardsMapTable.setStatus("mandatory")
_VoxCardsMapEntry_Object = MibTableRow
voxCardsMapEntry = _VoxCardsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3, 1, 1)
)
voxCardsMapEntry.setIndexNames(
    (0, "CXVSHELL-MIB", "voxCardNo"),
)
if mibBuilder.loadTexts:
    voxCardsMapEntry.setStatus("mandatory")


class _VoxCardNo_Type(Integer32):
    """Custom type voxCardNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VoxCardNo_Type.__name__ = "Integer32"
_VoxCardNo_Object = MibTableColumn
voxCardNo = _VoxCardNo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3, 1, 1, 1),
    _VoxCardNo_Type()
)
voxCardNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voxCardNo.setStatus("mandatory")


class _VoxSlotNo_Type(Integer32):
    """Custom type voxSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VoxSlotNo_Type.__name__ = "Integer32"
_VoxSlotNo_Object = MibTableColumn
voxSlotNo = _VoxSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3, 1, 1, 2),
    _VoxSlotNo_Type()
)
voxSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voxSlotNo.setStatus("mandatory")


class _VoxConnStatus_Type(Integer32):
    """Custom type voxConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("failed", 2),
          ("recorded-in-config", 1))
    )


_VoxConnStatus_Type.__name__ = "Integer32"
_VoxConnStatus_Object = MibTableColumn
voxConnStatus = _VoxConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3, 1, 1, 3),
    _VoxConnStatus_Type()
)
voxConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voxConnStatus.setStatus("mandatory")


class _VoxCardRowStatus_Type(Integer32):
    """Custom type voxCardRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_VoxCardRowStatus_Type.__name__ = "Integer32"
_VoxCardRowStatus_Object = MibTableColumn
voxCardRowStatus = _VoxCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3, 1, 1, 4),
    _VoxCardRowStatus_Type()
)
voxCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voxCardRowStatus.setStatus("mandatory")


class _CxvshellMibLevel_Type(Integer32):
    """Custom type cxvshellMibLevel based on Integer32"""
    defaultValue = 0


_CxvshellMibLevel_Object = MibScalar
cxvshellMibLevel = _CxvshellMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 1, 3, 2),
    _CxvshellMibLevel_Type()
)
cxvshellMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxvshellMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXVSHELL-MIB",
    **{"cxVShell": cxVShell,
       "voxCardsMapTable": voxCardsMapTable,
       "voxCardsMapEntry": voxCardsMapEntry,
       "voxCardNo": voxCardNo,
       "voxSlotNo": voxSlotNo,
       "voxConnStatus": voxConnStatus,
       "voxCardRowStatus": voxCardRowStatus,
       "cxvshellMibLevel": cxvshellMibLevel}
)
