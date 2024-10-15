# SNMP MIB module (RADLAN-iscsi-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-iscsi-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:03 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class QosType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 1),
          ("vpt", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RlIscsiSnoop_ObjectIdentity = ObjectIdentity
rlIscsiSnoop = _RlIscsiSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 126)
)
_RlIscsiSnoopEnable_Type = TruthValue
_RlIscsiSnoopEnable_Object = MibScalar
rlIscsiSnoopEnable = _RlIscsiSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 1),
    _RlIscsiSnoopEnable_Type()
)
rlIscsiSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopEnable.setStatus("current")


class _RlIscsiSnoopAgingTimeOut_Type(Integer32):
    """Custom type rlIscsiSnoopAgingTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2592000),
    )


_RlIscsiSnoopAgingTimeOut_Type.__name__ = "Integer32"
_RlIscsiSnoopAgingTimeOut_Object = MibScalar
rlIscsiSnoopAgingTimeOut = _RlIscsiSnoopAgingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 2),
    _RlIscsiSnoopAgingTimeOut_Type()
)
rlIscsiSnoopAgingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopAgingTimeOut.setStatus("current")
_RlIscsiSnoopQosTable_Object = MibTable
rlIscsiSnoopQosTable = _RlIscsiSnoopQosTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 3)
)
if mibBuilder.loadTexts:
    rlIscsiSnoopQosTable.setStatus("current")
_RlIscsiSnoopQosEntry_Object = MibTableRow
rlIscsiSnoopQosEntry = _RlIscsiSnoopQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 3, 1)
)
rlIscsiSnoopQosEntry.setIndexNames(
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopQosKey"),
)
if mibBuilder.loadTexts:
    rlIscsiSnoopQosEntry.setStatus("current")


class _RlIscsiSnoopQosKey_Type(Integer32):
    """Custom type rlIscsiSnoopQosKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlIscsiSnoopQosKey_Type.__name__ = "Integer32"
_RlIscsiSnoopQosKey_Object = MibTableColumn
rlIscsiSnoopQosKey = _RlIscsiSnoopQosKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 3, 1, 1),
    _RlIscsiSnoopQosKey_Type()
)
rlIscsiSnoopQosKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopQosKey.setStatus("current")
_RlIscsiSnoopQosType_Type = QosType
_RlIscsiSnoopQosType_Object = MibTableColumn
rlIscsiSnoopQosType = _RlIscsiSnoopQosType_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 3, 1, 2),
    _RlIscsiSnoopQosType_Type()
)
rlIscsiSnoopQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopQosType.setStatus("current")


class _RlIscsiSnoopQosValue_Type(Integer32):
    """Custom type rlIscsiSnoopQosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlIscsiSnoopQosValue_Type.__name__ = "Integer32"
_RlIscsiSnoopQosValue_Object = MibTableColumn
rlIscsiSnoopQosValue = _RlIscsiSnoopQosValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 3, 1, 4),
    _RlIscsiSnoopQosValue_Type()
)
rlIscsiSnoopQosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopQosValue.setStatus("current")
_RlIscsiSnoopQosRemark_Type = TruthValue
_RlIscsiSnoopQosRemark_Object = MibTableColumn
rlIscsiSnoopQosRemark = _RlIscsiSnoopQosRemark_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 3, 1, 5),
    _RlIscsiSnoopQosRemark_Type()
)
rlIscsiSnoopQosRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopQosRemark.setStatus("current")
_RlIscsiSnoopTargetConfigTable_Object = MibTable
rlIscsiSnoopTargetConfigTable = _RlIscsiSnoopTargetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 4)
)
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetConfigTable.setStatus("current")
_RlIscsiSnoopTargetConfigEntry_Object = MibTableRow
rlIscsiSnoopTargetConfigEntry = _RlIscsiSnoopTargetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 4, 1)
)
rlIscsiSnoopTargetConfigEntry.setIndexNames(
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopTargetConfigTcpPort"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopTargetConfigAddr"),
)
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetConfigEntry.setStatus("current")
_RlIscsiSnoopTargetConfigTcpPort_Type = Integer32
_RlIscsiSnoopTargetConfigTcpPort_Object = MibTableColumn
rlIscsiSnoopTargetConfigTcpPort = _RlIscsiSnoopTargetConfigTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 4, 1, 1),
    _RlIscsiSnoopTargetConfigTcpPort_Type()
)
rlIscsiSnoopTargetConfigTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetConfigTcpPort.setStatus("current")
_RlIscsiSnoopTargetConfigAddr_Type = IpAddress
_RlIscsiSnoopTargetConfigAddr_Object = MibTableColumn
rlIscsiSnoopTargetConfigAddr = _RlIscsiSnoopTargetConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 4, 1, 3),
    _RlIscsiSnoopTargetConfigAddr_Type()
)
rlIscsiSnoopTargetConfigAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetConfigAddr.setStatus("current")


class _RlIscsiSnoopTargetConfigName1_Type(DisplayString):
    """Custom type rlIscsiSnoopTargetConfigName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlIscsiSnoopTargetConfigName1_Type.__name__ = "DisplayString"
_RlIscsiSnoopTargetConfigName1_Object = MibTableColumn
rlIscsiSnoopTargetConfigName1 = _RlIscsiSnoopTargetConfigName1_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 4, 1, 4),
    _RlIscsiSnoopTargetConfigName1_Type()
)
rlIscsiSnoopTargetConfigName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetConfigName1.setStatus("current")


class _RlIscsiSnoopTargetConfigName2_Type(DisplayString):
    """Custom type rlIscsiSnoopTargetConfigName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RlIscsiSnoopTargetConfigName2_Type.__name__ = "DisplayString"
_RlIscsiSnoopTargetConfigName2_Object = MibTableColumn
rlIscsiSnoopTargetConfigName2 = _RlIscsiSnoopTargetConfigName2_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 4, 1, 5),
    _RlIscsiSnoopTargetConfigName2_Type()
)
rlIscsiSnoopTargetConfigName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetConfigName2.setStatus("current")
_RlIscsiSnoopTargetConfigStatus_Type = RowStatus
_RlIscsiSnoopTargetConfigStatus_Object = MibTableColumn
rlIscsiSnoopTargetConfigStatus = _RlIscsiSnoopTargetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 4, 1, 6),
    _RlIscsiSnoopTargetConfigStatus_Type()
)
rlIscsiSnoopTargetConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetConfigStatus.setStatus("current")
_RlIscsiSnoopTargetNameTable_Object = MibTable
rlIscsiSnoopTargetNameTable = _RlIscsiSnoopTargetNameTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 5)
)
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetNameTable.setStatus("current")
_RlIscsiSnoopTargetNameEntry_Object = MibTableRow
rlIscsiSnoopTargetNameEntry = _RlIscsiSnoopTargetNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 5, 1)
)
rlIscsiSnoopTargetNameEntry.setIndexNames(
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopTargetNameId"),
)
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetNameEntry.setStatus("current")
_RlIscsiSnoopTargetNameId_Type = Integer32
_RlIscsiSnoopTargetNameId_Object = MibTableColumn
rlIscsiSnoopTargetNameId = _RlIscsiSnoopTargetNameId_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 5, 1, 1),
    _RlIscsiSnoopTargetNameId_Type()
)
rlIscsiSnoopTargetNameId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetNameId.setStatus("current")


class _RlIscsiSnoopTargetName1_Type(DisplayString):
    """Custom type rlIscsiSnoopTargetName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlIscsiSnoopTargetName1_Type.__name__ = "DisplayString"
_RlIscsiSnoopTargetName1_Object = MibTableColumn
rlIscsiSnoopTargetName1 = _RlIscsiSnoopTargetName1_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 5, 1, 2),
    _RlIscsiSnoopTargetName1_Type()
)
rlIscsiSnoopTargetName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetName1.setStatus("current")


class _RlIscsiSnoopTargetName2_Type(DisplayString):
    """Custom type rlIscsiSnoopTargetName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RlIscsiSnoopTargetName2_Type.__name__ = "DisplayString"
_RlIscsiSnoopTargetName2_Object = MibTableColumn
rlIscsiSnoopTargetName2 = _RlIscsiSnoopTargetName2_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 5, 1, 3),
    _RlIscsiSnoopTargetName2_Type()
)
rlIscsiSnoopTargetName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopTargetName2.setStatus("current")
_RlIscsiSnoopInitiatorNameTable_Object = MibTable
rlIscsiSnoopInitiatorNameTable = _RlIscsiSnoopInitiatorNameTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 6)
)
if mibBuilder.loadTexts:
    rlIscsiSnoopInitiatorNameTable.setStatus("current")
_RlIscsiSnoopInitiatorNameEntry_Object = MibTableRow
rlIscsiSnoopInitiatorNameEntry = _RlIscsiSnoopInitiatorNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 6, 1)
)
rlIscsiSnoopInitiatorNameEntry.setIndexNames(
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopInitiatorNameId"),
)
if mibBuilder.loadTexts:
    rlIscsiSnoopInitiatorNameEntry.setStatus("current")
_RlIscsiSnoopInitiatorNameId_Type = Integer32
_RlIscsiSnoopInitiatorNameId_Object = MibTableColumn
rlIscsiSnoopInitiatorNameId = _RlIscsiSnoopInitiatorNameId_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 6, 1, 1),
    _RlIscsiSnoopInitiatorNameId_Type()
)
rlIscsiSnoopInitiatorNameId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopInitiatorNameId.setStatus("current")


class _RlIscsiSnoopInitiatorName1_Type(DisplayString):
    """Custom type rlIscsiSnoopInitiatorName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlIscsiSnoopInitiatorName1_Type.__name__ = "DisplayString"
_RlIscsiSnoopInitiatorName1_Object = MibTableColumn
rlIscsiSnoopInitiatorName1 = _RlIscsiSnoopInitiatorName1_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 6, 1, 2),
    _RlIscsiSnoopInitiatorName1_Type()
)
rlIscsiSnoopInitiatorName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopInitiatorName1.setStatus("current")


class _RlIscsiSnoopInitiatorName2_Type(DisplayString):
    """Custom type rlIscsiSnoopInitiatorName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RlIscsiSnoopInitiatorName2_Type.__name__ = "DisplayString"
_RlIscsiSnoopInitiatorName2_Object = MibTableColumn
rlIscsiSnoopInitiatorName2 = _RlIscsiSnoopInitiatorName2_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 6, 1, 3),
    _RlIscsiSnoopInitiatorName2_Type()
)
rlIscsiSnoopInitiatorName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopInitiatorName2.setStatus("current")
_RlIscsiSnoopSessionTable_Object = MibTable
rlIscsiSnoopSessionTable = _RlIscsiSnoopSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 7)
)
if mibBuilder.loadTexts:
    rlIscsiSnoopSessionTable.setStatus("current")
_RlIscsiSnoopSessionEntry_Object = MibTableRow
rlIscsiSnoopSessionEntry = _RlIscsiSnoopSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 7, 1)
)
rlIscsiSnoopSessionEntry.setIndexNames(
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopTargetNameId"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopInitiatorNameId"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopSessionISID"),
)
if mibBuilder.loadTexts:
    rlIscsiSnoopSessionEntry.setStatus("current")
_RlIscsiSnoopSessionISID_Type = OctetString
_RlIscsiSnoopSessionISID_Object = MibTableColumn
rlIscsiSnoopSessionISID = _RlIscsiSnoopSessionISID_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 7, 1, 1),
    _RlIscsiSnoopSessionISID_Type()
)
rlIscsiSnoopSessionISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopSessionISID.setStatus("current")
_RlIscsiSnoopSessAgingTime_Type = Integer32
_RlIscsiSnoopSessAgingTime_Object = MibTableColumn
rlIscsiSnoopSessAgingTime = _RlIscsiSnoopSessAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 7, 1, 2),
    _RlIscsiSnoopSessAgingTime_Type()
)
rlIscsiSnoopSessAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopSessAgingTime.setStatus("current")
_RlIscsiSnoopSessionUpTime_Type = Integer32
_RlIscsiSnoopSessionUpTime_Object = MibTableColumn
rlIscsiSnoopSessionUpTime = _RlIscsiSnoopSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 7, 1, 3),
    _RlIscsiSnoopSessionUpTime_Type()
)
rlIscsiSnoopSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopSessionUpTime.setStatus("current")
_RlIscsiSnoopConnectionTable_Object = MibTable
rlIscsiSnoopConnectionTable = _RlIscsiSnoopConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8)
)
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionTable.setStatus("current")
_RlIscsiSnoopConnectionEntry_Object = MibTableRow
rlIscsiSnoopConnectionEntry = _RlIscsiSnoopConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1)
)
rlIscsiSnoopConnectionEntry.setIndexNames(
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopTargetNameId"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopInitiatorNameId"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopSessionISID"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopConnectionTargetAddr"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopConnectionTargetPort"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopConnectionInitiatorAddr"),
    (0, "RADLAN-iscsi-MIB", "rlIscsiSnoopConnectionInitiatorPort"),
)
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionEntry.setStatus("current")
_RlIscsiSnoopConnectionTargetAddr_Type = IpAddress
_RlIscsiSnoopConnectionTargetAddr_Object = MibTableColumn
rlIscsiSnoopConnectionTargetAddr = _RlIscsiSnoopConnectionTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 2),
    _RlIscsiSnoopConnectionTargetAddr_Type()
)
rlIscsiSnoopConnectionTargetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionTargetAddr.setStatus("current")
_RlIscsiSnoopConnectionTargetPort_Type = Integer32
_RlIscsiSnoopConnectionTargetPort_Object = MibTableColumn
rlIscsiSnoopConnectionTargetPort = _RlIscsiSnoopConnectionTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 3),
    _RlIscsiSnoopConnectionTargetPort_Type()
)
rlIscsiSnoopConnectionTargetPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionTargetPort.setStatus("current")
_RlIscsiSnoopConnectionInitiatorAddr_Type = IpAddress
_RlIscsiSnoopConnectionInitiatorAddr_Object = MibTableColumn
rlIscsiSnoopConnectionInitiatorAddr = _RlIscsiSnoopConnectionInitiatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 5),
    _RlIscsiSnoopConnectionInitiatorAddr_Type()
)
rlIscsiSnoopConnectionInitiatorAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionInitiatorAddr.setStatus("current")
_RlIscsiSnoopConnectionInitiatorPort_Type = Integer32
_RlIscsiSnoopConnectionInitiatorPort_Object = MibTableColumn
rlIscsiSnoopConnectionInitiatorPort = _RlIscsiSnoopConnectionInitiatorPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 6),
    _RlIscsiSnoopConnectionInitiatorPort_Type()
)
rlIscsiSnoopConnectionInitiatorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionInitiatorPort.setStatus("current")
_RlIscsiSnoopConnectionCreationTime_Type = TimeStamp
_RlIscsiSnoopConnectionCreationTime_Object = MibTableColumn
rlIscsiSnoopConnectionCreationTime = _RlIscsiSnoopConnectionCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 7),
    _RlIscsiSnoopConnectionCreationTime_Type()
)
rlIscsiSnoopConnectionCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionCreationTime.setStatus("current")
_RlIscsiSnoopConnectionLastActTime_Type = TimeStamp
_RlIscsiSnoopConnectionLastActTime_Object = MibTableColumn
rlIscsiSnoopConnectionLastActTime = _RlIscsiSnoopConnectionLastActTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 8),
    _RlIscsiSnoopConnectionLastActTime_Type()
)
rlIscsiSnoopConnectionLastActTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionLastActTime.setStatus("current")
_RlIscsiSnoopConnectionLastPollTime_Type = TimeStamp
_RlIscsiSnoopConnectionLastPollTime_Object = MibTableColumn
rlIscsiSnoopConnectionLastPollTime = _RlIscsiSnoopConnectionLastPollTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 9),
    _RlIscsiSnoopConnectionLastPollTime_Type()
)
rlIscsiSnoopConnectionLastPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionLastPollTime.setStatus("current")
_RlIscsiSnoopConnectionExpiryTime_Type = TimeStamp
_RlIscsiSnoopConnectionExpiryTime_Object = MibTableColumn
rlIscsiSnoopConnectionExpiryTime = _RlIscsiSnoopConnectionExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 10),
    _RlIscsiSnoopConnectionExpiryTime_Type()
)
rlIscsiSnoopConnectionExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionExpiryTime.setStatus("current")
_RlIscsiSnoopConnectionCounterIndex_Type = Unsigned32
_RlIscsiSnoopConnectionCounterIndex_Object = MibTableColumn
rlIscsiSnoopConnectionCounterIndex = _RlIscsiSnoopConnectionCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 8, 1, 11),
    _RlIscsiSnoopConnectionCounterIndex_Type()
)
rlIscsiSnoopConnectionCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIscsiSnoopConnectionCounterIndex.setStatus("current")
_RlIscsiSnoopCosEnable_Type = TruthValue
_RlIscsiSnoopCosEnable_Object = MibScalar
rlIscsiSnoopCosEnable = _RlIscsiSnoopCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 126, 9),
    _RlIscsiSnoopCosEnable_Type()
)
rlIscsiSnoopCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIscsiSnoopCosEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-iscsi-MIB",
    **{"QosType": QosType,
       "rlIscsiSnoop": rlIscsiSnoop,
       "rlIscsiSnoopEnable": rlIscsiSnoopEnable,
       "rlIscsiSnoopAgingTimeOut": rlIscsiSnoopAgingTimeOut,
       "rlIscsiSnoopQosTable": rlIscsiSnoopQosTable,
       "rlIscsiSnoopQosEntry": rlIscsiSnoopQosEntry,
       "rlIscsiSnoopQosKey": rlIscsiSnoopQosKey,
       "rlIscsiSnoopQosType": rlIscsiSnoopQosType,
       "rlIscsiSnoopQosValue": rlIscsiSnoopQosValue,
       "rlIscsiSnoopQosRemark": rlIscsiSnoopQosRemark,
       "rlIscsiSnoopTargetConfigTable": rlIscsiSnoopTargetConfigTable,
       "rlIscsiSnoopTargetConfigEntry": rlIscsiSnoopTargetConfigEntry,
       "rlIscsiSnoopTargetConfigTcpPort": rlIscsiSnoopTargetConfigTcpPort,
       "rlIscsiSnoopTargetConfigAddr": rlIscsiSnoopTargetConfigAddr,
       "rlIscsiSnoopTargetConfigName1": rlIscsiSnoopTargetConfigName1,
       "rlIscsiSnoopTargetConfigName2": rlIscsiSnoopTargetConfigName2,
       "rlIscsiSnoopTargetConfigStatus": rlIscsiSnoopTargetConfigStatus,
       "rlIscsiSnoopTargetNameTable": rlIscsiSnoopTargetNameTable,
       "rlIscsiSnoopTargetNameEntry": rlIscsiSnoopTargetNameEntry,
       "rlIscsiSnoopTargetNameId": rlIscsiSnoopTargetNameId,
       "rlIscsiSnoopTargetName1": rlIscsiSnoopTargetName1,
       "rlIscsiSnoopTargetName2": rlIscsiSnoopTargetName2,
       "rlIscsiSnoopInitiatorNameTable": rlIscsiSnoopInitiatorNameTable,
       "rlIscsiSnoopInitiatorNameEntry": rlIscsiSnoopInitiatorNameEntry,
       "rlIscsiSnoopInitiatorNameId": rlIscsiSnoopInitiatorNameId,
       "rlIscsiSnoopInitiatorName1": rlIscsiSnoopInitiatorName1,
       "rlIscsiSnoopInitiatorName2": rlIscsiSnoopInitiatorName2,
       "rlIscsiSnoopSessionTable": rlIscsiSnoopSessionTable,
       "rlIscsiSnoopSessionEntry": rlIscsiSnoopSessionEntry,
       "rlIscsiSnoopSessionISID": rlIscsiSnoopSessionISID,
       "rlIscsiSnoopSessAgingTime": rlIscsiSnoopSessAgingTime,
       "rlIscsiSnoopSessionUpTime": rlIscsiSnoopSessionUpTime,
       "rlIscsiSnoopConnectionTable": rlIscsiSnoopConnectionTable,
       "rlIscsiSnoopConnectionEntry": rlIscsiSnoopConnectionEntry,
       "rlIscsiSnoopConnectionTargetAddr": rlIscsiSnoopConnectionTargetAddr,
       "rlIscsiSnoopConnectionTargetPort": rlIscsiSnoopConnectionTargetPort,
       "rlIscsiSnoopConnectionInitiatorAddr": rlIscsiSnoopConnectionInitiatorAddr,
       "rlIscsiSnoopConnectionInitiatorPort": rlIscsiSnoopConnectionInitiatorPort,
       "rlIscsiSnoopConnectionCreationTime": rlIscsiSnoopConnectionCreationTime,
       "rlIscsiSnoopConnectionLastActTime": rlIscsiSnoopConnectionLastActTime,
       "rlIscsiSnoopConnectionLastPollTime": rlIscsiSnoopConnectionLastPollTime,
       "rlIscsiSnoopConnectionExpiryTime": rlIscsiSnoopConnectionExpiryTime,
       "rlIscsiSnoopConnectionCounterIndex": rlIscsiSnoopConnectionCounterIndex,
       "rlIscsiSnoopCosEnable": rlIscsiSnoopCosEnable}
)
