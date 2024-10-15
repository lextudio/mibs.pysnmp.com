# SNMP MIB module (TERAWAVE-teraSerialize-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraSerialize-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:19 2024
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
_TeraCardSerializeTable_Object = MibTable
teraCardSerializeTable = _TeraCardSerializeTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17)
)
if mibBuilder.loadTexts:
    teraCardSerializeTable.setStatus("mandatory")
_TeraCardSerializeTableEntry_Object = MibTableRow
teraCardSerializeTableEntry = _TeraCardSerializeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1)
)
teraCardSerializeTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSerialize-MIB", "teraInstallSlotNumber"),
)
if mibBuilder.loadTexts:
    teraCardSerializeTableEntry.setStatus("mandatory")
_TeraCardMfgName_Type = OctetString
_TeraCardMfgName_Object = MibTableColumn
teraCardMfgName = _TeraCardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 1),
    _TeraCardMfgName_Type()
)
teraCardMfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgName.setStatus("mandatory")
_TeraCardMfgRevision_Type = OctetString
_TeraCardMfgRevision_Object = MibTableColumn
teraCardMfgRevision = _TeraCardMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 2),
    _TeraCardMfgRevision_Type()
)
teraCardMfgRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgRevision.setStatus("mandatory")
_TeraCardMfgSerial_Type = Integer32
_TeraCardMfgSerial_Object = MibTableColumn
teraCardMfgSerial = _TeraCardMfgSerial_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 3),
    _TeraCardMfgSerial_Type()
)
teraCardMfgSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgSerial.setStatus("mandatory")
_TeraCardMfgSWVersion_Type = Integer32
_TeraCardMfgSWVersion_Object = MibTableColumn
teraCardMfgSWVersion = _TeraCardMfgSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 4),
    _TeraCardMfgSWVersion_Type()
)
teraCardMfgSWVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgSWVersion.setStatus("mandatory")
_TeraCardMfgDate_Type = Integer32
_TeraCardMfgDate_Object = MibTableColumn
teraCardMfgDate = _TeraCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 5),
    _TeraCardMfgDate_Type()
)
teraCardMfgDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgDate.setStatus("mandatory")
_TeraCardMfgPN_Type = Integer32
_TeraCardMfgPN_Object = MibTableColumn
teraCardMfgPN = _TeraCardMfgPN_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 6),
    _TeraCardMfgPN_Type()
)
teraCardMfgPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgPN.setStatus("mandatory")
_TeraCardMfgInfo_Type = OctetString
_TeraCardMfgInfo_Object = MibTableColumn
teraCardMfgInfo = _TeraCardMfgInfo_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 7),
    _TeraCardMfgInfo_Type()
)
teraCardMfgInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgInfo.setStatus("mandatory")
_TeraCardMfgReservedCRC_Type = Integer32
_TeraCardMfgReservedCRC_Object = MibTableColumn
teraCardMfgReservedCRC = _TeraCardMfgReservedCRC_Object(
    (1, 3, 6, 1, 4, 1, 4513, 17, 1, 8),
    _TeraCardMfgReservedCRC_Type()
)
teraCardMfgReservedCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCardMfgReservedCRC.setStatus("mandatory")
_TeraEEPROMSerializeTable_Object = MibTable
teraEEPROMSerializeTable = _TeraEEPROMSerializeTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21)
)
if mibBuilder.loadTexts:
    teraEEPROMSerializeTable.setStatus("mandatory")
_TeraEEPROMSerializeTableEntry_Object = MibTableRow
teraEEPROMSerializeTableEntry = _TeraEEPROMSerializeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1)
)
teraEEPROMSerializeTableEntry.setIndexNames(
    (0, "TERAWAVE-teraSerialize-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-teraSerialize-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraEEPROMSerializeTableEntry.setStatus("mandatory")
_TeraEEPROMMfgName_Type = OctetString
_TeraEEPROMMfgName_Object = MibTableColumn
teraEEPROMMfgName = _TeraEEPROMMfgName_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 1),
    _TeraEEPROMMfgName_Type()
)
teraEEPROMMfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgName.setStatus("mandatory")
_TeraEEPROMMfgRevision_Type = OctetString
_TeraEEPROMMfgRevision_Object = MibTableColumn
teraEEPROMMfgRevision = _TeraEEPROMMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 2),
    _TeraEEPROMMfgRevision_Type()
)
teraEEPROMMfgRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgRevision.setStatus("mandatory")
_TeraEEPROMMfgSerial_Type = Integer32
_TeraEEPROMMfgSerial_Object = MibTableColumn
teraEEPROMMfgSerial = _TeraEEPROMMfgSerial_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 3),
    _TeraEEPROMMfgSerial_Type()
)
teraEEPROMMfgSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgSerial.setStatus("mandatory")
_TeraEEPROMMfgHWVersion_Type = Integer32
_TeraEEPROMMfgHWVersion_Object = MibTableColumn
teraEEPROMMfgHWVersion = _TeraEEPROMMfgHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 4),
    _TeraEEPROMMfgHWVersion_Type()
)
teraEEPROMMfgHWVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgHWVersion.setStatus("mandatory")
_TeraEEPROMMfgDate_Type = Integer32
_TeraEEPROMMfgDate_Object = MibTableColumn
teraEEPROMMfgDate = _TeraEEPROMMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 5),
    _TeraEEPROMMfgDate_Type()
)
teraEEPROMMfgDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgDate.setStatus("mandatory")
_TeraEEPROMMfgPN_Type = Integer32
_TeraEEPROMMfgPN_Object = MibTableColumn
teraEEPROMMfgPN = _TeraEEPROMMfgPN_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 6),
    _TeraEEPROMMfgPN_Type()
)
teraEEPROMMfgPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgPN.setStatus("mandatory")
_TeraEEPROMMfgInfo_Type = OctetString
_TeraEEPROMMfgInfo_Object = MibTableColumn
teraEEPROMMfgInfo = _TeraEEPROMMfgInfo_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 7),
    _TeraEEPROMMfgInfo_Type()
)
teraEEPROMMfgInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgInfo.setStatus("mandatory")
_TeraEEPROMMfgReservedCRC_Type = Integer32
_TeraEEPROMMfgReservedCRC_Object = MibTableColumn
teraEEPROMMfgReservedCRC = _TeraEEPROMMfgReservedCRC_Object(
    (1, 3, 6, 1, 4, 1, 4513, 21, 1, 8),
    _TeraEEPROMMfgReservedCRC_Type()
)
teraEEPROMMfgReservedCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEEPROMMfgReservedCRC.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraSerialize-MIB",
    **{"terawave": terawave,
       "teraCardSerializeTable": teraCardSerializeTable,
       "teraCardSerializeTableEntry": teraCardSerializeTableEntry,
       "teraCardMfgName": teraCardMfgName,
       "teraCardMfgRevision": teraCardMfgRevision,
       "teraCardMfgSerial": teraCardMfgSerial,
       "teraCardMfgSWVersion": teraCardMfgSWVersion,
       "teraCardMfgDate": teraCardMfgDate,
       "teraCardMfgPN": teraCardMfgPN,
       "teraCardMfgInfo": teraCardMfgInfo,
       "teraCardMfgReservedCRC": teraCardMfgReservedCRC,
       "teraEEPROMSerializeTable": teraEEPROMSerializeTable,
       "teraEEPROMSerializeTableEntry": teraEEPROMSerializeTableEntry,
       "teraEEPROMMfgName": teraEEPROMMfgName,
       "teraEEPROMMfgRevision": teraEEPROMMfgRevision,
       "teraEEPROMMfgSerial": teraEEPROMMfgSerial,
       "teraEEPROMMfgHWVersion": teraEEPROMMfgHWVersion,
       "teraEEPROMMfgDate": teraEEPROMMfgDate,
       "teraEEPROMMfgPN": teraEEPROMMfgPN,
       "teraEEPROMMfgInfo": teraEEPROMMfgInfo,
       "teraEEPROMMfgReservedCRC": teraEEPROMMfgReservedCRC}
)
