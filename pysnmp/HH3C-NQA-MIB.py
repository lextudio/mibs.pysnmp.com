# SNMP MIB module (HH3C-NQA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-NQA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:22 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cNqa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNqaObjects_ObjectIdentity = ObjectIdentity
hh3cNqaObjects = _Hh3cNqaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1)
)
_Hh3cNqaMIBVersion_Type = DisplayString
_Hh3cNqaMIBVersion_Object = MibScalar
hh3cNqaMIBVersion = _Hh3cNqaMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 1),
    _Hh3cNqaMIBVersion_Type()
)
hh3cNqaMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaMIBVersion.setStatus("current")
_Hh3cNqaCtlTable_Object = MibTable
hh3cNqaCtlTable = _Hh3cNqaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cNqaCtlTable.setStatus("current")
_Hh3cNqaCtlEntry_Object = MibTableRow
hh3cNqaCtlEntry = _Hh3cNqaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cNqaCtlEntry.setStatus("current")


class _Hh3cNqaCtlTargetPort_Type(Integer32):
    """Custom type hh3cNqaCtlTargetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cNqaCtlTargetPort_Type.__name__ = "Integer32"
_Hh3cNqaCtlTargetPort_Object = MibTableColumn
hh3cNqaCtlTargetPort = _Hh3cNqaCtlTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 1),
    _Hh3cNqaCtlTargetPort_Type()
)
hh3cNqaCtlTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlTargetPort.setStatus("current")


class _Hh3cNqaCtlSourcePort_Type(Integer32):
    """Custom type hh3cNqaCtlSourcePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cNqaCtlSourcePort_Type.__name__ = "Integer32"
_Hh3cNqaCtlSourcePort_Object = MibTableColumn
hh3cNqaCtlSourcePort = _Hh3cNqaCtlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 2),
    _Hh3cNqaCtlSourcePort_Type()
)
hh3cNqaCtlSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlSourcePort.setStatus("current")


class _Hh3cNqaCtlTTL_Type(Integer32):
    """Custom type hh3cNqaCtlTTL based on Integer32"""
    defaultValue = 20


_Hh3cNqaCtlTTL_Object = MibTableColumn
hh3cNqaCtlTTL = _Hh3cNqaCtlTTL_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 3),
    _Hh3cNqaCtlTTL_Type()
)
hh3cNqaCtlTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlTTL.setStatus("current")


class _Hh3cNqaCtlJitterAdminInterval_Type(Integer32):
    """Custom type hh3cNqaCtlJitterAdminInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_Hh3cNqaCtlJitterAdminInterval_Type.__name__ = "Integer32"
_Hh3cNqaCtlJitterAdminInterval_Object = MibTableColumn
hh3cNqaCtlJitterAdminInterval = _Hh3cNqaCtlJitterAdminInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 4),
    _Hh3cNqaCtlJitterAdminInterval_Type()
)
hh3cNqaCtlJitterAdminInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlJitterAdminInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaCtlJitterAdminInterval.setUnits("milliseconds")


class _Hh3cNqaCtlJitterAdminNumPackets_Type(Integer32):
    """Custom type hh3cNqaCtlJitterAdminNumPackets based on Integer32"""
    defaultValue = 10


_Hh3cNqaCtlJitterAdminNumPackets_Object = MibTableColumn
hh3cNqaCtlJitterAdminNumPackets = _Hh3cNqaCtlJitterAdminNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 5),
    _Hh3cNqaCtlJitterAdminNumPackets_Type()
)
hh3cNqaCtlJitterAdminNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlJitterAdminNumPackets.setStatus("current")


class _Hh3cNqaCtlHttpOperationType_Type(Integer32):
    """Custom type hh3cNqaCtlHttpOperationType based on Integer32"""
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
          ("post", 2))
    )


_Hh3cNqaCtlHttpOperationType_Type.__name__ = "Integer32"
_Hh3cNqaCtlHttpOperationType_Object = MibTableColumn
hh3cNqaCtlHttpOperationType = _Hh3cNqaCtlHttpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 6),
    _Hh3cNqaCtlHttpOperationType_Type()
)
hh3cNqaCtlHttpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlHttpOperationType.setStatus("current")


class _Hh3cNqaCtlHttpOperationString_Type(DisplayString):
    """Custom type hh3cNqaCtlHttpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cNqaCtlHttpOperationString_Type.__name__ = "DisplayString"
_Hh3cNqaCtlHttpOperationString_Object = MibTableColumn
hh3cNqaCtlHttpOperationString = _Hh3cNqaCtlHttpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 7),
    _Hh3cNqaCtlHttpOperationString_Type()
)
hh3cNqaCtlHttpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlHttpOperationString.setStatus("current")


class _Hh3cNqaCtlFtpOperationType_Type(Integer32):
    """Custom type hh3cNqaCtlFtpOperationType based on Integer32"""
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


_Hh3cNqaCtlFtpOperationType_Type.__name__ = "Integer32"
_Hh3cNqaCtlFtpOperationType_Object = MibTableColumn
hh3cNqaCtlFtpOperationType = _Hh3cNqaCtlFtpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 8),
    _Hh3cNqaCtlFtpOperationType_Type()
)
hh3cNqaCtlFtpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlFtpOperationType.setStatus("current")


class _Hh3cNqaCtlFtpUsername_Type(DisplayString):
    """Custom type hh3cNqaCtlFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cNqaCtlFtpUsername_Type.__name__ = "DisplayString"
_Hh3cNqaCtlFtpUsername_Object = MibTableColumn
hh3cNqaCtlFtpUsername = _Hh3cNqaCtlFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 9),
    _Hh3cNqaCtlFtpUsername_Type()
)
hh3cNqaCtlFtpUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlFtpUsername.setStatus("current")


class _Hh3cNqaCtlFtpPassword_Type(DisplayString):
    """Custom type hh3cNqaCtlFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cNqaCtlFtpPassword_Type.__name__ = "DisplayString"
_Hh3cNqaCtlFtpPassword_Object = MibTableColumn
hh3cNqaCtlFtpPassword = _Hh3cNqaCtlFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 10),
    _Hh3cNqaCtlFtpPassword_Type()
)
hh3cNqaCtlFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlFtpPassword.setStatus("current")


class _Hh3cNqaCtlFtpOperationString_Type(DisplayString):
    """Custom type hh3cNqaCtlFtpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cNqaCtlFtpOperationString_Type.__name__ = "DisplayString"
_Hh3cNqaCtlFtpOperationString_Object = MibTableColumn
hh3cNqaCtlFtpOperationString = _Hh3cNqaCtlFtpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 11),
    _Hh3cNqaCtlFtpOperationString_Type()
)
hh3cNqaCtlFtpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlFtpOperationString.setStatus("current")


class _Hh3cNqaCtlVPNInstance_Type(DisplayString):
    """Custom type hh3cNqaCtlVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cNqaCtlVPNInstance_Type.__name__ = "DisplayString"
_Hh3cNqaCtlVPNInstance_Object = MibTableColumn
hh3cNqaCtlVPNInstance = _Hh3cNqaCtlVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 12),
    _Hh3cNqaCtlVPNInstance_Type()
)
hh3cNqaCtlVPNInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlVPNInstance.setStatus("current")


class _Hh3cNqaCtlHistoryKeptTime_Type(Integer32):
    """Custom type hh3cNqaCtlHistoryKeptTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Hh3cNqaCtlHistoryKeptTime_Type.__name__ = "Integer32"
_Hh3cNqaCtlHistoryKeptTime_Object = MibTableColumn
hh3cNqaCtlHistoryKeptTime = _Hh3cNqaCtlHistoryKeptTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 13),
    _Hh3cNqaCtlHistoryKeptTime_Type()
)
hh3cNqaCtlHistoryKeptTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlHistoryKeptTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaCtlHistoryKeptTime.setUnits("minutes")


class _Hh3cNqaCtlHistoryEnable_Type(Integer32):
    """Custom type hh3cNqaCtlHistoryEnable based on Integer32"""
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


_Hh3cNqaCtlHistoryEnable_Type.__name__ = "Integer32"
_Hh3cNqaCtlHistoryEnable_Object = MibTableColumn
hh3cNqaCtlHistoryEnable = _Hh3cNqaCtlHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 14),
    _Hh3cNqaCtlHistoryEnable_Type()
)
hh3cNqaCtlHistoryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlHistoryEnable.setStatus("current")


class _Hh3cNqaCtlICPIFAdvFactor_Type(Integer32):
    """Custom type hh3cNqaCtlICPIFAdvFactor based on Integer32"""
    defaultValue = 0


_Hh3cNqaCtlICPIFAdvFactor_Object = MibTableColumn
hh3cNqaCtlICPIFAdvFactor = _Hh3cNqaCtlICPIFAdvFactor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 15),
    _Hh3cNqaCtlICPIFAdvFactor_Type()
)
hh3cNqaCtlICPIFAdvFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlICPIFAdvFactor.setStatus("current")


class _Hh3cNqaCtlCodecType_Type(Integer32):
    """Custom type hh3cNqaCtlCodecType based on Integer32"""
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


_Hh3cNqaCtlCodecType_Type.__name__ = "Integer32"
_Hh3cNqaCtlCodecType_Object = MibTableColumn
hh3cNqaCtlCodecType = _Hh3cNqaCtlCodecType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 2, 1, 16),
    _Hh3cNqaCtlCodecType_Type()
)
hh3cNqaCtlCodecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlCodecType.setStatus("current")
_Hh3cNqaResultsTable_Object = MibTable
hh3cNqaResultsTable = _Hh3cNqaResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cNqaResultsTable.setStatus("current")
_Hh3cNqaResultsEntry_Object = MibTableRow
hh3cNqaResultsEntry = _Hh3cNqaResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1)
)
hh3cNqaResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hh3cNqaResultsEntry.setStatus("current")
_Hh3cNqaResultsRttNumDisconnects_Type = Unsigned32
_Hh3cNqaResultsRttNumDisconnects_Object = MibTableColumn
hh3cNqaResultsRttNumDisconnects = _Hh3cNqaResultsRttNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 1),
    _Hh3cNqaResultsRttNumDisconnects_Type()
)
hh3cNqaResultsRttNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttNumDisconnects.setStatus("current")
_Hh3cNqaResultsRttTimeouts_Type = Unsigned32
_Hh3cNqaResultsRttTimeouts_Object = MibTableColumn
hh3cNqaResultsRttTimeouts = _Hh3cNqaResultsRttTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 2),
    _Hh3cNqaResultsRttTimeouts_Type()
)
hh3cNqaResultsRttTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttTimeouts.setStatus("current")
_Hh3cNqaResultsRttBusies_Type = Unsigned32
_Hh3cNqaResultsRttBusies_Object = MibTableColumn
hh3cNqaResultsRttBusies = _Hh3cNqaResultsRttBusies_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 3),
    _Hh3cNqaResultsRttBusies_Type()
)
hh3cNqaResultsRttBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttBusies.setStatus("current")
_Hh3cNqaResultsRttNoConnections_Type = Unsigned32
_Hh3cNqaResultsRttNoConnections_Object = MibTableColumn
hh3cNqaResultsRttNoConnections = _Hh3cNqaResultsRttNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 4),
    _Hh3cNqaResultsRttNoConnections_Type()
)
hh3cNqaResultsRttNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttNoConnections.setStatus("current")
_Hh3cNqaResultsRttDrops_Type = Unsigned32
_Hh3cNqaResultsRttDrops_Object = MibTableColumn
hh3cNqaResultsRttDrops = _Hh3cNqaResultsRttDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 5),
    _Hh3cNqaResultsRttDrops_Type()
)
hh3cNqaResultsRttDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttDrops.setStatus("current")
_Hh3cNqaResultsRttSequenceErrors_Type = Unsigned32
_Hh3cNqaResultsRttSequenceErrors_Object = MibTableColumn
hh3cNqaResultsRttSequenceErrors = _Hh3cNqaResultsRttSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 6),
    _Hh3cNqaResultsRttSequenceErrors_Type()
)
hh3cNqaResultsRttSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttSequenceErrors.setStatus("current")
_Hh3cNqaResultsRttStatsErrors_Type = Unsigned32
_Hh3cNqaResultsRttStatsErrors_Object = MibTableColumn
hh3cNqaResultsRttStatsErrors = _Hh3cNqaResultsRttStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 7),
    _Hh3cNqaResultsRttStatsErrors_Type()
)
hh3cNqaResultsRttStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttStatsErrors.setStatus("current")
_Hh3cNqaResultsMaxDelaySD_Type = Unsigned32
_Hh3cNqaResultsMaxDelaySD_Object = MibTableColumn
hh3cNqaResultsMaxDelaySD = _Hh3cNqaResultsMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 8),
    _Hh3cNqaResultsMaxDelaySD_Type()
)
hh3cNqaResultsMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsMaxDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaResultsMaxDelaySD.setUnits("milliseconds")
_Hh3cNqaResultsMaxDelayDS_Type = Unsigned32
_Hh3cNqaResultsMaxDelayDS_Object = MibTableColumn
hh3cNqaResultsMaxDelayDS = _Hh3cNqaResultsMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 9),
    _Hh3cNqaResultsMaxDelayDS_Type()
)
hh3cNqaResultsMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsMaxDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaResultsMaxDelayDS.setUnits("milliseconds")
_Hh3cNqaResultsLostPacketRatio_Type = Unsigned32
_Hh3cNqaResultsLostPacketRatio_Object = MibTableColumn
hh3cNqaResultsLostPacketRatio = _Hh3cNqaResultsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 10),
    _Hh3cNqaResultsLostPacketRatio_Type()
)
hh3cNqaResultsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsLostPacketRatio.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaResultsLostPacketRatio.setUnits("milliseconds")
_Hh3cNqaResultsPacketLateArrival_Type = Unsigned32
_Hh3cNqaResultsPacketLateArrival_Object = MibTableColumn
hh3cNqaResultsPacketLateArrival = _Hh3cNqaResultsPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 11),
    _Hh3cNqaResultsPacketLateArrival_Type()
)
hh3cNqaResultsPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsPacketLateArrival.setStatus("current")
_Hh3cNqaResultsRttSum_Type = Unsigned32
_Hh3cNqaResultsRttSum_Object = MibTableColumn
hh3cNqaResultsRttSum = _Hh3cNqaResultsRttSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 12),
    _Hh3cNqaResultsRttSum_Type()
)
hh3cNqaResultsRttSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsRttSum.setStatus("current")
_Hh3cNqaResultsNumOfDelaySD_Type = Unsigned32
_Hh3cNqaResultsNumOfDelaySD_Object = MibTableColumn
hh3cNqaResultsNumOfDelaySD = _Hh3cNqaResultsNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 13),
    _Hh3cNqaResultsNumOfDelaySD_Type()
)
hh3cNqaResultsNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsNumOfDelaySD.setStatus("current")
_Hh3cNqaResultsMinDelaySD_Type = Unsigned32
_Hh3cNqaResultsMinDelaySD_Object = MibTableColumn
hh3cNqaResultsMinDelaySD = _Hh3cNqaResultsMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 14),
    _Hh3cNqaResultsMinDelaySD_Type()
)
hh3cNqaResultsMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsMinDelaySD.setStatus("current")
_Hh3cNqaResultsSumDelaySD_Type = Unsigned32
_Hh3cNqaResultsSumDelaySD_Object = MibTableColumn
hh3cNqaResultsSumDelaySD = _Hh3cNqaResultsSumDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 15),
    _Hh3cNqaResultsSumDelaySD_Type()
)
hh3cNqaResultsSumDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsSumDelaySD.setStatus("current")
_Hh3cNqaResultsSum2DelaySD_Type = Unsigned32
_Hh3cNqaResultsSum2DelaySD_Object = MibTableColumn
hh3cNqaResultsSum2DelaySD = _Hh3cNqaResultsSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 16),
    _Hh3cNqaResultsSum2DelaySD_Type()
)
hh3cNqaResultsSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsSum2DelaySD.setStatus("current")
_Hh3cNqaResultsNumOfDelayDS_Type = Unsigned32
_Hh3cNqaResultsNumOfDelayDS_Object = MibTableColumn
hh3cNqaResultsNumOfDelayDS = _Hh3cNqaResultsNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 17),
    _Hh3cNqaResultsNumOfDelayDS_Type()
)
hh3cNqaResultsNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsNumOfDelayDS.setStatus("current")
_Hh3cNqaResultsMinDelayDS_Type = Unsigned32
_Hh3cNqaResultsMinDelayDS_Object = MibTableColumn
hh3cNqaResultsMinDelayDS = _Hh3cNqaResultsMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 18),
    _Hh3cNqaResultsMinDelayDS_Type()
)
hh3cNqaResultsMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsMinDelayDS.setStatus("current")
_Hh3cNqaResultsSumDelayDS_Type = Unsigned32
_Hh3cNqaResultsSumDelayDS_Object = MibTableColumn
hh3cNqaResultsSumDelayDS = _Hh3cNqaResultsSumDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 19),
    _Hh3cNqaResultsSumDelayDS_Type()
)
hh3cNqaResultsSumDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsSumDelayDS.setStatus("current")
_Hh3cNqaResultsSum2DelayDS_Type = Unsigned32
_Hh3cNqaResultsSum2DelayDS_Object = MibTableColumn
hh3cNqaResultsSum2DelayDS = _Hh3cNqaResultsSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 3, 1, 20),
    _Hh3cNqaResultsSum2DelayDS_Type()
)
hh3cNqaResultsSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaResultsSum2DelayDS.setStatus("current")
_Hh3cNqaJitterStatsTable_Object = MibTable
hh3cNqaJitterStatsTable = _Hh3cNqaJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsTable.setStatus("current")
_Hh3cNqaJitterStatsEntry_Object = MibTableRow
hh3cNqaJitterStatsEntry = _Hh3cNqaJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1)
)
hh3cNqaJitterStatsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsEntry.setStatus("current")
_Hh3cNqaJitterStatsNumOfRTT_Type = Counter32
_Hh3cNqaJitterStatsNumOfRTT_Object = MibTableColumn
hh3cNqaJitterStatsNumOfRTT = _Hh3cNqaJitterStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 1),
    _Hh3cNqaJitterStatsNumOfRTT_Type()
)
hh3cNqaJitterStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsNumOfRTT.setStatus("current")
_Hh3cNqaJitterStatsMinOfPositivesSD_Type = Gauge32
_Hh3cNqaJitterStatsMinOfPositivesSD_Object = MibTableColumn
hh3cNqaJitterStatsMinOfPositivesSD = _Hh3cNqaJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 2),
    _Hh3cNqaJitterStatsMinOfPositivesSD_Type()
)
hh3cNqaJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMinOfPositivesSD.setStatus("current")
_Hh3cNqaJitterStatsMaxOfPositivesSD_Type = Gauge32
_Hh3cNqaJitterStatsMaxOfPositivesSD_Object = MibTableColumn
hh3cNqaJitterStatsMaxOfPositivesSD = _Hh3cNqaJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 3),
    _Hh3cNqaJitterStatsMaxOfPositivesSD_Type()
)
hh3cNqaJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMaxOfPositivesSD.setStatus("current")
_Hh3cNqaJitterStatsNumOfPositivesSD_Type = Gauge32
_Hh3cNqaJitterStatsNumOfPositivesSD_Object = MibTableColumn
hh3cNqaJitterStatsNumOfPositivesSD = _Hh3cNqaJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 4),
    _Hh3cNqaJitterStatsNumOfPositivesSD_Type()
)
hh3cNqaJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsNumOfPositivesSD.setStatus("current")
_Hh3cNqaJitterStatsSumOfPositivesSD_Type = Gauge32
_Hh3cNqaJitterStatsSumOfPositivesSD_Object = MibTableColumn
hh3cNqaJitterStatsSumOfPositivesSD = _Hh3cNqaJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 5),
    _Hh3cNqaJitterStatsSumOfPositivesSD_Type()
)
hh3cNqaJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSumOfPositivesSD.setStatus("current")
_Hh3cNqaJitterStatsSum2PositivesSD_Type = Gauge32
_Hh3cNqaJitterStatsSum2PositivesSD_Object = MibTableColumn
hh3cNqaJitterStatsSum2PositivesSD = _Hh3cNqaJitterStatsSum2PositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 6),
    _Hh3cNqaJitterStatsSum2PositivesSD_Type()
)
hh3cNqaJitterStatsSum2PositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSum2PositivesSD.setStatus("current")
_Hh3cNqaJitterStatsMinOfNegativesSD_Type = Gauge32
_Hh3cNqaJitterStatsMinOfNegativesSD_Object = MibTableColumn
hh3cNqaJitterStatsMinOfNegativesSD = _Hh3cNqaJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 7),
    _Hh3cNqaJitterStatsMinOfNegativesSD_Type()
)
hh3cNqaJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMinOfNegativesSD.setStatus("current")
_Hh3cNqaJitterStatsMaxOfNegativesSD_Type = Gauge32
_Hh3cNqaJitterStatsMaxOfNegativesSD_Object = MibTableColumn
hh3cNqaJitterStatsMaxOfNegativesSD = _Hh3cNqaJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 8),
    _Hh3cNqaJitterStatsMaxOfNegativesSD_Type()
)
hh3cNqaJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMaxOfNegativesSD.setStatus("current")
_Hh3cNqaJitterStatsNumOfNegativesSD_Type = Gauge32
_Hh3cNqaJitterStatsNumOfNegativesSD_Object = MibTableColumn
hh3cNqaJitterStatsNumOfNegativesSD = _Hh3cNqaJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 9),
    _Hh3cNqaJitterStatsNumOfNegativesSD_Type()
)
hh3cNqaJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsNumOfNegativesSD.setStatus("current")
_Hh3cNqaJitterStatsSumOfNegativesSD_Type = Gauge32
_Hh3cNqaJitterStatsSumOfNegativesSD_Object = MibTableColumn
hh3cNqaJitterStatsSumOfNegativesSD = _Hh3cNqaJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 10),
    _Hh3cNqaJitterStatsSumOfNegativesSD_Type()
)
hh3cNqaJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSumOfNegativesSD.setStatus("current")
_Hh3cNqaJitterStatsSum2NegativesSD_Type = Gauge32
_Hh3cNqaJitterStatsSum2NegativesSD_Object = MibTableColumn
hh3cNqaJitterStatsSum2NegativesSD = _Hh3cNqaJitterStatsSum2NegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 11),
    _Hh3cNqaJitterStatsSum2NegativesSD_Type()
)
hh3cNqaJitterStatsSum2NegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSum2NegativesSD.setStatus("current")
_Hh3cNqaJitterStatsMinOfPositivesDS_Type = Gauge32
_Hh3cNqaJitterStatsMinOfPositivesDS_Object = MibTableColumn
hh3cNqaJitterStatsMinOfPositivesDS = _Hh3cNqaJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 12),
    _Hh3cNqaJitterStatsMinOfPositivesDS_Type()
)
hh3cNqaJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMinOfPositivesDS.setStatus("current")
_Hh3cNqaJitterStatsMaxOfPositivesDS_Type = Gauge32
_Hh3cNqaJitterStatsMaxOfPositivesDS_Object = MibTableColumn
hh3cNqaJitterStatsMaxOfPositivesDS = _Hh3cNqaJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 13),
    _Hh3cNqaJitterStatsMaxOfPositivesDS_Type()
)
hh3cNqaJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMaxOfPositivesDS.setStatus("current")
_Hh3cNqaJitterStatsNumOfPositivesDS_Type = Gauge32
_Hh3cNqaJitterStatsNumOfPositivesDS_Object = MibTableColumn
hh3cNqaJitterStatsNumOfPositivesDS = _Hh3cNqaJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 14),
    _Hh3cNqaJitterStatsNumOfPositivesDS_Type()
)
hh3cNqaJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsNumOfPositivesDS.setStatus("current")
_Hh3cNqaJitterStatsSumOfPositivesDS_Type = Gauge32
_Hh3cNqaJitterStatsSumOfPositivesDS_Object = MibTableColumn
hh3cNqaJitterStatsSumOfPositivesDS = _Hh3cNqaJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 15),
    _Hh3cNqaJitterStatsSumOfPositivesDS_Type()
)
hh3cNqaJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSumOfPositivesDS.setStatus("current")
_Hh3cNqaJitterStatsSum2PositivesDS_Type = Gauge32
_Hh3cNqaJitterStatsSum2PositivesDS_Object = MibTableColumn
hh3cNqaJitterStatsSum2PositivesDS = _Hh3cNqaJitterStatsSum2PositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 16),
    _Hh3cNqaJitterStatsSum2PositivesDS_Type()
)
hh3cNqaJitterStatsSum2PositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSum2PositivesDS.setStatus("current")
_Hh3cNqaJitterStatsMinOfNegativesDS_Type = Gauge32
_Hh3cNqaJitterStatsMinOfNegativesDS_Object = MibTableColumn
hh3cNqaJitterStatsMinOfNegativesDS = _Hh3cNqaJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 17),
    _Hh3cNqaJitterStatsMinOfNegativesDS_Type()
)
hh3cNqaJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMinOfNegativesDS.setStatus("current")
_Hh3cNqaJitterStatsMaxOfNegativesDS_Type = Gauge32
_Hh3cNqaJitterStatsMaxOfNegativesDS_Object = MibTableColumn
hh3cNqaJitterStatsMaxOfNegativesDS = _Hh3cNqaJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 18),
    _Hh3cNqaJitterStatsMaxOfNegativesDS_Type()
)
hh3cNqaJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsMaxOfNegativesDS.setStatus("current")
_Hh3cNqaJitterStatsNumOfNegativesDS_Type = Gauge32
_Hh3cNqaJitterStatsNumOfNegativesDS_Object = MibTableColumn
hh3cNqaJitterStatsNumOfNegativesDS = _Hh3cNqaJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 19),
    _Hh3cNqaJitterStatsNumOfNegativesDS_Type()
)
hh3cNqaJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsNumOfNegativesDS.setStatus("current")
_Hh3cNqaJitterStatsSumOfNegativesDS_Type = Gauge32
_Hh3cNqaJitterStatsSumOfNegativesDS_Object = MibTableColumn
hh3cNqaJitterStatsSumOfNegativesDS = _Hh3cNqaJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 20),
    _Hh3cNqaJitterStatsSumOfNegativesDS_Type()
)
hh3cNqaJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSumOfNegativesDS.setStatus("current")
_Hh3cNqaJitterStatsSum2NegativesDS_Type = Gauge32
_Hh3cNqaJitterStatsSum2NegativesDS_Object = MibTableColumn
hh3cNqaJitterStatsSum2NegativesDS = _Hh3cNqaJitterStatsSum2NegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 21),
    _Hh3cNqaJitterStatsSum2NegativesDS_Type()
)
hh3cNqaJitterStatsSum2NegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsSum2NegativesDS.setStatus("current")
_Hh3cNqaJitterStatsPacketLossSD_Type = Gauge32
_Hh3cNqaJitterStatsPacketLossSD_Object = MibTableColumn
hh3cNqaJitterStatsPacketLossSD = _Hh3cNqaJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 22),
    _Hh3cNqaJitterStatsPacketLossSD_Type()
)
hh3cNqaJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsPacketLossSD.setStatus("current")
_Hh3cNqaJitterStatsPacketLossDS_Type = Gauge32
_Hh3cNqaJitterStatsPacketLossDS_Object = MibTableColumn
hh3cNqaJitterStatsPacketLossDS = _Hh3cNqaJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 23),
    _Hh3cNqaJitterStatsPacketLossDS_Type()
)
hh3cNqaJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsPacketLossDS.setStatus("current")
_Hh3cNqaJitterStatsAvePositivesSD_Type = Gauge32
_Hh3cNqaJitterStatsAvePositivesSD_Object = MibTableColumn
hh3cNqaJitterStatsAvePositivesSD = _Hh3cNqaJitterStatsAvePositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 24),
    _Hh3cNqaJitterStatsAvePositivesSD_Type()
)
hh3cNqaJitterStatsAvePositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsAvePositivesSD.setStatus("current")
_Hh3cNqaJitterStatsAveNegativesSD_Type = Gauge32
_Hh3cNqaJitterStatsAveNegativesSD_Object = MibTableColumn
hh3cNqaJitterStatsAveNegativesSD = _Hh3cNqaJitterStatsAveNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 25),
    _Hh3cNqaJitterStatsAveNegativesSD_Type()
)
hh3cNqaJitterStatsAveNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsAveNegativesSD.setStatus("current")
_Hh3cNqaJitterStatsAvePositivesDS_Type = Gauge32
_Hh3cNqaJitterStatsAvePositivesDS_Object = MibTableColumn
hh3cNqaJitterStatsAvePositivesDS = _Hh3cNqaJitterStatsAvePositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 26),
    _Hh3cNqaJitterStatsAvePositivesDS_Type()
)
hh3cNqaJitterStatsAvePositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsAvePositivesDS.setStatus("current")
_Hh3cNqaJitterStatsAveNegativesDS_Type = Gauge32
_Hh3cNqaJitterStatsAveNegativesDS_Object = MibTableColumn
hh3cNqaJitterStatsAveNegativesDS = _Hh3cNqaJitterStatsAveNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 27),
    _Hh3cNqaJitterStatsAveNegativesDS_Type()
)
hh3cNqaJitterStatsAveNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsAveNegativesDS.setStatus("current")
_Hh3cNqaJitterStatsPktLossUnknown_Type = Gauge32
_Hh3cNqaJitterStatsPktLossUnknown_Object = MibTableColumn
hh3cNqaJitterStatsPktLossUnknown = _Hh3cNqaJitterStatsPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 28),
    _Hh3cNqaJitterStatsPktLossUnknown_Type()
)
hh3cNqaJitterStatsPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsPktLossUnknown.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsPktLossUnknown.setUnits("milliseconds")
_Hh3cNqaJitterStatsOperOfICPIF_Type = Gauge32
_Hh3cNqaJitterStatsOperOfICPIF_Object = MibTableColumn
hh3cNqaJitterStatsOperOfICPIF = _Hh3cNqaJitterStatsOperOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 29),
    _Hh3cNqaJitterStatsOperOfICPIF_Type()
)
hh3cNqaJitterStatsOperOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsOperOfICPIF.setStatus("current")
_Hh3cNqaJitterStatsOperOfMOS_Type = Gauge32
_Hh3cNqaJitterStatsOperOfMOS_Object = MibTableColumn
hh3cNqaJitterStatsOperOfMOS = _Hh3cNqaJitterStatsOperOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 4, 1, 30),
    _Hh3cNqaJitterStatsOperOfMOS_Type()
)
hh3cNqaJitterStatsOperOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaJitterStatsOperOfMOS.setStatus("current")


class _Hh3cNqaAgentEnable_Type(Integer32):
    """Custom type hh3cNqaAgentEnable based on Integer32"""
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


_Hh3cNqaAgentEnable_Type.__name__ = "Integer32"
_Hh3cNqaAgentEnable_Object = MibScalar
hh3cNqaAgentEnable = _Hh3cNqaAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 5),
    _Hh3cNqaAgentEnable_Type()
)
hh3cNqaAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNqaAgentEnable.setStatus("current")
_Hh3cNqaTcpServerTable_Object = MibTable
hh3cNqaTcpServerTable = _Hh3cNqaTcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cNqaTcpServerTable.setStatus("current")
_Hh3cNqaTcpServerEntry_Object = MibTableRow
hh3cNqaTcpServerEntry = _Hh3cNqaTcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 6, 1)
)
hh3cNqaTcpServerEntry.setIndexNames(
    (0, "HH3C-NQA-MIB", "hh3cNqaTcpServerIpAddress"),
    (0, "HH3C-NQA-MIB", "hh3cNqaTcpServerPort"),
)
if mibBuilder.loadTexts:
    hh3cNqaTcpServerEntry.setStatus("current")


class _Hh3cNqaTcpServerIpAddress_Type(InetAddress):
    """Custom type hh3cNqaTcpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_Hh3cNqaTcpServerIpAddress_Object = MibTableColumn
hh3cNqaTcpServerIpAddress = _Hh3cNqaTcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 6, 1, 1),
    _Hh3cNqaTcpServerIpAddress_Type()
)
hh3cNqaTcpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaTcpServerIpAddress.setStatus("current")


class _Hh3cNqaTcpServerPort_Type(Integer32):
    """Custom type hh3cNqaTcpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cNqaTcpServerPort_Type.__name__ = "Integer32"
_Hh3cNqaTcpServerPort_Object = MibTableColumn
hh3cNqaTcpServerPort = _Hh3cNqaTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 6, 1, 2),
    _Hh3cNqaTcpServerPort_Type()
)
hh3cNqaTcpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaTcpServerPort.setStatus("current")
_Hh3cNqaTcpServerRowStatus_Type = RowStatus
_Hh3cNqaTcpServerRowStatus_Object = MibTableColumn
hh3cNqaTcpServerRowStatus = _Hh3cNqaTcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 6, 1, 3),
    _Hh3cNqaTcpServerRowStatus_Type()
)
hh3cNqaTcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaTcpServerRowStatus.setStatus("current")
_Hh3cNqaUdpServerTable_Object = MibTable
hh3cNqaUdpServerTable = _Hh3cNqaUdpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cNqaUdpServerTable.setStatus("current")
_Hh3cNqaUdpServerEntry_Object = MibTableRow
hh3cNqaUdpServerEntry = _Hh3cNqaUdpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 7, 1)
)
hh3cNqaUdpServerEntry.setIndexNames(
    (0, "HH3C-NQA-MIB", "hh3cNqaUdpServerIpAddress"),
    (0, "HH3C-NQA-MIB", "hh3cNqaUdpServerPort"),
)
if mibBuilder.loadTexts:
    hh3cNqaUdpServerEntry.setStatus("current")


class _Hh3cNqaUdpServerIpAddress_Type(InetAddress):
    """Custom type hh3cNqaUdpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_Hh3cNqaUdpServerIpAddress_Object = MibTableColumn
hh3cNqaUdpServerIpAddress = _Hh3cNqaUdpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 7, 1, 1),
    _Hh3cNqaUdpServerIpAddress_Type()
)
hh3cNqaUdpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaUdpServerIpAddress.setStatus("current")


class _Hh3cNqaUdpServerPort_Type(Integer32):
    """Custom type hh3cNqaUdpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cNqaUdpServerPort_Type.__name__ = "Integer32"
_Hh3cNqaUdpServerPort_Object = MibTableColumn
hh3cNqaUdpServerPort = _Hh3cNqaUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 7, 1, 2),
    _Hh3cNqaUdpServerPort_Type()
)
hh3cNqaUdpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaUdpServerPort.setStatus("current")
_Hh3cNqaUdpServerRowStatus_Type = RowStatus
_Hh3cNqaUdpServerRowStatus_Object = MibTableColumn
hh3cNqaUdpServerRowStatus = _Hh3cNqaUdpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 7, 1, 3),
    _Hh3cNqaUdpServerRowStatus_Type()
)
hh3cNqaUdpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaUdpServerRowStatus.setStatus("current")


class _Hh3cNqaServerEnable_Type(Integer32):
    """Custom type hh3cNqaServerEnable based on Integer32"""
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


_Hh3cNqaServerEnable_Type.__name__ = "Integer32"
_Hh3cNqaServerEnable_Object = MibScalar
hh3cNqaServerEnable = _Hh3cNqaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 8),
    _Hh3cNqaServerEnable_Type()
)
hh3cNqaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNqaServerEnable.setStatus("current")
_Hh3cNqaStatsMaxGroupNumber_Type = Integer32
_Hh3cNqaStatsMaxGroupNumber_Object = MibScalar
hh3cNqaStatsMaxGroupNumber = _Hh3cNqaStatsMaxGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 9),
    _Hh3cNqaStatsMaxGroupNumber_Type()
)
hh3cNqaStatsMaxGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatsMaxGroupNumber.setStatus("current")
_Hh3cNqaStatisticsCtlTable_Object = MibTable
hh3cNqaStatisticsCtlTable = _Hh3cNqaStatisticsCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cNqaStatisticsCtlTable.setStatus("current")
_Hh3cNqaStatisticsCtlEntry_Object = MibTableRow
hh3cNqaStatisticsCtlEntry = _Hh3cNqaStatisticsCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hh3cNqaStatisticsCtlEntry.setStatus("current")
_Hh3cNqaCtlStatisticsInterval_Type = Unsigned32
_Hh3cNqaCtlStatisticsInterval_Object = MibTableColumn
hh3cNqaCtlStatisticsInterval = _Hh3cNqaCtlStatisticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 10, 1, 1),
    _Hh3cNqaCtlStatisticsInterval_Type()
)
hh3cNqaCtlStatisticsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlStatisticsInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaCtlStatisticsInterval.setUnits("minutes")


class _Hh3cNqaCtlStatisticsGroupNumber_Type(Unsigned32):
    """Custom type hh3cNqaCtlStatisticsGroupNumber based on Unsigned32"""
    defaultValue = 2


_Hh3cNqaCtlStatisticsGroupNumber_Object = MibTableColumn
hh3cNqaCtlStatisticsGroupNumber = _Hh3cNqaCtlStatisticsGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 10, 1, 2),
    _Hh3cNqaCtlStatisticsGroupNumber_Type()
)
hh3cNqaCtlStatisticsGroupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlStatisticsGroupNumber.setStatus("current")


class _Hh3cNqaCtlStatisticsKeptTime_Type(Unsigned32):
    """Custom type hh3cNqaCtlStatisticsKeptTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Hh3cNqaCtlStatisticsKeptTime_Type.__name__ = "Unsigned32"
_Hh3cNqaCtlStatisticsKeptTime_Object = MibTableColumn
hh3cNqaCtlStatisticsKeptTime = _Hh3cNqaCtlStatisticsKeptTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 10, 1, 3),
    _Hh3cNqaCtlStatisticsKeptTime_Type()
)
hh3cNqaCtlStatisticsKeptTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlStatisticsKeptTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaCtlStatisticsKeptTime.setUnits("minutes")
_Hh3cNqaCtlBeginTime_Type = DateAndTime
_Hh3cNqaCtlBeginTime_Object = MibTableColumn
hh3cNqaCtlBeginTime = _Hh3cNqaCtlBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 10, 1, 4),
    _Hh3cNqaCtlBeginTime_Type()
)
hh3cNqaCtlBeginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlBeginTime.setStatus("current")


class _Hh3cNqaCtlLifeTime_Type(Unsigned32):
    """Custom type hh3cNqaCtlLifeTime based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaCtlLifeTime_Object = MibTableColumn
hh3cNqaCtlLifeTime = _Hh3cNqaCtlLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 10, 1, 5),
    _Hh3cNqaCtlLifeTime_Type()
)
hh3cNqaCtlLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaCtlLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaCtlLifeTime.setUnits("seconds")
_Hh3cNqaStatisticsResultsTable_Object = MibTable
hh3cNqaStatisticsResultsTable = _Hh3cNqaStatisticsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cNqaStatisticsResultsTable.setStatus("current")
_Hh3cNqaStatisticsResultsEntry_Object = MibTableRow
hh3cNqaStatisticsResultsEntry = _Hh3cNqaStatisticsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1)
)
hh3cNqaStatisticsResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "HH3C-NQA-MIB", "hh3cNqaStatResIndex"),
)
if mibBuilder.loadTexts:
    hh3cNqaStatisticsResultsEntry.setStatus("current")


class _Hh3cNqaStatResIndex_Type(Unsigned32):
    """Custom type hh3cNqaStatResIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cNqaStatResIndex_Type.__name__ = "Unsigned32"
_Hh3cNqaStatResIndex_Object = MibTableColumn
hh3cNqaStatResIndex = _Hh3cNqaStatResIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 1),
    _Hh3cNqaStatResIndex_Type()
)
hh3cNqaStatResIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaStatResIndex.setStatus("current")


class _Hh3cNqaStatResIpTargetAddressType_Type(InetAddressType):
    """Custom type hh3cNqaStatResIpTargetAddressType based on InetAddressType"""


_Hh3cNqaStatResIpTargetAddressType_Object = MibTableColumn
hh3cNqaStatResIpTargetAddressType = _Hh3cNqaStatResIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 2),
    _Hh3cNqaStatResIpTargetAddressType_Type()
)
hh3cNqaStatResIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResIpTargetAddressType.setStatus("current")


class _Hh3cNqaStatResIpTargetAddress_Type(InetAddress):
    """Custom type hh3cNqaStatResIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_Hh3cNqaStatResIpTargetAddress_Object = MibTableColumn
hh3cNqaStatResIpTargetAddress = _Hh3cNqaStatResIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 3),
    _Hh3cNqaStatResIpTargetAddress_Type()
)
hh3cNqaStatResIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResIpTargetAddress.setStatus("current")
_Hh3cNqaStatResMinRtt_Type = Gauge32
_Hh3cNqaStatResMinRtt_Object = MibTableColumn
hh3cNqaStatResMinRtt = _Hh3cNqaStatResMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 4),
    _Hh3cNqaStatResMinRtt_Type()
)
hh3cNqaStatResMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatResMinRtt.setUnits("milliseconds")
_Hh3cNqaStatResMaxRtt_Type = Gauge32
_Hh3cNqaStatResMaxRtt_Object = MibTableColumn
hh3cNqaStatResMaxRtt = _Hh3cNqaStatResMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 5),
    _Hh3cNqaStatResMaxRtt_Type()
)
hh3cNqaStatResMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatResMaxRtt.setUnits("milliseconds")
_Hh3cNqaStatResAverageRtt_Type = Gauge32
_Hh3cNqaStatResAverageRtt_Object = MibTableColumn
hh3cNqaStatResAverageRtt = _Hh3cNqaStatResAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 6),
    _Hh3cNqaStatResAverageRtt_Type()
)
hh3cNqaStatResAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatResAverageRtt.setUnits("milliseconds")
_Hh3cNqaStatResProbeResponses_Type = Counter32
_Hh3cNqaStatResProbeResponses_Object = MibTableColumn
hh3cNqaStatResProbeResponses = _Hh3cNqaStatResProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 7),
    _Hh3cNqaStatResProbeResponses_Type()
)
hh3cNqaStatResProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResProbeResponses.setStatus("current")
_Hh3cNqaStatResSentProbes_Type = Counter32
_Hh3cNqaStatResSentProbes_Object = MibTableColumn
hh3cNqaStatResSentProbes = _Hh3cNqaStatResSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 8),
    _Hh3cNqaStatResSentProbes_Type()
)
hh3cNqaStatResSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatResSentProbes.setUnits("probes")
_Hh3cNqaStatResRttSumOfSquares_Type = Counter32
_Hh3cNqaStatResRttSumOfSquares_Object = MibTableColumn
hh3cNqaStatResRttSumOfSquares = _Hh3cNqaStatResRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 9),
    _Hh3cNqaStatResRttSumOfSquares_Type()
)
hh3cNqaStatResRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttSumOfSquares.setUnits("milliseconds")
_Hh3cNqaStatResStartTime_Type = DateAndTime
_Hh3cNqaStatResStartTime_Object = MibTableColumn
hh3cNqaStatResStartTime = _Hh3cNqaStatResStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 10),
    _Hh3cNqaStatResStartTime_Type()
)
hh3cNqaStatResStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResStartTime.setStatus("current")
_Hh3cNqaStatResInterval_Type = Gauge32
_Hh3cNqaStatResInterval_Object = MibTableColumn
hh3cNqaStatResInterval = _Hh3cNqaStatResInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 11),
    _Hh3cNqaStatResInterval_Type()
)
hh3cNqaStatResInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatResInterval.setUnits("seconds")
_Hh3cNqaStatResRttNumDisconnects_Type = Counter32
_Hh3cNqaStatResRttNumDisconnects_Object = MibTableColumn
hh3cNqaStatResRttNumDisconnects = _Hh3cNqaStatResRttNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 12),
    _Hh3cNqaStatResRttNumDisconnects_Type()
)
hh3cNqaStatResRttNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttNumDisconnects.setStatus("current")
_Hh3cNqaStatResRttTimeouts_Type = Counter32
_Hh3cNqaStatResRttTimeouts_Object = MibTableColumn
hh3cNqaStatResRttTimeouts = _Hh3cNqaStatResRttTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 13),
    _Hh3cNqaStatResRttTimeouts_Type()
)
hh3cNqaStatResRttTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttTimeouts.setStatus("current")
_Hh3cNqaStatResRttBusies_Type = Counter32
_Hh3cNqaStatResRttBusies_Object = MibTableColumn
hh3cNqaStatResRttBusies = _Hh3cNqaStatResRttBusies_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 14),
    _Hh3cNqaStatResRttBusies_Type()
)
hh3cNqaStatResRttBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttBusies.setStatus("current")
_Hh3cNqaStatResRttNoConnections_Type = Counter32
_Hh3cNqaStatResRttNoConnections_Object = MibTableColumn
hh3cNqaStatResRttNoConnections = _Hh3cNqaStatResRttNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 15),
    _Hh3cNqaStatResRttNoConnections_Type()
)
hh3cNqaStatResRttNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttNoConnections.setStatus("current")
_Hh3cNqaStatResRttDrops_Type = Counter32
_Hh3cNqaStatResRttDrops_Object = MibTableColumn
hh3cNqaStatResRttDrops = _Hh3cNqaStatResRttDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 16),
    _Hh3cNqaStatResRttDrops_Type()
)
hh3cNqaStatResRttDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttDrops.setStatus("current")
_Hh3cNqaStatResRttSequenceErrors_Type = Counter32
_Hh3cNqaStatResRttSequenceErrors_Object = MibTableColumn
hh3cNqaStatResRttSequenceErrors = _Hh3cNqaStatResRttSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 17),
    _Hh3cNqaStatResRttSequenceErrors_Type()
)
hh3cNqaStatResRttSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttSequenceErrors.setStatus("current")
_Hh3cNqaStatResRttErrors_Type = Counter32
_Hh3cNqaStatResRttErrors_Object = MibTableColumn
hh3cNqaStatResRttErrors = _Hh3cNqaStatResRttErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 18),
    _Hh3cNqaStatResRttErrors_Type()
)
hh3cNqaStatResRttErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttErrors.setStatus("current")
_Hh3cNqaStatResLostPacketRatio_Type = Gauge32
_Hh3cNqaStatResLostPacketRatio_Object = MibTableColumn
hh3cNqaStatResLostPacketRatio = _Hh3cNqaStatResLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 19),
    _Hh3cNqaStatResLostPacketRatio_Type()
)
hh3cNqaStatResLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResLostPacketRatio.setStatus("current")
_Hh3cNqaStatResPacketLateArrival_Type = Counter32
_Hh3cNqaStatResPacketLateArrival_Object = MibTableColumn
hh3cNqaStatResPacketLateArrival = _Hh3cNqaStatResPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 20),
    _Hh3cNqaStatResPacketLateArrival_Type()
)
hh3cNqaStatResPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResPacketLateArrival.setStatus("current")
_Hh3cNqaStatResRttSum_Type = Counter32
_Hh3cNqaStatResRttSum_Object = MibTableColumn
hh3cNqaStatResRttSum = _Hh3cNqaStatResRttSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 21),
    _Hh3cNqaStatResRttSum_Type()
)
hh3cNqaStatResRttSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResRttSum.setStatus("current")
_Hh3cNqaStatResNumOfDelaySD_Type = Counter32
_Hh3cNqaStatResNumOfDelaySD_Object = MibTableColumn
hh3cNqaStatResNumOfDelaySD = _Hh3cNqaStatResNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 22),
    _Hh3cNqaStatResNumOfDelaySD_Type()
)
hh3cNqaStatResNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResNumOfDelaySD.setStatus("current")
_Hh3cNqaStatResMinDelaySD_Type = Gauge32
_Hh3cNqaStatResMinDelaySD_Object = MibTableColumn
hh3cNqaStatResMinDelaySD = _Hh3cNqaStatResMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 23),
    _Hh3cNqaStatResMinDelaySD_Type()
)
hh3cNqaStatResMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResMinDelaySD.setStatus("current")
_Hh3cNqaStatResMaxDelaySD_Type = Gauge32
_Hh3cNqaStatResMaxDelaySD_Object = MibTableColumn
hh3cNqaStatResMaxDelaySD = _Hh3cNqaStatResMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 24),
    _Hh3cNqaStatResMaxDelaySD_Type()
)
hh3cNqaStatResMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResMaxDelaySD.setStatus("current")
_Hh3cNqaStatResSumDelaySD_Type = Counter32
_Hh3cNqaStatResSumDelaySD_Object = MibTableColumn
hh3cNqaStatResSumDelaySD = _Hh3cNqaStatResSumDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 25),
    _Hh3cNqaStatResSumDelaySD_Type()
)
hh3cNqaStatResSumDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResSumDelaySD.setStatus("current")
_Hh3cNqaStatResSum2DelaySD_Type = Counter32
_Hh3cNqaStatResSum2DelaySD_Object = MibTableColumn
hh3cNqaStatResSum2DelaySD = _Hh3cNqaStatResSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 26),
    _Hh3cNqaStatResSum2DelaySD_Type()
)
hh3cNqaStatResSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResSum2DelaySD.setStatus("current")
_Hh3cNqaStatResNumOfDelayDS_Type = Counter32
_Hh3cNqaStatResNumOfDelayDS_Object = MibTableColumn
hh3cNqaStatResNumOfDelayDS = _Hh3cNqaStatResNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 27),
    _Hh3cNqaStatResNumOfDelayDS_Type()
)
hh3cNqaStatResNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResNumOfDelayDS.setStatus("current")
_Hh3cNqaStatResMinDelayDS_Type = Gauge32
_Hh3cNqaStatResMinDelayDS_Object = MibTableColumn
hh3cNqaStatResMinDelayDS = _Hh3cNqaStatResMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 28),
    _Hh3cNqaStatResMinDelayDS_Type()
)
hh3cNqaStatResMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResMinDelayDS.setStatus("current")
_Hh3cNqaStatResMaxDelayDS_Type = Gauge32
_Hh3cNqaStatResMaxDelayDS_Object = MibTableColumn
hh3cNqaStatResMaxDelayDS = _Hh3cNqaStatResMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 29),
    _Hh3cNqaStatResMaxDelayDS_Type()
)
hh3cNqaStatResMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResMaxDelayDS.setStatus("current")
_Hh3cNqaStatResSumDelayDS_Type = Counter32
_Hh3cNqaStatResSumDelayDS_Object = MibTableColumn
hh3cNqaStatResSumDelayDS = _Hh3cNqaStatResSumDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 30),
    _Hh3cNqaStatResSumDelayDS_Type()
)
hh3cNqaStatResSumDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResSumDelayDS.setStatus("current")
_Hh3cNqaStatResSum2DelayDS_Type = Counter32
_Hh3cNqaStatResSum2DelayDS_Object = MibTableColumn
hh3cNqaStatResSum2DelayDS = _Hh3cNqaStatResSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 11, 1, 31),
    _Hh3cNqaStatResSum2DelayDS_Type()
)
hh3cNqaStatResSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatResSum2DelayDS.setStatus("current")
_Hh3cNqaGroupStatsJitterTable_Object = MibTable
hh3cNqaGroupStatsJitterTable = _Hh3cNqaGroupStatsJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12)
)
if mibBuilder.loadTexts:
    hh3cNqaGroupStatsJitterTable.setStatus("current")
_Hh3cNqaGroupStatsJitterEntry_Object = MibTableRow
hh3cNqaGroupStatsJitterEntry = _Hh3cNqaGroupStatsJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1)
)
hh3cNqaGroupStatsJitterEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "HH3C-NQA-MIB", "hh3cNqaStatJitterIndex"),
)
if mibBuilder.loadTexts:
    hh3cNqaGroupStatsJitterEntry.setStatus("current")


class _Hh3cNqaStatJitterIndex_Type(Unsigned32):
    """Custom type hh3cNqaStatJitterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cNqaStatJitterIndex_Type.__name__ = "Unsigned32"
_Hh3cNqaStatJitterIndex_Object = MibTableColumn
hh3cNqaStatJitterIndex = _Hh3cNqaStatJitterIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 1),
    _Hh3cNqaStatJitterIndex_Type()
)
hh3cNqaStatJitterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterIndex.setStatus("current")
_Hh3cNqaStatJitterMinOfPosSD_Type = Gauge32
_Hh3cNqaStatJitterMinOfPosSD_Object = MibTableColumn
hh3cNqaStatJitterMinOfPosSD = _Hh3cNqaStatJitterMinOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 2),
    _Hh3cNqaStatJitterMinOfPosSD_Type()
)
hh3cNqaStatJitterMinOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfPosSD.setUnits("milliseconds")
_Hh3cNqaStatJitterMaxOfPosSD_Type = Gauge32
_Hh3cNqaStatJitterMaxOfPosSD_Object = MibTableColumn
hh3cNqaStatJitterMaxOfPosSD = _Hh3cNqaStatJitterMaxOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 3),
    _Hh3cNqaStatJitterMaxOfPosSD_Type()
)
hh3cNqaStatJitterMaxOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfPosSD.setUnits("milliseconds")
_Hh3cNqaStatJitterNumOfPosSD_Type = Counter32
_Hh3cNqaStatJitterNumOfPosSD_Object = MibTableColumn
hh3cNqaStatJitterNumOfPosSD = _Hh3cNqaStatJitterNumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 4),
    _Hh3cNqaStatJitterNumOfPosSD_Type()
)
hh3cNqaStatJitterNumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterNumOfPosSD.setStatus("current")
_Hh3cNqaStatJitterSumOfPosSD_Type = Counter32
_Hh3cNqaStatJitterSumOfPosSD_Object = MibTableColumn
hh3cNqaStatJitterSumOfPosSD = _Hh3cNqaStatJitterSumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 5),
    _Hh3cNqaStatJitterSumOfPosSD_Type()
)
hh3cNqaStatJitterSumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfPosSD.setUnits("milliseconds")
_Hh3cNqaStatJitterSumOfSquarePosSD_Type = Counter32
_Hh3cNqaStatJitterSumOfSquarePosSD_Object = MibTableColumn
hh3cNqaStatJitterSumOfSquarePosSD = _Hh3cNqaStatJitterSumOfSquarePosSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 6),
    _Hh3cNqaStatJitterSumOfSquarePosSD_Type()
)
hh3cNqaStatJitterSumOfSquarePosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquarePosSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquarePosSD.setUnits("milliseconds")
_Hh3cNqaStatJitterMinOfNegSD_Type = Gauge32
_Hh3cNqaStatJitterMinOfNegSD_Object = MibTableColumn
hh3cNqaStatJitterMinOfNegSD = _Hh3cNqaStatJitterMinOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 7),
    _Hh3cNqaStatJitterMinOfNegSD_Type()
)
hh3cNqaStatJitterMinOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfNegSD.setUnits("milliseconds")
_Hh3cNqaStatJitterMaxOfNegSD_Type = Gauge32
_Hh3cNqaStatJitterMaxOfNegSD_Object = MibTableColumn
hh3cNqaStatJitterMaxOfNegSD = _Hh3cNqaStatJitterMaxOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 8),
    _Hh3cNqaStatJitterMaxOfNegSD_Type()
)
hh3cNqaStatJitterMaxOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfNegSD.setUnits("milliseconds")
_Hh3cNqaStatJitterNumOfNegSD_Type = Counter32
_Hh3cNqaStatJitterNumOfNegSD_Object = MibTableColumn
hh3cNqaStatJitterNumOfNegSD = _Hh3cNqaStatJitterNumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 9),
    _Hh3cNqaStatJitterNumOfNegSD_Type()
)
hh3cNqaStatJitterNumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterNumOfNegSD.setStatus("current")
_Hh3cNqaStatJitterSumOfNegSD_Type = Counter32
_Hh3cNqaStatJitterSumOfNegSD_Object = MibTableColumn
hh3cNqaStatJitterSumOfNegSD = _Hh3cNqaStatJitterSumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 10),
    _Hh3cNqaStatJitterSumOfNegSD_Type()
)
hh3cNqaStatJitterSumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfNegSD.setUnits("milliseconds")
_Hh3cNqaStatJitterSumOfSquareNegSD_Type = Counter32
_Hh3cNqaStatJitterSumOfSquareNegSD_Object = MibTableColumn
hh3cNqaStatJitterSumOfSquareNegSD = _Hh3cNqaStatJitterSumOfSquareNegSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 11),
    _Hh3cNqaStatJitterSumOfSquareNegSD_Type()
)
hh3cNqaStatJitterSumOfSquareNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquareNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquareNegSD.setUnits("milliseconds")
_Hh3cNqaStatJitterMinOfPosDS_Type = Gauge32
_Hh3cNqaStatJitterMinOfPosDS_Object = MibTableColumn
hh3cNqaStatJitterMinOfPosDS = _Hh3cNqaStatJitterMinOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 12),
    _Hh3cNqaStatJitterMinOfPosDS_Type()
)
hh3cNqaStatJitterMinOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfPosDS.setUnits("milliseconds")
_Hh3cNqaStatJitterMaxOfPosDS_Type = Gauge32
_Hh3cNqaStatJitterMaxOfPosDS_Object = MibTableColumn
hh3cNqaStatJitterMaxOfPosDS = _Hh3cNqaStatJitterMaxOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 13),
    _Hh3cNqaStatJitterMaxOfPosDS_Type()
)
hh3cNqaStatJitterMaxOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfPosDS.setUnits("milliseconds")
_Hh3cNqaStatJitterNumOfPosDS_Type = Counter32
_Hh3cNqaStatJitterNumOfPosDS_Object = MibTableColumn
hh3cNqaStatJitterNumOfPosDS = _Hh3cNqaStatJitterNumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 14),
    _Hh3cNqaStatJitterNumOfPosDS_Type()
)
hh3cNqaStatJitterNumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterNumOfPosDS.setStatus("current")
_Hh3cNqaStatJitterSumOfPosDS_Type = Counter32
_Hh3cNqaStatJitterSumOfPosDS_Object = MibTableColumn
hh3cNqaStatJitterSumOfPosDS = _Hh3cNqaStatJitterSumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 15),
    _Hh3cNqaStatJitterSumOfPosDS_Type()
)
hh3cNqaStatJitterSumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfPosDS.setUnits("milliseconds")
_Hh3cNqaStatJitterSumOfSquarePosDS_Type = Counter32
_Hh3cNqaStatJitterSumOfSquarePosDS_Object = MibTableColumn
hh3cNqaStatJitterSumOfSquarePosDS = _Hh3cNqaStatJitterSumOfSquarePosDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 16),
    _Hh3cNqaStatJitterSumOfSquarePosDS_Type()
)
hh3cNqaStatJitterSumOfSquarePosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquarePosDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquarePosDS.setUnits("milliseconds")
_Hh3cNqaStatJitterMinOfNegDS_Type = Gauge32
_Hh3cNqaStatJitterMinOfNegDS_Object = MibTableColumn
hh3cNqaStatJitterMinOfNegDS = _Hh3cNqaStatJitterMinOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 17),
    _Hh3cNqaStatJitterMinOfNegDS_Type()
)
hh3cNqaStatJitterMinOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfNegDS.setUnits("milliseconds")
_Hh3cNqaStatJitterMaxOfNegDS_Type = Gauge32
_Hh3cNqaStatJitterMaxOfNegDS_Object = MibTableColumn
hh3cNqaStatJitterMaxOfNegDS = _Hh3cNqaStatJitterMaxOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 18),
    _Hh3cNqaStatJitterMaxOfNegDS_Type()
)
hh3cNqaStatJitterMaxOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfNegDS.setUnits("milliseconds")
_Hh3cNqaStatJitterNumOfNegDS_Type = Counter32
_Hh3cNqaStatJitterNumOfNegDS_Object = MibTableColumn
hh3cNqaStatJitterNumOfNegDS = _Hh3cNqaStatJitterNumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 19),
    _Hh3cNqaStatJitterNumOfNegDS_Type()
)
hh3cNqaStatJitterNumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterNumOfNegDS.setStatus("current")
_Hh3cNqaStatJitterSumOfNegDS_Type = Counter32
_Hh3cNqaStatJitterSumOfNegDS_Object = MibTableColumn
hh3cNqaStatJitterSumOfNegDS = _Hh3cNqaStatJitterSumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 20),
    _Hh3cNqaStatJitterSumOfNegDS_Type()
)
hh3cNqaStatJitterSumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfNegDS.setUnits("milliseconds")
_Hh3cNqaStatJitterSumOfSquareNegDS_Type = Counter32
_Hh3cNqaStatJitterSumOfSquareNegDS_Object = MibTableColumn
hh3cNqaStatJitterSumOfSquareNegDS = _Hh3cNqaStatJitterSumOfSquareNegDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 21),
    _Hh3cNqaStatJitterSumOfSquareNegDS_Type()
)
hh3cNqaStatJitterSumOfSquareNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquareNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterSumOfSquareNegDS.setUnits("milliseconds")
_Hh3cNqaStatJitterPacketLossSD_Type = Counter32
_Hh3cNqaStatJitterPacketLossSD_Object = MibTableColumn
hh3cNqaStatJitterPacketLossSD = _Hh3cNqaStatJitterPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 22),
    _Hh3cNqaStatJitterPacketLossSD_Type()
)
hh3cNqaStatJitterPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterPacketLossSD.setStatus("current")
_Hh3cNqaStatJitterPacketLossDS_Type = Counter32
_Hh3cNqaStatJitterPacketLossDS_Object = MibTableColumn
hh3cNqaStatJitterPacketLossDS = _Hh3cNqaStatJitterPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 23),
    _Hh3cNqaStatJitterPacketLossDS_Type()
)
hh3cNqaStatJitterPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterPacketLossDS.setStatus("current")
_Hh3cNqaStatJitterAvePosSD_Type = Gauge32
_Hh3cNqaStatJitterAvePosSD_Object = MibTableColumn
hh3cNqaStatJitterAvePosSD = _Hh3cNqaStatJitterAvePosSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 24),
    _Hh3cNqaStatJitterAvePosSD_Type()
)
hh3cNqaStatJitterAvePosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAvePosSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAvePosSD.setUnits("milliseconds")
_Hh3cNqaStatJitterAveNegSD_Type = Gauge32
_Hh3cNqaStatJitterAveNegSD_Object = MibTableColumn
hh3cNqaStatJitterAveNegSD = _Hh3cNqaStatJitterAveNegSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 25),
    _Hh3cNqaStatJitterAveNegSD_Type()
)
hh3cNqaStatJitterAveNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAveNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAveNegSD.setUnits("milliseconds")
_Hh3cNqaStatJitterAvePosDS_Type = Gauge32
_Hh3cNqaStatJitterAvePosDS_Object = MibTableColumn
hh3cNqaStatJitterAvePosDS = _Hh3cNqaStatJitterAvePosDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 26),
    _Hh3cNqaStatJitterAvePosDS_Type()
)
hh3cNqaStatJitterAvePosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAvePosDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAvePosDS.setUnits("milliseconds")
_Hh3cNqaStatJitterAveNegDS_Type = Gauge32
_Hh3cNqaStatJitterAveNegDS_Object = MibTableColumn
hh3cNqaStatJitterAveNegDS = _Hh3cNqaStatJitterAveNegDS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 27),
    _Hh3cNqaStatJitterAveNegDS_Type()
)
hh3cNqaStatJitterAveNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAveNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterAveNegDS.setUnits("milliseconds")
_Hh3cNqaStatJitterPktLossUnknown_Type = Counter32
_Hh3cNqaStatJitterPktLossUnknown_Object = MibTableColumn
hh3cNqaStatJitterPktLossUnknown = _Hh3cNqaStatJitterPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 28),
    _Hh3cNqaStatJitterPktLossUnknown_Type()
)
hh3cNqaStatJitterPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterPktLossUnknown.setStatus("current")
_Hh3cNqaStatJitterMaxOfICPIF_Type = Gauge32
_Hh3cNqaStatJitterMaxOfICPIF_Object = MibTableColumn
hh3cNqaStatJitterMaxOfICPIF = _Hh3cNqaStatJitterMaxOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 29),
    _Hh3cNqaStatJitterMaxOfICPIF_Type()
)
hh3cNqaStatJitterMaxOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfICPIF.setStatus("current")
_Hh3cNqaStatJitterMinOfICPIF_Type = Gauge32
_Hh3cNqaStatJitterMinOfICPIF_Object = MibTableColumn
hh3cNqaStatJitterMinOfICPIF = _Hh3cNqaStatJitterMinOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 30),
    _Hh3cNqaStatJitterMinOfICPIF_Type()
)
hh3cNqaStatJitterMinOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfICPIF.setStatus("current")
_Hh3cNqaStatJitterMaxOfMOS_Type = Gauge32
_Hh3cNqaStatJitterMaxOfMOS_Object = MibTableColumn
hh3cNqaStatJitterMaxOfMOS = _Hh3cNqaStatJitterMaxOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 31),
    _Hh3cNqaStatJitterMaxOfMOS_Type()
)
hh3cNqaStatJitterMaxOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMaxOfMOS.setStatus("current")
_Hh3cNqaStatJitterMinOfMOS_Type = Gauge32
_Hh3cNqaStatJitterMinOfMOS_Object = MibTableColumn
hh3cNqaStatJitterMinOfMOS = _Hh3cNqaStatJitterMinOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 12, 1, 32),
    _Hh3cNqaStatJitterMinOfMOS_Type()
)
hh3cNqaStatJitterMinOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatJitterMinOfMOS.setStatus("current")
_Hh3cNqaReactionTable_Object = MibTable
hh3cNqaReactionTable = _Hh3cNqaReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13)
)
if mibBuilder.loadTexts:
    hh3cNqaReactionTable.setStatus("current")
_Hh3cNqaReactionEntry_Object = MibTableRow
hh3cNqaReactionEntry = _Hh3cNqaReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1)
)
hh3cNqaReactionEntry.setIndexNames(
    (0, "HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
    (0, "HH3C-NQA-MIB", "hh3cNqaReactTestName"),
    (0, "HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
)
if mibBuilder.loadTexts:
    hh3cNqaReactionEntry.setStatus("current")


class _Hh3cNqaReactOwnerIndex_Type(SnmpAdminString):
    """Custom type hh3cNqaReactOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cNqaReactOwnerIndex_Type.__name__ = "SnmpAdminString"
_Hh3cNqaReactOwnerIndex_Object = MibTableColumn
hh3cNqaReactOwnerIndex = _Hh3cNqaReactOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 1),
    _Hh3cNqaReactOwnerIndex_Type()
)
hh3cNqaReactOwnerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNqaReactOwnerIndex.setStatus("current")


class _Hh3cNqaReactTestName_Type(SnmpAdminString):
    """Custom type hh3cNqaReactTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cNqaReactTestName_Type.__name__ = "SnmpAdminString"
_Hh3cNqaReactTestName_Object = MibTableColumn
hh3cNqaReactTestName = _Hh3cNqaReactTestName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 2),
    _Hh3cNqaReactTestName_Type()
)
hh3cNqaReactTestName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNqaReactTestName.setStatus("current")


class _Hh3cNqaReactItemIndex_Type(Unsigned32):
    """Custom type hh3cNqaReactItemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cNqaReactItemIndex_Type.__name__ = "Unsigned32"
_Hh3cNqaReactItemIndex_Object = MibTableColumn
hh3cNqaReactItemIndex = _Hh3cNqaReactItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 3),
    _Hh3cNqaReactItemIndex_Type()
)
hh3cNqaReactItemIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNqaReactItemIndex.setStatus("current")


class _Hh3cNqaReactCheckedElement_Type(Integer32):
    """Custom type hh3cNqaReactCheckedElement based on Integer32"""
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


_Hh3cNqaReactCheckedElement_Type.__name__ = "Integer32"
_Hh3cNqaReactCheckedElement_Object = MibTableColumn
hh3cNqaReactCheckedElement = _Hh3cNqaReactCheckedElement_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 4),
    _Hh3cNqaReactCheckedElement_Type()
)
hh3cNqaReactCheckedElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactCheckedElement.setStatus("current")


class _Hh3cNqaReactThresholdUpperLimit_Type(Unsigned32):
    """Custom type hh3cNqaReactThresholdUpperLimit based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaReactThresholdUpperLimit_Object = MibTableColumn
hh3cNqaReactThresholdUpperLimit = _Hh3cNqaReactThresholdUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 5),
    _Hh3cNqaReactThresholdUpperLimit_Type()
)
hh3cNqaReactThresholdUpperLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactThresholdUpperLimit.setStatus("current")


class _Hh3cNqaReactThresholdLowerLimit_Type(Unsigned32):
    """Custom type hh3cNqaReactThresholdLowerLimit based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaReactThresholdLowerLimit_Object = MibTableColumn
hh3cNqaReactThresholdLowerLimit = _Hh3cNqaReactThresholdLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 6),
    _Hh3cNqaReactThresholdLowerLimit_Type()
)
hh3cNqaReactThresholdLowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactThresholdLowerLimit.setStatus("current")


class _Hh3cNqaReactThresholdType_Type(Integer32):
    """Custom type hh3cNqaReactThresholdType based on Integer32"""
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


_Hh3cNqaReactThresholdType_Type.__name__ = "Integer32"
_Hh3cNqaReactThresholdType_Object = MibTableColumn
hh3cNqaReactThresholdType = _Hh3cNqaReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 7),
    _Hh3cNqaReactThresholdType_Type()
)
hh3cNqaReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactThresholdType.setStatus("current")


class _Hh3cNqaReactThresholdConsecNum_Type(Unsigned32):
    """Custom type hh3cNqaReactThresholdConsecNum based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaReactThresholdConsecNum_Object = MibTableColumn
hh3cNqaReactThresholdConsecNum = _Hh3cNqaReactThresholdConsecNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 8),
    _Hh3cNqaReactThresholdConsecNum_Type()
)
hh3cNqaReactThresholdConsecNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactThresholdConsecNum.setStatus("current")


class _Hh3cNqaReactThresholdAccumNum_Type(Unsigned32):
    """Custom type hh3cNqaReactThresholdAccumNum based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaReactThresholdAccumNum_Object = MibTableColumn
hh3cNqaReactThresholdAccumNum = _Hh3cNqaReactThresholdAccumNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 9),
    _Hh3cNqaReactThresholdAccumNum_Type()
)
hh3cNqaReactThresholdAccumNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactThresholdAccumNum.setStatus("current")


class _Hh3cNqaReactActionType_Type(Integer32):
    """Custom type hh3cNqaReactActionType based on Integer32"""
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


_Hh3cNqaReactActionType_Type.__name__ = "Integer32"
_Hh3cNqaReactActionType_Object = MibTableColumn
hh3cNqaReactActionType = _Hh3cNqaReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 10),
    _Hh3cNqaReactActionType_Type()
)
hh3cNqaReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactActionType.setStatus("current")


class _Hh3cNqaReactCurrentStatus_Type(Integer32):
    """Custom type hh3cNqaReactCurrentStatus based on Integer32"""
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


_Hh3cNqaReactCurrentStatus_Type.__name__ = "Integer32"
_Hh3cNqaReactCurrentStatus_Object = MibTableColumn
hh3cNqaReactCurrentStatus = _Hh3cNqaReactCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 11),
    _Hh3cNqaReactCurrentStatus_Type()
)
hh3cNqaReactCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaReactCurrentStatus.setStatus("current")
_Hh3cNqaReactRowStatus_Type = RowStatus
_Hh3cNqaReactRowStatus_Object = MibTableColumn
hh3cNqaReactRowStatus = _Hh3cNqaReactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 12),
    _Hh3cNqaReactRowStatus_Type()
)
hh3cNqaReactRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNqaReactRowStatus.setStatus("current")


class _Hh3cNqaReactCheckedNum_Type(Unsigned32):
    """Custom type hh3cNqaReactCheckedNum based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaReactCheckedNum_Object = MibTableColumn
hh3cNqaReactCheckedNum = _Hh3cNqaReactCheckedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 13),
    _Hh3cNqaReactCheckedNum_Type()
)
hh3cNqaReactCheckedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaReactCheckedNum.setStatus("current")


class _Hh3cNqaReactThresholdNum_Type(Unsigned32):
    """Custom type hh3cNqaReactThresholdNum based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaReactThresholdNum_Object = MibTableColumn
hh3cNqaReactThresholdNum = _Hh3cNqaReactThresholdNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 13, 1, 14),
    _Hh3cNqaReactThresholdNum_Type()
)
hh3cNqaReactThresholdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaReactThresholdNum.setStatus("current")
_Hh3cNqaStatisticsReactionTable_Object = MibTable
hh3cNqaStatisticsReactionTable = _Hh3cNqaStatisticsReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14)
)
if mibBuilder.loadTexts:
    hh3cNqaStatisticsReactionTable.setStatus("current")
_Hh3cNqaStatisticsReactionEntry_Object = MibTableRow
hh3cNqaStatisticsReactionEntry = _Hh3cNqaStatisticsReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14, 1)
)
hh3cNqaStatisticsReactionEntry.setIndexNames(
    (0, "HH3C-NQA-MIB", "hh3cNqaStatReactOwnerIndex"),
    (0, "HH3C-NQA-MIB", "hh3cNqaStatReactTestName"),
    (0, "HH3C-NQA-MIB", "hh3cNqaStatReactIndex"),
    (0, "HH3C-NQA-MIB", "hh3cNqaStatReactItemIndex"),
)
if mibBuilder.loadTexts:
    hh3cNqaStatisticsReactionEntry.setStatus("current")


class _Hh3cNqaStatReactOwnerIndex_Type(SnmpAdminString):
    """Custom type hh3cNqaStatReactOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cNqaStatReactOwnerIndex_Type.__name__ = "SnmpAdminString"
_Hh3cNqaStatReactOwnerIndex_Object = MibTableColumn
hh3cNqaStatReactOwnerIndex = _Hh3cNqaStatReactOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14, 1, 1),
    _Hh3cNqaStatReactOwnerIndex_Type()
)
hh3cNqaStatReactOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaStatReactOwnerIndex.setStatus("current")


class _Hh3cNqaStatReactTestName_Type(SnmpAdminString):
    """Custom type hh3cNqaStatReactTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cNqaStatReactTestName_Type.__name__ = "SnmpAdminString"
_Hh3cNqaStatReactTestName_Object = MibTableColumn
hh3cNqaStatReactTestName = _Hh3cNqaStatReactTestName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14, 1, 2),
    _Hh3cNqaStatReactTestName_Type()
)
hh3cNqaStatReactTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaStatReactTestName.setStatus("current")


class _Hh3cNqaStatReactIndex_Type(Unsigned32):
    """Custom type hh3cNqaStatReactIndex based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaStatReactIndex_Object = MibTableColumn
hh3cNqaStatReactIndex = _Hh3cNqaStatReactIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14, 1, 3),
    _Hh3cNqaStatReactIndex_Type()
)
hh3cNqaStatReactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaStatReactIndex.setStatus("current")


class _Hh3cNqaStatReactItemIndex_Type(Unsigned32):
    """Custom type hh3cNqaStatReactItemIndex based on Unsigned32"""
    defaultValue = 0


_Hh3cNqaStatReactItemIndex_Object = MibTableColumn
hh3cNqaStatReactItemIndex = _Hh3cNqaStatReactItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14, 1, 4),
    _Hh3cNqaStatReactItemIndex_Type()
)
hh3cNqaStatReactItemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNqaStatReactItemIndex.setStatus("current")


class _Hh3cNqaStatReactCheckedNum_Type(Counter32):
    """Custom type hh3cNqaStatReactCheckedNum based on Counter32"""
    defaultValue = 0


_Hh3cNqaStatReactCheckedNum_Object = MibTableColumn
hh3cNqaStatReactCheckedNum = _Hh3cNqaStatReactCheckedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14, 1, 5),
    _Hh3cNqaStatReactCheckedNum_Type()
)
hh3cNqaStatReactCheckedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatReactCheckedNum.setStatus("current")


class _Hh3cNqaStatReactThresholdNum_Type(Counter32):
    """Custom type hh3cNqaStatReactThresholdNum based on Counter32"""
    defaultValue = 0


_Hh3cNqaStatReactThresholdNum_Object = MibTableColumn
hh3cNqaStatReactThresholdNum = _Hh3cNqaStatReactThresholdNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 1, 14, 1, 6),
    _Hh3cNqaStatReactThresholdNum_Type()
)
hh3cNqaStatReactThresholdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNqaStatReactThresholdNum.setStatus("current")
_Hh3cNqaImplementationTypeDomains_ObjectIdentity = ObjectIdentity
hh3cNqaImplementationTypeDomains = _Hh3cNqaImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2)
)
_Hh3cNqaUdpEcho_ObjectIdentity = ObjectIdentity
hh3cNqaUdpEcho = _Hh3cNqaUdpEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cNqaUdpEcho.setStatus("current")
_Hh3cNqaTcpconnect_ObjectIdentity = ObjectIdentity
hh3cNqaTcpconnect = _Hh3cNqaTcpconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cNqaTcpconnect.setStatus("current")
_Hh3cNqajitter_ObjectIdentity = ObjectIdentity
hh3cNqajitter = _Hh3cNqajitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cNqajitter.setStatus("current")
_Hh3cNqaHttp_ObjectIdentity = ObjectIdentity
hh3cNqaHttp = _Hh3cNqaHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cNqaHttp.setStatus("current")
_Hh3cNqadlsw_ObjectIdentity = ObjectIdentity
hh3cNqadlsw = _Hh3cNqadlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cNqadlsw.setStatus("current")
_Hh3cNqadhcp_ObjectIdentity = ObjectIdentity
hh3cNqadhcp = _Hh3cNqadhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cNqadhcp.setStatus("current")
_Hh3cNqaftp_ObjectIdentity = ObjectIdentity
hh3cNqaftp = _Hh3cNqaftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cNqaftp.setStatus("current")
_Hh3cNqaNotifications_ObjectIdentity = ObjectIdentity
hh3cNqaNotifications = _Hh3cNqaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3)
)
pingCtlEntry.registerAugmentions(
    ("HH3C-NQA-MIB",
     "hh3cNqaCtlEntry")
)
hh3cNqaCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions(
    ("HH3C-NQA-MIB",
     "hh3cNqaStatisticsCtlEntry")
)
hh3cNqaStatisticsCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hh3cNqaProbeTimeOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 1)
)
hh3cNqaProbeTimeOverThreshold.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactThresholdType"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaProbeTimeOverThreshold.setStatus(
        "current"
    )

hh3cNqaJitterRTTOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 2)
)
hh3cNqaJitterRTTOverThreshold.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactThresholdType"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaJitterRTTOverThreshold.setStatus(
        "current"
    )

hh3cNqaProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 3)
)
hh3cNqaProbeFailure.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactThresholdType"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaProbeFailure.setStatus(
        "current"
    )

hh3cNqaJitterPacketLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 4)
)
hh3cNqaJitterPacketLoss.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactThresholdType"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaJitterPacketLoss.setStatus(
        "current"
    )

hh3cNqaJitterSDOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 5)
)
hh3cNqaJitterSDOverThreshold.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactThresholdType"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaJitterSDOverThreshold.setStatus(
        "current"
    )

hh3cNqaJitterDSOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 6)
)
hh3cNqaJitterDSOverThreshold.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactThresholdType"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaJitterDSOverThreshold.setStatus(
        "current"
    )

hh3cNqaICPIFOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 7)
)
hh3cNqaICPIFOverThreshold.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaICPIFOverThreshold.setStatus(
        "current"
    )

hh3cNqaMOSOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3, 3, 8)
)
hh3cNqaMOSOverThreshold.setObjects(
      *(("HH3C-NQA-MIB", "hh3cNqaReactOwnerIndex"),
        ("HH3C-NQA-MIB", "hh3cNqaReactTestName"),
        ("HH3C-NQA-MIB", "hh3cNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("HH3C-NQA-MIB", "hh3cNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hh3cNqaMOSOverThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NQA-MIB",
    **{"hh3cNqa": hh3cNqa,
       "hh3cNqaObjects": hh3cNqaObjects,
       "hh3cNqaMIBVersion": hh3cNqaMIBVersion,
       "hh3cNqaCtlTable": hh3cNqaCtlTable,
       "hh3cNqaCtlEntry": hh3cNqaCtlEntry,
       "hh3cNqaCtlTargetPort": hh3cNqaCtlTargetPort,
       "hh3cNqaCtlSourcePort": hh3cNqaCtlSourcePort,
       "hh3cNqaCtlTTL": hh3cNqaCtlTTL,
       "hh3cNqaCtlJitterAdminInterval": hh3cNqaCtlJitterAdminInterval,
       "hh3cNqaCtlJitterAdminNumPackets": hh3cNqaCtlJitterAdminNumPackets,
       "hh3cNqaCtlHttpOperationType": hh3cNqaCtlHttpOperationType,
       "hh3cNqaCtlHttpOperationString": hh3cNqaCtlHttpOperationString,
       "hh3cNqaCtlFtpOperationType": hh3cNqaCtlFtpOperationType,
       "hh3cNqaCtlFtpUsername": hh3cNqaCtlFtpUsername,
       "hh3cNqaCtlFtpPassword": hh3cNqaCtlFtpPassword,
       "hh3cNqaCtlFtpOperationString": hh3cNqaCtlFtpOperationString,
       "hh3cNqaCtlVPNInstance": hh3cNqaCtlVPNInstance,
       "hh3cNqaCtlHistoryKeptTime": hh3cNqaCtlHistoryKeptTime,
       "hh3cNqaCtlHistoryEnable": hh3cNqaCtlHistoryEnable,
       "hh3cNqaCtlICPIFAdvFactor": hh3cNqaCtlICPIFAdvFactor,
       "hh3cNqaCtlCodecType": hh3cNqaCtlCodecType,
       "hh3cNqaResultsTable": hh3cNqaResultsTable,
       "hh3cNqaResultsEntry": hh3cNqaResultsEntry,
       "hh3cNqaResultsRttNumDisconnects": hh3cNqaResultsRttNumDisconnects,
       "hh3cNqaResultsRttTimeouts": hh3cNqaResultsRttTimeouts,
       "hh3cNqaResultsRttBusies": hh3cNqaResultsRttBusies,
       "hh3cNqaResultsRttNoConnections": hh3cNqaResultsRttNoConnections,
       "hh3cNqaResultsRttDrops": hh3cNqaResultsRttDrops,
       "hh3cNqaResultsRttSequenceErrors": hh3cNqaResultsRttSequenceErrors,
       "hh3cNqaResultsRttStatsErrors": hh3cNqaResultsRttStatsErrors,
       "hh3cNqaResultsMaxDelaySD": hh3cNqaResultsMaxDelaySD,
       "hh3cNqaResultsMaxDelayDS": hh3cNqaResultsMaxDelayDS,
       "hh3cNqaResultsLostPacketRatio": hh3cNqaResultsLostPacketRatio,
       "hh3cNqaResultsPacketLateArrival": hh3cNqaResultsPacketLateArrival,
       "hh3cNqaResultsRttSum": hh3cNqaResultsRttSum,
       "hh3cNqaResultsNumOfDelaySD": hh3cNqaResultsNumOfDelaySD,
       "hh3cNqaResultsMinDelaySD": hh3cNqaResultsMinDelaySD,
       "hh3cNqaResultsSumDelaySD": hh3cNqaResultsSumDelaySD,
       "hh3cNqaResultsSum2DelaySD": hh3cNqaResultsSum2DelaySD,
       "hh3cNqaResultsNumOfDelayDS": hh3cNqaResultsNumOfDelayDS,
       "hh3cNqaResultsMinDelayDS": hh3cNqaResultsMinDelayDS,
       "hh3cNqaResultsSumDelayDS": hh3cNqaResultsSumDelayDS,
       "hh3cNqaResultsSum2DelayDS": hh3cNqaResultsSum2DelayDS,
       "hh3cNqaJitterStatsTable": hh3cNqaJitterStatsTable,
       "hh3cNqaJitterStatsEntry": hh3cNqaJitterStatsEntry,
       "hh3cNqaJitterStatsNumOfRTT": hh3cNqaJitterStatsNumOfRTT,
       "hh3cNqaJitterStatsMinOfPositivesSD": hh3cNqaJitterStatsMinOfPositivesSD,
       "hh3cNqaJitterStatsMaxOfPositivesSD": hh3cNqaJitterStatsMaxOfPositivesSD,
       "hh3cNqaJitterStatsNumOfPositivesSD": hh3cNqaJitterStatsNumOfPositivesSD,
       "hh3cNqaJitterStatsSumOfPositivesSD": hh3cNqaJitterStatsSumOfPositivesSD,
       "hh3cNqaJitterStatsSum2PositivesSD": hh3cNqaJitterStatsSum2PositivesSD,
       "hh3cNqaJitterStatsMinOfNegativesSD": hh3cNqaJitterStatsMinOfNegativesSD,
       "hh3cNqaJitterStatsMaxOfNegativesSD": hh3cNqaJitterStatsMaxOfNegativesSD,
       "hh3cNqaJitterStatsNumOfNegativesSD": hh3cNqaJitterStatsNumOfNegativesSD,
       "hh3cNqaJitterStatsSumOfNegativesSD": hh3cNqaJitterStatsSumOfNegativesSD,
       "hh3cNqaJitterStatsSum2NegativesSD": hh3cNqaJitterStatsSum2NegativesSD,
       "hh3cNqaJitterStatsMinOfPositivesDS": hh3cNqaJitterStatsMinOfPositivesDS,
       "hh3cNqaJitterStatsMaxOfPositivesDS": hh3cNqaJitterStatsMaxOfPositivesDS,
       "hh3cNqaJitterStatsNumOfPositivesDS": hh3cNqaJitterStatsNumOfPositivesDS,
       "hh3cNqaJitterStatsSumOfPositivesDS": hh3cNqaJitterStatsSumOfPositivesDS,
       "hh3cNqaJitterStatsSum2PositivesDS": hh3cNqaJitterStatsSum2PositivesDS,
       "hh3cNqaJitterStatsMinOfNegativesDS": hh3cNqaJitterStatsMinOfNegativesDS,
       "hh3cNqaJitterStatsMaxOfNegativesDS": hh3cNqaJitterStatsMaxOfNegativesDS,
       "hh3cNqaJitterStatsNumOfNegativesDS": hh3cNqaJitterStatsNumOfNegativesDS,
       "hh3cNqaJitterStatsSumOfNegativesDS": hh3cNqaJitterStatsSumOfNegativesDS,
       "hh3cNqaJitterStatsSum2NegativesDS": hh3cNqaJitterStatsSum2NegativesDS,
       "hh3cNqaJitterStatsPacketLossSD": hh3cNqaJitterStatsPacketLossSD,
       "hh3cNqaJitterStatsPacketLossDS": hh3cNqaJitterStatsPacketLossDS,
       "hh3cNqaJitterStatsAvePositivesSD": hh3cNqaJitterStatsAvePositivesSD,
       "hh3cNqaJitterStatsAveNegativesSD": hh3cNqaJitterStatsAveNegativesSD,
       "hh3cNqaJitterStatsAvePositivesDS": hh3cNqaJitterStatsAvePositivesDS,
       "hh3cNqaJitterStatsAveNegativesDS": hh3cNqaJitterStatsAveNegativesDS,
       "hh3cNqaJitterStatsPktLossUnknown": hh3cNqaJitterStatsPktLossUnknown,
       "hh3cNqaJitterStatsOperOfICPIF": hh3cNqaJitterStatsOperOfICPIF,
       "hh3cNqaJitterStatsOperOfMOS": hh3cNqaJitterStatsOperOfMOS,
       "hh3cNqaAgentEnable": hh3cNqaAgentEnable,
       "hh3cNqaTcpServerTable": hh3cNqaTcpServerTable,
       "hh3cNqaTcpServerEntry": hh3cNqaTcpServerEntry,
       "hh3cNqaTcpServerIpAddress": hh3cNqaTcpServerIpAddress,
       "hh3cNqaTcpServerPort": hh3cNqaTcpServerPort,
       "hh3cNqaTcpServerRowStatus": hh3cNqaTcpServerRowStatus,
       "hh3cNqaUdpServerTable": hh3cNqaUdpServerTable,
       "hh3cNqaUdpServerEntry": hh3cNqaUdpServerEntry,
       "hh3cNqaUdpServerIpAddress": hh3cNqaUdpServerIpAddress,
       "hh3cNqaUdpServerPort": hh3cNqaUdpServerPort,
       "hh3cNqaUdpServerRowStatus": hh3cNqaUdpServerRowStatus,
       "hh3cNqaServerEnable": hh3cNqaServerEnable,
       "hh3cNqaStatsMaxGroupNumber": hh3cNqaStatsMaxGroupNumber,
       "hh3cNqaStatisticsCtlTable": hh3cNqaStatisticsCtlTable,
       "hh3cNqaStatisticsCtlEntry": hh3cNqaStatisticsCtlEntry,
       "hh3cNqaCtlStatisticsInterval": hh3cNqaCtlStatisticsInterval,
       "hh3cNqaCtlStatisticsGroupNumber": hh3cNqaCtlStatisticsGroupNumber,
       "hh3cNqaCtlStatisticsKeptTime": hh3cNqaCtlStatisticsKeptTime,
       "hh3cNqaCtlBeginTime": hh3cNqaCtlBeginTime,
       "hh3cNqaCtlLifeTime": hh3cNqaCtlLifeTime,
       "hh3cNqaStatisticsResultsTable": hh3cNqaStatisticsResultsTable,
       "hh3cNqaStatisticsResultsEntry": hh3cNqaStatisticsResultsEntry,
       "hh3cNqaStatResIndex": hh3cNqaStatResIndex,
       "hh3cNqaStatResIpTargetAddressType": hh3cNqaStatResIpTargetAddressType,
       "hh3cNqaStatResIpTargetAddress": hh3cNqaStatResIpTargetAddress,
       "hh3cNqaStatResMinRtt": hh3cNqaStatResMinRtt,
       "hh3cNqaStatResMaxRtt": hh3cNqaStatResMaxRtt,
       "hh3cNqaStatResAverageRtt": hh3cNqaStatResAverageRtt,
       "hh3cNqaStatResProbeResponses": hh3cNqaStatResProbeResponses,
       "hh3cNqaStatResSentProbes": hh3cNqaStatResSentProbes,
       "hh3cNqaStatResRttSumOfSquares": hh3cNqaStatResRttSumOfSquares,
       "hh3cNqaStatResStartTime": hh3cNqaStatResStartTime,
       "hh3cNqaStatResInterval": hh3cNqaStatResInterval,
       "hh3cNqaStatResRttNumDisconnects": hh3cNqaStatResRttNumDisconnects,
       "hh3cNqaStatResRttTimeouts": hh3cNqaStatResRttTimeouts,
       "hh3cNqaStatResRttBusies": hh3cNqaStatResRttBusies,
       "hh3cNqaStatResRttNoConnections": hh3cNqaStatResRttNoConnections,
       "hh3cNqaStatResRttDrops": hh3cNqaStatResRttDrops,
       "hh3cNqaStatResRttSequenceErrors": hh3cNqaStatResRttSequenceErrors,
       "hh3cNqaStatResRttErrors": hh3cNqaStatResRttErrors,
       "hh3cNqaStatResLostPacketRatio": hh3cNqaStatResLostPacketRatio,
       "hh3cNqaStatResPacketLateArrival": hh3cNqaStatResPacketLateArrival,
       "hh3cNqaStatResRttSum": hh3cNqaStatResRttSum,
       "hh3cNqaStatResNumOfDelaySD": hh3cNqaStatResNumOfDelaySD,
       "hh3cNqaStatResMinDelaySD": hh3cNqaStatResMinDelaySD,
       "hh3cNqaStatResMaxDelaySD": hh3cNqaStatResMaxDelaySD,
       "hh3cNqaStatResSumDelaySD": hh3cNqaStatResSumDelaySD,
       "hh3cNqaStatResSum2DelaySD": hh3cNqaStatResSum2DelaySD,
       "hh3cNqaStatResNumOfDelayDS": hh3cNqaStatResNumOfDelayDS,
       "hh3cNqaStatResMinDelayDS": hh3cNqaStatResMinDelayDS,
       "hh3cNqaStatResMaxDelayDS": hh3cNqaStatResMaxDelayDS,
       "hh3cNqaStatResSumDelayDS": hh3cNqaStatResSumDelayDS,
       "hh3cNqaStatResSum2DelayDS": hh3cNqaStatResSum2DelayDS,
       "hh3cNqaGroupStatsJitterTable": hh3cNqaGroupStatsJitterTable,
       "hh3cNqaGroupStatsJitterEntry": hh3cNqaGroupStatsJitterEntry,
       "hh3cNqaStatJitterIndex": hh3cNqaStatJitterIndex,
       "hh3cNqaStatJitterMinOfPosSD": hh3cNqaStatJitterMinOfPosSD,
       "hh3cNqaStatJitterMaxOfPosSD": hh3cNqaStatJitterMaxOfPosSD,
       "hh3cNqaStatJitterNumOfPosSD": hh3cNqaStatJitterNumOfPosSD,
       "hh3cNqaStatJitterSumOfPosSD": hh3cNqaStatJitterSumOfPosSD,
       "hh3cNqaStatJitterSumOfSquarePosSD": hh3cNqaStatJitterSumOfSquarePosSD,
       "hh3cNqaStatJitterMinOfNegSD": hh3cNqaStatJitterMinOfNegSD,
       "hh3cNqaStatJitterMaxOfNegSD": hh3cNqaStatJitterMaxOfNegSD,
       "hh3cNqaStatJitterNumOfNegSD": hh3cNqaStatJitterNumOfNegSD,
       "hh3cNqaStatJitterSumOfNegSD": hh3cNqaStatJitterSumOfNegSD,
       "hh3cNqaStatJitterSumOfSquareNegSD": hh3cNqaStatJitterSumOfSquareNegSD,
       "hh3cNqaStatJitterMinOfPosDS": hh3cNqaStatJitterMinOfPosDS,
       "hh3cNqaStatJitterMaxOfPosDS": hh3cNqaStatJitterMaxOfPosDS,
       "hh3cNqaStatJitterNumOfPosDS": hh3cNqaStatJitterNumOfPosDS,
       "hh3cNqaStatJitterSumOfPosDS": hh3cNqaStatJitterSumOfPosDS,
       "hh3cNqaStatJitterSumOfSquarePosDS": hh3cNqaStatJitterSumOfSquarePosDS,
       "hh3cNqaStatJitterMinOfNegDS": hh3cNqaStatJitterMinOfNegDS,
       "hh3cNqaStatJitterMaxOfNegDS": hh3cNqaStatJitterMaxOfNegDS,
       "hh3cNqaStatJitterNumOfNegDS": hh3cNqaStatJitterNumOfNegDS,
       "hh3cNqaStatJitterSumOfNegDS": hh3cNqaStatJitterSumOfNegDS,
       "hh3cNqaStatJitterSumOfSquareNegDS": hh3cNqaStatJitterSumOfSquareNegDS,
       "hh3cNqaStatJitterPacketLossSD": hh3cNqaStatJitterPacketLossSD,
       "hh3cNqaStatJitterPacketLossDS": hh3cNqaStatJitterPacketLossDS,
       "hh3cNqaStatJitterAvePosSD": hh3cNqaStatJitterAvePosSD,
       "hh3cNqaStatJitterAveNegSD": hh3cNqaStatJitterAveNegSD,
       "hh3cNqaStatJitterAvePosDS": hh3cNqaStatJitterAvePosDS,
       "hh3cNqaStatJitterAveNegDS": hh3cNqaStatJitterAveNegDS,
       "hh3cNqaStatJitterPktLossUnknown": hh3cNqaStatJitterPktLossUnknown,
       "hh3cNqaStatJitterMaxOfICPIF": hh3cNqaStatJitterMaxOfICPIF,
       "hh3cNqaStatJitterMinOfICPIF": hh3cNqaStatJitterMinOfICPIF,
       "hh3cNqaStatJitterMaxOfMOS": hh3cNqaStatJitterMaxOfMOS,
       "hh3cNqaStatJitterMinOfMOS": hh3cNqaStatJitterMinOfMOS,
       "hh3cNqaReactionTable": hh3cNqaReactionTable,
       "hh3cNqaReactionEntry": hh3cNqaReactionEntry,
       "hh3cNqaReactOwnerIndex": hh3cNqaReactOwnerIndex,
       "hh3cNqaReactTestName": hh3cNqaReactTestName,
       "hh3cNqaReactItemIndex": hh3cNqaReactItemIndex,
       "hh3cNqaReactCheckedElement": hh3cNqaReactCheckedElement,
       "hh3cNqaReactThresholdUpperLimit": hh3cNqaReactThresholdUpperLimit,
       "hh3cNqaReactThresholdLowerLimit": hh3cNqaReactThresholdLowerLimit,
       "hh3cNqaReactThresholdType": hh3cNqaReactThresholdType,
       "hh3cNqaReactThresholdConsecNum": hh3cNqaReactThresholdConsecNum,
       "hh3cNqaReactThresholdAccumNum": hh3cNqaReactThresholdAccumNum,
       "hh3cNqaReactActionType": hh3cNqaReactActionType,
       "hh3cNqaReactCurrentStatus": hh3cNqaReactCurrentStatus,
       "hh3cNqaReactRowStatus": hh3cNqaReactRowStatus,
       "hh3cNqaReactCheckedNum": hh3cNqaReactCheckedNum,
       "hh3cNqaReactThresholdNum": hh3cNqaReactThresholdNum,
       "hh3cNqaStatisticsReactionTable": hh3cNqaStatisticsReactionTable,
       "hh3cNqaStatisticsReactionEntry": hh3cNqaStatisticsReactionEntry,
       "hh3cNqaStatReactOwnerIndex": hh3cNqaStatReactOwnerIndex,
       "hh3cNqaStatReactTestName": hh3cNqaStatReactTestName,
       "hh3cNqaStatReactIndex": hh3cNqaStatReactIndex,
       "hh3cNqaStatReactItemIndex": hh3cNqaStatReactItemIndex,
       "hh3cNqaStatReactCheckedNum": hh3cNqaStatReactCheckedNum,
       "hh3cNqaStatReactThresholdNum": hh3cNqaStatReactThresholdNum,
       "hh3cNqaImplementationTypeDomains": hh3cNqaImplementationTypeDomains,
       "hh3cNqaUdpEcho": hh3cNqaUdpEcho,
       "hh3cNqaTcpconnect": hh3cNqaTcpconnect,
       "hh3cNqajitter": hh3cNqajitter,
       "hh3cNqaHttp": hh3cNqaHttp,
       "hh3cNqadlsw": hh3cNqadlsw,
       "hh3cNqadhcp": hh3cNqadhcp,
       "hh3cNqaftp": hh3cNqaftp,
       "hh3cNqaNotifications": hh3cNqaNotifications,
       "hh3cNqaProbeTimeOverThreshold": hh3cNqaProbeTimeOverThreshold,
       "hh3cNqaJitterRTTOverThreshold": hh3cNqaJitterRTTOverThreshold,
       "hh3cNqaProbeFailure": hh3cNqaProbeFailure,
       "hh3cNqaJitterPacketLoss": hh3cNqaJitterPacketLoss,
       "hh3cNqaJitterSDOverThreshold": hh3cNqaJitterSDOverThreshold,
       "hh3cNqaJitterDSOverThreshold": hh3cNqaJitterDSOverThreshold,
       "hh3cNqaICPIFOverThreshold": hh3cNqaICPIFOverThreshold,
       "hh3cNqaMOSOverThreshold": hh3cNqaMOSOverThreshold}
)
