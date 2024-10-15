# SNMP MIB module (CISCO-VISM-SVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-SVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:57 2024
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
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

ciscoVismSvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 90)
)
ciscoVismSvcMIB.setRevisions(
        ("2003-10-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismSvcGrp_ObjectIdentity = ObjectIdentity
vismSvcGrp = _VismSvcGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10)
)
_VismSvcTxSetups_Type = Counter32
_VismSvcTxSetups_Object = MibScalar
vismSvcTxSetups = _VismSvcTxSetups_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 1),
    _VismSvcTxSetups_Type()
)
vismSvcTxSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxSetups.setStatus("current")
_VismSvcRxSetups_Type = Counter32
_VismSvcRxSetups_Object = MibScalar
vismSvcRxSetups = _VismSvcRxSetups_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 2),
    _VismSvcRxSetups_Type()
)
vismSvcRxSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxSetups.setStatus("current")
_VismSvcTxCallProcs_Type = Counter32
_VismSvcTxCallProcs_Object = MibScalar
vismSvcTxCallProcs = _VismSvcTxCallProcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 3),
    _VismSvcTxCallProcs_Type()
)
vismSvcTxCallProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxCallProcs.setStatus("current")
_VismSvcRxCallProcs_Type = Counter32
_VismSvcRxCallProcs_Object = MibScalar
vismSvcRxCallProcs = _VismSvcRxCallProcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 4),
    _VismSvcRxCallProcs_Type()
)
vismSvcRxCallProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxCallProcs.setStatus("current")
_VismSvcTxConns_Type = Counter32
_VismSvcTxConns_Object = MibScalar
vismSvcTxConns = _VismSvcTxConns_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 5),
    _VismSvcTxConns_Type()
)
vismSvcTxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxConns.setStatus("current")
_VismSvcTxConnAcks_Type = Counter32
_VismSvcTxConnAcks_Object = MibScalar
vismSvcTxConnAcks = _VismSvcTxConnAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 6),
    _VismSvcTxConnAcks_Type()
)
vismSvcTxConnAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxConnAcks.setStatus("current")
_VismSvcRxConns_Type = Counter32
_VismSvcRxConns_Object = MibScalar
vismSvcRxConns = _VismSvcRxConns_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 7),
    _VismSvcRxConns_Type()
)
vismSvcRxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxConns.setStatus("current")
_VismSvcRxConnAcks_Type = Counter32
_VismSvcRxConnAcks_Object = MibScalar
vismSvcRxConnAcks = _VismSvcRxConnAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 8),
    _VismSvcRxConnAcks_Type()
)
vismSvcRxConnAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxConnAcks.setStatus("current")
_VismSvcTxReleases_Type = Counter32
_VismSvcTxReleases_Object = MibScalar
vismSvcTxReleases = _VismSvcTxReleases_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 9),
    _VismSvcTxReleases_Type()
)
vismSvcTxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxReleases.setStatus("current")
_VismSvcTxReleaseCompls_Type = Counter32
_VismSvcTxReleaseCompls_Object = MibScalar
vismSvcTxReleaseCompls = _VismSvcTxReleaseCompls_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 10),
    _VismSvcTxReleaseCompls_Type()
)
vismSvcTxReleaseCompls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxReleaseCompls.setStatus("current")
_VismSvcRxReleases_Type = Counter32
_VismSvcRxReleases_Object = MibScalar
vismSvcRxReleases = _VismSvcRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 11),
    _VismSvcRxReleases_Type()
)
vismSvcRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxReleases.setStatus("current")
_VismSvcRxReleaseCompls_Type = Counter32
_VismSvcRxReleaseCompls_Object = MibScalar
vismSvcRxReleaseCompls = _VismSvcRxReleaseCompls_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 12),
    _VismSvcRxReleaseCompls_Type()
)
vismSvcRxReleaseCompls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxReleaseCompls.setStatus("current")
_VismSvcTxRestarts_Type = Counter32
_VismSvcTxRestarts_Object = MibScalar
vismSvcTxRestarts = _VismSvcTxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 13),
    _VismSvcTxRestarts_Type()
)
vismSvcTxRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxRestarts.setStatus("current")
_VismSvcTxRestartAcks_Type = Counter32
_VismSvcTxRestartAcks_Object = MibScalar
vismSvcTxRestartAcks = _VismSvcTxRestartAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 14),
    _VismSvcTxRestartAcks_Type()
)
vismSvcTxRestartAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxRestartAcks.setStatus("current")
_VismSvcRxRestarts_Type = Counter32
_VismSvcRxRestarts_Object = MibScalar
vismSvcRxRestarts = _VismSvcRxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 15),
    _VismSvcRxRestarts_Type()
)
vismSvcRxRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxRestarts.setStatus("current")
_VismSvcRxRestartAcks_Type = Counter32
_VismSvcRxRestartAcks_Object = MibScalar
vismSvcRxRestartAcks = _VismSvcRxRestartAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 16),
    _VismSvcRxRestartAcks_Type()
)
vismSvcRxRestartAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxRestartAcks.setStatus("current")
_VismSvcTxResyncStrts_Type = Counter32
_VismSvcTxResyncStrts_Object = MibScalar
vismSvcTxResyncStrts = _VismSvcTxResyncStrts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 17),
    _VismSvcTxResyncStrts_Type()
)
vismSvcTxResyncStrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxResyncStrts.setStatus("current")
_VismSvcTxResyncStrtAcks_Type = Counter32
_VismSvcTxResyncStrtAcks_Object = MibScalar
vismSvcTxResyncStrtAcks = _VismSvcTxResyncStrtAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 18),
    _VismSvcTxResyncStrtAcks_Type()
)
vismSvcTxResyncStrtAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxResyncStrtAcks.setStatus("current")
_VismSvcRxResyncStrts_Type = Counter32
_VismSvcRxResyncStrts_Object = MibScalar
vismSvcRxResyncStrts = _VismSvcRxResyncStrts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 19),
    _VismSvcRxResyncStrts_Type()
)
vismSvcRxResyncStrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxResyncStrts.setStatus("current")
_VismSvcRxResyncStrtAcks_Type = Counter32
_VismSvcRxResyncStrtAcks_Object = MibScalar
vismSvcRxResyncStrtAcks = _VismSvcRxResyncStrtAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 20),
    _VismSvcRxResyncStrtAcks_Type()
)
vismSvcRxResyncStrtAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxResyncStrtAcks.setStatus("current")
_VismSvcTxResyncEnds_Type = Counter32
_VismSvcTxResyncEnds_Object = MibScalar
vismSvcTxResyncEnds = _VismSvcTxResyncEnds_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 21),
    _VismSvcTxResyncEnds_Type()
)
vismSvcTxResyncEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxResyncEnds.setStatus("current")
_VismSvcTxResyncEndAcks_Type = Counter32
_VismSvcTxResyncEndAcks_Object = MibScalar
vismSvcTxResyncEndAcks = _VismSvcTxResyncEndAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 22),
    _VismSvcTxResyncEndAcks_Type()
)
vismSvcTxResyncEndAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxResyncEndAcks.setStatus("current")
_VismSvcRxResyncEnds_Type = Counter32
_VismSvcRxResyncEnds_Object = MibScalar
vismSvcRxResyncEnds = _VismSvcRxResyncEnds_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 23),
    _VismSvcRxResyncEnds_Type()
)
vismSvcRxResyncEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxResyncEnds.setStatus("current")
_VismSvcRxResyncEndAcks_Type = Counter32
_VismSvcRxResyncEndAcks_Object = MibScalar
vismSvcRxResyncEndAcks = _VismSvcRxResyncEndAcks_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 24),
    _VismSvcRxResyncEndAcks_Type()
)
vismSvcRxResyncEndAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxResyncEndAcks.setStatus("current")
_VismSvcTxBulkResyncs_Type = Counter32
_VismSvcTxBulkResyncs_Object = MibScalar
vismSvcTxBulkResyncs = _VismSvcTxBulkResyncs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 25),
    _VismSvcTxBulkResyncs_Type()
)
vismSvcTxBulkResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcTxBulkResyncs.setStatus("current")
_VismSvcRxBulkResyncs_Type = Counter32
_VismSvcRxBulkResyncs_Object = MibScalar
vismSvcRxBulkResyncs = _VismSvcRxBulkResyncs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 26),
    _VismSvcRxBulkResyncs_Type()
)
vismSvcRxBulkResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRxBulkResyncs.setStatus("current")
_VismSvcCallProcExpiries_Type = Counter32
_VismSvcCallProcExpiries_Object = MibScalar
vismSvcCallProcExpiries = _VismSvcCallProcExpiries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 27),
    _VismSvcCallProcExpiries_Type()
)
vismSvcCallProcExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcCallProcExpiries.setStatus("current")
_VismSvcReleasExpiries_Type = Counter32
_VismSvcReleasExpiries_Object = MibScalar
vismSvcReleasExpiries = _VismSvcReleasExpiries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 28),
    _VismSvcReleasExpiries_Type()
)
vismSvcReleasExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcReleasExpiries.setStatus("current")
_VismSvcConnExpiries_Type = Counter32
_VismSvcConnExpiries_Object = MibScalar
vismSvcConnExpiries = _VismSvcConnExpiries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 29),
    _VismSvcConnExpiries_Type()
)
vismSvcConnExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcConnExpiries.setStatus("current")
_VismSvcConnAckExpiries_Type = Counter32
_VismSvcConnAckExpiries_Object = MibScalar
vismSvcConnAckExpiries = _VismSvcConnAckExpiries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 30),
    _VismSvcConnAckExpiries_Type()
)
vismSvcConnAckExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcConnAckExpiries.setStatus("current")
_VismSvcRestartExpiries_Type = Counter32
_VismSvcRestartExpiries_Object = MibScalar
vismSvcRestartExpiries = _VismSvcRestartExpiries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 31),
    _VismSvcRestartExpiries_Type()
)
vismSvcRestartExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcRestartExpiries.setStatus("current")
_VismSvcResyncExpiries_Type = Counter32
_VismSvcResyncExpiries_Object = MibScalar
vismSvcResyncExpiries = _VismSvcResyncExpiries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 10, 32),
    _VismSvcResyncExpiries_Type()
)
vismSvcResyncExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSvcResyncExpiries.setStatus("current")
_VismSvcCnfGroups_ObjectIdentity = ObjectIdentity
vismSvcCnfGroups = _VismSvcCnfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19)
)
_VismSvcAtmQosGrp_ObjectIdentity = ObjectIdentity
vismSvcAtmQosGrp = _VismSvcAtmQosGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 1)
)


class _VismSvcAtmQosCdv_Type(Integer32):
    """Custom type vismSvcAtmQosCdv based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 20000),
    )


_VismSvcAtmQosCdv_Type.__name__ = "Integer32"
_VismSvcAtmQosCdv_Object = MibScalar
vismSvcAtmQosCdv = _VismSvcAtmQosCdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 1, 1),
    _VismSvcAtmQosCdv_Type()
)
vismSvcAtmQosCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSvcAtmQosCdv.setStatus("current")


class _VismSvcAtmQosCtd_Type(Integer32):
    """Custom type vismSvcAtmQosCtd based on Integer32"""
    defaultValue = 150000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 150000),
    )


_VismSvcAtmQosCtd_Type.__name__ = "Integer32"
_VismSvcAtmQosCtd_Object = MibScalar
vismSvcAtmQosCtd = _VismSvcAtmQosCtd_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 1, 2),
    _VismSvcAtmQosCtd_Type()
)
vismSvcAtmQosCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSvcAtmQosCtd.setStatus("current")


class _VismSvcAtmQosClr_Type(Integer32):
    """Custom type vismSvcAtmQosClr based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_VismSvcAtmQosClr_Type.__name__ = "Integer32"
_VismSvcAtmQosClr_Object = MibScalar
vismSvcAtmQosClr = _VismSvcAtmQosClr_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 1, 3),
    _VismSvcAtmQosClr_Type()
)
vismSvcAtmQosClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSvcAtmQosClr.setStatus("current")
_VismSvcTrfScalingGrp_ObjectIdentity = ObjectIdentity
vismSvcTrfScalingGrp = _VismSvcTrfScalingGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 2)
)


class _VismSvcTrfScalingFactor_Type(Integer32):
    """Custom type vismSvcTrfScalingFactor based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_VismSvcTrfScalingFactor_Type.__name__ = "Integer32"
_VismSvcTrfScalingFactor_Object = MibScalar
vismSvcTrfScalingFactor = _VismSvcTrfScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 2, 1),
    _VismSvcTrfScalingFactor_Type()
)
vismSvcTrfScalingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSvcTrfScalingFactor.setStatus("current")
_VismSvcAal2CidGrp_ObjectIdentity = ObjectIdentity
vismSvcAal2CidGrp = _VismSvcAal2CidGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 3)
)


class _VismSvcAal2CidNumber_Type(Integer32):
    """Custom type vismSvcAal2CidNumber based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 255),
    )


_VismSvcAal2CidNumber_Type.__name__ = "Integer32"
_VismSvcAal2CidNumber_Object = MibScalar
vismSvcAal2CidNumber = _VismSvcAal2CidNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 19, 3, 1),
    _VismSvcAal2CidNumber_Type()
)
vismSvcAal2CidNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSvcAal2CidNumber.setStatus("current")
_CiscoVismSvcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismSvcMIBConformance = _CiscoVismSvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2)
)
_CiscoVismSvcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismSvcMIBGroups = _CiscoVismSvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2, 1)
)
_CiscoVismSvcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismSvcMIBCompliances = _CiscoVismSvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2, 2)
)

# Managed Objects groups

ciscoVismSvcCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2, 1, 1)
)
ciscoVismSvcCounterGroup.setObjects(
      *(("CISCO-VISM-SVC-MIB", "vismSvcTxSetups"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxSetups"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxCallProcs"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxCallProcs"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxConns"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxConnAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxConns"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxConnAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxReleases"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxReleaseCompls"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxReleases"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxReleaseCompls"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxRestarts"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxRestartAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxRestarts"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxRestartAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxResyncStrts"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxResyncStrtAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxResyncStrts"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxResyncStrtAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxResyncEnds"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxResyncEndAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxResyncEnds"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxResyncEndAcks"),
        ("CISCO-VISM-SVC-MIB", "vismSvcTxBulkResyncs"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRxBulkResyncs"),
        ("CISCO-VISM-SVC-MIB", "vismSvcCallProcExpiries"),
        ("CISCO-VISM-SVC-MIB", "vismSvcReleasExpiries"),
        ("CISCO-VISM-SVC-MIB", "vismSvcConnExpiries"),
        ("CISCO-VISM-SVC-MIB", "vismSvcConnAckExpiries"),
        ("CISCO-VISM-SVC-MIB", "vismSvcRestartExpiries"),
        ("CISCO-VISM-SVC-MIB", "vismSvcResyncExpiries"))
)
if mibBuilder.loadTexts:
    ciscoVismSvcCounterGroup.setStatus("current")

ciscoVismSvcAtmQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2, 1, 2)
)
ciscoVismSvcAtmQosGroup.setObjects(
      *(("CISCO-VISM-SVC-MIB", "vismSvcAtmQosCdv"),
        ("CISCO-VISM-SVC-MIB", "vismSvcAtmQosCtd"),
        ("CISCO-VISM-SVC-MIB", "vismSvcAtmQosClr"))
)
if mibBuilder.loadTexts:
    ciscoVismSvcAtmQosGroup.setStatus("current")

ciscoVismSvcTrfScalingGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2, 1, 3)
)
ciscoVismSvcTrfScalingGrp.setObjects(
    ("CISCO-VISM-SVC-MIB", "vismSvcTrfScalingFactor")
)
if mibBuilder.loadTexts:
    ciscoVismSvcTrfScalingGrp.setStatus("current")

ciscoVismSvcAal2CidGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2, 1, 4)
)
ciscoVismSvcAal2CidGrp.setObjects(
    ("CISCO-VISM-SVC-MIB", "vismSvcAal2CidNumber")
)
if mibBuilder.loadTexts:
    ciscoVismSvcAal2CidGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismSvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 90, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismSvcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-SVC-MIB",
    **{"vismSvcGrp": vismSvcGrp,
       "vismSvcTxSetups": vismSvcTxSetups,
       "vismSvcRxSetups": vismSvcRxSetups,
       "vismSvcTxCallProcs": vismSvcTxCallProcs,
       "vismSvcRxCallProcs": vismSvcRxCallProcs,
       "vismSvcTxConns": vismSvcTxConns,
       "vismSvcTxConnAcks": vismSvcTxConnAcks,
       "vismSvcRxConns": vismSvcRxConns,
       "vismSvcRxConnAcks": vismSvcRxConnAcks,
       "vismSvcTxReleases": vismSvcTxReleases,
       "vismSvcTxReleaseCompls": vismSvcTxReleaseCompls,
       "vismSvcRxReleases": vismSvcRxReleases,
       "vismSvcRxReleaseCompls": vismSvcRxReleaseCompls,
       "vismSvcTxRestarts": vismSvcTxRestarts,
       "vismSvcTxRestartAcks": vismSvcTxRestartAcks,
       "vismSvcRxRestarts": vismSvcRxRestarts,
       "vismSvcRxRestartAcks": vismSvcRxRestartAcks,
       "vismSvcTxResyncStrts": vismSvcTxResyncStrts,
       "vismSvcTxResyncStrtAcks": vismSvcTxResyncStrtAcks,
       "vismSvcRxResyncStrts": vismSvcRxResyncStrts,
       "vismSvcRxResyncStrtAcks": vismSvcRxResyncStrtAcks,
       "vismSvcTxResyncEnds": vismSvcTxResyncEnds,
       "vismSvcTxResyncEndAcks": vismSvcTxResyncEndAcks,
       "vismSvcRxResyncEnds": vismSvcRxResyncEnds,
       "vismSvcRxResyncEndAcks": vismSvcRxResyncEndAcks,
       "vismSvcTxBulkResyncs": vismSvcTxBulkResyncs,
       "vismSvcRxBulkResyncs": vismSvcRxBulkResyncs,
       "vismSvcCallProcExpiries": vismSvcCallProcExpiries,
       "vismSvcReleasExpiries": vismSvcReleasExpiries,
       "vismSvcConnExpiries": vismSvcConnExpiries,
       "vismSvcConnAckExpiries": vismSvcConnAckExpiries,
       "vismSvcRestartExpiries": vismSvcRestartExpiries,
       "vismSvcResyncExpiries": vismSvcResyncExpiries,
       "vismSvcCnfGroups": vismSvcCnfGroups,
       "vismSvcAtmQosGrp": vismSvcAtmQosGrp,
       "vismSvcAtmQosCdv": vismSvcAtmQosCdv,
       "vismSvcAtmQosCtd": vismSvcAtmQosCtd,
       "vismSvcAtmQosClr": vismSvcAtmQosClr,
       "vismSvcTrfScalingGrp": vismSvcTrfScalingGrp,
       "vismSvcTrfScalingFactor": vismSvcTrfScalingFactor,
       "vismSvcAal2CidGrp": vismSvcAal2CidGrp,
       "vismSvcAal2CidNumber": vismSvcAal2CidNumber,
       "ciscoVismSvcMIB": ciscoVismSvcMIB,
       "ciscoVismSvcMIBConformance": ciscoVismSvcMIBConformance,
       "ciscoVismSvcMIBGroups": ciscoVismSvcMIBGroups,
       "ciscoVismSvcCounterGroup": ciscoVismSvcCounterGroup,
       "ciscoVismSvcAtmQosGroup": ciscoVismSvcAtmQosGroup,
       "ciscoVismSvcTrfScalingGrp": ciscoVismSvcTrfScalingGrp,
       "ciscoVismSvcAal2CidGrp": ciscoVismSvcAal2CidGrp,
       "ciscoVismSvcMIBCompliances": ciscoVismSvcMIBCompliances,
       "ciscoVismSvcCompliance": ciscoVismSvcCompliance}
)
