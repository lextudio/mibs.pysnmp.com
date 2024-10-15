# SNMP MIB module (GSMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GSMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:15 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

gsmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 98)
)
gsmpMIB.setRevisions(
        ("2002-05-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class GsmpNameType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class GsmpPartitionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixedPartitionAssigned", 3),
          ("fixedPartitionRequest", 2),
          ("noPartition", 1))
    )



class GsmpPartitionIdType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class GsmpVersion(Unsigned32, TextualConvention):
    status = "current"


class GsmpLabelType(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_GsmpNotifications_ObjectIdentity = ObjectIdentity
gsmpNotifications = _GsmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 98, 0)
)
_GsmpObjects_ObjectIdentity = ObjectIdentity
gsmpObjects = _GsmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 98, 1)
)
_GsmpControllerTable_Object = MibTable
gsmpControllerTable = _GsmpControllerTable_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1)
)
if mibBuilder.loadTexts:
    gsmpControllerTable.setStatus("current")
_GsmpControllerEntry_Object = MibTableRow
gsmpControllerEntry = _GsmpControllerEntry_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1)
)
gsmpControllerEntry.setIndexNames(
    (0, "GSMP-MIB", "gsmpControllerEntityId"),
)
if mibBuilder.loadTexts:
    gsmpControllerEntry.setStatus("current")
_GsmpControllerEntityId_Type = GsmpNameType
_GsmpControllerEntityId_Object = MibTableColumn
gsmpControllerEntityId = _GsmpControllerEntityId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 1),
    _GsmpControllerEntityId_Type()
)
gsmpControllerEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmpControllerEntityId.setStatus("current")


class _GsmpControllerMaxVersion_Type(GsmpVersion):
    """Custom type gsmpControllerMaxVersion based on GsmpVersion"""
    defaultValue = 3


_GsmpControllerMaxVersion_Object = MibTableColumn
gsmpControllerMaxVersion = _GsmpControllerMaxVersion_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 2),
    _GsmpControllerMaxVersion_Type()
)
gsmpControllerMaxVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerMaxVersion.setStatus("current")


class _GsmpControllerTimer_Type(Unsigned32):
    """Custom type gsmpControllerTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmpControllerTimer_Type.__name__ = "Unsigned32"
_GsmpControllerTimer_Object = MibTableColumn
gsmpControllerTimer = _GsmpControllerTimer_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 3),
    _GsmpControllerTimer_Type()
)
gsmpControllerTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerTimer.setStatus("current")
if mibBuilder.loadTexts:
    gsmpControllerTimer.setUnits("100ms")
_GsmpControllerPort_Type = Unsigned32
_GsmpControllerPort_Object = MibTableColumn
gsmpControllerPort = _GsmpControllerPort_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 4),
    _GsmpControllerPort_Type()
)
gsmpControllerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerPort.setStatus("current")


class _GsmpControllerInstance_Type(Unsigned32):
    """Custom type gsmpControllerInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_GsmpControllerInstance_Type.__name__ = "Unsigned32"
_GsmpControllerInstance_Object = MibTableColumn
gsmpControllerInstance = _GsmpControllerInstance_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 5),
    _GsmpControllerInstance_Type()
)
gsmpControllerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpControllerInstance.setStatus("current")
_GsmpControllerPartitionType_Type = GsmpPartitionType
_GsmpControllerPartitionType_Object = MibTableColumn
gsmpControllerPartitionType = _GsmpControllerPartitionType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 6),
    _GsmpControllerPartitionType_Type()
)
gsmpControllerPartitionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerPartitionType.setStatus("current")
_GsmpControllerPartitionId_Type = GsmpPartitionIdType
_GsmpControllerPartitionId_Object = MibTableColumn
gsmpControllerPartitionId = _GsmpControllerPartitionId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 7),
    _GsmpControllerPartitionId_Type()
)
gsmpControllerPartitionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerPartitionId.setStatus("current")


class _GsmpControllerDoResync_Type(TruthValue):
    """Custom type gsmpControllerDoResync based on TruthValue"""


_GsmpControllerDoResync_Object = MibTableColumn
gsmpControllerDoResync = _GsmpControllerDoResync_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 8),
    _GsmpControllerDoResync_Type()
)
gsmpControllerDoResync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerDoResync.setStatus("current")


class _GsmpControllerNotificationMap_Type(Bits):
    """Custom type gsmpControllerNotificationMap based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("adjacencyUpdateEvent", 9),
          ("deadPortEvent", 8),
          ("invalidLabelEvent", 6),
          ("newPortEvent", 7),
          ("portDownEvent", 5),
          ("portUpEvent", 4),
          ("receivedFailureIndication", 3),
          ("sendFailureIndication", 2),
          ("sessionDown", 0),
          ("sessionUp", 1))
    )

_GsmpControllerNotificationMap_Type.__name__ = "Bits"
_GsmpControllerNotificationMap_Object = MibTableColumn
gsmpControllerNotificationMap = _GsmpControllerNotificationMap_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 9),
    _GsmpControllerNotificationMap_Type()
)
gsmpControllerNotificationMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerNotificationMap.setStatus("current")


class _GsmpControllerSessionState_Type(Integer32):
    """Custom type gsmpControllerSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("estab", 4),
          ("null", 1),
          ("synrcvd", 3),
          ("synsent", 2))
    )


_GsmpControllerSessionState_Type.__name__ = "Integer32"
_GsmpControllerSessionState_Object = MibTableColumn
gsmpControllerSessionState = _GsmpControllerSessionState_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 10),
    _GsmpControllerSessionState_Type()
)
gsmpControllerSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpControllerSessionState.setStatus("current")


class _GsmpControllerStorageType_Type(StorageType):
    """Custom type gsmpControllerStorageType based on StorageType"""


_GsmpControllerStorageType_Object = MibTableColumn
gsmpControllerStorageType = _GsmpControllerStorageType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 11),
    _GsmpControllerStorageType_Type()
)
gsmpControllerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerStorageType.setStatus("current")
_GsmpControllerRowStatus_Type = RowStatus
_GsmpControllerRowStatus_Object = MibTableColumn
gsmpControllerRowStatus = _GsmpControllerRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 12),
    _GsmpControllerRowStatus_Type()
)
gsmpControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpControllerRowStatus.setStatus("current")
_GsmpSwitchTable_Object = MibTable
gsmpSwitchTable = _GsmpSwitchTable_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2)
)
if mibBuilder.loadTexts:
    gsmpSwitchTable.setStatus("current")
_GsmpSwitchEntry_Object = MibTableRow
gsmpSwitchEntry = _GsmpSwitchEntry_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1)
)
gsmpSwitchEntry.setIndexNames(
    (0, "GSMP-MIB", "gsmpSwitchEntityId"),
)
if mibBuilder.loadTexts:
    gsmpSwitchEntry.setStatus("current")
_GsmpSwitchEntityId_Type = GsmpNameType
_GsmpSwitchEntityId_Object = MibTableColumn
gsmpSwitchEntityId = _GsmpSwitchEntityId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 1),
    _GsmpSwitchEntityId_Type()
)
gsmpSwitchEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmpSwitchEntityId.setStatus("current")


class _GsmpSwitchMaxVersion_Type(GsmpVersion):
    """Custom type gsmpSwitchMaxVersion based on GsmpVersion"""
    defaultValue = 3


_GsmpSwitchMaxVersion_Object = MibTableColumn
gsmpSwitchMaxVersion = _GsmpSwitchMaxVersion_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 2),
    _GsmpSwitchMaxVersion_Type()
)
gsmpSwitchMaxVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchMaxVersion.setStatus("current")


class _GsmpSwitchTimer_Type(Unsigned32):
    """Custom type gsmpSwitchTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmpSwitchTimer_Type.__name__ = "Unsigned32"
_GsmpSwitchTimer_Object = MibTableColumn
gsmpSwitchTimer = _GsmpSwitchTimer_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 3),
    _GsmpSwitchTimer_Type()
)
gsmpSwitchTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchTimer.setStatus("current")
if mibBuilder.loadTexts:
    gsmpSwitchTimer.setUnits("100ms")
_GsmpSwitchName_Type = GsmpNameType
_GsmpSwitchName_Object = MibTableColumn
gsmpSwitchName = _GsmpSwitchName_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 4),
    _GsmpSwitchName_Type()
)
gsmpSwitchName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchName.setStatus("current")
_GsmpSwitchPort_Type = Unsigned32
_GsmpSwitchPort_Object = MibTableColumn
gsmpSwitchPort = _GsmpSwitchPort_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 5),
    _GsmpSwitchPort_Type()
)
gsmpSwitchPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchPort.setStatus("current")


class _GsmpSwitchInstance_Type(Unsigned32):
    """Custom type gsmpSwitchInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_GsmpSwitchInstance_Type.__name__ = "Unsigned32"
_GsmpSwitchInstance_Object = MibTableColumn
gsmpSwitchInstance = _GsmpSwitchInstance_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 6),
    _GsmpSwitchInstance_Type()
)
gsmpSwitchInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSwitchInstance.setStatus("current")
_GsmpSwitchPartitionType_Type = GsmpPartitionType
_GsmpSwitchPartitionType_Object = MibTableColumn
gsmpSwitchPartitionType = _GsmpSwitchPartitionType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 7),
    _GsmpSwitchPartitionType_Type()
)
gsmpSwitchPartitionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchPartitionType.setStatus("current")
_GsmpSwitchPartitionId_Type = GsmpPartitionIdType
_GsmpSwitchPartitionId_Object = MibTableColumn
gsmpSwitchPartitionId = _GsmpSwitchPartitionId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 8),
    _GsmpSwitchPartitionId_Type()
)
gsmpSwitchPartitionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchPartitionId.setStatus("current")


class _GsmpSwitchNotificationMap_Type(Bits):
    """Custom type gsmpSwitchNotificationMap based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("adjacencyUpdateEvent", 9),
          ("deadPortEvent", 8),
          ("invalidLabelEvent", 6),
          ("newPortEvent", 7),
          ("portDownEvent", 5),
          ("portUpEvent", 4),
          ("receivedFailureIndication", 3),
          ("sendFailureIndication", 2),
          ("sessionDown", 0),
          ("sessionUp", 1))
    )

_GsmpSwitchNotificationMap_Type.__name__ = "Bits"
_GsmpSwitchNotificationMap_Object = MibTableColumn
gsmpSwitchNotificationMap = _GsmpSwitchNotificationMap_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 9),
    _GsmpSwitchNotificationMap_Type()
)
gsmpSwitchNotificationMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchNotificationMap.setStatus("current")


class _GsmpSwitchSwitchType_Type(OctetString):
    """Custom type gsmpSwitchSwitchType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GsmpSwitchSwitchType_Type.__name__ = "OctetString"
_GsmpSwitchSwitchType_Object = MibTableColumn
gsmpSwitchSwitchType = _GsmpSwitchSwitchType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 10),
    _GsmpSwitchSwitchType_Type()
)
gsmpSwitchSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchSwitchType.setStatus("current")


class _GsmpSwitchWindowSize_Type(Unsigned32):
    """Custom type gsmpSwitchWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsmpSwitchWindowSize_Type.__name__ = "Unsigned32"
_GsmpSwitchWindowSize_Object = MibTableColumn
gsmpSwitchWindowSize = _GsmpSwitchWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 11),
    _GsmpSwitchWindowSize_Type()
)
gsmpSwitchWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchWindowSize.setStatus("current")


class _GsmpSwitchSessionState_Type(Integer32):
    """Custom type gsmpSwitchSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("estab", 4),
          ("null", 1),
          ("synrcvd", 3),
          ("synsent", 2))
    )


_GsmpSwitchSessionState_Type.__name__ = "Integer32"
_GsmpSwitchSessionState_Object = MibTableColumn
gsmpSwitchSessionState = _GsmpSwitchSessionState_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 12),
    _GsmpSwitchSessionState_Type()
)
gsmpSwitchSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSwitchSessionState.setStatus("current")


class _GsmpSwitchStorageType_Type(StorageType):
    """Custom type gsmpSwitchStorageType based on StorageType"""


_GsmpSwitchStorageType_Object = MibTableColumn
gsmpSwitchStorageType = _GsmpSwitchStorageType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 13),
    _GsmpSwitchStorageType_Type()
)
gsmpSwitchStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchStorageType.setStatus("current")
_GsmpSwitchRowStatus_Type = RowStatus
_GsmpSwitchRowStatus_Object = MibTableColumn
gsmpSwitchRowStatus = _GsmpSwitchRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 14),
    _GsmpSwitchRowStatus_Type()
)
gsmpSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpSwitchRowStatus.setStatus("current")
_GsmpAtmEncapTable_Object = MibTable
gsmpAtmEncapTable = _GsmpAtmEncapTable_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3)
)
if mibBuilder.loadTexts:
    gsmpAtmEncapTable.setStatus("current")
_GsmpAtmEncapEntry_Object = MibTableRow
gsmpAtmEncapEntry = _GsmpAtmEncapEntry_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3, 1)
)
gsmpAtmEncapEntry.setIndexNames(
    (0, "GSMP-MIB", "gsmpAtmEncapEntityId"),
)
if mibBuilder.loadTexts:
    gsmpAtmEncapEntry.setStatus("current")
_GsmpAtmEncapEntityId_Type = GsmpNameType
_GsmpAtmEncapEntityId_Object = MibTableColumn
gsmpAtmEncapEntityId = _GsmpAtmEncapEntityId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 1),
    _GsmpAtmEncapEntityId_Type()
)
gsmpAtmEncapEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmpAtmEncapEntityId.setStatus("current")
_GsmpAtmEncapIfIndex_Type = InterfaceIndex
_GsmpAtmEncapIfIndex_Object = MibTableColumn
gsmpAtmEncapIfIndex = _GsmpAtmEncapIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 2),
    _GsmpAtmEncapIfIndex_Type()
)
gsmpAtmEncapIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpAtmEncapIfIndex.setStatus("current")


class _GsmpAtmEncapVpi_Type(AtmVpIdentifier):
    """Custom type gsmpAtmEncapVpi based on AtmVpIdentifier"""
    defaultValue = 0


_GsmpAtmEncapVpi_Object = MibTableColumn
gsmpAtmEncapVpi = _GsmpAtmEncapVpi_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 3),
    _GsmpAtmEncapVpi_Type()
)
gsmpAtmEncapVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpAtmEncapVpi.setStatus("current")


class _GsmpAtmEncapVci_Type(AtmVcIdentifier):
    """Custom type gsmpAtmEncapVci based on AtmVcIdentifier"""
    defaultValue = 15


_GsmpAtmEncapVci_Object = MibTableColumn
gsmpAtmEncapVci = _GsmpAtmEncapVci_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 4),
    _GsmpAtmEncapVci_Type()
)
gsmpAtmEncapVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpAtmEncapVci.setStatus("current")


class _GsmpAtmEncapStorageType_Type(StorageType):
    """Custom type gsmpAtmEncapStorageType based on StorageType"""


_GsmpAtmEncapStorageType_Object = MibTableColumn
gsmpAtmEncapStorageType = _GsmpAtmEncapStorageType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 5),
    _GsmpAtmEncapStorageType_Type()
)
gsmpAtmEncapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpAtmEncapStorageType.setStatus("current")
_GsmpAtmEncapRowStatus_Type = RowStatus
_GsmpAtmEncapRowStatus_Object = MibTableColumn
gsmpAtmEncapRowStatus = _GsmpAtmEncapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 6),
    _GsmpAtmEncapRowStatus_Type()
)
gsmpAtmEncapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpAtmEncapRowStatus.setStatus("current")
_GsmpTcpIpEncapTable_Object = MibTable
gsmpTcpIpEncapTable = _GsmpTcpIpEncapTable_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4)
)
if mibBuilder.loadTexts:
    gsmpTcpIpEncapTable.setStatus("current")
_GsmpTcpIpEncapEntry_Object = MibTableRow
gsmpTcpIpEncapEntry = _GsmpTcpIpEncapEntry_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4, 1)
)
gsmpTcpIpEncapEntry.setIndexNames(
    (0, "GSMP-MIB", "gsmpTcpIpEncapEntityId"),
)
if mibBuilder.loadTexts:
    gsmpTcpIpEncapEntry.setStatus("current")
_GsmpTcpIpEncapEntityId_Type = GsmpNameType
_GsmpTcpIpEncapEntityId_Object = MibTableColumn
gsmpTcpIpEncapEntityId = _GsmpTcpIpEncapEntityId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 1),
    _GsmpTcpIpEncapEntityId_Type()
)
gsmpTcpIpEncapEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmpTcpIpEncapEntityId.setStatus("current")
_GsmpTcpIpEncapAddressType_Type = InetAddressType
_GsmpTcpIpEncapAddressType_Object = MibTableColumn
gsmpTcpIpEncapAddressType = _GsmpTcpIpEncapAddressType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 2),
    _GsmpTcpIpEncapAddressType_Type()
)
gsmpTcpIpEncapAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpTcpIpEncapAddressType.setStatus("current")
_GsmpTcpIpEncapAddress_Type = InetAddress
_GsmpTcpIpEncapAddress_Object = MibTableColumn
gsmpTcpIpEncapAddress = _GsmpTcpIpEncapAddress_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 3),
    _GsmpTcpIpEncapAddress_Type()
)
gsmpTcpIpEncapAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpTcpIpEncapAddress.setStatus("current")


class _GsmpTcpIpEncapPortNumber_Type(InetPortNumber):
    """Custom type gsmpTcpIpEncapPortNumber based on InetPortNumber"""
    defaultValue = 6068


_GsmpTcpIpEncapPortNumber_Object = MibTableColumn
gsmpTcpIpEncapPortNumber = _GsmpTcpIpEncapPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 4),
    _GsmpTcpIpEncapPortNumber_Type()
)
gsmpTcpIpEncapPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpTcpIpEncapPortNumber.setStatus("current")


class _GsmpTcpIpEncapStorageType_Type(StorageType):
    """Custom type gsmpTcpIpEncapStorageType based on StorageType"""


_GsmpTcpIpEncapStorageType_Object = MibTableColumn
gsmpTcpIpEncapStorageType = _GsmpTcpIpEncapStorageType_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 5),
    _GsmpTcpIpEncapStorageType_Type()
)
gsmpTcpIpEncapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpTcpIpEncapStorageType.setStatus("current")
_GsmpTcpIpEncapRowStatus_Type = RowStatus
_GsmpTcpIpEncapRowStatus_Object = MibTableColumn
gsmpTcpIpEncapRowStatus = _GsmpTcpIpEncapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 6),
    _GsmpTcpIpEncapRowStatus_Type()
)
gsmpTcpIpEncapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gsmpTcpIpEncapRowStatus.setStatus("current")
_GsmpSessionTable_Object = MibTable
gsmpSessionTable = _GsmpSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5)
)
if mibBuilder.loadTexts:
    gsmpSessionTable.setStatus("current")
_GsmpSessionEntry_Object = MibTableRow
gsmpSessionEntry = _GsmpSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1)
)
gsmpSessionEntry.setIndexNames(
    (0, "GSMP-MIB", "gsmpSessionThisSideId"),
    (0, "GSMP-MIB", "gsmpSessionFarSideId"),
)
if mibBuilder.loadTexts:
    gsmpSessionEntry.setStatus("current")
_GsmpSessionThisSideId_Type = GsmpNameType
_GsmpSessionThisSideId_Object = MibTableColumn
gsmpSessionThisSideId = _GsmpSessionThisSideId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 1),
    _GsmpSessionThisSideId_Type()
)
gsmpSessionThisSideId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmpSessionThisSideId.setStatus("current")
_GsmpSessionFarSideId_Type = GsmpNameType
_GsmpSessionFarSideId_Object = MibTableColumn
gsmpSessionFarSideId = _GsmpSessionFarSideId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 2),
    _GsmpSessionFarSideId_Type()
)
gsmpSessionFarSideId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmpSessionFarSideId.setStatus("current")
_GsmpSessionVersion_Type = GsmpVersion
_GsmpSessionVersion_Object = MibTableColumn
gsmpSessionVersion = _GsmpSessionVersion_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 3),
    _GsmpSessionVersion_Type()
)
gsmpSessionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionVersion.setStatus("current")
_GsmpSessionTimer_Type = Integer32
_GsmpSessionTimer_Object = MibTableColumn
gsmpSessionTimer = _GsmpSessionTimer_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 4),
    _GsmpSessionTimer_Type()
)
gsmpSessionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionTimer.setStatus("current")
if mibBuilder.loadTexts:
    gsmpSessionTimer.setUnits("100ms")
_GsmpSessionPartitionId_Type = GsmpPartitionIdType
_GsmpSessionPartitionId_Object = MibTableColumn
gsmpSessionPartitionId = _GsmpSessionPartitionId_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 5),
    _GsmpSessionPartitionId_Type()
)
gsmpSessionPartitionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionPartitionId.setStatus("current")


class _GsmpSessionAdjacencyCount_Type(Unsigned32):
    """Custom type gsmpSessionAdjacencyCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmpSessionAdjacencyCount_Type.__name__ = "Unsigned32"
_GsmpSessionAdjacencyCount_Object = MibTableColumn
gsmpSessionAdjacencyCount = _GsmpSessionAdjacencyCount_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 6),
    _GsmpSessionAdjacencyCount_Type()
)
gsmpSessionAdjacencyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionAdjacencyCount.setStatus("current")
_GsmpSessionFarSideName_Type = GsmpNameType
_GsmpSessionFarSideName_Object = MibTableColumn
gsmpSessionFarSideName = _GsmpSessionFarSideName_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 7),
    _GsmpSessionFarSideName_Type()
)
gsmpSessionFarSideName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionFarSideName.setStatus("current")
_GsmpSessionFarSidePort_Type = Unsigned32
_GsmpSessionFarSidePort_Object = MibTableColumn
gsmpSessionFarSidePort = _GsmpSessionFarSidePort_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 8),
    _GsmpSessionFarSidePort_Type()
)
gsmpSessionFarSidePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionFarSidePort.setStatus("current")


class _GsmpSessionFarSideInstance_Type(Unsigned32):
    """Custom type gsmpSessionFarSideInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_GsmpSessionFarSideInstance_Type.__name__ = "Unsigned32"
_GsmpSessionFarSideInstance_Object = MibTableColumn
gsmpSessionFarSideInstance = _GsmpSessionFarSideInstance_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 9),
    _GsmpSessionFarSideInstance_Type()
)
gsmpSessionFarSideInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionFarSideInstance.setStatus("current")


class _GsmpSessionLastFailureCode_Type(Unsigned32):
    """Custom type gsmpSessionLastFailureCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GsmpSessionLastFailureCode_Type.__name__ = "Unsigned32"
_GsmpSessionLastFailureCode_Object = MibTableColumn
gsmpSessionLastFailureCode = _GsmpSessionLastFailureCode_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 10),
    _GsmpSessionLastFailureCode_Type()
)
gsmpSessionLastFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionLastFailureCode.setStatus("current")
_GsmpSessionDiscontinuityTime_Type = TimeStamp
_GsmpSessionDiscontinuityTime_Object = MibTableColumn
gsmpSessionDiscontinuityTime = _GsmpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 11),
    _GsmpSessionDiscontinuityTime_Type()
)
gsmpSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionDiscontinuityTime.setStatus("current")
_GsmpSessionStartUptime_Type = TimeStamp
_GsmpSessionStartUptime_Object = MibTableColumn
gsmpSessionStartUptime = _GsmpSessionStartUptime_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 12),
    _GsmpSessionStartUptime_Type()
)
gsmpSessionStartUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStartUptime.setStatus("current")
_GsmpSessionStatSentMessages_Type = ZeroBasedCounter32
_GsmpSessionStatSentMessages_Object = MibTableColumn
gsmpSessionStatSentMessages = _GsmpSessionStatSentMessages_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 13),
    _GsmpSessionStatSentMessages_Type()
)
gsmpSessionStatSentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatSentMessages.setStatus("current")
_GsmpSessionStatFailureInds_Type = ZeroBasedCounter32
_GsmpSessionStatFailureInds_Object = MibTableColumn
gsmpSessionStatFailureInds = _GsmpSessionStatFailureInds_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 14),
    _GsmpSessionStatFailureInds_Type()
)
gsmpSessionStatFailureInds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatFailureInds.setStatus("current")
_GsmpSessionStatReceivedMessages_Type = ZeroBasedCounter32
_GsmpSessionStatReceivedMessages_Object = MibTableColumn
gsmpSessionStatReceivedMessages = _GsmpSessionStatReceivedMessages_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 15),
    _GsmpSessionStatReceivedMessages_Type()
)
gsmpSessionStatReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatReceivedMessages.setStatus("current")
_GsmpSessionStatReceivedFailures_Type = ZeroBasedCounter32
_GsmpSessionStatReceivedFailures_Object = MibTableColumn
gsmpSessionStatReceivedFailures = _GsmpSessionStatReceivedFailures_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 16),
    _GsmpSessionStatReceivedFailures_Type()
)
gsmpSessionStatReceivedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatReceivedFailures.setStatus("current")
_GsmpSessionStatPortUpEvents_Type = ZeroBasedCounter32
_GsmpSessionStatPortUpEvents_Object = MibTableColumn
gsmpSessionStatPortUpEvents = _GsmpSessionStatPortUpEvents_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 17),
    _GsmpSessionStatPortUpEvents_Type()
)
gsmpSessionStatPortUpEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatPortUpEvents.setStatus("current")
_GsmpSessionStatPortDownEvents_Type = ZeroBasedCounter32
_GsmpSessionStatPortDownEvents_Object = MibTableColumn
gsmpSessionStatPortDownEvents = _GsmpSessionStatPortDownEvents_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 18),
    _GsmpSessionStatPortDownEvents_Type()
)
gsmpSessionStatPortDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatPortDownEvents.setStatus("current")
_GsmpSessionStatInvLabelEvents_Type = ZeroBasedCounter32
_GsmpSessionStatInvLabelEvents_Object = MibTableColumn
gsmpSessionStatInvLabelEvents = _GsmpSessionStatInvLabelEvents_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 19),
    _GsmpSessionStatInvLabelEvents_Type()
)
gsmpSessionStatInvLabelEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatInvLabelEvents.setStatus("current")
_GsmpSessionStatNewPortEvents_Type = ZeroBasedCounter32
_GsmpSessionStatNewPortEvents_Object = MibTableColumn
gsmpSessionStatNewPortEvents = _GsmpSessionStatNewPortEvents_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 20),
    _GsmpSessionStatNewPortEvents_Type()
)
gsmpSessionStatNewPortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatNewPortEvents.setStatus("current")
_GsmpSessionStatDeadPortEvents_Type = ZeroBasedCounter32
_GsmpSessionStatDeadPortEvents_Object = MibTableColumn
gsmpSessionStatDeadPortEvents = _GsmpSessionStatDeadPortEvents_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 21),
    _GsmpSessionStatDeadPortEvents_Type()
)
gsmpSessionStatDeadPortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatDeadPortEvents.setStatus("current")
_GsmpSessionStatAdjUpdateEvents_Type = ZeroBasedCounter32
_GsmpSessionStatAdjUpdateEvents_Object = MibTableColumn
gsmpSessionStatAdjUpdateEvents = _GsmpSessionStatAdjUpdateEvents_Object(
    (1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 22),
    _GsmpSessionStatAdjUpdateEvents_Type()
)
gsmpSessionStatAdjUpdateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmpSessionStatAdjUpdateEvents.setStatus("current")
_GsmpNotificationsObjects_ObjectIdentity = ObjectIdentity
gsmpNotificationsObjects = _GsmpNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 98, 2)
)
_GsmpEventPort_Type = Unsigned32
_GsmpEventPort_Object = MibScalar
gsmpEventPort = _GsmpEventPort_Object(
    (1, 3, 6, 1, 2, 1, 98, 2, 1),
    _GsmpEventPort_Type()
)
gsmpEventPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gsmpEventPort.setStatus("current")
_GsmpEventPortSessionNumber_Type = Unsigned32
_GsmpEventPortSessionNumber_Object = MibScalar
gsmpEventPortSessionNumber = _GsmpEventPortSessionNumber_Object(
    (1, 3, 6, 1, 2, 1, 98, 2, 2),
    _GsmpEventPortSessionNumber_Type()
)
gsmpEventPortSessionNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gsmpEventPortSessionNumber.setStatus("current")
_GsmpEventSequenceNumber_Type = Unsigned32
_GsmpEventSequenceNumber_Object = MibScalar
gsmpEventSequenceNumber = _GsmpEventSequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 98, 2, 3),
    _GsmpEventSequenceNumber_Type()
)
gsmpEventSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gsmpEventSequenceNumber.setStatus("current")
_GsmpEventLabel_Type = GsmpLabelType
_GsmpEventLabel_Object = MibScalar
gsmpEventLabel = _GsmpEventLabel_Object(
    (1, 3, 6, 1, 2, 1, 98, 2, 4),
    _GsmpEventLabel_Type()
)
gsmpEventLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gsmpEventLabel.setStatus("current")
_GsmpConformance_ObjectIdentity = ObjectIdentity
gsmpConformance = _GsmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 98, 3)
)
_GsmpGroups_ObjectIdentity = ObjectIdentity
gsmpGroups = _GsmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 98, 3, 1)
)
_GsmpCompliances_ObjectIdentity = ObjectIdentity
gsmpCompliances = _GsmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 98, 3, 2)
)

# Managed Objects groups

gsmpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 98, 3, 1, 1)
)
gsmpGeneralGroup.setObjects(
      *(("GSMP-MIB", "gsmpSessionVersion"),
        ("GSMP-MIB", "gsmpSessionTimer"),
        ("GSMP-MIB", "gsmpSessionPartitionId"),
        ("GSMP-MIB", "gsmpSessionAdjacencyCount"),
        ("GSMP-MIB", "gsmpSessionFarSideName"),
        ("GSMP-MIB", "gsmpSessionFarSidePort"),
        ("GSMP-MIB", "gsmpSessionFarSideInstance"),
        ("GSMP-MIB", "gsmpSessionLastFailureCode"),
        ("GSMP-MIB", "gsmpSessionDiscontinuityTime"),
        ("GSMP-MIB", "gsmpSessionStartUptime"),
        ("GSMP-MIB", "gsmpSessionStatSentMessages"),
        ("GSMP-MIB", "gsmpSessionStatFailureInds"),
        ("GSMP-MIB", "gsmpSessionStatReceivedMessages"),
        ("GSMP-MIB", "gsmpSessionStatReceivedFailures"),
        ("GSMP-MIB", "gsmpSessionStatPortUpEvents"),
        ("GSMP-MIB", "gsmpSessionStatPortDownEvents"),
        ("GSMP-MIB", "gsmpSessionStatInvLabelEvents"),
        ("GSMP-MIB", "gsmpSessionStatNewPortEvents"),
        ("GSMP-MIB", "gsmpSessionStatDeadPortEvents"),
        ("GSMP-MIB", "gsmpSessionStatAdjUpdateEvents"))
)
if mibBuilder.loadTexts:
    gsmpGeneralGroup.setStatus("current")

gsmpControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 98, 3, 1, 2)
)
gsmpControllerGroup.setObjects(
      *(("GSMP-MIB", "gsmpControllerMaxVersion"),
        ("GSMP-MIB", "gsmpControllerTimer"),
        ("GSMP-MIB", "gsmpControllerPort"),
        ("GSMP-MIB", "gsmpControllerInstance"),
        ("GSMP-MIB", "gsmpControllerPartitionType"),
        ("GSMP-MIB", "gsmpControllerPartitionId"),
        ("GSMP-MIB", "gsmpControllerDoResync"),
        ("GSMP-MIB", "gsmpControllerNotificationMap"),
        ("GSMP-MIB", "gsmpControllerSessionState"),
        ("GSMP-MIB", "gsmpControllerStorageType"),
        ("GSMP-MIB", "gsmpControllerRowStatus"))
)
if mibBuilder.loadTexts:
    gsmpControllerGroup.setStatus("current")

gsmpSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 98, 3, 1, 3)
)
gsmpSwitchGroup.setObjects(
      *(("GSMP-MIB", "gsmpSwitchMaxVersion"),
        ("GSMP-MIB", "gsmpSwitchTimer"),
        ("GSMP-MIB", "gsmpSwitchName"),
        ("GSMP-MIB", "gsmpSwitchPort"),
        ("GSMP-MIB", "gsmpSwitchInstance"),
        ("GSMP-MIB", "gsmpSwitchPartitionType"),
        ("GSMP-MIB", "gsmpSwitchPartitionId"),
        ("GSMP-MIB", "gsmpSwitchNotificationMap"),
        ("GSMP-MIB", "gsmpSwitchSwitchType"),
        ("GSMP-MIB", "gsmpSwitchWindowSize"),
        ("GSMP-MIB", "gsmpSwitchSessionState"),
        ("GSMP-MIB", "gsmpSwitchStorageType"),
        ("GSMP-MIB", "gsmpSwitchRowStatus"))
)
if mibBuilder.loadTexts:
    gsmpSwitchGroup.setStatus("current")

gsmpAtmEncapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 98, 3, 1, 4)
)
gsmpAtmEncapGroup.setObjects(
      *(("GSMP-MIB", "gsmpAtmEncapIfIndex"),
        ("GSMP-MIB", "gsmpAtmEncapVpi"),
        ("GSMP-MIB", "gsmpAtmEncapVci"),
        ("GSMP-MIB", "gsmpAtmEncapStorageType"),
        ("GSMP-MIB", "gsmpAtmEncapRowStatus"))
)
if mibBuilder.loadTexts:
    gsmpAtmEncapGroup.setStatus("current")

gsmpTcpIpEncapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 98, 3, 1, 5)
)
gsmpTcpIpEncapGroup.setObjects(
      *(("GSMP-MIB", "gsmpTcpIpEncapAddressType"),
        ("GSMP-MIB", "gsmpTcpIpEncapAddress"),
        ("GSMP-MIB", "gsmpTcpIpEncapPortNumber"),
        ("GSMP-MIB", "gsmpTcpIpEncapStorageType"),
        ("GSMP-MIB", "gsmpTcpIpEncapRowStatus"))
)
if mibBuilder.loadTexts:
    gsmpTcpIpEncapGroup.setStatus("current")

gsmpNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 98, 3, 1, 6)
)
gsmpNotificationObjectsGroup.setObjects(
      *(("GSMP-MIB", "gsmpEventPort"),
        ("GSMP-MIB", "gsmpEventPortSessionNumber"),
        ("GSMP-MIB", "gsmpEventSequenceNumber"),
        ("GSMP-MIB", "gsmpEventLabel"))
)
if mibBuilder.loadTexts:
    gsmpNotificationObjectsGroup.setStatus("current")


# Notification objects

gsmpSessionDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 1)
)
gsmpSessionDown.setObjects(
      *(("GSMP-MIB", "gsmpSessionStartUptime"),
        ("GSMP-MIB", "gsmpSessionStatSentMessages"),
        ("GSMP-MIB", "gsmpSessionStatFailureInds"),
        ("GSMP-MIB", "gsmpSessionStatReceivedMessages"),
        ("GSMP-MIB", "gsmpSessionStatReceivedFailures"),
        ("GSMP-MIB", "gsmpSessionStatPortUpEvents"),
        ("GSMP-MIB", "gsmpSessionStatPortDownEvents"),
        ("GSMP-MIB", "gsmpSessionStatInvLabelEvents"),
        ("GSMP-MIB", "gsmpSessionStatNewPortEvents"),
        ("GSMP-MIB", "gsmpSessionStatDeadPortEvents"),
        ("GSMP-MIB", "gsmpSessionStatAdjUpdateEvents"))
)
if mibBuilder.loadTexts:
    gsmpSessionDown.setStatus(
        "current"
    )

gsmpSessionUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 2)
)
gsmpSessionUp.setObjects(
    ("GSMP-MIB", "gsmpSessionFarSideInstance")
)
if mibBuilder.loadTexts:
    gsmpSessionUp.setStatus(
        "current"
    )

gsmpSentFailureInd = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 3)
)
gsmpSentFailureInd.setObjects(
      *(("GSMP-MIB", "gsmpSessionLastFailureCode"),
        ("GSMP-MIB", "gsmpSessionStatFailureInds"))
)
if mibBuilder.loadTexts:
    gsmpSentFailureInd.setStatus(
        "current"
    )

gsmpReceivedFailureInd = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 4)
)
gsmpReceivedFailureInd.setObjects(
      *(("GSMP-MIB", "gsmpSessionLastFailureCode"),
        ("GSMP-MIB", "gsmpSessionStatReceivedFailures"))
)
if mibBuilder.loadTexts:
    gsmpReceivedFailureInd.setStatus(
        "current"
    )

gsmpPortUpEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 5)
)
gsmpPortUpEvent.setObjects(
      *(("GSMP-MIB", "gsmpSessionStatPortUpEvents"),
        ("GSMP-MIB", "gsmpEventPort"),
        ("GSMP-MIB", "gsmpEventPortSessionNumber"),
        ("GSMP-MIB", "gsmpEventSequenceNumber"))
)
if mibBuilder.loadTexts:
    gsmpPortUpEvent.setStatus(
        "current"
    )

gsmpPortDownEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 6)
)
gsmpPortDownEvent.setObjects(
      *(("GSMP-MIB", "gsmpSessionStatPortDownEvents"),
        ("GSMP-MIB", "gsmpEventPort"),
        ("GSMP-MIB", "gsmpEventPortSessionNumber"),
        ("GSMP-MIB", "gsmpEventSequenceNumber"))
)
if mibBuilder.loadTexts:
    gsmpPortDownEvent.setStatus(
        "current"
    )

gsmpInvalidLabelEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 7)
)
gsmpInvalidLabelEvent.setObjects(
      *(("GSMP-MIB", "gsmpSessionStatInvLabelEvents"),
        ("GSMP-MIB", "gsmpEventPort"),
        ("GSMP-MIB", "gsmpEventLabel"),
        ("GSMP-MIB", "gsmpEventSequenceNumber"))
)
if mibBuilder.loadTexts:
    gsmpInvalidLabelEvent.setStatus(
        "current"
    )

gsmpNewPortEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 8)
)
gsmpNewPortEvent.setObjects(
      *(("GSMP-MIB", "gsmpSessionStatNewPortEvents"),
        ("GSMP-MIB", "gsmpEventPort"),
        ("GSMP-MIB", "gsmpEventPortSessionNumber"),
        ("GSMP-MIB", "gsmpEventSequenceNumber"))
)
if mibBuilder.loadTexts:
    gsmpNewPortEvent.setStatus(
        "current"
    )

gsmpDeadPortEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 9)
)
gsmpDeadPortEvent.setObjects(
      *(("GSMP-MIB", "gsmpSessionStatDeadPortEvents"),
        ("GSMP-MIB", "gsmpEventPort"),
        ("GSMP-MIB", "gsmpEventPortSessionNumber"),
        ("GSMP-MIB", "gsmpEventSequenceNumber"))
)
if mibBuilder.loadTexts:
    gsmpDeadPortEvent.setStatus(
        "current"
    )

gsmpAdjacencyUpdateEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 98, 0, 10)
)
gsmpAdjacencyUpdateEvent.setObjects(
      *(("GSMP-MIB", "gsmpSessionAdjacencyCount"),
        ("GSMP-MIB", "gsmpSessionStatAdjUpdateEvents"),
        ("GSMP-MIB", "gsmpEventSequenceNumber"))
)
if mibBuilder.loadTexts:
    gsmpAdjacencyUpdateEvent.setStatus(
        "current"
    )


# Notifications groups

gsmpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 98, 3, 1, 7)
)
gsmpNotificationsGroup.setObjects(
      *(("GSMP-MIB", "gsmpSessionDown"),
        ("GSMP-MIB", "gsmpSessionUp"),
        ("GSMP-MIB", "gsmpSentFailureInd"),
        ("GSMP-MIB", "gsmpReceivedFailureInd"),
        ("GSMP-MIB", "gsmpPortUpEvent"),
        ("GSMP-MIB", "gsmpPortDownEvent"),
        ("GSMP-MIB", "gsmpInvalidLabelEvent"),
        ("GSMP-MIB", "gsmpNewPortEvent"),
        ("GSMP-MIB", "gsmpDeadPortEvent"),
        ("GSMP-MIB", "gsmpAdjacencyUpdateEvent"))
)
if mibBuilder.loadTexts:
    gsmpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

gsmpModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 98, 3, 2, 1)
)
if mibBuilder.loadTexts:
    gsmpModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GSMP-MIB",
    **{"GsmpNameType": GsmpNameType,
       "GsmpPartitionType": GsmpPartitionType,
       "GsmpPartitionIdType": GsmpPartitionIdType,
       "GsmpVersion": GsmpVersion,
       "GsmpLabelType": GsmpLabelType,
       "gsmpMIB": gsmpMIB,
       "gsmpNotifications": gsmpNotifications,
       "gsmpSessionDown": gsmpSessionDown,
       "gsmpSessionUp": gsmpSessionUp,
       "gsmpSentFailureInd": gsmpSentFailureInd,
       "gsmpReceivedFailureInd": gsmpReceivedFailureInd,
       "gsmpPortUpEvent": gsmpPortUpEvent,
       "gsmpPortDownEvent": gsmpPortDownEvent,
       "gsmpInvalidLabelEvent": gsmpInvalidLabelEvent,
       "gsmpNewPortEvent": gsmpNewPortEvent,
       "gsmpDeadPortEvent": gsmpDeadPortEvent,
       "gsmpAdjacencyUpdateEvent": gsmpAdjacencyUpdateEvent,
       "gsmpObjects": gsmpObjects,
       "gsmpControllerTable": gsmpControllerTable,
       "gsmpControllerEntry": gsmpControllerEntry,
       "gsmpControllerEntityId": gsmpControllerEntityId,
       "gsmpControllerMaxVersion": gsmpControllerMaxVersion,
       "gsmpControllerTimer": gsmpControllerTimer,
       "gsmpControllerPort": gsmpControllerPort,
       "gsmpControllerInstance": gsmpControllerInstance,
       "gsmpControllerPartitionType": gsmpControllerPartitionType,
       "gsmpControllerPartitionId": gsmpControllerPartitionId,
       "gsmpControllerDoResync": gsmpControllerDoResync,
       "gsmpControllerNotificationMap": gsmpControllerNotificationMap,
       "gsmpControllerSessionState": gsmpControllerSessionState,
       "gsmpControllerStorageType": gsmpControllerStorageType,
       "gsmpControllerRowStatus": gsmpControllerRowStatus,
       "gsmpSwitchTable": gsmpSwitchTable,
       "gsmpSwitchEntry": gsmpSwitchEntry,
       "gsmpSwitchEntityId": gsmpSwitchEntityId,
       "gsmpSwitchMaxVersion": gsmpSwitchMaxVersion,
       "gsmpSwitchTimer": gsmpSwitchTimer,
       "gsmpSwitchName": gsmpSwitchName,
       "gsmpSwitchPort": gsmpSwitchPort,
       "gsmpSwitchInstance": gsmpSwitchInstance,
       "gsmpSwitchPartitionType": gsmpSwitchPartitionType,
       "gsmpSwitchPartitionId": gsmpSwitchPartitionId,
       "gsmpSwitchNotificationMap": gsmpSwitchNotificationMap,
       "gsmpSwitchSwitchType": gsmpSwitchSwitchType,
       "gsmpSwitchWindowSize": gsmpSwitchWindowSize,
       "gsmpSwitchSessionState": gsmpSwitchSessionState,
       "gsmpSwitchStorageType": gsmpSwitchStorageType,
       "gsmpSwitchRowStatus": gsmpSwitchRowStatus,
       "gsmpAtmEncapTable": gsmpAtmEncapTable,
       "gsmpAtmEncapEntry": gsmpAtmEncapEntry,
       "gsmpAtmEncapEntityId": gsmpAtmEncapEntityId,
       "gsmpAtmEncapIfIndex": gsmpAtmEncapIfIndex,
       "gsmpAtmEncapVpi": gsmpAtmEncapVpi,
       "gsmpAtmEncapVci": gsmpAtmEncapVci,
       "gsmpAtmEncapStorageType": gsmpAtmEncapStorageType,
       "gsmpAtmEncapRowStatus": gsmpAtmEncapRowStatus,
       "gsmpTcpIpEncapTable": gsmpTcpIpEncapTable,
       "gsmpTcpIpEncapEntry": gsmpTcpIpEncapEntry,
       "gsmpTcpIpEncapEntityId": gsmpTcpIpEncapEntityId,
       "gsmpTcpIpEncapAddressType": gsmpTcpIpEncapAddressType,
       "gsmpTcpIpEncapAddress": gsmpTcpIpEncapAddress,
       "gsmpTcpIpEncapPortNumber": gsmpTcpIpEncapPortNumber,
       "gsmpTcpIpEncapStorageType": gsmpTcpIpEncapStorageType,
       "gsmpTcpIpEncapRowStatus": gsmpTcpIpEncapRowStatus,
       "gsmpSessionTable": gsmpSessionTable,
       "gsmpSessionEntry": gsmpSessionEntry,
       "gsmpSessionThisSideId": gsmpSessionThisSideId,
       "gsmpSessionFarSideId": gsmpSessionFarSideId,
       "gsmpSessionVersion": gsmpSessionVersion,
       "gsmpSessionTimer": gsmpSessionTimer,
       "gsmpSessionPartitionId": gsmpSessionPartitionId,
       "gsmpSessionAdjacencyCount": gsmpSessionAdjacencyCount,
       "gsmpSessionFarSideName": gsmpSessionFarSideName,
       "gsmpSessionFarSidePort": gsmpSessionFarSidePort,
       "gsmpSessionFarSideInstance": gsmpSessionFarSideInstance,
       "gsmpSessionLastFailureCode": gsmpSessionLastFailureCode,
       "gsmpSessionDiscontinuityTime": gsmpSessionDiscontinuityTime,
       "gsmpSessionStartUptime": gsmpSessionStartUptime,
       "gsmpSessionStatSentMessages": gsmpSessionStatSentMessages,
       "gsmpSessionStatFailureInds": gsmpSessionStatFailureInds,
       "gsmpSessionStatReceivedMessages": gsmpSessionStatReceivedMessages,
       "gsmpSessionStatReceivedFailures": gsmpSessionStatReceivedFailures,
       "gsmpSessionStatPortUpEvents": gsmpSessionStatPortUpEvents,
       "gsmpSessionStatPortDownEvents": gsmpSessionStatPortDownEvents,
       "gsmpSessionStatInvLabelEvents": gsmpSessionStatInvLabelEvents,
       "gsmpSessionStatNewPortEvents": gsmpSessionStatNewPortEvents,
       "gsmpSessionStatDeadPortEvents": gsmpSessionStatDeadPortEvents,
       "gsmpSessionStatAdjUpdateEvents": gsmpSessionStatAdjUpdateEvents,
       "gsmpNotificationsObjects": gsmpNotificationsObjects,
       "gsmpEventPort": gsmpEventPort,
       "gsmpEventPortSessionNumber": gsmpEventPortSessionNumber,
       "gsmpEventSequenceNumber": gsmpEventSequenceNumber,
       "gsmpEventLabel": gsmpEventLabel,
       "gsmpConformance": gsmpConformance,
       "gsmpGroups": gsmpGroups,
       "gsmpGeneralGroup": gsmpGeneralGroup,
       "gsmpControllerGroup": gsmpControllerGroup,
       "gsmpSwitchGroup": gsmpSwitchGroup,
       "gsmpAtmEncapGroup": gsmpAtmEncapGroup,
       "gsmpTcpIpEncapGroup": gsmpTcpIpEncapGroup,
       "gsmpNotificationObjectsGroup": gsmpNotificationObjectsGroup,
       "gsmpNotificationsGroup": gsmpNotificationsGroup,
       "gsmpCompliances": gsmpCompliances,
       "gsmpModuleCompliance": gsmpModuleCompliance}
)
