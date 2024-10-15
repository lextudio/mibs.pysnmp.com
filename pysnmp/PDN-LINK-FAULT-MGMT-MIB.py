# SNMP MIB module (PDN-LINK-FAULT-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-LINK-FAULT-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:50 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdnLinkFaultMgmt,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnLinkFaultMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pdnLinkFaultMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1)
)
pdnLinkFaultMgmtMIB.setRevisions(
        ("2003-04-23 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnLinkFaultMgmtMIBObjects_ObjectIdentity = ObjectIdentity
pdnLinkFaultMgmtMIBObjects = _PdnLinkFaultMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1)
)


class _PdnLinkFaultMgmtApsSelection_Type(Integer32):
    """Custom type pdnLinkFaultMgmtApsSelection based on Integer32"""
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


_PdnLinkFaultMgmtApsSelection_Type.__name__ = "Integer32"
_PdnLinkFaultMgmtApsSelection_Object = MibScalar
pdnLinkFaultMgmtApsSelection = _PdnLinkFaultMgmtApsSelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 1),
    _PdnLinkFaultMgmtApsSelection_Type()
)
pdnLinkFaultMgmtApsSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFaultMgmtApsSelection.setStatus("current")


class _PdnLinkFaultMgmtSwitchoverSelection_Type(Integer32):
    """Custom type pdnLinkFaultMgmtSwitchoverSelection based on Integer32"""
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


_PdnLinkFaultMgmtSwitchoverSelection_Type.__name__ = "Integer32"
_PdnLinkFaultMgmtSwitchoverSelection_Object = MibScalar
pdnLinkFaultMgmtSwitchoverSelection = _PdnLinkFaultMgmtSwitchoverSelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 2),
    _PdnLinkFaultMgmtSwitchoverSelection_Type()
)
pdnLinkFaultMgmtSwitchoverSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFaultMgmtSwitchoverSelection.setStatus("current")
_PdnLinkFailureConfigTable_Object = MibTable
pdnLinkFailureConfigTable = _PdnLinkFailureConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pdnLinkFailureConfigTable.setStatus("current")
_PdnLinkFailureConfigEntry_Object = MibTableRow
pdnLinkFailureConfigEntry = _PdnLinkFailureConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1)
)
pdnLinkFailureConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnLinkFailureConfigEntry.setStatus("current")


class _PdnLinkFailureLOSPeriodBeforeSwitching_Type(Integer32):
    """Custom type pdnLinkFailureLOSPeriodBeforeSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PdnLinkFailureLOSPeriodBeforeSwitching_Type.__name__ = "Integer32"
_PdnLinkFailureLOSPeriodBeforeSwitching_Object = MibTableColumn
pdnLinkFailureLOSPeriodBeforeSwitching = _PdnLinkFailureLOSPeriodBeforeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1, 1),
    _PdnLinkFailureLOSPeriodBeforeSwitching_Type()
)
pdnLinkFailureLOSPeriodBeforeSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFailureLOSPeriodBeforeSwitching.setStatus("current")
if mibBuilder.loadTexts:
    pdnLinkFailureLOSPeriodBeforeSwitching.setUnits("seconds")


class _PdnLinkFailureLOFPeriodBeforeSwitching_Type(Integer32):
    """Custom type pdnLinkFailureLOFPeriodBeforeSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PdnLinkFailureLOFPeriodBeforeSwitching_Type.__name__ = "Integer32"
_PdnLinkFailureLOFPeriodBeforeSwitching_Object = MibTableColumn
pdnLinkFailureLOFPeriodBeforeSwitching = _PdnLinkFailureLOFPeriodBeforeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1, 2),
    _PdnLinkFailureLOFPeriodBeforeSwitching_Type()
)
pdnLinkFailureLOFPeriodBeforeSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFailureLOFPeriodBeforeSwitching.setStatus("current")
if mibBuilder.loadTexts:
    pdnLinkFailureLOFPeriodBeforeSwitching.setUnits("seconds")


class _PdnLinkFailureAISLPeriodBeforeSwitching_Type(Integer32):
    """Custom type pdnLinkFailureAISLPeriodBeforeSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PdnLinkFailureAISLPeriodBeforeSwitching_Type.__name__ = "Integer32"
_PdnLinkFailureAISLPeriodBeforeSwitching_Object = MibTableColumn
pdnLinkFailureAISLPeriodBeforeSwitching = _PdnLinkFailureAISLPeriodBeforeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1, 3),
    _PdnLinkFailureAISLPeriodBeforeSwitching_Type()
)
pdnLinkFailureAISLPeriodBeforeSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFailureAISLPeriodBeforeSwitching.setStatus("current")
if mibBuilder.loadTexts:
    pdnLinkFailureAISLPeriodBeforeSwitching.setUnits("seconds")


class _PdnLinkFailureSdPeriodBeforeSwitching_Type(Integer32):
    """Custom type pdnLinkFailureSdPeriodBeforeSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PdnLinkFailureSdPeriodBeforeSwitching_Type.__name__ = "Integer32"
_PdnLinkFailureSdPeriodBeforeSwitching_Object = MibTableColumn
pdnLinkFailureSdPeriodBeforeSwitching = _PdnLinkFailureSdPeriodBeforeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1, 4),
    _PdnLinkFailureSdPeriodBeforeSwitching_Type()
)
pdnLinkFailureSdPeriodBeforeSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFailureSdPeriodBeforeSwitching.setStatus("current")
if mibBuilder.loadTexts:
    pdnLinkFailureSdPeriodBeforeSwitching.setUnits("seconds")


class _PdnLinkFailureSfPeriodBeforeSwitching_Type(Integer32):
    """Custom type pdnLinkFailureSfPeriodBeforeSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PdnLinkFailureSfPeriodBeforeSwitching_Type.__name__ = "Integer32"
_PdnLinkFailureSfPeriodBeforeSwitching_Object = MibTableColumn
pdnLinkFailureSfPeriodBeforeSwitching = _PdnLinkFailureSfPeriodBeforeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1, 5),
    _PdnLinkFailureSfPeriodBeforeSwitching_Type()
)
pdnLinkFailureSfPeriodBeforeSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFailureSfPeriodBeforeSwitching.setStatus("current")
if mibBuilder.loadTexts:
    pdnLinkFailureSfPeriodBeforeSwitching.setUnits("seconds")


class _PdnLinkFailureSdBerThreshold_Type(Integer32):
    """Custom type pdnLinkFailureSdBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_PdnLinkFailureSdBerThreshold_Type.__name__ = "Integer32"
_PdnLinkFailureSdBerThreshold_Object = MibTableColumn
pdnLinkFailureSdBerThreshold = _PdnLinkFailureSdBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1, 6),
    _PdnLinkFailureSdBerThreshold_Type()
)
pdnLinkFailureSdBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFailureSdBerThreshold.setStatus("current")


class _PdnLinkFailureSfBerThreshold_Type(Integer32):
    """Custom type pdnLinkFailureSfBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_PdnLinkFailureSfBerThreshold_Type.__name__ = "Integer32"
_PdnLinkFailureSfBerThreshold_Object = MibTableColumn
pdnLinkFailureSfBerThreshold = _PdnLinkFailureSfBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 3, 1, 7),
    _PdnLinkFailureSfBerThreshold_Type()
)
pdnLinkFailureSfBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnLinkFailureSfBerThreshold.setStatus("current")


class _PdnDualLinkSelection_Type(Integer32):
    """Custom type pdnDualLinkSelection based on Integer32"""
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


_PdnDualLinkSelection_Type.__name__ = "Integer32"
_PdnDualLinkSelection_Object = MibScalar
pdnDualLinkSelection = _PdnDualLinkSelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 1, 4),
    _PdnDualLinkSelection_Type()
)
pdnDualLinkSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDualLinkSelection.setStatus("current")
_PdnLinkFaultMgmtMIBConformance_ObjectIdentity = ObjectIdentity
pdnLinkFaultMgmtMIBConformance = _PdnLinkFaultMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 2)
)
_PdnLinkFaultMgmtCompliances_ObjectIdentity = ObjectIdentity
pdnLinkFaultMgmtCompliances = _PdnLinkFaultMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 2, 1)
)
_PdnLinkFaultMgmtGroups_ObjectIdentity = ObjectIdentity
pdnLinkFaultMgmtGroups = _PdnLinkFaultMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 2, 2)
)

# Managed Objects groups

pdnLinkFaultMgmtGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 2, 2, 1)
)
pdnLinkFaultMgmtGeneralGroup.setObjects(
      *(("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFaultMgmtApsSelection"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFaultMgmtSwitchoverSelection"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnDualLinkSelection"))
)
if mibBuilder.loadTexts:
    pdnLinkFaultMgmtGeneralGroup.setStatus("current")

pdnLinkSwitchoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 2, 2, 2)
)
pdnLinkSwitchoverGroup.setObjects(
      *(("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFailureLOSPeriodBeforeSwitching"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFailureLOFPeriodBeforeSwitching"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFailureAISLPeriodBeforeSwitching"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFailureSdPeriodBeforeSwitching"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFailureSfPeriodBeforeSwitching"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFailureSdBerThreshold"),
        ("PDN-LINK-FAULT-MGMT-MIB", "pdnLinkFailureSfBerThreshold"))
)
if mibBuilder.loadTexts:
    pdnLinkSwitchoverGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnLinkFaultMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 40, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pdnLinkFaultMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-LINK-FAULT-MGMT-MIB",
    **{"pdnLinkFaultMgmtMIB": pdnLinkFaultMgmtMIB,
       "pdnLinkFaultMgmtMIBObjects": pdnLinkFaultMgmtMIBObjects,
       "pdnLinkFaultMgmtApsSelection": pdnLinkFaultMgmtApsSelection,
       "pdnLinkFaultMgmtSwitchoverSelection": pdnLinkFaultMgmtSwitchoverSelection,
       "pdnLinkFailureConfigTable": pdnLinkFailureConfigTable,
       "pdnLinkFailureConfigEntry": pdnLinkFailureConfigEntry,
       "pdnLinkFailureLOSPeriodBeforeSwitching": pdnLinkFailureLOSPeriodBeforeSwitching,
       "pdnLinkFailureLOFPeriodBeforeSwitching": pdnLinkFailureLOFPeriodBeforeSwitching,
       "pdnLinkFailureAISLPeriodBeforeSwitching": pdnLinkFailureAISLPeriodBeforeSwitching,
       "pdnLinkFailureSdPeriodBeforeSwitching": pdnLinkFailureSdPeriodBeforeSwitching,
       "pdnLinkFailureSfPeriodBeforeSwitching": pdnLinkFailureSfPeriodBeforeSwitching,
       "pdnLinkFailureSdBerThreshold": pdnLinkFailureSdBerThreshold,
       "pdnLinkFailureSfBerThreshold": pdnLinkFailureSfBerThreshold,
       "pdnDualLinkSelection": pdnDualLinkSelection,
       "pdnLinkFaultMgmtMIBConformance": pdnLinkFaultMgmtMIBConformance,
       "pdnLinkFaultMgmtCompliances": pdnLinkFaultMgmtCompliances,
       "pdnLinkFaultMgmtCompliance": pdnLinkFaultMgmtCompliance,
       "pdnLinkFaultMgmtGroups": pdnLinkFaultMgmtGroups,
       "pdnLinkFaultMgmtGeneralGroup": pdnLinkFaultMgmtGeneralGroup,
       "pdnLinkSwitchoverGroup": pdnLinkSwitchoverGroup}
)
