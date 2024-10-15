# SNMP MIB module (Wellfleet-AT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-AT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:48 2024
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

(wfAppletalkGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAppletalkGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAppleBase_ObjectIdentity = ObjectIdentity
wfAppleBase = _WfAppleBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1)
)


class _WfAppleBaseDelete_Type(Integer32):
    """Custom type wfAppleBaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppleBaseDelete_Type.__name__ = "Integer32"
_WfAppleBaseDelete_Object = MibScalar
wfAppleBaseDelete = _WfAppleBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 1),
    _WfAppleBaseDelete_Type()
)
wfAppleBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDelete.setStatus("mandatory")


class _WfAppleBaseDisable_Type(Integer32):
    """Custom type wfAppleBaseDisable based on Integer32"""
    defaultValue = 1

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


_WfAppleBaseDisable_Type.__name__ = "Integer32"
_WfAppleBaseDisable_Object = MibScalar
wfAppleBaseDisable = _WfAppleBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 2),
    _WfAppleBaseDisable_Type()
)
wfAppleBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDisable.setStatus("mandatory")


class _WfAppleBaseState_Type(Integer32):
    """Custom type wfAppleBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfAppleBaseState_Type.__name__ = "Integer32"
_WfAppleBaseState_Object = MibScalar
wfAppleBaseState = _WfAppleBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 3),
    _WfAppleBaseState_Type()
)
wfAppleBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseState.setStatus("mandatory")
_WfAppleBaseDebugLevel_Type = Integer32
_WfAppleBaseDebugLevel_Object = MibScalar
wfAppleBaseDebugLevel = _WfAppleBaseDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 4),
    _WfAppleBaseDebugLevel_Type()
)
wfAppleBaseDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDebugLevel.setStatus("mandatory")


class _WfAppleBaseDdpQueLen_Type(Integer32):
    """Custom type wfAppleBaseDdpQueLen based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_WfAppleBaseDdpQueLen_Type.__name__ = "Integer32"
_WfAppleBaseDdpQueLen_Object = MibScalar
wfAppleBaseDdpQueLen = _WfAppleBaseDdpQueLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 5),
    _WfAppleBaseDdpQueLen_Type()
)
wfAppleBaseDdpQueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseDdpQueLen.setStatus("mandatory")
_WfAppleBaseHomedPort_Type = Integer32
_WfAppleBaseHomedPort_Object = MibScalar
wfAppleBaseHomedPort = _WfAppleBaseHomedPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 6),
    _WfAppleBaseHomedPort_Type()
)
wfAppleBaseHomedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseHomedPort.setStatus("mandatory")
_WfAppleBaseTotalNets_Type = Integer32
_WfAppleBaseTotalNets_Object = MibScalar
wfAppleBaseTotalNets = _WfAppleBaseTotalNets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 7),
    _WfAppleBaseTotalNets_Type()
)
wfAppleBaseTotalNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseTotalNets.setStatus("mandatory")
_WfAppleBaseTotalZones_Type = Integer32
_WfAppleBaseTotalZones_Object = MibScalar
wfAppleBaseTotalZones = _WfAppleBaseTotalZones_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 8),
    _WfAppleBaseTotalZones_Type()
)
wfAppleBaseTotalZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseTotalZones.setStatus("mandatory")
_WfAppleBaseTotalZoneNames_Type = Integer32
_WfAppleBaseTotalZoneNames_Object = MibScalar
wfAppleBaseTotalZoneNames = _WfAppleBaseTotalZoneNames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 9),
    _WfAppleBaseTotalZoneNames_Type()
)
wfAppleBaseTotalZoneNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseTotalZoneNames.setStatus("mandatory")
_WfAppleBaseTotalAarpEntries_Type = Integer32
_WfAppleBaseTotalAarpEntries_Object = MibScalar
wfAppleBaseTotalAarpEntries = _WfAppleBaseTotalAarpEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 10),
    _WfAppleBaseTotalAarpEntries_Type()
)
wfAppleBaseTotalAarpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleBaseTotalAarpEntries.setStatus("mandatory")
_WfAppleBaseEstimatedNets_Type = Integer32
_WfAppleBaseEstimatedNets_Object = MibScalar
wfAppleBaseEstimatedNets = _WfAppleBaseEstimatedNets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 11),
    _WfAppleBaseEstimatedNets_Type()
)
wfAppleBaseEstimatedNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseEstimatedNets.setStatus("mandatory")
_WfAppleBaseEstimatedHosts_Type = Integer32
_WfAppleBaseEstimatedHosts_Object = MibScalar
wfAppleBaseEstimatedHosts = _WfAppleBaseEstimatedHosts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 12),
    _WfAppleBaseEstimatedHosts_Type()
)
wfAppleBaseEstimatedHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleBaseEstimatedHosts.setStatus("mandatory")


class _WfAppleMacIPBaseDelete_Type(Integer32):
    """Custom type wfAppleMacIPBaseDelete based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppleMacIPBaseDelete_Type.__name__ = "Integer32"
_WfAppleMacIPBaseDelete_Object = MibScalar
wfAppleMacIPBaseDelete = _WfAppleMacIPBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 13),
    _WfAppleMacIPBaseDelete_Type()
)
wfAppleMacIPBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleMacIPBaseDelete.setStatus("mandatory")


class _WfAppleMacIPBaseDisable_Type(Integer32):
    """Custom type wfAppleMacIPBaseDisable based on Integer32"""
    defaultValue = 2

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


_WfAppleMacIPBaseDisable_Type.__name__ = "Integer32"
_WfAppleMacIPBaseDisable_Object = MibScalar
wfAppleMacIPBaseDisable = _WfAppleMacIPBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 14),
    _WfAppleMacIPBaseDisable_Type()
)
wfAppleMacIPBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleMacIPBaseDisable.setStatus("mandatory")


class _WfAppleMacIPBaseState_Type(Integer32):
    """Custom type wfAppleMacIPBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfAppleMacIPBaseState_Type.__name__ = "Integer32"
_WfAppleMacIPBaseState_Object = MibScalar
wfAppleMacIPBaseState = _WfAppleMacIPBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 15),
    _WfAppleMacIPBaseState_Type()
)
wfAppleMacIPBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleMacIPBaseState.setStatus("mandatory")
_WfAppleMacIPZone_Type = DisplayString
_WfAppleMacIPZone_Object = MibScalar
wfAppleMacIPZone = _WfAppleMacIPZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 16),
    _WfAppleMacIPZone_Type()
)
wfAppleMacIPZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleMacIPZone.setStatus("mandatory")
_WfMacIPAddress1_Type = IpAddress
_WfMacIPAddress1_Object = MibScalar
wfMacIPAddress1 = _WfMacIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 17),
    _WfMacIPAddress1_Type()
)
wfMacIPAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPAddress1.setStatus("mandatory")


class _WfMacIPLowerIpAddress1_Type(Integer32):
    """Custom type wfMacIPLowerIpAddress1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfMacIPLowerIpAddress1_Type.__name__ = "Integer32"
_WfMacIPLowerIpAddress1_Object = MibScalar
wfMacIPLowerIpAddress1 = _WfMacIPLowerIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 18),
    _WfMacIPLowerIpAddress1_Type()
)
wfMacIPLowerIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPLowerIpAddress1.setStatus("mandatory")


class _WfMacIPUpperIpAddress1_Type(Integer32):
    """Custom type wfMacIPUpperIpAddress1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfMacIPUpperIpAddress1_Type.__name__ = "Integer32"
_WfMacIPUpperIpAddress1_Object = MibScalar
wfMacIPUpperIpAddress1 = _WfMacIPUpperIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 19),
    _WfMacIPUpperIpAddress1_Type()
)
wfMacIPUpperIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPUpperIpAddress1.setStatus("mandatory")
_WfMacIPAddress2_Type = IpAddress
_WfMacIPAddress2_Object = MibScalar
wfMacIPAddress2 = _WfMacIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 20),
    _WfMacIPAddress2_Type()
)
wfMacIPAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPAddress2.setStatus("mandatory")


class _WfMacIPLowerIpAddress2_Type(Integer32):
    """Custom type wfMacIPLowerIpAddress2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfMacIPLowerIpAddress2_Type.__name__ = "Integer32"
_WfMacIPLowerIpAddress2_Object = MibScalar
wfMacIPLowerIpAddress2 = _WfMacIPLowerIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 21),
    _WfMacIPLowerIpAddress2_Type()
)
wfMacIPLowerIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPLowerIpAddress2.setStatus("mandatory")


class _WfMacIPUpperIpAddress2_Type(Integer32):
    """Custom type wfMacIPUpperIpAddress2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfMacIPUpperIpAddress2_Type.__name__ = "Integer32"
_WfMacIPUpperIpAddress2_Object = MibScalar
wfMacIPUpperIpAddress2 = _WfMacIPUpperIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 22),
    _WfMacIPUpperIpAddress2_Type()
)
wfMacIPUpperIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPUpperIpAddress2.setStatus("mandatory")
_WfMacIPAddress3_Type = IpAddress
_WfMacIPAddress3_Object = MibScalar
wfMacIPAddress3 = _WfMacIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 23),
    _WfMacIPAddress3_Type()
)
wfMacIPAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPAddress3.setStatus("mandatory")


class _WfMacIPLowerIpAddress3_Type(Integer32):
    """Custom type wfMacIPLowerIpAddress3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfMacIPLowerIpAddress3_Type.__name__ = "Integer32"
_WfMacIPLowerIpAddress3_Object = MibScalar
wfMacIPLowerIpAddress3 = _WfMacIPLowerIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 24),
    _WfMacIPLowerIpAddress3_Type()
)
wfMacIPLowerIpAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPLowerIpAddress3.setStatus("mandatory")


class _WfMacIPUpperIpAddress3_Type(Integer32):
    """Custom type wfMacIPUpperIpAddress3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfMacIPUpperIpAddress3_Type.__name__ = "Integer32"
_WfMacIPUpperIpAddress3_Object = MibScalar
wfMacIPUpperIpAddress3 = _WfMacIPUpperIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 25),
    _WfMacIPUpperIpAddress3_Type()
)
wfMacIPUpperIpAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMacIPUpperIpAddress3.setStatus("mandatory")


class _WfAppleMacIPAddressTimeOut_Type(Integer32):
    """Custom type wfAppleMacIPAddressTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfAppleMacIPAddressTimeOut_Type.__name__ = "Integer32"
_WfAppleMacIPAddressTimeOut_Object = MibScalar
wfAppleMacIPAddressTimeOut = _WfAppleMacIPAddressTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 26),
    _WfAppleMacIPAddressTimeOut_Type()
)
wfAppleMacIPAddressTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleMacIPAddressTimeOut.setStatus("mandatory")
_WfAppleMacIPServerRequests_Type = Integer32
_WfAppleMacIPServerRequests_Object = MibScalar
wfAppleMacIPServerRequests = _WfAppleMacIPServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 27),
    _WfAppleMacIPServerRequests_Type()
)
wfAppleMacIPServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleMacIPServerRequests.setStatus("mandatory")
_WfAppleMacIPServerResponces_Type = Integer32
_WfAppleMacIPServerResponces_Object = MibScalar
wfAppleMacIPServerResponces = _WfAppleMacIPServerResponces_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 1, 28),
    _WfAppleMacIPServerResponces_Type()
)
wfAppleMacIPServerResponces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleMacIPServerResponces.setStatus("mandatory")
_WfAppleRtmpTable_Object = MibTable
wfAppleRtmpTable = _WfAppleRtmpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    wfAppleRtmpTable.setStatus("mandatory")
_WfAppleRtmpEntry_Object = MibTableRow
wfAppleRtmpEntry = _WfAppleRtmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1)
)
wfAppleRtmpEntry.setIndexNames(
    (0, "Wellfleet-AT-MIB", "wfAppleRtmpNetStart"),
    (0, "Wellfleet-AT-MIB", "wfAppleRtmpNetEnd"),
)
if mibBuilder.loadTexts:
    wfAppleRtmpEntry.setStatus("mandatory")
_WfAppleRtmpNetStart_Type = Integer32
_WfAppleRtmpNetStart_Object = MibTableColumn
wfAppleRtmpNetStart = _WfAppleRtmpNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 1),
    _WfAppleRtmpNetStart_Type()
)
wfAppleRtmpNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNetStart.setStatus("mandatory")
_WfAppleRtmpNetEnd_Type = Integer32
_WfAppleRtmpNetEnd_Object = MibTableColumn
wfAppleRtmpNetEnd = _WfAppleRtmpNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 2),
    _WfAppleRtmpNetEnd_Type()
)
wfAppleRtmpNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNetEnd.setStatus("mandatory")
_WfAppleRtmpPort_Type = Integer32
_WfAppleRtmpPort_Object = MibTableColumn
wfAppleRtmpPort = _WfAppleRtmpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 3),
    _WfAppleRtmpPort_Type()
)
wfAppleRtmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpPort.setStatus("mandatory")
_WfAppleRtmpHops_Type = Integer32
_WfAppleRtmpHops_Object = MibTableColumn
wfAppleRtmpHops = _WfAppleRtmpHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 4),
    _WfAppleRtmpHops_Type()
)
wfAppleRtmpHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpHops.setStatus("mandatory")
_WfAppleRtmpNextHopNet_Type = Integer32
_WfAppleRtmpNextHopNet_Object = MibTableColumn
wfAppleRtmpNextHopNet = _WfAppleRtmpNextHopNet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 5),
    _WfAppleRtmpNextHopNet_Type()
)
wfAppleRtmpNextHopNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNextHopNet.setStatus("mandatory")
_WfAppleRtmpNextHopNode_Type = Integer32
_WfAppleRtmpNextHopNode_Object = MibTableColumn
wfAppleRtmpNextHopNode = _WfAppleRtmpNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 6),
    _WfAppleRtmpNextHopNode_Type()
)
wfAppleRtmpNextHopNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpNextHopNode.setStatus("mandatory")


class _WfAppleRtmpState_Type(Integer32):
    """Custom type wfAppleRtmpState based on Integer32"""
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
        *(("bad", 4),
          ("goingbad", 3),
          ("good", 1),
          ("suspect", 2))
    )


_WfAppleRtmpState_Type.__name__ = "Integer32"
_WfAppleRtmpState_Object = MibTableColumn
wfAppleRtmpState = _WfAppleRtmpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 7),
    _WfAppleRtmpState_Type()
)
wfAppleRtmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpState.setStatus("mandatory")


class _WfAppleRtmpProto_Type(Integer32):
    """Custom type wfAppleRtmpProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aurp", 2),
          ("rtmp", 1),
          ("static", 3))
    )


_WfAppleRtmpProto_Type.__name__ = "Integer32"
_WfAppleRtmpProto_Object = MibTableColumn
wfAppleRtmpProto = _WfAppleRtmpProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 8),
    _WfAppleRtmpProto_Type()
)
wfAppleRtmpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpProto.setStatus("mandatory")
_WfAppleRtmpAurpNextHopIpAddress_Type = IpAddress
_WfAppleRtmpAurpNextHopIpAddress_Object = MibTableColumn
wfAppleRtmpAurpNextHopIpAddress = _WfAppleRtmpAurpNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 2, 1, 9),
    _WfAppleRtmpAurpNextHopIpAddress_Type()
)
wfAppleRtmpAurpNextHopIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleRtmpAurpNextHopIpAddress.setStatus("mandatory")
_WfApplePortTable_Object = MibTable
wfApplePortTable = _WfApplePortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3)
)
if mibBuilder.loadTexts:
    wfApplePortTable.setStatus("mandatory")
_WfApplePortEntry_Object = MibTableRow
wfApplePortEntry = _WfApplePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1)
)
wfApplePortEntry.setIndexNames(
    (0, "Wellfleet-AT-MIB", "wfApplePortCircuit"),
)
if mibBuilder.loadTexts:
    wfApplePortEntry.setStatus("mandatory")


class _WfApplePortDelete_Type(Integer32):
    """Custom type wfApplePortDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfApplePortDelete_Type.__name__ = "Integer32"
_WfApplePortDelete_Object = MibTableColumn
wfApplePortDelete = _WfApplePortDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 1),
    _WfApplePortDelete_Type()
)
wfApplePortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortDelete.setStatus("mandatory")


class _WfApplePortDisable_Type(Integer32):
    """Custom type wfApplePortDisable based on Integer32"""
    defaultValue = 1

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


_WfApplePortDisable_Type.__name__ = "Integer32"
_WfApplePortDisable_Object = MibTableColumn
wfApplePortDisable = _WfApplePortDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 2),
    _WfApplePortDisable_Type()
)
wfApplePortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortDisable.setStatus("mandatory")
_WfApplePortCircuit_Type = Integer32
_WfApplePortCircuit_Object = MibTableColumn
wfApplePortCircuit = _WfApplePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 3),
    _WfApplePortCircuit_Type()
)
wfApplePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCircuit.setStatus("mandatory")


class _WfApplePortState_Type(Integer32):
    """Custom type wfApplePortState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfApplePortState_Type.__name__ = "Integer32"
_WfApplePortState_Object = MibTableColumn
wfApplePortState = _WfApplePortState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 4),
    _WfApplePortState_Type()
)
wfApplePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortState.setStatus("mandatory")
_WfApplePortType_Type = Integer32
_WfApplePortType_Object = MibTableColumn
wfApplePortType = _WfApplePortType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 5),
    _WfApplePortType_Type()
)
wfApplePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortType.setStatus("mandatory")


class _WfApplePortCksumDisable_Type(Integer32):
    """Custom type wfApplePortCksumDisable based on Integer32"""
    defaultValue = 2

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


_WfApplePortCksumDisable_Type.__name__ = "Integer32"
_WfApplePortCksumDisable_Object = MibTableColumn
wfApplePortCksumDisable = _WfApplePortCksumDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 6),
    _WfApplePortCksumDisable_Type()
)
wfApplePortCksumDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortCksumDisable.setStatus("mandatory")


class _WfApplePortTrEndStation_Type(Integer32):
    """Custom type wfApplePortTrEndStation based on Integer32"""
    defaultValue = 2

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


_WfApplePortTrEndStation_Type.__name__ = "Integer32"
_WfApplePortTrEndStation_Object = MibTableColumn
wfApplePortTrEndStation = _WfApplePortTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 7),
    _WfApplePortTrEndStation_Type()
)
wfApplePortTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortTrEndStation.setStatus("mandatory")
_WfApplePortGniForever_Type = Integer32
_WfApplePortGniForever_Object = MibTableColumn
wfApplePortGniForever = _WfApplePortGniForever_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 8),
    _WfApplePortGniForever_Type()
)
wfApplePortGniForever.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortGniForever.setStatus("obsolete")
_WfApplePortAarpFlush_Type = Integer32
_WfApplePortAarpFlush_Object = MibTableColumn
wfApplePortAarpFlush = _WfApplePortAarpFlush_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 9),
    _WfApplePortAarpFlush_Type()
)
wfApplePortAarpFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortAarpFlush.setStatus("mandatory")
_WfApplePortMacAddress_Type = OctetString
_WfApplePortMacAddress_Object = MibTableColumn
wfApplePortMacAddress = _WfApplePortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 10),
    _WfApplePortMacAddress_Type()
)
wfApplePortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortMacAddress.setStatus("mandatory")
_WfApplePortNodeId_Type = Integer32
_WfApplePortNodeId_Object = MibTableColumn
wfApplePortNodeId = _WfApplePortNodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 11),
    _WfApplePortNodeId_Type()
)
wfApplePortNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNodeId.setStatus("mandatory")
_WfApplePortNetwork_Type = Integer32
_WfApplePortNetwork_Object = MibTableColumn
wfApplePortNetwork = _WfApplePortNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 12),
    _WfApplePortNetwork_Type()
)
wfApplePortNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNetwork.setStatus("mandatory")
_WfApplePortNetStart_Type = Integer32
_WfApplePortNetStart_Object = MibTableColumn
wfApplePortNetStart = _WfApplePortNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 13),
    _WfApplePortNetStart_Type()
)
wfApplePortNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNetStart.setStatus("mandatory")
_WfApplePortNetEnd_Type = Integer32
_WfApplePortNetEnd_Object = MibTableColumn
wfApplePortNetEnd = _WfApplePortNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 14),
    _WfApplePortNetEnd_Type()
)
wfApplePortNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortNetEnd.setStatus("mandatory")
_WfApplePortDfltZone_Type = DisplayString
_WfApplePortDfltZone_Object = MibTableColumn
wfApplePortDfltZone = _WfApplePortDfltZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 15),
    _WfApplePortDfltZone_Type()
)
wfApplePortDfltZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortDfltZone.setStatus("mandatory")
_WfApplePortCurMacAddress_Type = OctetString
_WfApplePortCurMacAddress_Object = MibTableColumn
wfApplePortCurMacAddress = _WfApplePortCurMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 16),
    _WfApplePortCurMacAddress_Type()
)
wfApplePortCurMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurMacAddress.setStatus("mandatory")
_WfApplePortCurNodeId_Type = Integer32
_WfApplePortCurNodeId_Object = MibTableColumn
wfApplePortCurNodeId = _WfApplePortCurNodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 17),
    _WfApplePortCurNodeId_Type()
)
wfApplePortCurNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNodeId.setStatus("mandatory")
_WfApplePortCurNetwork_Type = Integer32
_WfApplePortCurNetwork_Object = MibTableColumn
wfApplePortCurNetwork = _WfApplePortCurNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 18),
    _WfApplePortCurNetwork_Type()
)
wfApplePortCurNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNetwork.setStatus("mandatory")
_WfApplePortCurNetStart_Type = Integer32
_WfApplePortCurNetStart_Object = MibTableColumn
wfApplePortCurNetStart = _WfApplePortCurNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 19),
    _WfApplePortCurNetStart_Type()
)
wfApplePortCurNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNetStart.setStatus("mandatory")
_WfApplePortCurNetEnd_Type = Integer32
_WfApplePortCurNetEnd_Object = MibTableColumn
wfApplePortCurNetEnd = _WfApplePortCurNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 20),
    _WfApplePortCurNetEnd_Type()
)
wfApplePortCurNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurNetEnd.setStatus("mandatory")
_WfApplePortCurDfltZone_Type = DisplayString
_WfApplePortCurDfltZone_Object = MibTableColumn
wfApplePortCurDfltZone = _WfApplePortCurDfltZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 21),
    _WfApplePortCurDfltZone_Type()
)
wfApplePortCurDfltZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortCurDfltZone.setStatus("mandatory")
_WfApplePortAarpProbeRxs_Type = Counter32
_WfApplePortAarpProbeRxs_Object = MibTableColumn
wfApplePortAarpProbeRxs = _WfApplePortAarpProbeRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 22),
    _WfApplePortAarpProbeRxs_Type()
)
wfApplePortAarpProbeRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpProbeRxs.setStatus("mandatory")
_WfApplePortAarpProbeTxs_Type = Counter32
_WfApplePortAarpProbeTxs_Object = MibTableColumn
wfApplePortAarpProbeTxs = _WfApplePortAarpProbeTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 23),
    _WfApplePortAarpProbeTxs_Type()
)
wfApplePortAarpProbeTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpProbeTxs.setStatus("mandatory")
_WfApplePortAarpReqRxs_Type = Counter32
_WfApplePortAarpReqRxs_Object = MibTableColumn
wfApplePortAarpReqRxs = _WfApplePortAarpReqRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 24),
    _WfApplePortAarpReqRxs_Type()
)
wfApplePortAarpReqRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpReqRxs.setStatus("mandatory")
_WfApplePortAarpReqTxs_Type = Counter32
_WfApplePortAarpReqTxs_Object = MibTableColumn
wfApplePortAarpReqTxs = _WfApplePortAarpReqTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 25),
    _WfApplePortAarpReqTxs_Type()
)
wfApplePortAarpReqTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpReqTxs.setStatus("mandatory")
_WfApplePortAarpRspRxs_Type = Counter32
_WfApplePortAarpRspRxs_Object = MibTableColumn
wfApplePortAarpRspRxs = _WfApplePortAarpRspRxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 26),
    _WfApplePortAarpRspRxs_Type()
)
wfApplePortAarpRspRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpRspRxs.setStatus("mandatory")
_WfApplePortAarpRspTxs_Type = Counter32
_WfApplePortAarpRspTxs_Object = MibTableColumn
wfApplePortAarpRspTxs = _WfApplePortAarpRspTxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 27),
    _WfApplePortAarpRspTxs_Type()
)
wfApplePortAarpRspTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortAarpRspTxs.setStatus("mandatory")
_WfApplePortDdpOutRequests_Type = Counter32
_WfApplePortDdpOutRequests_Object = MibTableColumn
wfApplePortDdpOutRequests = _WfApplePortDdpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 28),
    _WfApplePortDdpOutRequests_Type()
)
wfApplePortDdpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpOutRequests.setStatus("mandatory")
_WfApplePortDdpInReceives_Type = Counter32
_WfApplePortDdpInReceives_Object = MibTableColumn
wfApplePortDdpInReceives = _WfApplePortDdpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 29),
    _WfApplePortDdpInReceives_Type()
)
wfApplePortDdpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpInReceives.setStatus("mandatory")
_WfApplePortDdpInLocalDatagrams_Type = Counter32
_WfApplePortDdpInLocalDatagrams_Object = MibTableColumn
wfApplePortDdpInLocalDatagrams = _WfApplePortDdpInLocalDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 30),
    _WfApplePortDdpInLocalDatagrams_Type()
)
wfApplePortDdpInLocalDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpInLocalDatagrams.setStatus("mandatory")
_WfApplePortDdpNoProtocolHandlers_Type = Counter32
_WfApplePortDdpNoProtocolHandlers_Object = MibTableColumn
wfApplePortDdpNoProtocolHandlers = _WfApplePortDdpNoProtocolHandlers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 31),
    _WfApplePortDdpNoProtocolHandlers_Type()
)
wfApplePortDdpNoProtocolHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpNoProtocolHandlers.setStatus("mandatory")
_WfApplePortDdpTooShortErrors_Type = Counter32
_WfApplePortDdpTooShortErrors_Object = MibTableColumn
wfApplePortDdpTooShortErrors = _WfApplePortDdpTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 32),
    _WfApplePortDdpTooShortErrors_Type()
)
wfApplePortDdpTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpTooShortErrors.setStatus("mandatory")
_WfApplePortDdpTooLongErrors_Type = Counter32
_WfApplePortDdpTooLongErrors_Object = MibTableColumn
wfApplePortDdpTooLongErrors = _WfApplePortDdpTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 33),
    _WfApplePortDdpTooLongErrors_Type()
)
wfApplePortDdpTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpTooLongErrors.setStatus("mandatory")
_WfApplePortDdpChecksumErrors_Type = Counter32
_WfApplePortDdpChecksumErrors_Object = MibTableColumn
wfApplePortDdpChecksumErrors = _WfApplePortDdpChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 34),
    _WfApplePortDdpChecksumErrors_Type()
)
wfApplePortDdpChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpChecksumErrors.setStatus("mandatory")
_WfApplePortDdpForwRequests_Type = Counter32
_WfApplePortDdpForwRequests_Object = MibTableColumn
wfApplePortDdpForwRequests = _WfApplePortDdpForwRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 35),
    _WfApplePortDdpForwRequests_Type()
)
wfApplePortDdpForwRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpForwRequests.setStatus("mandatory")
_WfApplePortDdpOutNoRoutes_Type = Counter32
_WfApplePortDdpOutNoRoutes_Object = MibTableColumn
wfApplePortDdpOutNoRoutes = _WfApplePortDdpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 36),
    _WfApplePortDdpOutNoRoutes_Type()
)
wfApplePortDdpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpOutNoRoutes.setStatus("mandatory")
_WfApplePortDdpBroadcastErrors_Type = Counter32
_WfApplePortDdpBroadcastErrors_Object = MibTableColumn
wfApplePortDdpBroadcastErrors = _WfApplePortDdpBroadcastErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 37),
    _WfApplePortDdpBroadcastErrors_Type()
)
wfApplePortDdpBroadcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpBroadcastErrors.setStatus("mandatory")
_WfApplePortDdpHopCountErrors_Type = Counter32
_WfApplePortDdpHopCountErrors_Object = MibTableColumn
wfApplePortDdpHopCountErrors = _WfApplePortDdpHopCountErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 38),
    _WfApplePortDdpHopCountErrors_Type()
)
wfApplePortDdpHopCountErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortDdpHopCountErrors.setStatus("mandatory")
_WfApplePortRtmpInDataPkts_Type = Counter32
_WfApplePortRtmpInDataPkts_Object = MibTableColumn
wfApplePortRtmpInDataPkts = _WfApplePortRtmpInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 39),
    _WfApplePortRtmpInDataPkts_Type()
)
wfApplePortRtmpInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpInDataPkts.setStatus("mandatory")
_WfApplePortRtmpOutDataPkts_Type = Counter32
_WfApplePortRtmpOutDataPkts_Object = MibTableColumn
wfApplePortRtmpOutDataPkts = _WfApplePortRtmpOutDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 40),
    _WfApplePortRtmpOutDataPkts_Type()
)
wfApplePortRtmpOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpOutDataPkts.setStatus("mandatory")
_WfApplePortRtmpInRequestPkts_Type = Counter32
_WfApplePortRtmpInRequestPkts_Object = MibTableColumn
wfApplePortRtmpInRequestPkts = _WfApplePortRtmpInRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 41),
    _WfApplePortRtmpInRequestPkts_Type()
)
wfApplePortRtmpInRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpInRequestPkts.setStatus("mandatory")
_WfApplePortRtmpNextIREqualChanges_Type = Counter32
_WfApplePortRtmpNextIREqualChanges_Object = MibTableColumn
wfApplePortRtmpNextIREqualChanges = _WfApplePortRtmpNextIREqualChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 42),
    _WfApplePortRtmpNextIREqualChanges_Type()
)
wfApplePortRtmpNextIREqualChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpNextIREqualChanges.setStatus("mandatory")
_WfApplePortRtmpNextIRLessChanges_Type = Counter32
_WfApplePortRtmpNextIRLessChanges_Object = MibTableColumn
wfApplePortRtmpNextIRLessChanges = _WfApplePortRtmpNextIRLessChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 43),
    _WfApplePortRtmpNextIRLessChanges_Type()
)
wfApplePortRtmpNextIRLessChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpNextIRLessChanges.setStatus("mandatory")
_WfApplePortRtmpRouteDeletes_Type = Counter32
_WfApplePortRtmpRouteDeletes_Object = MibTableColumn
wfApplePortRtmpRouteDeletes = _WfApplePortRtmpRouteDeletes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 44),
    _WfApplePortRtmpRouteDeletes_Type()
)
wfApplePortRtmpRouteDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpRouteDeletes.setStatus("mandatory")
_WfApplePortRtmpNetworkMismatchErrors_Type = Counter32
_WfApplePortRtmpNetworkMismatchErrors_Object = MibTableColumn
wfApplePortRtmpNetworkMismatchErrors = _WfApplePortRtmpNetworkMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 45),
    _WfApplePortRtmpNetworkMismatchErrors_Type()
)
wfApplePortRtmpNetworkMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpNetworkMismatchErrors.setStatus("mandatory")
_WfApplePortRtmpRoutingTableOverflows_Type = Counter32
_WfApplePortRtmpRoutingTableOverflows_Object = MibTableColumn
wfApplePortRtmpRoutingTableOverflows = _WfApplePortRtmpRoutingTableOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 46),
    _WfApplePortRtmpRoutingTableOverflows_Type()
)
wfApplePortRtmpRoutingTableOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortRtmpRoutingTableOverflows.setStatus("mandatory")
_WfApplePortZipInZipQueries_Type = Counter32
_WfApplePortZipInZipQueries_Object = MibTableColumn
wfApplePortZipInZipQueries = _WfApplePortZipInZipQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 47),
    _WfApplePortZipInZipQueries_Type()
)
wfApplePortZipInZipQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInZipQueries.setStatus("mandatory")
_WfApplePortZipInZipReplies_Type = Counter32
_WfApplePortZipInZipReplies_Object = MibTableColumn
wfApplePortZipInZipReplies = _WfApplePortZipInZipReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 48),
    _WfApplePortZipInZipReplies_Type()
)
wfApplePortZipInZipReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInZipReplies.setStatus("mandatory")
_WfApplePortZipOutZipReplies_Type = Counter32
_WfApplePortZipOutZipReplies_Object = MibTableColumn
wfApplePortZipOutZipReplies = _WfApplePortZipOutZipReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 49),
    _WfApplePortZipOutZipReplies_Type()
)
wfApplePortZipOutZipReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutZipReplies.setStatus("mandatory")
_WfApplePortZipInZipExtendedReplies_Type = Counter32
_WfApplePortZipInZipExtendedReplies_Object = MibTableColumn
wfApplePortZipInZipExtendedReplies = _WfApplePortZipInZipExtendedReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 50),
    _WfApplePortZipInZipExtendedReplies_Type()
)
wfApplePortZipInZipExtendedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInZipExtendedReplies.setStatus("mandatory")
_WfApplePortZipOutZipExtendedReplies_Type = Counter32
_WfApplePortZipOutZipExtendedReplies_Object = MibTableColumn
wfApplePortZipOutZipExtendedReplies = _WfApplePortZipOutZipExtendedReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 51),
    _WfApplePortZipOutZipExtendedReplies_Type()
)
wfApplePortZipOutZipExtendedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutZipExtendedReplies.setStatus("mandatory")
_WfApplePortZipInGetZoneLists_Type = Counter32
_WfApplePortZipInGetZoneLists_Object = MibTableColumn
wfApplePortZipInGetZoneLists = _WfApplePortZipInGetZoneLists_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 52),
    _WfApplePortZipInGetZoneLists_Type()
)
wfApplePortZipInGetZoneLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetZoneLists.setStatus("mandatory")
_WfApplePortZipOutGetZoneListReplies_Type = Counter32
_WfApplePortZipOutGetZoneListReplies_Object = MibTableColumn
wfApplePortZipOutGetZoneListReplies = _WfApplePortZipOutGetZoneListReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 53),
    _WfApplePortZipOutGetZoneListReplies_Type()
)
wfApplePortZipOutGetZoneListReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetZoneListReplies.setStatus("mandatory")
_WfApplePortZipInGetLocalZones_Type = Counter32
_WfApplePortZipInGetLocalZones_Object = MibTableColumn
wfApplePortZipInGetLocalZones = _WfApplePortZipInGetLocalZones_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 54),
    _WfApplePortZipInGetLocalZones_Type()
)
wfApplePortZipInGetLocalZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetLocalZones.setStatus("mandatory")
_WfApplePortZipOutGetLocalZoneReplies_Type = Counter32
_WfApplePortZipOutGetLocalZoneReplies_Object = MibTableColumn
wfApplePortZipOutGetLocalZoneReplies = _WfApplePortZipOutGetLocalZoneReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 55),
    _WfApplePortZipOutGetLocalZoneReplies_Type()
)
wfApplePortZipOutGetLocalZoneReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetLocalZoneReplies.setStatus("mandatory")
_WfApplePortZipInGetMyZones_Type = Counter32
_WfApplePortZipInGetMyZones_Object = MibTableColumn
wfApplePortZipInGetMyZones = _WfApplePortZipInGetMyZones_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 56),
    _WfApplePortZipInGetMyZones_Type()
)
wfApplePortZipInGetMyZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetMyZones.setStatus("obsolete")
_WfApplePortZipOutGetMyZoneReplies_Type = Counter32
_WfApplePortZipOutGetMyZoneReplies_Object = MibTableColumn
wfApplePortZipOutGetMyZoneReplies = _WfApplePortZipOutGetMyZoneReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 57),
    _WfApplePortZipOutGetMyZoneReplies_Type()
)
wfApplePortZipOutGetMyZoneReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetMyZoneReplies.setStatus("obsolete")
_WfApplePortZipZoneConflictErrors_Type = Counter32
_WfApplePortZipZoneConflictErrors_Object = MibTableColumn
wfApplePortZipZoneConflictErrors = _WfApplePortZipZoneConflictErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 58),
    _WfApplePortZipZoneConflictErrors_Type()
)
wfApplePortZipZoneConflictErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipZoneConflictErrors.setStatus("mandatory")
_WfApplePortZipInGetNetInfos_Type = Counter32
_WfApplePortZipInGetNetInfos_Object = MibTableColumn
wfApplePortZipInGetNetInfos = _WfApplePortZipInGetNetInfos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 59),
    _WfApplePortZipInGetNetInfos_Type()
)
wfApplePortZipInGetNetInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetNetInfos.setStatus("mandatory")
_WfApplePortZipOutGetNetInfoReplies_Type = Counter32
_WfApplePortZipOutGetNetInfoReplies_Object = MibTableColumn
wfApplePortZipOutGetNetInfoReplies = _WfApplePortZipOutGetNetInfoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 60),
    _WfApplePortZipOutGetNetInfoReplies_Type()
)
wfApplePortZipOutGetNetInfoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetNetInfoReplies.setStatus("mandatory")
_WfApplePortZipZoneOutInvalids_Type = Counter32
_WfApplePortZipZoneOutInvalids_Object = MibTableColumn
wfApplePortZipZoneOutInvalids = _WfApplePortZipZoneOutInvalids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 61),
    _WfApplePortZipZoneOutInvalids_Type()
)
wfApplePortZipZoneOutInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipZoneOutInvalids.setStatus("mandatory")
_WfApplePortZipAddressInvalids_Type = Counter32
_WfApplePortZipAddressInvalids_Object = MibTableColumn
wfApplePortZipAddressInvalids = _WfApplePortZipAddressInvalids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 62),
    _WfApplePortZipAddressInvalids_Type()
)
wfApplePortZipAddressInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipAddressInvalids.setStatus("mandatory")
_WfApplePortZipOutGetNetInfos_Type = Counter32
_WfApplePortZipOutGetNetInfos_Object = MibTableColumn
wfApplePortZipOutGetNetInfos = _WfApplePortZipOutGetNetInfos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 63),
    _WfApplePortZipOutGetNetInfos_Type()
)
wfApplePortZipOutGetNetInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutGetNetInfos.setStatus("mandatory")
_WfApplePortZipInGetNetInfoReplies_Type = Counter32
_WfApplePortZipInGetNetInfoReplies_Object = MibTableColumn
wfApplePortZipInGetNetInfoReplies = _WfApplePortZipInGetNetInfoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 64),
    _WfApplePortZipInGetNetInfoReplies_Type()
)
wfApplePortZipInGetNetInfoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInGetNetInfoReplies.setStatus("mandatory")
_WfApplePortZipOutZipQueries_Type = Counter32
_WfApplePortZipOutZipQueries_Object = MibTableColumn
wfApplePortZipOutZipQueries = _WfApplePortZipOutZipQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 65),
    _WfApplePortZipOutZipQueries_Type()
)
wfApplePortZipOutZipQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipOutZipQueries.setStatus("mandatory")
_WfApplePortZipInErrors_Type = Counter32
_WfApplePortZipInErrors_Object = MibTableColumn
wfApplePortZipInErrors = _WfApplePortZipInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 66),
    _WfApplePortZipInErrors_Type()
)
wfApplePortZipInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortZipInErrors.setStatus("mandatory")
_WfApplePortNbpInLookUpRequests_Type = Counter32
_WfApplePortNbpInLookUpRequests_Object = MibTableColumn
wfApplePortNbpInLookUpRequests = _WfApplePortNbpInLookUpRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 67),
    _WfApplePortNbpInLookUpRequests_Type()
)
wfApplePortNbpInLookUpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInLookUpRequests.setStatus("mandatory")
_WfApplePortNbpInLookUpReplies_Type = Counter32
_WfApplePortNbpInLookUpReplies_Object = MibTableColumn
wfApplePortNbpInLookUpReplies = _WfApplePortNbpInLookUpReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 68),
    _WfApplePortNbpInLookUpReplies_Type()
)
wfApplePortNbpInLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInLookUpReplies.setStatus("mandatory")
_WfApplePortNbpInBroadcastRequests_Type = Counter32
_WfApplePortNbpInBroadcastRequests_Object = MibTableColumn
wfApplePortNbpInBroadcastRequests = _WfApplePortNbpInBroadcastRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 69),
    _WfApplePortNbpInBroadcastRequests_Type()
)
wfApplePortNbpInBroadcastRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInBroadcastRequests.setStatus("mandatory")
_WfApplePortNbpInForwardRequests_Type = Counter32
_WfApplePortNbpInForwardRequests_Object = MibTableColumn
wfApplePortNbpInForwardRequests = _WfApplePortNbpInForwardRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 70),
    _WfApplePortNbpInForwardRequests_Type()
)
wfApplePortNbpInForwardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInForwardRequests.setStatus("mandatory")
_WfApplePortNbpOutLookUpRequests_Type = Counter32
_WfApplePortNbpOutLookUpRequests_Object = MibTableColumn
wfApplePortNbpOutLookUpRequests = _WfApplePortNbpOutLookUpRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 71),
    _WfApplePortNbpOutLookUpRequests_Type()
)
wfApplePortNbpOutLookUpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutLookUpRequests.setStatus("mandatory")
_WfApplePortNbpOutLookUpReplies_Type = Counter32
_WfApplePortNbpOutLookUpReplies_Object = MibTableColumn
wfApplePortNbpOutLookUpReplies = _WfApplePortNbpOutLookUpReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 72),
    _WfApplePortNbpOutLookUpReplies_Type()
)
wfApplePortNbpOutLookUpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutLookUpReplies.setStatus("mandatory")
_WfApplePortNbpOutBroadcastRequests_Type = Counter32
_WfApplePortNbpOutBroadcastRequests_Object = MibTableColumn
wfApplePortNbpOutBroadcastRequests = _WfApplePortNbpOutBroadcastRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 73),
    _WfApplePortNbpOutBroadcastRequests_Type()
)
wfApplePortNbpOutBroadcastRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutBroadcastRequests.setStatus("mandatory")
_WfApplePortNbpOutForwardRequests_Type = Counter32
_WfApplePortNbpOutForwardRequests_Object = MibTableColumn
wfApplePortNbpOutForwardRequests = _WfApplePortNbpOutForwardRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 74),
    _WfApplePortNbpOutForwardRequests_Type()
)
wfApplePortNbpOutForwardRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpOutForwardRequests.setStatus("mandatory")
_WfApplePortNbpRegistrationFailures_Type = Counter32
_WfApplePortNbpRegistrationFailures_Object = MibTableColumn
wfApplePortNbpRegistrationFailures = _WfApplePortNbpRegistrationFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 75),
    _WfApplePortNbpRegistrationFailures_Type()
)
wfApplePortNbpRegistrationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpRegistrationFailures.setStatus("mandatory")
_WfApplePortNbpInErrors_Type = Counter32
_WfApplePortNbpInErrors_Object = MibTableColumn
wfApplePortNbpInErrors = _WfApplePortNbpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 76),
    _WfApplePortNbpInErrors_Type()
)
wfApplePortNbpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortNbpInErrors.setStatus("mandatory")
_WfApplePortEchoRequests_Type = Counter32
_WfApplePortEchoRequests_Object = MibTableColumn
wfApplePortEchoRequests = _WfApplePortEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 77),
    _WfApplePortEchoRequests_Type()
)
wfApplePortEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortEchoRequests.setStatus("mandatory")
_WfApplePortEchoReplies_Type = Counter32
_WfApplePortEchoReplies_Object = MibTableColumn
wfApplePortEchoReplies = _WfApplePortEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 78),
    _WfApplePortEchoReplies_Type()
)
wfApplePortEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfApplePortEchoReplies.setStatus("mandatory")


class _WfApplePortInterfaceCost_Type(Integer32):
    """Custom type wfApplePortInterfaceCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            15
        )
    )
    namedValues = NamedValues(
        ("cost", 15)
    )


_WfApplePortInterfaceCost_Type.__name__ = "Integer32"
_WfApplePortInterfaceCost_Object = MibTableColumn
wfApplePortInterfaceCost = _WfApplePortInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 79),
    _WfApplePortInterfaceCost_Type()
)
wfApplePortInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortInterfaceCost.setStatus("mandatory")
_WfApplePortWanBroadcastAddress_Type = OctetString
_WfApplePortWanBroadcastAddress_Object = MibTableColumn
wfApplePortWanBroadcastAddress = _WfApplePortWanBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 80),
    _WfApplePortWanBroadcastAddress_Type()
)
wfApplePortWanBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortWanBroadcastAddress.setStatus("mandatory")


class _WfApplePortWanSplitHorizonDisable_Type(Integer32):
    """Custom type wfApplePortWanSplitHorizonDisable based on Integer32"""
    defaultValue = 1

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


_WfApplePortWanSplitHorizonDisable_Type.__name__ = "Integer32"
_WfApplePortWanSplitHorizonDisable_Object = MibTableColumn
wfApplePortWanSplitHorizonDisable = _WfApplePortWanSplitHorizonDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 81),
    _WfApplePortWanSplitHorizonDisable_Type()
)
wfApplePortWanSplitHorizonDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortWanSplitHorizonDisable.setStatus("mandatory")


class _WfApplePortZoneFilterType_Type(Integer32):
    """Custom type wfApplePortZoneFilterType based on Integer32"""
    defaultValue = 2

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
        *(("allow", 1),
          ("deny", 2),
          ("partallow", 3),
          ("partdeny", 4))
    )


_WfApplePortZoneFilterType_Type.__name__ = "Integer32"
_WfApplePortZoneFilterType_Object = MibTableColumn
wfApplePortZoneFilterType = _WfApplePortZoneFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 82),
    _WfApplePortZoneFilterType_Type()
)
wfApplePortZoneFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortZoneFilterType.setStatus("mandatory")


class _WfApplePortMacIPDisable_Type(Integer32):
    """Custom type wfApplePortMacIPDisable based on Integer32"""
    defaultValue = 2

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


_WfApplePortMacIPDisable_Type.__name__ = "Integer32"
_WfApplePortMacIPDisable_Object = MibTableColumn
wfApplePortMacIPDisable = _WfApplePortMacIPDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 3, 1, 83),
    _WfApplePortMacIPDisable_Type()
)
wfApplePortMacIPDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfApplePortMacIPDisable.setStatus("mandatory")
_WfAppleLclZoneTable_Object = MibTable
wfAppleLclZoneTable = _WfAppleLclZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4)
)
if mibBuilder.loadTexts:
    wfAppleLclZoneTable.setStatus("mandatory")
_WfAppleLclZoneEntry_Object = MibTableRow
wfAppleLclZoneEntry = _WfAppleLclZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1)
)
wfAppleLclZoneEntry.setIndexNames(
    (0, "Wellfleet-AT-MIB", "wfAppleLclZonePortCircuit"),
    (0, "Wellfleet-AT-MIB", "wfAppleLclZoneIndex"),
)
if mibBuilder.loadTexts:
    wfAppleLclZoneEntry.setStatus("mandatory")


class _WfAppleLclZoneDelete_Type(Integer32):
    """Custom type wfAppleLclZoneDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppleLclZoneDelete_Type.__name__ = "Integer32"
_WfAppleLclZoneDelete_Object = MibTableColumn
wfAppleLclZoneDelete = _WfAppleLclZoneDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 1),
    _WfAppleLclZoneDelete_Type()
)
wfAppleLclZoneDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleLclZoneDelete.setStatus("mandatory")
_WfAppleLclZonePortCircuit_Type = Integer32
_WfAppleLclZonePortCircuit_Object = MibTableColumn
wfAppleLclZonePortCircuit = _WfAppleLclZonePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 2),
    _WfAppleLclZonePortCircuit_Type()
)
wfAppleLclZonePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleLclZonePortCircuit.setStatus("mandatory")
_WfAppleLclZoneIndex_Type = Integer32
_WfAppleLclZoneIndex_Object = MibTableColumn
wfAppleLclZoneIndex = _WfAppleLclZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 3),
    _WfAppleLclZoneIndex_Type()
)
wfAppleLclZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleLclZoneIndex.setStatus("mandatory")
_WfAppleLclZoneName_Type = DisplayString
_WfAppleLclZoneName_Object = MibTableColumn
wfAppleLclZoneName = _WfAppleLclZoneName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 4, 1, 4),
    _WfAppleLclZoneName_Type()
)
wfAppleLclZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleLclZoneName.setStatus("mandatory")
_WfAppleAarpTable_Object = MibTable
wfAppleAarpTable = _WfAppleAarpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5)
)
if mibBuilder.loadTexts:
    wfAppleAarpTable.setStatus("mandatory")
_WfAppleAarpEntry_Object = MibTableRow
wfAppleAarpEntry = _WfAppleAarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1)
)
wfAppleAarpEntry.setIndexNames(
    (0, "Wellfleet-AT-MIB", "wfAppleAarpNet"),
    (0, "Wellfleet-AT-MIB", "wfAppleAarpNode"),
    (0, "Wellfleet-AT-MIB", "wfAppleAarpIfIndex"),
)
if mibBuilder.loadTexts:
    wfAppleAarpEntry.setStatus("mandatory")
_WfAppleAarpIfIndex_Type = Integer32
_WfAppleAarpIfIndex_Object = MibTableColumn
wfAppleAarpIfIndex = _WfAppleAarpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 1),
    _WfAppleAarpIfIndex_Type()
)
wfAppleAarpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpIfIndex.setStatus("mandatory")
_WfAppleAarpNet_Type = Integer32
_WfAppleAarpNet_Object = MibTableColumn
wfAppleAarpNet = _WfAppleAarpNet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 2),
    _WfAppleAarpNet_Type()
)
wfAppleAarpNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpNet.setStatus("mandatory")
_WfAppleAarpNode_Type = Integer32
_WfAppleAarpNode_Object = MibTableColumn
wfAppleAarpNode = _WfAppleAarpNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 3),
    _WfAppleAarpNode_Type()
)
wfAppleAarpNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpNode.setStatus("mandatory")
_WfAppleAarpPhysAddress_Type = OctetString
_WfAppleAarpPhysAddress_Object = MibTableColumn
wfAppleAarpPhysAddress = _WfAppleAarpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 5, 1, 4),
    _WfAppleAarpPhysAddress_Type()
)
wfAppleAarpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAarpPhysAddress.setStatus("mandatory")
_WfAppleZipTable_Object = MibTable
wfAppleZipTable = _WfAppleZipTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6)
)
if mibBuilder.loadTexts:
    wfAppleZipTable.setStatus("mandatory")
_WfAppleZipEntry_Object = MibTableRow
wfAppleZipEntry = _WfAppleZipEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1)
)
wfAppleZipEntry.setIndexNames(
    (0, "Wellfleet-AT-MIB", "wfAppleZipZoneNetStart"),
    (0, "Wellfleet-AT-MIB", "wfAppleZipIndex"),
)
if mibBuilder.loadTexts:
    wfAppleZipEntry.setStatus("mandatory")
_WfAppleZipZoneNetStart_Type = Integer32
_WfAppleZipZoneNetStart_Object = MibTableColumn
wfAppleZipZoneNetStart = _WfAppleZipZoneNetStart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 1),
    _WfAppleZipZoneNetStart_Type()
)
wfAppleZipZoneNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneNetStart.setStatus("mandatory")
_WfAppleZipZoneNetEnd_Type = Integer32
_WfAppleZipZoneNetEnd_Object = MibTableColumn
wfAppleZipZoneNetEnd = _WfAppleZipZoneNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 2),
    _WfAppleZipZoneNetEnd_Type()
)
wfAppleZipZoneNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneNetEnd.setStatus("mandatory")
_WfAppleZipIndex_Type = Integer32
_WfAppleZipIndex_Object = MibTableColumn
wfAppleZipIndex = _WfAppleZipIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 3),
    _WfAppleZipIndex_Type()
)
wfAppleZipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipIndex.setStatus("mandatory")
_WfAppleZipZoneName_Type = DisplayString
_WfAppleZipZoneName_Object = MibTableColumn
wfAppleZipZoneName = _WfAppleZipZoneName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 4),
    _WfAppleZipZoneName_Type()
)
wfAppleZipZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneName.setStatus("mandatory")


class _WfAppleZipZoneState_Type(Integer32):
    """Custom type wfAppleZipZoneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfAppleZipZoneState_Type.__name__ = "Integer32"
_WfAppleZipZoneState_Object = MibTableColumn
wfAppleZipZoneState = _WfAppleZipZoneState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 6, 1, 5),
    _WfAppleZipZoneState_Type()
)
wfAppleZipZoneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZipZoneState.setStatus("mandatory")
_WfAppleZoneFilterTable_Object = MibTable
wfAppleZoneFilterTable = _WfAppleZoneFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7)
)
if mibBuilder.loadTexts:
    wfAppleZoneFilterTable.setStatus("mandatory")
_WfAppleZoneFilterEntry_Object = MibTableRow
wfAppleZoneFilterEntry = _WfAppleZoneFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7, 1)
)
wfAppleZoneFilterEntry.setIndexNames(
    (0, "Wellfleet-AT-MIB", "wfAppleZoneFilterIndex"),
)
if mibBuilder.loadTexts:
    wfAppleZoneFilterEntry.setStatus("mandatory")


class _WfAppleZoneFilterDelete_Type(Integer32):
    """Custom type wfAppleZoneFilterDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppleZoneFilterDelete_Type.__name__ = "Integer32"
_WfAppleZoneFilterDelete_Object = MibTableColumn
wfAppleZoneFilterDelete = _WfAppleZoneFilterDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7, 1, 1),
    _WfAppleZoneFilterDelete_Type()
)
wfAppleZoneFilterDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleZoneFilterDelete.setStatus("mandatory")
_WfAppleZoneFilterCircuit_Type = Integer32
_WfAppleZoneFilterCircuit_Object = MibTableColumn
wfAppleZoneFilterCircuit = _WfAppleZoneFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7, 1, 2),
    _WfAppleZoneFilterCircuit_Type()
)
wfAppleZoneFilterCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleZoneFilterCircuit.setStatus("mandatory")
_WfAppleZoneFilterIpAddress_Type = IpAddress
_WfAppleZoneFilterIpAddress_Object = MibTableColumn
wfAppleZoneFilterIpAddress = _WfAppleZoneFilterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7, 1, 3),
    _WfAppleZoneFilterIpAddress_Type()
)
wfAppleZoneFilterIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleZoneFilterIpAddress.setStatus("mandatory")


class _WfAppleZoneFilterCircuitType_Type(Integer32):
    """Custom type wfAppleZoneFilterCircuitType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aurp", 2),
          ("rtmp", 1))
    )


_WfAppleZoneFilterCircuitType_Type.__name__ = "Integer32"
_WfAppleZoneFilterCircuitType_Object = MibTableColumn
wfAppleZoneFilterCircuitType = _WfAppleZoneFilterCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7, 1, 4),
    _WfAppleZoneFilterCircuitType_Type()
)
wfAppleZoneFilterCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleZoneFilterCircuitType.setStatus("mandatory")
_WfAppleZoneFilterIndex_Type = Integer32
_WfAppleZoneFilterIndex_Object = MibTableColumn
wfAppleZoneFilterIndex = _WfAppleZoneFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7, 1, 5),
    _WfAppleZoneFilterIndex_Type()
)
wfAppleZoneFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleZoneFilterIndex.setStatus("mandatory")
_WfAppleZoneFilterName_Type = DisplayString
_WfAppleZoneFilterName_Object = MibTableColumn
wfAppleZoneFilterName = _WfAppleZoneFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 7, 1, 6),
    _WfAppleZoneFilterName_Type()
)
wfAppleZoneFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleZoneFilterName.setStatus("mandatory")
_WfAppleAurpBase_ObjectIdentity = ObjectIdentity
wfAppleAurpBase = _WfAppleAurpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8)
)


class _WfAppleAurpBaseDelete_Type(Integer32):
    """Custom type wfAppleAurpBaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppleAurpBaseDelete_Type.__name__ = "Integer32"
_WfAppleAurpBaseDelete_Object = MibScalar
wfAppleAurpBaseDelete = _WfAppleAurpBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 1),
    _WfAppleAurpBaseDelete_Type()
)
wfAppleAurpBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpBaseDelete.setStatus("mandatory")


class _WfAppleAurpBaseDisable_Type(Integer32):
    """Custom type wfAppleAurpBaseDisable based on Integer32"""
    defaultValue = 1

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


_WfAppleAurpBaseDisable_Type.__name__ = "Integer32"
_WfAppleAurpBaseDisable_Object = MibScalar
wfAppleAurpBaseDisable = _WfAppleAurpBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 2),
    _WfAppleAurpBaseDisable_Type()
)
wfAppleAurpBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpBaseDisable.setStatus("mandatory")


class _WfAppleAurpBaseState_Type(Integer32):
    """Custom type wfAppleAurpBaseState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfAppleAurpBaseState_Type.__name__ = "Integer32"
_WfAppleAurpBaseState_Object = MibScalar
wfAppleAurpBaseState = _WfAppleAurpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 3),
    _WfAppleAurpBaseState_Type()
)
wfAppleAurpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpBaseState.setStatus("mandatory")
_WfAppleAurpBaseDomain_Type = OctetString
_WfAppleAurpBaseDomain_Object = MibScalar
wfAppleAurpBaseDomain = _WfAppleAurpBaseDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 4),
    _WfAppleAurpBaseDomain_Type()
)
wfAppleAurpBaseDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpBaseDomain.setStatus("mandatory")
_WfAppleAurpBaseIpAddress_Type = IpAddress
_WfAppleAurpBaseIpAddress_Object = MibScalar
wfAppleAurpBaseIpAddress = _WfAppleAurpBaseIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 5),
    _WfAppleAurpBaseIpAddress_Type()
)
wfAppleAurpBaseIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpBaseIpAddress.setStatus("mandatory")


class _WfAppleAurpBasePromiscuous_Type(Integer32):
    """Custom type wfAppleAurpBasePromiscuous based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpromisc", 1),
          ("promisc", 2))
    )


_WfAppleAurpBasePromiscuous_Type.__name__ = "Integer32"
_WfAppleAurpBasePromiscuous_Object = MibScalar
wfAppleAurpBasePromiscuous = _WfAppleAurpBasePromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 6),
    _WfAppleAurpBasePromiscuous_Type()
)
wfAppleAurpBasePromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpBasePromiscuous.setStatus("mandatory")
_WfAppleAurpBaseInAcceptedOpenReqs_Type = Counter32
_WfAppleAurpBaseInAcceptedOpenReqs_Object = MibScalar
wfAppleAurpBaseInAcceptedOpenReqs = _WfAppleAurpBaseInAcceptedOpenReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 7),
    _WfAppleAurpBaseInAcceptedOpenReqs_Type()
)
wfAppleAurpBaseInAcceptedOpenReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpBaseInAcceptedOpenReqs.setStatus("mandatory")
_WfAppleAurpBaseInRejectedOpenReqs_Type = Counter32
_WfAppleAurpBaseInRejectedOpenReqs_Object = MibScalar
wfAppleAurpBaseInRejectedOpenReqs = _WfAppleAurpBaseInRejectedOpenReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 8),
    _WfAppleAurpBaseInRejectedOpenReqs_Type()
)
wfAppleAurpBaseInRejectedOpenReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpBaseInRejectedOpenReqs.setStatus("mandatory")
_WfAppleAurpBaseInRouterDowns_Type = Counter32
_WfAppleAurpBaseInRouterDowns_Object = MibScalar
wfAppleAurpBaseInRouterDowns = _WfAppleAurpBaseInRouterDowns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 9),
    _WfAppleAurpBaseInRouterDowns_Type()
)
wfAppleAurpBaseInRouterDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpBaseInRouterDowns.setStatus("mandatory")
_WfAppleAurpBaseInPktsNoPeers_Type = Counter32
_WfAppleAurpBaseInPktsNoPeers_Object = MibScalar
wfAppleAurpBaseInPktsNoPeers = _WfAppleAurpBaseInPktsNoPeers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 10),
    _WfAppleAurpBaseInPktsNoPeers_Type()
)
wfAppleAurpBaseInPktsNoPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpBaseInPktsNoPeers.setStatus("mandatory")
_WfAppleAurpBaseInInvalidVerions_Type = Counter32
_WfAppleAurpBaseInInvalidVerions_Object = MibScalar
wfAppleAurpBaseInInvalidVerions = _WfAppleAurpBaseInInvalidVerions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 8, 11),
    _WfAppleAurpBaseInInvalidVerions_Type()
)
wfAppleAurpBaseInInvalidVerions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpBaseInInvalidVerions.setStatus("mandatory")
_WfAppleAurpTable_Object = MibTable
wfAppleAurpTable = _WfAppleAurpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9)
)
if mibBuilder.loadTexts:
    wfAppleAurpTable.setStatus("mandatory")
_WfAppleAurpEntry_Object = MibTableRow
wfAppleAurpEntry = _WfAppleAurpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1)
)
wfAppleAurpEntry.setIndexNames(
    (0, "Wellfleet-AT-MIB", "wfAppleAurpEntryIpAddress"),
)
if mibBuilder.loadTexts:
    wfAppleAurpEntry.setStatus("mandatory")


class _WfAppleAurpEntryDelete_Type(Integer32):
    """Custom type wfAppleAurpEntryDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppleAurpEntryDelete_Type.__name__ = "Integer32"
_WfAppleAurpEntryDelete_Object = MibTableColumn
wfAppleAurpEntryDelete = _WfAppleAurpEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 1),
    _WfAppleAurpEntryDelete_Type()
)
wfAppleAurpEntryDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryDelete.setStatus("mandatory")


class _WfAppleAurpEntryDisable_Type(Integer32):
    """Custom type wfAppleAurpEntryDisable based on Integer32"""
    defaultValue = 1

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


_WfAppleAurpEntryDisable_Type.__name__ = "Integer32"
_WfAppleAurpEntryDisable_Object = MibTableColumn
wfAppleAurpEntryDisable = _WfAppleAurpEntryDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 2),
    _WfAppleAurpEntryDisable_Type()
)
wfAppleAurpEntryDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryDisable.setStatus("mandatory")


class _WfAppleAurpEntryState_Type(Integer32):
    """Custom type wfAppleAurpEntryState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfAppleAurpEntryState_Type.__name__ = "Integer32"
_WfAppleAurpEntryState_Object = MibTableColumn
wfAppleAurpEntryState = _WfAppleAurpEntryState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 3),
    _WfAppleAurpEntryState_Type()
)
wfAppleAurpEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryState.setStatus("mandatory")
_WfAppleAurpEntryIpAddress_Type = IpAddress
_WfAppleAurpEntryIpAddress_Object = MibTableColumn
wfAppleAurpEntryIpAddress = _WfAppleAurpEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 4),
    _WfAppleAurpEntryIpAddress_Type()
)
wfAppleAurpEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryIpAddress.setStatus("mandatory")


class _WfAppleAurpEntryZoneFilterType_Type(Integer32):
    """Custom type wfAppleAurpEntryZoneFilterType based on Integer32"""
    defaultValue = 2

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
        *(("allow", 1),
          ("deny", 2),
          ("partallow", 3),
          ("partdeny", 4))
    )


_WfAppleAurpEntryZoneFilterType_Type.__name__ = "Integer32"
_WfAppleAurpEntryZoneFilterType_Object = MibTableColumn
wfAppleAurpEntryZoneFilterType = _WfAppleAurpEntryZoneFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 5),
    _WfAppleAurpEntryZoneFilterType_Type()
)
wfAppleAurpEntryZoneFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryZoneFilterType.setStatus("mandatory")


class _WfAppleAurpEntryTimeoutCommand_Type(Integer32):
    """Custom type wfAppleAurpEntryTimeoutCommand based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WfAppleAurpEntryTimeoutCommand_Type.__name__ = "Integer32"
_WfAppleAurpEntryTimeoutCommand_Object = MibTableColumn
wfAppleAurpEntryTimeoutCommand = _WfAppleAurpEntryTimeoutCommand_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 6),
    _WfAppleAurpEntryTimeoutCommand_Type()
)
wfAppleAurpEntryTimeoutCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryTimeoutCommand.setStatus("mandatory")


class _WfAppleAurpEntryRetryCommand_Type(Integer32):
    """Custom type wfAppleAurpEntryRetryCommand based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfAppleAurpEntryRetryCommand_Type.__name__ = "Integer32"
_WfAppleAurpEntryRetryCommand_Object = MibTableColumn
wfAppleAurpEntryRetryCommand = _WfAppleAurpEntryRetryCommand_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 7),
    _WfAppleAurpEntryRetryCommand_Type()
)
wfAppleAurpEntryRetryCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryRetryCommand.setStatus("mandatory")


class _WfAppleAurpEntryUpdateRate_Type(Integer32):
    """Custom type wfAppleAurpEntryUpdateRate based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 604800),
    )


_WfAppleAurpEntryUpdateRate_Type.__name__ = "Integer32"
_WfAppleAurpEntryUpdateRate_Object = MibTableColumn
wfAppleAurpEntryUpdateRate = _WfAppleAurpEntryUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 8),
    _WfAppleAurpEntryUpdateRate_Type()
)
wfAppleAurpEntryUpdateRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryUpdateRate.setStatus("mandatory")


class _WfAppleAurpEntryLhfTimeout_Type(Integer32):
    """Custom type wfAppleAurpEntryLhfTimeout based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 31536000),
    )


_WfAppleAurpEntryLhfTimeout_Type.__name__ = "Integer32"
_WfAppleAurpEntryLhfTimeout_Object = MibTableColumn
wfAppleAurpEntryLhfTimeout = _WfAppleAurpEntryLhfTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 9),
    _WfAppleAurpEntryLhfTimeout_Type()
)
wfAppleAurpEntryLhfTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryLhfTimeout.setStatus("mandatory")


class _WfAppleAurpEntryHopCountReduction_Type(Integer32):
    """Custom type wfAppleAurpEntryHopCountReduction based on Integer32"""
    defaultValue = 2

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


_WfAppleAurpEntryHopCountReduction_Type.__name__ = "Integer32"
_WfAppleAurpEntryHopCountReduction_Object = MibTableColumn
wfAppleAurpEntryHopCountReduction = _WfAppleAurpEntryHopCountReduction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 10),
    _WfAppleAurpEntryHopCountReduction_Type()
)
wfAppleAurpEntryHopCountReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryHopCountReduction.setStatus("mandatory")
_WfAppleAurpEntryInterfaceCost_Type = Integer32
_WfAppleAurpEntryInterfaceCost_Object = MibTableColumn
wfAppleAurpEntryInterfaceCost = _WfAppleAurpEntryInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 11),
    _WfAppleAurpEntryInterfaceCost_Type()
)
wfAppleAurpEntryInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInterfaceCost.setStatus("mandatory")


class _WfAppleAurpEntrySuiFlags_Type(Integer32):
    """Custom type wfAppleAurpEntrySuiFlags based on Integer32"""
    defaultValue = 30720

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            30720
        )
    )
    namedValues = NamedValues(
        ("all", 30720)
    )


_WfAppleAurpEntrySuiFlags_Type.__name__ = "Integer32"
_WfAppleAurpEntrySuiFlags_Object = MibTableColumn
wfAppleAurpEntrySuiFlags = _WfAppleAurpEntrySuiFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 12),
    _WfAppleAurpEntrySuiFlags_Type()
)
wfAppleAurpEntrySuiFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntrySuiFlags.setStatus("mandatory")
_WfAppleAurpEntryType_Type = Integer32
_WfAppleAurpEntryType_Object = MibTableColumn
wfAppleAurpEntryType = _WfAppleAurpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 13),
    _WfAppleAurpEntryType_Type()
)
wfAppleAurpEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryType.setStatus("mandatory")
_WfAppleAurpEntryPeerDomainId_Type = IpAddress
_WfAppleAurpEntryPeerDomainId_Object = MibTableColumn
wfAppleAurpEntryPeerDomainId = _WfAppleAurpEntryPeerDomainId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 14),
    _WfAppleAurpEntryPeerDomainId_Type()
)
wfAppleAurpEntryPeerDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryPeerDomainId.setStatus("mandatory")
_WfAppleAurpEntryPeerUpdateRate_Type = Integer32
_WfAppleAurpEntryPeerUpdateRate_Object = MibTableColumn
wfAppleAurpEntryPeerUpdateRate = _WfAppleAurpEntryPeerUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 15),
    _WfAppleAurpEntryPeerUpdateRate_Type()
)
wfAppleAurpEntryPeerUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryPeerUpdateRate.setStatus("mandatory")
_WfAppleAurpEntryPeerEnvironment_Type = Integer32
_WfAppleAurpEntryPeerEnvironment_Object = MibTableColumn
wfAppleAurpEntryPeerEnvironment = _WfAppleAurpEntryPeerEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 16),
    _WfAppleAurpEntryPeerEnvironment_Type()
)
wfAppleAurpEntryPeerEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryPeerEnvironment.setStatus("mandatory")
_WfAppleAurpEntryPeerSuiFlags_Type = Integer32
_WfAppleAurpEntryPeerSuiFlags_Object = MibTableColumn
wfAppleAurpEntryPeerSuiFlags = _WfAppleAurpEntryPeerSuiFlags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 17),
    _WfAppleAurpEntryPeerSuiFlags_Type()
)
wfAppleAurpEntryPeerSuiFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryPeerSuiFlags.setStatus("mandatory")
_WfAppleAurpEntryCliConnId_Type = Integer32
_WfAppleAurpEntryCliConnId_Object = MibTableColumn
wfAppleAurpEntryCliConnId = _WfAppleAurpEntryCliConnId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 18),
    _WfAppleAurpEntryCliConnId_Type()
)
wfAppleAurpEntryCliConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryCliConnId.setStatus("mandatory")
_WfAppleAurpEntrySrvConnId_Type = Integer32
_WfAppleAurpEntrySrvConnId_Object = MibTableColumn
wfAppleAurpEntrySrvConnId = _WfAppleAurpEntrySrvConnId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 19),
    _WfAppleAurpEntrySrvConnId_Type()
)
wfAppleAurpEntrySrvConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntrySrvConnId.setStatus("mandatory")
_WfAppleAurpEntryCliSeqNum_Type = Integer32
_WfAppleAurpEntryCliSeqNum_Object = MibTableColumn
wfAppleAurpEntryCliSeqNum = _WfAppleAurpEntryCliSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 20),
    _WfAppleAurpEntryCliSeqNum_Type()
)
wfAppleAurpEntryCliSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryCliSeqNum.setStatus("mandatory")
_WfAppleAurpEntrySrvSeqNum_Type = Integer32
_WfAppleAurpEntrySrvSeqNum_Object = MibTableColumn
wfAppleAurpEntrySrvSeqNum = _WfAppleAurpEntrySrvSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 21),
    _WfAppleAurpEntrySrvSeqNum_Type()
)
wfAppleAurpEntrySrvSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntrySrvSeqNum.setStatus("mandatory")
_WfAppleAurpEntryCommandRetries_Type = Counter32
_WfAppleAurpEntryCommandRetries_Object = MibTableColumn
wfAppleAurpEntryCommandRetries = _WfAppleAurpEntryCommandRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 22),
    _WfAppleAurpEntryCommandRetries_Type()
)
wfAppleAurpEntryCommandRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryCommandRetries.setStatus("mandatory")
_WfAppleAurpEntryInDelayedDuplicates_Type = Counter32
_WfAppleAurpEntryInDelayedDuplicates_Object = MibTableColumn
wfAppleAurpEntryInDelayedDuplicates = _WfAppleAurpEntryInDelayedDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 23),
    _WfAppleAurpEntryInDelayedDuplicates_Type()
)
wfAppleAurpEntryInDelayedDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInDelayedDuplicates.setStatus("mandatory")
_WfAppleAurpEntryInInvalidConnIds_Type = Counter32
_WfAppleAurpEntryInInvalidConnIds_Object = MibTableColumn
wfAppleAurpEntryInInvalidConnIds = _WfAppleAurpEntryInInvalidConnIds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 24),
    _WfAppleAurpEntryInInvalidConnIds_Type()
)
wfAppleAurpEntryInInvalidConnIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInInvalidConnIds.setStatus("mandatory")
_WfAppleAurpEntryInInvalidCommands_Type = Counter32
_WfAppleAurpEntryInInvalidCommands_Object = MibTableColumn
wfAppleAurpEntryInInvalidCommands = _WfAppleAurpEntryInInvalidCommands_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 25),
    _WfAppleAurpEntryInInvalidCommands_Type()
)
wfAppleAurpEntryInInvalidCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInInvalidCommands.setStatus("mandatory")
_WfAppleAurpEntryInInvalidSubCodes_Type = Counter32
_WfAppleAurpEntryInInvalidSubCodes_Object = MibTableColumn
wfAppleAurpEntryInInvalidSubCodes = _WfAppleAurpEntryInInvalidSubCodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 26),
    _WfAppleAurpEntryInInvalidSubCodes_Type()
)
wfAppleAurpEntryInInvalidSubCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInInvalidSubCodes.setStatus("mandatory")
_WfAppleAurpEntryInPkts_Type = Counter32
_WfAppleAurpEntryInPkts_Object = MibTableColumn
wfAppleAurpEntryInPkts = _WfAppleAurpEntryInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 27),
    _WfAppleAurpEntryInPkts_Type()
)
wfAppleAurpEntryInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInPkts.setStatus("mandatory")
_WfAppleAurpEntryOutPkts_Type = Counter32
_WfAppleAurpEntryOutPkts_Object = MibTableColumn
wfAppleAurpEntryOutPkts = _WfAppleAurpEntryOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 28),
    _WfAppleAurpEntryOutPkts_Type()
)
wfAppleAurpEntryOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutPkts.setStatus("mandatory")
_WfAppleAurpEntryInDdpPkts_Type = Counter32
_WfAppleAurpEntryInDdpPkts_Object = MibTableColumn
wfAppleAurpEntryInDdpPkts = _WfAppleAurpEntryInDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 29),
    _WfAppleAurpEntryInDdpPkts_Type()
)
wfAppleAurpEntryInDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInDdpPkts.setStatus("mandatory")
_WfAppleAurpEntryOutDdpPkts_Type = Counter32
_WfAppleAurpEntryOutDdpPkts_Object = MibTableColumn
wfAppleAurpEntryOutDdpPkts = _WfAppleAurpEntryOutDdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 30),
    _WfAppleAurpEntryOutDdpPkts_Type()
)
wfAppleAurpEntryOutDdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutDdpPkts.setStatus("mandatory")
_WfAppleAurpEntryOutNoRoutes_Type = Counter32
_WfAppleAurpEntryOutNoRoutes_Object = MibTableColumn
wfAppleAurpEntryOutNoRoutes = _WfAppleAurpEntryOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 31),
    _WfAppleAurpEntryOutNoRoutes_Type()
)
wfAppleAurpEntryOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutNoRoutes.setStatus("mandatory")
_WfAppleAurpEntryHopCountErrors_Type = Counter32
_WfAppleAurpEntryHopCountErrors_Object = MibTableColumn
wfAppleAurpEntryHopCountErrors = _WfAppleAurpEntryHopCountErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 32),
    _WfAppleAurpEntryHopCountErrors_Type()
)
wfAppleAurpEntryHopCountErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryHopCountErrors.setStatus("mandatory")
_WfAppleAurpEntryHopCountAdjustments_Type = Counter32
_WfAppleAurpEntryHopCountAdjustments_Object = MibTableColumn
wfAppleAurpEntryHopCountAdjustments = _WfAppleAurpEntryHopCountAdjustments_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 33),
    _WfAppleAurpEntryHopCountAdjustments_Type()
)
wfAppleAurpEntryHopCountAdjustments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryHopCountAdjustments.setStatus("mandatory")
_WfAppleAurpEntryInAurpPkts_Type = Counter32
_WfAppleAurpEntryInAurpPkts_Object = MibTableColumn
wfAppleAurpEntryInAurpPkts = _WfAppleAurpEntryInAurpPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 34),
    _WfAppleAurpEntryInAurpPkts_Type()
)
wfAppleAurpEntryInAurpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInAurpPkts.setStatus("mandatory")
_WfAppleAurpEntryOutAurpPkts_Type = Counter32
_WfAppleAurpEntryOutAurpPkts_Object = MibTableColumn
wfAppleAurpEntryOutAurpPkts = _WfAppleAurpEntryOutAurpPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 35),
    _WfAppleAurpEntryOutAurpPkts_Type()
)
wfAppleAurpEntryOutAurpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutAurpPkts.setStatus("mandatory")
_WfAppleAurpEntryInOpenRequests_Type = Counter32
_WfAppleAurpEntryInOpenRequests_Object = MibTableColumn
wfAppleAurpEntryInOpenRequests = _WfAppleAurpEntryInOpenRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 36),
    _WfAppleAurpEntryInOpenRequests_Type()
)
wfAppleAurpEntryInOpenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInOpenRequests.setStatus("mandatory")
_WfAppleAurpEntryOutOpenRequests_Type = Counter32
_WfAppleAurpEntryOutOpenRequests_Object = MibTableColumn
wfAppleAurpEntryOutOpenRequests = _WfAppleAurpEntryOutOpenRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 37),
    _WfAppleAurpEntryOutOpenRequests_Type()
)
wfAppleAurpEntryOutOpenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutOpenRequests.setStatus("mandatory")
_WfAppleAurpEntryInOpenResponses_Type = Counter32
_WfAppleAurpEntryInOpenResponses_Object = MibTableColumn
wfAppleAurpEntryInOpenResponses = _WfAppleAurpEntryInOpenResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 38),
    _WfAppleAurpEntryInOpenResponses_Type()
)
wfAppleAurpEntryInOpenResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInOpenResponses.setStatus("mandatory")
_WfAppleAurpEntryOutOpenResponses_Type = Counter32
_WfAppleAurpEntryOutOpenResponses_Object = MibTableColumn
wfAppleAurpEntryOutOpenResponses = _WfAppleAurpEntryOutOpenResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 39),
    _WfAppleAurpEntryOutOpenResponses_Type()
)
wfAppleAurpEntryOutOpenResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutOpenResponses.setStatus("mandatory")
_WfAppleAurpEntryInRiRequests_Type = Counter32
_WfAppleAurpEntryInRiRequests_Object = MibTableColumn
wfAppleAurpEntryInRiRequests = _WfAppleAurpEntryInRiRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 40),
    _WfAppleAurpEntryInRiRequests_Type()
)
wfAppleAurpEntryInRiRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInRiRequests.setStatus("mandatory")
_WfAppleAurpEntryOutRiRequests_Type = Counter32
_WfAppleAurpEntryOutRiRequests_Object = MibTableColumn
wfAppleAurpEntryOutRiRequests = _WfAppleAurpEntryOutRiRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 41),
    _WfAppleAurpEntryOutRiRequests_Type()
)
wfAppleAurpEntryOutRiRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutRiRequests.setStatus("mandatory")
_WfAppleAurpEntryInRiResponses_Type = Counter32
_WfAppleAurpEntryInRiResponses_Object = MibTableColumn
wfAppleAurpEntryInRiResponses = _WfAppleAurpEntryInRiResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 42),
    _WfAppleAurpEntryInRiResponses_Type()
)
wfAppleAurpEntryInRiResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInRiResponses.setStatus("mandatory")
_WfAppleAurpEntryOutRiResponses_Type = Counter32
_WfAppleAurpEntryOutRiResponses_Object = MibTableColumn
wfAppleAurpEntryOutRiResponses = _WfAppleAurpEntryOutRiResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 43),
    _WfAppleAurpEntryOutRiResponses_Type()
)
wfAppleAurpEntryOutRiResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutRiResponses.setStatus("mandatory")
_WfAppleAurpEntryInRiAcks_Type = Counter32
_WfAppleAurpEntryInRiAcks_Object = MibTableColumn
wfAppleAurpEntryInRiAcks = _WfAppleAurpEntryInRiAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 44),
    _WfAppleAurpEntryInRiAcks_Type()
)
wfAppleAurpEntryInRiAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInRiAcks.setStatus("mandatory")
_WfAppleAurpEntryOutRiAcks_Type = Counter32
_WfAppleAurpEntryOutRiAcks_Object = MibTableColumn
wfAppleAurpEntryOutRiAcks = _WfAppleAurpEntryOutRiAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 45),
    _WfAppleAurpEntryOutRiAcks_Type()
)
wfAppleAurpEntryOutRiAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutRiAcks.setStatus("mandatory")
_WfAppleAurpEntryInRiUpdates_Type = Counter32
_WfAppleAurpEntryInRiUpdates_Object = MibTableColumn
wfAppleAurpEntryInRiUpdates = _WfAppleAurpEntryInRiUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 46),
    _WfAppleAurpEntryInRiUpdates_Type()
)
wfAppleAurpEntryInRiUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInRiUpdates.setStatus("mandatory")
_WfAppleAurpEntryOutRiUpdates_Type = Counter32
_WfAppleAurpEntryOutRiUpdates_Object = MibTableColumn
wfAppleAurpEntryOutRiUpdates = _WfAppleAurpEntryOutRiUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 47),
    _WfAppleAurpEntryOutRiUpdates_Type()
)
wfAppleAurpEntryOutRiUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutRiUpdates.setStatus("mandatory")
_WfAppleAurpEntryInUpdateNullEvents_Type = Counter32
_WfAppleAurpEntryInUpdateNullEvents_Object = MibTableColumn
wfAppleAurpEntryInUpdateNullEvents = _WfAppleAurpEntryInUpdateNullEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 48),
    _WfAppleAurpEntryInUpdateNullEvents_Type()
)
wfAppleAurpEntryInUpdateNullEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInUpdateNullEvents.setStatus("mandatory")
_WfAppleAurpEntryOutUpdateNullEvents_Type = Counter32
_WfAppleAurpEntryOutUpdateNullEvents_Object = MibTableColumn
wfAppleAurpEntryOutUpdateNullEvents = _WfAppleAurpEntryOutUpdateNullEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 49),
    _WfAppleAurpEntryOutUpdateNullEvents_Type()
)
wfAppleAurpEntryOutUpdateNullEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutUpdateNullEvents.setStatus("mandatory")
_WfAppleAurpEntryInUpdateNetAdds_Type = Counter32
_WfAppleAurpEntryInUpdateNetAdds_Object = MibTableColumn
wfAppleAurpEntryInUpdateNetAdds = _WfAppleAurpEntryInUpdateNetAdds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 50),
    _WfAppleAurpEntryInUpdateNetAdds_Type()
)
wfAppleAurpEntryInUpdateNetAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInUpdateNetAdds.setStatus("mandatory")
_WfAppleAurpEntryOutUpdateNetAdds_Type = Counter32
_WfAppleAurpEntryOutUpdateNetAdds_Object = MibTableColumn
wfAppleAurpEntryOutUpdateNetAdds = _WfAppleAurpEntryOutUpdateNetAdds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 51),
    _WfAppleAurpEntryOutUpdateNetAdds_Type()
)
wfAppleAurpEntryOutUpdateNetAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutUpdateNetAdds.setStatus("mandatory")
_WfAppleAurpEntryInUpdateNetDeletes_Type = Counter32
_WfAppleAurpEntryInUpdateNetDeletes_Object = MibTableColumn
wfAppleAurpEntryInUpdateNetDeletes = _WfAppleAurpEntryInUpdateNetDeletes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 52),
    _WfAppleAurpEntryInUpdateNetDeletes_Type()
)
wfAppleAurpEntryInUpdateNetDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInUpdateNetDeletes.setStatus("mandatory")
_WfAppleAurpEntryOutUpdateNetDeletes_Type = Counter32
_WfAppleAurpEntryOutUpdateNetDeletes_Object = MibTableColumn
wfAppleAurpEntryOutUpdateNetDeletes = _WfAppleAurpEntryOutUpdateNetDeletes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 53),
    _WfAppleAurpEntryOutUpdateNetDeletes_Type()
)
wfAppleAurpEntryOutUpdateNetDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutUpdateNetDeletes.setStatus("mandatory")
_WfAppleAurpEntryInUpdateNetRouteChanges_Type = Counter32
_WfAppleAurpEntryInUpdateNetRouteChanges_Object = MibTableColumn
wfAppleAurpEntryInUpdateNetRouteChanges = _WfAppleAurpEntryInUpdateNetRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 54),
    _WfAppleAurpEntryInUpdateNetRouteChanges_Type()
)
wfAppleAurpEntryInUpdateNetRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInUpdateNetRouteChanges.setStatus("mandatory")
_WfAppleAurpEntryOutUpdateNetRouteChanges_Type = Counter32
_WfAppleAurpEntryOutUpdateNetRouteChanges_Object = MibTableColumn
wfAppleAurpEntryOutUpdateNetRouteChanges = _WfAppleAurpEntryOutUpdateNetRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 55),
    _WfAppleAurpEntryOutUpdateNetRouteChanges_Type()
)
wfAppleAurpEntryOutUpdateNetRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutUpdateNetRouteChanges.setStatus("mandatory")
_WfAppleAurpEntryInUpdateNetDistanceChanges_Type = Counter32
_WfAppleAurpEntryInUpdateNetDistanceChanges_Object = MibTableColumn
wfAppleAurpEntryInUpdateNetDistanceChanges = _WfAppleAurpEntryInUpdateNetDistanceChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 56),
    _WfAppleAurpEntryInUpdateNetDistanceChanges_Type()
)
wfAppleAurpEntryInUpdateNetDistanceChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInUpdateNetDistanceChanges.setStatus("mandatory")
_WfAppleAurpEntryOutUpdateNetDistanceChanges_Type = Counter32
_WfAppleAurpEntryOutUpdateNetDistanceChanges_Object = MibTableColumn
wfAppleAurpEntryOutUpdateNetDistanceChanges = _WfAppleAurpEntryOutUpdateNetDistanceChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 57),
    _WfAppleAurpEntryOutUpdateNetDistanceChanges_Type()
)
wfAppleAurpEntryOutUpdateNetDistanceChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutUpdateNetDistanceChanges.setStatus("mandatory")
_WfAppleAurpEntryInUpdateZoneChanges_Type = Counter32
_WfAppleAurpEntryInUpdateZoneChanges_Object = MibTableColumn
wfAppleAurpEntryInUpdateZoneChanges = _WfAppleAurpEntryInUpdateZoneChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 58),
    _WfAppleAurpEntryInUpdateZoneChanges_Type()
)
wfAppleAurpEntryInUpdateZoneChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInUpdateZoneChanges.setStatus("mandatory")
_WfAppleAurpEntryOutUpdateZoneChanges_Type = Counter32
_WfAppleAurpEntryOutUpdateZoneChanges_Object = MibTableColumn
wfAppleAurpEntryOutUpdateZoneChanges = _WfAppleAurpEntryOutUpdateZoneChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 59),
    _WfAppleAurpEntryOutUpdateZoneChanges_Type()
)
wfAppleAurpEntryOutUpdateZoneChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutUpdateZoneChanges.setStatus("mandatory")
_WfAppleAurpEntryInUpdateInvalidEvents_Type = Counter32
_WfAppleAurpEntryInUpdateInvalidEvents_Object = MibTableColumn
wfAppleAurpEntryInUpdateInvalidEvents = _WfAppleAurpEntryInUpdateInvalidEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 60),
    _WfAppleAurpEntryInUpdateInvalidEvents_Type()
)
wfAppleAurpEntryInUpdateInvalidEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInUpdateInvalidEvents.setStatus("mandatory")
_WfAppleAurpEntryOutUpdateInvalidEvents_Type = Counter32
_WfAppleAurpEntryOutUpdateInvalidEvents_Object = MibTableColumn
wfAppleAurpEntryOutUpdateInvalidEvents = _WfAppleAurpEntryOutUpdateInvalidEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 61),
    _WfAppleAurpEntryOutUpdateInvalidEvents_Type()
)
wfAppleAurpEntryOutUpdateInvalidEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutUpdateInvalidEvents.setStatus("mandatory")
_WfAppleAurpEntryInZiRequests_Type = Counter32
_WfAppleAurpEntryInZiRequests_Object = MibTableColumn
wfAppleAurpEntryInZiRequests = _WfAppleAurpEntryInZiRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 62),
    _WfAppleAurpEntryInZiRequests_Type()
)
wfAppleAurpEntryInZiRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInZiRequests.setStatus("mandatory")
_WfAppleAurpEntryOutZiRequests_Type = Counter32
_WfAppleAurpEntryOutZiRequests_Object = MibTableColumn
wfAppleAurpEntryOutZiRequests = _WfAppleAurpEntryOutZiRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 63),
    _WfAppleAurpEntryOutZiRequests_Type()
)
wfAppleAurpEntryOutZiRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutZiRequests.setStatus("mandatory")
_WfAppleAurpEntryInZiResponses_Type = Counter32
_WfAppleAurpEntryInZiResponses_Object = MibTableColumn
wfAppleAurpEntryInZiResponses = _WfAppleAurpEntryInZiResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 64),
    _WfAppleAurpEntryInZiResponses_Type()
)
wfAppleAurpEntryInZiResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInZiResponses.setStatus("mandatory")
_WfAppleAurpEntryOutZiResponses_Type = Counter32
_WfAppleAurpEntryOutZiResponses_Object = MibTableColumn
wfAppleAurpEntryOutZiResponses = _WfAppleAurpEntryOutZiResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 65),
    _WfAppleAurpEntryOutZiResponses_Type()
)
wfAppleAurpEntryOutZiResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutZiResponses.setStatus("mandatory")
_WfAppleAurpEntryInGdzlRequests_Type = Counter32
_WfAppleAurpEntryInGdzlRequests_Object = MibTableColumn
wfAppleAurpEntryInGdzlRequests = _WfAppleAurpEntryInGdzlRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 66),
    _WfAppleAurpEntryInGdzlRequests_Type()
)
wfAppleAurpEntryInGdzlRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInGdzlRequests.setStatus("mandatory")
_WfAppleAurpEntryOutGdzlRequests_Type = Counter32
_WfAppleAurpEntryOutGdzlRequests_Object = MibTableColumn
wfAppleAurpEntryOutGdzlRequests = _WfAppleAurpEntryOutGdzlRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 67),
    _WfAppleAurpEntryOutGdzlRequests_Type()
)
wfAppleAurpEntryOutGdzlRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutGdzlRequests.setStatus("mandatory")
_WfAppleAurpEntryInGdzlResponses_Type = Counter32
_WfAppleAurpEntryInGdzlResponses_Object = MibTableColumn
wfAppleAurpEntryInGdzlResponses = _WfAppleAurpEntryInGdzlResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 68),
    _WfAppleAurpEntryInGdzlResponses_Type()
)
wfAppleAurpEntryInGdzlResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInGdzlResponses.setStatus("mandatory")
_WfAppleAurpEntryOutGdzlResponses_Type = Counter32
_WfAppleAurpEntryOutGdzlResponses_Object = MibTableColumn
wfAppleAurpEntryOutGdzlResponses = _WfAppleAurpEntryOutGdzlResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 69),
    _WfAppleAurpEntryOutGdzlResponses_Type()
)
wfAppleAurpEntryOutGdzlResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutGdzlResponses.setStatus("mandatory")
_WfAppleAurpEntryInGznRequests_Type = Counter32
_WfAppleAurpEntryInGznRequests_Object = MibTableColumn
wfAppleAurpEntryInGznRequests = _WfAppleAurpEntryInGznRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 70),
    _WfAppleAurpEntryInGznRequests_Type()
)
wfAppleAurpEntryInGznRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInGznRequests.setStatus("mandatory")
_WfAppleAurpEntryOutGznRequests_Type = Counter32
_WfAppleAurpEntryOutGznRequests_Object = MibTableColumn
wfAppleAurpEntryOutGznRequests = _WfAppleAurpEntryOutGznRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 71),
    _WfAppleAurpEntryOutGznRequests_Type()
)
wfAppleAurpEntryOutGznRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutGznRequests.setStatus("mandatory")
_WfAppleAurpEntryInGznResponses_Type = Counter32
_WfAppleAurpEntryInGznResponses_Object = MibTableColumn
wfAppleAurpEntryInGznResponses = _WfAppleAurpEntryInGznResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 72),
    _WfAppleAurpEntryInGznResponses_Type()
)
wfAppleAurpEntryInGznResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInGznResponses.setStatus("mandatory")
_WfAppleAurpEntryOutGznResponses_Type = Counter32
_WfAppleAurpEntryOutGznResponses_Object = MibTableColumn
wfAppleAurpEntryOutGznResponses = _WfAppleAurpEntryOutGznResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 73),
    _WfAppleAurpEntryOutGznResponses_Type()
)
wfAppleAurpEntryOutGznResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutGznResponses.setStatus("mandatory")
_WfAppleAurpEntryInTickles_Type = Counter32
_WfAppleAurpEntryInTickles_Object = MibTableColumn
wfAppleAurpEntryInTickles = _WfAppleAurpEntryInTickles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 74),
    _WfAppleAurpEntryInTickles_Type()
)
wfAppleAurpEntryInTickles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInTickles.setStatus("mandatory")
_WfAppleAurpEntryOutTickles_Type = Counter32
_WfAppleAurpEntryOutTickles_Object = MibTableColumn
wfAppleAurpEntryOutTickles = _WfAppleAurpEntryOutTickles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 75),
    _WfAppleAurpEntryOutTickles_Type()
)
wfAppleAurpEntryOutTickles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutTickles.setStatus("mandatory")
_WfAppleAurpEntryInTickleAcks_Type = Counter32
_WfAppleAurpEntryInTickleAcks_Object = MibTableColumn
wfAppleAurpEntryInTickleAcks = _WfAppleAurpEntryInTickleAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 76),
    _WfAppleAurpEntryInTickleAcks_Type()
)
wfAppleAurpEntryInTickleAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInTickleAcks.setStatus("mandatory")
_WfAppleAurpEntryOutTickleAcks_Type = Counter32
_WfAppleAurpEntryOutTickleAcks_Object = MibTableColumn
wfAppleAurpEntryOutTickleAcks = _WfAppleAurpEntryOutTickleAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 77),
    _WfAppleAurpEntryOutTickleAcks_Type()
)
wfAppleAurpEntryOutTickleAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutTickleAcks.setStatus("mandatory")
_WfAppleAurpEntryInRouterDowns_Type = Counter32
_WfAppleAurpEntryInRouterDowns_Object = MibTableColumn
wfAppleAurpEntryInRouterDowns = _WfAppleAurpEntryInRouterDowns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 78),
    _WfAppleAurpEntryInRouterDowns_Type()
)
wfAppleAurpEntryInRouterDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryInRouterDowns.setStatus("mandatory")
_WfAppleAurpEntryOutRouterDowns_Type = Counter32
_WfAppleAurpEntryOutRouterDowns_Object = MibTableColumn
wfAppleAurpEntryOutRouterDowns = _WfAppleAurpEntryOutRouterDowns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 79),
    _WfAppleAurpEntryOutRouterDowns_Type()
)
wfAppleAurpEntryOutRouterDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAurpEntryOutRouterDowns.setStatus("mandatory")
_WfAppleAurpEntryZoneFiltDfltZone_Type = DisplayString
_WfAppleAurpEntryZoneFiltDfltZone_Object = MibTableColumn
wfAppleAurpEntryZoneFiltDfltZone = _WfAppleAurpEntryZoneFiltDfltZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 9, 1, 80),
    _WfAppleAurpEntryZoneFiltDfltZone_Type()
)
wfAppleAurpEntryZoneFiltDfltZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppleAurpEntryZoneFiltDfltZone.setStatus("mandatory")
_WfAppleAggrStats_ObjectIdentity = ObjectIdentity
wfAppleAggrStats = _WfAppleAggrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10)
)
_WfAppleAggrInPkts_Type = Counter32
_WfAppleAggrInPkts_Object = MibScalar
wfAppleAggrInPkts = _WfAppleAggrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 1),
    _WfAppleAggrInPkts_Type()
)
wfAppleAggrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrInPkts.setStatus("mandatory")
_WfAppleAggrOutPkts_Type = Counter32
_WfAppleAggrOutPkts_Object = MibScalar
wfAppleAggrOutPkts = _WfAppleAggrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 2),
    _WfAppleAggrOutPkts_Type()
)
wfAppleAggrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrOutPkts.setStatus("mandatory")
_WfAppleAggrFwdDatagrams_Type = Counter32
_WfAppleAggrFwdDatagrams_Object = MibScalar
wfAppleAggrFwdDatagrams = _WfAppleAggrFwdDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 3),
    _WfAppleAggrFwdDatagrams_Type()
)
wfAppleAggrFwdDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrFwdDatagrams.setStatus("mandatory")
_WfAppleAggrInXsumErrs_Type = Counter32
_WfAppleAggrInXsumErrs_Object = MibScalar
wfAppleAggrInXsumErrs = _WfAppleAggrInXsumErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 4),
    _WfAppleAggrInXsumErrs_Type()
)
wfAppleAggrInXsumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrInXsumErrs.setStatus("mandatory")
_WfAppleAggrInHopCountErrs_Type = Counter32
_WfAppleAggrInHopCountErrs_Object = MibScalar
wfAppleAggrInHopCountErrs = _WfAppleAggrInHopCountErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 5),
    _WfAppleAggrInHopCountErrs_Type()
)
wfAppleAggrInHopCountErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrInHopCountErrs.setStatus("mandatory")
_WfAppleAggrInTooShorts_Type = Counter32
_WfAppleAggrInTooShorts_Object = MibScalar
wfAppleAggrInTooShorts = _WfAppleAggrInTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 6),
    _WfAppleAggrInTooShorts_Type()
)
wfAppleAggrInTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrInTooShorts.setStatus("mandatory")
_WfAppleAggrInTooLongs_Type = Counter32
_WfAppleAggrInTooLongs_Object = MibScalar
wfAppleAggrInTooLongs = _WfAppleAggrInTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 7),
    _WfAppleAggrInTooLongs_Type()
)
wfAppleAggrInTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrInTooLongs.setStatus("mandatory")
_WfAppleAggrOutNoRoutes_Type = Counter32
_WfAppleAggrOutNoRoutes_Object = MibScalar
wfAppleAggrOutNoRoutes = _WfAppleAggrOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 8),
    _WfAppleAggrOutNoRoutes_Type()
)
wfAppleAggrOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrOutNoRoutes.setStatus("mandatory")
_WfAppleAggrInLocalDests_Type = Counter32
_WfAppleAggrInLocalDests_Object = MibScalar
wfAppleAggrInLocalDests = _WfAppleAggrInLocalDests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 9),
    _WfAppleAggrInLocalDests_Type()
)
wfAppleAggrInLocalDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrInLocalDests.setStatus("mandatory")
_WfAppleAggrInRtmps_Type = Counter32
_WfAppleAggrInRtmps_Object = MibScalar
wfAppleAggrInRtmps = _WfAppleAggrInRtmps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 10),
    _WfAppleAggrInRtmps_Type()
)
wfAppleAggrInRtmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrInRtmps.setStatus("mandatory")
_WfAppleAggrOutRtmps_Type = Counter32
_WfAppleAggrOutRtmps_Object = MibScalar
wfAppleAggrOutRtmps = _WfAppleAggrOutRtmps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 4, 10, 11),
    _WfAppleAggrOutRtmps_Type()
)
wfAppleAggrOutRtmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppleAggrOutRtmps.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-AT-MIB",
    **{"wfAppleBase": wfAppleBase,
       "wfAppleBaseDelete": wfAppleBaseDelete,
       "wfAppleBaseDisable": wfAppleBaseDisable,
       "wfAppleBaseState": wfAppleBaseState,
       "wfAppleBaseDebugLevel": wfAppleBaseDebugLevel,
       "wfAppleBaseDdpQueLen": wfAppleBaseDdpQueLen,
       "wfAppleBaseHomedPort": wfAppleBaseHomedPort,
       "wfAppleBaseTotalNets": wfAppleBaseTotalNets,
       "wfAppleBaseTotalZones": wfAppleBaseTotalZones,
       "wfAppleBaseTotalZoneNames": wfAppleBaseTotalZoneNames,
       "wfAppleBaseTotalAarpEntries": wfAppleBaseTotalAarpEntries,
       "wfAppleBaseEstimatedNets": wfAppleBaseEstimatedNets,
       "wfAppleBaseEstimatedHosts": wfAppleBaseEstimatedHosts,
       "wfAppleMacIPBaseDelete": wfAppleMacIPBaseDelete,
       "wfAppleMacIPBaseDisable": wfAppleMacIPBaseDisable,
       "wfAppleMacIPBaseState": wfAppleMacIPBaseState,
       "wfAppleMacIPZone": wfAppleMacIPZone,
       "wfMacIPAddress1": wfMacIPAddress1,
       "wfMacIPLowerIpAddress1": wfMacIPLowerIpAddress1,
       "wfMacIPUpperIpAddress1": wfMacIPUpperIpAddress1,
       "wfMacIPAddress2": wfMacIPAddress2,
       "wfMacIPLowerIpAddress2": wfMacIPLowerIpAddress2,
       "wfMacIPUpperIpAddress2": wfMacIPUpperIpAddress2,
       "wfMacIPAddress3": wfMacIPAddress3,
       "wfMacIPLowerIpAddress3": wfMacIPLowerIpAddress3,
       "wfMacIPUpperIpAddress3": wfMacIPUpperIpAddress3,
       "wfAppleMacIPAddressTimeOut": wfAppleMacIPAddressTimeOut,
       "wfAppleMacIPServerRequests": wfAppleMacIPServerRequests,
       "wfAppleMacIPServerResponces": wfAppleMacIPServerResponces,
       "wfAppleRtmpTable": wfAppleRtmpTable,
       "wfAppleRtmpEntry": wfAppleRtmpEntry,
       "wfAppleRtmpNetStart": wfAppleRtmpNetStart,
       "wfAppleRtmpNetEnd": wfAppleRtmpNetEnd,
       "wfAppleRtmpPort": wfAppleRtmpPort,
       "wfAppleRtmpHops": wfAppleRtmpHops,
       "wfAppleRtmpNextHopNet": wfAppleRtmpNextHopNet,
       "wfAppleRtmpNextHopNode": wfAppleRtmpNextHopNode,
       "wfAppleRtmpState": wfAppleRtmpState,
       "wfAppleRtmpProto": wfAppleRtmpProto,
       "wfAppleRtmpAurpNextHopIpAddress": wfAppleRtmpAurpNextHopIpAddress,
       "wfApplePortTable": wfApplePortTable,
       "wfApplePortEntry": wfApplePortEntry,
       "wfApplePortDelete": wfApplePortDelete,
       "wfApplePortDisable": wfApplePortDisable,
       "wfApplePortCircuit": wfApplePortCircuit,
       "wfApplePortState": wfApplePortState,
       "wfApplePortType": wfApplePortType,
       "wfApplePortCksumDisable": wfApplePortCksumDisable,
       "wfApplePortTrEndStation": wfApplePortTrEndStation,
       "wfApplePortGniForever": wfApplePortGniForever,
       "wfApplePortAarpFlush": wfApplePortAarpFlush,
       "wfApplePortMacAddress": wfApplePortMacAddress,
       "wfApplePortNodeId": wfApplePortNodeId,
       "wfApplePortNetwork": wfApplePortNetwork,
       "wfApplePortNetStart": wfApplePortNetStart,
       "wfApplePortNetEnd": wfApplePortNetEnd,
       "wfApplePortDfltZone": wfApplePortDfltZone,
       "wfApplePortCurMacAddress": wfApplePortCurMacAddress,
       "wfApplePortCurNodeId": wfApplePortCurNodeId,
       "wfApplePortCurNetwork": wfApplePortCurNetwork,
       "wfApplePortCurNetStart": wfApplePortCurNetStart,
       "wfApplePortCurNetEnd": wfApplePortCurNetEnd,
       "wfApplePortCurDfltZone": wfApplePortCurDfltZone,
       "wfApplePortAarpProbeRxs": wfApplePortAarpProbeRxs,
       "wfApplePortAarpProbeTxs": wfApplePortAarpProbeTxs,
       "wfApplePortAarpReqRxs": wfApplePortAarpReqRxs,
       "wfApplePortAarpReqTxs": wfApplePortAarpReqTxs,
       "wfApplePortAarpRspRxs": wfApplePortAarpRspRxs,
       "wfApplePortAarpRspTxs": wfApplePortAarpRspTxs,
       "wfApplePortDdpOutRequests": wfApplePortDdpOutRequests,
       "wfApplePortDdpInReceives": wfApplePortDdpInReceives,
       "wfApplePortDdpInLocalDatagrams": wfApplePortDdpInLocalDatagrams,
       "wfApplePortDdpNoProtocolHandlers": wfApplePortDdpNoProtocolHandlers,
       "wfApplePortDdpTooShortErrors": wfApplePortDdpTooShortErrors,
       "wfApplePortDdpTooLongErrors": wfApplePortDdpTooLongErrors,
       "wfApplePortDdpChecksumErrors": wfApplePortDdpChecksumErrors,
       "wfApplePortDdpForwRequests": wfApplePortDdpForwRequests,
       "wfApplePortDdpOutNoRoutes": wfApplePortDdpOutNoRoutes,
       "wfApplePortDdpBroadcastErrors": wfApplePortDdpBroadcastErrors,
       "wfApplePortDdpHopCountErrors": wfApplePortDdpHopCountErrors,
       "wfApplePortRtmpInDataPkts": wfApplePortRtmpInDataPkts,
       "wfApplePortRtmpOutDataPkts": wfApplePortRtmpOutDataPkts,
       "wfApplePortRtmpInRequestPkts": wfApplePortRtmpInRequestPkts,
       "wfApplePortRtmpNextIREqualChanges": wfApplePortRtmpNextIREqualChanges,
       "wfApplePortRtmpNextIRLessChanges": wfApplePortRtmpNextIRLessChanges,
       "wfApplePortRtmpRouteDeletes": wfApplePortRtmpRouteDeletes,
       "wfApplePortRtmpNetworkMismatchErrors": wfApplePortRtmpNetworkMismatchErrors,
       "wfApplePortRtmpRoutingTableOverflows": wfApplePortRtmpRoutingTableOverflows,
       "wfApplePortZipInZipQueries": wfApplePortZipInZipQueries,
       "wfApplePortZipInZipReplies": wfApplePortZipInZipReplies,
       "wfApplePortZipOutZipReplies": wfApplePortZipOutZipReplies,
       "wfApplePortZipInZipExtendedReplies": wfApplePortZipInZipExtendedReplies,
       "wfApplePortZipOutZipExtendedReplies": wfApplePortZipOutZipExtendedReplies,
       "wfApplePortZipInGetZoneLists": wfApplePortZipInGetZoneLists,
       "wfApplePortZipOutGetZoneListReplies": wfApplePortZipOutGetZoneListReplies,
       "wfApplePortZipInGetLocalZones": wfApplePortZipInGetLocalZones,
       "wfApplePortZipOutGetLocalZoneReplies": wfApplePortZipOutGetLocalZoneReplies,
       "wfApplePortZipInGetMyZones": wfApplePortZipInGetMyZones,
       "wfApplePortZipOutGetMyZoneReplies": wfApplePortZipOutGetMyZoneReplies,
       "wfApplePortZipZoneConflictErrors": wfApplePortZipZoneConflictErrors,
       "wfApplePortZipInGetNetInfos": wfApplePortZipInGetNetInfos,
       "wfApplePortZipOutGetNetInfoReplies": wfApplePortZipOutGetNetInfoReplies,
       "wfApplePortZipZoneOutInvalids": wfApplePortZipZoneOutInvalids,
       "wfApplePortZipAddressInvalids": wfApplePortZipAddressInvalids,
       "wfApplePortZipOutGetNetInfos": wfApplePortZipOutGetNetInfos,
       "wfApplePortZipInGetNetInfoReplies": wfApplePortZipInGetNetInfoReplies,
       "wfApplePortZipOutZipQueries": wfApplePortZipOutZipQueries,
       "wfApplePortZipInErrors": wfApplePortZipInErrors,
       "wfApplePortNbpInLookUpRequests": wfApplePortNbpInLookUpRequests,
       "wfApplePortNbpInLookUpReplies": wfApplePortNbpInLookUpReplies,
       "wfApplePortNbpInBroadcastRequests": wfApplePortNbpInBroadcastRequests,
       "wfApplePortNbpInForwardRequests": wfApplePortNbpInForwardRequests,
       "wfApplePortNbpOutLookUpRequests": wfApplePortNbpOutLookUpRequests,
       "wfApplePortNbpOutLookUpReplies": wfApplePortNbpOutLookUpReplies,
       "wfApplePortNbpOutBroadcastRequests": wfApplePortNbpOutBroadcastRequests,
       "wfApplePortNbpOutForwardRequests": wfApplePortNbpOutForwardRequests,
       "wfApplePortNbpRegistrationFailures": wfApplePortNbpRegistrationFailures,
       "wfApplePortNbpInErrors": wfApplePortNbpInErrors,
       "wfApplePortEchoRequests": wfApplePortEchoRequests,
       "wfApplePortEchoReplies": wfApplePortEchoReplies,
       "wfApplePortInterfaceCost": wfApplePortInterfaceCost,
       "wfApplePortWanBroadcastAddress": wfApplePortWanBroadcastAddress,
       "wfApplePortWanSplitHorizonDisable": wfApplePortWanSplitHorizonDisable,
       "wfApplePortZoneFilterType": wfApplePortZoneFilterType,
       "wfApplePortMacIPDisable": wfApplePortMacIPDisable,
       "wfAppleLclZoneTable": wfAppleLclZoneTable,
       "wfAppleLclZoneEntry": wfAppleLclZoneEntry,
       "wfAppleLclZoneDelete": wfAppleLclZoneDelete,
       "wfAppleLclZonePortCircuit": wfAppleLclZonePortCircuit,
       "wfAppleLclZoneIndex": wfAppleLclZoneIndex,
       "wfAppleLclZoneName": wfAppleLclZoneName,
       "wfAppleAarpTable": wfAppleAarpTable,
       "wfAppleAarpEntry": wfAppleAarpEntry,
       "wfAppleAarpIfIndex": wfAppleAarpIfIndex,
       "wfAppleAarpNet": wfAppleAarpNet,
       "wfAppleAarpNode": wfAppleAarpNode,
       "wfAppleAarpPhysAddress": wfAppleAarpPhysAddress,
       "wfAppleZipTable": wfAppleZipTable,
       "wfAppleZipEntry": wfAppleZipEntry,
       "wfAppleZipZoneNetStart": wfAppleZipZoneNetStart,
       "wfAppleZipZoneNetEnd": wfAppleZipZoneNetEnd,
       "wfAppleZipIndex": wfAppleZipIndex,
       "wfAppleZipZoneName": wfAppleZipZoneName,
       "wfAppleZipZoneState": wfAppleZipZoneState,
       "wfAppleZoneFilterTable": wfAppleZoneFilterTable,
       "wfAppleZoneFilterEntry": wfAppleZoneFilterEntry,
       "wfAppleZoneFilterDelete": wfAppleZoneFilterDelete,
       "wfAppleZoneFilterCircuit": wfAppleZoneFilterCircuit,
       "wfAppleZoneFilterIpAddress": wfAppleZoneFilterIpAddress,
       "wfAppleZoneFilterCircuitType": wfAppleZoneFilterCircuitType,
       "wfAppleZoneFilterIndex": wfAppleZoneFilterIndex,
       "wfAppleZoneFilterName": wfAppleZoneFilterName,
       "wfAppleAurpBase": wfAppleAurpBase,
       "wfAppleAurpBaseDelete": wfAppleAurpBaseDelete,
       "wfAppleAurpBaseDisable": wfAppleAurpBaseDisable,
       "wfAppleAurpBaseState": wfAppleAurpBaseState,
       "wfAppleAurpBaseDomain": wfAppleAurpBaseDomain,
       "wfAppleAurpBaseIpAddress": wfAppleAurpBaseIpAddress,
       "wfAppleAurpBasePromiscuous": wfAppleAurpBasePromiscuous,
       "wfAppleAurpBaseInAcceptedOpenReqs": wfAppleAurpBaseInAcceptedOpenReqs,
       "wfAppleAurpBaseInRejectedOpenReqs": wfAppleAurpBaseInRejectedOpenReqs,
       "wfAppleAurpBaseInRouterDowns": wfAppleAurpBaseInRouterDowns,
       "wfAppleAurpBaseInPktsNoPeers": wfAppleAurpBaseInPktsNoPeers,
       "wfAppleAurpBaseInInvalidVerions": wfAppleAurpBaseInInvalidVerions,
       "wfAppleAurpTable": wfAppleAurpTable,
       "wfAppleAurpEntry": wfAppleAurpEntry,
       "wfAppleAurpEntryDelete": wfAppleAurpEntryDelete,
       "wfAppleAurpEntryDisable": wfAppleAurpEntryDisable,
       "wfAppleAurpEntryState": wfAppleAurpEntryState,
       "wfAppleAurpEntryIpAddress": wfAppleAurpEntryIpAddress,
       "wfAppleAurpEntryZoneFilterType": wfAppleAurpEntryZoneFilterType,
       "wfAppleAurpEntryTimeoutCommand": wfAppleAurpEntryTimeoutCommand,
       "wfAppleAurpEntryRetryCommand": wfAppleAurpEntryRetryCommand,
       "wfAppleAurpEntryUpdateRate": wfAppleAurpEntryUpdateRate,
       "wfAppleAurpEntryLhfTimeout": wfAppleAurpEntryLhfTimeout,
       "wfAppleAurpEntryHopCountReduction": wfAppleAurpEntryHopCountReduction,
       "wfAppleAurpEntryInterfaceCost": wfAppleAurpEntryInterfaceCost,
       "wfAppleAurpEntrySuiFlags": wfAppleAurpEntrySuiFlags,
       "wfAppleAurpEntryType": wfAppleAurpEntryType,
       "wfAppleAurpEntryPeerDomainId": wfAppleAurpEntryPeerDomainId,
       "wfAppleAurpEntryPeerUpdateRate": wfAppleAurpEntryPeerUpdateRate,
       "wfAppleAurpEntryPeerEnvironment": wfAppleAurpEntryPeerEnvironment,
       "wfAppleAurpEntryPeerSuiFlags": wfAppleAurpEntryPeerSuiFlags,
       "wfAppleAurpEntryCliConnId": wfAppleAurpEntryCliConnId,
       "wfAppleAurpEntrySrvConnId": wfAppleAurpEntrySrvConnId,
       "wfAppleAurpEntryCliSeqNum": wfAppleAurpEntryCliSeqNum,
       "wfAppleAurpEntrySrvSeqNum": wfAppleAurpEntrySrvSeqNum,
       "wfAppleAurpEntryCommandRetries": wfAppleAurpEntryCommandRetries,
       "wfAppleAurpEntryInDelayedDuplicates": wfAppleAurpEntryInDelayedDuplicates,
       "wfAppleAurpEntryInInvalidConnIds": wfAppleAurpEntryInInvalidConnIds,
       "wfAppleAurpEntryInInvalidCommands": wfAppleAurpEntryInInvalidCommands,
       "wfAppleAurpEntryInInvalidSubCodes": wfAppleAurpEntryInInvalidSubCodes,
       "wfAppleAurpEntryInPkts": wfAppleAurpEntryInPkts,
       "wfAppleAurpEntryOutPkts": wfAppleAurpEntryOutPkts,
       "wfAppleAurpEntryInDdpPkts": wfAppleAurpEntryInDdpPkts,
       "wfAppleAurpEntryOutDdpPkts": wfAppleAurpEntryOutDdpPkts,
       "wfAppleAurpEntryOutNoRoutes": wfAppleAurpEntryOutNoRoutes,
       "wfAppleAurpEntryHopCountErrors": wfAppleAurpEntryHopCountErrors,
       "wfAppleAurpEntryHopCountAdjustments": wfAppleAurpEntryHopCountAdjustments,
       "wfAppleAurpEntryInAurpPkts": wfAppleAurpEntryInAurpPkts,
       "wfAppleAurpEntryOutAurpPkts": wfAppleAurpEntryOutAurpPkts,
       "wfAppleAurpEntryInOpenRequests": wfAppleAurpEntryInOpenRequests,
       "wfAppleAurpEntryOutOpenRequests": wfAppleAurpEntryOutOpenRequests,
       "wfAppleAurpEntryInOpenResponses": wfAppleAurpEntryInOpenResponses,
       "wfAppleAurpEntryOutOpenResponses": wfAppleAurpEntryOutOpenResponses,
       "wfAppleAurpEntryInRiRequests": wfAppleAurpEntryInRiRequests,
       "wfAppleAurpEntryOutRiRequests": wfAppleAurpEntryOutRiRequests,
       "wfAppleAurpEntryInRiResponses": wfAppleAurpEntryInRiResponses,
       "wfAppleAurpEntryOutRiResponses": wfAppleAurpEntryOutRiResponses,
       "wfAppleAurpEntryInRiAcks": wfAppleAurpEntryInRiAcks,
       "wfAppleAurpEntryOutRiAcks": wfAppleAurpEntryOutRiAcks,
       "wfAppleAurpEntryInRiUpdates": wfAppleAurpEntryInRiUpdates,
       "wfAppleAurpEntryOutRiUpdates": wfAppleAurpEntryOutRiUpdates,
       "wfAppleAurpEntryInUpdateNullEvents": wfAppleAurpEntryInUpdateNullEvents,
       "wfAppleAurpEntryOutUpdateNullEvents": wfAppleAurpEntryOutUpdateNullEvents,
       "wfAppleAurpEntryInUpdateNetAdds": wfAppleAurpEntryInUpdateNetAdds,
       "wfAppleAurpEntryOutUpdateNetAdds": wfAppleAurpEntryOutUpdateNetAdds,
       "wfAppleAurpEntryInUpdateNetDeletes": wfAppleAurpEntryInUpdateNetDeletes,
       "wfAppleAurpEntryOutUpdateNetDeletes": wfAppleAurpEntryOutUpdateNetDeletes,
       "wfAppleAurpEntryInUpdateNetRouteChanges": wfAppleAurpEntryInUpdateNetRouteChanges,
       "wfAppleAurpEntryOutUpdateNetRouteChanges": wfAppleAurpEntryOutUpdateNetRouteChanges,
       "wfAppleAurpEntryInUpdateNetDistanceChanges": wfAppleAurpEntryInUpdateNetDistanceChanges,
       "wfAppleAurpEntryOutUpdateNetDistanceChanges": wfAppleAurpEntryOutUpdateNetDistanceChanges,
       "wfAppleAurpEntryInUpdateZoneChanges": wfAppleAurpEntryInUpdateZoneChanges,
       "wfAppleAurpEntryOutUpdateZoneChanges": wfAppleAurpEntryOutUpdateZoneChanges,
       "wfAppleAurpEntryInUpdateInvalidEvents": wfAppleAurpEntryInUpdateInvalidEvents,
       "wfAppleAurpEntryOutUpdateInvalidEvents": wfAppleAurpEntryOutUpdateInvalidEvents,
       "wfAppleAurpEntryInZiRequests": wfAppleAurpEntryInZiRequests,
       "wfAppleAurpEntryOutZiRequests": wfAppleAurpEntryOutZiRequests,
       "wfAppleAurpEntryInZiResponses": wfAppleAurpEntryInZiResponses,
       "wfAppleAurpEntryOutZiResponses": wfAppleAurpEntryOutZiResponses,
       "wfAppleAurpEntryInGdzlRequests": wfAppleAurpEntryInGdzlRequests,
       "wfAppleAurpEntryOutGdzlRequests": wfAppleAurpEntryOutGdzlRequests,
       "wfAppleAurpEntryInGdzlResponses": wfAppleAurpEntryInGdzlResponses,
       "wfAppleAurpEntryOutGdzlResponses": wfAppleAurpEntryOutGdzlResponses,
       "wfAppleAurpEntryInGznRequests": wfAppleAurpEntryInGznRequests,
       "wfAppleAurpEntryOutGznRequests": wfAppleAurpEntryOutGznRequests,
       "wfAppleAurpEntryInGznResponses": wfAppleAurpEntryInGznResponses,
       "wfAppleAurpEntryOutGznResponses": wfAppleAurpEntryOutGznResponses,
       "wfAppleAurpEntryInTickles": wfAppleAurpEntryInTickles,
       "wfAppleAurpEntryOutTickles": wfAppleAurpEntryOutTickles,
       "wfAppleAurpEntryInTickleAcks": wfAppleAurpEntryInTickleAcks,
       "wfAppleAurpEntryOutTickleAcks": wfAppleAurpEntryOutTickleAcks,
       "wfAppleAurpEntryInRouterDowns": wfAppleAurpEntryInRouterDowns,
       "wfAppleAurpEntryOutRouterDowns": wfAppleAurpEntryOutRouterDowns,
       "wfAppleAurpEntryZoneFiltDfltZone": wfAppleAurpEntryZoneFiltDfltZone,
       "wfAppleAggrStats": wfAppleAggrStats,
       "wfAppleAggrInPkts": wfAppleAggrInPkts,
       "wfAppleAggrOutPkts": wfAppleAggrOutPkts,
       "wfAppleAggrFwdDatagrams": wfAppleAggrFwdDatagrams,
       "wfAppleAggrInXsumErrs": wfAppleAggrInXsumErrs,
       "wfAppleAggrInHopCountErrs": wfAppleAggrInHopCountErrs,
       "wfAppleAggrInTooShorts": wfAppleAggrInTooShorts,
       "wfAppleAggrInTooLongs": wfAppleAggrInTooLongs,
       "wfAppleAggrOutNoRoutes": wfAppleAggrOutNoRoutes,
       "wfAppleAggrInLocalDests": wfAppleAggrInLocalDests,
       "wfAppleAggrInRtmps": wfAppleAggrInRtmps,
       "wfAppleAggrOutRtmps": wfAppleAggrOutRtmps}
)
