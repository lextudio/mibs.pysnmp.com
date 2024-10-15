# SNMP MIB module (HARMONIC-INC-NSG9000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HARMONIC-INC-NSG9000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:01 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 NotificationType,
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
    "NotificationType",
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

_HarmonicInc_ObjectIdentity = ObjectIdentity
harmonicInc = _HarmonicInc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563)
)
_HOids_ObjectIdentity = ObjectIdentity
hOids = _HOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1)
)
_HModuleOids_ObjectIdentity = ObjectIdentity
hModuleOids = _HModuleOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1)
)
_HSystemOid_ObjectIdentity = ObjectIdentity
hSystemOid = _HSystemOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1, 1)
)
_HPlatformOid_ObjectIdentity = ObjectIdentity
hPlatformOid = _HPlatformOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1, 2)
)
_HGbePortOid_ObjectIdentity = ObjectIdentity
hGbePortOid = _HGbePortOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1, 3)
)
_HSlotOid_ObjectIdentity = ObjectIdentity
hSlotOid = _HSlotOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1, 4)
)
_HRfModuleOid_ObjectIdentity = ObjectIdentity
hRfModuleOid = _HRfModuleOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1, 5)
)
_HRfPortOid_ObjectIdentity = ObjectIdentity
hRfPortOid = _HRfPortOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1, 6)
)
_HQamChannelOid_ObjectIdentity = ObjectIdentity
hQamChannelOid = _HQamChannelOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 1, 7)
)
_HTraps_ObjectIdentity = ObjectIdentity
hTraps = _HTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2)
)
_HObjects_ObjectIdentity = ObjectIdentity
hObjects = _HObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 2)
)
_HSystem_ObjectIdentity = ObjectIdentity
hSystem = _HSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 2, 1)
)
_HTrapTimeLastGenerated_Type = TimeTicks
_HTrapTimeLastGenerated_Object = MibScalar
hTrapTimeLastGenerated = _HTrapTimeLastGenerated_Object(
    (1, 3, 6, 1, 4, 1, 1563, 2, 1, 3),
    _HTrapTimeLastGenerated_Type()
)
hTrapTimeLastGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hTrapTimeLastGenerated.setStatus("mandatory")
_HTrapForwardTable_Object = MibTable
hTrapForwardTable = _HTrapForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 1563, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hTrapForwardTable.setStatus("mandatory")
_HTrapForwardEntry_Object = MibTableRow
hTrapForwardEntry = _HTrapForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1563, 2, 1, 4, 1)
)
hTrapForwardEntry.setIndexNames(
    (0, "HARMONIC-INC-NSG9000-MIB", "hTrapDestAddr"),
)
if mibBuilder.loadTexts:
    hTrapForwardEntry.setStatus("mandatory")
_HTrapDestAddr_Type = IpAddress
_HTrapDestAddr_Object = MibTableColumn
hTrapDestAddr = _HTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1563, 2, 1, 4, 1, 1),
    _HTrapDestAddr_Type()
)
hTrapDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hTrapDestAddr.setStatus("mandatory")


class _HTrapDestAddrStatus_Type(Integer32):
    """Custom type hTrapDestAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_HTrapDestAddrStatus_Type.__name__ = "Integer32"
_HTrapDestAddrStatus_Object = MibTableColumn
hTrapDestAddrStatus = _HTrapDestAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1563, 2, 1, 4, 1, 2),
    _HTrapDestAddrStatus_Type()
)
hTrapDestAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTrapDestAddrStatus.setStatus("mandatory")
_HTrapFields_ObjectIdentity = ObjectIdentity
hTrapFields = _HTrapFields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 3)
)
_HAlarmStatus_ObjectIdentity = ObjectIdentity
hAlarmStatus = _HAlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 3, 1)
)
_HAlarmSeverity_ObjectIdentity = ObjectIdentity
hAlarmSeverity = _HAlarmSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 3, 2)
)
_HAlarmDesc_ObjectIdentity = ObjectIdentity
hAlarmDesc = _HAlarmDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1563, 3, 3)
)

# Managed Objects groups


# Notification objects

hPlatformTempFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 1)
)
hPlatformTempFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformTempFailTrap.setStatus(
        ""
    )

hPlatformVoltageFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 2)
)
hPlatformVoltageFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformVoltageFailTrap.setStatus(
        ""
    )

hPlatformFan1FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 3)
)
hPlatformFan1FailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformFan1FailTrap.setStatus(
        ""
    )

hPlatformFan2FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 4)
)
hPlatformFan2FailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformFan2FailTrap.setStatus(
        ""
    )

hPlatformFan3FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 5)
)
hPlatformFan3FailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformFan3FailTrap.setStatus(
        ""
    )

hPlatformFan4FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 6)
)
hPlatformFan4FailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformFan4FailTrap.setStatus(
        ""
    )

hPlatformPS1VoltageFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 7)
)
hPlatformPS1VoltageFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformPS1VoltageFailTrap.setStatus(
        ""
    )

hPlatformPS2VoltageFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 8)
)
hPlatformPS2VoltageFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformPS2VoltageFailTrap.setStatus(
        ""
    )

hPlatformR6ConnLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 9)
)
hPlatformR6ConnLossTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformR6ConnLossTrap.setStatus(
        ""
    )

hPlatformD6ConnLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 10)
)
hPlatformD6ConnLossTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPlatformD6ConnLossTrap.setStatus(
        ""
    )

hGbePortLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 11)
)
hGbePortLinkDownTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hGbePortLinkDownTrap.setStatus(
        ""
    )

hRfModuleHwFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 12)
)
hRfModuleHwFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hRfModuleHwFailTrap.setStatus(
        ""
    )

hRfModuleTempFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 13)
)
hRfModuleTempFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hRfModuleTempFailTrap.setStatus(
        ""
    )

hRfPortHwFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 14)
)
hRfPortHwFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hRfPortHwFailTrap.setStatus(
        ""
    )

hRfPortTempFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 15)
)
hRfPortTempFailTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hRfPortTempFailTrap.setStatus(
        ""
    )

hQamChanneOverflowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 16)
)
hQamChanneOverflowTrap.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hQamChanneOverflowTrap.setStatus(
        ""
    )

hServicePatMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 17)
)
hServicePatMissing.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hServicePatMissing.setStatus(
        ""
    )

hServicePmtMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 18)
)
hServicePmtMissing.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hServicePmtMissing.setStatus(
        ""
    )

hSwitchToAlternateSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 19)
)
hSwitchToAlternateSource.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hSwitchToAlternateSource.setStatus(
        ""
    )

hPassThroughSourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 20)
)
hPassThroughSourceFailure.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPassThroughSourceFailure.setStatus(
        ""
    )

hPidRemuxSourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 21)
)
hPidRemuxSourceFailure.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hPidRemuxSourceFailure.setStatus(
        ""
    )

hDtiCardMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 22)
)
hDtiCardMissing.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hDtiCardMissing.setStatus(
        ""
    )

hMcECMMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 23)
)
hMcECMMissing.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hMcECMMissing.setStatus(
        ""
    )

hMcECMNearingExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 24)
)
hMcECMNearingExpiration.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hMcECMNearingExpiration.setStatus(
        ""
    )

hMcECMExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 25)
)
hMcECMExpired.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hMcECMExpired.setStatus(
        ""
    )

hDtiClientLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 26)
)
hDtiClientLinkDown.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hDtiClientLinkDown.setStatus(
        ""
    )

hDtiClientNotLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1563, 1, 2, 0, 27)
)
hDtiClientNotLocked.setObjects(
      *(("HARMONIC-INC-NSG9000-MIB", "hAlarmStatus"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmSeverity"),
        ("HARMONIC-INC-NSG9000-MIB", "hAlarmDesc"),
        ("ENTITY-MIB", "entPhysicalIndex"))
)
if mibBuilder.loadTexts:
    hDtiClientNotLocked.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HARMONIC-INC-NSG9000-MIB",
    **{"harmonicInc": harmonicInc,
       "hOids": hOids,
       "hModuleOids": hModuleOids,
       "hSystemOid": hSystemOid,
       "hPlatformOid": hPlatformOid,
       "hGbePortOid": hGbePortOid,
       "hSlotOid": hSlotOid,
       "hRfModuleOid": hRfModuleOid,
       "hRfPortOid": hRfPortOid,
       "hQamChannelOid": hQamChannelOid,
       "hTraps": hTraps,
       "hPlatformTempFailTrap": hPlatformTempFailTrap,
       "hPlatformVoltageFailTrap": hPlatformVoltageFailTrap,
       "hPlatformFan1FailTrap": hPlatformFan1FailTrap,
       "hPlatformFan2FailTrap": hPlatformFan2FailTrap,
       "hPlatformFan3FailTrap": hPlatformFan3FailTrap,
       "hPlatformFan4FailTrap": hPlatformFan4FailTrap,
       "hPlatformPS1VoltageFailTrap": hPlatformPS1VoltageFailTrap,
       "hPlatformPS2VoltageFailTrap": hPlatformPS2VoltageFailTrap,
       "hPlatformR6ConnLossTrap": hPlatformR6ConnLossTrap,
       "hPlatformD6ConnLossTrap": hPlatformD6ConnLossTrap,
       "hGbePortLinkDownTrap": hGbePortLinkDownTrap,
       "hRfModuleHwFailTrap": hRfModuleHwFailTrap,
       "hRfModuleTempFailTrap": hRfModuleTempFailTrap,
       "hRfPortHwFailTrap": hRfPortHwFailTrap,
       "hRfPortTempFailTrap": hRfPortTempFailTrap,
       "hQamChanneOverflowTrap": hQamChanneOverflowTrap,
       "hServicePatMissing": hServicePatMissing,
       "hServicePmtMissing": hServicePmtMissing,
       "hSwitchToAlternateSource": hSwitchToAlternateSource,
       "hPassThroughSourceFailure": hPassThroughSourceFailure,
       "hPidRemuxSourceFailure": hPidRemuxSourceFailure,
       "hDtiCardMissing": hDtiCardMissing,
       "hMcECMMissing": hMcECMMissing,
       "hMcECMNearingExpiration": hMcECMNearingExpiration,
       "hMcECMExpired": hMcECMExpired,
       "hDtiClientLinkDown": hDtiClientLinkDown,
       "hDtiClientNotLocked": hDtiClientNotLocked,
       "hObjects": hObjects,
       "hSystem": hSystem,
       "hTrapTimeLastGenerated": hTrapTimeLastGenerated,
       "hTrapForwardTable": hTrapForwardTable,
       "hTrapForwardEntry": hTrapForwardEntry,
       "hTrapDestAddr": hTrapDestAddr,
       "hTrapDestAddrStatus": hTrapDestAddrStatus,
       "hTrapFields": hTrapFields,
       "hAlarmStatus": hAlarmStatus,
       "hAlarmSeverity": hAlarmSeverity,
       "hAlarmDesc": hAlarmDesc}
)
