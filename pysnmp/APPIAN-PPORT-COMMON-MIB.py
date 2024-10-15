# SNMP MIB module (APPIAN-PPORT-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PPORT-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:38 2024
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

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 AcPortNumber,
 AcSlotNumber,
 acPport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "AcPortNumber",
    "AcSlotNumber",
    "acPport")

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

acPportCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1)
)
acPportCommon.setRevisions(
        ("1900-03-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcInterfaceTable_Object = MibTable
acInterfaceTable = _AcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    acInterfaceTable.setStatus("current")
_AcInterfaceEntry_Object = MibTableRow
acInterfaceEntry = _AcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1)
)
acInterfaceEntry.setIndexNames(
    (0, "APPIAN-PPORT-COMMON-MIB", "acInterfaceNodeId"),
    (0, "APPIAN-PPORT-COMMON-MIB", "acInterfaceSlot"),
    (0, "APPIAN-PPORT-COMMON-MIB", "acInterfacePort"),
)
if mibBuilder.loadTexts:
    acInterfaceEntry.setStatus("current")
_AcInterfaceNodeId_Type = AcNodeId
_AcInterfaceNodeId_Object = MibTableColumn
acInterfaceNodeId = _AcInterfaceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 1),
    _AcInterfaceNodeId_Type()
)
acInterfaceNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acInterfaceNodeId.setStatus("current")
_AcInterfaceSlot_Type = AcSlotNumber
_AcInterfaceSlot_Object = MibTableColumn
acInterfaceSlot = _AcInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 2),
    _AcInterfaceSlot_Type()
)
acInterfaceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acInterfaceSlot.setStatus("current")
_AcInterfacePort_Type = AcPortNumber
_AcInterfacePort_Object = MibTableColumn
acInterfacePort = _AcInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 3),
    _AcInterfacePort_Type()
)
acInterfacePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acInterfacePort.setStatus("current")


class _AcInterfaceType_Type(Integer32):
    """Custom type acInterfaceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 2),
          ("ds3", 3),
          ("enet", 1),
          ("sonet", 4),
          ("unknown", 0))
    )


_AcInterfaceType_Type.__name__ = "Integer32"
_AcInterfaceType_Object = MibTableColumn
acInterfaceType = _AcInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 4),
    _AcInterfaceType_Type()
)
acInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acInterfaceType.setStatus("current")
_AcInterfaceChannel_Type = Integer32
_AcInterfaceChannel_Object = MibTableColumn
acInterfaceChannel = _AcInterfaceChannel_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 5),
    _AcInterfaceChannel_Type()
)
acInterfaceChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acInterfaceChannel.setStatus("current")
_AcInterfaceIfIndex_Type = Integer32
_AcInterfaceIfIndex_Object = MibTableColumn
acInterfaceIfIndex = _AcInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 6),
    _AcInterfaceIfIndex_Type()
)
acInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceIfIndex.setStatus("current")


class _AcInterfaceAdminStatus_Type(AcAdminStatus):
    """Custom type acInterfaceAdminStatus based on AcAdminStatus"""


_AcInterfaceAdminStatus_Object = MibTableColumn
acInterfaceAdminStatus = _AcInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 7),
    _AcInterfaceAdminStatus_Type()
)
acInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acInterfaceAdminStatus.setStatus("current")
_AcInterfaceOpStatus_Type = AcOpStatus
_AcInterfaceOpStatus_Object = MibTableColumn
acInterfaceOpStatus = _AcInterfaceOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 8),
    _AcInterfaceOpStatus_Type()
)
acInterfaceOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceOpStatus.setStatus("current")


class _AcInterfaceInterfaceName_Type(DisplayString):
    """Custom type acInterfaceInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcInterfaceInterfaceName_Type.__name__ = "DisplayString"
_AcInterfaceInterfaceName_Object = MibTableColumn
acInterfaceInterfaceName = _AcInterfaceInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 9),
    _AcInterfaceInterfaceName_Type()
)
acInterfaceInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInterfaceInterfaceName.setStatus("current")
_AcInterfaceSubscriberId_Type = Integer32
_AcInterfaceSubscriberId_Object = MibTableColumn
acInterfaceSubscriberId = _AcInterfaceSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 10),
    _AcInterfaceSubscriberId_Type()
)
acInterfaceSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acInterfaceSubscriberId.setStatus("current")


class _AcInterfaceSubscriberName_Type(DisplayString):
    """Custom type acInterfaceSubscriberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcInterfaceSubscriberName_Type.__name__ = "DisplayString"
_AcInterfaceSubscriberName_Object = MibTableColumn
acInterfaceSubscriberName = _AcInterfaceSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 11),
    _AcInterfaceSubscriberName_Type()
)
acInterfaceSubscriberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acInterfaceSubscriberName.setStatus("current")
_AcInterfaceResellerId_Type = Integer32
_AcInterfaceResellerId_Object = MibTableColumn
acInterfaceResellerId = _AcInterfaceResellerId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 12),
    _AcInterfaceResellerId_Type()
)
acInterfaceResellerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acInterfaceResellerId.setStatus("current")


class _AcInterfaceResellerName_Type(DisplayString):
    """Custom type acInterfaceResellerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcInterfaceResellerName_Type.__name__ = "DisplayString"
_AcInterfaceResellerName_Object = MibTableColumn
acInterfaceResellerName = _AcInterfaceResellerName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 1, 1, 1, 13),
    _AcInterfaceResellerName_Type()
)
acInterfaceResellerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acInterfaceResellerName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PPORT-COMMON-MIB",
    **{"acPportCommon": acPportCommon,
       "acInterfaceTable": acInterfaceTable,
       "acInterfaceEntry": acInterfaceEntry,
       "acInterfaceNodeId": acInterfaceNodeId,
       "acInterfaceSlot": acInterfaceSlot,
       "acInterfacePort": acInterfacePort,
       "acInterfaceType": acInterfaceType,
       "acInterfaceChannel": acInterfaceChannel,
       "acInterfaceIfIndex": acInterfaceIfIndex,
       "acInterfaceAdminStatus": acInterfaceAdminStatus,
       "acInterfaceOpStatus": acInterfaceOpStatus,
       "acInterfaceInterfaceName": acInterfaceInterfaceName,
       "acInterfaceSubscriberId": acInterfaceSubscriberId,
       "acInterfaceSubscriberName": acInterfaceSubscriberName,
       "acInterfaceResellerId": acInterfaceResellerId,
       "acInterfaceResellerName": acInterfaceResellerName}
)
