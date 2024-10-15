# SNMP MIB module (APPIAN-TIMESLOTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-TIMESLOTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:46 2024
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
 acOsap) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "acOsap")

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

acTimeSlots = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5)
)
acTimeSlots.setRevisions(
        ("1900-08-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcTimeSlotTable_Object = MibTable
acTimeSlotTable = _AcTimeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1)
)
if mibBuilder.loadTexts:
    acTimeSlotTable.setStatus("current")
_AcTimeSlotEntry_Object = MibTableRow
acTimeSlotEntry = _AcTimeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1)
)
acTimeSlotEntry.setIndexNames(
    (0, "APPIAN-TIMESLOTS-MIB", "acTimeSlotIndex"),
)
if mibBuilder.loadTexts:
    acTimeSlotEntry.setStatus("current")
_AcTimeSlotIndex_Type = Integer32
_AcTimeSlotIndex_Object = MibTableColumn
acTimeSlotIndex = _AcTimeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 1),
    _AcTimeSlotIndex_Type()
)
acTimeSlotIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTimeSlotIndex.setStatus("current")


class _AcTimeSlotAdminStatus_Type(AcAdminStatus):
    """Custom type acTimeSlotAdminStatus based on AcAdminStatus"""


_AcTimeSlotAdminStatus_Object = MibTableColumn
acTimeSlotAdminStatus = _AcTimeSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 2),
    _AcTimeSlotAdminStatus_Type()
)
acTimeSlotAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotAdminStatus.setStatus("current")


class _AcTimeSlotWidth_Type(Integer32):
    """Custom type acTimeSlotWidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sts1", 3),
          ("sts12", 5),
          ("sts3", 4),
          ("sts48", 6),
          ("unknown", 0),
          ("vt1dot5", 1),
          ("vtgroup", 2))
    )


_AcTimeSlotWidth_Type.__name__ = "Integer32"
_AcTimeSlotWidth_Object = MibTableColumn
acTimeSlotWidth = _AcTimeSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 3),
    _AcTimeSlotWidth_Type()
)
acTimeSlotWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotWidth.setStatus("current")


class _AcTimeSlotOuterIndex_Type(Integer32):
    """Custom type acTimeSlotOuterIndex based on Integer32"""
    defaultValue = 0


_AcTimeSlotOuterIndex_Object = MibTableColumn
acTimeSlotOuterIndex = _AcTimeSlotOuterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 4),
    _AcTimeSlotOuterIndex_Type()
)
acTimeSlotOuterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotOuterIndex.setStatus("current")


class _AcTimeSlotNumber_Type(Integer32):
    """Custom type acTimeSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AcTimeSlotNumber_Type.__name__ = "Integer32"
_AcTimeSlotNumber_Object = MibTableColumn
acTimeSlotNumber = _AcTimeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 5),
    _AcTimeSlotNumber_Type()
)
acTimeSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotNumber.setStatus("current")


class _AcTimeSlotPathProtectionMode_Type(Integer32):
    """Custom type acTimeSlotPathProtectionMode based on Integer32"""
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
        *(("not-used", 0),
          ("odp", 2),
          ("unprotected", 1),
          ("upsr", 3))
    )


_AcTimeSlotPathProtectionMode_Type.__name__ = "Integer32"
_AcTimeSlotPathProtectionMode_Object = MibTableColumn
acTimeSlotPathProtectionMode = _AcTimeSlotPathProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 6),
    _AcTimeSlotPathProtectionMode_Type()
)
acTimeSlotPathProtectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotPathProtectionMode.setStatus("current")


class _AcTimeSlotChassisSlot_Type(Integer32):
    """Custom type acTimeSlotChassisSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("slot1", 1),
          ("slot2", 2))
    )


_AcTimeSlotChassisSlot_Type.__name__ = "Integer32"
_AcTimeSlotChassisSlot_Object = MibTableColumn
acTimeSlotChassisSlot = _AcTimeSlotChassisSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 7),
    _AcTimeSlotChassisSlot_Type()
)
acTimeSlotChassisSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotChassisSlot.setStatus("current")


class _AcTimeSlotPort_Type(Integer32):
    """Custom type acTimeSlotPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("port1", 1),
          ("port2", 2))
    )


_AcTimeSlotPort_Type.__name__ = "Integer32"
_AcTimeSlotPort_Object = MibTableColumn
acTimeSlotPort = _AcTimeSlotPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 8),
    _AcTimeSlotPort_Type()
)
acTimeSlotPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotPort.setStatus("current")


class _AcTimeSlotPayloadConfiguration_Type(Integer32):
    """Custom type acTimeSlotPayloadConfiguration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ring-interconnect", 2),
          ("ring-only", 1),
          ("unprovisioned", 0))
    )


_AcTimeSlotPayloadConfiguration_Type.__name__ = "Integer32"
_AcTimeSlotPayloadConfiguration_Object = MibTableColumn
acTimeSlotPayloadConfiguration = _AcTimeSlotPayloadConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 9),
    _AcTimeSlotPayloadConfiguration_Type()
)
acTimeSlotPayloadConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotPayloadConfiguration.setStatus("current")


class _AcTimeSlotPayloadLineType_Type(Integer32):
    """Custom type acTimeSlotPayloadLineType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ds1D4", 2),
          ("ds1ESF", 1),
          ("ds1tdm", 5),
          ("ds3CbitParity", 4),
          ("ds3M23", 3),
          ("not-applicable", 0))
    )


_AcTimeSlotPayloadLineType_Type.__name__ = "Integer32"
_AcTimeSlotPayloadLineType_Object = MibTableColumn
acTimeSlotPayloadLineType = _AcTimeSlotPayloadLineType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 10),
    _AcTimeSlotPayloadLineType_Type()
)
acTimeSlotPayloadLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotPayloadLineType.setStatus("current")


class _AcTimeSlotPayloadMgmtDLType_Type(Integer32):
    """Custom type acTimeSlotPayloadMgmtDLType based on Integer32"""
    defaultValue = 1


_AcTimeSlotPayloadMgmtDLType_Object = MibTableColumn
acTimeSlotPayloadMgmtDLType = _AcTimeSlotPayloadMgmtDLType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 11),
    _AcTimeSlotPayloadMgmtDLType_Type()
)
acTimeSlotPayloadMgmtDLType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotPayloadMgmtDLType.setStatus("current")


class _AcTimeSlotChannelConfiguration_Type(Integer32):
    """Custom type acTimeSlotChannelConfiguration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-and-tdm", 1),
          ("tdm-only", 2),
          ("unprovisioned", 0))
    )


_AcTimeSlotChannelConfiguration_Type.__name__ = "Integer32"
_AcTimeSlotChannelConfiguration_Object = MibTableColumn
acTimeSlotChannelConfiguration = _AcTimeSlotChannelConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 12),
    _AcTimeSlotChannelConfiguration_Type()
)
acTimeSlotChannelConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotChannelConfiguration.setStatus("current")


class _AcTimeSlotPayloadContent_Type(Integer32):
    """Custom type acTimeSlotPayloadContent based on Integer32"""
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
        *(("data", 1),
          ("tdm", 2),
          ("unequipped", 3),
          ("unprovisioned", 0))
    )


_AcTimeSlotPayloadContent_Type.__name__ = "Integer32"
_AcTimeSlotPayloadContent_Object = MibTableColumn
acTimeSlotPayloadContent = _AcTimeSlotPayloadContent_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 5, 1, 1, 13),
    _AcTimeSlotPayloadContent_Type()
)
acTimeSlotPayloadContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTimeSlotPayloadContent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-TIMESLOTS-MIB",
    **{"acTimeSlots": acTimeSlots,
       "acTimeSlotTable": acTimeSlotTable,
       "acTimeSlotEntry": acTimeSlotEntry,
       "acTimeSlotIndex": acTimeSlotIndex,
       "acTimeSlotAdminStatus": acTimeSlotAdminStatus,
       "acTimeSlotWidth": acTimeSlotWidth,
       "acTimeSlotOuterIndex": acTimeSlotOuterIndex,
       "acTimeSlotNumber": acTimeSlotNumber,
       "acTimeSlotPathProtectionMode": acTimeSlotPathProtectionMode,
       "acTimeSlotChassisSlot": acTimeSlotChassisSlot,
       "acTimeSlotPort": acTimeSlotPort,
       "acTimeSlotPayloadConfiguration": acTimeSlotPayloadConfiguration,
       "acTimeSlotPayloadLineType": acTimeSlotPayloadLineType,
       "acTimeSlotPayloadMgmtDLType": acTimeSlotPayloadMgmtDLType,
       "acTimeSlotChannelConfiguration": acTimeSlotChannelConfiguration,
       "acTimeSlotPayloadContent": acTimeSlotPayloadContent}
)
