# SNMP MIB module (HPN-ICF-NQA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-NQA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:20 2024
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

(pingCtlDescr,
 pingCtlEntry,
 pingCtlOwnerIndex,
 pingCtlTargetAddress,
 pingCtlTargetAddressType,
 pingCtlTestName,
 pingCtlType) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlDescr",
    "pingCtlEntry",
    "pingCtlOwnerIndex",
    "pingCtlTargetAddress",
    "pingCtlTargetAddressType",
    "pingCtlTestName",
    "pingCtlType")

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfNqa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfNqaObjects_ObjectIdentity = ObjectIdentity
hpnicfNqaObjects = _HpnicfNqaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1)
)
_HpnicfNqaMIBVersion_Type = DisplayString
_HpnicfNqaMIBVersion_Object = MibScalar
hpnicfNqaMIBVersion = _HpnicfNqaMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 1),
    _HpnicfNqaMIBVersion_Type()
)
hpnicfNqaMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaMIBVersion.setStatus("current")
_HpnicfNqaCtlTable_Object = MibTable
hpnicfNqaCtlTable = _HpnicfNqaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfNqaCtlTable.setStatus("current")
_HpnicfNqaCtlEntry_Object = MibTableRow
hpnicfNqaCtlEntry = _HpnicfNqaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfNqaCtlEntry.setStatus("current")


class _HpnicfNqaCtlTargetPort_Type(Integer32):
    """Custom type hpnicfNqaCtlTargetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HpnicfNqaCtlTargetPort_Type.__name__ = "Integer32"
_HpnicfNqaCtlTargetPort_Object = MibTableColumn
hpnicfNqaCtlTargetPort = _HpnicfNqaCtlTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 1),
    _HpnicfNqaCtlTargetPort_Type()
)
hpnicfNqaCtlTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlTargetPort.setStatus("current")


class _HpnicfNqaCtlSourcePort_Type(Integer32):
    """Custom type hpnicfNqaCtlSourcePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HpnicfNqaCtlSourcePort_Type.__name__ = "Integer32"
_HpnicfNqaCtlSourcePort_Object = MibTableColumn
hpnicfNqaCtlSourcePort = _HpnicfNqaCtlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 2),
    _HpnicfNqaCtlSourcePort_Type()
)
hpnicfNqaCtlSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlSourcePort.setStatus("current")


class _HpnicfNqaCtlTTL_Type(Integer32):
    """Custom type hpnicfNqaCtlTTL based on Integer32"""
    defaultValue = 20


_HpnicfNqaCtlTTL_Object = MibTableColumn
hpnicfNqaCtlTTL = _HpnicfNqaCtlTTL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 3),
    _HpnicfNqaCtlTTL_Type()
)
hpnicfNqaCtlTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlTTL.setStatus("current")


class _HpnicfNqaCtlJitterAdminInterval_Type(Integer32):
    """Custom type hpnicfNqaCtlJitterAdminInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HpnicfNqaCtlJitterAdminInterval_Type.__name__ = "Integer32"
_HpnicfNqaCtlJitterAdminInterval_Object = MibTableColumn
hpnicfNqaCtlJitterAdminInterval = _HpnicfNqaCtlJitterAdminInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 4),
    _HpnicfNqaCtlJitterAdminInterval_Type()
)
hpnicfNqaCtlJitterAdminInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlJitterAdminInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaCtlJitterAdminInterval.setUnits("milliseconds")


class _HpnicfNqaCtlJitterAdminNumPackets_Type(Integer32):
    """Custom type hpnicfNqaCtlJitterAdminNumPackets based on Integer32"""
    defaultValue = 10


_HpnicfNqaCtlJitterAdminNumPackets_Object = MibTableColumn
hpnicfNqaCtlJitterAdminNumPackets = _HpnicfNqaCtlJitterAdminNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 5),
    _HpnicfNqaCtlJitterAdminNumPackets_Type()
)
hpnicfNqaCtlJitterAdminNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlJitterAdminNumPackets.setStatus("current")


class _HpnicfNqaCtlHttpOperationType_Type(Integer32):
    """Custom type hpnicfNqaCtlHttpOperationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("post", 2),
          ("raw", 3))
    )


_HpnicfNqaCtlHttpOperationType_Type.__name__ = "Integer32"
_HpnicfNqaCtlHttpOperationType_Object = MibTableColumn
hpnicfNqaCtlHttpOperationType = _HpnicfNqaCtlHttpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 6),
    _HpnicfNqaCtlHttpOperationType_Type()
)
hpnicfNqaCtlHttpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlHttpOperationType.setStatus("current")


class _HpnicfNqaCtlHttpOperationString_Type(DisplayString):
    """Custom type hpnicfNqaCtlHttpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_HpnicfNqaCtlHttpOperationString_Type.__name__ = "DisplayString"
_HpnicfNqaCtlHttpOperationString_Object = MibTableColumn
hpnicfNqaCtlHttpOperationString = _HpnicfNqaCtlHttpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 7),
    _HpnicfNqaCtlHttpOperationString_Type()
)
hpnicfNqaCtlHttpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlHttpOperationString.setStatus("current")


class _HpnicfNqaCtlFtpOperationType_Type(Integer32):
    """Custom type hpnicfNqaCtlFtpOperationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_HpnicfNqaCtlFtpOperationType_Type.__name__ = "Integer32"
_HpnicfNqaCtlFtpOperationType_Object = MibTableColumn
hpnicfNqaCtlFtpOperationType = _HpnicfNqaCtlFtpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 8),
    _HpnicfNqaCtlFtpOperationType_Type()
)
hpnicfNqaCtlFtpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlFtpOperationType.setStatus("current")


class _HpnicfNqaCtlFtpUsername_Type(DisplayString):
    """Custom type hpnicfNqaCtlFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfNqaCtlFtpUsername_Type.__name__ = "DisplayString"
_HpnicfNqaCtlFtpUsername_Object = MibTableColumn
hpnicfNqaCtlFtpUsername = _HpnicfNqaCtlFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 9),
    _HpnicfNqaCtlFtpUsername_Type()
)
hpnicfNqaCtlFtpUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlFtpUsername.setStatus("current")


class _HpnicfNqaCtlFtpPassword_Type(DisplayString):
    """Custom type hpnicfNqaCtlFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfNqaCtlFtpPassword_Type.__name__ = "DisplayString"
_HpnicfNqaCtlFtpPassword_Object = MibTableColumn
hpnicfNqaCtlFtpPassword = _HpnicfNqaCtlFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 10),
    _HpnicfNqaCtlFtpPassword_Type()
)
hpnicfNqaCtlFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlFtpPassword.setStatus("current")


class _HpnicfNqaCtlFtpOperationString_Type(DisplayString):
    """Custom type hpnicfNqaCtlFtpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfNqaCtlFtpOperationString_Type.__name__ = "DisplayString"
_HpnicfNqaCtlFtpOperationString_Object = MibTableColumn
hpnicfNqaCtlFtpOperationString = _HpnicfNqaCtlFtpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 11),
    _HpnicfNqaCtlFtpOperationString_Type()
)
hpnicfNqaCtlFtpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlFtpOperationString.setStatus("current")


class _HpnicfNqaCtlVPNInstance_Type(DisplayString):
    """Custom type hpnicfNqaCtlVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfNqaCtlVPNInstance_Type.__name__ = "DisplayString"
_HpnicfNqaCtlVPNInstance_Object = MibTableColumn
hpnicfNqaCtlVPNInstance = _HpnicfNqaCtlVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 12),
    _HpnicfNqaCtlVPNInstance_Type()
)
hpnicfNqaCtlVPNInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlVPNInstance.setStatus("current")


class _HpnicfNqaCtlHistoryKeptTime_Type(Integer32):
    """Custom type hpnicfNqaCtlHistoryKeptTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_HpnicfNqaCtlHistoryKeptTime_Type.__name__ = "Integer32"
_HpnicfNqaCtlHistoryKeptTime_Object = MibTableColumn
hpnicfNqaCtlHistoryKeptTime = _HpnicfNqaCtlHistoryKeptTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 13),
    _HpnicfNqaCtlHistoryKeptTime_Type()
)
hpnicfNqaCtlHistoryKeptTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlHistoryKeptTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaCtlHistoryKeptTime.setUnits("minutes")


class _HpnicfNqaCtlHistoryEnable_Type(Integer32):
    """Custom type hpnicfNqaCtlHistoryEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpnicfNqaCtlHistoryEnable_Type.__name__ = "Integer32"
_HpnicfNqaCtlHistoryEnable_Object = MibTableColumn
hpnicfNqaCtlHistoryEnable = _HpnicfNqaCtlHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 14),
    _HpnicfNqaCtlHistoryEnable_Type()
)
hpnicfNqaCtlHistoryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlHistoryEnable.setStatus("current")


class _HpnicfNqaCtlICPIFAdvFactor_Type(Integer32):
    """Custom type hpnicfNqaCtlICPIFAdvFactor based on Integer32"""
    defaultValue = 0


_HpnicfNqaCtlICPIFAdvFactor_Object = MibTableColumn
hpnicfNqaCtlICPIFAdvFactor = _HpnicfNqaCtlICPIFAdvFactor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 15),
    _HpnicfNqaCtlICPIFAdvFactor_Type()
)
hpnicfNqaCtlICPIFAdvFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlICPIFAdvFactor.setStatus("current")


class _HpnicfNqaCtlCodecType_Type(Integer32):
    """Custom type hpnicfNqaCtlCodecType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711Alaw", 2),
          ("g711Ulaw", 3),
          ("g729A", 4),
          ("icmpTimestamp", 5),
          ("notDefined", 1))
    )


_HpnicfNqaCtlCodecType_Type.__name__ = "Integer32"
_HpnicfNqaCtlCodecType_Object = MibTableColumn
hpnicfNqaCtlCodecType = _HpnicfNqaCtlCodecType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 2, 1, 16),
    _HpnicfNqaCtlCodecType_Type()
)
hpnicfNqaCtlCodecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlCodecType.setStatus("current")
_HpnicfNqaResultsTable_Object = MibTable
hpnicfNqaResultsTable = _HpnicfNqaResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfNqaResultsTable.setStatus("current")
_HpnicfNqaResultsEntry_Object = MibTableRow
hpnicfNqaResultsEntry = _HpnicfNqaResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1)
)
hpnicfNqaResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hpnicfNqaResultsEntry.setStatus("current")
_HpnicfNqaResultsRttNumDisconnects_Type = Unsigned32
_HpnicfNqaResultsRttNumDisconnects_Object = MibTableColumn
hpnicfNqaResultsRttNumDisconnects = _HpnicfNqaResultsRttNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 1),
    _HpnicfNqaResultsRttNumDisconnects_Type()
)
hpnicfNqaResultsRttNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttNumDisconnects.setStatus("current")
_HpnicfNqaResultsRttTimeouts_Type = Unsigned32
_HpnicfNqaResultsRttTimeouts_Object = MibTableColumn
hpnicfNqaResultsRttTimeouts = _HpnicfNqaResultsRttTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 2),
    _HpnicfNqaResultsRttTimeouts_Type()
)
hpnicfNqaResultsRttTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttTimeouts.setStatus("current")
_HpnicfNqaResultsRttBusies_Type = Unsigned32
_HpnicfNqaResultsRttBusies_Object = MibTableColumn
hpnicfNqaResultsRttBusies = _HpnicfNqaResultsRttBusies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 3),
    _HpnicfNqaResultsRttBusies_Type()
)
hpnicfNqaResultsRttBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttBusies.setStatus("current")
_HpnicfNqaResultsRttNoConnections_Type = Unsigned32
_HpnicfNqaResultsRttNoConnections_Object = MibTableColumn
hpnicfNqaResultsRttNoConnections = _HpnicfNqaResultsRttNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 4),
    _HpnicfNqaResultsRttNoConnections_Type()
)
hpnicfNqaResultsRttNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttNoConnections.setStatus("current")
_HpnicfNqaResultsRttDrops_Type = Unsigned32
_HpnicfNqaResultsRttDrops_Object = MibTableColumn
hpnicfNqaResultsRttDrops = _HpnicfNqaResultsRttDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 5),
    _HpnicfNqaResultsRttDrops_Type()
)
hpnicfNqaResultsRttDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttDrops.setStatus("current")
_HpnicfNqaResultsRttSequenceErrors_Type = Unsigned32
_HpnicfNqaResultsRttSequenceErrors_Object = MibTableColumn
hpnicfNqaResultsRttSequenceErrors = _HpnicfNqaResultsRttSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 6),
    _HpnicfNqaResultsRttSequenceErrors_Type()
)
hpnicfNqaResultsRttSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttSequenceErrors.setStatus("current")
_HpnicfNqaResultsRttStatsErrors_Type = Unsigned32
_HpnicfNqaResultsRttStatsErrors_Object = MibTableColumn
hpnicfNqaResultsRttStatsErrors = _HpnicfNqaResultsRttStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 7),
    _HpnicfNqaResultsRttStatsErrors_Type()
)
hpnicfNqaResultsRttStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttStatsErrors.setStatus("current")
_HpnicfNqaResultsMaxDelaySD_Type = Unsigned32
_HpnicfNqaResultsMaxDelaySD_Object = MibTableColumn
hpnicfNqaResultsMaxDelaySD = _HpnicfNqaResultsMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 8),
    _HpnicfNqaResultsMaxDelaySD_Type()
)
hpnicfNqaResultsMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsMaxDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaResultsMaxDelaySD.setUnits("milliseconds")
_HpnicfNqaResultsMaxDelayDS_Type = Unsigned32
_HpnicfNqaResultsMaxDelayDS_Object = MibTableColumn
hpnicfNqaResultsMaxDelayDS = _HpnicfNqaResultsMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 9),
    _HpnicfNqaResultsMaxDelayDS_Type()
)
hpnicfNqaResultsMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsMaxDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaResultsMaxDelayDS.setUnits("milliseconds")
_HpnicfNqaResultsLostPacketRatio_Type = Unsigned32
_HpnicfNqaResultsLostPacketRatio_Object = MibTableColumn
hpnicfNqaResultsLostPacketRatio = _HpnicfNqaResultsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 10),
    _HpnicfNqaResultsLostPacketRatio_Type()
)
hpnicfNqaResultsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsLostPacketRatio.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaResultsLostPacketRatio.setUnits("milliseconds")
_HpnicfNqaResultsPacketLateArrival_Type = Unsigned32
_HpnicfNqaResultsPacketLateArrival_Object = MibTableColumn
hpnicfNqaResultsPacketLateArrival = _HpnicfNqaResultsPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 11),
    _HpnicfNqaResultsPacketLateArrival_Type()
)
hpnicfNqaResultsPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsPacketLateArrival.setStatus("current")
_HpnicfNqaResultsRttSum_Type = Unsigned32
_HpnicfNqaResultsRttSum_Object = MibTableColumn
hpnicfNqaResultsRttSum = _HpnicfNqaResultsRttSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 12),
    _HpnicfNqaResultsRttSum_Type()
)
hpnicfNqaResultsRttSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsRttSum.setStatus("current")
_HpnicfNqaResultsNumOfDelaySD_Type = Unsigned32
_HpnicfNqaResultsNumOfDelaySD_Object = MibTableColumn
hpnicfNqaResultsNumOfDelaySD = _HpnicfNqaResultsNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 13),
    _HpnicfNqaResultsNumOfDelaySD_Type()
)
hpnicfNqaResultsNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsNumOfDelaySD.setStatus("current")
_HpnicfNqaResultsMinDelaySD_Type = Unsigned32
_HpnicfNqaResultsMinDelaySD_Object = MibTableColumn
hpnicfNqaResultsMinDelaySD = _HpnicfNqaResultsMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 14),
    _HpnicfNqaResultsMinDelaySD_Type()
)
hpnicfNqaResultsMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsMinDelaySD.setStatus("current")
_HpnicfNqaResultsSumDelaySD_Type = Unsigned32
_HpnicfNqaResultsSumDelaySD_Object = MibTableColumn
hpnicfNqaResultsSumDelaySD = _HpnicfNqaResultsSumDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 15),
    _HpnicfNqaResultsSumDelaySD_Type()
)
hpnicfNqaResultsSumDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsSumDelaySD.setStatus("current")
_HpnicfNqaResultsSum2DelaySD_Type = Unsigned32
_HpnicfNqaResultsSum2DelaySD_Object = MibTableColumn
hpnicfNqaResultsSum2DelaySD = _HpnicfNqaResultsSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 16),
    _HpnicfNqaResultsSum2DelaySD_Type()
)
hpnicfNqaResultsSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsSum2DelaySD.setStatus("current")
_HpnicfNqaResultsNumOfDelayDS_Type = Unsigned32
_HpnicfNqaResultsNumOfDelayDS_Object = MibTableColumn
hpnicfNqaResultsNumOfDelayDS = _HpnicfNqaResultsNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 17),
    _HpnicfNqaResultsNumOfDelayDS_Type()
)
hpnicfNqaResultsNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsNumOfDelayDS.setStatus("current")
_HpnicfNqaResultsMinDelayDS_Type = Unsigned32
_HpnicfNqaResultsMinDelayDS_Object = MibTableColumn
hpnicfNqaResultsMinDelayDS = _HpnicfNqaResultsMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 18),
    _HpnicfNqaResultsMinDelayDS_Type()
)
hpnicfNqaResultsMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsMinDelayDS.setStatus("current")
_HpnicfNqaResultsSumDelayDS_Type = Unsigned32
_HpnicfNqaResultsSumDelayDS_Object = MibTableColumn
hpnicfNqaResultsSumDelayDS = _HpnicfNqaResultsSumDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 19),
    _HpnicfNqaResultsSumDelayDS_Type()
)
hpnicfNqaResultsSumDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsSumDelayDS.setStatus("current")
_HpnicfNqaResultsSum2DelayDS_Type = Unsigned32
_HpnicfNqaResultsSum2DelayDS_Object = MibTableColumn
hpnicfNqaResultsSum2DelayDS = _HpnicfNqaResultsSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 3, 1, 20),
    _HpnicfNqaResultsSum2DelayDS_Type()
)
hpnicfNqaResultsSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaResultsSum2DelayDS.setStatus("current")
_HpnicfNqaJitterStatsTable_Object = MibTable
hpnicfNqaJitterStatsTable = _HpnicfNqaJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsTable.setStatus("current")
_HpnicfNqaJitterStatsEntry_Object = MibTableRow
hpnicfNqaJitterStatsEntry = _HpnicfNqaJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1)
)
hpnicfNqaJitterStatsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsEntry.setStatus("current")
_HpnicfNqaJitterStatsNumOfRTT_Type = Counter32
_HpnicfNqaJitterStatsNumOfRTT_Object = MibTableColumn
hpnicfNqaJitterStatsNumOfRTT = _HpnicfNqaJitterStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 1),
    _HpnicfNqaJitterStatsNumOfRTT_Type()
)
hpnicfNqaJitterStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsNumOfRTT.setStatus("current")
_HpnicfNqaJitterStatsMinOfPositivesSD_Type = Gauge32
_HpnicfNqaJitterStatsMinOfPositivesSD_Object = MibTableColumn
hpnicfNqaJitterStatsMinOfPositivesSD = _HpnicfNqaJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 2),
    _HpnicfNqaJitterStatsMinOfPositivesSD_Type()
)
hpnicfNqaJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMinOfPositivesSD.setStatus("current")
_HpnicfNqaJitterStatsMaxOfPositivesSD_Type = Gauge32
_HpnicfNqaJitterStatsMaxOfPositivesSD_Object = MibTableColumn
hpnicfNqaJitterStatsMaxOfPositivesSD = _HpnicfNqaJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 3),
    _HpnicfNqaJitterStatsMaxOfPositivesSD_Type()
)
hpnicfNqaJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMaxOfPositivesSD.setStatus("current")
_HpnicfNqaJitterStatsNumOfPositivesSD_Type = Gauge32
_HpnicfNqaJitterStatsNumOfPositivesSD_Object = MibTableColumn
hpnicfNqaJitterStatsNumOfPositivesSD = _HpnicfNqaJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 4),
    _HpnicfNqaJitterStatsNumOfPositivesSD_Type()
)
hpnicfNqaJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsNumOfPositivesSD.setStatus("current")
_HpnicfNqaJitterStatsSumOfPositivesSD_Type = Gauge32
_HpnicfNqaJitterStatsSumOfPositivesSD_Object = MibTableColumn
hpnicfNqaJitterStatsSumOfPositivesSD = _HpnicfNqaJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 5),
    _HpnicfNqaJitterStatsSumOfPositivesSD_Type()
)
hpnicfNqaJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSumOfPositivesSD.setStatus("current")
_HpnicfNqaJitterStatsSum2PositivesSD_Type = Gauge32
_HpnicfNqaJitterStatsSum2PositivesSD_Object = MibTableColumn
hpnicfNqaJitterStatsSum2PositivesSD = _HpnicfNqaJitterStatsSum2PositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 6),
    _HpnicfNqaJitterStatsSum2PositivesSD_Type()
)
hpnicfNqaJitterStatsSum2PositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSum2PositivesSD.setStatus("current")
_HpnicfNqaJitterStatsMinOfNegativesSD_Type = Gauge32
_HpnicfNqaJitterStatsMinOfNegativesSD_Object = MibTableColumn
hpnicfNqaJitterStatsMinOfNegativesSD = _HpnicfNqaJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 7),
    _HpnicfNqaJitterStatsMinOfNegativesSD_Type()
)
hpnicfNqaJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMinOfNegativesSD.setStatus("current")
_HpnicfNqaJitterStatsMaxOfNegativesSD_Type = Gauge32
_HpnicfNqaJitterStatsMaxOfNegativesSD_Object = MibTableColumn
hpnicfNqaJitterStatsMaxOfNegativesSD = _HpnicfNqaJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 8),
    _HpnicfNqaJitterStatsMaxOfNegativesSD_Type()
)
hpnicfNqaJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMaxOfNegativesSD.setStatus("current")
_HpnicfNqaJitterStatsNumOfNegativesSD_Type = Gauge32
_HpnicfNqaJitterStatsNumOfNegativesSD_Object = MibTableColumn
hpnicfNqaJitterStatsNumOfNegativesSD = _HpnicfNqaJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 9),
    _HpnicfNqaJitterStatsNumOfNegativesSD_Type()
)
hpnicfNqaJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsNumOfNegativesSD.setStatus("current")
_HpnicfNqaJitterStatsSumOfNegativesSD_Type = Gauge32
_HpnicfNqaJitterStatsSumOfNegativesSD_Object = MibTableColumn
hpnicfNqaJitterStatsSumOfNegativesSD = _HpnicfNqaJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 10),
    _HpnicfNqaJitterStatsSumOfNegativesSD_Type()
)
hpnicfNqaJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSumOfNegativesSD.setStatus("current")
_HpnicfNqaJitterStatsSum2NegativesSD_Type = Gauge32
_HpnicfNqaJitterStatsSum2NegativesSD_Object = MibTableColumn
hpnicfNqaJitterStatsSum2NegativesSD = _HpnicfNqaJitterStatsSum2NegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 11),
    _HpnicfNqaJitterStatsSum2NegativesSD_Type()
)
hpnicfNqaJitterStatsSum2NegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSum2NegativesSD.setStatus("current")
_HpnicfNqaJitterStatsMinOfPositivesDS_Type = Gauge32
_HpnicfNqaJitterStatsMinOfPositivesDS_Object = MibTableColumn
hpnicfNqaJitterStatsMinOfPositivesDS = _HpnicfNqaJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 12),
    _HpnicfNqaJitterStatsMinOfPositivesDS_Type()
)
hpnicfNqaJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMinOfPositivesDS.setStatus("current")
_HpnicfNqaJitterStatsMaxOfPositivesDS_Type = Gauge32
_HpnicfNqaJitterStatsMaxOfPositivesDS_Object = MibTableColumn
hpnicfNqaJitterStatsMaxOfPositivesDS = _HpnicfNqaJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 13),
    _HpnicfNqaJitterStatsMaxOfPositivesDS_Type()
)
hpnicfNqaJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMaxOfPositivesDS.setStatus("current")
_HpnicfNqaJitterStatsNumOfPositivesDS_Type = Gauge32
_HpnicfNqaJitterStatsNumOfPositivesDS_Object = MibTableColumn
hpnicfNqaJitterStatsNumOfPositivesDS = _HpnicfNqaJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 14),
    _HpnicfNqaJitterStatsNumOfPositivesDS_Type()
)
hpnicfNqaJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsNumOfPositivesDS.setStatus("current")
_HpnicfNqaJitterStatsSumOfPositivesDS_Type = Gauge32
_HpnicfNqaJitterStatsSumOfPositivesDS_Object = MibTableColumn
hpnicfNqaJitterStatsSumOfPositivesDS = _HpnicfNqaJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 15),
    _HpnicfNqaJitterStatsSumOfPositivesDS_Type()
)
hpnicfNqaJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSumOfPositivesDS.setStatus("current")
_HpnicfNqaJitterStatsSum2PositivesDS_Type = Gauge32
_HpnicfNqaJitterStatsSum2PositivesDS_Object = MibTableColumn
hpnicfNqaJitterStatsSum2PositivesDS = _HpnicfNqaJitterStatsSum2PositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 16),
    _HpnicfNqaJitterStatsSum2PositivesDS_Type()
)
hpnicfNqaJitterStatsSum2PositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSum2PositivesDS.setStatus("current")
_HpnicfNqaJitterStatsMinOfNegativesDS_Type = Gauge32
_HpnicfNqaJitterStatsMinOfNegativesDS_Object = MibTableColumn
hpnicfNqaJitterStatsMinOfNegativesDS = _HpnicfNqaJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 17),
    _HpnicfNqaJitterStatsMinOfNegativesDS_Type()
)
hpnicfNqaJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMinOfNegativesDS.setStatus("current")
_HpnicfNqaJitterStatsMaxOfNegativesDS_Type = Gauge32
_HpnicfNqaJitterStatsMaxOfNegativesDS_Object = MibTableColumn
hpnicfNqaJitterStatsMaxOfNegativesDS = _HpnicfNqaJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 18),
    _HpnicfNqaJitterStatsMaxOfNegativesDS_Type()
)
hpnicfNqaJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsMaxOfNegativesDS.setStatus("current")
_HpnicfNqaJitterStatsNumOfNegativesDS_Type = Gauge32
_HpnicfNqaJitterStatsNumOfNegativesDS_Object = MibTableColumn
hpnicfNqaJitterStatsNumOfNegativesDS = _HpnicfNqaJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 19),
    _HpnicfNqaJitterStatsNumOfNegativesDS_Type()
)
hpnicfNqaJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsNumOfNegativesDS.setStatus("current")
_HpnicfNqaJitterStatsSumOfNegativesDS_Type = Gauge32
_HpnicfNqaJitterStatsSumOfNegativesDS_Object = MibTableColumn
hpnicfNqaJitterStatsSumOfNegativesDS = _HpnicfNqaJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 20),
    _HpnicfNqaJitterStatsSumOfNegativesDS_Type()
)
hpnicfNqaJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSumOfNegativesDS.setStatus("current")
_HpnicfNqaJitterStatsSum2NegativesDS_Type = Gauge32
_HpnicfNqaJitterStatsSum2NegativesDS_Object = MibTableColumn
hpnicfNqaJitterStatsSum2NegativesDS = _HpnicfNqaJitterStatsSum2NegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 21),
    _HpnicfNqaJitterStatsSum2NegativesDS_Type()
)
hpnicfNqaJitterStatsSum2NegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsSum2NegativesDS.setStatus("current")
_HpnicfNqaJitterStatsPacketLossSD_Type = Gauge32
_HpnicfNqaJitterStatsPacketLossSD_Object = MibTableColumn
hpnicfNqaJitterStatsPacketLossSD = _HpnicfNqaJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 22),
    _HpnicfNqaJitterStatsPacketLossSD_Type()
)
hpnicfNqaJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsPacketLossSD.setStatus("current")
_HpnicfNqaJitterStatsPacketLossDS_Type = Gauge32
_HpnicfNqaJitterStatsPacketLossDS_Object = MibTableColumn
hpnicfNqaJitterStatsPacketLossDS = _HpnicfNqaJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 23),
    _HpnicfNqaJitterStatsPacketLossDS_Type()
)
hpnicfNqaJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsPacketLossDS.setStatus("current")
_HpnicfNqaJitterStatsAvePositivesSD_Type = Gauge32
_HpnicfNqaJitterStatsAvePositivesSD_Object = MibTableColumn
hpnicfNqaJitterStatsAvePositivesSD = _HpnicfNqaJitterStatsAvePositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 24),
    _HpnicfNqaJitterStatsAvePositivesSD_Type()
)
hpnicfNqaJitterStatsAvePositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsAvePositivesSD.setStatus("current")
_HpnicfNqaJitterStatsAveNegativesSD_Type = Gauge32
_HpnicfNqaJitterStatsAveNegativesSD_Object = MibTableColumn
hpnicfNqaJitterStatsAveNegativesSD = _HpnicfNqaJitterStatsAveNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 25),
    _HpnicfNqaJitterStatsAveNegativesSD_Type()
)
hpnicfNqaJitterStatsAveNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsAveNegativesSD.setStatus("current")
_HpnicfNqaJitterStatsAvePositivesDS_Type = Gauge32
_HpnicfNqaJitterStatsAvePositivesDS_Object = MibTableColumn
hpnicfNqaJitterStatsAvePositivesDS = _HpnicfNqaJitterStatsAvePositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 26),
    _HpnicfNqaJitterStatsAvePositivesDS_Type()
)
hpnicfNqaJitterStatsAvePositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsAvePositivesDS.setStatus("current")
_HpnicfNqaJitterStatsAveNegativesDS_Type = Gauge32
_HpnicfNqaJitterStatsAveNegativesDS_Object = MibTableColumn
hpnicfNqaJitterStatsAveNegativesDS = _HpnicfNqaJitterStatsAveNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 27),
    _HpnicfNqaJitterStatsAveNegativesDS_Type()
)
hpnicfNqaJitterStatsAveNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsAveNegativesDS.setStatus("current")
_HpnicfNqaJitterStatsPktLossUnknown_Type = Gauge32
_HpnicfNqaJitterStatsPktLossUnknown_Object = MibTableColumn
hpnicfNqaJitterStatsPktLossUnknown = _HpnicfNqaJitterStatsPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 28),
    _HpnicfNqaJitterStatsPktLossUnknown_Type()
)
hpnicfNqaJitterStatsPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsPktLossUnknown.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsPktLossUnknown.setUnits("milliseconds")
_HpnicfNqaJitterStatsOperOfICPIF_Type = Gauge32
_HpnicfNqaJitterStatsOperOfICPIF_Object = MibTableColumn
hpnicfNqaJitterStatsOperOfICPIF = _HpnicfNqaJitterStatsOperOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 29),
    _HpnicfNqaJitterStatsOperOfICPIF_Type()
)
hpnicfNqaJitterStatsOperOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsOperOfICPIF.setStatus("current")
_HpnicfNqaJitterStatsOperOfMOS_Type = Gauge32
_HpnicfNqaJitterStatsOperOfMOS_Object = MibTableColumn
hpnicfNqaJitterStatsOperOfMOS = _HpnicfNqaJitterStatsOperOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 4, 1, 30),
    _HpnicfNqaJitterStatsOperOfMOS_Type()
)
hpnicfNqaJitterStatsOperOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaJitterStatsOperOfMOS.setStatus("current")


class _HpnicfNqaAgentEnable_Type(Integer32):
    """Custom type hpnicfNqaAgentEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpnicfNqaAgentEnable_Type.__name__ = "Integer32"
_HpnicfNqaAgentEnable_Object = MibScalar
hpnicfNqaAgentEnable = _HpnicfNqaAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 5),
    _HpnicfNqaAgentEnable_Type()
)
hpnicfNqaAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNqaAgentEnable.setStatus("current")
_HpnicfNqaTcpServerTable_Object = MibTable
hpnicfNqaTcpServerTable = _HpnicfNqaTcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfNqaTcpServerTable.setStatus("current")
_HpnicfNqaTcpServerEntry_Object = MibTableRow
hpnicfNqaTcpServerEntry = _HpnicfNqaTcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 6, 1)
)
hpnicfNqaTcpServerEntry.setIndexNames(
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaTcpServerIpAddress"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaTcpServerPort"),
)
if mibBuilder.loadTexts:
    hpnicfNqaTcpServerEntry.setStatus("current")


class _HpnicfNqaTcpServerIpAddress_Type(InetAddress):
    """Custom type hpnicfNqaTcpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_HpnicfNqaTcpServerIpAddress_Object = MibTableColumn
hpnicfNqaTcpServerIpAddress = _HpnicfNqaTcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 6, 1, 1),
    _HpnicfNqaTcpServerIpAddress_Type()
)
hpnicfNqaTcpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaTcpServerIpAddress.setStatus("current")


class _HpnicfNqaTcpServerPort_Type(Integer32):
    """Custom type hpnicfNqaTcpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HpnicfNqaTcpServerPort_Type.__name__ = "Integer32"
_HpnicfNqaTcpServerPort_Object = MibTableColumn
hpnicfNqaTcpServerPort = _HpnicfNqaTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 6, 1, 2),
    _HpnicfNqaTcpServerPort_Type()
)
hpnicfNqaTcpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaTcpServerPort.setStatus("current")
_HpnicfNqaTcpServerRowStatus_Type = RowStatus
_HpnicfNqaTcpServerRowStatus_Object = MibTableColumn
hpnicfNqaTcpServerRowStatus = _HpnicfNqaTcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 6, 1, 3),
    _HpnicfNqaTcpServerRowStatus_Type()
)
hpnicfNqaTcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaTcpServerRowStatus.setStatus("current")
_HpnicfNqaUdpServerTable_Object = MibTable
hpnicfNqaUdpServerTable = _HpnicfNqaUdpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfNqaUdpServerTable.setStatus("current")
_HpnicfNqaUdpServerEntry_Object = MibTableRow
hpnicfNqaUdpServerEntry = _HpnicfNqaUdpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 7, 1)
)
hpnicfNqaUdpServerEntry.setIndexNames(
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaUdpServerIpAddress"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaUdpServerPort"),
)
if mibBuilder.loadTexts:
    hpnicfNqaUdpServerEntry.setStatus("current")


class _HpnicfNqaUdpServerIpAddress_Type(InetAddress):
    """Custom type hpnicfNqaUdpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_HpnicfNqaUdpServerIpAddress_Object = MibTableColumn
hpnicfNqaUdpServerIpAddress = _HpnicfNqaUdpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 7, 1, 1),
    _HpnicfNqaUdpServerIpAddress_Type()
)
hpnicfNqaUdpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaUdpServerIpAddress.setStatus("current")


class _HpnicfNqaUdpServerPort_Type(Integer32):
    """Custom type hpnicfNqaUdpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HpnicfNqaUdpServerPort_Type.__name__ = "Integer32"
_HpnicfNqaUdpServerPort_Object = MibTableColumn
hpnicfNqaUdpServerPort = _HpnicfNqaUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 7, 1, 2),
    _HpnicfNqaUdpServerPort_Type()
)
hpnicfNqaUdpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaUdpServerPort.setStatus("current")
_HpnicfNqaUdpServerRowStatus_Type = RowStatus
_HpnicfNqaUdpServerRowStatus_Object = MibTableColumn
hpnicfNqaUdpServerRowStatus = _HpnicfNqaUdpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 7, 1, 3),
    _HpnicfNqaUdpServerRowStatus_Type()
)
hpnicfNqaUdpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaUdpServerRowStatus.setStatus("current")


class _HpnicfNqaServerEnable_Type(Integer32):
    """Custom type hpnicfNqaServerEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpnicfNqaServerEnable_Type.__name__ = "Integer32"
_HpnicfNqaServerEnable_Object = MibScalar
hpnicfNqaServerEnable = _HpnicfNqaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 8),
    _HpnicfNqaServerEnable_Type()
)
hpnicfNqaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNqaServerEnable.setStatus("current")
_HpnicfNqaStatsMaxGroupNumber_Type = Integer32
_HpnicfNqaStatsMaxGroupNumber_Object = MibScalar
hpnicfNqaStatsMaxGroupNumber = _HpnicfNqaStatsMaxGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 9),
    _HpnicfNqaStatsMaxGroupNumber_Type()
)
hpnicfNqaStatsMaxGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatsMaxGroupNumber.setStatus("current")
_HpnicfNqaStatisticsCtlTable_Object = MibTable
hpnicfNqaStatisticsCtlTable = _HpnicfNqaStatisticsCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hpnicfNqaStatisticsCtlTable.setStatus("current")
_HpnicfNqaStatisticsCtlEntry_Object = MibTableRow
hpnicfNqaStatisticsCtlEntry = _HpnicfNqaStatisticsCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hpnicfNqaStatisticsCtlEntry.setStatus("current")
_HpnicfNqaCtlStatisticsInterval_Type = Unsigned32
_HpnicfNqaCtlStatisticsInterval_Object = MibTableColumn
hpnicfNqaCtlStatisticsInterval = _HpnicfNqaCtlStatisticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 10, 1, 1),
    _HpnicfNqaCtlStatisticsInterval_Type()
)
hpnicfNqaCtlStatisticsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlStatisticsInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaCtlStatisticsInterval.setUnits("minutes")


class _HpnicfNqaCtlStatisticsGroupNumber_Type(Unsigned32):
    """Custom type hpnicfNqaCtlStatisticsGroupNumber based on Unsigned32"""
    defaultValue = 2


_HpnicfNqaCtlStatisticsGroupNumber_Object = MibTableColumn
hpnicfNqaCtlStatisticsGroupNumber = _HpnicfNqaCtlStatisticsGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 10, 1, 2),
    _HpnicfNqaCtlStatisticsGroupNumber_Type()
)
hpnicfNqaCtlStatisticsGroupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlStatisticsGroupNumber.setStatus("current")


class _HpnicfNqaCtlStatisticsKeptTime_Type(Unsigned32):
    """Custom type hpnicfNqaCtlStatisticsKeptTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_HpnicfNqaCtlStatisticsKeptTime_Type.__name__ = "Unsigned32"
_HpnicfNqaCtlStatisticsKeptTime_Object = MibTableColumn
hpnicfNqaCtlStatisticsKeptTime = _HpnicfNqaCtlStatisticsKeptTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 10, 1, 3),
    _HpnicfNqaCtlStatisticsKeptTime_Type()
)
hpnicfNqaCtlStatisticsKeptTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlStatisticsKeptTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaCtlStatisticsKeptTime.setUnits("minutes")
_HpnicfNqaCtlBeginTime_Type = DateAndTime
_HpnicfNqaCtlBeginTime_Object = MibTableColumn
hpnicfNqaCtlBeginTime = _HpnicfNqaCtlBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 10, 1, 4),
    _HpnicfNqaCtlBeginTime_Type()
)
hpnicfNqaCtlBeginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlBeginTime.setStatus("current")


class _HpnicfNqaCtlLifeTime_Type(Unsigned32):
    """Custom type hpnicfNqaCtlLifeTime based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaCtlLifeTime_Object = MibTableColumn
hpnicfNqaCtlLifeTime = _HpnicfNqaCtlLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 10, 1, 5),
    _HpnicfNqaCtlLifeTime_Type()
)
hpnicfNqaCtlLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaCtlLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaCtlLifeTime.setUnits("seconds")
_HpnicfNqaStatisticsResultsTable_Object = MibTable
hpnicfNqaStatisticsResultsTable = _HpnicfNqaStatisticsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11)
)
if mibBuilder.loadTexts:
    hpnicfNqaStatisticsResultsTable.setStatus("current")
_HpnicfNqaStatisticsResultsEntry_Object = MibTableRow
hpnicfNqaStatisticsResultsEntry = _HpnicfNqaStatisticsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1)
)
hpnicfNqaStatisticsResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaStatResIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNqaStatisticsResultsEntry.setStatus("current")


class _HpnicfNqaStatResIndex_Type(Unsigned32):
    """Custom type hpnicfNqaStatResIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfNqaStatResIndex_Type.__name__ = "Unsigned32"
_HpnicfNqaStatResIndex_Object = MibTableColumn
hpnicfNqaStatResIndex = _HpnicfNqaStatResIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 1),
    _HpnicfNqaStatResIndex_Type()
)
hpnicfNqaStatResIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaStatResIndex.setStatus("current")


class _HpnicfNqaStatResIpTargetAddressType_Type(InetAddressType):
    """Custom type hpnicfNqaStatResIpTargetAddressType based on InetAddressType"""


_HpnicfNqaStatResIpTargetAddressType_Object = MibTableColumn
hpnicfNqaStatResIpTargetAddressType = _HpnicfNqaStatResIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 2),
    _HpnicfNqaStatResIpTargetAddressType_Type()
)
hpnicfNqaStatResIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResIpTargetAddressType.setStatus("current")


class _HpnicfNqaStatResIpTargetAddress_Type(InetAddress):
    """Custom type hpnicfNqaStatResIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_HpnicfNqaStatResIpTargetAddress_Object = MibTableColumn
hpnicfNqaStatResIpTargetAddress = _HpnicfNqaStatResIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 3),
    _HpnicfNqaStatResIpTargetAddress_Type()
)
hpnicfNqaStatResIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResIpTargetAddress.setStatus("current")
_HpnicfNqaStatResMinRtt_Type = Gauge32
_HpnicfNqaStatResMinRtt_Object = MibTableColumn
hpnicfNqaStatResMinRtt = _HpnicfNqaStatResMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 4),
    _HpnicfNqaStatResMinRtt_Type()
)
hpnicfNqaStatResMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMinRtt.setUnits("milliseconds")
_HpnicfNqaStatResMaxRtt_Type = Gauge32
_HpnicfNqaStatResMaxRtt_Object = MibTableColumn
hpnicfNqaStatResMaxRtt = _HpnicfNqaStatResMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 5),
    _HpnicfNqaStatResMaxRtt_Type()
)
hpnicfNqaStatResMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMaxRtt.setUnits("milliseconds")
_HpnicfNqaStatResAverageRtt_Type = Gauge32
_HpnicfNqaStatResAverageRtt_Object = MibTableColumn
hpnicfNqaStatResAverageRtt = _HpnicfNqaStatResAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 6),
    _HpnicfNqaStatResAverageRtt_Type()
)
hpnicfNqaStatResAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatResAverageRtt.setUnits("milliseconds")
_HpnicfNqaStatResProbeResponses_Type = Counter32
_HpnicfNqaStatResProbeResponses_Object = MibTableColumn
hpnicfNqaStatResProbeResponses = _HpnicfNqaStatResProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 7),
    _HpnicfNqaStatResProbeResponses_Type()
)
hpnicfNqaStatResProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResProbeResponses.setStatus("current")
_HpnicfNqaStatResSentProbes_Type = Counter32
_HpnicfNqaStatResSentProbes_Object = MibTableColumn
hpnicfNqaStatResSentProbes = _HpnicfNqaStatResSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 8),
    _HpnicfNqaStatResSentProbes_Type()
)
hpnicfNqaStatResSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatResSentProbes.setUnits("probes")
_HpnicfNqaStatResRttSumOfSquares_Type = Counter32
_HpnicfNqaStatResRttSumOfSquares_Object = MibTableColumn
hpnicfNqaStatResRttSumOfSquares = _HpnicfNqaStatResRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 9),
    _HpnicfNqaStatResRttSumOfSquares_Type()
)
hpnicfNqaStatResRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttSumOfSquares.setUnits("milliseconds")
_HpnicfNqaStatResStartTime_Type = DateAndTime
_HpnicfNqaStatResStartTime_Object = MibTableColumn
hpnicfNqaStatResStartTime = _HpnicfNqaStatResStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 10),
    _HpnicfNqaStatResStartTime_Type()
)
hpnicfNqaStatResStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResStartTime.setStatus("current")
_HpnicfNqaStatResInterval_Type = Gauge32
_HpnicfNqaStatResInterval_Object = MibTableColumn
hpnicfNqaStatResInterval = _HpnicfNqaStatResInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 11),
    _HpnicfNqaStatResInterval_Type()
)
hpnicfNqaStatResInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatResInterval.setUnits("seconds")
_HpnicfNqaStatResRttNumDisconnects_Type = Counter32
_HpnicfNqaStatResRttNumDisconnects_Object = MibTableColumn
hpnicfNqaStatResRttNumDisconnects = _HpnicfNqaStatResRttNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 12),
    _HpnicfNqaStatResRttNumDisconnects_Type()
)
hpnicfNqaStatResRttNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttNumDisconnects.setStatus("current")
_HpnicfNqaStatResRttTimeouts_Type = Counter32
_HpnicfNqaStatResRttTimeouts_Object = MibTableColumn
hpnicfNqaStatResRttTimeouts = _HpnicfNqaStatResRttTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 13),
    _HpnicfNqaStatResRttTimeouts_Type()
)
hpnicfNqaStatResRttTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttTimeouts.setStatus("current")
_HpnicfNqaStatResRttBusies_Type = Counter32
_HpnicfNqaStatResRttBusies_Object = MibTableColumn
hpnicfNqaStatResRttBusies = _HpnicfNqaStatResRttBusies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 14),
    _HpnicfNqaStatResRttBusies_Type()
)
hpnicfNqaStatResRttBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttBusies.setStatus("current")
_HpnicfNqaStatResRttNoConnections_Type = Counter32
_HpnicfNqaStatResRttNoConnections_Object = MibTableColumn
hpnicfNqaStatResRttNoConnections = _HpnicfNqaStatResRttNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 15),
    _HpnicfNqaStatResRttNoConnections_Type()
)
hpnicfNqaStatResRttNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttNoConnections.setStatus("current")
_HpnicfNqaStatResRttDrops_Type = Counter32
_HpnicfNqaStatResRttDrops_Object = MibTableColumn
hpnicfNqaStatResRttDrops = _HpnicfNqaStatResRttDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 16),
    _HpnicfNqaStatResRttDrops_Type()
)
hpnicfNqaStatResRttDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttDrops.setStatus("current")
_HpnicfNqaStatResRttSequenceErrors_Type = Counter32
_HpnicfNqaStatResRttSequenceErrors_Object = MibTableColumn
hpnicfNqaStatResRttSequenceErrors = _HpnicfNqaStatResRttSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 17),
    _HpnicfNqaStatResRttSequenceErrors_Type()
)
hpnicfNqaStatResRttSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttSequenceErrors.setStatus("current")
_HpnicfNqaStatResRttErrors_Type = Counter32
_HpnicfNqaStatResRttErrors_Object = MibTableColumn
hpnicfNqaStatResRttErrors = _HpnicfNqaStatResRttErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 18),
    _HpnicfNqaStatResRttErrors_Type()
)
hpnicfNqaStatResRttErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttErrors.setStatus("current")
_HpnicfNqaStatResLostPacketRatio_Type = Gauge32
_HpnicfNqaStatResLostPacketRatio_Object = MibTableColumn
hpnicfNqaStatResLostPacketRatio = _HpnicfNqaStatResLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 19),
    _HpnicfNqaStatResLostPacketRatio_Type()
)
hpnicfNqaStatResLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResLostPacketRatio.setStatus("current")
_HpnicfNqaStatResPacketLateArrival_Type = Counter32
_HpnicfNqaStatResPacketLateArrival_Object = MibTableColumn
hpnicfNqaStatResPacketLateArrival = _HpnicfNqaStatResPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 20),
    _HpnicfNqaStatResPacketLateArrival_Type()
)
hpnicfNqaStatResPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResPacketLateArrival.setStatus("current")
_HpnicfNqaStatResRttSum_Type = Counter32
_HpnicfNqaStatResRttSum_Object = MibTableColumn
hpnicfNqaStatResRttSum = _HpnicfNqaStatResRttSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 21),
    _HpnicfNqaStatResRttSum_Type()
)
hpnicfNqaStatResRttSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResRttSum.setStatus("current")
_HpnicfNqaStatResNumOfDelaySD_Type = Counter32
_HpnicfNqaStatResNumOfDelaySD_Object = MibTableColumn
hpnicfNqaStatResNumOfDelaySD = _HpnicfNqaStatResNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 22),
    _HpnicfNqaStatResNumOfDelaySD_Type()
)
hpnicfNqaStatResNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResNumOfDelaySD.setStatus("current")
_HpnicfNqaStatResMinDelaySD_Type = Gauge32
_HpnicfNqaStatResMinDelaySD_Object = MibTableColumn
hpnicfNqaStatResMinDelaySD = _HpnicfNqaStatResMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 23),
    _HpnicfNqaStatResMinDelaySD_Type()
)
hpnicfNqaStatResMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMinDelaySD.setStatus("current")
_HpnicfNqaStatResMaxDelaySD_Type = Gauge32
_HpnicfNqaStatResMaxDelaySD_Object = MibTableColumn
hpnicfNqaStatResMaxDelaySD = _HpnicfNqaStatResMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 24),
    _HpnicfNqaStatResMaxDelaySD_Type()
)
hpnicfNqaStatResMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMaxDelaySD.setStatus("current")
_HpnicfNqaStatResSumDelaySD_Type = Counter32
_HpnicfNqaStatResSumDelaySD_Object = MibTableColumn
hpnicfNqaStatResSumDelaySD = _HpnicfNqaStatResSumDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 25),
    _HpnicfNqaStatResSumDelaySD_Type()
)
hpnicfNqaStatResSumDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResSumDelaySD.setStatus("current")
_HpnicfNqaStatResSum2DelaySD_Type = Counter32
_HpnicfNqaStatResSum2DelaySD_Object = MibTableColumn
hpnicfNqaStatResSum2DelaySD = _HpnicfNqaStatResSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 26),
    _HpnicfNqaStatResSum2DelaySD_Type()
)
hpnicfNqaStatResSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResSum2DelaySD.setStatus("current")
_HpnicfNqaStatResNumOfDelayDS_Type = Counter32
_HpnicfNqaStatResNumOfDelayDS_Object = MibTableColumn
hpnicfNqaStatResNumOfDelayDS = _HpnicfNqaStatResNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 27),
    _HpnicfNqaStatResNumOfDelayDS_Type()
)
hpnicfNqaStatResNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResNumOfDelayDS.setStatus("current")
_HpnicfNqaStatResMinDelayDS_Type = Gauge32
_HpnicfNqaStatResMinDelayDS_Object = MibTableColumn
hpnicfNqaStatResMinDelayDS = _HpnicfNqaStatResMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 28),
    _HpnicfNqaStatResMinDelayDS_Type()
)
hpnicfNqaStatResMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMinDelayDS.setStatus("current")
_HpnicfNqaStatResMaxDelayDS_Type = Gauge32
_HpnicfNqaStatResMaxDelayDS_Object = MibTableColumn
hpnicfNqaStatResMaxDelayDS = _HpnicfNqaStatResMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 29),
    _HpnicfNqaStatResMaxDelayDS_Type()
)
hpnicfNqaStatResMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResMaxDelayDS.setStatus("current")
_HpnicfNqaStatResSumDelayDS_Type = Counter32
_HpnicfNqaStatResSumDelayDS_Object = MibTableColumn
hpnicfNqaStatResSumDelayDS = _HpnicfNqaStatResSumDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 30),
    _HpnicfNqaStatResSumDelayDS_Type()
)
hpnicfNqaStatResSumDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResSumDelayDS.setStatus("current")
_HpnicfNqaStatResSum2DelayDS_Type = Counter32
_HpnicfNqaStatResSum2DelayDS_Object = MibTableColumn
hpnicfNqaStatResSum2DelayDS = _HpnicfNqaStatResSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 11, 1, 31),
    _HpnicfNqaStatResSum2DelayDS_Type()
)
hpnicfNqaStatResSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatResSum2DelayDS.setStatus("current")
_HpnicfNqaGroupStatsJitterTable_Object = MibTable
hpnicfNqaGroupStatsJitterTable = _HpnicfNqaGroupStatsJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12)
)
if mibBuilder.loadTexts:
    hpnicfNqaGroupStatsJitterTable.setStatus("current")
_HpnicfNqaGroupStatsJitterEntry_Object = MibTableRow
hpnicfNqaGroupStatsJitterEntry = _HpnicfNqaGroupStatsJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1)
)
hpnicfNqaGroupStatsJitterEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaStatJitterIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNqaGroupStatsJitterEntry.setStatus("current")


class _HpnicfNqaStatJitterIndex_Type(Unsigned32):
    """Custom type hpnicfNqaStatJitterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfNqaStatJitterIndex_Type.__name__ = "Unsigned32"
_HpnicfNqaStatJitterIndex_Object = MibTableColumn
hpnicfNqaStatJitterIndex = _HpnicfNqaStatJitterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 1),
    _HpnicfNqaStatJitterIndex_Type()
)
hpnicfNqaStatJitterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterIndex.setStatus("current")
_HpnicfNqaStatJitterMinOfPosSD_Type = Gauge32
_HpnicfNqaStatJitterMinOfPosSD_Object = MibTableColumn
hpnicfNqaStatJitterMinOfPosSD = _HpnicfNqaStatJitterMinOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 2),
    _HpnicfNqaStatJitterMinOfPosSD_Type()
)
hpnicfNqaStatJitterMinOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfPosSD.setUnits("milliseconds")
_HpnicfNqaStatJitterMaxOfPosSD_Type = Gauge32
_HpnicfNqaStatJitterMaxOfPosSD_Object = MibTableColumn
hpnicfNqaStatJitterMaxOfPosSD = _HpnicfNqaStatJitterMaxOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 3),
    _HpnicfNqaStatJitterMaxOfPosSD_Type()
)
hpnicfNqaStatJitterMaxOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfPosSD.setUnits("milliseconds")
_HpnicfNqaStatJitterNumOfPosSD_Type = Counter32
_HpnicfNqaStatJitterNumOfPosSD_Object = MibTableColumn
hpnicfNqaStatJitterNumOfPosSD = _HpnicfNqaStatJitterNumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 4),
    _HpnicfNqaStatJitterNumOfPosSD_Type()
)
hpnicfNqaStatJitterNumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterNumOfPosSD.setStatus("current")
_HpnicfNqaStatJitterSumOfPosSD_Type = Counter32
_HpnicfNqaStatJitterSumOfPosSD_Object = MibTableColumn
hpnicfNqaStatJitterSumOfPosSD = _HpnicfNqaStatJitterSumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 5),
    _HpnicfNqaStatJitterSumOfPosSD_Type()
)
hpnicfNqaStatJitterSumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfPosSD.setUnits("milliseconds")
_HpnicfNqaStatJitterSumOfSquarePosSD_Type = Counter32
_HpnicfNqaStatJitterSumOfSquarePosSD_Object = MibTableColumn
hpnicfNqaStatJitterSumOfSquarePosSD = _HpnicfNqaStatJitterSumOfSquarePosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 6),
    _HpnicfNqaStatJitterSumOfSquarePosSD_Type()
)
hpnicfNqaStatJitterSumOfSquarePosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquarePosSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquarePosSD.setUnits("milliseconds")
_HpnicfNqaStatJitterMinOfNegSD_Type = Gauge32
_HpnicfNqaStatJitterMinOfNegSD_Object = MibTableColumn
hpnicfNqaStatJitterMinOfNegSD = _HpnicfNqaStatJitterMinOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 7),
    _HpnicfNqaStatJitterMinOfNegSD_Type()
)
hpnicfNqaStatJitterMinOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfNegSD.setUnits("milliseconds")
_HpnicfNqaStatJitterMaxOfNegSD_Type = Gauge32
_HpnicfNqaStatJitterMaxOfNegSD_Object = MibTableColumn
hpnicfNqaStatJitterMaxOfNegSD = _HpnicfNqaStatJitterMaxOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 8),
    _HpnicfNqaStatJitterMaxOfNegSD_Type()
)
hpnicfNqaStatJitterMaxOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfNegSD.setUnits("milliseconds")
_HpnicfNqaStatJitterNumOfNegSD_Type = Counter32
_HpnicfNqaStatJitterNumOfNegSD_Object = MibTableColumn
hpnicfNqaStatJitterNumOfNegSD = _HpnicfNqaStatJitterNumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 9),
    _HpnicfNqaStatJitterNumOfNegSD_Type()
)
hpnicfNqaStatJitterNumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterNumOfNegSD.setStatus("current")
_HpnicfNqaStatJitterSumOfNegSD_Type = Counter32
_HpnicfNqaStatJitterSumOfNegSD_Object = MibTableColumn
hpnicfNqaStatJitterSumOfNegSD = _HpnicfNqaStatJitterSumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 10),
    _HpnicfNqaStatJitterSumOfNegSD_Type()
)
hpnicfNqaStatJitterSumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfNegSD.setUnits("milliseconds")
_HpnicfNqaStatJitterSumOfSquareNegSD_Type = Counter32
_HpnicfNqaStatJitterSumOfSquareNegSD_Object = MibTableColumn
hpnicfNqaStatJitterSumOfSquareNegSD = _HpnicfNqaStatJitterSumOfSquareNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 11),
    _HpnicfNqaStatJitterSumOfSquareNegSD_Type()
)
hpnicfNqaStatJitterSumOfSquareNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquareNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquareNegSD.setUnits("milliseconds")
_HpnicfNqaStatJitterMinOfPosDS_Type = Gauge32
_HpnicfNqaStatJitterMinOfPosDS_Object = MibTableColumn
hpnicfNqaStatJitterMinOfPosDS = _HpnicfNqaStatJitterMinOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 12),
    _HpnicfNqaStatJitterMinOfPosDS_Type()
)
hpnicfNqaStatJitterMinOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfPosDS.setUnits("milliseconds")
_HpnicfNqaStatJitterMaxOfPosDS_Type = Gauge32
_HpnicfNqaStatJitterMaxOfPosDS_Object = MibTableColumn
hpnicfNqaStatJitterMaxOfPosDS = _HpnicfNqaStatJitterMaxOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 13),
    _HpnicfNqaStatJitterMaxOfPosDS_Type()
)
hpnicfNqaStatJitterMaxOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfPosDS.setUnits("milliseconds")
_HpnicfNqaStatJitterNumOfPosDS_Type = Counter32
_HpnicfNqaStatJitterNumOfPosDS_Object = MibTableColumn
hpnicfNqaStatJitterNumOfPosDS = _HpnicfNqaStatJitterNumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 14),
    _HpnicfNqaStatJitterNumOfPosDS_Type()
)
hpnicfNqaStatJitterNumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterNumOfPosDS.setStatus("current")
_HpnicfNqaStatJitterSumOfPosDS_Type = Counter32
_HpnicfNqaStatJitterSumOfPosDS_Object = MibTableColumn
hpnicfNqaStatJitterSumOfPosDS = _HpnicfNqaStatJitterSumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 15),
    _HpnicfNqaStatJitterSumOfPosDS_Type()
)
hpnicfNqaStatJitterSumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfPosDS.setUnits("milliseconds")
_HpnicfNqaStatJitterSumOfSquarePosDS_Type = Counter32
_HpnicfNqaStatJitterSumOfSquarePosDS_Object = MibTableColumn
hpnicfNqaStatJitterSumOfSquarePosDS = _HpnicfNqaStatJitterSumOfSquarePosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 16),
    _HpnicfNqaStatJitterSumOfSquarePosDS_Type()
)
hpnicfNqaStatJitterSumOfSquarePosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquarePosDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquarePosDS.setUnits("milliseconds")
_HpnicfNqaStatJitterMinOfNegDS_Type = Gauge32
_HpnicfNqaStatJitterMinOfNegDS_Object = MibTableColumn
hpnicfNqaStatJitterMinOfNegDS = _HpnicfNqaStatJitterMinOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 17),
    _HpnicfNqaStatJitterMinOfNegDS_Type()
)
hpnicfNqaStatJitterMinOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfNegDS.setUnits("milliseconds")
_HpnicfNqaStatJitterMaxOfNegDS_Type = Gauge32
_HpnicfNqaStatJitterMaxOfNegDS_Object = MibTableColumn
hpnicfNqaStatJitterMaxOfNegDS = _HpnicfNqaStatJitterMaxOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 18),
    _HpnicfNqaStatJitterMaxOfNegDS_Type()
)
hpnicfNqaStatJitterMaxOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfNegDS.setUnits("milliseconds")
_HpnicfNqaStatJitterNumOfNegDS_Type = Counter32
_HpnicfNqaStatJitterNumOfNegDS_Object = MibTableColumn
hpnicfNqaStatJitterNumOfNegDS = _HpnicfNqaStatJitterNumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 19),
    _HpnicfNqaStatJitterNumOfNegDS_Type()
)
hpnicfNqaStatJitterNumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterNumOfNegDS.setStatus("current")
_HpnicfNqaStatJitterSumOfNegDS_Type = Counter32
_HpnicfNqaStatJitterSumOfNegDS_Object = MibTableColumn
hpnicfNqaStatJitterSumOfNegDS = _HpnicfNqaStatJitterSumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 20),
    _HpnicfNqaStatJitterSumOfNegDS_Type()
)
hpnicfNqaStatJitterSumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfNegDS.setUnits("milliseconds")
_HpnicfNqaStatJitterSumOfSquareNegDS_Type = Counter32
_HpnicfNqaStatJitterSumOfSquareNegDS_Object = MibTableColumn
hpnicfNqaStatJitterSumOfSquareNegDS = _HpnicfNqaStatJitterSumOfSquareNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 21),
    _HpnicfNqaStatJitterSumOfSquareNegDS_Type()
)
hpnicfNqaStatJitterSumOfSquareNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquareNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterSumOfSquareNegDS.setUnits("milliseconds")
_HpnicfNqaStatJitterPacketLossSD_Type = Counter32
_HpnicfNqaStatJitterPacketLossSD_Object = MibTableColumn
hpnicfNqaStatJitterPacketLossSD = _HpnicfNqaStatJitterPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 22),
    _HpnicfNqaStatJitterPacketLossSD_Type()
)
hpnicfNqaStatJitterPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterPacketLossSD.setStatus("current")
_HpnicfNqaStatJitterPacketLossDS_Type = Counter32
_HpnicfNqaStatJitterPacketLossDS_Object = MibTableColumn
hpnicfNqaStatJitterPacketLossDS = _HpnicfNqaStatJitterPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 23),
    _HpnicfNqaStatJitterPacketLossDS_Type()
)
hpnicfNqaStatJitterPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterPacketLossDS.setStatus("current")
_HpnicfNqaStatJitterAvePosSD_Type = Gauge32
_HpnicfNqaStatJitterAvePosSD_Object = MibTableColumn
hpnicfNqaStatJitterAvePosSD = _HpnicfNqaStatJitterAvePosSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 24),
    _HpnicfNqaStatJitterAvePosSD_Type()
)
hpnicfNqaStatJitterAvePosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAvePosSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAvePosSD.setUnits("milliseconds")
_HpnicfNqaStatJitterAveNegSD_Type = Gauge32
_HpnicfNqaStatJitterAveNegSD_Object = MibTableColumn
hpnicfNqaStatJitterAveNegSD = _HpnicfNqaStatJitterAveNegSD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 25),
    _HpnicfNqaStatJitterAveNegSD_Type()
)
hpnicfNqaStatJitterAveNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAveNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAveNegSD.setUnits("milliseconds")
_HpnicfNqaStatJitterAvePosDS_Type = Gauge32
_HpnicfNqaStatJitterAvePosDS_Object = MibTableColumn
hpnicfNqaStatJitterAvePosDS = _HpnicfNqaStatJitterAvePosDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 26),
    _HpnicfNqaStatJitterAvePosDS_Type()
)
hpnicfNqaStatJitterAvePosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAvePosDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAvePosDS.setUnits("milliseconds")
_HpnicfNqaStatJitterAveNegDS_Type = Gauge32
_HpnicfNqaStatJitterAveNegDS_Object = MibTableColumn
hpnicfNqaStatJitterAveNegDS = _HpnicfNqaStatJitterAveNegDS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 27),
    _HpnicfNqaStatJitterAveNegDS_Type()
)
hpnicfNqaStatJitterAveNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAveNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterAveNegDS.setUnits("milliseconds")
_HpnicfNqaStatJitterPktLossUnknown_Type = Counter32
_HpnicfNqaStatJitterPktLossUnknown_Object = MibTableColumn
hpnicfNqaStatJitterPktLossUnknown = _HpnicfNqaStatJitterPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 28),
    _HpnicfNqaStatJitterPktLossUnknown_Type()
)
hpnicfNqaStatJitterPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterPktLossUnknown.setStatus("current")
_HpnicfNqaStatJitterMaxOfICPIF_Type = Gauge32
_HpnicfNqaStatJitterMaxOfICPIF_Object = MibTableColumn
hpnicfNqaStatJitterMaxOfICPIF = _HpnicfNqaStatJitterMaxOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 29),
    _HpnicfNqaStatJitterMaxOfICPIF_Type()
)
hpnicfNqaStatJitterMaxOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfICPIF.setStatus("current")
_HpnicfNqaStatJitterMinOfICPIF_Type = Gauge32
_HpnicfNqaStatJitterMinOfICPIF_Object = MibTableColumn
hpnicfNqaStatJitterMinOfICPIF = _HpnicfNqaStatJitterMinOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 30),
    _HpnicfNqaStatJitterMinOfICPIF_Type()
)
hpnicfNqaStatJitterMinOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfICPIF.setStatus("current")
_HpnicfNqaStatJitterMaxOfMOS_Type = Gauge32
_HpnicfNqaStatJitterMaxOfMOS_Object = MibTableColumn
hpnicfNqaStatJitterMaxOfMOS = _HpnicfNqaStatJitterMaxOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 31),
    _HpnicfNqaStatJitterMaxOfMOS_Type()
)
hpnicfNqaStatJitterMaxOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMaxOfMOS.setStatus("current")
_HpnicfNqaStatJitterMinOfMOS_Type = Gauge32
_HpnicfNqaStatJitterMinOfMOS_Object = MibTableColumn
hpnicfNqaStatJitterMinOfMOS = _HpnicfNqaStatJitterMinOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 12, 1, 32),
    _HpnicfNqaStatJitterMinOfMOS_Type()
)
hpnicfNqaStatJitterMinOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatJitterMinOfMOS.setStatus("current")
_HpnicfNqaReactionTable_Object = MibTable
hpnicfNqaReactionTable = _HpnicfNqaReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13)
)
if mibBuilder.loadTexts:
    hpnicfNqaReactionTable.setStatus("current")
_HpnicfNqaReactionEntry_Object = MibTableRow
hpnicfNqaReactionEntry = _HpnicfNqaReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1)
)
hpnicfNqaReactionEntry.setIndexNames(
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNqaReactionEntry.setStatus("current")


class _HpnicfNqaReactOwnerIndex_Type(SnmpAdminString):
    """Custom type hpnicfNqaReactOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfNqaReactOwnerIndex_Type.__name__ = "SnmpAdminString"
_HpnicfNqaReactOwnerIndex_Object = MibTableColumn
hpnicfNqaReactOwnerIndex = _HpnicfNqaReactOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 1),
    _HpnicfNqaReactOwnerIndex_Type()
)
hpnicfNqaReactOwnerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfNqaReactOwnerIndex.setStatus("current")


class _HpnicfNqaReactTestName_Type(SnmpAdminString):
    """Custom type hpnicfNqaReactTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfNqaReactTestName_Type.__name__ = "SnmpAdminString"
_HpnicfNqaReactTestName_Object = MibTableColumn
hpnicfNqaReactTestName = _HpnicfNqaReactTestName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 2),
    _HpnicfNqaReactTestName_Type()
)
hpnicfNqaReactTestName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfNqaReactTestName.setStatus("current")


class _HpnicfNqaReactItemIndex_Type(Unsigned32):
    """Custom type hpnicfNqaReactItemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpnicfNqaReactItemIndex_Type.__name__ = "Unsigned32"
_HpnicfNqaReactItemIndex_Object = MibTableColumn
hpnicfNqaReactItemIndex = _HpnicfNqaReactItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 3),
    _HpnicfNqaReactItemIndex_Type()
)
hpnicfNqaReactItemIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfNqaReactItemIndex.setStatus("current")


class _HpnicfNqaReactCheckedElement_Type(Integer32):
    """Custom type hpnicfNqaReactCheckedElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("icpif", 7),
          ("jitterOwdDS", 10),
          ("jitterOwdSD", 9),
          ("jitterds", 6),
          ("jitterpacketloss", 4),
          ("jitterrtt", 3),
          ("jittersd", 5),
          ("mos", 8),
          ("probefailure", 2),
          ("probetime", 1))
    )


_HpnicfNqaReactCheckedElement_Type.__name__ = "Integer32"
_HpnicfNqaReactCheckedElement_Object = MibTableColumn
hpnicfNqaReactCheckedElement = _HpnicfNqaReactCheckedElement_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 4),
    _HpnicfNqaReactCheckedElement_Type()
)
hpnicfNqaReactCheckedElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactCheckedElement.setStatus("current")


class _HpnicfNqaReactThresholdUpperLimit_Type(Unsigned32):
    """Custom type hpnicfNqaReactThresholdUpperLimit based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaReactThresholdUpperLimit_Object = MibTableColumn
hpnicfNqaReactThresholdUpperLimit = _HpnicfNqaReactThresholdUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 5),
    _HpnicfNqaReactThresholdUpperLimit_Type()
)
hpnicfNqaReactThresholdUpperLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactThresholdUpperLimit.setStatus("current")


class _HpnicfNqaReactThresholdLowerLimit_Type(Unsigned32):
    """Custom type hpnicfNqaReactThresholdLowerLimit based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaReactThresholdLowerLimit_Object = MibTableColumn
hpnicfNqaReactThresholdLowerLimit = _HpnicfNqaReactThresholdLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 6),
    _HpnicfNqaReactThresholdLowerLimit_Type()
)
hpnicfNqaReactThresholdLowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactThresholdLowerLimit.setStatus("current")


class _HpnicfNqaReactThresholdType_Type(Integer32):
    """Custom type hpnicfNqaReactThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accumulative", 3),
          ("average", 1),
          ("consecutive", 2),
          ("invalid", 0))
    )


_HpnicfNqaReactThresholdType_Type.__name__ = "Integer32"
_HpnicfNqaReactThresholdType_Object = MibTableColumn
hpnicfNqaReactThresholdType = _HpnicfNqaReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 7),
    _HpnicfNqaReactThresholdType_Type()
)
hpnicfNqaReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactThresholdType.setStatus("current")


class _HpnicfNqaReactThresholdConsecNum_Type(Unsigned32):
    """Custom type hpnicfNqaReactThresholdConsecNum based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaReactThresholdConsecNum_Object = MibTableColumn
hpnicfNqaReactThresholdConsecNum = _HpnicfNqaReactThresholdConsecNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 8),
    _HpnicfNqaReactThresholdConsecNum_Type()
)
hpnicfNqaReactThresholdConsecNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactThresholdConsecNum.setStatus("current")


class _HpnicfNqaReactThresholdAccumNum_Type(Unsigned32):
    """Custom type hpnicfNqaReactThresholdAccumNum based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaReactThresholdAccumNum_Object = MibTableColumn
hpnicfNqaReactThresholdAccumNum = _HpnicfNqaReactThresholdAccumNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 9),
    _HpnicfNqaReactThresholdAccumNum_Type()
)
hpnicfNqaReactThresholdAccumNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactThresholdAccumNum.setStatus("current")


class _HpnicfNqaReactActionType_Type(Integer32):
    """Custom type hpnicfNqaReactActionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trapAndTrigger", 3),
          ("trapOnly", 1),
          ("triggerOnly", 2))
    )


_HpnicfNqaReactActionType_Type.__name__ = "Integer32"
_HpnicfNqaReactActionType_Object = MibTableColumn
hpnicfNqaReactActionType = _HpnicfNqaReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 10),
    _HpnicfNqaReactActionType_Type()
)
hpnicfNqaReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactActionType.setStatus("current")


class _HpnicfNqaReactCurrentStatus_Type(Integer32):
    """Custom type hpnicfNqaReactCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("belowThreshold", 3),
          ("invalid", 1),
          ("overThreshold", 2))
    )


_HpnicfNqaReactCurrentStatus_Type.__name__ = "Integer32"
_HpnicfNqaReactCurrentStatus_Object = MibTableColumn
hpnicfNqaReactCurrentStatus = _HpnicfNqaReactCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 11),
    _HpnicfNqaReactCurrentStatus_Type()
)
hpnicfNqaReactCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaReactCurrentStatus.setStatus("current")
_HpnicfNqaReactRowStatus_Type = RowStatus
_HpnicfNqaReactRowStatus_Object = MibTableColumn
hpnicfNqaReactRowStatus = _HpnicfNqaReactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 12),
    _HpnicfNqaReactRowStatus_Type()
)
hpnicfNqaReactRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNqaReactRowStatus.setStatus("current")


class _HpnicfNqaReactCheckedNum_Type(Unsigned32):
    """Custom type hpnicfNqaReactCheckedNum based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaReactCheckedNum_Object = MibTableColumn
hpnicfNqaReactCheckedNum = _HpnicfNqaReactCheckedNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 13),
    _HpnicfNqaReactCheckedNum_Type()
)
hpnicfNqaReactCheckedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaReactCheckedNum.setStatus("current")


class _HpnicfNqaReactThresholdNum_Type(Unsigned32):
    """Custom type hpnicfNqaReactThresholdNum based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaReactThresholdNum_Object = MibTableColumn
hpnicfNqaReactThresholdNum = _HpnicfNqaReactThresholdNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 13, 1, 14),
    _HpnicfNqaReactThresholdNum_Type()
)
hpnicfNqaReactThresholdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaReactThresholdNum.setStatus("current")
_HpnicfNqaStatisticsReactionTable_Object = MibTable
hpnicfNqaStatisticsReactionTable = _HpnicfNqaStatisticsReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14)
)
if mibBuilder.loadTexts:
    hpnicfNqaStatisticsReactionTable.setStatus("current")
_HpnicfNqaStatisticsReactionEntry_Object = MibTableRow
hpnicfNqaStatisticsReactionEntry = _HpnicfNqaStatisticsReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14, 1)
)
hpnicfNqaStatisticsReactionEntry.setIndexNames(
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaStatReactOwnerIndex"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaStatReactTestName"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaStatReactIndex"),
    (0, "HPN-ICF-NQA-MIB", "hpnicfNqaStatReactItemIndex"),
)
if mibBuilder.loadTexts:
    hpnicfNqaStatisticsReactionEntry.setStatus("current")


class _HpnicfNqaStatReactOwnerIndex_Type(SnmpAdminString):
    """Custom type hpnicfNqaStatReactOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfNqaStatReactOwnerIndex_Type.__name__ = "SnmpAdminString"
_HpnicfNqaStatReactOwnerIndex_Object = MibTableColumn
hpnicfNqaStatReactOwnerIndex = _HpnicfNqaStatReactOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14, 1, 1),
    _HpnicfNqaStatReactOwnerIndex_Type()
)
hpnicfNqaStatReactOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaStatReactOwnerIndex.setStatus("current")


class _HpnicfNqaStatReactTestName_Type(SnmpAdminString):
    """Custom type hpnicfNqaStatReactTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfNqaStatReactTestName_Type.__name__ = "SnmpAdminString"
_HpnicfNqaStatReactTestName_Object = MibTableColumn
hpnicfNqaStatReactTestName = _HpnicfNqaStatReactTestName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14, 1, 2),
    _HpnicfNqaStatReactTestName_Type()
)
hpnicfNqaStatReactTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaStatReactTestName.setStatus("current")


class _HpnicfNqaStatReactIndex_Type(Unsigned32):
    """Custom type hpnicfNqaStatReactIndex based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaStatReactIndex_Object = MibTableColumn
hpnicfNqaStatReactIndex = _HpnicfNqaStatReactIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14, 1, 3),
    _HpnicfNqaStatReactIndex_Type()
)
hpnicfNqaStatReactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaStatReactIndex.setStatus("current")


class _HpnicfNqaStatReactItemIndex_Type(Unsigned32):
    """Custom type hpnicfNqaStatReactItemIndex based on Unsigned32"""
    defaultValue = 0


_HpnicfNqaStatReactItemIndex_Object = MibTableColumn
hpnicfNqaStatReactItemIndex = _HpnicfNqaStatReactItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14, 1, 4),
    _HpnicfNqaStatReactItemIndex_Type()
)
hpnicfNqaStatReactItemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNqaStatReactItemIndex.setStatus("current")


class _HpnicfNqaStatReactCheckedNum_Type(Counter32):
    """Custom type hpnicfNqaStatReactCheckedNum based on Counter32"""
    defaultValue = 0


_HpnicfNqaStatReactCheckedNum_Object = MibTableColumn
hpnicfNqaStatReactCheckedNum = _HpnicfNqaStatReactCheckedNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14, 1, 5),
    _HpnicfNqaStatReactCheckedNum_Type()
)
hpnicfNqaStatReactCheckedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatReactCheckedNum.setStatus("current")


class _HpnicfNqaStatReactThresholdNum_Type(Counter32):
    """Custom type hpnicfNqaStatReactThresholdNum based on Counter32"""
    defaultValue = 0


_HpnicfNqaStatReactThresholdNum_Object = MibTableColumn
hpnicfNqaStatReactThresholdNum = _HpnicfNqaStatReactThresholdNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 1, 14, 1, 6),
    _HpnicfNqaStatReactThresholdNum_Type()
)
hpnicfNqaStatReactThresholdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNqaStatReactThresholdNum.setStatus("current")
_HpnicfNqaImplementationTypeDomains_ObjectIdentity = ObjectIdentity
hpnicfNqaImplementationTypeDomains = _HpnicfNqaImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2)
)
_HpnicfNqaUdpEcho_ObjectIdentity = ObjectIdentity
hpnicfNqaUdpEcho = _HpnicfNqaUdpEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfNqaUdpEcho.setStatus("current")
_HpnicfNqaTcpconnect_ObjectIdentity = ObjectIdentity
hpnicfNqaTcpconnect = _HpnicfNqaTcpconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfNqaTcpconnect.setStatus("current")
_HpnicfNqajitter_ObjectIdentity = ObjectIdentity
hpnicfNqajitter = _HpnicfNqajitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfNqajitter.setStatus("current")
_HpnicfNqaHttp_ObjectIdentity = ObjectIdentity
hpnicfNqaHttp = _HpnicfNqaHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfNqaHttp.setStatus("current")
_HpnicfNqadlsw_ObjectIdentity = ObjectIdentity
hpnicfNqadlsw = _HpnicfNqadlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfNqadlsw.setStatus("current")
_HpnicfNqadhcp_ObjectIdentity = ObjectIdentity
hpnicfNqadhcp = _HpnicfNqadhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfNqadhcp.setStatus("current")
_HpnicfNqaftp_ObjectIdentity = ObjectIdentity
hpnicfNqaftp = _HpnicfNqaftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfNqaftp.setStatus("current")
_HpnicfNqaNotifications_ObjectIdentity = ObjectIdentity
hpnicfNqaNotifications = _HpnicfNqaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3)
)
pingCtlEntry.registerAugmentions(
    ("HPN-ICF-NQA-MIB",
     "hpnicfNqaCtlEntry")
)
hpnicfNqaCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions(
    ("HPN-ICF-NQA-MIB",
     "hpnicfNqaStatisticsCtlEntry")
)
hpnicfNqaStatisticsCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hpnicfNqaProbeTimeOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 1)
)
hpnicfNqaProbeTimeOverThreshold.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactThresholdType"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaProbeTimeOverThreshold.setStatus(
        "current"
    )

hpnicfNqaJitterRTTOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 2)
)
hpnicfNqaJitterRTTOverThreshold.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactThresholdType"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaJitterRTTOverThreshold.setStatus(
        "current"
    )

hpnicfNqaProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 3)
)
hpnicfNqaProbeFailure.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactThresholdType"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaProbeFailure.setStatus(
        "current"
    )

hpnicfNqaJitterPacketLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 4)
)
hpnicfNqaJitterPacketLoss.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactThresholdType"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaJitterPacketLoss.setStatus(
        "current"
    )

hpnicfNqaJitterSDOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 5)
)
hpnicfNqaJitterSDOverThreshold.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactThresholdType"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaJitterSDOverThreshold.setStatus(
        "current"
    )

hpnicfNqaJitterDSOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 6)
)
hpnicfNqaJitterDSOverThreshold.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactThresholdType"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaJitterDSOverThreshold.setStatus(
        "current"
    )

hpnicfNqaICPIFOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 7)
)
hpnicfNqaICPIFOverThreshold.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaICPIFOverThreshold.setStatus(
        "current"
    )

hpnicfNqaMOSOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3, 3, 8)
)
hpnicfNqaMOSOverThreshold.setObjects(
      *(("HPN-ICF-NQA-MIB", "hpnicfNqaReactOwnerIndex"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactTestName"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HPN-ICF-NQA-MIB", "hpnicfNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hpnicfNqaMOSOverThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-NQA-MIB",
    **{"hpnicfNqa": hpnicfNqa,
       "hpnicfNqaObjects": hpnicfNqaObjects,
       "hpnicfNqaMIBVersion": hpnicfNqaMIBVersion,
       "hpnicfNqaCtlTable": hpnicfNqaCtlTable,
       "hpnicfNqaCtlEntry": hpnicfNqaCtlEntry,
       "hpnicfNqaCtlTargetPort": hpnicfNqaCtlTargetPort,
       "hpnicfNqaCtlSourcePort": hpnicfNqaCtlSourcePort,
       "hpnicfNqaCtlTTL": hpnicfNqaCtlTTL,
       "hpnicfNqaCtlJitterAdminInterval": hpnicfNqaCtlJitterAdminInterval,
       "hpnicfNqaCtlJitterAdminNumPackets": hpnicfNqaCtlJitterAdminNumPackets,
       "hpnicfNqaCtlHttpOperationType": hpnicfNqaCtlHttpOperationType,
       "hpnicfNqaCtlHttpOperationString": hpnicfNqaCtlHttpOperationString,
       "hpnicfNqaCtlFtpOperationType": hpnicfNqaCtlFtpOperationType,
       "hpnicfNqaCtlFtpUsername": hpnicfNqaCtlFtpUsername,
       "hpnicfNqaCtlFtpPassword": hpnicfNqaCtlFtpPassword,
       "hpnicfNqaCtlFtpOperationString": hpnicfNqaCtlFtpOperationString,
       "hpnicfNqaCtlVPNInstance": hpnicfNqaCtlVPNInstance,
       "hpnicfNqaCtlHistoryKeptTime": hpnicfNqaCtlHistoryKeptTime,
       "hpnicfNqaCtlHistoryEnable": hpnicfNqaCtlHistoryEnable,
       "hpnicfNqaCtlICPIFAdvFactor": hpnicfNqaCtlICPIFAdvFactor,
       "hpnicfNqaCtlCodecType": hpnicfNqaCtlCodecType,
       "hpnicfNqaResultsTable": hpnicfNqaResultsTable,
       "hpnicfNqaResultsEntry": hpnicfNqaResultsEntry,
       "hpnicfNqaResultsRttNumDisconnects": hpnicfNqaResultsRttNumDisconnects,
       "hpnicfNqaResultsRttTimeouts": hpnicfNqaResultsRttTimeouts,
       "hpnicfNqaResultsRttBusies": hpnicfNqaResultsRttBusies,
       "hpnicfNqaResultsRttNoConnections": hpnicfNqaResultsRttNoConnections,
       "hpnicfNqaResultsRttDrops": hpnicfNqaResultsRttDrops,
       "hpnicfNqaResultsRttSequenceErrors": hpnicfNqaResultsRttSequenceErrors,
       "hpnicfNqaResultsRttStatsErrors": hpnicfNqaResultsRttStatsErrors,
       "hpnicfNqaResultsMaxDelaySD": hpnicfNqaResultsMaxDelaySD,
       "hpnicfNqaResultsMaxDelayDS": hpnicfNqaResultsMaxDelayDS,
       "hpnicfNqaResultsLostPacketRatio": hpnicfNqaResultsLostPacketRatio,
       "hpnicfNqaResultsPacketLateArrival": hpnicfNqaResultsPacketLateArrival,
       "hpnicfNqaResultsRttSum": hpnicfNqaResultsRttSum,
       "hpnicfNqaResultsNumOfDelaySD": hpnicfNqaResultsNumOfDelaySD,
       "hpnicfNqaResultsMinDelaySD": hpnicfNqaResultsMinDelaySD,
       "hpnicfNqaResultsSumDelaySD": hpnicfNqaResultsSumDelaySD,
       "hpnicfNqaResultsSum2DelaySD": hpnicfNqaResultsSum2DelaySD,
       "hpnicfNqaResultsNumOfDelayDS": hpnicfNqaResultsNumOfDelayDS,
       "hpnicfNqaResultsMinDelayDS": hpnicfNqaResultsMinDelayDS,
       "hpnicfNqaResultsSumDelayDS": hpnicfNqaResultsSumDelayDS,
       "hpnicfNqaResultsSum2DelayDS": hpnicfNqaResultsSum2DelayDS,
       "hpnicfNqaJitterStatsTable": hpnicfNqaJitterStatsTable,
       "hpnicfNqaJitterStatsEntry": hpnicfNqaJitterStatsEntry,
       "hpnicfNqaJitterStatsNumOfRTT": hpnicfNqaJitterStatsNumOfRTT,
       "hpnicfNqaJitterStatsMinOfPositivesSD": hpnicfNqaJitterStatsMinOfPositivesSD,
       "hpnicfNqaJitterStatsMaxOfPositivesSD": hpnicfNqaJitterStatsMaxOfPositivesSD,
       "hpnicfNqaJitterStatsNumOfPositivesSD": hpnicfNqaJitterStatsNumOfPositivesSD,
       "hpnicfNqaJitterStatsSumOfPositivesSD": hpnicfNqaJitterStatsSumOfPositivesSD,
       "hpnicfNqaJitterStatsSum2PositivesSD": hpnicfNqaJitterStatsSum2PositivesSD,
       "hpnicfNqaJitterStatsMinOfNegativesSD": hpnicfNqaJitterStatsMinOfNegativesSD,
       "hpnicfNqaJitterStatsMaxOfNegativesSD": hpnicfNqaJitterStatsMaxOfNegativesSD,
       "hpnicfNqaJitterStatsNumOfNegativesSD": hpnicfNqaJitterStatsNumOfNegativesSD,
       "hpnicfNqaJitterStatsSumOfNegativesSD": hpnicfNqaJitterStatsSumOfNegativesSD,
       "hpnicfNqaJitterStatsSum2NegativesSD": hpnicfNqaJitterStatsSum2NegativesSD,
       "hpnicfNqaJitterStatsMinOfPositivesDS": hpnicfNqaJitterStatsMinOfPositivesDS,
       "hpnicfNqaJitterStatsMaxOfPositivesDS": hpnicfNqaJitterStatsMaxOfPositivesDS,
       "hpnicfNqaJitterStatsNumOfPositivesDS": hpnicfNqaJitterStatsNumOfPositivesDS,
       "hpnicfNqaJitterStatsSumOfPositivesDS": hpnicfNqaJitterStatsSumOfPositivesDS,
       "hpnicfNqaJitterStatsSum2PositivesDS": hpnicfNqaJitterStatsSum2PositivesDS,
       "hpnicfNqaJitterStatsMinOfNegativesDS": hpnicfNqaJitterStatsMinOfNegativesDS,
       "hpnicfNqaJitterStatsMaxOfNegativesDS": hpnicfNqaJitterStatsMaxOfNegativesDS,
       "hpnicfNqaJitterStatsNumOfNegativesDS": hpnicfNqaJitterStatsNumOfNegativesDS,
       "hpnicfNqaJitterStatsSumOfNegativesDS": hpnicfNqaJitterStatsSumOfNegativesDS,
       "hpnicfNqaJitterStatsSum2NegativesDS": hpnicfNqaJitterStatsSum2NegativesDS,
       "hpnicfNqaJitterStatsPacketLossSD": hpnicfNqaJitterStatsPacketLossSD,
       "hpnicfNqaJitterStatsPacketLossDS": hpnicfNqaJitterStatsPacketLossDS,
       "hpnicfNqaJitterStatsAvePositivesSD": hpnicfNqaJitterStatsAvePositivesSD,
       "hpnicfNqaJitterStatsAveNegativesSD": hpnicfNqaJitterStatsAveNegativesSD,
       "hpnicfNqaJitterStatsAvePositivesDS": hpnicfNqaJitterStatsAvePositivesDS,
       "hpnicfNqaJitterStatsAveNegativesDS": hpnicfNqaJitterStatsAveNegativesDS,
       "hpnicfNqaJitterStatsPktLossUnknown": hpnicfNqaJitterStatsPktLossUnknown,
       "hpnicfNqaJitterStatsOperOfICPIF": hpnicfNqaJitterStatsOperOfICPIF,
       "hpnicfNqaJitterStatsOperOfMOS": hpnicfNqaJitterStatsOperOfMOS,
       "hpnicfNqaAgentEnable": hpnicfNqaAgentEnable,
       "hpnicfNqaTcpServerTable": hpnicfNqaTcpServerTable,
       "hpnicfNqaTcpServerEntry": hpnicfNqaTcpServerEntry,
       "hpnicfNqaTcpServerIpAddress": hpnicfNqaTcpServerIpAddress,
       "hpnicfNqaTcpServerPort": hpnicfNqaTcpServerPort,
       "hpnicfNqaTcpServerRowStatus": hpnicfNqaTcpServerRowStatus,
       "hpnicfNqaUdpServerTable": hpnicfNqaUdpServerTable,
       "hpnicfNqaUdpServerEntry": hpnicfNqaUdpServerEntry,
       "hpnicfNqaUdpServerIpAddress": hpnicfNqaUdpServerIpAddress,
       "hpnicfNqaUdpServerPort": hpnicfNqaUdpServerPort,
       "hpnicfNqaUdpServerRowStatus": hpnicfNqaUdpServerRowStatus,
       "hpnicfNqaServerEnable": hpnicfNqaServerEnable,
       "hpnicfNqaStatsMaxGroupNumber": hpnicfNqaStatsMaxGroupNumber,
       "hpnicfNqaStatisticsCtlTable": hpnicfNqaStatisticsCtlTable,
       "hpnicfNqaStatisticsCtlEntry": hpnicfNqaStatisticsCtlEntry,
       "hpnicfNqaCtlStatisticsInterval": hpnicfNqaCtlStatisticsInterval,
       "hpnicfNqaCtlStatisticsGroupNumber": hpnicfNqaCtlStatisticsGroupNumber,
       "hpnicfNqaCtlStatisticsKeptTime": hpnicfNqaCtlStatisticsKeptTime,
       "hpnicfNqaCtlBeginTime": hpnicfNqaCtlBeginTime,
       "hpnicfNqaCtlLifeTime": hpnicfNqaCtlLifeTime,
       "hpnicfNqaStatisticsResultsTable": hpnicfNqaStatisticsResultsTable,
       "hpnicfNqaStatisticsResultsEntry": hpnicfNqaStatisticsResultsEntry,
       "hpnicfNqaStatResIndex": hpnicfNqaStatResIndex,
       "hpnicfNqaStatResIpTargetAddressType": hpnicfNqaStatResIpTargetAddressType,
       "hpnicfNqaStatResIpTargetAddress": hpnicfNqaStatResIpTargetAddress,
       "hpnicfNqaStatResMinRtt": hpnicfNqaStatResMinRtt,
       "hpnicfNqaStatResMaxRtt": hpnicfNqaStatResMaxRtt,
       "hpnicfNqaStatResAverageRtt": hpnicfNqaStatResAverageRtt,
       "hpnicfNqaStatResProbeResponses": hpnicfNqaStatResProbeResponses,
       "hpnicfNqaStatResSentProbes": hpnicfNqaStatResSentProbes,
       "hpnicfNqaStatResRttSumOfSquares": hpnicfNqaStatResRttSumOfSquares,
       "hpnicfNqaStatResStartTime": hpnicfNqaStatResStartTime,
       "hpnicfNqaStatResInterval": hpnicfNqaStatResInterval,
       "hpnicfNqaStatResRttNumDisconnects": hpnicfNqaStatResRttNumDisconnects,
       "hpnicfNqaStatResRttTimeouts": hpnicfNqaStatResRttTimeouts,
       "hpnicfNqaStatResRttBusies": hpnicfNqaStatResRttBusies,
       "hpnicfNqaStatResRttNoConnections": hpnicfNqaStatResRttNoConnections,
       "hpnicfNqaStatResRttDrops": hpnicfNqaStatResRttDrops,
       "hpnicfNqaStatResRttSequenceErrors": hpnicfNqaStatResRttSequenceErrors,
       "hpnicfNqaStatResRttErrors": hpnicfNqaStatResRttErrors,
       "hpnicfNqaStatResLostPacketRatio": hpnicfNqaStatResLostPacketRatio,
       "hpnicfNqaStatResPacketLateArrival": hpnicfNqaStatResPacketLateArrival,
       "hpnicfNqaStatResRttSum": hpnicfNqaStatResRttSum,
       "hpnicfNqaStatResNumOfDelaySD": hpnicfNqaStatResNumOfDelaySD,
       "hpnicfNqaStatResMinDelaySD": hpnicfNqaStatResMinDelaySD,
       "hpnicfNqaStatResMaxDelaySD": hpnicfNqaStatResMaxDelaySD,
       "hpnicfNqaStatResSumDelaySD": hpnicfNqaStatResSumDelaySD,
       "hpnicfNqaStatResSum2DelaySD": hpnicfNqaStatResSum2DelaySD,
       "hpnicfNqaStatResNumOfDelayDS": hpnicfNqaStatResNumOfDelayDS,
       "hpnicfNqaStatResMinDelayDS": hpnicfNqaStatResMinDelayDS,
       "hpnicfNqaStatResMaxDelayDS": hpnicfNqaStatResMaxDelayDS,
       "hpnicfNqaStatResSumDelayDS": hpnicfNqaStatResSumDelayDS,
       "hpnicfNqaStatResSum2DelayDS": hpnicfNqaStatResSum2DelayDS,
       "hpnicfNqaGroupStatsJitterTable": hpnicfNqaGroupStatsJitterTable,
       "hpnicfNqaGroupStatsJitterEntry": hpnicfNqaGroupStatsJitterEntry,
       "hpnicfNqaStatJitterIndex": hpnicfNqaStatJitterIndex,
       "hpnicfNqaStatJitterMinOfPosSD": hpnicfNqaStatJitterMinOfPosSD,
       "hpnicfNqaStatJitterMaxOfPosSD": hpnicfNqaStatJitterMaxOfPosSD,
       "hpnicfNqaStatJitterNumOfPosSD": hpnicfNqaStatJitterNumOfPosSD,
       "hpnicfNqaStatJitterSumOfPosSD": hpnicfNqaStatJitterSumOfPosSD,
       "hpnicfNqaStatJitterSumOfSquarePosSD": hpnicfNqaStatJitterSumOfSquarePosSD,
       "hpnicfNqaStatJitterMinOfNegSD": hpnicfNqaStatJitterMinOfNegSD,
       "hpnicfNqaStatJitterMaxOfNegSD": hpnicfNqaStatJitterMaxOfNegSD,
       "hpnicfNqaStatJitterNumOfNegSD": hpnicfNqaStatJitterNumOfNegSD,
       "hpnicfNqaStatJitterSumOfNegSD": hpnicfNqaStatJitterSumOfNegSD,
       "hpnicfNqaStatJitterSumOfSquareNegSD": hpnicfNqaStatJitterSumOfSquareNegSD,
       "hpnicfNqaStatJitterMinOfPosDS": hpnicfNqaStatJitterMinOfPosDS,
       "hpnicfNqaStatJitterMaxOfPosDS": hpnicfNqaStatJitterMaxOfPosDS,
       "hpnicfNqaStatJitterNumOfPosDS": hpnicfNqaStatJitterNumOfPosDS,
       "hpnicfNqaStatJitterSumOfPosDS": hpnicfNqaStatJitterSumOfPosDS,
       "hpnicfNqaStatJitterSumOfSquarePosDS": hpnicfNqaStatJitterSumOfSquarePosDS,
       "hpnicfNqaStatJitterMinOfNegDS": hpnicfNqaStatJitterMinOfNegDS,
       "hpnicfNqaStatJitterMaxOfNegDS": hpnicfNqaStatJitterMaxOfNegDS,
       "hpnicfNqaStatJitterNumOfNegDS": hpnicfNqaStatJitterNumOfNegDS,
       "hpnicfNqaStatJitterSumOfNegDS": hpnicfNqaStatJitterSumOfNegDS,
       "hpnicfNqaStatJitterSumOfSquareNegDS": hpnicfNqaStatJitterSumOfSquareNegDS,
       "hpnicfNqaStatJitterPacketLossSD": hpnicfNqaStatJitterPacketLossSD,
       "hpnicfNqaStatJitterPacketLossDS": hpnicfNqaStatJitterPacketLossDS,
       "hpnicfNqaStatJitterAvePosSD": hpnicfNqaStatJitterAvePosSD,
       "hpnicfNqaStatJitterAveNegSD": hpnicfNqaStatJitterAveNegSD,
       "hpnicfNqaStatJitterAvePosDS": hpnicfNqaStatJitterAvePosDS,
       "hpnicfNqaStatJitterAveNegDS": hpnicfNqaStatJitterAveNegDS,
       "hpnicfNqaStatJitterPktLossUnknown": hpnicfNqaStatJitterPktLossUnknown,
       "hpnicfNqaStatJitterMaxOfICPIF": hpnicfNqaStatJitterMaxOfICPIF,
       "hpnicfNqaStatJitterMinOfICPIF": hpnicfNqaStatJitterMinOfICPIF,
       "hpnicfNqaStatJitterMaxOfMOS": hpnicfNqaStatJitterMaxOfMOS,
       "hpnicfNqaStatJitterMinOfMOS": hpnicfNqaStatJitterMinOfMOS,
       "hpnicfNqaReactionTable": hpnicfNqaReactionTable,
       "hpnicfNqaReactionEntry": hpnicfNqaReactionEntry,
       "hpnicfNqaReactOwnerIndex": hpnicfNqaReactOwnerIndex,
       "hpnicfNqaReactTestName": hpnicfNqaReactTestName,
       "hpnicfNqaReactItemIndex": hpnicfNqaReactItemIndex,
       "hpnicfNqaReactCheckedElement": hpnicfNqaReactCheckedElement,
       "hpnicfNqaReactThresholdUpperLimit": hpnicfNqaReactThresholdUpperLimit,
       "hpnicfNqaReactThresholdLowerLimit": hpnicfNqaReactThresholdLowerLimit,
       "hpnicfNqaReactThresholdType": hpnicfNqaReactThresholdType,
       "hpnicfNqaReactThresholdConsecNum": hpnicfNqaReactThresholdConsecNum,
       "hpnicfNqaReactThresholdAccumNum": hpnicfNqaReactThresholdAccumNum,
       "hpnicfNqaReactActionType": hpnicfNqaReactActionType,
       "hpnicfNqaReactCurrentStatus": hpnicfNqaReactCurrentStatus,
       "hpnicfNqaReactRowStatus": hpnicfNqaReactRowStatus,
       "hpnicfNqaReactCheckedNum": hpnicfNqaReactCheckedNum,
       "hpnicfNqaReactThresholdNum": hpnicfNqaReactThresholdNum,
       "hpnicfNqaStatisticsReactionTable": hpnicfNqaStatisticsReactionTable,
       "hpnicfNqaStatisticsReactionEntry": hpnicfNqaStatisticsReactionEntry,
       "hpnicfNqaStatReactOwnerIndex": hpnicfNqaStatReactOwnerIndex,
       "hpnicfNqaStatReactTestName": hpnicfNqaStatReactTestName,
       "hpnicfNqaStatReactIndex": hpnicfNqaStatReactIndex,
       "hpnicfNqaStatReactItemIndex": hpnicfNqaStatReactItemIndex,
       "hpnicfNqaStatReactCheckedNum": hpnicfNqaStatReactCheckedNum,
       "hpnicfNqaStatReactThresholdNum": hpnicfNqaStatReactThresholdNum,
       "hpnicfNqaImplementationTypeDomains": hpnicfNqaImplementationTypeDomains,
       "hpnicfNqaUdpEcho": hpnicfNqaUdpEcho,
       "hpnicfNqaTcpconnect": hpnicfNqaTcpconnect,
       "hpnicfNqajitter": hpnicfNqajitter,
       "hpnicfNqaHttp": hpnicfNqaHttp,
       "hpnicfNqadlsw": hpnicfNqadlsw,
       "hpnicfNqadhcp": hpnicfNqadhcp,
       "hpnicfNqaftp": hpnicfNqaftp,
       "hpnicfNqaNotifications": hpnicfNqaNotifications,
       "hpnicfNqaProbeTimeOverThreshold": hpnicfNqaProbeTimeOverThreshold,
       "hpnicfNqaJitterRTTOverThreshold": hpnicfNqaJitterRTTOverThreshold,
       "hpnicfNqaProbeFailure": hpnicfNqaProbeFailure,
       "hpnicfNqaJitterPacketLoss": hpnicfNqaJitterPacketLoss,
       "hpnicfNqaJitterSDOverThreshold": hpnicfNqaJitterSDOverThreshold,
       "hpnicfNqaJitterDSOverThreshold": hpnicfNqaJitterDSOverThreshold,
       "hpnicfNqaICPIFOverThreshold": hpnicfNqaICPIFOverThreshold,
       "hpnicfNqaMOSOverThreshold": hpnicfNqaMOSOverThreshold}
)
