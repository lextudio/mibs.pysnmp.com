# SNMP MIB module (CISCO-UDLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UDLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:58 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoUdldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118)
)
ciscoUdldpMIB.setRevisions(
        ("2009-11-09 09:00",
         "2007-11-27 00:00",
         "2003-02-21 00:00",
         "2002-10-10 00:00",
         "2000-04-10 00:00",
         "1998-11-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoUdldpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoUdldpMIBNotifs = _CiscoUdldpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 0)
)
_CiscoUdldpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUdldpMIBObjects = _CiscoUdldpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1)
)
_CudldpGlobal_ObjectIdentity = ObjectIdentity
cudldpGlobal = _CudldpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1)
)
_CudldpGlobalEnable_Type = TruthValue
_CudldpGlobalEnable_Object = MibScalar
cudldpGlobalEnable = _CudldpGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 1),
    _CudldpGlobalEnable_Type()
)
cudldpGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpGlobalEnable.setStatus("deprecated")


class _CudldpHelloInterval_Type(Integer32):
    """Custom type cudldpHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 90),
    )


_CudldpHelloInterval_Type.__name__ = "Integer32"
_CudldpHelloInterval_Object = MibScalar
cudldpHelloInterval = _CudldpHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 2),
    _CudldpHelloInterval_Type()
)
cudldpHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    cudldpHelloInterval.setUnits("seconds")


class _CudldpGlobalMode_Type(Integer32):
    """Custom type cudldpGlobalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 3),
          ("disable", 2),
          ("enable", 1))
    )


_CudldpGlobalMode_Type.__name__ = "Integer32"
_CudldpGlobalMode_Object = MibScalar
cudldpGlobalMode = _CudldpGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 3),
    _CudldpGlobalMode_Type()
)
cudldpGlobalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpGlobalMode.setStatus("current")


class _CudldpHelloIntervalExt_Type(Unsigned32):
    """Custom type cudldpHelloIntervalExt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_CudldpHelloIntervalExt_Type.__name__ = "Unsigned32"
_CudldpHelloIntervalExt_Object = MibScalar
cudldpHelloIntervalExt = _CudldpHelloIntervalExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 4),
    _CudldpHelloIntervalExt_Type()
)
cudldpHelloIntervalExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpHelloIntervalExt.setStatus("current")
if mibBuilder.loadTexts:
    cudldpHelloIntervalExt.setUnits("seconds")
_CudldpFastHelloLinkFailRptNotifEnable_Type = TruthValue
_CudldpFastHelloLinkFailRptNotifEnable_Object = MibScalar
cudldpFastHelloLinkFailRptNotifEnable = _CudldpFastHelloLinkFailRptNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 5),
    _CudldpFastHelloLinkFailRptNotifEnable_Type()
)
cudldpFastHelloLinkFailRptNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpFastHelloLinkFailRptNotifEnable.setStatus("current")
_CudldpFastHelloStatusChangeNotifEnable_Type = TruthValue
_CudldpFastHelloStatusChangeNotifEnable_Object = MibScalar
cudldpFastHelloStatusChangeNotifEnable = _CudldpFastHelloStatusChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 1, 6),
    _CudldpFastHelloStatusChangeNotifEnable_Type()
)
cudldpFastHelloStatusChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpFastHelloStatusChangeNotifEnable.setStatus("current")
_CudldpInterface_ObjectIdentity = ObjectIdentity
cudldpInterface = _CudldpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2)
)
_CudldpInterfaceTable_Object = MibTable
cudldpInterfaceTable = _CudldpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cudldpInterfaceTable.setStatus("current")
_CudldpInterfaceEntry_Object = MibTableRow
cudldpInterfaceEntry = _CudldpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1)
)
cudldpInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cudldpInterfaceEntry.setStatus("current")
_CudldpInterfaceEnable_Type = TruthValue
_CudldpInterfaceEnable_Object = MibTableColumn
cudldpInterfaceEnable = _CudldpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 1),
    _CudldpInterfaceEnable_Type()
)
cudldpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpInterfaceEnable.setStatus("deprecated")


class _CudldpInterfaceOperStatus_Type(Integer32):
    """Custom type cudldpInterfaceOperStatus based on Integer32"""
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
        *(("biDirectional", 3),
          ("indeterminant", 2),
          ("notApplicable", 4),
          ("shutdown", 1))
    )


_CudldpInterfaceOperStatus_Type.__name__ = "Integer32"
_CudldpInterfaceOperStatus_Object = MibTableColumn
cudldpInterfaceOperStatus = _CudldpInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 2),
    _CudldpInterfaceOperStatus_Type()
)
cudldpInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cudldpInterfaceOperStatus.setStatus("current")
_CudldpInterfaceAggressiveMode_Type = TruthValue
_CudldpInterfaceAggressiveMode_Object = MibTableColumn
cudldpInterfaceAggressiveMode = _CudldpInterfaceAggressiveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 3),
    _CudldpInterfaceAggressiveMode_Type()
)
cudldpInterfaceAggressiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpInterfaceAggressiveMode.setStatus("deprecated")


class _CudldpInterfaceAdminMode_Type(Integer32):
    """Custom type cudldpInterfaceAdminMode based on Integer32"""
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
        *(("aggressive", 3),
          ("default", 4),
          ("disable", 2),
          ("enable", 1))
    )


_CudldpInterfaceAdminMode_Type.__name__ = "Integer32"
_CudldpInterfaceAdminMode_Object = MibTableColumn
cudldpInterfaceAdminMode = _CudldpInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 4),
    _CudldpInterfaceAdminMode_Type()
)
cudldpInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpInterfaceAdminMode.setStatus("current")


class _CudldpInterfaceOperMode_Type(Integer32):
    """Custom type cudldpInterfaceOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 3),
          ("disable", 2),
          ("enable", 1))
    )


_CudldpInterfaceOperMode_Type.__name__ = "Integer32"
_CudldpInterfaceOperMode_Object = MibTableColumn
cudldpInterfaceOperMode = _CudldpInterfaceOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 5),
    _CudldpInterfaceOperMode_Type()
)
cudldpInterfaceOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cudldpInterfaceOperMode.setStatus("current")
_CudldpIfFastHelloInterval_Type = Unsigned32
_CudldpIfFastHelloInterval_Object = MibTableColumn
cudldpIfFastHelloInterval = _CudldpIfFastHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 6),
    _CudldpIfFastHelloInterval_Type()
)
cudldpIfFastHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpIfFastHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    cudldpIfFastHelloInterval.setUnits("milliseconds")
_CudldpIfOperHelloInterval_Type = Unsigned32
_CudldpIfOperHelloInterval_Object = MibTableColumn
cudldpIfOperHelloInterval = _CudldpIfOperHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 7),
    _CudldpIfOperHelloInterval_Type()
)
cudldpIfOperHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cudldpIfOperHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    cudldpIfOperHelloInterval.setUnits("milliseconds")


class _CudldpIfFastHelloOperStatus_Type(Integer32):
    """Custom type cudldpIfFastHelloOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("operational", 1))
    )


_CudldpIfFastHelloOperStatus_Type.__name__ = "Integer32"
_CudldpIfFastHelloOperStatus_Object = MibTableColumn
cudldpIfFastHelloOperStatus = _CudldpIfFastHelloOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 2, 1, 1, 8),
    _CudldpIfFastHelloOperStatus_Type()
)
cudldpIfFastHelloOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cudldpIfFastHelloOperStatus.setStatus("current")
_CudldpFastHello_ObjectIdentity = ObjectIdentity
cudldpFastHello = _CudldpFastHello_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3)
)
_CudldpFastHelloErrorReportEnable_Type = TruthValue
_CudldpFastHelloErrorReportEnable_Object = MibScalar
cudldpFastHelloErrorReportEnable = _CudldpFastHelloErrorReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 1),
    _CudldpFastHelloErrorReportEnable_Type()
)
cudldpFastHelloErrorReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cudldpFastHelloErrorReportEnable.setStatus("current")
_CudldpFastHelloMaxPorts_Type = Unsigned32
_CudldpFastHelloMaxPorts_Object = MibScalar
cudldpFastHelloMaxPorts = _CudldpFastHelloMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 2),
    _CudldpFastHelloMaxPorts_Type()
)
cudldpFastHelloMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cudldpFastHelloMaxPorts.setStatus("current")
_CudldpFastHelloConfigPorts_Type = Unsigned32
_CudldpFastHelloConfigPorts_Object = MibScalar
cudldpFastHelloConfigPorts = _CudldpFastHelloConfigPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 3),
    _CudldpFastHelloConfigPorts_Type()
)
cudldpFastHelloConfigPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cudldpFastHelloConfigPorts.setStatus("current")
_CudldpFastHelloOperationalPorts_Type = Unsigned32
_CudldpFastHelloOperationalPorts_Object = MibScalar
cudldpFastHelloOperationalPorts = _CudldpFastHelloOperationalPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 1, 3, 4),
    _CudldpFastHelloOperationalPorts_Type()
)
cudldpFastHelloOperationalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cudldpFastHelloOperationalPorts.setStatus("current")
_CiscoUdldpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoUdldpMIBConformance = _CiscoUdldpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3)
)
_CiscoUdldpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUdldpMIBCompliances = _CiscoUdldpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1)
)
_CiscoUdldpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUdldpMIBGroups = _CiscoUdldpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2)
)

# Managed Objects groups

ciscoUdldpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 1)
)
ciscoUdldpMIBGroup.setObjects(
      *(("CISCO-UDLDP-MIB", "cudldpGlobalEnable"),
        ("CISCO-UDLDP-MIB", "cudldpInterfaceEnable"),
        ("CISCO-UDLDP-MIB", "cudldpInterfaceOperStatus"))
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBGroup.setStatus("deprecated")

ciscoUdldpAggreModeOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 2)
)
ciscoUdldpAggreModeOptionalGroup.setObjects(
      *(("CISCO-UDLDP-MIB", "cudldpInterfaceAggressiveMode"),
        ("CISCO-UDLDP-MIB", "cudldpHelloInterval"))
)
if mibBuilder.loadTexts:
    ciscoUdldpAggreModeOptionalGroup.setStatus("deprecated")

ciscoUdldpMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 3)
)
ciscoUdldpMIBGroup2.setObjects(
      *(("CISCO-UDLDP-MIB", "cudldpGlobalMode"),
        ("CISCO-UDLDP-MIB", "cudldpInterfaceAdminMode"),
        ("CISCO-UDLDP-MIB", "cudldpInterfaceOperMode"),
        ("CISCO-UDLDP-MIB", "cudldpHelloInterval"),
        ("CISCO-UDLDP-MIB", "cudldpInterfaceOperStatus"))
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBGroup2.setStatus("current")

ciscoUdldpMIBGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 4)
)
ciscoUdldpMIBGroup3.setObjects(
    ("CISCO-UDLDP-MIB", "cudldpHelloIntervalExt")
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBGroup3.setStatus("current")

ciscoUdldpFastHelloGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 5)
)
ciscoUdldpFastHelloGroup.setObjects(
      *(("CISCO-UDLDP-MIB", "cudldpIfFastHelloInterval"),
        ("CISCO-UDLDP-MIB", "cudldpIfOperHelloInterval"),
        ("CISCO-UDLDP-MIB", "cudldpIfFastHelloOperStatus"),
        ("CISCO-UDLDP-MIB", "cudldpFastHelloErrorReportEnable"),
        ("CISCO-UDLDP-MIB", "cudldpFastHelloLinkFailRptNotifEnable"),
        ("CISCO-UDLDP-MIB", "cudldpFastHelloStatusChangeNotifEnable"),
        ("CISCO-UDLDP-MIB", "cudldpFastHelloMaxPorts"),
        ("CISCO-UDLDP-MIB", "cudldpFastHelloConfigPorts"),
        ("CISCO-UDLDP-MIB", "cudldpFastHelloOperationalPorts"))
)
if mibBuilder.loadTexts:
    ciscoUdldpFastHelloGroup.setStatus("current")


# Notification objects

cudldpFastHelloLinkFailRptNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 0, 1)
)
cudldpFastHelloLinkFailRptNotification.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    cudldpFastHelloLinkFailRptNotification.setStatus(
        "current"
    )

cudldpFastHelloStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 0, 2)
)
cudldpFastHelloStatusChangeNotification.setObjects(
      *(("CISCO-UDLDP-MIB", "cudldpHelloInterval"),
        ("CISCO-UDLDP-MIB", "cudldpIfFastHelloInterval"),
        ("CISCO-UDLDP-MIB", "cudldpIfOperHelloInterval"),
        ("CISCO-UDLDP-MIB", "cudldpIfFastHelloOperStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    cudldpFastHelloStatusChangeNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoUdldpFastHelloNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 2, 6)
)
ciscoUdldpFastHelloNotificationGroup.setObjects(
      *(("CISCO-UDLDP-MIB", "cudldpFastHelloLinkFailRptNotification"),
        ("CISCO-UDLDP-MIB", "cudldpFastHelloStatusChangeNotification"))
)
if mibBuilder.loadTexts:
    ciscoUdldpFastHelloNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoUdldpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoUdldpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoUdldpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoUdldpMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoUdldpMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 118, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoUdldpMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UDLDP-MIB",
    **{"ciscoUdldpMIB": ciscoUdldpMIB,
       "ciscoUdldpMIBNotifs": ciscoUdldpMIBNotifs,
       "cudldpFastHelloLinkFailRptNotification": cudldpFastHelloLinkFailRptNotification,
       "cudldpFastHelloStatusChangeNotification": cudldpFastHelloStatusChangeNotification,
       "ciscoUdldpMIBObjects": ciscoUdldpMIBObjects,
       "cudldpGlobal": cudldpGlobal,
       "cudldpGlobalEnable": cudldpGlobalEnable,
       "cudldpHelloInterval": cudldpHelloInterval,
       "cudldpGlobalMode": cudldpGlobalMode,
       "cudldpHelloIntervalExt": cudldpHelloIntervalExt,
       "cudldpFastHelloLinkFailRptNotifEnable": cudldpFastHelloLinkFailRptNotifEnable,
       "cudldpFastHelloStatusChangeNotifEnable": cudldpFastHelloStatusChangeNotifEnable,
       "cudldpInterface": cudldpInterface,
       "cudldpInterfaceTable": cudldpInterfaceTable,
       "cudldpInterfaceEntry": cudldpInterfaceEntry,
       "cudldpInterfaceEnable": cudldpInterfaceEnable,
       "cudldpInterfaceOperStatus": cudldpInterfaceOperStatus,
       "cudldpInterfaceAggressiveMode": cudldpInterfaceAggressiveMode,
       "cudldpInterfaceAdminMode": cudldpInterfaceAdminMode,
       "cudldpInterfaceOperMode": cudldpInterfaceOperMode,
       "cudldpIfFastHelloInterval": cudldpIfFastHelloInterval,
       "cudldpIfOperHelloInterval": cudldpIfOperHelloInterval,
       "cudldpIfFastHelloOperStatus": cudldpIfFastHelloOperStatus,
       "cudldpFastHello": cudldpFastHello,
       "cudldpFastHelloErrorReportEnable": cudldpFastHelloErrorReportEnable,
       "cudldpFastHelloMaxPorts": cudldpFastHelloMaxPorts,
       "cudldpFastHelloConfigPorts": cudldpFastHelloConfigPorts,
       "cudldpFastHelloOperationalPorts": cudldpFastHelloOperationalPorts,
       "ciscoUdldpMIBConformance": ciscoUdldpMIBConformance,
       "ciscoUdldpMIBCompliances": ciscoUdldpMIBCompliances,
       "ciscoUdldpMIBCompliance": ciscoUdldpMIBCompliance,
       "ciscoUdldpMIBComplianceRev1": ciscoUdldpMIBComplianceRev1,
       "ciscoUdldpMIBComplianceRev2": ciscoUdldpMIBComplianceRev2,
       "ciscoUdldpMIBComplianceRev3": ciscoUdldpMIBComplianceRev3,
       "ciscoUdldpMIBComplianceRev4": ciscoUdldpMIBComplianceRev4,
       "ciscoUdldpMIBGroups": ciscoUdldpMIBGroups,
       "ciscoUdldpMIBGroup": ciscoUdldpMIBGroup,
       "ciscoUdldpAggreModeOptionalGroup": ciscoUdldpAggreModeOptionalGroup,
       "ciscoUdldpMIBGroup2": ciscoUdldpMIBGroup2,
       "ciscoUdldpMIBGroup3": ciscoUdldpMIBGroup3,
       "ciscoUdldpFastHelloGroup": ciscoUdldpFastHelloGroup,
       "ciscoUdldpFastHelloNotificationGroup": ciscoUdldpFastHelloNotificationGroup}
)
