# SNMP MIB module (ELTEX-MES-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-COPY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:33 2024
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

(eltMesCopy,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesCopy")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(RlCopyLocationType,) = mibBuilder.importSymbols(
    "RADLAN-COPY-MIB",
    "RlCopyLocationType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EltCopyUserBackupStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starting", 1),
          ("stopped", 2))
    )



# MIB Managed Objects in the order of their OIDs



class _EltCopyAutoBackupEnable_Type(TruthValue):
    """Custom type eltCopyAutoBackupEnable based on TruthValue"""


_EltCopyAutoBackupEnable_Object = MibScalar
eltCopyAutoBackupEnable = _EltCopyAutoBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 1),
    _EltCopyAutoBackupEnable_Type()
)
eltCopyAutoBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyAutoBackupEnable.setStatus("current")
_EltCopyAutoBackupTimeout_Type = Unsigned32
_EltCopyAutoBackupTimeout_Object = MibScalar
eltCopyAutoBackupTimeout = _EltCopyAutoBackupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 2),
    _EltCopyAutoBackupTimeout_Type()
)
eltCopyAutoBackupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyAutoBackupTimeout.setStatus("current")
_EltCopyAutoBackupFilePath_Type = DisplayString
_EltCopyAutoBackupFilePath_Object = MibScalar
eltCopyAutoBackupFilePath = _EltCopyAutoBackupFilePath_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 3),
    _EltCopyAutoBackupFilePath_Type()
)
eltCopyAutoBackupFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyAutoBackupFilePath.setStatus("current")
_EltCopyAutoBackupServerAddress_Type = DisplayString
_EltCopyAutoBackupServerAddress_Object = MibScalar
eltCopyAutoBackupServerAddress = _EltCopyAutoBackupServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 4),
    _EltCopyAutoBackupServerAddress_Type()
)
eltCopyAutoBackupServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyAutoBackupServerAddress.setStatus("current")


class _EltCopyAutoBackupOnWrite_Type(TruthValue):
    """Custom type eltCopyAutoBackupOnWrite based on TruthValue"""


_EltCopyAutoBackupOnWrite_Object = MibScalar
eltCopyAutoBackupOnWrite = _EltCopyAutoBackupOnWrite_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 5),
    _EltCopyAutoBackupOnWrite_Type()
)
eltCopyAutoBackupOnWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyAutoBackupOnWrite.setStatus("current")


class _EltCopyUserBackupStart_Type(EltCopyUserBackupStatus):
    """Custom type eltCopyUserBackupStart based on EltCopyUserBackupStatus"""


_EltCopyUserBackupStart_Object = MibScalar
eltCopyUserBackupStart = _EltCopyUserBackupStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 6),
    _EltCopyUserBackupStart_Type()
)
eltCopyUserBackupStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyUserBackupStart.setStatus("current")


class _EltCopyBackupHistoryEnable_Type(TruthValue):
    """Custom type eltCopyBackupHistoryEnable based on TruthValue"""


_EltCopyBackupHistoryEnable_Object = MibScalar
eltCopyBackupHistoryEnable = _EltCopyBackupHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 7),
    _EltCopyBackupHistoryEnable_Type()
)
eltCopyBackupHistoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryEnable.setStatus("current")
_EltCopyBackupHistoryTable_Object = MibTable
eltCopyBackupHistoryTable = _EltCopyBackupHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8)
)
if mibBuilder.loadTexts:
    eltCopyBackupHistoryTable.setStatus("current")
_EltCopyBackupHistoryEntry_Object = MibTableRow
eltCopyBackupHistoryEntry = _EltCopyBackupHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8, 1)
)
eltCopyBackupHistoryEntry.setIndexNames(
    (0, "ELTEX-MES-COPY-MIB", "eltCopyBackupHistoryIndex"),
)
if mibBuilder.loadTexts:
    eltCopyBackupHistoryEntry.setStatus("current")
_EltCopyBackupHistoryIndex_Type = Integer32
_EltCopyBackupHistoryIndex_Object = MibTableColumn
eltCopyBackupHistoryIndex = _EltCopyBackupHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8, 1, 1),
    _EltCopyBackupHistoryIndex_Type()
)
eltCopyBackupHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryIndex.setStatus("current")
_EltCopyBackupHistoryDateTime_Type = DisplayString
_EltCopyBackupHistoryDateTime_Object = MibTableColumn
eltCopyBackupHistoryDateTime = _EltCopyBackupHistoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8, 1, 2),
    _EltCopyBackupHistoryDateTime_Type()
)
eltCopyBackupHistoryDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryDateTime.setStatus("current")
_EltCopyBackupHistoryDstLocation_Type = RlCopyLocationType
_EltCopyBackupHistoryDstLocation_Object = MibTableColumn
eltCopyBackupHistoryDstLocation = _EltCopyBackupHistoryDstLocation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8, 1, 3),
    _EltCopyBackupHistoryDstLocation_Type()
)
eltCopyBackupHistoryDstLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryDstLocation.setStatus("current")
_EltCopyBackupHistoryServerAddr_Type = DisplayString
_EltCopyBackupHistoryServerAddr_Object = MibTableColumn
eltCopyBackupHistoryServerAddr = _EltCopyBackupHistoryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8, 1, 4),
    _EltCopyBackupHistoryServerAddr_Type()
)
eltCopyBackupHistoryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryServerAddr.setStatus("current")
_EltCopyBackupHistoryFilePath_Type = DisplayString
_EltCopyBackupHistoryFilePath_Object = MibTableColumn
eltCopyBackupHistoryFilePath = _EltCopyBackupHistoryFilePath_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8, 1, 5),
    _EltCopyBackupHistoryFilePath_Type()
)
eltCopyBackupHistoryFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryFilePath.setStatus("current")
_EltCopyBackupHistoryStatus_Type = RowStatus
_EltCopyBackupHistoryStatus_Object = MibTableColumn
eltCopyBackupHistoryStatus = _EltCopyBackupHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 8, 1, 6),
    _EltCopyBackupHistoryStatus_Type()
)
eltCopyBackupHistoryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryStatus.setStatus("current")


class _EltCopyBackupHistoryAction_Type(Integer32):
    """Custom type eltCopyBackupHistoryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearNow", 2),
          ("noAction", 1))
    )


_EltCopyBackupHistoryAction_Type.__name__ = "Integer32"
_EltCopyBackupHistoryAction_Object = MibScalar
eltCopyBackupHistoryAction = _EltCopyBackupHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 3, 9),
    _EltCopyBackupHistoryAction_Type()
)
eltCopyBackupHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCopyBackupHistoryAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-COPY-MIB",
    **{"EltCopyUserBackupStatus": EltCopyUserBackupStatus,
       "eltCopyAutoBackupEnable": eltCopyAutoBackupEnable,
       "eltCopyAutoBackupTimeout": eltCopyAutoBackupTimeout,
       "eltCopyAutoBackupFilePath": eltCopyAutoBackupFilePath,
       "eltCopyAutoBackupServerAddress": eltCopyAutoBackupServerAddress,
       "eltCopyAutoBackupOnWrite": eltCopyAutoBackupOnWrite,
       "eltCopyUserBackupStart": eltCopyUserBackupStart,
       "eltCopyBackupHistoryEnable": eltCopyBackupHistoryEnable,
       "eltCopyBackupHistoryTable": eltCopyBackupHistoryTable,
       "eltCopyBackupHistoryEntry": eltCopyBackupHistoryEntry,
       "eltCopyBackupHistoryIndex": eltCopyBackupHistoryIndex,
       "eltCopyBackupHistoryDateTime": eltCopyBackupHistoryDateTime,
       "eltCopyBackupHistoryDstLocation": eltCopyBackupHistoryDstLocation,
       "eltCopyBackupHistoryServerAddr": eltCopyBackupHistoryServerAddr,
       "eltCopyBackupHistoryFilePath": eltCopyBackupHistoryFilePath,
       "eltCopyBackupHistoryStatus": eltCopyBackupHistoryStatus,
       "eltCopyBackupHistoryAction": eltCopyBackupHistoryAction}
)
