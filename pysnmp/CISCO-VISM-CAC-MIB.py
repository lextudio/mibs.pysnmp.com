# SNMP MIB module (CISCO-VISM-CAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-CAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:46 2024
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

(vismChanCnfGrp,
 voice) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "vismChanCnfGrp",
    "voice")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoVismCacMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 96)
)
ciscoVismCacMIB.setRevisions(
        ("2004-02-20 00:00",
         "2003-06-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismChanCacTable_Object = MibTable
vismChanCacTable = _VismChanCacTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vismChanCacTable.setStatus("current")
_VismChanCacEntry_Object = MibTableRow
vismChanCacEntry = _VismChanCacEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1)
)
vismChanCacEntry.setIndexNames(
    (0, "CISCO-VISM-CAC-MIB", "vismChanNum"),
)
if mibBuilder.loadTexts:
    vismChanCacEntry.setStatus("current")


class _VismChanNum_Type(Integer32):
    """Custom type vismChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismChanNum_Type.__name__ = "Integer32"
_VismChanNum_Object = MibTableColumn
vismChanNum = _VismChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 1),
    _VismChanNum_Type()
)
vismChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanNum.setStatus("current")


class _VismChanCacMaster_Type(Integer32):
    """Custom type vismChanCacMaster based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_VismChanCacMaster_Type.__name__ = "Integer32"
_VismChanCacMaster_Object = MibTableColumn
vismChanCacMaster = _VismChanCacMaster_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 2),
    _VismChanCacMaster_Type()
)
vismChanCacMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanCacMaster.setStatus("current")
_VismChanCacPassedCons_Type = Counter32
_VismChanCacPassedCons_Object = MibTableColumn
vismChanCacPassedCons = _VismChanCacPassedCons_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 3),
    _VismChanCacPassedCons_Type()
)
vismChanCacPassedCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanCacPassedCons.setStatus("current")
_VismChanCacRejectedCons_Type = Counter32
_VismChanCacRejectedCons_Object = MibTableColumn
vismChanCacRejectedCons = _VismChanCacRejectedCons_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 4),
    _VismChanCacRejectedCons_Type()
)
vismChanCacRejectedCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanCacRejectedCons.setStatus("current")


class _VismChanCacRejectionPolicy_Type(Integer32):
    """Custom type vismChanCacRejectionPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("maintain", 2),
          ("unspecified", 3))
    )


_VismChanCacRejectionPolicy_Type.__name__ = "Integer32"
_VismChanCacRejectionPolicy_Object = MibTableColumn
vismChanCacRejectionPolicy = _VismChanCacRejectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 5),
    _VismChanCacRejectionPolicy_Type()
)
vismChanCacRejectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanCacRejectionPolicy.setStatus("current")


class _VismChanCarrierLossPolicy_Type(Integer32):
    """Custom type vismChanCarrierLossPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("previousCodec", 1),
          ("unspecified", 3),
          ("upspeedCodec", 2))
    )


_VismChanCarrierLossPolicy_Type.__name__ = "Integer32"
_VismChanCarrierLossPolicy_Object = MibTableColumn
vismChanCarrierLossPolicy = _VismChanCarrierLossPolicy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 6),
    _VismChanCarrierLossPolicy_Type()
)
vismChanCarrierLossPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanCarrierLossPolicy.setStatus("current")


class _VismChanVADTolerance_Type(Integer32):
    """Custom type vismChanVADTolerance based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VismChanVADTolerance_Type.__name__ = "Integer32"
_VismChanVADTolerance_Object = MibTableColumn
vismChanVADTolerance = _VismChanVADTolerance_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 7),
    _VismChanVADTolerance_Type()
)
vismChanVADTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanVADTolerance.setStatus("current")
if mibBuilder.loadTexts:
    vismChanVADTolerance.setUnits("0.0001 percentage")


class _VismChanVADDutyCycle_Type(Integer32):
    """Custom type vismChanVADDutyCycle based on Integer32"""
    defaultValue = 61

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismChanVADDutyCycle_Type.__name__ = "Integer32"
_VismChanVADDutyCycle_Object = MibTableColumn
vismChanVADDutyCycle = _VismChanVADDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 8),
    _VismChanVADDutyCycle_Type()
)
vismChanVADDutyCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanVADDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    vismChanVADDutyCycle.setUnits("0.01 percentage")


class _NetworkCacConfigState_Type(Integer32):
    """Custom type networkCacConfigState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("ok", 1))
    )


_NetworkCacConfigState_Type.__name__ = "Integer32"
_NetworkCacConfigState_Object = MibTableColumn
networkCacConfigState = _NetworkCacConfigState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 3, 1, 9),
    _NetworkCacConfigState_Type()
)
networkCacConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkCacConfigState.setStatus("current")
_VismCardCacFailuresGrp_ObjectIdentity = ObjectIdentity
vismCardCacFailuresGrp = _VismCardCacFailuresGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20)
)
_VismPortCacPvcAddFailures_Type = Counter32
_VismPortCacPvcAddFailures_Object = MibScalar
vismPortCacPvcAddFailures = _VismPortCacPvcAddFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 1),
    _VismPortCacPvcAddFailures_Type()
)
vismPortCacPvcAddFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPortCacPvcAddFailures.setStatus("current")
_VismPortCacSvcAddFailures_Type = Counter32
_VismPortCacSvcAddFailures_Object = MibScalar
vismPortCacSvcAddFailures = _VismPortCacSvcAddFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 2),
    _VismPortCacSvcAddFailures_Type()
)
vismPortCacSvcAddFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPortCacSvcAddFailures.setStatus("current")
_VismVcCacPvcFailures_Type = Counter32
_VismVcCacPvcFailures_Object = MibScalar
vismVcCacPvcFailures = _VismVcCacPvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 3),
    _VismVcCacPvcFailures_Type()
)
vismVcCacPvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismVcCacPvcFailures.setStatus("current")
_VismVcCacPvcUpspeedFailures_Type = Counter32
_VismVcCacPvcUpspeedFailures_Object = MibScalar
vismVcCacPvcUpspeedFailures = _VismVcCacPvcUpspeedFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 4),
    _VismVcCacPvcUpspeedFailures_Type()
)
vismVcCacPvcUpspeedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismVcCacPvcUpspeedFailures.setStatus("current")
_VismPortCacSvcUpspeedFailures_Type = Counter32
_VismPortCacSvcUpspeedFailures_Object = MibScalar
vismPortCacSvcUpspeedFailures = _VismPortCacSvcUpspeedFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 20, 5),
    _VismPortCacSvcUpspeedFailures_Type()
)
vismPortCacSvcUpspeedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismPortCacSvcUpspeedFailures.setStatus("current")
_CiscoVismCacMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismCacMIBConformance = _CiscoVismCacMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 96, 2)
)
_CiscoVismCacMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismCacMIBGroups = _CiscoVismCacMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 1)
)
_CiscoVismCacMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismCacMIBCompliances = _CiscoVismCacMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 2)
)

# Managed Objects groups

ciscoVismChanCacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 1, 1)
)
ciscoVismChanCacGroup.setObjects(
      *(("CISCO-VISM-CAC-MIB", "vismChanNum"),
        ("CISCO-VISM-CAC-MIB", "vismChanCacMaster"),
        ("CISCO-VISM-CAC-MIB", "vismChanCacPassedCons"),
        ("CISCO-VISM-CAC-MIB", "vismChanCacRejectedCons"),
        ("CISCO-VISM-CAC-MIB", "vismChanCacRejectionPolicy"),
        ("CISCO-VISM-CAC-MIB", "vismChanCarrierLossPolicy"),
        ("CISCO-VISM-CAC-MIB", "vismChanVADTolerance"),
        ("CISCO-VISM-CAC-MIB", "vismChanVADDutyCycle"),
        ("CISCO-VISM-CAC-MIB", "networkCacConfigState"))
)
if mibBuilder.loadTexts:
    ciscoVismChanCacGroup.setStatus("current")

ciscoVismCardCacFailuresGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 1, 2)
)
ciscoVismCardCacFailuresGrp.setObjects(
      *(("CISCO-VISM-CAC-MIB", "vismPortCacPvcAddFailures"),
        ("CISCO-VISM-CAC-MIB", "vismPortCacSvcAddFailures"),
        ("CISCO-VISM-CAC-MIB", "vismVcCacPvcFailures"),
        ("CISCO-VISM-CAC-MIB", "vismVcCacPvcUpspeedFailures"),
        ("CISCO-VISM-CAC-MIB", "vismPortCacSvcUpspeedFailures"))
)
if mibBuilder.loadTexts:
    ciscoVismCardCacFailuresGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismCacCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 96, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismCacCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-CAC-MIB",
    **{"vismChanCacTable": vismChanCacTable,
       "vismChanCacEntry": vismChanCacEntry,
       "vismChanNum": vismChanNum,
       "vismChanCacMaster": vismChanCacMaster,
       "vismChanCacPassedCons": vismChanCacPassedCons,
       "vismChanCacRejectedCons": vismChanCacRejectedCons,
       "vismChanCacRejectionPolicy": vismChanCacRejectionPolicy,
       "vismChanCarrierLossPolicy": vismChanCarrierLossPolicy,
       "vismChanVADTolerance": vismChanVADTolerance,
       "vismChanVADDutyCycle": vismChanVADDutyCycle,
       "networkCacConfigState": networkCacConfigState,
       "vismCardCacFailuresGrp": vismCardCacFailuresGrp,
       "vismPortCacPvcAddFailures": vismPortCacPvcAddFailures,
       "vismPortCacSvcAddFailures": vismPortCacSvcAddFailures,
       "vismVcCacPvcFailures": vismVcCacPvcFailures,
       "vismVcCacPvcUpspeedFailures": vismVcCacPvcUpspeedFailures,
       "vismPortCacSvcUpspeedFailures": vismPortCacSvcUpspeedFailures,
       "ciscoVismCacMIB": ciscoVismCacMIB,
       "ciscoVismCacMIBConformance": ciscoVismCacMIBConformance,
       "ciscoVismCacMIBGroups": ciscoVismCacMIBGroups,
       "ciscoVismChanCacGroup": ciscoVismChanCacGroup,
       "ciscoVismCardCacFailuresGrp": ciscoVismCardCacFailuresGrp,
       "ciscoVismCacMIBCompliances": ciscoVismCacMIBCompliances,
       "ciscoVismCacCompliance": ciscoVismCacCompliance}
)
