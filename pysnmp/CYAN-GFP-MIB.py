# SNMP MIB module (CYAN-GFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-GFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:09 2024
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

(cyanEntityModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanEnDisabledTc,
 CyanGfpUpiTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanEnDisabledTc",
    "CyanGfpUpiTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc")

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

cyanGFPModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210)
)
cyanGFPModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanGFPMibObjects_ObjectIdentity = ObjectIdentity
cyanGFPMibObjects = _CyanGFPMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1)
)
_CyanGFPTable_Object = MibTable
cyanGFPTable = _CyanGFPTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1)
)
if mibBuilder.loadTexts:
    cyanGFPTable.setStatus("current")
_CyanGFPEntry_Object = MibTableRow
cyanGFPEntry = _CyanGFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1)
)
cyanGFPEntry.setIndexNames(
    (0, "CYAN-GFP-MIB", "cyanGFPShelfId"),
    (0, "CYAN-GFP-MIB", "cyanGFPModuleId"),
    (0, "CYAN-GFP-MIB", "cyanGFPGFPId"),
)
if mibBuilder.loadTexts:
    cyanGFPEntry.setStatus("current")


class _CyanGFPShelfId_Type(Unsigned32):
    """Custom type cyanGFPShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanGFPShelfId_Type.__name__ = "Unsigned32"
_CyanGFPShelfId_Object = MibTableColumn
cyanGFPShelfId = _CyanGFPShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 1),
    _CyanGFPShelfId_Type()
)
cyanGFPShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanGFPShelfId.setStatus("current")
_CyanGFPModuleId_Type = Unsigned32
_CyanGFPModuleId_Object = MibTableColumn
cyanGFPModuleId = _CyanGFPModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 2),
    _CyanGFPModuleId_Type()
)
cyanGFPModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanGFPModuleId.setStatus("current")
_CyanGFPGFPId_Type = Unsigned32
_CyanGFPGFPId_Object = MibTableColumn
cyanGFPGFPId = _CyanGFPGFPId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 3),
    _CyanGFPGFPId_Type()
)
cyanGFPGFPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanGFPGFPId.setStatus("current")


class _CyanGFPAcceptedPayloadFcs_Type(Unsigned32):
    """Custom type cyanGFPAcceptedPayloadFcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanGFPAcceptedPayloadFcs_Type.__name__ = "Unsigned32"
_CyanGFPAcceptedPayloadFcs_Object = MibTableColumn
cyanGFPAcceptedPayloadFcs = _CyanGFPAcceptedPayloadFcs_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 4),
    _CyanGFPAcceptedPayloadFcs_Type()
)
cyanGFPAcceptedPayloadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPAcceptedPayloadFcs.setStatus("current")


class _CyanGFPAcceptedPayloadType_Type(Unsigned32):
    """Custom type cyanGFPAcceptedPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanGFPAcceptedPayloadType_Type.__name__ = "Unsigned32"
_CyanGFPAcceptedPayloadType_Object = MibTableColumn
cyanGFPAcceptedPayloadType = _CyanGFPAcceptedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 5),
    _CyanGFPAcceptedPayloadType_Type()
)
cyanGFPAcceptedPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPAcceptedPayloadType.setStatus("current")


class _CyanGFPAcceptedUserPayload_Type(Unsigned32):
    """Custom type cyanGFPAcceptedUserPayload based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanGFPAcceptedUserPayload_Type.__name__ = "Unsigned32"
_CyanGFPAcceptedUserPayload_Object = MibTableColumn
cyanGFPAcceptedUserPayload = _CyanGFPAcceptedUserPayload_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 6),
    _CyanGFPAcceptedUserPayload_Type()
)
cyanGFPAcceptedUserPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPAcceptedUserPayload.setStatus("current")
_CyanGFPAdminState_Type = CyanAdminStateTc
_CyanGFPAdminState_Object = MibTableColumn
cyanGFPAdminState = _CyanGFPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 7),
    _CyanGFPAdminState_Type()
)
cyanGFPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPAdminState.setStatus("current")
_CyanGFPAutoinserviceSoakTimeSec_Type = Integer32
_CyanGFPAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanGFPAutoinserviceSoakTimeSec = _CyanGFPAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 8),
    _CyanGFPAutoinserviceSoakTimeSec_Type()
)
cyanGFPAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPAutoinserviceSoakTimeSec.setStatus("current")
_CyanGFPClientSignalFail_Type = CyanEnDisabledTc
_CyanGFPClientSignalFail_Object = MibTableColumn
cyanGFPClientSignalFail = _CyanGFPClientSignalFail_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 9),
    _CyanGFPClientSignalFail_Type()
)
cyanGFPClientSignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPClientSignalFail.setStatus("current")
_CyanGFPDiscardErrorFrames_Type = CyanEnDisabledTc
_CyanGFPDiscardErrorFrames_Object = MibTableColumn
cyanGFPDiscardErrorFrames = _CyanGFPDiscardErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 10),
    _CyanGFPDiscardErrorFrames_Type()
)
cyanGFPDiscardErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPDiscardErrorFrames.setStatus("current")
_CyanGFPExpectedUserPayload_Type = CyanGfpUpiTc
_CyanGFPExpectedUserPayload_Object = MibTableColumn
cyanGFPExpectedUserPayload = _CyanGFPExpectedUserPayload_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 11),
    _CyanGFPExpectedUserPayload_Type()
)
cyanGFPExpectedUserPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPExpectedUserPayload.setStatus("current")
_CyanGFPInsertPayloadFcs_Type = CyanEnDisabledTc
_CyanGFPInsertPayloadFcs_Object = MibTableColumn
cyanGFPInsertPayloadFcs = _CyanGFPInsertPayloadFcs_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 12),
    _CyanGFPInsertPayloadFcs_Type()
)
cyanGFPInsertPayloadFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPInsertPayloadFcs.setStatus("current")
_CyanGFPInsertedUserPayload_Type = CyanGfpUpiTc
_CyanGFPInsertedUserPayload_Object = MibTableColumn
cyanGFPInsertedUserPayload = _CyanGFPInsertedUserPayload_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 13),
    _CyanGFPInsertedUserPayload_Type()
)
cyanGFPInsertedUserPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPInsertedUserPayload.setStatus("current")
_CyanGFPOperState_Type = CyanOpStateTc
_CyanGFPOperState_Object = MibTableColumn
cyanGFPOperState = _CyanGFPOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 14),
    _CyanGFPOperState_Type()
)
cyanGFPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPOperState.setStatus("current")
_CyanGFPOperStateQual_Type = CyanOpStateQualTc
_CyanGFPOperStateQual_Object = MibTableColumn
cyanGFPOperStateQual = _CyanGFPOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 15),
    _CyanGFPOperStateQual_Type()
)
cyanGFPOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPOperStateQual.setStatus("current")
_CyanGFPPayloadScrambling_Type = CyanEnDisabledTc
_CyanGFPPayloadScrambling_Object = MibTableColumn
cyanGFPPayloadScrambling = _CyanGFPPayloadScrambling_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 16),
    _CyanGFPPayloadScrambling_Type()
)
cyanGFPPayloadScrambling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPPayloadScrambling.setStatus("current")
_CyanGFPSecServState_Type = CyanSecServiceStateTc
_CyanGFPSecServState_Object = MibTableColumn
cyanGFPSecServState = _CyanGFPSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 1, 1, 1, 17),
    _CyanGFPSecServState_Type()
)
cyanGFPSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGFPSecServState.setStatus("current")

# Managed Objects groups

cyanGFPObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 20)
)
cyanGFPObjectGroup.setObjects(
      *(("CYAN-GFP-MIB", "cyanGFPAcceptedPayloadFcs"),
        ("CYAN-GFP-MIB", "cyanGFPAcceptedPayloadType"),
        ("CYAN-GFP-MIB", "cyanGFPAcceptedUserPayload"),
        ("CYAN-GFP-MIB", "cyanGFPAdminState"),
        ("CYAN-GFP-MIB", "cyanGFPAutoinserviceSoakTimeSec"),
        ("CYAN-GFP-MIB", "cyanGFPClientSignalFail"),
        ("CYAN-GFP-MIB", "cyanGFPDiscardErrorFrames"),
        ("CYAN-GFP-MIB", "cyanGFPExpectedUserPayload"),
        ("CYAN-GFP-MIB", "cyanGFPInsertPayloadFcs"),
        ("CYAN-GFP-MIB", "cyanGFPInsertedUserPayload"),
        ("CYAN-GFP-MIB", "cyanGFPOperState"),
        ("CYAN-GFP-MIB", "cyanGFPOperStateQual"),
        ("CYAN-GFP-MIB", "cyanGFPPayloadScrambling"),
        ("CYAN-GFP-MIB", "cyanGFPSecServState"))
)
if mibBuilder.loadTexts:
    cyanGFPObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanGFPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 210, 30)
)
if mibBuilder.loadTexts:
    cyanGFPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-GFP-MIB",
    **{"cyanGFPModule": cyanGFPModule,
       "cyanGFPMibObjects": cyanGFPMibObjects,
       "cyanGFPTable": cyanGFPTable,
       "cyanGFPEntry": cyanGFPEntry,
       "cyanGFPShelfId": cyanGFPShelfId,
       "cyanGFPModuleId": cyanGFPModuleId,
       "cyanGFPGFPId": cyanGFPGFPId,
       "cyanGFPAcceptedPayloadFcs": cyanGFPAcceptedPayloadFcs,
       "cyanGFPAcceptedPayloadType": cyanGFPAcceptedPayloadType,
       "cyanGFPAcceptedUserPayload": cyanGFPAcceptedUserPayload,
       "cyanGFPAdminState": cyanGFPAdminState,
       "cyanGFPAutoinserviceSoakTimeSec": cyanGFPAutoinserviceSoakTimeSec,
       "cyanGFPClientSignalFail": cyanGFPClientSignalFail,
       "cyanGFPDiscardErrorFrames": cyanGFPDiscardErrorFrames,
       "cyanGFPExpectedUserPayload": cyanGFPExpectedUserPayload,
       "cyanGFPInsertPayloadFcs": cyanGFPInsertPayloadFcs,
       "cyanGFPInsertedUserPayload": cyanGFPInsertedUserPayload,
       "cyanGFPOperState": cyanGFPOperState,
       "cyanGFPOperStateQual": cyanGFPOperStateQual,
       "cyanGFPPayloadScrambling": cyanGFPPayloadScrambling,
       "cyanGFPSecServState": cyanGFPSecServState,
       "cyanGFPObjectGroup": cyanGFPObjectGroup,
       "cyanGFPCompliance": cyanGFPCompliance}
)
