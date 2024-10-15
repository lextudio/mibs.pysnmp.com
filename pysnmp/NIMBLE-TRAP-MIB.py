# SNMP MIB module (NIMBLE-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NIMBLE-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:30 2024
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

(nimble,) = mibBuilder.importSymbols(
    "NIMBLE-MIB",
    "nimble")

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

nimble_traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2)
)
nimble_traps.setRevisions(
        ("2014-06-13 00:00",
         "2014-05-09 00:00",
         "2012-07-12 00:00",
         "2012-06-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrapObjects_ObjectIdentity = ObjectIdentity
trapObjects = _TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1)
)
_Trapvariables_ObjectIdentity = ObjectIdentity
trapvariables = _Trapvariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1)
)


class _TrapMsg_Type(DisplayString):
    """Custom type trapMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapMsg_Type.__name__ = "DisplayString"
_TrapMsg_Object = MibScalar
trapMsg = _TrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 1),
    _TrapMsg_Type()
)
trapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMsg.setStatus("current")
_TrapSeverity_Type = DisplayString
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 2),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_TrapOriginatorName_Type = DisplayString
_TrapOriginatorName_Object = MibScalar
trapOriginatorName = _TrapOriginatorName_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 3),
    _TrapOriginatorName_Type()
)
trapOriginatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorName.setStatus("current")
_TrapOriginatorSerialNumber_Type = DisplayString
_TrapOriginatorSerialNumber_Object = MibScalar
trapOriginatorSerialNumber = _TrapOriginatorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 4),
    _TrapOriginatorSerialNumber_Type()
)
trapOriginatorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorSerialNumber.setStatus("current")
_TrapOriginatorGroupName_Type = DisplayString
_TrapOriginatorGroupName_Object = MibScalar
trapOriginatorGroupName = _TrapOriginatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 5),
    _TrapOriginatorGroupName_Type()
)
trapOriginatorGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorGroupName.setStatus("current")
_TrapOriginatorGroupID_Type = DisplayString
_TrapOriginatorGroupID_Object = MibScalar
trapOriginatorGroupID = _TrapOriginatorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 6),
    _TrapOriginatorGroupID_Type()
)
trapOriginatorGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOriginatorGroupID.setStatus("current")
_TrapTarget_Type = DisplayString
_TrapTarget_Object = MibScalar
trapTarget = _TrapTarget_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 7),
    _TrapTarget_Type()
)
trapTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTarget.setStatus("current")
_TrapTargetType_Type = DisplayString
_TrapTargetType_Object = MibScalar
trapTargetType = _TrapTargetType_Object(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 1, 8),
    _TrapTargetType_Type()
)
trapTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTargetType.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2)
)

# Managed Objects groups


# Notification objects

nimbleDsdRedEntry0101Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 101)
)
nimbleDsdRedEntry0101Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdRedEntry0101Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdSpaceRedExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 102)
)
nimbleDsdSpaceRedExit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceRedExit.setStatus(
        "current"
    )

nimbleDsdSpaceCrit0103Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 103)
)
nimbleDsdSpaceCrit0103Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceCrit0103Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdSpaceUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 104)
)
nimbleDsdSpaceUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceUtilizationHigh.setStatus(
        "current"
    )

nimbleDsdSpaceUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 105)
)
nimbleDsdSpaceUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceUtilizationOk.setStatus(
        "current"
    )

nimbleDsdSpaceUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 106)
)
nimbleDsdSpaceUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceUtilizationCrit.setStatus(
        "current"
    )

nimbleDsdSpaceRedEntry0107Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 107)
)
nimbleDsdSpaceRedEntry0107Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceRedEntry0107Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdSpaceCrit0110Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 110)
)
nimbleDsdSpaceCrit0110Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceCrit0110Deprecated.setStatus(
        "obsolete"
    )

nimbleDsdSpaceRedEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 111)
)
nimbleDsdSpaceRedEntry.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceRedEntry.setStatus(
        "current"
    )

nimbleDsdSpaceCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 112)
)
nimbleDsdSpaceCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDsdSpaceCrit.setStatus(
        "current"
    )

nimbleCtrlrException = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2001)
)
nimbleCtrlrException.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrException.setStatus(
        "current"
    )

nimbleCtrlrTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2002)
)
nimbleCtrlrTakeover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrTakeover.setStatus(
        "current"
    )

nimbleCtrlrStandbyAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2003)
)
nimbleCtrlrStandbyAvail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyAvail.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2004)
)
nimbleCtrlrStandbyUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavail.setStatus(
        "current"
    )

nimbleCtrlrExcessiveRestarts = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2005)
)
nimbleCtrlrExcessiveRestarts.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrExcessiveRestarts.setStatus(
        "current"
    )

nimbleServiceReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2006)
)
nimbleServiceReboot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceReboot.setStatus(
        "current"
    )

nimbleUserReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2007)
)
nimbleUserReboot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserReboot.setStatus(
        "current"
    )

nimbleUserRebootFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2008)
)
nimbleUserRebootFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserRebootFailed.setStatus(
        "current"
    )

nimbleUserHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2009)
)
nimbleUserHalt.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserHalt.setStatus(
        "current"
    )

nimbleUserHaltFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2010)
)
nimbleUserHaltFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserHaltFailed.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavailInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2011)
)
nimbleCtrlrStandbyUnavailInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailInfo.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavailWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2012)
)
nimbleCtrlrStandbyUnavailWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailWarn.setStatus(
        "current"
    )

nimbleCtrlrExceptionWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2013)
)
nimbleCtrlrExceptionWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrExceptionWarn.setStatus(
        "current"
    )

nimbleCtrlrExceptionCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2014)
)
nimbleCtrlrExceptionCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrExceptionCrit.setStatus(
        "current"
    )

nimbleCtrlrStandbyUnavailWarnTimeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2015)
)
nimbleCtrlrStandbyUnavailWarnTimeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailWarnTimeDeprecated.setStatus(
        "obsolete"
    )

nimbleCtrlrStandbyUnavailWarnTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2016)
)
nimbleCtrlrStandbyUnavailWarnTime.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrStandbyUnavailWarnTime.setStatus(
        "current"
    )

nimbleCtrlrTakeoverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2017)
)
nimbleCtrlrTakeoverWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrTakeoverWarn.setStatus(
        "current"
    )

nimbleCtrlrFailoverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2018)
)
nimbleCtrlrFailoverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailoverDeprecated.setStatus(
        "obsolete"
    )

nimbleCtrlrFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2019)
)
nimbleCtrlrFailover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrFailover.setStatus(
        "current"
    )

nimbleServiceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2101)
)
nimbleServiceStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceStarted.setStatus(
        "current"
    )

nimbleServiceDeadRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2102)
)
nimbleServiceDeadRestart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceDeadRestart.setStatus(
        "current"
    )

nimbleServiceDeadNoRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2103)
)
nimbleServiceDeadNoRestart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceDeadNoRestart.setStatus(
        "current"
    )

nimbleServiceCreateTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2104)
)
nimbleServiceCreateTunnel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceCreateTunnel.setStatus(
        "current"
    )

nimbleServiceTerminateTunnel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2105)
)
nimbleServiceTerminateTunnel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceTerminateTunnel.setStatus(
        "current"
    )

nimbleServiceEssentialStoppedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2106)
)
nimbleServiceEssentialStoppedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEssentialStoppedDeprecated.setStatus(
        "obsolete"
    )

nimbleServiceEssentialStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2107)
)
nimbleServiceEssentialStopped.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEssentialStopped.setStatus(
        "current"
    )

nimbleServiceEmailAlertFailedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2108)
)
nimbleServiceEmailAlertFailedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEmailAlertFailedDeprecated.setStatus(
        "obsolete"
    )

nimbleServiceEmailAlertFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 2109)
)
nimbleServiceEmailAlertFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleServiceEmailAlertFailed.setStatus(
        "current"
    )

nimbleTestDbg = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5000)
)
nimbleTestDbg.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestDbg.setStatus(
        "current"
    )

nimbleTestInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5001)
)
nimbleTestInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestInfo.setStatus(
        "current"
    )

nimbleTestErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5002)
)
nimbleTestErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestErr.setStatus(
        "current"
    )

nimbleTestNot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5003)
)
nimbleTestNot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestNot.setStatus(
        "current"
    )

nimbleTestNoteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5004)
)
nimbleTestNoteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestNoteDeprecated.setStatus(
        "obsolete"
    )

nimbleTestWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5005)
)
nimbleTestWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestWarn.setStatus(
        "current"
    )

nimbleTestCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5006)
)
nimbleTestCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestCrit.setStatus(
        "current"
    )

nimbleTestNote = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 5007)
)
nimbleTestNote.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTestNote.setStatus(
        "current"
    )

nimbleUpdateUnpackFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6000)
)
nimbleUpdateUnpackFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnpackFail.setStatus(
        "current"
    )

nimbleUpdateStartedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6001)
)
nimbleUpdateStartedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateStartedDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateRevert = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6002)
)
nimbleUpdateRevert.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateRevert.setStatus(
        "current"
    )

nimbleUpdateSuccessDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6003)
)
nimbleUpdateSuccessDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateSuccessDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6004)
)
nimbleUpdateRollback.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateRollback.setStatus(
        "current"
    )

nimbleUpdatePrecheckFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6005)
)
nimbleUpdatePrecheckFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePrecheckFail.setStatus(
        "current"
    )

nimbleUpdateFailMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6007)
)
nimbleUpdateFailMsg.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailMsg.setStatus(
        "current"
    )

nimbleUpdateUnpackStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6008)
)
nimbleUpdateUnpackStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnpackStarted.setStatus(
        "current"
    )

nimbleUpdateUnpackDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6009)
)
nimbleUpdateUnpackDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnpackDone.setStatus(
        "current"
    )

nimbleUpdateSwitchRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6010)
)
nimbleUpdateSwitchRoot.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateSwitchRoot.setStatus(
        "current"
    )

nimbleUpdateDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6011)
)
nimbleUpdateDownloadFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateDownloadFailed.setStatus(
        "current"
    )

nimbleUpdateFailTmpFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6012)
)
nimbleUpdateFailTmpFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailTmpFsFull.setStatus(
        "current"
    )

nimbleUpdateFailScratchFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6013)
)
nimbleUpdateFailScratchFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailScratchFsFull.setStatus(
        "current"
    )

nimbleUpdateFailVarFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6014)
)
nimbleUpdateFailVarFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailVarFsFull.setStatus(
        "current"
    )

nimbleUpdateFailConfigFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6015)
)
nimbleUpdateFailConfigFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailConfigFsFull.setStatus(
        "current"
    )

nimbleUpdateFailUsbFsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6016)
)
nimbleUpdateFailUsbFsFull.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateFailUsbFsFull.setStatus(
        "current"
    )

nimbleUpdatePkgNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6017)
)
nimbleUpdatePkgNotFound.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgNotFound.setStatus(
        "current"
    )

nimbleUpdatePkgWrongSig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6018)
)
nimbleUpdatePkgWrongSig.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgWrongSig.setStatus(
        "current"
    )

nimbleUpdatePkgWrongCksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6019)
)
nimbleUpdatePkgWrongCksum.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdatePkgWrongCksum.setStatus(
        "current"
    )

nimbleUpdateNetDegradeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6020)
)
nimbleUpdateNetDegradeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateNetDegradeDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateDisallowSoloDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6021)
)
nimbleUpdateDisallowSoloDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateDisallowSoloDeprecated.setStatus(
        "obsolete"
    )

nimbleUpdateDisallowSolo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6022)
)
nimbleUpdateDisallowSolo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateDisallowSolo.setStatus(
        "current"
    )

nimbleUpdateNetDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6023)
)
nimbleUpdateNetDegrade.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateNetDegrade.setStatus(
        "current"
    )

nimbleUpdateRaidDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6024)
)
nimbleUpdateRaidDegrade.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateRaidDegrade.setStatus(
        "current"
    )

nimbleUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6025)
)
nimbleUpdateStarted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateStarted.setStatus(
        "current"
    )

nimbleUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6026)
)
nimbleUpdateSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateSuccess.setStatus(
        "current"
    )

nimbleUpdateArrayUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6501)
)
nimbleUpdateArrayUnreachable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateArrayUnreachable.setStatus(
        "current"
    )

nimbleUpdateArrayFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6502)
)
nimbleUpdateArrayFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateArrayFailed.setStatus(
        "current"
    )

nimbleUpdateArrayTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 6503)
)
nimbleUpdateArrayTimedOut.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateArrayTimedOut.setStatus(
        "current"
    )

nimbleArrayUnreachableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10010)
)
nimbleArrayUnreachableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUnreachableDeprecated.setStatus(
        "obsolete"
    )

nimbleArrayReachableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10011)
)
nimbleArrayReachableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayReachableDeprecated.setStatus(
        "obsolete"
    )

nimbleArrayUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10012)
)
nimbleArrayUnreachable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayUnreachable.setStatus(
        "current"
    )

nimbleArrayReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10013)
)
nimbleArrayReachable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleArrayReachable.setStatus(
        "current"
    )

nimbleUserClearedSysCache = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10101)
)
nimbleUserClearedSysCache.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUserClearedSysCache.setStatus(
        "current"
    )

nimbleVolSpcCurWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10200)
)
nimbleVolSpcCurWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurWarningUp.setStatus(
        "current"
    )

nimbleVolSpcCurWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10201)
)
nimbleVolSpcCurWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurWarningDown.setStatus(
        "current"
    )

nimbleVolSpcCurQuotaUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10202)
)
nimbleVolSpcCurQuotaUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurQuotaUp.setStatus(
        "current"
    )

nimbleVolSpcCurQuotaDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10203)
)
nimbleVolSpcCurQuotaDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcCurQuotaDown.setStatus(
        "current"
    )

nimbleVolSpcSnapWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10204)
)
nimbleVolSpcSnapWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapWarningUp.setStatus(
        "current"
    )

nimbleVolSpcSnapWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10205)
)
nimbleVolSpcSnapWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapWarningDown.setStatus(
        "current"
    )

nimbleVolSpcSnapQuotaUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10206)
)
nimbleVolSpcSnapQuotaUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapQuotaUp.setStatus(
        "current"
    )

nimbleVolSpcSnapQuotaDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10207)
)
nimbleVolSpcSnapQuotaDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSpcSnapQuotaDown.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10208)
)
nimbleGmVolSpcCurCritUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUp.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10209)
)
nimbleGmVolSpcCurCritDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritDown.setStatus(
        "current"
    )

nimbleGmSnapSpcCurCritUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10210)
)
nimbleGmSnapSpcCurCritUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritUp.setStatus(
        "current"
    )

nimbleGmSnapSpcCurCritDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10211)
)
nimbleGmSnapSpcCurCritDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritDown.setStatus(
        "current"
    )

nimbleGmVolSpcCurQuotaOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10212)
)
nimbleGmVolSpcCurQuotaOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaOffline.setStatus(
        "current"
    )

nimbleGmVolSpcCurQuotaSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10213)
)
nimbleGmVolSpcCurQuotaSet.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaSet.setStatus(
        "current"
    )

nimbleGmVolSpcSnapQuotaOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10214)
)
nimbleGmVolSpcSnapQuotaOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaOffline.setStatus(
        "current"
    )

nimbleGmVolSpcSnapQuotaSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10215)
)
nimbleGmVolSpcSnapQuotaSet.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaSet.setStatus(
        "current"
    )

nimbleGmVolSpcCurReserveOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10216)
)
nimbleGmVolSpcCurReserveOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurReserveOffline.setStatus(
        "current"
    )

nimbleGmVolSpcCurReserveSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10217)
)
nimbleGmVolSpcCurReserveSet.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurReserveSet.setStatus(
        "current"
    )

nimbleGmVolSpcSnapReserveOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10218)
)
nimbleGmVolSpcSnapReserveOffline.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapReserveOffline.setStatus(
        "current"
    )

nimbleGmVolSpcSnapReserveSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10219)
)
nimbleGmVolSpcSnapReserveSet.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapReserveSet.setStatus(
        "current"
    )

nimbleGmVolSpcCurWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10220)
)
nimbleGmVolSpcCurWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurWarningUp.setStatus(
        "current"
    )

nimbleGmVolSpcCurWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10221)
)
nimbleGmVolSpcCurWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurWarningDown.setStatus(
        "current"
    )

nimbleGmVolSpcCurQuotaUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10222)
)
nimbleGmVolSpcCurQuotaUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaUp.setStatus(
        "current"
    )

nimbleGmVolSpcCurQuotaDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10223)
)
nimbleGmVolSpcCurQuotaDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaDown.setStatus(
        "current"
    )

nimbleGmVolSpcSnapWarningUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10224)
)
nimbleGmVolSpcSnapWarningUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapWarningUp.setStatus(
        "current"
    )

nimbleGmVolSpcSnapWarningDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10225)
)
nimbleGmVolSpcSnapWarningDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapWarningDown.setStatus(
        "current"
    )

nimbleGmVolSpcSnapQuotaUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10226)
)
nimbleGmVolSpcSnapQuotaUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaUp.setStatus(
        "current"
    )

nimbleGmVolSpcSnapQuotaDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10227)
)
nimbleGmVolSpcSnapQuotaDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaDown.setStatus(
        "current"
    )

nimbleVolAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10228)
)
nimbleVolAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolAttrSyncDelay.setStatus(
        "current"
    )

nimbleGmPoolArrAssgnDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10229)
)
nimbleGmPoolArrAssgnDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrAssgnDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolArrUnassgnDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10230)
)
nimbleGmPoolArrUnassgnDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgnDeprecated.setStatus(
        "obsolete"
    )

nimbleGmVolSpcCurCritUpUnlim = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10231)
)
nimbleGmVolSpcCurCritUpUnlim.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUpUnlim.setStatus(
        "current"
    )

nimbleGmSnapSpcCurCritUpUnlim = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10232)
)
nimbleGmSnapSpcCurCritUpUnlim.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritUpUnlim.setStatus(
        "current"
    )

nimbleGmVolSpcReserveUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10233)
)
nimbleGmVolSpcReserveUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcReserveUp.setStatus(
        "current"
    )

nimbleGmVolSpcReserveDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10234)
)
nimbleGmVolSpcReserveDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcReserveDown.setStatus(
        "current"
    )

nimbleGmSnapSpcReserveUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10235)
)
nimbleGmSnapSpcReserveUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcReserveUp.setStatus(
        "current"
    )

nimbleGmSnapSpcReserveDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10236)
)
nimbleGmSnapSpcReserveDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcReserveDown.setStatus(
        "current"
    )

nimbleGmPoolMrgDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10240)
)
nimbleGmPoolMrgDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolMrgDeprecated.setStatus(
        "obsolete"
    )

nimbleVolAttrSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10241)
)
nimbleVolAttrSyncSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolAttrSyncSuccess.setStatus(
        "current"
    )

nimbleSnapAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10242)
)
nimbleSnapAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSnapAttrSyncDelay.setStatus(
        "current"
    )

nimbleSnapAttrSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10243)
)
nimbleSnapAttrSyncSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSnapAttrSyncSuccess.setStatus(
        "current"
    )

nimbleGroupAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10244)
)
nimbleGroupAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGroupAttrSyncDelay.setStatus(
        "current"
    )

nimbleGroupAttrSyncComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10245)
)
nimbleGroupAttrSyncComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGroupAttrSyncComplete.setStatus(
        "current"
    )

nimbleGlCtrlrAttrSyncDelayDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10246)
)
nimbleGlCtrlrAttrSyncDelayDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncDelayDeprecated.setStatus(
        "obsolete"
    )

nimbleGlCtrlrAttrSyncCompleteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10247)
)
nimbleGlCtrlrAttrSyncCompleteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncCompleteDeprecated.setStatus(
        "obsolete"
    )

nimbleGlCtrlrAttrSyncDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10248)
)
nimbleGlCtrlrAttrSyncDelay.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncDelay.setStatus(
        "current"
    )

nimbleGlCtrlrAttrSyncComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10249)
)
nimbleGlCtrlrAttrSyncComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGlCtrlrAttrSyncComplete.setStatus(
        "current"
    )

nimbleVolMoveComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10250)
)
nimbleVolMoveComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolMoveComplete.setStatus(
        "current"
    )

nimbleVolMoveAbortComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10251)
)
nimbleVolMoveAbortComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolMoveAbortComplete.setStatus(
        "current"
    )

nimbleGmPoolArrUnassgnCompleteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10252)
)
nimbleGmPoolArrUnassgnCompleteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgnCompleteDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolArrUnassgnComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10253)
)
nimbleGmPoolArrUnassgnComplete.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgnComplete.setStatus(
        "current"
    )

nimbleGmPoolArrAssgn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10256)
)
nimbleGmPoolArrAssgn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrAssgn.setStatus(
        "current"
    )

nimbleGmPoolArrUnassgn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10257)
)
nimbleGmPoolArrUnassgn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolArrUnassgn.setStatus(
        "current"
    )

nimbleGmPoolMrg = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10260)
)
nimbleGmPoolMrg.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolMrg.setStatus(
        "current"
    )

nimbleGmVolSpcCurCritUpNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10261)
)
nimbleGmVolSpcCurCritUpNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurCritUpNonWritable.setStatus(
        "current"
    )

nimbleGmVolSpcCurQuotaNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10262)
)
nimbleGmVolSpcCurQuotaNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurQuotaNonWritable.setStatus(
        "current"
    )

nimbleGmSnapSpcCurCritUpNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10263)
)
nimbleGmSnapSpcCurCritUpNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSnapSpcCurCritUpNonWritable.setStatus(
        "current"
    )

nimbleGmVolSpcSnapQuotaNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10264)
)
nimbleGmVolSpcSnapQuotaNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapQuotaNonWritable.setStatus(
        "current"
    )

nimbleGmVolSpcCurReserveNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10265)
)
nimbleGmVolSpcCurReserveNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcCurReserveNonWritable.setStatus(
        "current"
    )

nimbleGmVolSpcSnapReserveNonWritable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10266)
)
nimbleGmVolSpcSnapReserveNonWritable.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmVolSpcSnapReserveNonWritable.setStatus(
        "current"
    )

nimbleSchedSnapSucceededDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10300)
)
nimbleSchedSnapSucceededDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceededDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10301)
)
nimbleSchedSnapFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailed.setStatus(
        "current"
    )

nimbleSchedSnapSkippedExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10302)
)
nimbleSchedSnapSkippedExists.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSkippedExists.setStatus(
        "current"
    )

nimbleSchedSnapSkippedHandover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10303)
)
nimbleSchedSnapSkippedHandover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSkippedHandover.setStatus(
        "current"
    )

nimbleSchedSnapSucceededLagInfoDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10304)
)
nimbleSchedSnapSucceededLagInfoDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceededLagInfoDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareCredentialDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10305)
)
nimbleSchedSnapFailedVmwareCredentialDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareCredentialDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10306)
)
nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10307)
)
nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionResetDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10308)
)
nimbleSchedSnapFailedVmwareConnectionResetDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionResetDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10309)
)
nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionSocketDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10310)
)
nimbleSchedSnapFailedVmwareConnectionSocketDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionSocketDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10311)
)
nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareDisabledDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10312)
)
nimbleSchedSnapFailedVmwareDisabledDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDisabledDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareObjectnfDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10313)
)
nimbleSchedSnapFailedVmwareObjectnfDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareObjectnfDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwarePermissionDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10314)
)
nimbleSchedSnapFailedVmwarePermissionDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwarePermissionDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareUkhostDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10315)
)
nimbleSchedSnapFailedVmwareUkhostDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUkhostDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareEncodingPlainDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10316)
)
nimbleSchedSnapFailedVmwareEncodingPlainDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareEncodingPlainDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareNullDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10317)
)
nimbleSchedSnapFailedVmwareNullDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareNullDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareDcnotfoundDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10318)
)
nimbleSchedSnapFailedVmwareDcnotfoundDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDcnotfoundDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareVolsnemptyDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10319)
)
nimbleSchedSnapFailedVmwareVolsnemptyDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareVolsnemptyDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareUnknownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10320)
)
nimbleSchedSnapFailedVmwareUnknownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareBsizeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10321)
)
nimbleSchedSnapFailedVmwareBsizeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareBsizeDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10322)
)
nimbleSchedSnapSucceeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceeded.setStatus(
        "current"
    )

nimbleSchedSnapSucceededLagInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10323)
)
nimbleSchedSnapSucceededLagInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapSucceededLagInfo.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10324)
)
nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareTimeoutDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10325)
)
nimbleSchedSnapFailedVmwareTimeoutDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareTimeoutDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10326)
)
nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10327)
)
nimbleSchedSnapFallback.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFallback.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwarePermissionPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10340)
)
nimbleSchedSnapFailedVmwarePermissionPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwarePermissionPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareObjectnfPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10341)
)
nimbleSchedSnapFailedVmwareObjectnfPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareObjectnfPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareEncodingPlainPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10342)
)
nimbleSchedSnapFailedVmwareEncodingPlainPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareEncodingPlainPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareNullPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10343)
)
nimbleSchedSnapFailedVmwareNullPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareNullPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareDcnotfoundPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10344)
)
nimbleSchedSnapFailedVmwareDcnotfoundPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDcnotfoundPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareVolsnemptyPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10345)
)
nimbleSchedSnapFailedVmwareVolsnemptyPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareVolsnemptyPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10346)
)
nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated.setStatus(
        "obsolete"
    )

nimbleSchedSnapFailedVmwareBsizePerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10347)
)
nimbleSchedSnapFailedVmwareBsizePerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareBsizePerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareDisabledPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10348)
)
nimbleSchedSnapFailedVmwareDisabledPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareDisabledPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareTimeoutPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10349)
)
nimbleSchedSnapFailedVmwareTimeoutPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareTimeoutPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10350)
)
nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10351)
)
nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareInvalidVcenter = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10352)
)
nimbleSchedSnapFailedVmwareInvalidVcenter.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareInvalidVcenter.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10353)
)
nimbleSchedSnapFailedVmwareBusy.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareBusy.setStatus(
        "current"
    )

nimbleSchedSnapFailedVssIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10354)
)
nimbleSchedSnapFailedVssIncompatible.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVssIncompatible.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareCredentialNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10355)
)
nimbleSchedSnapFailedVmwareCredentialNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareCredentialNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionTimeoutNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10356)
)
nimbleSchedSnapFailedVmwareConnectionTimeoutNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionTimeoutNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionRefusedNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10357)
)
nimbleSchedSnapFailedVmwareConnectionRefusedNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionRefusedNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionResetNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10358)
)
nimbleSchedSnapFailedVmwareConnectionResetNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionResetNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionNorouteNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10359)
)
nimbleSchedSnapFailedVmwareConnectionNorouteNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionNorouteNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionSocketNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10360)
)
nimbleSchedSnapFailedVmwareConnectionSocketNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionSocketNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionUnreachableNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10361)
)
nimbleSchedSnapFailedVmwareConnectionUnreachableNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionUnreachableNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUkhostNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10362)
)
nimbleSchedSnapFailedVmwareUkhostNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUkhostNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareConnectionUnknownNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10363)
)
nimbleSchedSnapFailedVmwareConnectionUnknownNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareConnectionUnknownNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareTimeoutNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10364)
)
nimbleSchedSnapFailedVmwareTimeoutNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareTimeoutNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUnknownNw = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10365)
)
nimbleSchedSnapFailedVmwareUnknownNw.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownNw.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareUnknownPerVm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10366)
)
nimbleSchedSnapFailedVmwareUnknownPerVm.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareUnknownPerVm.setStatus(
        "current"
    )

nimbleSchedSnapFailedVmwareQuiescingVmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10367)
)
nimbleSchedSnapFailedVmwareQuiescingVmFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSchedSnapFailedVmwareQuiescingVmFailed.setStatus(
        "current"
    )

nimbleGmSpaceReserveWarnUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10401)
)
nimbleGmSpaceReserveWarnUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveWarnUp.setStatus(
        "current"
    )

nimbleGmSpaceReserveWarnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10402)
)
nimbleGmSpaceReserveWarnDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveWarnDown.setStatus(
        "current"
    )

nimbleGmSpaceReserveCritUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10403)
)
nimbleGmSpaceReserveCritUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveCritUp.setStatus(
        "current"
    )

nimbleGmSpaceReserveCritDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10404)
)
nimbleGmSpaceReserveCritDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceReserveCritDown.setStatus(
        "current"
    )

nimbleGmSpaceUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10405)
)
nimbleGmSpaceUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationOk.setStatus(
        "current"
    )

nimbleGmSpaceUtilizationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10406)
)
nimbleGmSpaceUtilizationInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationInfo.setStatus(
        "current"
    )

nimbleGmSpaceUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10407)
)
nimbleGmSpaceUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationHigh.setStatus(
        "current"
    )

nimbleGmSpaceUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10408)
)
nimbleGmSpaceUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmSpaceUtilizationCrit.setStatus(
        "current"
    )

nimbleGmPoolSpaceReserveWarnUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10409)
)
nimbleGmPoolSpaceReserveWarnUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveWarnDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10410)
)
nimbleGmPoolSpaceReserveWarnDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveCritUpDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10411)
)
nimbleGmPoolSpaceReserveCritUpDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritUpDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveCritDownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10412)
)
nimbleGmPoolSpaceReserveCritDownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritDownDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationOkDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10413)
)
nimbleGmPoolSpaceUtilizationOkDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationOkDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationInfoDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10414)
)
nimbleGmPoolSpaceUtilizationInfoDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationInfoDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationHighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10415)
)
nimbleGmPoolSpaceUtilizationHighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationHighDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceUtilizationCritDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10416)
)
nimbleGmPoolSpaceUtilizationCritDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationCritDeprecated.setStatus(
        "obsolete"
    )

nimbleGmPoolSpaceReserveWarnUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10417)
)
nimbleGmPoolSpaceReserveWarnUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnUp.setStatus(
        "current"
    )

nimbleGmPoolSpaceReserveWarnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10418)
)
nimbleGmPoolSpaceReserveWarnDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveWarnDown.setStatus(
        "current"
    )

nimbleGmPoolSpaceReserveCritUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10419)
)
nimbleGmPoolSpaceReserveCritUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritUp.setStatus(
        "current"
    )

nimbleGmPoolSpaceReserveCritDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10420)
)
nimbleGmPoolSpaceReserveCritDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceReserveCritDown.setStatus(
        "current"
    )

nimbleGmPoolSpaceUtilizationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10421)
)
nimbleGmPoolSpaceUtilizationOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationOk.setStatus(
        "current"
    )

nimbleGmPoolSpaceUtilizationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10422)
)
nimbleGmPoolSpaceUtilizationInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationInfo.setStatus(
        "current"
    )

nimbleGmPoolSpaceUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10423)
)
nimbleGmPoolSpaceUtilizationHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationHigh.setStatus(
        "current"
    )

nimbleGmPoolSpaceUtilizationCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10424)
)
nimbleGmPoolSpaceUtilizationCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmPoolSpaceUtilizationCrit.setStatus(
        "current"
    )

nimbleLimitMaxOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10500)
)
nimbleLimitMaxOver.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxOver.setStatus(
        "current"
    )

nimbleLimitMaxUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10501)
)
nimbleLimitMaxUnder.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitMaxUnder.setStatus(
        "current"
    )

nimbleLimitWarnOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10502)
)
nimbleLimitWarnOver.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnOver.setStatus(
        "current"
    )

nimbleLimitWarnUnder = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 10503)
)
nimbleLimitWarnUnder.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleLimitWarnUnder.setStatus(
        "current"
    )

nimbleReplSnapcollSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11000)
)
nimbleReplSnapcollSucceeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapcollSucceeded.setStatus(
        "current"
    )

nimbleReplSnapcollDelayedInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11001)
)
nimbleReplSnapcollDelayedInfo.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapcollDelayedInfo.setStatus(
        "current"
    )

nimbleReplSnapcollDelayedWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11002)
)
nimbleReplSnapcollDelayedWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapcollDelayedWarn.setStatus(
        "current"
    )

nimbleReplPartnerSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11003)
)
nimbleReplPartnerSyncFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerSyncFail.setStatus(
        "current"
    )

nimbleReplBranchPinned = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11004)
)
nimbleReplBranchPinned.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplBranchPinned.setStatus(
        "current"
    )

nimbleReplHandoverCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11005)
)
nimbleReplHandoverCompleted.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplHandoverCompleted.setStatus(
        "current"
    )

nimbleReplMultiArrayGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11006)
)
nimbleReplMultiArrayGroup.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplMultiArrayGroup.setStatus(
        "current"
    )

nimbleReplPartnerMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11007)
)
nimbleReplPartnerMisconfiguration.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerMisconfiguration.setStatus(
        "current"
    )

nimbleReplSnapshotCorrectedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11008)
)
nimbleReplSnapshotCorrectedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrectedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplCbrRequestedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11009)
)
nimbleReplCbrRequestedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrRequestedDeprecated.setStatus(
        "obsolete"
    )

nimbleReplCbrNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11010)
)
nimbleReplCbrNeeded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrNeeded.setStatus(
        "current"
    )

nimbleReplSnapshotCorrectedDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11011)
)
nimbleReplSnapshotCorrectedDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrectedDeprecated2.setStatus(
        "current"
    )

nimbleReplCbrRequestedDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11012)
)
nimbleReplCbrRequestedDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrRequestedDeprecated2.setStatus(
        "current"
    )

nimbleReplPartnerAuthFailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11013)
)
nimbleReplPartnerAuthFailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerAuthFailDeprecated.setStatus(
        "obsolete"
    )

nimbleReplSnapshotCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11014)
)
nimbleReplSnapshotCorrected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplSnapshotCorrected.setStatus(
        "current"
    )

nimbleReplCbrRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11015)
)
nimbleReplCbrRequested.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplCbrRequested.setStatus(
        "current"
    )

nimbleReplPartnerAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 11016)
)
nimbleReplPartnerAuthFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleReplPartnerAuthFail.setStatus(
        "current"
    )

nimbleOvertempShutdownDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12000)
)
nimbleOvertempShutdownDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleOvertempShutdownDeprecated.setStatus(
        "obsolete"
    )

nimbleCtrlrOvertempDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12001)
)
nimbleCtrlrOvertempDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrOvertempDeprecated.setStatus(
        "obsolete"
    )

nimbleBackplaneOvertempDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12002)
)
nimbleBackplaneOvertempDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBackplaneOvertempDeprecated.setStatus(
        "obsolete"
    )

nimbleIscsiErroneousItorConns = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12057)
)
nimbleIscsiErroneousItorConns.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiErroneousItorConns.setStatus(
        "current"
    )

nimbleDiskFailedCritDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12100)
)
nimbleDiskFailedCritDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFailedCritDeprecated.setStatus(
        "obsolete"
    )

nimbleDiskFailedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12101)
)
nimbleDiskFailedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskFailedDeprecated.setStatus(
        "obsolete"
    )

nimbleDiskAbsentDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12102)
)
nimbleDiskAbsentDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskAbsentDeprecated.setStatus(
        "obsolete"
    )

nimbleDiskAddedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12103)
)
nimbleDiskAddedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskAddedDeprecated.setStatus(
        "obsolete"
    )

nimbleDiskRemovedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12104)
)
nimbleDiskRemovedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskRemovedDeprecated.setStatus(
        "obsolete"
    )

nimbleSsdFailedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12105)
)
nimbleSsdFailedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdFailedDeprecated.setStatus(
        "obsolete"
    )

nimbleSsdAbsentDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12106)
)
nimbleSsdAbsentDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAbsentDeprecated.setStatus(
        "obsolete"
    )

nimbleSsdAddedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12107)
)
nimbleSsdAddedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAddedDeprecated.setStatus(
        "obsolete"
    )

nimbleSsdRemovedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12108)
)
nimbleSsdRemovedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdRemovedDeprecated.setStatus(
        "obsolete"
    )

nimbleDiskInvalidLabel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12109)
)
nimbleDiskInvalidLabel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskInvalidLabel.setStatus(
        "current"
    )

nimbleSsdInvalidLabel = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12110)
)
nimbleSsdInvalidLabel.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdInvalidLabel.setStatus(
        "current"
    )

nimbleDiskSizeMismatchDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12111)
)
nimbleDiskSizeMismatchDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskSizeMismatchDeprecated.setStatus(
        "obsolete"
    )

nimbleHddFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12112)
)
nimbleHddFailedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedV2.setStatus(
        "current"
    )

nimbleHddAbsentV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12113)
)
nimbleHddAbsentV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddAbsentV2.setStatus(
        "current"
    )

nimbleHddAddedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12114)
)
nimbleHddAddedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddAddedV2.setStatus(
        "current"
    )

nimbleHddRemovedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12115)
)
nimbleHddRemovedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddRemovedV2.setStatus(
        "current"
    )

nimbleSsdFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12116)
)
nimbleSsdFailedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdFailedV2.setStatus(
        "current"
    )

nimbleSsdAbsentV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12117)
)
nimbleSsdAbsentV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAbsentV2.setStatus(
        "current"
    )

nimbleSsdAddedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12118)
)
nimbleSsdAddedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAddedV2.setStatus(
        "current"
    )

nimbleSsdRemovedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12119)
)
nimbleSsdRemovedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdRemovedV2.setStatus(
        "current"
    )

nimbleSsdLastOne = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12120)
)
nimbleSsdLastOne.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdLastOne.setStatus(
        "current"
    )

nimbleHddFailedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12121)
)
nimbleHddFailedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedV3.setStatus(
        "current"
    )

nimbleHddAddedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12122)
)
nimbleHddAddedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddAddedV3.setStatus(
        "current"
    )

nimbleHddRemovedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12123)
)
nimbleHddRemovedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddRemovedV3.setStatus(
        "current"
    )

nimbleSsdFailedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12124)
)
nimbleSsdFailedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdFailedV3.setStatus(
        "current"
    )

nimbleSsdAddedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12125)
)
nimbleSsdAddedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdAddedV3.setStatus(
        "current"
    )

nimbleSsdRemovedV3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12126)
)
nimbleSsdRemovedV3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdRemovedV3.setStatus(
        "current"
    )

nimbleDiskSizeMismatchV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12127)
)
nimbleDiskSizeMismatchV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleDiskSizeMismatchV2.setStatus(
        "current"
    )

nimbleSsdSizeMismatchV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12128)
)
nimbleSsdSizeMismatchV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSsdSizeMismatchV2.setStatus(
        "current"
    )

nimbleHddFailedAfsDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12129)
)
nimbleHddFailedAfsDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedAfsDeprecated.setStatus(
        "obsolete"
    )

nimbleHddFailedAfs = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12130)
)
nimbleHddFailedAfs.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleHddFailedAfs.setStatus(
        "current"
    )

nimbleIpIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12200)
)
nimbleIpIfDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDown.setStatus(
        "current"
    )

nimbleIpIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12201)
)
nimbleIpIfUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfUp.setStatus(
        "current"
    )

nimbleIpIfGroupUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12202)
)
nimbleIpIfGroupUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfGroupUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfDataUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12203)
)
nimbleIpIfDataUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDataUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfCantFailoverDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12204)
)
nimbleIpIfCantFailoverDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfCantFailoverDeprecated.setStatus(
        "obsolete"
    )

nimbleSubnetNicMigrationDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12205)
)
nimbleSubnetNicMigrationDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSubnetNicMigrationDeprecated.setStatus(
        "obsolete"
    )

nimbleSubnetNicMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12206)
)
nimbleSubnetNicMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSubnetNicMissingDeprecated.setStatus(
        "obsolete"
    )

nimbleIpNicMigrationDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12207)
)
nimbleIpNicMigrationDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpNicMigrationDeprecated.setStatus(
        "obsolete"
    )

nimbleIpNicMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12208)
)
nimbleIpNicMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpNicMissingDeprecated.setStatus(
        "obsolete"
    )

nimbleRouteNicMigrationDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12209)
)
nimbleRouteNicMigrationDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRouteNicMigrationDeprecated.setStatus(
        "obsolete"
    )

nimbleRouteNicMissingDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12210)
)
nimbleRouteNicMissingDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRouteNicMissingDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12211)
)
nimbleIpIfFailover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfFailover.setStatus(
        "current"
    )

nimbleIpDupFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12212)
)
nimbleIpDupFound.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpDupFound.setStatus(
        "current"
    )

nimbleIpIfDiscoveryUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12213)
)
nimbleIpIfDiscoveryUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDiscoveryUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfTargetUnavailDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12214)
)
nimbleIpIfTargetUnavailDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfTargetUnavailDeprecated.setStatus(
        "obsolete"
    )

nimbleIpIfGroupUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12215)
)
nimbleIpIfGroupUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfGroupUnavail.setStatus(
        "current"
    )

nimbleIpIfDiscoveryUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12216)
)
nimbleIpIfDiscoveryUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDiscoveryUnavail.setStatus(
        "current"
    )

nimbleIpIfTargetUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12217)
)
nimbleIpIfTargetUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfTargetUnavail.setStatus(
        "current"
    )

nimbleIpIfDataUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12218)
)
nimbleIpIfDataUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfDataUnavail.setStatus(
        "current"
    )

nimbleIpIfIscsiDataUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12219)
)
nimbleIpIfIscsiDataUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfIscsiDataUnavail.setStatus(
        "current"
    )

nimbleIpIfClusterDataUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12220)
)
nimbleIpIfClusterDataUnavail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfClusterDataUnavail.setStatus(
        "current"
    )

nimbleUnresponsiveNicDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12221)
)
nimbleUnresponsiveNicDetected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUnresponsiveNicDetected.setStatus(
        "current"
    )

nimbleIpIfCantFailoverDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12222)
)
nimbleIpIfCantFailoverDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfCantFailoverDeprecated2.setStatus(
        "current"
    )

nimbleIpIfCantFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12223)
)
nimbleIpIfCantFailover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIpIfCantFailover.setStatus(
        "current"
    )

nimbleSensorLinearWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12301)
)
nimbleSensorLinearWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorLinearWarn.setStatus(
        "current"
    )

nimbleSensorLinearClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12302)
)
nimbleSensorLinearClear.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorLinearClear.setStatus(
        "current"
    )

nimbleSensorBoolWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12303)
)
nimbleSensorBoolWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorBoolWarn.setStatus(
        "current"
    )

nimbleSensorBoolClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12304)
)
nimbleSensorBoolClear.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorBoolClear.setStatus(
        "current"
    )

nimbleSensorDoesNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12305)
)
nimbleSensorDoesNotExist.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleSensorDoesNotExist.setStatus(
        "current"
    )

nimbleNvramBattDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12306)
)
nimbleNvramBattDisabled.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattDisabled.setStatus(
        "current"
    )

nimbleNvramBattDisabledCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12307)
)
nimbleNvramBattDisabledCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattDisabledCrit.setStatus(
        "current"
    )

nimbleNvramBattOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12308)
)
nimbleNvramBattOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattOk.setStatus(
        "current"
    )

nimbleTempSensorHighDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12310)
)
nimbleTempSensorHighDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDep.setStatus(
        "obsolete"
    )

nimbleTempSensorLowDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12311)
)
nimbleTempSensorLowDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorLowDep.setStatus(
        "obsolete"
    )

nimbleTempSensorOkDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12312)
)
nimbleTempSensorOkDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOkDep.setStatus(
        "obsolete"
    )

nimbleTempSensorMissingDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12313)
)
nimbleTempSensorMissingDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorMissingDep.setStatus(
        "obsolete"
    )

nimbleTempSensorOperationalDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12314)
)
nimbleTempSensorOperationalDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOperationalDep.setStatus(
        "obsolete"
    )

nimbleFanSensorHighDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12315)
)
nimbleFanSensorHighDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorHighDep.setStatus(
        "obsolete"
    )

nimbleFanSensorLowDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12316)
)
nimbleFanSensorLowDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorLowDep.setStatus(
        "obsolete"
    )

nimbleFanSensorOkDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12317)
)
nimbleFanSensorOkDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorOkDep.setStatus(
        "obsolete"
    )

nimbleFanSensorStoppedDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12318)
)
nimbleFanSensorStoppedDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorStoppedDep.setStatus(
        "obsolete"
    )

nimbleFanSensorMissingDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12319)
)
nimbleFanSensorMissingDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorMissingDep.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorFailDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12320)
)
nimblePwrSupplySensorFailDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorFailDep.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorMissingDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12321)
)
nimblePwrSupplySensorMissingDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorMissingDep.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorOkDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12322)
)
nimblePwrSupplySensorOkDep.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorOkDep.setStatus(
        "obsolete"
    )

nimbleTempSensorHighDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12323)
)
nimbleTempSensorHighDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDep2.setStatus(
        "obsolete"
    )

nimbleTempSensorLowDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12324)
)
nimbleTempSensorLowDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorLowDep2.setStatus(
        "obsolete"
    )

nimbleTempSensorOkDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12325)
)
nimbleTempSensorOkDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOkDep2.setStatus(
        "obsolete"
    )

nimbleTempSensorMissingDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12326)
)
nimbleTempSensorMissingDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorMissingDep2.setStatus(
        "obsolete"
    )

nimbleTempSensorOperationalDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12327)
)
nimbleTempSensorOperationalDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOperationalDep2.setStatus(
        "obsolete"
    )

nimbleFanSensorHighDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12328)
)
nimbleFanSensorHighDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorHighDep2.setStatus(
        "obsolete"
    )

nimbleFanSensorLowDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12329)
)
nimbleFanSensorLowDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorLowDep2.setStatus(
        "obsolete"
    )

nimbleFanSensorOkDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12330)
)
nimbleFanSensorOkDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorOkDep2.setStatus(
        "obsolete"
    )

nimbleFanSensorStoppedDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12331)
)
nimbleFanSensorStoppedDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorStoppedDep2.setStatus(
        "obsolete"
    )

nimbleFanSensorMissingDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12332)
)
nimbleFanSensorMissingDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorMissingDep2.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorFailDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12333)
)
nimblePwrSupplySensorFailDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorFailDep2.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorMissingDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12334)
)
nimblePwrSupplySensorMissingDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorMissingDep2.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorOkDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12335)
)
nimblePwrSupplySensorOkDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorOkDep2.setStatus(
        "obsolete"
    )

nimbleTempSensorHighDeprecatedDep2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12336)
)
nimbleTempSensorHighDeprecatedDep2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecatedDep2.setStatus(
        "obsolete"
    )

nimbleTempSensorLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12337)
)
nimbleTempSensorLow.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorLow.setStatus(
        "current"
    )

nimbleTempSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12338)
)
nimbleTempSensorOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOk.setStatus(
        "current"
    )

nimbleTempSensorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12339)
)
nimbleTempSensorMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorMissing.setStatus(
        "current"
    )

nimbleTempSensorOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12340)
)
nimbleTempSensorOperational.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorOperational.setStatus(
        "current"
    )

nimbleFanSensorHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12341)
)
nimbleFanSensorHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorHigh.setStatus(
        "current"
    )

nimbleFanSensorLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12342)
)
nimbleFanSensorLow.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorLow.setStatus(
        "current"
    )

nimbleFanSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12343)
)
nimbleFanSensorOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorOk.setStatus(
        "current"
    )

nimbleFanSensorStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12344)
)
nimbleFanSensorStopped.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorStopped.setStatus(
        "current"
    )

nimbleFanSensorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12345)
)
nimbleFanSensorMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFanSensorMissing.setStatus(
        "current"
    )

nimblePwrSupplySensorFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12346)
)
nimblePwrSupplySensorFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorFail.setStatus(
        "current"
    )

nimblePwrSupplySensorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12347)
)
nimblePwrSupplySensorMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorMissing.setStatus(
        "current"
    )

nimblePwrSupplySensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12348)
)
nimblePwrSupplySensorOk.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorOk.setStatus(
        "current"
    )

nimbleRaidDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12400)
)
nimbleRaidDegraded.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDegraded.setStatus(
        "current"
    )

nimbleRaidRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12401)
)
nimbleRaidRebuildStart.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildStart.setStatus(
        "current"
    )

nimbleRaidRebuildDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12402)
)
nimbleRaidRebuildDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildDone.setStatus(
        "current"
    )

nimbleRaidRebuildFailRead = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12403)
)
nimbleRaidRebuildFailRead.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFailRead.setStatus(
        "current"
    )

nimbleRaidRebuildFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12404)
)
nimbleRaidRebuildFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFail.setStatus(
        "current"
    )

nimbleRaidDisksMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12405)
)
nimbleRaidDisksMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDisksMissing.setStatus(
        "current"
    )

nimbleRaidSpare = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12406)
)
nimbleRaidSpare.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidSpare.setStatus(
        "current"
    )

nimbleRaidAssemblyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12407)
)
nimbleRaidAssemblyFailed.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidAssemblyFailed.setStatus(
        "current"
    )

nimbleRaidDegradedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12408)
)
nimbleRaidDegradedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDegradedV2.setStatus(
        "current"
    )

nimbleRaidRebuildStartV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12409)
)
nimbleRaidRebuildStartV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildStartV2.setStatus(
        "current"
    )

nimbleRaidRebuildDoneV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12410)
)
nimbleRaidRebuildDoneV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildDoneV2.setStatus(
        "current"
    )

nimbleRaidRebuildFailReadV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12411)
)
nimbleRaidRebuildFailReadV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFailReadV2.setStatus(
        "current"
    )

nimbleRaidRebuildFailV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12412)
)
nimbleRaidRebuildFailV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildFailV2.setStatus(
        "current"
    )

nimbleRaidDisksMissingV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12413)
)
nimbleRaidDisksMissingV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidDisksMissingV2.setStatus(
        "current"
    )

nimbleRaidSpareV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12414)
)
nimbleRaidSpareV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidSpareV2.setStatus(
        "current"
    )

nimbleRaidAssemblyFailedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12415)
)
nimbleRaidAssemblyFailedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidAssemblyFailedV2.setStatus(
        "current"
    )

nimbleRaidRebuildScheduledV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12416)
)
nimbleRaidRebuildScheduledV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildScheduledV2.setStatus(
        "current"
    )

nimbleRaidRebuildStopV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12417)
)
nimbleRaidRebuildStopV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleRaidRebuildStopV2.setStatus(
        "current"
    )

nimbleIscsiMultiInitiatorDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12500)
)
nimbleIscsiMultiInitiatorDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiMultiInitiatorDeprecated.setStatus(
        "obsolete"
    )

nimbleIscsiConnHardLimitDeprecated1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12501)
)
nimbleIscsiConnHardLimitDeprecated1.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiConnHardLimitDeprecated1.setStatus(
        "current"
    )

nimbleIscsiUnalignedOpsDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12502)
)
nimbleIscsiUnalignedOpsDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiUnalignedOpsDeprecated.setStatus(
        "obsolete"
    )

nimbleIscsiMultiInitiator = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12503)
)
nimbleIscsiMultiInitiator.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiMultiInitiator.setStatus(
        "current"
    )

nimbleIscsiConnHardLimitDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12504)
)
nimbleIscsiConnHardLimitDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiConnHardLimitDeprecated2.setStatus(
        "current"
    )

nimbleIscsiUnalignedOps = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12505)
)
nimbleIscsiUnalignedOps.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiUnalignedOps.setStatus(
        "current"
    )

nimbleIscsiConnHardLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12506)
)
nimbleIscsiConnHardLimit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleIscsiConnHardLimit.setStatus(
        "current"
    )

nimbleNvramBattCharging = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12601)
)
nimbleNvramBattCharging.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattCharging.setStatus(
        "current"
    )

nimbleNvramBattCharged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12602)
)
nimbleNvramBattCharged.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramBattCharged.setStatus(
        "current"
    )

nimbleNvramFpgaVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12603)
)
nimbleNvramFpgaVersion.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramFpgaVersion.setStatus(
        "current"
    )

nimbleNvramMbeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12604)
)
nimbleNvramMbeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramMbeDeprecated.setStatus(
        "obsolete"
    )

nimbleNvramSbeDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12605)
)
nimbleNvramSbeDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramSbeDeprecated.setStatus(
        "obsolete"
    )

nimbleNvramMbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12606)
)
nimbleNvramMbe.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramMbe.setStatus(
        "current"
    )

nimbleNvramSbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12607)
)
nimbleNvramSbe.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramSbe.setStatus(
        "current"
    )

nimbleNvdimmReservedBlocksWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12608)
)
nimbleNvdimmReservedBlocksWarn.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmReservedBlocksWarn.setStatus(
        "current"
    )

nimbleNvdimmReservedBlocksCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12609)
)
nimbleNvdimmReservedBlocksCrit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmReservedBlocksCrit.setStatus(
        "current"
    )

nimbleNvdimmUltracapDischargedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12610)
)
nimbleNvdimmUltracapDischargedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmUltracapDischargedDeprecated.setStatus(
        "obsolete"
    )

nimbleNtbBadLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12611)
)
nimbleNtbBadLink.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNtbBadLink.setStatus(
        "current"
    )

nimbleNvdimmUltracapDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12612)
)
nimbleNvdimmUltracapDischarged.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvdimmUltracapDischarged.setStatus(
        "current"
    )

nimbleNvramMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12613)
)
nimbleNvramMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleNvramMissing.setStatus(
        "current"
    )

nimbleShelfCtrlrSide = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12701)
)
nimbleShelfCtrlrSide.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfCtrlrSide.setStatus(
        "current"
    )

nimbleShelfSesErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12702)
)
nimbleShelfSesErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesErr.setStatus(
        "current"
    )

nimbleShelfDiskSasLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12703)
)
nimbleShelfDiskSasLink.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskSasLink.setStatus(
        "current"
    )

nimbleShelfDiskCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12704)
)
nimbleShelfDiskCount.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskCount.setStatus(
        "current"
    )

nimbleShelfInvalidEeprom = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12705)
)
nimbleShelfInvalidEeprom.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfInvalidEeprom.setStatus(
        "current"
    )

nimbleShelfWrongSasPortDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12706)
)
nimbleShelfWrongSasPortDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfWrongSasPortDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfSasLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12707)
)
nimbleShelfSasLink.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasLink.setStatus(
        "current"
    )

nimbleShelfSasExpErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12708)
)
nimbleShelfSasExpErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasExpErr.setStatus(
        "current"
    )

nimbleShelfCtrlrLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12709)
)
nimbleShelfCtrlrLoop.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfCtrlrLoop.setStatus(
        "current"
    )

nimbleShelfMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12710)
)
nimbleShelfMissing.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfMissing.setStatus(
        "current"
    )

nimbleShelfOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12711)
)
nimbleShelfOrder.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfOrder.setStatus(
        "current"
    )

nimbleShelfSesMshipErrDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12712)
)
nimbleShelfSesMshipErrDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12713)
)
nimbleShelfFailover.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfFailover.setStatus(
        "current"
    )

nimbleShelfNewShelf = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12714)
)
nimbleShelfNewShelf.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfNewShelf.setStatus(
        "current"
    )

nimbleShelfDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12715)
)
nimbleShelfDisconnect.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDisconnect.setStatus(
        "current"
    )

nimbleShelfChassisSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12716)
)
nimbleShelfChassisSwap.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfChassisSwap.setStatus(
        "current"
    )

nimbleShelfLocIdOverLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12717)
)
nimbleShelfLocIdOverLimit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfLocIdOverLimit.setStatus(
        "current"
    )

nimbleShelfActivatedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12718)
)
nimbleShelfActivatedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfActivatedDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12719)
)
nimbleShelfReconnect.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfReconnect.setStatus(
        "current"
    )

nimbleShelfSasLinkDisabledDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12720)
)
nimbleShelfSasLinkDisabledDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasLinkDisabledDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfDiskSasLinkErrDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12721)
)
nimbleShelfDiskSasLinkErrDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskSasLinkErrDeprecated.setStatus(
        "obsolete"
    )

nimbleShelfWrongSasPortDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12730)
)
nimbleShelfWrongSasPortDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfWrongSasPortDeprecated2.setStatus(
        "current"
    )

nimbleShelfSesMshipErrDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12731)
)
nimbleShelfSesMshipErrDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated2.setStatus(
        "current"
    )

nimbleShelfSasLinkDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12732)
)
nimbleShelfSasLinkDisabled.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSasLinkDisabled.setStatus(
        "current"
    )

nimbleShelfDiskSasLinkErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12733)
)
nimbleShelfDiskSasLinkErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfDiskSasLinkErr.setStatus(
        "current"
    )

nimbleShelfWrongSasPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12734)
)
nimbleShelfWrongSasPort.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfWrongSasPort.setStatus(
        "current"
    )

nimbleShelfSesMshipErrDeprecated3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12735)
)
nimbleShelfSesMshipErrDeprecated3.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated3.setStatus(
        "current"
    )

nimbleShelfSesMshipErrDeprecated4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12736)
)
nimbleShelfSesMshipErrDeprecated4.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErrDeprecated4.setStatus(
        "current"
    )

nimbleShelfActivatedV2Deprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12737)
)
nimbleShelfActivatedV2Deprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfActivatedV2Deprecated.setStatus(
        "obsolete"
    )

nimbleShelfSesMshipErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12738)
)
nimbleShelfSesMshipErr.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfSesMshipErr.setStatus(
        "current"
    )

nimbleShelfActivatedV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12739)
)
nimbleShelfActivatedV2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleShelfActivatedV2.setStatus(
        "current"
    )

nimblePhysMemMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 12901)
)
nimblePhysMemMismatch.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePhysMemMismatch.setStatus(
        "current"
    )

nimbleVolSysLimitWarnEnter = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13101)
)
nimbleVolSysLimitWarnEnter.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSysLimitWarnEnter.setStatus(
        "current"
    )

nimbleVolSysLimitWarnExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13102)
)
nimbleVolSysLimitWarnExit.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleVolSysLimitWarnExit.setStatus(
        "current"
    )

nimbleGmTakeoverSuccessDeprecatedDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13501)
)
nimbleGmTakeoverSuccessDeprecatedDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverSuccessDeprecatedDeprecated.setStatus(
        "obsolete"
    )

nimbleGmTakeoverRejectByArrayDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13502)
)
nimbleGmTakeoverRejectByArrayDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverRejectByArrayDeprecated.setStatus(
        "obsolete"
    )

nimbleGmTakeoverRejectByArray = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13503)
)
nimbleGmTakeoverRejectByArray.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverRejectByArray.setStatus(
        "current"
    )

nimbleGmTakeoverSuccessDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13504)
)
nimbleGmTakeoverSuccessDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverSuccessDeprecated.setStatus(
        "obsolete"
    )

nimbleGmTakeoverSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13505)
)
nimbleGmTakeoverSuccess.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmTakeoverSuccess.setStatus(
        "current"
    )

nimbleGmMigrateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13506)
)
nimbleGmMigrateFailure.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmMigrateFailure.setStatus(
        "current"
    )

nimbleGmGrpMrgDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13601)
)
nimbleGmGrpMrgDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgDone.setStatus(
        "current"
    )

nimbleGmGrpQscFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13602)
)
nimbleGmGrpQscFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpQscFail.setStatus(
        "current"
    )

nimbleGmGrpMrgRollbackDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13603)
)
nimbleGmGrpMrgRollbackDone.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgRollbackDone.setStatus(
        "current"
    )

nimbleGmGrpMrgReassFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13604)
)
nimbleGmGrpMrgReassFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgReassFail.setStatus(
        "current"
    )

nimbleGmGrpMrgDbFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13605)
)
nimbleGmGrpMrgDbFail.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmGrpMrgDbFail.setStatus(
        "current"
    )

nimbleGmBinMigContAbortDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13701)
)
nimbleGmBinMigContAbortDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmBinMigContAbortDeprecated.setStatus(
        "obsolete"
    )

nimbleGmBinMigContAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 13702)
)
nimbleGmBinMigContAbort.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleGmBinMigContAbort.setStatus(
        "current"
    )

nimbleCsmodelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14000)
)
nimbleCsmodelChanged.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCsmodelChanged.setStatus(
        "current"
    )

nimbleCsmodelUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14001)
)
nimbleCsmodelUnknown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCsmodelUnknown.setStatus(
        "current"
    )

nimbleTempSensorHighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14002)
)
nimbleTempSensorHighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated.setStatus(
        "obsolete"
    )

nimbleOvertempShutdownDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14003)
)
nimbleOvertempShutdownDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleOvertempShutdownDeprecated2.setStatus(
        "current"
    )

nimbleCtrlrOvertemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14004)
)
nimbleCtrlrOvertemp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleCtrlrOvertemp.setStatus(
        "current"
    )

nimbleBackplaneOvertemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14005)
)
nimbleBackplaneOvertemp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleBackplaneOvertemp.setStatus(
        "current"
    )

nimbleTempSensorHighDeprecated2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14006)
)
nimbleTempSensorHighDeprecated2.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHighDeprecated2.setStatus(
        "current"
    )

nimbleTempSensorCrithighDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14007)
)
nimbleTempSensorCrithighDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorCrithighDeprecated.setStatus(
        "obsolete"
    )

nimblePwrSupplySensorCallsupportDeprecated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14008)
)
nimblePwrSupplySensorCallsupportDeprecated.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorCallsupportDeprecated.setStatus(
        "obsolete"
    )

nimbleOvertempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14009)
)
nimbleOvertempShutdown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleOvertempShutdown.setStatus(
        "current"
    )

nimblePwrSupplySensorCallsupport = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14010)
)
nimblePwrSupplySensorCallsupport.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimblePwrSupplySensorCallsupport.setStatus(
        "current"
    )

nimbleTempSensorHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14011)
)
nimbleTempSensorHigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorHigh.setStatus(
        "current"
    )

nimbleTempSensorCrithigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14012)
)
nimbleTempSensorCrithigh.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleTempSensorCrithigh.setStatus(
        "current"
    )

nimbleUpdateUnknownFirmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14200)
)
nimbleUpdateUnknownFirmware.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleUpdateUnknownFirmware.setStatus(
        "current"
    )

nimbleFcLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14400)
)
nimbleFcLinkUp.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcLinkUp.setStatus(
        "current"
    )

nimbleFcLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14401)
)
nimbleFcLinkDown.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcLinkDown.setStatus(
        "current"
    )

nimbleFcLinkNotConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14402)
)
nimbleFcLinkNotConnected.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleFcLinkNotConnected.setStatus(
        "current"
    )

nimbleEventPurging = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14700)
)
nimbleEventPurging.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEventPurging.setStatus(
        "current"
    )

nimbleEventWarnOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 37447, 2, 1, 2, 14701)
)
nimbleEventWarnOver.setObjects(
      *(("NIMBLE-TRAP-MIB", "trapMsg"),
        ("NIMBLE-TRAP-MIB", "trapSeverity"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorSerialNumber"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupName"),
        ("NIMBLE-TRAP-MIB", "trapOriginatorGroupID"),
        ("NIMBLE-TRAP-MIB", "trapTarget"),
        ("NIMBLE-TRAP-MIB", "trapTargetType"))
)
if mibBuilder.loadTexts:
    nimbleEventWarnOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NIMBLE-TRAP-MIB",
    **{"nimble-traps": nimble_traps,
       "trapObjects": trapObjects,
       "trapvariables": trapvariables,
       "trapMsg": trapMsg,
       "trapSeverity": trapSeverity,
       "trapOriginatorName": trapOriginatorName,
       "trapOriginatorSerialNumber": trapOriginatorSerialNumber,
       "trapOriginatorGroupName": trapOriginatorGroupName,
       "trapOriginatorGroupID": trapOriginatorGroupID,
       "trapTarget": trapTarget,
       "trapTargetType": trapTargetType,
       "traps": traps,
       "nimbleDsdRedEntry0101Deprecated": nimbleDsdRedEntry0101Deprecated,
       "nimbleDsdSpaceRedExit": nimbleDsdSpaceRedExit,
       "nimbleDsdSpaceCrit0103Deprecated": nimbleDsdSpaceCrit0103Deprecated,
       "nimbleDsdSpaceUtilizationHigh": nimbleDsdSpaceUtilizationHigh,
       "nimbleDsdSpaceUtilizationOk": nimbleDsdSpaceUtilizationOk,
       "nimbleDsdSpaceUtilizationCrit": nimbleDsdSpaceUtilizationCrit,
       "nimbleDsdSpaceRedEntry0107Deprecated": nimbleDsdSpaceRedEntry0107Deprecated,
       "nimbleDsdSpaceCrit0110Deprecated": nimbleDsdSpaceCrit0110Deprecated,
       "nimbleDsdSpaceRedEntry": nimbleDsdSpaceRedEntry,
       "nimbleDsdSpaceCrit": nimbleDsdSpaceCrit,
       "nimbleCtrlrException": nimbleCtrlrException,
       "nimbleCtrlrTakeover": nimbleCtrlrTakeover,
       "nimbleCtrlrStandbyAvail": nimbleCtrlrStandbyAvail,
       "nimbleCtrlrStandbyUnavail": nimbleCtrlrStandbyUnavail,
       "nimbleCtrlrExcessiveRestarts": nimbleCtrlrExcessiveRestarts,
       "nimbleServiceReboot": nimbleServiceReboot,
       "nimbleUserReboot": nimbleUserReboot,
       "nimbleUserRebootFailed": nimbleUserRebootFailed,
       "nimbleUserHalt": nimbleUserHalt,
       "nimbleUserHaltFailed": nimbleUserHaltFailed,
       "nimbleCtrlrStandbyUnavailInfo": nimbleCtrlrStandbyUnavailInfo,
       "nimbleCtrlrStandbyUnavailWarn": nimbleCtrlrStandbyUnavailWarn,
       "nimbleCtrlrExceptionWarn": nimbleCtrlrExceptionWarn,
       "nimbleCtrlrExceptionCrit": nimbleCtrlrExceptionCrit,
       "nimbleCtrlrStandbyUnavailWarnTimeDeprecated": nimbleCtrlrStandbyUnavailWarnTimeDeprecated,
       "nimbleCtrlrStandbyUnavailWarnTime": nimbleCtrlrStandbyUnavailWarnTime,
       "nimbleCtrlrTakeoverWarn": nimbleCtrlrTakeoverWarn,
       "nimbleCtrlrFailoverDeprecated": nimbleCtrlrFailoverDeprecated,
       "nimbleCtrlrFailover": nimbleCtrlrFailover,
       "nimbleServiceStarted": nimbleServiceStarted,
       "nimbleServiceDeadRestart": nimbleServiceDeadRestart,
       "nimbleServiceDeadNoRestart": nimbleServiceDeadNoRestart,
       "nimbleServiceCreateTunnel": nimbleServiceCreateTunnel,
       "nimbleServiceTerminateTunnel": nimbleServiceTerminateTunnel,
       "nimbleServiceEssentialStoppedDeprecated": nimbleServiceEssentialStoppedDeprecated,
       "nimbleServiceEssentialStopped": nimbleServiceEssentialStopped,
       "nimbleServiceEmailAlertFailedDeprecated": nimbleServiceEmailAlertFailedDeprecated,
       "nimbleServiceEmailAlertFailed": nimbleServiceEmailAlertFailed,
       "nimbleTestDbg": nimbleTestDbg,
       "nimbleTestInfo": nimbleTestInfo,
       "nimbleTestErr": nimbleTestErr,
       "nimbleTestNot": nimbleTestNot,
       "nimbleTestNoteDeprecated": nimbleTestNoteDeprecated,
       "nimbleTestWarn": nimbleTestWarn,
       "nimbleTestCrit": nimbleTestCrit,
       "nimbleTestNote": nimbleTestNote,
       "nimbleUpdateUnpackFail": nimbleUpdateUnpackFail,
       "nimbleUpdateStartedDeprecated": nimbleUpdateStartedDeprecated,
       "nimbleUpdateRevert": nimbleUpdateRevert,
       "nimbleUpdateSuccessDeprecated": nimbleUpdateSuccessDeprecated,
       "nimbleUpdateRollback": nimbleUpdateRollback,
       "nimbleUpdatePrecheckFail": nimbleUpdatePrecheckFail,
       "nimbleUpdateFailMsg": nimbleUpdateFailMsg,
       "nimbleUpdateUnpackStarted": nimbleUpdateUnpackStarted,
       "nimbleUpdateUnpackDone": nimbleUpdateUnpackDone,
       "nimbleUpdateSwitchRoot": nimbleUpdateSwitchRoot,
       "nimbleUpdateDownloadFailed": nimbleUpdateDownloadFailed,
       "nimbleUpdateFailTmpFsFull": nimbleUpdateFailTmpFsFull,
       "nimbleUpdateFailScratchFsFull": nimbleUpdateFailScratchFsFull,
       "nimbleUpdateFailVarFsFull": nimbleUpdateFailVarFsFull,
       "nimbleUpdateFailConfigFsFull": nimbleUpdateFailConfigFsFull,
       "nimbleUpdateFailUsbFsFull": nimbleUpdateFailUsbFsFull,
       "nimbleUpdatePkgNotFound": nimbleUpdatePkgNotFound,
       "nimbleUpdatePkgWrongSig": nimbleUpdatePkgWrongSig,
       "nimbleUpdatePkgWrongCksum": nimbleUpdatePkgWrongCksum,
       "nimbleUpdateNetDegradeDeprecated": nimbleUpdateNetDegradeDeprecated,
       "nimbleUpdateDisallowSoloDeprecated": nimbleUpdateDisallowSoloDeprecated,
       "nimbleUpdateDisallowSolo": nimbleUpdateDisallowSolo,
       "nimbleUpdateNetDegrade": nimbleUpdateNetDegrade,
       "nimbleUpdateRaidDegrade": nimbleUpdateRaidDegrade,
       "nimbleUpdateStarted": nimbleUpdateStarted,
       "nimbleUpdateSuccess": nimbleUpdateSuccess,
       "nimbleUpdateArrayUnreachable": nimbleUpdateArrayUnreachable,
       "nimbleUpdateArrayFailed": nimbleUpdateArrayFailed,
       "nimbleUpdateArrayTimedOut": nimbleUpdateArrayTimedOut,
       "nimbleArrayUnreachableDeprecated": nimbleArrayUnreachableDeprecated,
       "nimbleArrayReachableDeprecated": nimbleArrayReachableDeprecated,
       "nimbleArrayUnreachable": nimbleArrayUnreachable,
       "nimbleArrayReachable": nimbleArrayReachable,
       "nimbleUserClearedSysCache": nimbleUserClearedSysCache,
       "nimbleVolSpcCurWarningUp": nimbleVolSpcCurWarningUp,
       "nimbleVolSpcCurWarningDown": nimbleVolSpcCurWarningDown,
       "nimbleVolSpcCurQuotaUp": nimbleVolSpcCurQuotaUp,
       "nimbleVolSpcCurQuotaDown": nimbleVolSpcCurQuotaDown,
       "nimbleVolSpcSnapWarningUp": nimbleVolSpcSnapWarningUp,
       "nimbleVolSpcSnapWarningDown": nimbleVolSpcSnapWarningDown,
       "nimbleVolSpcSnapQuotaUp": nimbleVolSpcSnapQuotaUp,
       "nimbleVolSpcSnapQuotaDown": nimbleVolSpcSnapQuotaDown,
       "nimbleGmVolSpcCurCritUp": nimbleGmVolSpcCurCritUp,
       "nimbleGmVolSpcCurCritDown": nimbleGmVolSpcCurCritDown,
       "nimbleGmSnapSpcCurCritUp": nimbleGmSnapSpcCurCritUp,
       "nimbleGmSnapSpcCurCritDown": nimbleGmSnapSpcCurCritDown,
       "nimbleGmVolSpcCurQuotaOffline": nimbleGmVolSpcCurQuotaOffline,
       "nimbleGmVolSpcCurQuotaSet": nimbleGmVolSpcCurQuotaSet,
       "nimbleGmVolSpcSnapQuotaOffline": nimbleGmVolSpcSnapQuotaOffline,
       "nimbleGmVolSpcSnapQuotaSet": nimbleGmVolSpcSnapQuotaSet,
       "nimbleGmVolSpcCurReserveOffline": nimbleGmVolSpcCurReserveOffline,
       "nimbleGmVolSpcCurReserveSet": nimbleGmVolSpcCurReserveSet,
       "nimbleGmVolSpcSnapReserveOffline": nimbleGmVolSpcSnapReserveOffline,
       "nimbleGmVolSpcSnapReserveSet": nimbleGmVolSpcSnapReserveSet,
       "nimbleGmVolSpcCurWarningUp": nimbleGmVolSpcCurWarningUp,
       "nimbleGmVolSpcCurWarningDown": nimbleGmVolSpcCurWarningDown,
       "nimbleGmVolSpcCurQuotaUp": nimbleGmVolSpcCurQuotaUp,
       "nimbleGmVolSpcCurQuotaDown": nimbleGmVolSpcCurQuotaDown,
       "nimbleGmVolSpcSnapWarningUp": nimbleGmVolSpcSnapWarningUp,
       "nimbleGmVolSpcSnapWarningDown": nimbleGmVolSpcSnapWarningDown,
       "nimbleGmVolSpcSnapQuotaUp": nimbleGmVolSpcSnapQuotaUp,
       "nimbleGmVolSpcSnapQuotaDown": nimbleGmVolSpcSnapQuotaDown,
       "nimbleVolAttrSyncDelay": nimbleVolAttrSyncDelay,
       "nimbleGmPoolArrAssgnDeprecated": nimbleGmPoolArrAssgnDeprecated,
       "nimbleGmPoolArrUnassgnDeprecated": nimbleGmPoolArrUnassgnDeprecated,
       "nimbleGmVolSpcCurCritUpUnlim": nimbleGmVolSpcCurCritUpUnlim,
       "nimbleGmSnapSpcCurCritUpUnlim": nimbleGmSnapSpcCurCritUpUnlim,
       "nimbleGmVolSpcReserveUp": nimbleGmVolSpcReserveUp,
       "nimbleGmVolSpcReserveDown": nimbleGmVolSpcReserveDown,
       "nimbleGmSnapSpcReserveUp": nimbleGmSnapSpcReserveUp,
       "nimbleGmSnapSpcReserveDown": nimbleGmSnapSpcReserveDown,
       "nimbleGmPoolMrgDeprecated": nimbleGmPoolMrgDeprecated,
       "nimbleVolAttrSyncSuccess": nimbleVolAttrSyncSuccess,
       "nimbleSnapAttrSyncDelay": nimbleSnapAttrSyncDelay,
       "nimbleSnapAttrSyncSuccess": nimbleSnapAttrSyncSuccess,
       "nimbleGroupAttrSyncDelay": nimbleGroupAttrSyncDelay,
       "nimbleGroupAttrSyncComplete": nimbleGroupAttrSyncComplete,
       "nimbleGlCtrlrAttrSyncDelayDeprecated": nimbleGlCtrlrAttrSyncDelayDeprecated,
       "nimbleGlCtrlrAttrSyncCompleteDeprecated": nimbleGlCtrlrAttrSyncCompleteDeprecated,
       "nimbleGlCtrlrAttrSyncDelay": nimbleGlCtrlrAttrSyncDelay,
       "nimbleGlCtrlrAttrSyncComplete": nimbleGlCtrlrAttrSyncComplete,
       "nimbleVolMoveComplete": nimbleVolMoveComplete,
       "nimbleVolMoveAbortComplete": nimbleVolMoveAbortComplete,
       "nimbleGmPoolArrUnassgnCompleteDeprecated": nimbleGmPoolArrUnassgnCompleteDeprecated,
       "nimbleGmPoolArrUnassgnComplete": nimbleGmPoolArrUnassgnComplete,
       "nimbleGmPoolArrAssgn": nimbleGmPoolArrAssgn,
       "nimbleGmPoolArrUnassgn": nimbleGmPoolArrUnassgn,
       "nimbleGmPoolMrg": nimbleGmPoolMrg,
       "nimbleGmVolSpcCurCritUpNonWritable": nimbleGmVolSpcCurCritUpNonWritable,
       "nimbleGmVolSpcCurQuotaNonWritable": nimbleGmVolSpcCurQuotaNonWritable,
       "nimbleGmSnapSpcCurCritUpNonWritable": nimbleGmSnapSpcCurCritUpNonWritable,
       "nimbleGmVolSpcSnapQuotaNonWritable": nimbleGmVolSpcSnapQuotaNonWritable,
       "nimbleGmVolSpcCurReserveNonWritable": nimbleGmVolSpcCurReserveNonWritable,
       "nimbleGmVolSpcSnapReserveNonWritable": nimbleGmVolSpcSnapReserveNonWritable,
       "nimbleSchedSnapSucceededDeprecated": nimbleSchedSnapSucceededDeprecated,
       "nimbleSchedSnapFailed": nimbleSchedSnapFailed,
       "nimbleSchedSnapSkippedExists": nimbleSchedSnapSkippedExists,
       "nimbleSchedSnapSkippedHandover": nimbleSchedSnapSkippedHandover,
       "nimbleSchedSnapSucceededLagInfoDeprecated": nimbleSchedSnapSucceededLagInfoDeprecated,
       "nimbleSchedSnapFailedVmwareCredentialDeprecated": nimbleSchedSnapFailedVmwareCredentialDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated": nimbleSchedSnapFailedVmwareConnectionTimeoutDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated": nimbleSchedSnapFailedVmwareConnectionRefusedDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionResetDeprecated": nimbleSchedSnapFailedVmwareConnectionResetDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated": nimbleSchedSnapFailedVmwareConnectionNorouteDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionSocketDeprecated": nimbleSchedSnapFailedVmwareConnectionSocketDeprecated,
       "nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated": nimbleSchedSnapFailedVmwareConnectionUnreachableDeprecated,
       "nimbleSchedSnapFailedVmwareDisabledDeprecated": nimbleSchedSnapFailedVmwareDisabledDeprecated,
       "nimbleSchedSnapFailedVmwareObjectnfDeprecated": nimbleSchedSnapFailedVmwareObjectnfDeprecated,
       "nimbleSchedSnapFailedVmwarePermissionDeprecated": nimbleSchedSnapFailedVmwarePermissionDeprecated,
       "nimbleSchedSnapFailedVmwareUkhostDeprecated": nimbleSchedSnapFailedVmwareUkhostDeprecated,
       "nimbleSchedSnapFailedVmwareEncodingPlainDeprecated": nimbleSchedSnapFailedVmwareEncodingPlainDeprecated,
       "nimbleSchedSnapFailedVmwareNullDeprecated": nimbleSchedSnapFailedVmwareNullDeprecated,
       "nimbleSchedSnapFailedVmwareDcnotfoundDeprecated": nimbleSchedSnapFailedVmwareDcnotfoundDeprecated,
       "nimbleSchedSnapFailedVmwareVolsnemptyDeprecated": nimbleSchedSnapFailedVmwareVolsnemptyDeprecated,
       "nimbleSchedSnapFailedVmwareUnknownDeprecated": nimbleSchedSnapFailedVmwareUnknownDeprecated,
       "nimbleSchedSnapFailedVmwareBsizeDeprecated": nimbleSchedSnapFailedVmwareBsizeDeprecated,
       "nimbleSchedSnapSucceeded": nimbleSchedSnapSucceeded,
       "nimbleSchedSnapSucceededLagInfo": nimbleSchedSnapSucceededLagInfo,
       "nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo": nimbleSchedSnapFailedVmwareDisabledDeprecatedTwo,
       "nimbleSchedSnapFailedVmwareTimeoutDeprecated": nimbleSchedSnapFailedVmwareTimeoutDeprecated,
       "nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated": nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededDeprecated,
       "nimbleSchedSnapFallback": nimbleSchedSnapFallback,
       "nimbleSchedSnapFailedVmwarePermissionPerVm": nimbleSchedSnapFailedVmwarePermissionPerVm,
       "nimbleSchedSnapFailedVmwareObjectnfPerVm": nimbleSchedSnapFailedVmwareObjectnfPerVm,
       "nimbleSchedSnapFailedVmwareEncodingPlainPerVm": nimbleSchedSnapFailedVmwareEncodingPlainPerVm,
       "nimbleSchedSnapFailedVmwareNullPerVm": nimbleSchedSnapFailedVmwareNullPerVm,
       "nimbleSchedSnapFailedVmwareDcnotfoundPerVm": nimbleSchedSnapFailedVmwareDcnotfoundPerVm,
       "nimbleSchedSnapFailedVmwareVolsnemptyPerVm": nimbleSchedSnapFailedVmwareVolsnemptyPerVm,
       "nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated": nimbleSchedSnapFailedVmwareUnknownPerVmDeprecated,
       "nimbleSchedSnapFailedVmwareBsizePerVm": nimbleSchedSnapFailedVmwareBsizePerVm,
       "nimbleSchedSnapFailedVmwareDisabledPerVm": nimbleSchedSnapFailedVmwareDisabledPerVm,
       "nimbleSchedSnapFailedVmwareTimeoutPerVm": nimbleSchedSnapFailedVmwareTimeoutPerVm,
       "nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm": nimbleSchedSnapFailedVmwareSnapNameMaxLengthExceededPerVm,
       "nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm": nimbleSchedSnapFailedVmwareGuestToolsNotRunningPerVm,
       "nimbleSchedSnapFailedVmwareInvalidVcenter": nimbleSchedSnapFailedVmwareInvalidVcenter,
       "nimbleSchedSnapFailedVmwareBusy": nimbleSchedSnapFailedVmwareBusy,
       "nimbleSchedSnapFailedVssIncompatible": nimbleSchedSnapFailedVssIncompatible,
       "nimbleSchedSnapFailedVmwareCredentialNw": nimbleSchedSnapFailedVmwareCredentialNw,
       "nimbleSchedSnapFailedVmwareConnectionTimeoutNw": nimbleSchedSnapFailedVmwareConnectionTimeoutNw,
       "nimbleSchedSnapFailedVmwareConnectionRefusedNw": nimbleSchedSnapFailedVmwareConnectionRefusedNw,
       "nimbleSchedSnapFailedVmwareConnectionResetNw": nimbleSchedSnapFailedVmwareConnectionResetNw,
       "nimbleSchedSnapFailedVmwareConnectionNorouteNw": nimbleSchedSnapFailedVmwareConnectionNorouteNw,
       "nimbleSchedSnapFailedVmwareConnectionSocketNw": nimbleSchedSnapFailedVmwareConnectionSocketNw,
       "nimbleSchedSnapFailedVmwareConnectionUnreachableNw": nimbleSchedSnapFailedVmwareConnectionUnreachableNw,
       "nimbleSchedSnapFailedVmwareUkhostNw": nimbleSchedSnapFailedVmwareUkhostNw,
       "nimbleSchedSnapFailedVmwareConnectionUnknownNw": nimbleSchedSnapFailedVmwareConnectionUnknownNw,
       "nimbleSchedSnapFailedVmwareTimeoutNw": nimbleSchedSnapFailedVmwareTimeoutNw,
       "nimbleSchedSnapFailedVmwareUnknownNw": nimbleSchedSnapFailedVmwareUnknownNw,
       "nimbleSchedSnapFailedVmwareUnknownPerVm": nimbleSchedSnapFailedVmwareUnknownPerVm,
       "nimbleSchedSnapFailedVmwareQuiescingVmFailed": nimbleSchedSnapFailedVmwareQuiescingVmFailed,
       "nimbleGmSpaceReserveWarnUp": nimbleGmSpaceReserveWarnUp,
       "nimbleGmSpaceReserveWarnDown": nimbleGmSpaceReserveWarnDown,
       "nimbleGmSpaceReserveCritUp": nimbleGmSpaceReserveCritUp,
       "nimbleGmSpaceReserveCritDown": nimbleGmSpaceReserveCritDown,
       "nimbleGmSpaceUtilizationOk": nimbleGmSpaceUtilizationOk,
       "nimbleGmSpaceUtilizationInfo": nimbleGmSpaceUtilizationInfo,
       "nimbleGmSpaceUtilizationHigh": nimbleGmSpaceUtilizationHigh,
       "nimbleGmSpaceUtilizationCrit": nimbleGmSpaceUtilizationCrit,
       "nimbleGmPoolSpaceReserveWarnUpDeprecated": nimbleGmPoolSpaceReserveWarnUpDeprecated,
       "nimbleGmPoolSpaceReserveWarnDownDeprecated": nimbleGmPoolSpaceReserveWarnDownDeprecated,
       "nimbleGmPoolSpaceReserveCritUpDeprecated": nimbleGmPoolSpaceReserveCritUpDeprecated,
       "nimbleGmPoolSpaceReserveCritDownDeprecated": nimbleGmPoolSpaceReserveCritDownDeprecated,
       "nimbleGmPoolSpaceUtilizationOkDeprecated": nimbleGmPoolSpaceUtilizationOkDeprecated,
       "nimbleGmPoolSpaceUtilizationInfoDeprecated": nimbleGmPoolSpaceUtilizationInfoDeprecated,
       "nimbleGmPoolSpaceUtilizationHighDeprecated": nimbleGmPoolSpaceUtilizationHighDeprecated,
       "nimbleGmPoolSpaceUtilizationCritDeprecated": nimbleGmPoolSpaceUtilizationCritDeprecated,
       "nimbleGmPoolSpaceReserveWarnUp": nimbleGmPoolSpaceReserveWarnUp,
       "nimbleGmPoolSpaceReserveWarnDown": nimbleGmPoolSpaceReserveWarnDown,
       "nimbleGmPoolSpaceReserveCritUp": nimbleGmPoolSpaceReserveCritUp,
       "nimbleGmPoolSpaceReserveCritDown": nimbleGmPoolSpaceReserveCritDown,
       "nimbleGmPoolSpaceUtilizationOk": nimbleGmPoolSpaceUtilizationOk,
       "nimbleGmPoolSpaceUtilizationInfo": nimbleGmPoolSpaceUtilizationInfo,
       "nimbleGmPoolSpaceUtilizationHigh": nimbleGmPoolSpaceUtilizationHigh,
       "nimbleGmPoolSpaceUtilizationCrit": nimbleGmPoolSpaceUtilizationCrit,
       "nimbleLimitMaxOver": nimbleLimitMaxOver,
       "nimbleLimitMaxUnder": nimbleLimitMaxUnder,
       "nimbleLimitWarnOver": nimbleLimitWarnOver,
       "nimbleLimitWarnUnder": nimbleLimitWarnUnder,
       "nimbleReplSnapcollSucceeded": nimbleReplSnapcollSucceeded,
       "nimbleReplSnapcollDelayedInfo": nimbleReplSnapcollDelayedInfo,
       "nimbleReplSnapcollDelayedWarn": nimbleReplSnapcollDelayedWarn,
       "nimbleReplPartnerSyncFail": nimbleReplPartnerSyncFail,
       "nimbleReplBranchPinned": nimbleReplBranchPinned,
       "nimbleReplHandoverCompleted": nimbleReplHandoverCompleted,
       "nimbleReplMultiArrayGroup": nimbleReplMultiArrayGroup,
       "nimbleReplPartnerMisconfiguration": nimbleReplPartnerMisconfiguration,
       "nimbleReplSnapshotCorrectedDeprecated": nimbleReplSnapshotCorrectedDeprecated,
       "nimbleReplCbrRequestedDeprecated": nimbleReplCbrRequestedDeprecated,
       "nimbleReplCbrNeeded": nimbleReplCbrNeeded,
       "nimbleReplSnapshotCorrectedDeprecated2": nimbleReplSnapshotCorrectedDeprecated2,
       "nimbleReplCbrRequestedDeprecated2": nimbleReplCbrRequestedDeprecated2,
       "nimbleReplPartnerAuthFailDeprecated": nimbleReplPartnerAuthFailDeprecated,
       "nimbleReplSnapshotCorrected": nimbleReplSnapshotCorrected,
       "nimbleReplCbrRequested": nimbleReplCbrRequested,
       "nimbleReplPartnerAuthFail": nimbleReplPartnerAuthFail,
       "nimbleOvertempShutdownDeprecated": nimbleOvertempShutdownDeprecated,
       "nimbleCtrlrOvertempDeprecated": nimbleCtrlrOvertempDeprecated,
       "nimbleBackplaneOvertempDeprecated": nimbleBackplaneOvertempDeprecated,
       "nimbleIscsiErroneousItorConns": nimbleIscsiErroneousItorConns,
       "nimbleDiskFailedCritDeprecated": nimbleDiskFailedCritDeprecated,
       "nimbleDiskFailedDeprecated": nimbleDiskFailedDeprecated,
       "nimbleDiskAbsentDeprecated": nimbleDiskAbsentDeprecated,
       "nimbleDiskAddedDeprecated": nimbleDiskAddedDeprecated,
       "nimbleDiskRemovedDeprecated": nimbleDiskRemovedDeprecated,
       "nimbleSsdFailedDeprecated": nimbleSsdFailedDeprecated,
       "nimbleSsdAbsentDeprecated": nimbleSsdAbsentDeprecated,
       "nimbleSsdAddedDeprecated": nimbleSsdAddedDeprecated,
       "nimbleSsdRemovedDeprecated": nimbleSsdRemovedDeprecated,
       "nimbleDiskInvalidLabel": nimbleDiskInvalidLabel,
       "nimbleSsdInvalidLabel": nimbleSsdInvalidLabel,
       "nimbleDiskSizeMismatchDeprecated": nimbleDiskSizeMismatchDeprecated,
       "nimbleHddFailedV2": nimbleHddFailedV2,
       "nimbleHddAbsentV2": nimbleHddAbsentV2,
       "nimbleHddAddedV2": nimbleHddAddedV2,
       "nimbleHddRemovedV2": nimbleHddRemovedV2,
       "nimbleSsdFailedV2": nimbleSsdFailedV2,
       "nimbleSsdAbsentV2": nimbleSsdAbsentV2,
       "nimbleSsdAddedV2": nimbleSsdAddedV2,
       "nimbleSsdRemovedV2": nimbleSsdRemovedV2,
       "nimbleSsdLastOne": nimbleSsdLastOne,
       "nimbleHddFailedV3": nimbleHddFailedV3,
       "nimbleHddAddedV3": nimbleHddAddedV3,
       "nimbleHddRemovedV3": nimbleHddRemovedV3,
       "nimbleSsdFailedV3": nimbleSsdFailedV3,
       "nimbleSsdAddedV3": nimbleSsdAddedV3,
       "nimbleSsdRemovedV3": nimbleSsdRemovedV3,
       "nimbleDiskSizeMismatchV2": nimbleDiskSizeMismatchV2,
       "nimbleSsdSizeMismatchV2": nimbleSsdSizeMismatchV2,
       "nimbleHddFailedAfsDeprecated": nimbleHddFailedAfsDeprecated,
       "nimbleHddFailedAfs": nimbleHddFailedAfs,
       "nimbleIpIfDown": nimbleIpIfDown,
       "nimbleIpIfUp": nimbleIpIfUp,
       "nimbleIpIfGroupUnavailDeprecated": nimbleIpIfGroupUnavailDeprecated,
       "nimbleIpIfDataUnavailDeprecated": nimbleIpIfDataUnavailDeprecated,
       "nimbleIpIfCantFailoverDeprecated": nimbleIpIfCantFailoverDeprecated,
       "nimbleSubnetNicMigrationDeprecated": nimbleSubnetNicMigrationDeprecated,
       "nimbleSubnetNicMissingDeprecated": nimbleSubnetNicMissingDeprecated,
       "nimbleIpNicMigrationDeprecated": nimbleIpNicMigrationDeprecated,
       "nimbleIpNicMissingDeprecated": nimbleIpNicMissingDeprecated,
       "nimbleRouteNicMigrationDeprecated": nimbleRouteNicMigrationDeprecated,
       "nimbleRouteNicMissingDeprecated": nimbleRouteNicMissingDeprecated,
       "nimbleIpIfFailover": nimbleIpIfFailover,
       "nimbleIpDupFound": nimbleIpDupFound,
       "nimbleIpIfDiscoveryUnavailDeprecated": nimbleIpIfDiscoveryUnavailDeprecated,
       "nimbleIpIfTargetUnavailDeprecated": nimbleIpIfTargetUnavailDeprecated,
       "nimbleIpIfGroupUnavail": nimbleIpIfGroupUnavail,
       "nimbleIpIfDiscoveryUnavail": nimbleIpIfDiscoveryUnavail,
       "nimbleIpIfTargetUnavail": nimbleIpIfTargetUnavail,
       "nimbleIpIfDataUnavail": nimbleIpIfDataUnavail,
       "nimbleIpIfIscsiDataUnavail": nimbleIpIfIscsiDataUnavail,
       "nimbleIpIfClusterDataUnavail": nimbleIpIfClusterDataUnavail,
       "nimbleUnresponsiveNicDetected": nimbleUnresponsiveNicDetected,
       "nimbleIpIfCantFailoverDeprecated2": nimbleIpIfCantFailoverDeprecated2,
       "nimbleIpIfCantFailover": nimbleIpIfCantFailover,
       "nimbleSensorLinearWarn": nimbleSensorLinearWarn,
       "nimbleSensorLinearClear": nimbleSensorLinearClear,
       "nimbleSensorBoolWarn": nimbleSensorBoolWarn,
       "nimbleSensorBoolClear": nimbleSensorBoolClear,
       "nimbleSensorDoesNotExist": nimbleSensorDoesNotExist,
       "nimbleNvramBattDisabled": nimbleNvramBattDisabled,
       "nimbleNvramBattDisabledCrit": nimbleNvramBattDisabledCrit,
       "nimbleNvramBattOk": nimbleNvramBattOk,
       "nimbleTempSensorHighDep": nimbleTempSensorHighDep,
       "nimbleTempSensorLowDep": nimbleTempSensorLowDep,
       "nimbleTempSensorOkDep": nimbleTempSensorOkDep,
       "nimbleTempSensorMissingDep": nimbleTempSensorMissingDep,
       "nimbleTempSensorOperationalDep": nimbleTempSensorOperationalDep,
       "nimbleFanSensorHighDep": nimbleFanSensorHighDep,
       "nimbleFanSensorLowDep": nimbleFanSensorLowDep,
       "nimbleFanSensorOkDep": nimbleFanSensorOkDep,
       "nimbleFanSensorStoppedDep": nimbleFanSensorStoppedDep,
       "nimbleFanSensorMissingDep": nimbleFanSensorMissingDep,
       "nimblePwrSupplySensorFailDep": nimblePwrSupplySensorFailDep,
       "nimblePwrSupplySensorMissingDep": nimblePwrSupplySensorMissingDep,
       "nimblePwrSupplySensorOkDep": nimblePwrSupplySensorOkDep,
       "nimbleTempSensorHighDep2": nimbleTempSensorHighDep2,
       "nimbleTempSensorLowDep2": nimbleTempSensorLowDep2,
       "nimbleTempSensorOkDep2": nimbleTempSensorOkDep2,
       "nimbleTempSensorMissingDep2": nimbleTempSensorMissingDep2,
       "nimbleTempSensorOperationalDep2": nimbleTempSensorOperationalDep2,
       "nimbleFanSensorHighDep2": nimbleFanSensorHighDep2,
       "nimbleFanSensorLowDep2": nimbleFanSensorLowDep2,
       "nimbleFanSensorOkDep2": nimbleFanSensorOkDep2,
       "nimbleFanSensorStoppedDep2": nimbleFanSensorStoppedDep2,
       "nimbleFanSensorMissingDep2": nimbleFanSensorMissingDep2,
       "nimblePwrSupplySensorFailDep2": nimblePwrSupplySensorFailDep2,
       "nimblePwrSupplySensorMissingDep2": nimblePwrSupplySensorMissingDep2,
       "nimblePwrSupplySensorOkDep2": nimblePwrSupplySensorOkDep2,
       "nimbleTempSensorHighDeprecatedDep2": nimbleTempSensorHighDeprecatedDep2,
       "nimbleTempSensorLow": nimbleTempSensorLow,
       "nimbleTempSensorOk": nimbleTempSensorOk,
       "nimbleTempSensorMissing": nimbleTempSensorMissing,
       "nimbleTempSensorOperational": nimbleTempSensorOperational,
       "nimbleFanSensorHigh": nimbleFanSensorHigh,
       "nimbleFanSensorLow": nimbleFanSensorLow,
       "nimbleFanSensorOk": nimbleFanSensorOk,
       "nimbleFanSensorStopped": nimbleFanSensorStopped,
       "nimbleFanSensorMissing": nimbleFanSensorMissing,
       "nimblePwrSupplySensorFail": nimblePwrSupplySensorFail,
       "nimblePwrSupplySensorMissing": nimblePwrSupplySensorMissing,
       "nimblePwrSupplySensorOk": nimblePwrSupplySensorOk,
       "nimbleRaidDegraded": nimbleRaidDegraded,
       "nimbleRaidRebuildStart": nimbleRaidRebuildStart,
       "nimbleRaidRebuildDone": nimbleRaidRebuildDone,
       "nimbleRaidRebuildFailRead": nimbleRaidRebuildFailRead,
       "nimbleRaidRebuildFail": nimbleRaidRebuildFail,
       "nimbleRaidDisksMissing": nimbleRaidDisksMissing,
       "nimbleRaidSpare": nimbleRaidSpare,
       "nimbleRaidAssemblyFailed": nimbleRaidAssemblyFailed,
       "nimbleRaidDegradedV2": nimbleRaidDegradedV2,
       "nimbleRaidRebuildStartV2": nimbleRaidRebuildStartV2,
       "nimbleRaidRebuildDoneV2": nimbleRaidRebuildDoneV2,
       "nimbleRaidRebuildFailReadV2": nimbleRaidRebuildFailReadV2,
       "nimbleRaidRebuildFailV2": nimbleRaidRebuildFailV2,
       "nimbleRaidDisksMissingV2": nimbleRaidDisksMissingV2,
       "nimbleRaidSpareV2": nimbleRaidSpareV2,
       "nimbleRaidAssemblyFailedV2": nimbleRaidAssemblyFailedV2,
       "nimbleRaidRebuildScheduledV2": nimbleRaidRebuildScheduledV2,
       "nimbleRaidRebuildStopV2": nimbleRaidRebuildStopV2,
       "nimbleIscsiMultiInitiatorDeprecated": nimbleIscsiMultiInitiatorDeprecated,
       "nimbleIscsiConnHardLimitDeprecated1": nimbleIscsiConnHardLimitDeprecated1,
       "nimbleIscsiUnalignedOpsDeprecated": nimbleIscsiUnalignedOpsDeprecated,
       "nimbleIscsiMultiInitiator": nimbleIscsiMultiInitiator,
       "nimbleIscsiConnHardLimitDeprecated2": nimbleIscsiConnHardLimitDeprecated2,
       "nimbleIscsiUnalignedOps": nimbleIscsiUnalignedOps,
       "nimbleIscsiConnHardLimit": nimbleIscsiConnHardLimit,
       "nimbleNvramBattCharging": nimbleNvramBattCharging,
       "nimbleNvramBattCharged": nimbleNvramBattCharged,
       "nimbleNvramFpgaVersion": nimbleNvramFpgaVersion,
       "nimbleNvramMbeDeprecated": nimbleNvramMbeDeprecated,
       "nimbleNvramSbeDeprecated": nimbleNvramSbeDeprecated,
       "nimbleNvramMbe": nimbleNvramMbe,
       "nimbleNvramSbe": nimbleNvramSbe,
       "nimbleNvdimmReservedBlocksWarn": nimbleNvdimmReservedBlocksWarn,
       "nimbleNvdimmReservedBlocksCrit": nimbleNvdimmReservedBlocksCrit,
       "nimbleNvdimmUltracapDischargedDeprecated": nimbleNvdimmUltracapDischargedDeprecated,
       "nimbleNtbBadLink": nimbleNtbBadLink,
       "nimbleNvdimmUltracapDischarged": nimbleNvdimmUltracapDischarged,
       "nimbleNvramMissing": nimbleNvramMissing,
       "nimbleShelfCtrlrSide": nimbleShelfCtrlrSide,
       "nimbleShelfSesErr": nimbleShelfSesErr,
       "nimbleShelfDiskSasLink": nimbleShelfDiskSasLink,
       "nimbleShelfDiskCount": nimbleShelfDiskCount,
       "nimbleShelfInvalidEeprom": nimbleShelfInvalidEeprom,
       "nimbleShelfWrongSasPortDeprecated": nimbleShelfWrongSasPortDeprecated,
       "nimbleShelfSasLink": nimbleShelfSasLink,
       "nimbleShelfSasExpErr": nimbleShelfSasExpErr,
       "nimbleShelfCtrlrLoop": nimbleShelfCtrlrLoop,
       "nimbleShelfMissing": nimbleShelfMissing,
       "nimbleShelfOrder": nimbleShelfOrder,
       "nimbleShelfSesMshipErrDeprecated": nimbleShelfSesMshipErrDeprecated,
       "nimbleShelfFailover": nimbleShelfFailover,
       "nimbleShelfNewShelf": nimbleShelfNewShelf,
       "nimbleShelfDisconnect": nimbleShelfDisconnect,
       "nimbleShelfChassisSwap": nimbleShelfChassisSwap,
       "nimbleShelfLocIdOverLimit": nimbleShelfLocIdOverLimit,
       "nimbleShelfActivatedDeprecated": nimbleShelfActivatedDeprecated,
       "nimbleShelfReconnect": nimbleShelfReconnect,
       "nimbleShelfSasLinkDisabledDeprecated": nimbleShelfSasLinkDisabledDeprecated,
       "nimbleShelfDiskSasLinkErrDeprecated": nimbleShelfDiskSasLinkErrDeprecated,
       "nimbleShelfWrongSasPortDeprecated2": nimbleShelfWrongSasPortDeprecated2,
       "nimbleShelfSesMshipErrDeprecated2": nimbleShelfSesMshipErrDeprecated2,
       "nimbleShelfSasLinkDisabled": nimbleShelfSasLinkDisabled,
       "nimbleShelfDiskSasLinkErr": nimbleShelfDiskSasLinkErr,
       "nimbleShelfWrongSasPort": nimbleShelfWrongSasPort,
       "nimbleShelfSesMshipErrDeprecated3": nimbleShelfSesMshipErrDeprecated3,
       "nimbleShelfSesMshipErrDeprecated4": nimbleShelfSesMshipErrDeprecated4,
       "nimbleShelfActivatedV2Deprecated": nimbleShelfActivatedV2Deprecated,
       "nimbleShelfSesMshipErr": nimbleShelfSesMshipErr,
       "nimbleShelfActivatedV2": nimbleShelfActivatedV2,
       "nimblePhysMemMismatch": nimblePhysMemMismatch,
       "nimbleVolSysLimitWarnEnter": nimbleVolSysLimitWarnEnter,
       "nimbleVolSysLimitWarnExit": nimbleVolSysLimitWarnExit,
       "nimbleGmTakeoverSuccessDeprecatedDeprecated": nimbleGmTakeoverSuccessDeprecatedDeprecated,
       "nimbleGmTakeoverRejectByArrayDeprecated": nimbleGmTakeoverRejectByArrayDeprecated,
       "nimbleGmTakeoverRejectByArray": nimbleGmTakeoverRejectByArray,
       "nimbleGmTakeoverSuccessDeprecated": nimbleGmTakeoverSuccessDeprecated,
       "nimbleGmTakeoverSuccess": nimbleGmTakeoverSuccess,
       "nimbleGmMigrateFailure": nimbleGmMigrateFailure,
       "nimbleGmGrpMrgDone": nimbleGmGrpMrgDone,
       "nimbleGmGrpQscFail": nimbleGmGrpQscFail,
       "nimbleGmGrpMrgRollbackDone": nimbleGmGrpMrgRollbackDone,
       "nimbleGmGrpMrgReassFail": nimbleGmGrpMrgReassFail,
       "nimbleGmGrpMrgDbFail": nimbleGmGrpMrgDbFail,
       "nimbleGmBinMigContAbortDeprecated": nimbleGmBinMigContAbortDeprecated,
       "nimbleGmBinMigContAbort": nimbleGmBinMigContAbort,
       "nimbleCsmodelChanged": nimbleCsmodelChanged,
       "nimbleCsmodelUnknown": nimbleCsmodelUnknown,
       "nimbleTempSensorHighDeprecated": nimbleTempSensorHighDeprecated,
       "nimbleOvertempShutdownDeprecated2": nimbleOvertempShutdownDeprecated2,
       "nimbleCtrlrOvertemp": nimbleCtrlrOvertemp,
       "nimbleBackplaneOvertemp": nimbleBackplaneOvertemp,
       "nimbleTempSensorHighDeprecated2": nimbleTempSensorHighDeprecated2,
       "nimbleTempSensorCrithighDeprecated": nimbleTempSensorCrithighDeprecated,
       "nimblePwrSupplySensorCallsupportDeprecated": nimblePwrSupplySensorCallsupportDeprecated,
       "nimbleOvertempShutdown": nimbleOvertempShutdown,
       "nimblePwrSupplySensorCallsupport": nimblePwrSupplySensorCallsupport,
       "nimbleTempSensorHigh": nimbleTempSensorHigh,
       "nimbleTempSensorCrithigh": nimbleTempSensorCrithigh,
       "nimbleUpdateUnknownFirmware": nimbleUpdateUnknownFirmware,
       "nimbleFcLinkUp": nimbleFcLinkUp,
       "nimbleFcLinkDown": nimbleFcLinkDown,
       "nimbleFcLinkNotConnected": nimbleFcLinkNotConnected,
       "nimbleEventPurging": nimbleEventPurging,
       "nimbleEventWarnOver": nimbleEventWarnOver}
)
