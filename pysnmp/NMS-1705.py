# SNMP MIB module (NMS-1705) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-1705
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:36 2024
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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

nms1705MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nms1705Objects_ObjectIdentity = ObjectIdentity
nms1705Objects = _Nms1705Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1)
)
_AdslLineTable_Object = MibTable
adslLineTable = _AdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 1)
)
if mibBuilder.loadTexts:
    adslLineTable.setStatus("mandatory")
_AdslLineEntry_Object = MibTableRow
adslLineEntry = _AdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 1, 1)
)
adslLineEntry.setIndexNames(
    (0, "NMS-1705", "adslLineNumber"),
)
if mibBuilder.loadTexts:
    adslLineEntry.setStatus("mandatory")
_AdslLineUser_Type = DisplayString
_AdslLineUser_Object = MibTableColumn
adslLineUser = _AdslLineUser_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 1, 1, 1),
    _AdslLineUser_Type()
)
adslLineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineUser.setStatus("mandatory")
_AdslProductID_Type = DisplayString
_AdslProductID_Object = MibTableColumn
adslProductID = _AdslProductID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 1, 1, 2),
    _AdslProductID_Type()
)
adslProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslProductID.setStatus("mandatory")
_AdslConfigAddr_Type = IpAddress
_AdslConfigAddr_Object = MibTableColumn
adslConfigAddr = _AdslConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 1, 1, 3),
    _AdslConfigAddr_Type()
)
adslConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslConfigAddr.setStatus("mandatory")
_AdslLineNumber_Type = Integer32
_AdslLineNumber_Object = MibTableColumn
adslLineNumber = _AdslLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 1, 1, 4),
    _AdslLineNumber_Type()
)
adslLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslLineNumber.setStatus("mandatory")
_AdslPeriodTable_Object = MibTable
adslPeriodTable = _AdslPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2)
)
if mibBuilder.loadTexts:
    adslPeriodTable.setStatus("mandatory")
_AdslPeriodEntry_Object = MibTableRow
adslPeriodEntry = _AdslPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1)
)
adslPeriodEntry.setIndexNames(
    (0, "NMS-1705", "adslLineNumber"),
)
if mibBuilder.loadTexts:
    adslPeriodEntry.setStatus("mandatory")
_AdslMemLoad_Type = ObjectIdentifier
_AdslMemLoad_Object = MibTableColumn
adslMemLoad = _AdslMemLoad_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 1),
    _AdslMemLoad_Type()
)
adslMemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslMemLoad.setStatus("mandatory")
_AdslCPULoad_Type = ObjectIdentifier
_AdslCPULoad_Object = MibTableColumn
adslCPULoad = _AdslCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 2),
    _AdslCPULoad_Type()
)
adslCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCPULoad.setStatus("mandatory")
_AdslPtInCRC_Type = Counter32
_AdslPtInCRC_Object = MibTableColumn
adslPtInCRC = _AdslPtInCRC_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 3),
    _AdslPtInCRC_Type()
)
adslPtInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtInCRC.setStatus("mandatory")


class _AdslPtStatus_Type(Integer32):
    """Custom type adslPtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AdslPtStatus_Type.__name__ = "Integer32"
_AdslPtStatus_Object = MibTableColumn
adslPtStatus = _AdslPtStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 4),
    _AdslPtStatus_Type()
)
adslPtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslPtStatus.setStatus("current")
_AdslPtSpeed_Type = ObjectIdentifier
_AdslPtSpeed_Object = MibTableColumn
adslPtSpeed = _AdslPtSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 5),
    _AdslPtSpeed_Type()
)
adslPtSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtSpeed.setStatus("mandatory")
_AdslPtOutPkts_Type = Counter32
_AdslPtOutPkts_Object = MibTableColumn
adslPtOutPkts = _AdslPtOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 6),
    _AdslPtOutPkts_Type()
)
adslPtOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtOutPkts.setStatus("mandatory")
_AdslPtInPkts_Type = Counter32
_AdslPtInPkts_Object = MibTableColumn
adslPtInPkts = _AdslPtInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 7),
    _AdslPtInPkts_Type()
)
adslPtInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtInPkts.setStatus("mandatory")
_AdslPtOutError_Type = ObjectIdentifier
_AdslPtOutError_Object = MibTableColumn
adslPtOutError = _AdslPtOutError_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 8),
    _AdslPtOutError_Type()
)
adslPtOutError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtOutError.setStatus("mandatory")
_AdslPtInError_Type = ObjectIdentifier
_AdslPtInError_Object = MibTableColumn
adslPtInError = _AdslPtInError_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 9),
    _AdslPtInError_Type()
)
adslPtInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtInError.setStatus("mandatory")
_AdslPtOutSpeed_Type = ObjectIdentifier
_AdslPtOutSpeed_Object = MibTableColumn
adslPtOutSpeed = _AdslPtOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 10),
    _AdslPtOutSpeed_Type()
)
adslPtOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtOutSpeed.setStatus("mandatory")
_AdslPtInSpeed_Type = ObjectIdentifier
_AdslPtInSpeed_Object = MibTableColumn
adslPtInSpeed = _AdslPtInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 11),
    _AdslPtInSpeed_Type()
)
adslPtInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtInSpeed.setStatus("mandatory")
_AdslPtOutDrop_Type = ObjectIdentifier
_AdslPtOutDrop_Object = MibTableColumn
adslPtOutDrop = _AdslPtOutDrop_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 12),
    _AdslPtOutDrop_Type()
)
adslPtOutDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtOutDrop.setStatus("mandatory")
_AdslPtInDrop_Type = ObjectIdentifier
_AdslPtInDrop_Object = MibTableColumn
adslPtInDrop = _AdslPtInDrop_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 175, 1, 2, 1, 13),
    _AdslPtInDrop_Type()
)
adslPtInDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslPtInDrop.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-1705",
    **{"nms1705MIB": nms1705MIB,
       "nms1705Objects": nms1705Objects,
       "adslLineTable": adslLineTable,
       "adslLineEntry": adslLineEntry,
       "adslLineUser": adslLineUser,
       "adslProductID": adslProductID,
       "adslConfigAddr": adslConfigAddr,
       "adslLineNumber": adslLineNumber,
       "adslPeriodTable": adslPeriodTable,
       "adslPeriodEntry": adslPeriodEntry,
       "adslMemLoad": adslMemLoad,
       "adslCPULoad": adslCPULoad,
       "adslPtInCRC": adslPtInCRC,
       "adslPtStatus": adslPtStatus,
       "adslPtSpeed": adslPtSpeed,
       "adslPtOutPkts": adslPtOutPkts,
       "adslPtInPkts": adslPtInPkts,
       "adslPtOutError": adslPtOutError,
       "adslPtInError": adslPtInError,
       "adslPtOutSpeed": adslPtOutSpeed,
       "adslPtInSpeed": adslPtInSpeed,
       "adslPtOutDrop": adslPtOutDrop,
       "adslPtInDrop": adslPtInDrop}
)
