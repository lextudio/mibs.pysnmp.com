# SNMP MIB module (IBM6611-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM6611-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:47 2024
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm6611_ObjectIdentity = ObjectIdentity
ibm6611 = _Ibm6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2)
)
_IbmSubagents_ObjectIdentity = ObjectIdentity
ibmSubagents = _IbmSubagents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 1)
)
_IbmChipSets_ObjectIdentity = ObjectIdentity
ibmChipSets = _IbmChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2)
)
_IbmChipSetIntel_ObjectIdentity = ObjectIdentity
ibmChipSetIntel = _IbmChipSetIntel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2, 1)
)
_IbmChipSetIntel82596B_ObjectIdentity = ObjectIdentity
ibmChipSetIntel82596B = _IbmChipSetIntel82596B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2, 1, 1)
)
_IbmChipSetIBM_ObjectIdentity = ObjectIdentity
ibmChipSetIBM = _IbmChipSetIBM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2, 2)
)
_IbmChipSetIBM8025A_ObjectIdentity = ObjectIdentity
ibmChipSetIBM8025A = _IbmChipSetIBM8025A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2, 2, 1)
)
_IbmChipSetIBM8025B_ObjectIdentity = ObjectIdentity
ibmChipSetIBM8025B = _IbmChipSetIBM8025B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2, 2, 2)
)
_IbmChipSetSignetics_ObjectIdentity = ObjectIdentity
ibmChipSetSignetics = _IbmChipSetSignetics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2, 3)
)
_IbmChipSetSigneticsSCN68562_ObjectIdentity = ObjectIdentity
ibmChipSetSigneticsSCN68562 = _IbmChipSetSigneticsSCN68562_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 2, 3, 1)
)
_IbmDSUs_ObjectIdentity = ObjectIdentity
ibmDSUs = _IbmDSUs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3)
)
_Cylink_ObjectIdentity = ObjectIdentity
cylink = _Cylink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1)
)
_CylinkStatusTable_Object = MibTable
cylinkStatusTable = _CylinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cylinkStatusTable.setStatus("mandatory")
_CylinkStatusEntry_Object = MibTableRow
cylinkStatusEntry = _CylinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 1, 1)
)
cylinkStatusEntry.setIndexNames(
    (0, "IBM6611-MIB", "cylinkIndex"),
)
if mibBuilder.loadTexts:
    cylinkStatusEntry.setStatus("mandatory")
_CylinkIndex_Type = Integer32
_CylinkIndex_Object = MibTableColumn
cylinkIndex = _CylinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 1, 1, 1),
    _CylinkIndex_Type()
)
cylinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkIndex.setStatus("mandatory")


class _CylinkLinkState_Type(Integer32):
    """Custom type cylinkLinkState based on Integer32"""
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
        *(("cylinkConnected", 4),
          ("cylinkNoInput", 2),
          ("cylinkNoOutput", 3),
          ("cylinkNotConnected", 1))
    )


_CylinkLinkState_Type.__name__ = "Integer32"
_CylinkLinkState_Object = MibTableColumn
cylinkLinkState = _CylinkLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 1, 1, 2),
    _CylinkLinkState_Type()
)
cylinkLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkLinkState.setStatus("mandatory")


class _CylinkLoopback_Type(Integer32):
    """Custom type cylinkLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cylinkFarEndLoopback", 3),
          ("cylinkNearEndLoopback", 2),
          ("cylinkNoLoopback", 1))
    )


_CylinkLoopback_Type.__name__ = "Integer32"
_CylinkLoopback_Object = MibTableColumn
cylinkLoopback = _CylinkLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 1, 1, 3),
    _CylinkLoopback_Type()
)
cylinkLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkLoopback.setStatus("mandatory")


class _CylinkQRSS_Type(Integer32):
    """Custom type cylinkQRSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cylinkNoQRSS", 1),
          ("cylinkQRSSMaster", 2),
          ("cylinkQRSSSlave", 3))
    )


_CylinkQRSS_Type.__name__ = "Integer32"
_CylinkQRSS_Object = MibTableColumn
cylinkQRSS = _CylinkQRSS_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 1, 1, 4),
    _CylinkQRSS_Type()
)
cylinkQRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkQRSS.setStatus("mandatory")
_CylinkConfigTable_Object = MibTable
cylinkConfigTable = _CylinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cylinkConfigTable.setStatus("mandatory")
_CylinkConfigEntry_Object = MibTableRow
cylinkConfigEntry = _CylinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1)
)
cylinkConfigEntry.setIndexNames(
    (0, "IBM6611-MIB", "cylinkConfigIndex"),
)
if mibBuilder.loadTexts:
    cylinkConfigEntry.setStatus("mandatory")
_CylinkConfigIndex_Type = Integer32
_CylinkConfigIndex_Object = MibTableColumn
cylinkConfigIndex = _CylinkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 1),
    _CylinkConfigIndex_Type()
)
cylinkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkConfigIndex.setStatus("mandatory")
_CylinkSerialNumber_Type = Integer32
_CylinkSerialNumber_Object = MibTableColumn
cylinkSerialNumber = _CylinkSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 2),
    _CylinkSerialNumber_Type()
)
cylinkSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkSerialNumber.setStatus("mandatory")


class _CylinkSoftwareVersion_Type(DisplayString):
    """Custom type cylinkSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CylinkSoftwareVersion_Type.__name__ = "DisplayString"
_CylinkSoftwareVersion_Object = MibTableColumn
cylinkSoftwareVersion = _CylinkSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 3),
    _CylinkSoftwareVersion_Type()
)
cylinkSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkSoftwareVersion.setStatus("mandatory")


class _CylinkDTEFraming_Type(Integer32):
    """Custom type cylinkDTEFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkDTEFramingD4", 1),
          ("cylinkDTEFramingESF", 2))
    )


_CylinkDTEFraming_Type.__name__ = "Integer32"
_CylinkDTEFraming_Object = MibTableColumn
cylinkDTEFraming = _CylinkDTEFraming_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 4),
    _CylinkDTEFraming_Type()
)
cylinkDTEFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkDTEFraming.setStatus("mandatory")


class _CylinkNetworkFraming_Type(Integer32):
    """Custom type cylinkNetworkFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkNetworkFramingD4", 1),
          ("cylinkNetworkFramingESF", 2))
    )


_CylinkNetworkFraming_Type.__name__ = "Integer32"
_CylinkNetworkFraming_Object = MibTableColumn
cylinkNetworkFraming = _CylinkNetworkFraming_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 5),
    _CylinkNetworkFraming_Type()
)
cylinkNetworkFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkNetworkFraming.setStatus("mandatory")


class _CylinkDTEDS1Mode_Type(Integer32):
    """Custom type cylinkDTEDS1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkDTEDS1ModeAMI", 2),
          ("cylinkDTEDS1ModeB8ZS", 1))
    )


_CylinkDTEDS1Mode_Type.__name__ = "Integer32"
_CylinkDTEDS1Mode_Object = MibTableColumn
cylinkDTEDS1Mode = _CylinkDTEDS1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 6),
    _CylinkDTEDS1Mode_Type()
)
cylinkDTEDS1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkDTEDS1Mode.setStatus("mandatory")


class _CylinkNetworkDS1Mode_Type(Integer32):
    """Custom type cylinkNetworkDS1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkNetworkDS1ModeAMI", 2),
          ("cylinkNetworkDS1ModeB8ZS", 1))
    )


_CylinkNetworkDS1Mode_Type.__name__ = "Integer32"
_CylinkNetworkDS1Mode_Object = MibTableColumn
cylinkNetworkDS1Mode = _CylinkNetworkDS1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 7),
    _CylinkNetworkDS1Mode_Type()
)
cylinkNetworkDS1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkNetworkDS1Mode.setStatus("mandatory")


class _CylinkOnesResponsibility_Type(Integer32):
    """Custom type cylinkOnesResponsibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkOnesResponsibilityACSU", 2),
          ("cylinkOnesResponsibilityDTE", 1))
    )


_CylinkOnesResponsibility_Type.__name__ = "Integer32"
_CylinkOnesResponsibility_Object = MibTableColumn
cylinkOnesResponsibility = _CylinkOnesResponsibility_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 8),
    _CylinkOnesResponsibility_Type()
)
cylinkOnesResponsibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkOnesResponsibility.setStatus("mandatory")


class _CylinkOnesControl_Type(Integer32):
    """Custom type cylinkOnesControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cylinkOnesControlD4FRM", 2),
          ("cylinkOnesControlESFDL", 3),
          ("cylinkOnesControlLSB24", 1))
    )


_CylinkOnesControl_Type.__name__ = "Integer32"
_CylinkOnesControl_Object = MibTableColumn
cylinkOnesControl = _CylinkOnesControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 9),
    _CylinkOnesControl_Type()
)
cylinkOnesControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkOnesControl.setStatus("mandatory")


class _CylinkZeroProtection_Type(Integer32):
    """Custom type cylinkZeroProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkZeroProtection15", 2),
          ("cylinkZeroProtection80", 1))
    )


_CylinkZeroProtection_Type.__name__ = "Integer32"
_CylinkZeroProtection_Object = MibTableColumn
cylinkZeroProtection = _CylinkZeroProtection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 10),
    _CylinkZeroProtection_Type()
)
cylinkZeroProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkZeroProtection.setStatus("mandatory")


class _CylinkClockSource_Type(Integer32):
    """Custom type cylinkClockSource based on Integer32"""
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
        *(("cylinkClockSourceDTE", 2),
          ("cylinkClockSourceExternal", 3),
          ("cylinkClockSourceInternal", 4),
          ("cylinkClockSourceNetwork", 1))
    )


_CylinkClockSource_Type.__name__ = "Integer32"
_CylinkClockSource_Object = MibTableColumn
cylinkClockSource = _CylinkClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 11),
    _CylinkClockSource_Type()
)
cylinkClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkClockSource.setStatus("mandatory")


class _CylinkClockFrequency_Type(Integer32):
    """Custom type cylinkClockFrequency based on Integer32"""
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
        *(("cylinkClockFreq-1-344MHz", 3),
          ("cylinkClockFreq-1-544MHz", 4),
          ("cylinkClockFreq-256kHz", 2),
          ("cylinkClockFreq-56kHz", 1))
    )


_CylinkClockFrequency_Type.__name__ = "Integer32"
_CylinkClockFrequency_Object = MibTableColumn
cylinkClockFrequency = _CylinkClockFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 12),
    _CylinkClockFrequency_Type()
)
cylinkClockFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkClockFrequency.setStatus("mandatory")


class _CylinkClockBackup_Type(Integer32):
    """Custom type cylinkClockBackup based on Integer32"""
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
        *(("cylinkClockBackupDTE", 2),
          ("cylinkClockBackupExternal", 3),
          ("cylinkClockBackupInternal", 4),
          ("cylinkClockBackupNetwork", 1))
    )


_CylinkClockBackup_Type.__name__ = "Integer32"
_CylinkClockBackup_Object = MibTableColumn
cylinkClockBackup = _CylinkClockBackup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 13),
    _CylinkClockBackup_Type()
)
cylinkClockBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkClockBackup.setStatus("mandatory")


class _CylinkDIUFrequency_Type(Integer32):
    """Custom type cylinkDIUFrequency based on Integer32"""
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
        *(("cylinkDIUFreq-1-344Mbps", 2),
          ("cylinkDIUFreq-1-528Mbps", 3),
          ("cylinkDIUFreq-1-536Mbps", 4),
          ("cylinkDIUFreq-768kbps", 1))
    )


_CylinkDIUFrequency_Type.__name__ = "Integer32"
_CylinkDIUFrequency_Object = MibTableColumn
cylinkDIUFrequency = _CylinkDIUFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 14),
    _CylinkDIUFrequency_Type()
)
cylinkDIUFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkDIUFrequency.setStatus("mandatory")


class _CylinkDIUTiming_Type(Integer32):
    """Custom type cylinkDIUTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkDIUTimingST", 2),
          ("cylinkDIUTimingTT", 1))
    )


_CylinkDIUTiming_Type.__name__ = "Integer32"
_CylinkDIUTiming_Object = MibTableColumn
cylinkDIUTiming = _CylinkDIUTiming_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 15),
    _CylinkDIUTiming_Type()
)
cylinkDIUTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkDIUTiming.setStatus("mandatory")


class _CylinkDialoutCapability_Type(Integer32):
    """Custom type cylinkDialoutCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cylinkDialoutCapabilityPolled", 1),
          ("cylinkDialoutCapabilityPulse", 3),
          ("cylinkDialoutCapabilityTone", 2))
    )


_CylinkDialoutCapability_Type.__name__ = "Integer32"
_CylinkDialoutCapability_Object = MibTableColumn
cylinkDialoutCapability = _CylinkDialoutCapability_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 16),
    _CylinkDialoutCapability_Type()
)
cylinkDialoutCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkDialoutCapability.setStatus("mandatory")


class _CylinkDialoutHoldoff_Type(Integer32):
    """Custom type cylinkDialoutHoldoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CylinkDialoutHoldoff_Type.__name__ = "Integer32"
_CylinkDialoutHoldoff_Object = MibTableColumn
cylinkDialoutHoldoff = _CylinkDialoutHoldoff_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 17),
    _CylinkDialoutHoldoff_Type()
)
cylinkDialoutHoldoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkDialoutHoldoff.setStatus("mandatory")


class _CylinkPrimaryPhone_Type(DisplayString):
    """Custom type cylinkPrimaryPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_CylinkPrimaryPhone_Type.__name__ = "DisplayString"
_CylinkPrimaryPhone_Object = MibTableColumn
cylinkPrimaryPhone = _CylinkPrimaryPhone_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 18),
    _CylinkPrimaryPhone_Type()
)
cylinkPrimaryPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkPrimaryPhone.setStatus("mandatory")


class _CylinkSecondaryPhone_Type(DisplayString):
    """Custom type cylinkSecondaryPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_CylinkSecondaryPhone_Type.__name__ = "DisplayString"
_CylinkSecondaryPhone_Object = MibTableColumn
cylinkSecondaryPhone = _CylinkSecondaryPhone_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 19),
    _CylinkSecondaryPhone_Type()
)
cylinkSecondaryPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkSecondaryPhone.setStatus("mandatory")


class _CylinkAlarmRepeatTime_Type(Integer32):
    """Custom type cylinkAlarmRepeatTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CylinkAlarmRepeatTime_Type.__name__ = "Integer32"
_CylinkAlarmRepeatTime_Object = MibTableColumn
cylinkAlarmRepeatTime = _CylinkAlarmRepeatTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 20),
    _CylinkAlarmRepeatTime_Type()
)
cylinkAlarmRepeatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkAlarmRepeatTime.setStatus("mandatory")


class _CylinkESThreshold_Type(Integer32):
    """Custom type cylinkESThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CylinkESThreshold_Type.__name__ = "Integer32"
_CylinkESThreshold_Object = MibTableColumn
cylinkESThreshold = _CylinkESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 21),
    _CylinkESThreshold_Type()
)
cylinkESThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkESThreshold.setStatus("mandatory")


class _CylinkSecondaryContact_Type(Integer32):
    """Custom type cylinkSecondaryContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cylinkSecondaryContactClosed", 2),
          ("cylinkSecondaryContactOpen", 1))
    )


_CylinkSecondaryContact_Type.__name__ = "Integer32"
_CylinkSecondaryContact_Object = MibTableColumn
cylinkSecondaryContact = _CylinkSecondaryContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 3, 1, 3, 1, 22),
    _CylinkSecondaryContact_Type()
)
cylinkSecondaryContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cylinkSecondaryContact.setStatus("mandatory")
_Ibmsystem_ObjectIdentity = ObjectIdentity
ibmsystem = _Ibmsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4)
)
_IbmMainProcessorLoadTable_Object = MibTable
ibmMainProcessorLoadTable = _IbmMainProcessorLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ibmMainProcessorLoadTable.setStatus("mandatory")
_IbmMainProcessorLoadEntry_Object = MibTableRow
ibmMainProcessorLoadEntry = _IbmMainProcessorLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1)
)
ibmMainProcessorLoadEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmMainProcessorLoadIndex"),
)
if mibBuilder.loadTexts:
    ibmMainProcessorLoadEntry.setStatus("mandatory")


class _IbmMainProcessorLoadIndex_Type(Integer32):
    """Custom type ibmMainProcessorLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IbmMainProcessorLoadIndex_Type.__name__ = "Integer32"
_IbmMainProcessorLoadIndex_Object = MibTableColumn
ibmMainProcessorLoadIndex = _IbmMainProcessorLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1, 1),
    _IbmMainProcessorLoadIndex_Type()
)
ibmMainProcessorLoadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMainProcessorLoadIndex.setStatus("mandatory")
_IbmMainProcessorLoad_Type = Gauge32
_IbmMainProcessorLoad_Object = MibTableColumn
ibmMainProcessorLoad = _IbmMainProcessorLoad_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1, 2),
    _IbmMainProcessorLoad_Type()
)
ibmMainProcessorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMainProcessorLoad.setStatus("mandatory")
_Ibmswvpd_ObjectIdentity = ObjectIdentity
ibmswvpd = _Ibmswvpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2)
)
_SwVpdTable_Object = MibTable
swVpdTable = _SwVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    swVpdTable.setStatus("mandatory")
_SwVpdEntry_Object = MibTableRow
swVpdEntry = _SwVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1)
)
swVpdEntry.setIndexNames(
    (0, "IBM6611-MIB", "swvpdIndex"),
)
if mibBuilder.loadTexts:
    swVpdEntry.setStatus("mandatory")
_SwvpdIndex_Type = Integer32
_SwvpdIndex_Object = MibTableColumn
swvpdIndex = _SwvpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 1),
    _SwvpdIndex_Type()
)
swvpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdIndex.setStatus("mandatory")
_SwvpdName_Type = DisplayString
_SwvpdName_Object = MibTableColumn
swvpdName = _SwvpdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 2),
    _SwvpdName_Type()
)
swvpdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdName.setStatus("mandatory")
_SwvpdPtfName_Type = DisplayString
_SwvpdPtfName_Object = MibTableColumn
swvpdPtfName = _SwvpdPtfName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 3),
    _SwvpdPtfName_Type()
)
swvpdPtfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdPtfName.setStatus("mandatory")
_SwvpdVerId_Type = Integer32
_SwvpdVerId_Object = MibTableColumn
swvpdVerId = _SwvpdVerId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 4),
    _SwvpdVerId_Type()
)
swvpdVerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdVerId.setStatus("mandatory")
_SwvpdRelId_Type = Integer32
_SwvpdRelId_Object = MibTableColumn
swvpdRelId = _SwvpdRelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 5),
    _SwvpdRelId_Type()
)
swvpdRelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdRelId.setStatus("mandatory")
_SwvpdModId_Type = Integer32
_SwvpdModId_Object = MibTableColumn
swvpdModId = _SwvpdModId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 6),
    _SwvpdModId_Type()
)
swvpdModId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdModId.setStatus("mandatory")
_SwvpdFixId_Type = Integer32
_SwvpdFixId_Object = MibTableColumn
swvpdFixId = _SwvpdFixId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 7),
    _SwvpdFixId_Type()
)
swvpdFixId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdFixId.setStatus("mandatory")


class _SwvpdState_Type(Integer32):
    """Custom type swvpdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broken", 3),
          ("cancelled", 4),
          ("complete", 1),
          ("pending", 2),
          ("unknown", 5))
    )


_SwvpdState_Type.__name__ = "Integer32"
_SwvpdState_Object = MibTableColumn
swvpdState = _SwvpdState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 8),
    _SwvpdState_Type()
)
swvpdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdState.setStatus("mandatory")


class _SwvpdAction_Type(Integer32):
    """Custom type swvpdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("cleanup", 5),
          ("commit", 2),
          ("decommit", 4),
          ("reject", 3),
          ("unknown", 6))
    )


_SwvpdAction_Type.__name__ = "Integer32"
_SwvpdAction_Object = MibTableColumn
swvpdAction = _SwvpdAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 9),
    _SwvpdAction_Type()
)
swvpdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdAction.setStatus("mandatory")


class _SwvpdPath_Type(Integer32):
    """Custom type swvpdPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("root", 1),
          ("share", 3),
          ("usr", 2))
    )


_SwvpdPath_Type.__name__ = "Integer32"
_SwvpdPath_Object = MibTableColumn
swvpdPath = _SwvpdPath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 10),
    _SwvpdPath_Type()
)
swvpdPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdPath.setStatus("mandatory")
_SwvpdDateTime_Type = DisplayString
_SwvpdDateTime_Object = MibTableColumn
swvpdDateTime = _SwvpdDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 2, 1, 1, 11),
    _SwvpdDateTime_Type()
)
swvpdDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swvpdDateTime.setStatus("mandatory")
_Ibmmaint_ObjectIdentity = ObjectIdentity
ibmmaint = _Ibmmaint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4)
)


class _IbmmaintShutdown_Type(Integer32):
    """Custom type ibmmaintShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("shutdown-ipl-local", 4),
          ("shutdown-noipl", 2))
    )


_IbmmaintShutdown_Type.__name__ = "Integer32"
_IbmmaintShutdown_Object = MibScalar
ibmmaintShutdown = _IbmmaintShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 1),
    _IbmmaintShutdown_Type()
)
ibmmaintShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmmaintShutdown.setStatus("mandatory")
_IbmsysInfo_ObjectIdentity = ObjectIdentity
ibmsysInfo = _IbmsysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7)
)
_IbmsysMBUFs_ObjectIdentity = ObjectIdentity
ibmsysMBUFs = _IbmsysMBUFs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 1)
)
_IbmsysMBUFsInUses_Type = Gauge32
_IbmsysMBUFsInUses_Object = MibScalar
ibmsysMBUFsInUses = _IbmsysMBUFsInUses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 1, 1),
    _IbmsysMBUFsInUses_Type()
)
ibmsysMBUFsInUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysMBUFsInUses.setStatus("mandatory")
_IbmsysMBUFsKbytes_Type = Gauge32
_IbmsysMBUFsKbytes_Object = MibScalar
ibmsysMBUFsKbytes = _IbmsysMBUFsKbytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 1, 2),
    _IbmsysMBUFsKbytes_Type()
)
ibmsysMBUFsKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysMBUFsKbytes.setStatus("mandatory")
_IbmsysMBUFsPercents_Type = Gauge32
_IbmsysMBUFsPercents_Object = MibScalar
ibmsysMBUFsPercents = _IbmsysMBUFsPercents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 1, 3),
    _IbmsysMBUFsPercents_Type()
)
ibmsysMBUFsPercents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysMBUFsPercents.setStatus("mandatory")
_IbmsysMBUFsDeniedRequests_Type = Counter32
_IbmsysMBUFsDeniedRequests_Object = MibScalar
ibmsysMBUFsDeniedRequests = _IbmsysMBUFsDeniedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 1, 4),
    _IbmsysMBUFsDeniedRequests_Type()
)
ibmsysMBUFsDeniedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysMBUFsDeniedRequests.setStatus("mandatory")
_IbmsysMBUFsDelayedRequests_Type = Counter32
_IbmsysMBUFsDelayedRequests_Object = MibScalar
ibmsysMBUFsDelayedRequests = _IbmsysMBUFsDelayedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 1, 5),
    _IbmsysMBUFsDelayedRequests_Type()
)
ibmsysMBUFsDelayedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysMBUFsDelayedRequests.setStatus("mandatory")
_IbmsysPageSpace_ObjectIdentity = ObjectIdentity
ibmsysPageSpace = _IbmsysPageSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 2)
)
_IbmsysPageSpaceTotal_Type = Integer32
_IbmsysPageSpaceTotal_Object = MibScalar
ibmsysPageSpaceTotal = _IbmsysPageSpaceTotal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 2, 1),
    _IbmsysPageSpaceTotal_Type()
)
ibmsysPageSpaceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysPageSpaceTotal.setStatus("mandatory")
_IbmsysPageSpaceInUse_Type = Gauge32
_IbmsysPageSpaceInUse_Object = MibScalar
ibmsysPageSpaceInUse = _IbmsysPageSpaceInUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 2, 2),
    _IbmsysPageSpaceInUse_Type()
)
ibmsysPageSpaceInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysPageSpaceInUse.setStatus("mandatory")
_IbmsysRealMem_ObjectIdentity = ObjectIdentity
ibmsysRealMem = _IbmsysRealMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 3)
)
_IbmsysRealMemSize_Type = Integer32
_IbmsysRealMemSize_Object = MibScalar
ibmsysRealMemSize = _IbmsysRealMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 3, 1),
    _IbmsysRealMemSize_Type()
)
ibmsysRealMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysRealMemSize.setStatus("mandatory")
_IbmsysRealMemInUse_Type = Gauge32
_IbmsysRealMemInUse_Object = MibScalar
ibmsysRealMemInUse = _IbmsysRealMemInUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 3, 2),
    _IbmsysRealMemInUse_Type()
)
ibmsysRealMemInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysRealMemInUse.setStatus("mandatory")
_IbmsysRealMemFree_Type = Gauge32
_IbmsysRealMemFree_Object = MibScalar
ibmsysRealMemFree = _IbmsysRealMemFree_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 4, 7, 3, 3),
    _IbmsysRealMemFree_Type()
)
ibmsysRealMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsysRealMemFree.setStatus("mandatory")
_Ibmicmp_ObjectIdentity = ObjectIdentity
ibmicmp = _Ibmicmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 5)
)
_Ibmsnmp_ObjectIdentity = ObjectIdentity
ibmsnmp = _Ibmsnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 6)
)
_IbmTrapNum_Type = Counter32
_IbmTrapNum_Object = MibScalar
ibmTrapNum = _IbmTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 6, 1),
    _IbmTrapNum_Type()
)
ibmTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTrapNum.setStatus("mandatory")
_IbmTrapThrottleCount_Type = Counter32
_IbmTrapThrottleCount_Object = MibScalar
ibmTrapThrottleCount = _IbmTrapThrottleCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 6, 2),
    _IbmTrapThrottleCount_Type()
)
ibmTrapThrottleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTrapThrottleCount.setStatus("mandatory")
_IbmTrapThrottleId_Type = Integer32
_IbmTrapThrottleId_Object = MibScalar
ibmTrapThrottleId = _IbmTrapThrottleId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 6, 3),
    _IbmTrapThrottleId_Type()
)
ibmTrapThrottleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTrapThrottleId.setStatus("mandatory")
_IbmTrapThrottleTime_Type = Integer32
_IbmTrapThrottleTime_Object = MibScalar
ibmTrapThrottleTime = _IbmTrapThrottleTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 6, 4),
    _IbmTrapThrottleTime_Type()
)
ibmTrapThrottleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTrapThrottleTime.setStatus("mandatory")
_Ibmbridge_ObjectIdentity = ObjectIdentity
ibmbridge = _Ibmbridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7)
)
_IbmbridgeMACAddressFilters_ObjectIdentity = ObjectIdentity
ibmbridgeMACAddressFilters = _IbmbridgeMACAddressFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1)
)
_IbmmacAddrFilterInfoTable_Object = MibTable
ibmmacAddrFilterInfoTable = _IbmmacAddrFilterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ibmmacAddrFilterInfoTable.setStatus("mandatory")
_IbmmacAddrFilterInfoEntry_Object = MibTableRow
ibmmacAddrFilterInfoEntry = _IbmmacAddrFilterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1)
)
ibmmacAddrFilterInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmmacAddrFilterType"),
    (0, "IBM6611-MIB", "ibmmacAddrFilterIfIndex"),
)
if mibBuilder.loadTexts:
    ibmmacAddrFilterInfoEntry.setStatus("mandatory")
_IbmmacAddrFilterIfIndex_Type = Integer32
_IbmmacAddrFilterIfIndex_Object = MibTableColumn
ibmmacAddrFilterIfIndex = _IbmmacAddrFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 1),
    _IbmmacAddrFilterIfIndex_Type()
)
ibmmacAddrFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterIfIndex.setStatus("mandatory")


class _IbmmacAddrFilterInBcastType_Type(Integer32):
    """Custom type ibmmacAddrFilterInBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmmacAddrFilterInBcastType_Type.__name__ = "Integer32"
_IbmmacAddrFilterInBcastType_Object = MibTableColumn
ibmmacAddrFilterInBcastType = _IbmmacAddrFilterInBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 2),
    _IbmmacAddrFilterInBcastType_Type()
)
ibmmacAddrFilterInBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInBcastType.setStatus("mandatory")


class _IbmmacAddrFilterOutBcastType_Type(Integer32):
    """Custom type ibmmacAddrFilterOutBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmmacAddrFilterOutBcastType_Type.__name__ = "Integer32"
_IbmmacAddrFilterOutBcastType_Object = MibTableColumn
ibmmacAddrFilterOutBcastType = _IbmmacAddrFilterOutBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 3),
    _IbmmacAddrFilterOutBcastType_Type()
)
ibmmacAddrFilterOutBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutBcastType.setStatus("mandatory")


class _IbmmacAddrFilterInFilterType_Type(Integer32):
    """Custom type ibmmacAddrFilterInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmmacAddrFilterInFilterType_Type.__name__ = "Integer32"
_IbmmacAddrFilterInFilterType_Object = MibTableColumn
ibmmacAddrFilterInFilterType = _IbmmacAddrFilterInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 4),
    _IbmmacAddrFilterInFilterType_Type()
)
ibmmacAddrFilterInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInFilterType.setStatus("mandatory")


class _IbmmacAddrFilterOutFilterType_Type(Integer32):
    """Custom type ibmmacAddrFilterOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmmacAddrFilterOutFilterType_Type.__name__ = "Integer32"
_IbmmacAddrFilterOutFilterType_Object = MibTableColumn
ibmmacAddrFilterOutFilterType = _IbmmacAddrFilterOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 5),
    _IbmmacAddrFilterOutFilterType_Type()
)
ibmmacAddrFilterOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutFilterType.setStatus("mandatory")
_IbmmacAddrFilterInNotForwarded_Type = Counter32
_IbmmacAddrFilterInNotForwarded_Object = MibTableColumn
ibmmacAddrFilterInNotForwarded = _IbmmacAddrFilterInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 6),
    _IbmmacAddrFilterInNotForwarded_Type()
)
ibmmacAddrFilterInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInNotForwarded.setStatus("mandatory")
_IbmmacAddrFilterOutNotForwarded_Type = Counter32
_IbmmacAddrFilterOutNotForwarded_Object = MibTableColumn
ibmmacAddrFilterOutNotForwarded = _IbmmacAddrFilterOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 7),
    _IbmmacAddrFilterOutNotForwarded_Type()
)
ibmmacAddrFilterOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutNotForwarded.setStatus("mandatory")


class _IbmmacAddrFilterType_Type(Integer32):
    """Custom type ibmmacAddrFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmmacAddrFilterType_Type.__name__ = "Integer32"
_IbmmacAddrFilterType_Object = MibTableColumn
ibmmacAddrFilterType = _IbmmacAddrFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 1, 1, 8),
    _IbmmacAddrFilterType_Type()
)
ibmmacAddrFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterType.setStatus("mandatory")
_IbmmacAddrFilterInTable_Object = MibTable
ibmmacAddrFilterInTable = _IbmmacAddrFilterInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ibmmacAddrFilterInTable.setStatus("mandatory")
_IbmmacAddrFilterInEntry_Object = MibTableRow
ibmmacAddrFilterInEntry = _IbmmacAddrFilterInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2, 1)
)
ibmmacAddrFilterInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmmacAddrFilterInType"),
    (0, "IBM6611-MIB", "ibmmacAddrFilterInIfIndex"),
    (0, "IBM6611-MIB", "ibmmacAddrFilterInSrcAddress"),
    (0, "IBM6611-MIB", "ibmmacAddrFilterInDestAddress"),
)
if mibBuilder.loadTexts:
    ibmmacAddrFilterInEntry.setStatus("mandatory")
_IbmmacAddrFilterInIfIndex_Type = Integer32
_IbmmacAddrFilterInIfIndex_Object = MibTableColumn
ibmmacAddrFilterInIfIndex = _IbmmacAddrFilterInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2, 1, 1),
    _IbmmacAddrFilterInIfIndex_Type()
)
ibmmacAddrFilterInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInIfIndex.setStatus("mandatory")


class _IbmmacAddrFilterInSrcAddress_Type(OctetString):
    """Custom type ibmmacAddrFilterInSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterInSrcAddress_Type.__name__ = "OctetString"
_IbmmacAddrFilterInSrcAddress_Object = MibTableColumn
ibmmacAddrFilterInSrcAddress = _IbmmacAddrFilterInSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2, 1, 2),
    _IbmmacAddrFilterInSrcAddress_Type()
)
ibmmacAddrFilterInSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInSrcAddress.setStatus("mandatory")


class _IbmmacAddrFilterInSrcMask_Type(OctetString):
    """Custom type ibmmacAddrFilterInSrcMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterInSrcMask_Type.__name__ = "OctetString"
_IbmmacAddrFilterInSrcMask_Object = MibTableColumn
ibmmacAddrFilterInSrcMask = _IbmmacAddrFilterInSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2, 1, 3),
    _IbmmacAddrFilterInSrcMask_Type()
)
ibmmacAddrFilterInSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInSrcMask.setStatus("mandatory")


class _IbmmacAddrFilterInDestAddress_Type(OctetString):
    """Custom type ibmmacAddrFilterInDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterInDestAddress_Type.__name__ = "OctetString"
_IbmmacAddrFilterInDestAddress_Object = MibTableColumn
ibmmacAddrFilterInDestAddress = _IbmmacAddrFilterInDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2, 1, 4),
    _IbmmacAddrFilterInDestAddress_Type()
)
ibmmacAddrFilterInDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInDestAddress.setStatus("mandatory")


class _IbmmacAddrFilterInDestMask_Type(OctetString):
    """Custom type ibmmacAddrFilterInDestMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterInDestMask_Type.__name__ = "OctetString"
_IbmmacAddrFilterInDestMask_Object = MibTableColumn
ibmmacAddrFilterInDestMask = _IbmmacAddrFilterInDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2, 1, 5),
    _IbmmacAddrFilterInDestMask_Type()
)
ibmmacAddrFilterInDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInDestMask.setStatus("mandatory")


class _IbmmacAddrFilterInType_Type(Integer32):
    """Custom type ibmmacAddrFilterInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmmacAddrFilterInType_Type.__name__ = "Integer32"
_IbmmacAddrFilterInType_Object = MibTableColumn
ibmmacAddrFilterInType = _IbmmacAddrFilterInType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 2, 1, 6),
    _IbmmacAddrFilterInType_Type()
)
ibmmacAddrFilterInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterInType.setStatus("mandatory")
_IbmmacAddrFilterOutTable_Object = MibTable
ibmmacAddrFilterOutTable = _IbmmacAddrFilterOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutTable.setStatus("mandatory")
_IbmmacAddrFilterOutEntry_Object = MibTableRow
ibmmacAddrFilterOutEntry = _IbmmacAddrFilterOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3, 1)
)
ibmmacAddrFilterOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmmacAddrFilterOutType"),
    (0, "IBM6611-MIB", "ibmmacAddrFilterOutIfIndex"),
    (0, "IBM6611-MIB", "ibmmacAddrFilterOutSrcAddress"),
    (0, "IBM6611-MIB", "ibmmacAddrFilterOutDestAddress"),
)
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutEntry.setStatus("mandatory")
_IbmmacAddrFilterOutIfIndex_Type = Integer32
_IbmmacAddrFilterOutIfIndex_Object = MibTableColumn
ibmmacAddrFilterOutIfIndex = _IbmmacAddrFilterOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3, 1, 1),
    _IbmmacAddrFilterOutIfIndex_Type()
)
ibmmacAddrFilterOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutIfIndex.setStatus("mandatory")


class _IbmmacAddrFilterOutSrcAddress_Type(OctetString):
    """Custom type ibmmacAddrFilterOutSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterOutSrcAddress_Type.__name__ = "OctetString"
_IbmmacAddrFilterOutSrcAddress_Object = MibTableColumn
ibmmacAddrFilterOutSrcAddress = _IbmmacAddrFilterOutSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3, 1, 2),
    _IbmmacAddrFilterOutSrcAddress_Type()
)
ibmmacAddrFilterOutSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutSrcAddress.setStatus("mandatory")


class _IbmmacAddrFilterOutSrcMask_Type(OctetString):
    """Custom type ibmmacAddrFilterOutSrcMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterOutSrcMask_Type.__name__ = "OctetString"
_IbmmacAddrFilterOutSrcMask_Object = MibTableColumn
ibmmacAddrFilterOutSrcMask = _IbmmacAddrFilterOutSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3, 1, 3),
    _IbmmacAddrFilterOutSrcMask_Type()
)
ibmmacAddrFilterOutSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutSrcMask.setStatus("mandatory")


class _IbmmacAddrFilterOutDestAddress_Type(OctetString):
    """Custom type ibmmacAddrFilterOutDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterOutDestAddress_Type.__name__ = "OctetString"
_IbmmacAddrFilterOutDestAddress_Object = MibTableColumn
ibmmacAddrFilterOutDestAddress = _IbmmacAddrFilterOutDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3, 1, 4),
    _IbmmacAddrFilterOutDestAddress_Type()
)
ibmmacAddrFilterOutDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutDestAddress.setStatus("mandatory")


class _IbmmacAddrFilterOutDestMask_Type(OctetString):
    """Custom type ibmmacAddrFilterOutDestMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmmacAddrFilterOutDestMask_Type.__name__ = "OctetString"
_IbmmacAddrFilterOutDestMask_Object = MibTableColumn
ibmmacAddrFilterOutDestMask = _IbmmacAddrFilterOutDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3, 1, 5),
    _IbmmacAddrFilterOutDestMask_Type()
)
ibmmacAddrFilterOutDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutDestMask.setStatus("mandatory")


class _IbmmacAddrFilterOutType_Type(Integer32):
    """Custom type ibmmacAddrFilterOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmmacAddrFilterOutType_Type.__name__ = "Integer32"
_IbmmacAddrFilterOutType_Object = MibTableColumn
ibmmacAddrFilterOutType = _IbmmacAddrFilterOutType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 1, 3, 1, 6),
    _IbmmacAddrFilterOutType_Type()
)
ibmmacAddrFilterOutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmmacAddrFilterOutType.setStatus("mandatory")
_IbmbridgeSAPFilters_ObjectIdentity = ObjectIdentity
ibmbridgeSAPFilters = _IbmbridgeSAPFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2)
)
_IbmsapFilterInfoTable_Object = MibTable
ibmsapFilterInfoTable = _IbmsapFilterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    ibmsapFilterInfoTable.setStatus("mandatory")
_IbmsapFilterInfoEntry_Object = MibTableRow
ibmsapFilterInfoEntry = _IbmsapFilterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1)
)
ibmsapFilterInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmsapFilterType"),
    (0, "IBM6611-MIB", "ibmsapFilterIfIndex"),
)
if mibBuilder.loadTexts:
    ibmsapFilterInfoEntry.setStatus("mandatory")
_IbmsapFilterIfIndex_Type = Integer32
_IbmsapFilterIfIndex_Object = MibTableColumn
ibmsapFilterIfIndex = _IbmsapFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 1),
    _IbmsapFilterIfIndex_Type()
)
ibmsapFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterIfIndex.setStatus("mandatory")


class _IbmsapFilterInBcastType_Type(Integer32):
    """Custom type ibmsapFilterInBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmsapFilterInBcastType_Type.__name__ = "Integer32"
_IbmsapFilterInBcastType_Object = MibTableColumn
ibmsapFilterInBcastType = _IbmsapFilterInBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 2),
    _IbmsapFilterInBcastType_Type()
)
ibmsapFilterInBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterInBcastType.setStatus("mandatory")


class _IbmsapFilterOutBcastType_Type(Integer32):
    """Custom type ibmsapFilterOutBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmsapFilterOutBcastType_Type.__name__ = "Integer32"
_IbmsapFilterOutBcastType_Object = MibTableColumn
ibmsapFilterOutBcastType = _IbmsapFilterOutBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 3),
    _IbmsapFilterOutBcastType_Type()
)
ibmsapFilterOutBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterOutBcastType.setStatus("mandatory")


class _IbmsapFilterIn_Type(OctetString):
    """Custom type ibmsapFilterIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbmsapFilterIn_Type.__name__ = "OctetString"
_IbmsapFilterIn_Object = MibTableColumn
ibmsapFilterIn = _IbmsapFilterIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 4),
    _IbmsapFilterIn_Type()
)
ibmsapFilterIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterIn.setStatus("mandatory")


class _IbmsapFilterOut_Type(OctetString):
    """Custom type ibmsapFilterOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbmsapFilterOut_Type.__name__ = "OctetString"
_IbmsapFilterOut_Object = MibTableColumn
ibmsapFilterOut = _IbmsapFilterOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 5),
    _IbmsapFilterOut_Type()
)
ibmsapFilterOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterOut.setStatus("mandatory")
_IbmsapFilterInNotForwarded_Type = Counter32
_IbmsapFilterInNotForwarded_Object = MibTableColumn
ibmsapFilterInNotForwarded = _IbmsapFilterInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 6),
    _IbmsapFilterInNotForwarded_Type()
)
ibmsapFilterInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterInNotForwarded.setStatus("mandatory")
_IbmsapFilterOutNotForwarded_Type = Counter32
_IbmsapFilterOutNotForwarded_Object = MibTableColumn
ibmsapFilterOutNotForwarded = _IbmsapFilterOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 7),
    _IbmsapFilterOutNotForwarded_Type()
)
ibmsapFilterOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterOutNotForwarded.setStatus("mandatory")


class _IbmsapFilterType_Type(Integer32):
    """Custom type ibmsapFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmsapFilterType_Type.__name__ = "Integer32"
_IbmsapFilterType_Object = MibTableColumn
ibmsapFilterType = _IbmsapFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 2, 1, 1, 8),
    _IbmsapFilterType_Type()
)
ibmsapFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsapFilterType.setStatus("mandatory")
_IbmbridgeSNAPFilters_ObjectIdentity = ObjectIdentity
ibmbridgeSNAPFilters = _IbmbridgeSNAPFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3)
)
_IbmsnapFilterInfoTable_Object = MibTable
ibmsnapFilterInfoTable = _IbmsnapFilterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    ibmsnapFilterInfoTable.setStatus("mandatory")
_IbmsnapFilterInfoEntry_Object = MibTableRow
ibmsnapFilterInfoEntry = _IbmsnapFilterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1, 1)
)
ibmsnapFilterInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmsnapFilterType"),
    (0, "IBM6611-MIB", "ibmsnapFilterIfIndex"),
)
if mibBuilder.loadTexts:
    ibmsnapFilterInfoEntry.setStatus("mandatory")
_IbmsnapFilterIfIndex_Type = Integer32
_IbmsnapFilterIfIndex_Object = MibTableColumn
ibmsnapFilterIfIndex = _IbmsnapFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1, 1, 1),
    _IbmsnapFilterIfIndex_Type()
)
ibmsnapFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterIfIndex.setStatus("mandatory")


class _IbmsnapFilterInFilterType_Type(Integer32):
    """Custom type ibmsnapFilterInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmsnapFilterInFilterType_Type.__name__ = "Integer32"
_IbmsnapFilterInFilterType_Object = MibTableColumn
ibmsnapFilterInFilterType = _IbmsnapFilterInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1, 1, 2),
    _IbmsnapFilterInFilterType_Type()
)
ibmsnapFilterInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterInFilterType.setStatus("mandatory")


class _IbmsnapFilterOutFilterType_Type(Integer32):
    """Custom type ibmsnapFilterOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmsnapFilterOutFilterType_Type.__name__ = "Integer32"
_IbmsnapFilterOutFilterType_Object = MibTableColumn
ibmsnapFilterOutFilterType = _IbmsnapFilterOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1, 1, 3),
    _IbmsnapFilterOutFilterType_Type()
)
ibmsnapFilterOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterOutFilterType.setStatus("mandatory")
_IbmsnapFilterInNotForwarded_Type = Counter32
_IbmsnapFilterInNotForwarded_Object = MibTableColumn
ibmsnapFilterInNotForwarded = _IbmsnapFilterInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1, 1, 4),
    _IbmsnapFilterInNotForwarded_Type()
)
ibmsnapFilterInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterInNotForwarded.setStatus("mandatory")
_IbmsnapFilterOutNotForwarded_Type = Counter32
_IbmsnapFilterOutNotForwarded_Object = MibTableColumn
ibmsnapFilterOutNotForwarded = _IbmsnapFilterOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1, 1, 5),
    _IbmsnapFilterOutNotForwarded_Type()
)
ibmsnapFilterOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterOutNotForwarded.setStatus("mandatory")


class _IbmsnapFilterType_Type(Integer32):
    """Custom type ibmsnapFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmsnapFilterType_Type.__name__ = "Integer32"
_IbmsnapFilterType_Object = MibTableColumn
ibmsnapFilterType = _IbmsnapFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 1, 1, 6),
    _IbmsnapFilterType_Type()
)
ibmsnapFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterType.setStatus("mandatory")
_IbmsnapFilterInTable_Object = MibTable
ibmsnapFilterInTable = _IbmsnapFilterInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 2)
)
if mibBuilder.loadTexts:
    ibmsnapFilterInTable.setStatus("mandatory")
_IbmsnapFilterInEntry_Object = MibTableRow
ibmsnapFilterInEntry = _IbmsnapFilterInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 2, 1)
)
ibmsnapFilterInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmsnapFilterInType"),
    (0, "IBM6611-MIB", "ibmsnapFilterInIfIndex"),
    (0, "IBM6611-MIB", "ibmsnapFilterInValue"),
)
if mibBuilder.loadTexts:
    ibmsnapFilterInEntry.setStatus("mandatory")
_IbmsnapFilterInIfIndex_Type = Integer32
_IbmsnapFilterInIfIndex_Object = MibTableColumn
ibmsnapFilterInIfIndex = _IbmsnapFilterInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 2, 1, 1),
    _IbmsnapFilterInIfIndex_Type()
)
ibmsnapFilterInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterInIfIndex.setStatus("mandatory")
_IbmsnapFilterInValue_Type = Integer32
_IbmsnapFilterInValue_Object = MibTableColumn
ibmsnapFilterInValue = _IbmsnapFilterInValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 2, 1, 2),
    _IbmsnapFilterInValue_Type()
)
ibmsnapFilterInValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterInValue.setStatus("mandatory")
_IbmsnapFilterInMask_Type = Integer32
_IbmsnapFilterInMask_Object = MibTableColumn
ibmsnapFilterInMask = _IbmsnapFilterInMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 2, 1, 3),
    _IbmsnapFilterInMask_Type()
)
ibmsnapFilterInMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterInMask.setStatus("mandatory")


class _IbmsnapFilterInType_Type(Integer32):
    """Custom type ibmsnapFilterInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmsnapFilterInType_Type.__name__ = "Integer32"
_IbmsnapFilterInType_Object = MibTableColumn
ibmsnapFilterInType = _IbmsnapFilterInType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 2, 1, 4),
    _IbmsnapFilterInType_Type()
)
ibmsnapFilterInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterInType.setStatus("mandatory")
_IbmsnapFilterOutTable_Object = MibTable
ibmsnapFilterOutTable = _IbmsnapFilterOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 3)
)
if mibBuilder.loadTexts:
    ibmsnapFilterOutTable.setStatus("mandatory")
_IbmsnapFilterOutEntry_Object = MibTableRow
ibmsnapFilterOutEntry = _IbmsnapFilterOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 3, 1)
)
ibmsnapFilterOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmsnapFilterOutType"),
    (0, "IBM6611-MIB", "ibmsnapFilterOutIfIndex"),
    (0, "IBM6611-MIB", "ibmsnapFilterOutValue"),
)
if mibBuilder.loadTexts:
    ibmsnapFilterOutEntry.setStatus("mandatory")
_IbmsnapFilterOutIfIndex_Type = Integer32
_IbmsnapFilterOutIfIndex_Object = MibTableColumn
ibmsnapFilterOutIfIndex = _IbmsnapFilterOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 3, 1, 1),
    _IbmsnapFilterOutIfIndex_Type()
)
ibmsnapFilterOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterOutIfIndex.setStatus("mandatory")
_IbmsnapFilterOutValue_Type = Integer32
_IbmsnapFilterOutValue_Object = MibTableColumn
ibmsnapFilterOutValue = _IbmsnapFilterOutValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 3, 1, 2),
    _IbmsnapFilterOutValue_Type()
)
ibmsnapFilterOutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterOutValue.setStatus("mandatory")
_IbmsnapFilterOutMask_Type = Integer32
_IbmsnapFilterOutMask_Object = MibTableColumn
ibmsnapFilterOutMask = _IbmsnapFilterOutMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 3, 1, 3),
    _IbmsnapFilterOutMask_Type()
)
ibmsnapFilterOutMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterOutMask.setStatus("mandatory")


class _IbmsnapFilterOutType_Type(Integer32):
    """Custom type ibmsnapFilterOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmsnapFilterOutType_Type.__name__ = "Integer32"
_IbmsnapFilterOutType_Object = MibTableColumn
ibmsnapFilterOutType = _IbmsnapFilterOutType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 3, 3, 1, 4),
    _IbmsnapFilterOutType_Type()
)
ibmsnapFilterOutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmsnapFilterOutType.setStatus("mandatory")
_IbmbridgeRingFilters_ObjectIdentity = ObjectIdentity
ibmbridgeRingFilters = _IbmbridgeRingFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4)
)
_IbmringFilterInfoTable_Object = MibTable
ibmringFilterInfoTable = _IbmringFilterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    ibmringFilterInfoTable.setStatus("mandatory")
_IbmringFilterInfoEntry_Object = MibTableRow
ibmringFilterInfoEntry = _IbmringFilterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1)
)
ibmringFilterInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmringFilterIfIndex"),
)
if mibBuilder.loadTexts:
    ibmringFilterInfoEntry.setStatus("mandatory")
_IbmringFilterIfIndex_Type = Integer32
_IbmringFilterIfIndex_Object = MibTableColumn
ibmringFilterIfIndex = _IbmringFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1, 1),
    _IbmringFilterIfIndex_Type()
)
ibmringFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterIfIndex.setStatus("mandatory")


class _IbmringFilterInBcastType_Type(Integer32):
    """Custom type ibmringFilterInBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmringFilterInBcastType_Type.__name__ = "Integer32"
_IbmringFilterInBcastType_Object = MibTableColumn
ibmringFilterInBcastType = _IbmringFilterInBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1, 2),
    _IbmringFilterInBcastType_Type()
)
ibmringFilterInBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterInBcastType.setStatus("mandatory")


class _IbmringFilterOutBcastType_Type(Integer32):
    """Custom type ibmringFilterOutBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmringFilterOutBcastType_Type.__name__ = "Integer32"
_IbmringFilterOutBcastType_Object = MibTableColumn
ibmringFilterOutBcastType = _IbmringFilterOutBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1, 3),
    _IbmringFilterOutBcastType_Type()
)
ibmringFilterOutBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterOutBcastType.setStatus("mandatory")


class _IbmringFilterInFilterType_Type(Integer32):
    """Custom type ibmringFilterInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmringFilterInFilterType_Type.__name__ = "Integer32"
_IbmringFilterInFilterType_Object = MibTableColumn
ibmringFilterInFilterType = _IbmringFilterInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1, 4),
    _IbmringFilterInFilterType_Type()
)
ibmringFilterInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterInFilterType.setStatus("mandatory")


class _IbmringFilterOutFilterType_Type(Integer32):
    """Custom type ibmringFilterOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmringFilterOutFilterType_Type.__name__ = "Integer32"
_IbmringFilterOutFilterType_Object = MibTableColumn
ibmringFilterOutFilterType = _IbmringFilterOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1, 5),
    _IbmringFilterOutFilterType_Type()
)
ibmringFilterOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterOutFilterType.setStatus("mandatory")
_IbmringFilterInNotForwarded_Type = Counter32
_IbmringFilterInNotForwarded_Object = MibTableColumn
ibmringFilterInNotForwarded = _IbmringFilterInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1, 6),
    _IbmringFilterInNotForwarded_Type()
)
ibmringFilterInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterInNotForwarded.setStatus("mandatory")
_IbmringFilterOutNotForwarded_Type = Counter32
_IbmringFilterOutNotForwarded_Object = MibTableColumn
ibmringFilterOutNotForwarded = _IbmringFilterOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 1, 1, 7),
    _IbmringFilterOutNotForwarded_Type()
)
ibmringFilterOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterOutNotForwarded.setStatus("mandatory")
_IbmringFilterInTable_Object = MibTable
ibmringFilterInTable = _IbmringFilterInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 2)
)
if mibBuilder.loadTexts:
    ibmringFilterInTable.setStatus("mandatory")
_IbmringFilterInEntry_Object = MibTableRow
ibmringFilterInEntry = _IbmringFilterInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 2, 1)
)
ibmringFilterInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmringFilterInIfIndex"),
    (0, "IBM6611-MIB", "ibmringFilterInNumber"),
)
if mibBuilder.loadTexts:
    ibmringFilterInEntry.setStatus("mandatory")
_IbmringFilterInIfIndex_Type = Integer32
_IbmringFilterInIfIndex_Object = MibTableColumn
ibmringFilterInIfIndex = _IbmringFilterInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 2, 1, 1),
    _IbmringFilterInIfIndex_Type()
)
ibmringFilterInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterInIfIndex.setStatus("mandatory")
_IbmringFilterInNumber_Type = Integer32
_IbmringFilterInNumber_Object = MibTableColumn
ibmringFilterInNumber = _IbmringFilterInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 2, 1, 2),
    _IbmringFilterInNumber_Type()
)
ibmringFilterInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterInNumber.setStatus("mandatory")
_IbmringFilterInMask_Type = Integer32
_IbmringFilterInMask_Object = MibTableColumn
ibmringFilterInMask = _IbmringFilterInMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 2, 1, 3),
    _IbmringFilterInMask_Type()
)
ibmringFilterInMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterInMask.setStatus("mandatory")
_IbmringFilterOutTable_Object = MibTable
ibmringFilterOutTable = _IbmringFilterOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 3)
)
if mibBuilder.loadTexts:
    ibmringFilterOutTable.setStatus("mandatory")
_IbmringFilterOutEntry_Object = MibTableRow
ibmringFilterOutEntry = _IbmringFilterOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 3, 1)
)
ibmringFilterOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmringFilterOutIfIndex"),
    (0, "IBM6611-MIB", "ibmringFilterOutNumber"),
)
if mibBuilder.loadTexts:
    ibmringFilterOutEntry.setStatus("mandatory")
_IbmringFilterOutIfIndex_Type = Integer32
_IbmringFilterOutIfIndex_Object = MibTableColumn
ibmringFilterOutIfIndex = _IbmringFilterOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 3, 1, 1),
    _IbmringFilterOutIfIndex_Type()
)
ibmringFilterOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterOutIfIndex.setStatus("mandatory")
_IbmringFilterOutNumber_Type = Integer32
_IbmringFilterOutNumber_Object = MibTableColumn
ibmringFilterOutNumber = _IbmringFilterOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 3, 1, 2),
    _IbmringFilterOutNumber_Type()
)
ibmringFilterOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterOutNumber.setStatus("mandatory")
_IbmringFilterOutMask_Type = Integer32
_IbmringFilterOutMask_Object = MibTableColumn
ibmringFilterOutMask = _IbmringFilterOutMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 4, 3, 1, 3),
    _IbmringFilterOutMask_Type()
)
ibmringFilterOutMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmringFilterOutMask.setStatus("mandatory")
_IbmbridgeHopCountFilters_ObjectIdentity = ObjectIdentity
ibmbridgeHopCountFilters = _IbmbridgeHopCountFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 5)
)
_IbmhopCountFilterInfoTable_Object = MibTable
ibmhopCountFilterInfoTable = _IbmhopCountFilterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 5, 1)
)
if mibBuilder.loadTexts:
    ibmhopCountFilterInfoTable.setStatus("mandatory")
_IbmhopCountFilterInfoEntry_Object = MibTableRow
ibmhopCountFilterInfoEntry = _IbmhopCountFilterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 5, 1, 1)
)
ibmhopCountFilterInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmhopCountFilterIfIndex"),
)
if mibBuilder.loadTexts:
    ibmhopCountFilterInfoEntry.setStatus("mandatory")
_IbmhopCountFilterIfIndex_Type = Integer32
_IbmhopCountFilterIfIndex_Object = MibTableColumn
ibmhopCountFilterIfIndex = _IbmhopCountFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 5, 1, 1, 1),
    _IbmhopCountFilterIfIndex_Type()
)
ibmhopCountFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmhopCountFilterIfIndex.setStatus("mandatory")


class _IbmhopCountFilterBcastType_Type(Integer32):
    """Custom type ibmhopCountFilterBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmhopCountFilterBcastType_Type.__name__ = "Integer32"
_IbmhopCountFilterBcastType_Object = MibTableColumn
ibmhopCountFilterBcastType = _IbmhopCountFilterBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 5, 1, 1, 2),
    _IbmhopCountFilterBcastType_Type()
)
ibmhopCountFilterBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmhopCountFilterBcastType.setStatus("mandatory")
_IbmhopCountFilterCount_Type = Integer32
_IbmhopCountFilterCount_Object = MibTableColumn
ibmhopCountFilterCount = _IbmhopCountFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 5, 1, 1, 3),
    _IbmhopCountFilterCount_Type()
)
ibmhopCountFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmhopCountFilterCount.setStatus("mandatory")
_IbmbridgeWindowFilters_ObjectIdentity = ObjectIdentity
ibmbridgeWindowFilters = _IbmbridgeWindowFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6)
)
_IbmwindowFilterInfoTable_Object = MibTable
ibmwindowFilterInfoTable = _IbmwindowFilterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1)
)
if mibBuilder.loadTexts:
    ibmwindowFilterInfoTable.setStatus("mandatory")
_IbmwindowFilterInfoEntry_Object = MibTableRow
ibmwindowFilterInfoEntry = _IbmwindowFilterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1)
)
ibmwindowFilterInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmwindowFilterType"),
    (0, "IBM6611-MIB", "ibmwindowFilterIfIndex"),
)
if mibBuilder.loadTexts:
    ibmwindowFilterInfoEntry.setStatus("mandatory")
_IbmwindowFilterIfIndex_Type = Integer32
_IbmwindowFilterIfIndex_Object = MibTableColumn
ibmwindowFilterIfIndex = _IbmwindowFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 1),
    _IbmwindowFilterIfIndex_Type()
)
ibmwindowFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterIfIndex.setStatus("mandatory")


class _IbmwindowFilterInBcastType_Type(Integer32):
    """Custom type ibmwindowFilterInBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmwindowFilterInBcastType_Type.__name__ = "Integer32"
_IbmwindowFilterInBcastType_Object = MibTableColumn
ibmwindowFilterInBcastType = _IbmwindowFilterInBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 2),
    _IbmwindowFilterInBcastType_Type()
)
ibmwindowFilterInBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInBcastType.setStatus("mandatory")


class _IbmwindowFilterOutBcastType_Type(Integer32):
    """Custom type ibmwindowFilterOutBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmwindowFilterOutBcastType_Type.__name__ = "Integer32"
_IbmwindowFilterOutBcastType_Object = MibTableColumn
ibmwindowFilterOutBcastType = _IbmwindowFilterOutBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 3),
    _IbmwindowFilterOutBcastType_Type()
)
ibmwindowFilterOutBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutBcastType.setStatus("mandatory")


class _IbmwindowFilterInFilterType_Type(Integer32):
    """Custom type ibmwindowFilterInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmwindowFilterInFilterType_Type.__name__ = "Integer32"
_IbmwindowFilterInFilterType_Object = MibTableColumn
ibmwindowFilterInFilterType = _IbmwindowFilterInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 4),
    _IbmwindowFilterInFilterType_Type()
)
ibmwindowFilterInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInFilterType.setStatus("mandatory")


class _IbmwindowFilterOutFilterType_Type(Integer32):
    """Custom type ibmwindowFilterOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmwindowFilterOutFilterType_Type.__name__ = "Integer32"
_IbmwindowFilterOutFilterType_Object = MibTableColumn
ibmwindowFilterOutFilterType = _IbmwindowFilterOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 5),
    _IbmwindowFilterOutFilterType_Type()
)
ibmwindowFilterOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutFilterType.setStatus("mandatory")
_IbmwindowFilterInNotForwarded_Type = Counter32
_IbmwindowFilterInNotForwarded_Object = MibTableColumn
ibmwindowFilterInNotForwarded = _IbmwindowFilterInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 6),
    _IbmwindowFilterInNotForwarded_Type()
)
ibmwindowFilterInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInNotForwarded.setStatus("mandatory")
_IbmwindowFilterOutNotForwarded_Type = Counter32
_IbmwindowFilterOutNotForwarded_Object = MibTableColumn
ibmwindowFilterOutNotForwarded = _IbmwindowFilterOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 7),
    _IbmwindowFilterOutNotForwarded_Type()
)
ibmwindowFilterOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutNotForwarded.setStatus("mandatory")


class _IbmwindowFilterType_Type(Integer32):
    """Custom type ibmwindowFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmwindowFilterType_Type.__name__ = "Integer32"
_IbmwindowFilterType_Object = MibTableColumn
ibmwindowFilterType = _IbmwindowFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 1, 1, 8),
    _IbmwindowFilterType_Type()
)
ibmwindowFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterType.setStatus("mandatory")
_IbmwindowFilterInTable_Object = MibTable
ibmwindowFilterInTable = _IbmwindowFilterInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2)
)
if mibBuilder.loadTexts:
    ibmwindowFilterInTable.setStatus("mandatory")
_IbmwindowFilterInEntry_Object = MibTableRow
ibmwindowFilterInEntry = _IbmwindowFilterInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1)
)
ibmwindowFilterInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmwindowFilterInType"),
    (0, "IBM6611-MIB", "ibmwindowFilterInIfIndex"),
    (0, "IBM6611-MIB", "ibmwindowFilterInId"),
    (0, "IBM6611-MIB", "ibmwindowFilterInContents"),
)
if mibBuilder.loadTexts:
    ibmwindowFilterInEntry.setStatus("mandatory")
_IbmwindowFilterInIfIndex_Type = Integer32
_IbmwindowFilterInIfIndex_Object = MibTableColumn
ibmwindowFilterInIfIndex = _IbmwindowFilterInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 1),
    _IbmwindowFilterInIfIndex_Type()
)
ibmwindowFilterInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInIfIndex.setStatus("mandatory")
_IbmwindowFilterInContents_Type = OctetString
_IbmwindowFilterInContents_Object = MibTableColumn
ibmwindowFilterInContents = _IbmwindowFilterInContents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 2),
    _IbmwindowFilterInContents_Type()
)
ibmwindowFilterInContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInContents.setStatus("mandatory")
_IbmwindowFilterInMaskString_Type = OctetString
_IbmwindowFilterInMaskString_Object = MibTableColumn
ibmwindowFilterInMaskString = _IbmwindowFilterInMaskString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 3),
    _IbmwindowFilterInMaskString_Type()
)
ibmwindowFilterInMaskString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInMaskString.setStatus("mandatory")
_IbmwindowFilterInOffsetStart_Type = DisplayString
_IbmwindowFilterInOffsetStart_Object = MibTableColumn
ibmwindowFilterInOffsetStart = _IbmwindowFilterInOffsetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 4),
    _IbmwindowFilterInOffsetStart_Type()
)
ibmwindowFilterInOffsetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInOffsetStart.setStatus("mandatory")


class _IbmwindowFilterInNumBytes_Type(OctetString):
    """Custom type ibmwindowFilterInNumBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmwindowFilterInNumBytes_Type.__name__ = "OctetString"
_IbmwindowFilterInNumBytes_Object = MibTableColumn
ibmwindowFilterInNumBytes = _IbmwindowFilterInNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 5),
    _IbmwindowFilterInNumBytes_Type()
)
ibmwindowFilterInNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInNumBytes.setStatus("mandatory")


class _IbmwindowFilterInOffset_Type(OctetString):
    """Custom type ibmwindowFilterInOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmwindowFilterInOffset_Type.__name__ = "OctetString"
_IbmwindowFilterInOffset_Object = MibTableColumn
ibmwindowFilterInOffset = _IbmwindowFilterInOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 6),
    _IbmwindowFilterInOffset_Type()
)
ibmwindowFilterInOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInOffset.setStatus("mandatory")
_IbmwindowFilterInId_Type = Integer32
_IbmwindowFilterInId_Object = MibTableColumn
ibmwindowFilterInId = _IbmwindowFilterInId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 7),
    _IbmwindowFilterInId_Type()
)
ibmwindowFilterInId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInId.setStatus("mandatory")


class _IbmwindowFilterInType_Type(Integer32):
    """Custom type ibmwindowFilterInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmwindowFilterInType_Type.__name__ = "Integer32"
_IbmwindowFilterInType_Object = MibTableColumn
ibmwindowFilterInType = _IbmwindowFilterInType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 2, 1, 8),
    _IbmwindowFilterInType_Type()
)
ibmwindowFilterInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterInType.setStatus("mandatory")
_IbmwindowFilterOutTable_Object = MibTable
ibmwindowFilterOutTable = _IbmwindowFilterOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3)
)
if mibBuilder.loadTexts:
    ibmwindowFilterOutTable.setStatus("mandatory")
_IbmwindowFilterOutEntry_Object = MibTableRow
ibmwindowFilterOutEntry = _IbmwindowFilterOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1)
)
ibmwindowFilterOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmwindowFilterOutType"),
    (0, "IBM6611-MIB", "ibmwindowFilterOutIfIndex"),
    (0, "IBM6611-MIB", "ibmwindowFilterOutId"),
    (0, "IBM6611-MIB", "ibmwindowFilterOutContents"),
)
if mibBuilder.loadTexts:
    ibmwindowFilterOutEntry.setStatus("mandatory")
_IbmwindowFilterOutIfIndex_Type = Integer32
_IbmwindowFilterOutIfIndex_Object = MibTableColumn
ibmwindowFilterOutIfIndex = _IbmwindowFilterOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 1),
    _IbmwindowFilterOutIfIndex_Type()
)
ibmwindowFilterOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutIfIndex.setStatus("mandatory")
_IbmwindowFilterOutContents_Type = OctetString
_IbmwindowFilterOutContents_Object = MibTableColumn
ibmwindowFilterOutContents = _IbmwindowFilterOutContents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 2),
    _IbmwindowFilterOutContents_Type()
)
ibmwindowFilterOutContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutContents.setStatus("mandatory")
_IbmwindowFilterOutMaskString_Type = OctetString
_IbmwindowFilterOutMaskString_Object = MibTableColumn
ibmwindowFilterOutMaskString = _IbmwindowFilterOutMaskString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 3),
    _IbmwindowFilterOutMaskString_Type()
)
ibmwindowFilterOutMaskString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutMaskString.setStatus("mandatory")
_IbmwindowFilterOutOffsetStart_Type = DisplayString
_IbmwindowFilterOutOffsetStart_Object = MibTableColumn
ibmwindowFilterOutOffsetStart = _IbmwindowFilterOutOffsetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 4),
    _IbmwindowFilterOutOffsetStart_Type()
)
ibmwindowFilterOutOffsetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutOffsetStart.setStatus("mandatory")


class _IbmwindowFilterOutNumBytes_Type(OctetString):
    """Custom type ibmwindowFilterOutNumBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmwindowFilterOutNumBytes_Type.__name__ = "OctetString"
_IbmwindowFilterOutNumBytes_Object = MibTableColumn
ibmwindowFilterOutNumBytes = _IbmwindowFilterOutNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 5),
    _IbmwindowFilterOutNumBytes_Type()
)
ibmwindowFilterOutNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutNumBytes.setStatus("mandatory")


class _IbmwindowFilterOutOffset_Type(OctetString):
    """Custom type ibmwindowFilterOutOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmwindowFilterOutOffset_Type.__name__ = "OctetString"
_IbmwindowFilterOutOffset_Object = MibTableColumn
ibmwindowFilterOutOffset = _IbmwindowFilterOutOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 6),
    _IbmwindowFilterOutOffset_Type()
)
ibmwindowFilterOutOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutOffset.setStatus("mandatory")
_IbmwindowFilterOutId_Type = Integer32
_IbmwindowFilterOutId_Object = MibTableColumn
ibmwindowFilterOutId = _IbmwindowFilterOutId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 7),
    _IbmwindowFilterOutId_Type()
)
ibmwindowFilterOutId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutId.setStatus("mandatory")


class _IbmwindowFilterOutType_Type(Integer32):
    """Custom type ibmwindowFilterOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmwindowFilterOutType_Type.__name__ = "Integer32"
_IbmwindowFilterOutType_Object = MibTableColumn
ibmwindowFilterOutType = _IbmwindowFilterOutType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 6, 3, 1, 8),
    _IbmwindowFilterOutType_Type()
)
ibmwindowFilterOutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmwindowFilterOutType.setStatus("mandatory")
_IbmbridgeFiltOrderTable_ObjectIdentity = ObjectIdentity
ibmbridgeFiltOrderTable = _IbmbridgeFiltOrderTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7)
)
_IbmFiltOrderInTable_Object = MibTable
ibmFiltOrderInTable = _IbmFiltOrderInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 1)
)
if mibBuilder.loadTexts:
    ibmFiltOrderInTable.setStatus("mandatory")
_IbmFiltOrderInEntry_Object = MibTableRow
ibmFiltOrderInEntry = _IbmFiltOrderInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 1, 1)
)
ibmFiltOrderInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmFiltOrderInType"),
    (0, "IBM6611-MIB", "ibmFiltOrderInIfIndex"),
    (0, "IBM6611-MIB", "ibmFiltOrderInPriority"),
)
if mibBuilder.loadTexts:
    ibmFiltOrderInEntry.setStatus("mandatory")
_IbmFiltOrderInIfIndex_Type = Integer32
_IbmFiltOrderInIfIndex_Object = MibTableColumn
ibmFiltOrderInIfIndex = _IbmFiltOrderInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 1, 1, 1),
    _IbmFiltOrderInIfIndex_Type()
)
ibmFiltOrderInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderInIfIndex.setStatus("mandatory")
_IbmFiltOrderInPriority_Type = Integer32
_IbmFiltOrderInPriority_Object = MibTableColumn
ibmFiltOrderInPriority = _IbmFiltOrderInPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 1, 1, 2),
    _IbmFiltOrderInPriority_Type()
)
ibmFiltOrderInPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderInPriority.setStatus("mandatory")
_IbmFiltOrderInName_Type = DisplayString
_IbmFiltOrderInName_Object = MibTableColumn
ibmFiltOrderInName = _IbmFiltOrderInName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 1, 1, 3),
    _IbmFiltOrderInName_Type()
)
ibmFiltOrderInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderInName.setStatus("mandatory")


class _IbmFiltOrderInType_Type(Integer32):
    """Custom type ibmFiltOrderInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmFiltOrderInType_Type.__name__ = "Integer32"
_IbmFiltOrderInType_Object = MibTableColumn
ibmFiltOrderInType = _IbmFiltOrderInType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 1, 1, 4),
    _IbmFiltOrderInType_Type()
)
ibmFiltOrderInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderInType.setStatus("mandatory")
_IbmFiltOrderOutTable_Object = MibTable
ibmFiltOrderOutTable = _IbmFiltOrderOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 2)
)
if mibBuilder.loadTexts:
    ibmFiltOrderOutTable.setStatus("mandatory")
_IbmFiltOrderOutEntry_Object = MibTableRow
ibmFiltOrderOutEntry = _IbmFiltOrderOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 2, 1)
)
ibmFiltOrderOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmFiltOrderOutType"),
    (0, "IBM6611-MIB", "ibmFiltOrderOutIfIndex"),
    (0, "IBM6611-MIB", "ibmFiltOrderOutPriority"),
)
if mibBuilder.loadTexts:
    ibmFiltOrderOutEntry.setStatus("mandatory")
_IbmFiltOrderOutIfIndex_Type = Integer32
_IbmFiltOrderOutIfIndex_Object = MibTableColumn
ibmFiltOrderOutIfIndex = _IbmFiltOrderOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 2, 1, 1),
    _IbmFiltOrderOutIfIndex_Type()
)
ibmFiltOrderOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderOutIfIndex.setStatus("mandatory")
_IbmFiltOrderOutPriority_Type = Integer32
_IbmFiltOrderOutPriority_Object = MibTableColumn
ibmFiltOrderOutPriority = _IbmFiltOrderOutPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 2, 1, 2),
    _IbmFiltOrderOutPriority_Type()
)
ibmFiltOrderOutPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderOutPriority.setStatus("mandatory")
_IbmFiltOrderOutName_Type = DisplayString
_IbmFiltOrderOutName_Object = MibTableColumn
ibmFiltOrderOutName = _IbmFiltOrderOutName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 2, 1, 3),
    _IbmFiltOrderOutName_Type()
)
ibmFiltOrderOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderOutName.setStatus("mandatory")


class _IbmFiltOrderOutType_Type(Integer32):
    """Custom type ibmFiltOrderOutType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr", 1),
          ("tb", 2))
    )


_IbmFiltOrderOutType_Type.__name__ = "Integer32"
_IbmFiltOrderOutType_Object = MibTableColumn
ibmFiltOrderOutType = _IbmFiltOrderOutType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 7, 2, 1, 4),
    _IbmFiltOrderOutType_Type()
)
ibmFiltOrderOutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmFiltOrderOutType.setStatus("mandatory")
_IbmbridgeRIFFilters_ObjectIdentity = ObjectIdentity
ibmbridgeRIFFilters = _IbmbridgeRIFFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8)
)
_IbmRIFFilterInfoTable_Object = MibTable
ibmRIFFilterInfoTable = _IbmRIFFilterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1)
)
if mibBuilder.loadTexts:
    ibmRIFFilterInfoTable.setStatus("mandatory")
_IbmRIFFilterInfoEntry_Object = MibTableRow
ibmRIFFilterInfoEntry = _IbmRIFFilterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1)
)
ibmRIFFilterInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmRIFFilterIfIndex"),
)
if mibBuilder.loadTexts:
    ibmRIFFilterInfoEntry.setStatus("mandatory")
_IbmRIFFilterIfIndex_Type = Integer32
_IbmRIFFilterIfIndex_Object = MibTableColumn
ibmRIFFilterIfIndex = _IbmRIFFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1, 1),
    _IbmRIFFilterIfIndex_Type()
)
ibmRIFFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterIfIndex.setStatus("mandatory")


class _IbmRIFFilterInBcastType_Type(Integer32):
    """Custom type ibmRIFFilterInBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmRIFFilterInBcastType_Type.__name__ = "Integer32"
_IbmRIFFilterInBcastType_Object = MibTableColumn
ibmRIFFilterInBcastType = _IbmRIFFilterInBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1, 2),
    _IbmRIFFilterInBcastType_Type()
)
ibmRIFFilterInBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInBcastType.setStatus("mandatory")


class _IbmRIFFilterOutBcastType_Type(Integer32):
    """Custom type ibmRIFFilterOutBcastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterARB", 1),
          ("filterBoth", 3),
          ("filterSRB", 2))
    )


_IbmRIFFilterOutBcastType_Type.__name__ = "Integer32"
_IbmRIFFilterOutBcastType_Object = MibTableColumn
ibmRIFFilterOutBcastType = _IbmRIFFilterOutBcastType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1, 3),
    _IbmRIFFilterOutBcastType_Type()
)
ibmRIFFilterOutBcastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutBcastType.setStatus("mandatory")


class _IbmRIFFilterInFilterType_Type(Integer32):
    """Custom type ibmRIFFilterInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmRIFFilterInFilterType_Type.__name__ = "Integer32"
_IbmRIFFilterInFilterType_Object = MibTableColumn
ibmRIFFilterInFilterType = _IbmRIFFilterInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1, 4),
    _IbmRIFFilterInFilterType_Type()
)
ibmRIFFilterInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInFilterType.setStatus("mandatory")


class _IbmRIFFilterOutFilterType_Type(Integer32):
    """Custom type ibmRIFFilterOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmRIFFilterOutFilterType_Type.__name__ = "Integer32"
_IbmRIFFilterOutFilterType_Object = MibTableColumn
ibmRIFFilterOutFilterType = _IbmRIFFilterOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1, 5),
    _IbmRIFFilterOutFilterType_Type()
)
ibmRIFFilterOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutFilterType.setStatus("mandatory")
_IbmRIFFilterInNotForwarded_Type = Counter32
_IbmRIFFilterInNotForwarded_Object = MibTableColumn
ibmRIFFilterInNotForwarded = _IbmRIFFilterInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1, 6),
    _IbmRIFFilterInNotForwarded_Type()
)
ibmRIFFilterInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInNotForwarded.setStatus("mandatory")
_IbmRIFFilterOutNotForwarded_Type = Counter32
_IbmRIFFilterOutNotForwarded_Object = MibTableColumn
ibmRIFFilterOutNotForwarded = _IbmRIFFilterOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 1, 1, 7),
    _IbmRIFFilterOutNotForwarded_Type()
)
ibmRIFFilterOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutNotForwarded.setStatus("mandatory")
_IbmRIFFilterInTable_Object = MibTable
ibmRIFFilterInTable = _IbmRIFFilterInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2)
)
if mibBuilder.loadTexts:
    ibmRIFFilterInTable.setStatus("mandatory")
_IbmRIFFilterInEntry_Object = MibTableRow
ibmRIFFilterInEntry = _IbmRIFFilterInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2, 1)
)
ibmRIFFilterInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmRIFFilterInIfIndex"),
    (0, "IBM6611-MIB", "ibmRIFFilterInRingNumber"),
    (0, "IBM6611-MIB", "ibmRIFFilterInBridgeNumber"),
)
if mibBuilder.loadTexts:
    ibmRIFFilterInEntry.setStatus("mandatory")
_IbmRIFFilterInIfIndex_Type = Integer32
_IbmRIFFilterInIfIndex_Object = MibTableColumn
ibmRIFFilterInIfIndex = _IbmRIFFilterInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2, 1, 1),
    _IbmRIFFilterInIfIndex_Type()
)
ibmRIFFilterInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInIfIndex.setStatus("mandatory")
_IbmRIFFilterInRingNumber_Type = Integer32
_IbmRIFFilterInRingNumber_Object = MibTableColumn
ibmRIFFilterInRingNumber = _IbmRIFFilterInRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2, 1, 2),
    _IbmRIFFilterInRingNumber_Type()
)
ibmRIFFilterInRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInRingNumber.setStatus("mandatory")
_IbmRIFFilterInRingMask_Type = Integer32
_IbmRIFFilterInRingMask_Object = MibTableColumn
ibmRIFFilterInRingMask = _IbmRIFFilterInRingMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2, 1, 3),
    _IbmRIFFilterInRingMask_Type()
)
ibmRIFFilterInRingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInRingMask.setStatus("mandatory")
_IbmRIFFilterInBridgeNumber_Type = Integer32
_IbmRIFFilterInBridgeNumber_Object = MibTableColumn
ibmRIFFilterInBridgeNumber = _IbmRIFFilterInBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2, 1, 4),
    _IbmRIFFilterInBridgeNumber_Type()
)
ibmRIFFilterInBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInBridgeNumber.setStatus("mandatory")
_IbmRIFFilterInBridgeMask_Type = Integer32
_IbmRIFFilterInBridgeMask_Object = MibTableColumn
ibmRIFFilterInBridgeMask = _IbmRIFFilterInBridgeMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2, 1, 5),
    _IbmRIFFilterInBridgeMask_Type()
)
ibmRIFFilterInBridgeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInBridgeMask.setStatus("mandatory")


class _IbmRIFFilterInRouteDesignator_Type(Integer32):
    """Custom type ibmRIFFilterInRouteDesignator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allroutedesignators", 3),
          ("firstroutedesignator", 1),
          ("nexttolastroutedesignator", 2))
    )


_IbmRIFFilterInRouteDesignator_Type.__name__ = "Integer32"
_IbmRIFFilterInRouteDesignator_Object = MibTableColumn
ibmRIFFilterInRouteDesignator = _IbmRIFFilterInRouteDesignator_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 2, 1, 6),
    _IbmRIFFilterInRouteDesignator_Type()
)
ibmRIFFilterInRouteDesignator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterInRouteDesignator.setStatus("mandatory")
_IbmRIFFilterOutTable_Object = MibTable
ibmRIFFilterOutTable = _IbmRIFFilterOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3)
)
if mibBuilder.loadTexts:
    ibmRIFFilterOutTable.setStatus("mandatory")
_IbmRIFFilterOutEntry_Object = MibTableRow
ibmRIFFilterOutEntry = _IbmRIFFilterOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3, 1)
)
ibmRIFFilterOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmRIFFilterOutIfIndex"),
    (0, "IBM6611-MIB", "ibmRIFFilterOutRingNumber"),
    (0, "IBM6611-MIB", "ibmRIFFilterOutBridgeNumber"),
)
if mibBuilder.loadTexts:
    ibmRIFFilterOutEntry.setStatus("mandatory")
_IbmRIFFilterOutIfIndex_Type = Integer32
_IbmRIFFilterOutIfIndex_Object = MibTableColumn
ibmRIFFilterOutIfIndex = _IbmRIFFilterOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3, 1, 1),
    _IbmRIFFilterOutIfIndex_Type()
)
ibmRIFFilterOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutIfIndex.setStatus("mandatory")
_IbmRIFFilterOutRingNumber_Type = Integer32
_IbmRIFFilterOutRingNumber_Object = MibTableColumn
ibmRIFFilterOutRingNumber = _IbmRIFFilterOutRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3, 1, 2),
    _IbmRIFFilterOutRingNumber_Type()
)
ibmRIFFilterOutRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutRingNumber.setStatus("mandatory")
_IbmRIFFilterOutRingMask_Type = Integer32
_IbmRIFFilterOutRingMask_Object = MibTableColumn
ibmRIFFilterOutRingMask = _IbmRIFFilterOutRingMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3, 1, 3),
    _IbmRIFFilterOutRingMask_Type()
)
ibmRIFFilterOutRingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutRingMask.setStatus("mandatory")
_IbmRIFFilterOutBridgeNumber_Type = Integer32
_IbmRIFFilterOutBridgeNumber_Object = MibTableColumn
ibmRIFFilterOutBridgeNumber = _IbmRIFFilterOutBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3, 1, 4),
    _IbmRIFFilterOutBridgeNumber_Type()
)
ibmRIFFilterOutBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutBridgeNumber.setStatus("mandatory")
_IbmRIFFilterOutBridgeMask_Type = Integer32
_IbmRIFFilterOutBridgeMask_Object = MibTableColumn
ibmRIFFilterOutBridgeMask = _IbmRIFFilterOutBridgeMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3, 1, 5),
    _IbmRIFFilterOutBridgeMask_Type()
)
ibmRIFFilterOutBridgeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutBridgeMask.setStatus("mandatory")


class _IbmRIFFilterOutRouteDesignator_Type(Integer32):
    """Custom type ibmRIFFilterOutRouteDesignator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allroutedesignators", 3),
          ("firstroutedesignator", 1),
          ("nexttolastroutedesignator", 2))
    )


_IbmRIFFilterOutRouteDesignator_Type.__name__ = "Integer32"
_IbmRIFFilterOutRouteDesignator_Object = MibTableColumn
ibmRIFFilterOutRouteDesignator = _IbmRIFFilterOutRouteDesignator_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 7, 8, 3, 1, 6),
    _IbmRIFFilterOutRouteDesignator_Type()
)
ibmRIFFilterOutRouteDesignator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmRIFFilterOutRouteDesignator.setStatus("mandatory")
_Ibmfr_ObjectIdentity = ObjectIdentity
ibmfr = _Ibmfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8)
)
_IbmfrDlcmiTable_Object = MibTable
ibmfrDlcmiTable = _IbmfrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ibmfrDlcmiTable.setStatus("mandatory")
_IbmfrDlcmiEntry_Object = MibTableRow
ibmfrDlcmiEntry = _IbmfrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1)
)
ibmfrDlcmiEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmfrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    ibmfrDlcmiEntry.setStatus("mandatory")
_IbmfrDlcmiIfIndex_Type = Integer32
_IbmfrDlcmiIfIndex_Object = MibTableColumn
ibmfrDlcmiIfIndex = _IbmfrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 1),
    _IbmfrDlcmiIfIndex_Type()
)
ibmfrDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiIfIndex.setStatus("mandatory")


class _IbmfrDlcmiState_Type(Integer32):
    """Custom type ibmfrDlcmiState based on Integer32"""
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
        *(("ansiT1-617-B", 4),
          ("ansiT1-617-D", 3),
          ("lmiRev1", 2),
          ("noLmiConfigured", 1))
    )


_IbmfrDlcmiState_Type.__name__ = "Integer32"
_IbmfrDlcmiState_Object = MibTableColumn
ibmfrDlcmiState = _IbmfrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 2),
    _IbmfrDlcmiState_Type()
)
ibmfrDlcmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiState.setStatus("mandatory")


class _IbmfrDlcmiAddress_Type(Integer32):
    """Custom type ibmfrDlcmiAddress based on Integer32"""
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
        *(("q921", 1),
          ("q922", 4),
          ("q922March90", 2),
          ("q922November90", 3))
    )


_IbmfrDlcmiAddress_Type.__name__ = "Integer32"
_IbmfrDlcmiAddress_Object = MibTableColumn
ibmfrDlcmiAddress = _IbmfrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 3),
    _IbmfrDlcmiAddress_Type()
)
ibmfrDlcmiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiAddress.setStatus("mandatory")


class _IbmfrDlcmiAddressLen_Type(Integer32):
    """Custom type ibmfrDlcmiAddressLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("four-octets", 4),
          ("three-octets", 3),
          ("two-octets", 2))
    )


_IbmfrDlcmiAddressLen_Type.__name__ = "Integer32"
_IbmfrDlcmiAddressLen_Object = MibTableColumn
ibmfrDlcmiAddressLen = _IbmfrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 4),
    _IbmfrDlcmiAddressLen_Type()
)
ibmfrDlcmiAddressLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiAddressLen.setStatus("mandatory")


class _IbmfrDlcmiPollingInterval_Type(Integer32):
    """Custom type ibmfrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_IbmfrDlcmiPollingInterval_Type.__name__ = "Integer32"
_IbmfrDlcmiPollingInterval_Object = MibTableColumn
ibmfrDlcmiPollingInterval = _IbmfrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 5),
    _IbmfrDlcmiPollingInterval_Type()
)
ibmfrDlcmiPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiPollingInterval.setStatus("mandatory")


class _IbmfrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type ibmfrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmfrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_IbmfrDlcmiFullEnquiryInterval_Object = MibTableColumn
ibmfrDlcmiFullEnquiryInterval = _IbmfrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 6),
    _IbmfrDlcmiFullEnquiryInterval_Type()
)
ibmfrDlcmiFullEnquiryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiFullEnquiryInterval.setStatus("mandatory")


class _IbmfrDlcmiErrorThreshold_Type(Integer32):
    """Custom type ibmfrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmfrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_IbmfrDlcmiErrorThreshold_Object = MibTableColumn
ibmfrDlcmiErrorThreshold = _IbmfrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 7),
    _IbmfrDlcmiErrorThreshold_Type()
)
ibmfrDlcmiErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiErrorThreshold.setStatus("mandatory")


class _IbmfrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type ibmfrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmfrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_IbmfrDlcmiMonitoredEvents_Object = MibTableColumn
ibmfrDlcmiMonitoredEvents = _IbmfrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 8),
    _IbmfrDlcmiMonitoredEvents_Type()
)
ibmfrDlcmiMonitoredEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiMonitoredEvents.setStatus("mandatory")
_IbmfrDlcmiMaxSupportedVCs_Type = Integer32
_IbmfrDlcmiMaxSupportedVCs_Object = MibTableColumn
ibmfrDlcmiMaxSupportedVCs = _IbmfrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 9),
    _IbmfrDlcmiMaxSupportedVCs_Type()
)
ibmfrDlcmiMaxSupportedVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiMaxSupportedVCs.setStatus("mandatory")


class _IbmfrDlcmiMulticast_Type(Integer32):
    """Custom type ibmfrDlcmiMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("nonBroadcast", 1))
    )


_IbmfrDlcmiMulticast_Type.__name__ = "Integer32"
_IbmfrDlcmiMulticast_Object = MibTableColumn
ibmfrDlcmiMulticast = _IbmfrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 1, 1, 10),
    _IbmfrDlcmiMulticast_Type()
)
ibmfrDlcmiMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrDlcmiMulticast.setStatus("mandatory")
_IbmfrCircuitTable_Object = MibTable
ibmfrCircuitTable = _IbmfrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2)
)
if mibBuilder.loadTexts:
    ibmfrCircuitTable.setStatus("mandatory")
_IbmfrCircuitEntry_Object = MibTableRow
ibmfrCircuitEntry = _IbmfrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1)
)
ibmfrCircuitEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmfrCircuitIfIndex"),
    (0, "IBM6611-MIB", "ibmfrCircuitDlci"),
)
if mibBuilder.loadTexts:
    ibmfrCircuitEntry.setStatus("mandatory")
_IbmfrCircuitIfIndex_Type = Integer32
_IbmfrCircuitIfIndex_Object = MibTableColumn
ibmfrCircuitIfIndex = _IbmfrCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 1),
    _IbmfrCircuitIfIndex_Type()
)
ibmfrCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitIfIndex.setStatus("mandatory")
_IbmfrCircuitDlci_Type = Integer32
_IbmfrCircuitDlci_Object = MibTableColumn
ibmfrCircuitDlci = _IbmfrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 2),
    _IbmfrCircuitDlci_Type()
)
ibmfrCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitDlci.setStatus("mandatory")


class _IbmfrCircuitState_Type(Integer32):
    """Custom type ibmfrCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_IbmfrCircuitState_Type.__name__ = "Integer32"
_IbmfrCircuitState_Object = MibTableColumn
ibmfrCircuitState = _IbmfrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 3),
    _IbmfrCircuitState_Type()
)
ibmfrCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitState.setStatus("mandatory")
_IbmfrCircuitReceivedFECNs_Type = Counter32
_IbmfrCircuitReceivedFECNs_Object = MibTableColumn
ibmfrCircuitReceivedFECNs = _IbmfrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 4),
    _IbmfrCircuitReceivedFECNs_Type()
)
ibmfrCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitReceivedFECNs.setStatus("mandatory")
_IbmfrCircuitReceivedBECNs_Type = Counter32
_IbmfrCircuitReceivedBECNs_Object = MibTableColumn
ibmfrCircuitReceivedBECNs = _IbmfrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 5),
    _IbmfrCircuitReceivedBECNs_Type()
)
ibmfrCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitReceivedBECNs.setStatus("mandatory")
_IbmfrCircuitSentFrames_Type = Counter32
_IbmfrCircuitSentFrames_Object = MibTableColumn
ibmfrCircuitSentFrames = _IbmfrCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 6),
    _IbmfrCircuitSentFrames_Type()
)
ibmfrCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitSentFrames.setStatus("mandatory")
_IbmfrCircuitSentOctets_Type = Counter32
_IbmfrCircuitSentOctets_Object = MibTableColumn
ibmfrCircuitSentOctets = _IbmfrCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 7),
    _IbmfrCircuitSentOctets_Type()
)
ibmfrCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitSentOctets.setStatus("mandatory")
_IbmfrCircuitReceivedFrames_Type = Counter32
_IbmfrCircuitReceivedFrames_Object = MibTableColumn
ibmfrCircuitReceivedFrames = _IbmfrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 8),
    _IbmfrCircuitReceivedFrames_Type()
)
ibmfrCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitReceivedFrames.setStatus("mandatory")
_IbmfrCircuitReceivedOctets_Type = Counter32
_IbmfrCircuitReceivedOctets_Object = MibTableColumn
ibmfrCircuitReceivedOctets = _IbmfrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 9),
    _IbmfrCircuitReceivedOctets_Type()
)
ibmfrCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitReceivedOctets.setStatus("mandatory")
_IbmfrCircuitCreationTime_Type = TimeTicks
_IbmfrCircuitCreationTime_Object = MibTableColumn
ibmfrCircuitCreationTime = _IbmfrCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 10),
    _IbmfrCircuitCreationTime_Type()
)
ibmfrCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitCreationTime.setStatus("mandatory")
_IbmfrCircuitLastTimeChange_Type = TimeTicks
_IbmfrCircuitLastTimeChange_Object = MibTableColumn
ibmfrCircuitLastTimeChange = _IbmfrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 11),
    _IbmfrCircuitLastTimeChange_Type()
)
ibmfrCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitLastTimeChange.setStatus("mandatory")


class _IbmfrCircuitCommittedBurst_Type(Integer32):
    """Custom type ibmfrCircuitCommittedBurst based on Integer32"""
    defaultValue = 0


_IbmfrCircuitCommittedBurst_Object = MibTableColumn
ibmfrCircuitCommittedBurst = _IbmfrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 12),
    _IbmfrCircuitCommittedBurst_Type()
)
ibmfrCircuitCommittedBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitCommittedBurst.setStatus("mandatory")
_IbmfrCircuitExcessBurst_Type = Integer32
_IbmfrCircuitExcessBurst_Object = MibTableColumn
ibmfrCircuitExcessBurst = _IbmfrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 13),
    _IbmfrCircuitExcessBurst_Type()
)
ibmfrCircuitExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitExcessBurst.setStatus("mandatory")


class _IbmfrCircuitThroughput_Type(Integer32):
    """Custom type ibmfrCircuitThroughput based on Integer32"""
    defaultValue = 0


_IbmfrCircuitThroughput_Object = MibTableColumn
ibmfrCircuitThroughput = _IbmfrCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 2, 1, 14),
    _IbmfrCircuitThroughput_Type()
)
ibmfrCircuitThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrCircuitThroughput.setStatus("mandatory")
_IbmfrErrTable_Object = MibTable
ibmfrErrTable = _IbmfrErrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 3)
)
if mibBuilder.loadTexts:
    ibmfrErrTable.setStatus("mandatory")
_IbmfrErrEntry_Object = MibTableRow
ibmfrErrEntry = _IbmfrErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 3, 1)
)
ibmfrErrEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmfrErrIfIndex"),
)
if mibBuilder.loadTexts:
    ibmfrErrEntry.setStatus("mandatory")
_IbmfrErrIfIndex_Type = Integer32
_IbmfrErrIfIndex_Object = MibTableColumn
ibmfrErrIfIndex = _IbmfrErrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 3, 1, 1),
    _IbmfrErrIfIndex_Type()
)
ibmfrErrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrErrIfIndex.setStatus("mandatory")


class _IbmfrErrType_Type(Integer32):
    """Custom type ibmfrErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dlcmiProtoErr", 6),
          ("dlcmiSequenceErr", 8),
          ("dlcmiUnknownIE", 7),
          ("dlcmiUnknownRpt", 9),
          ("illegalDLCI", 4),
          ("receiveLong", 3),
          ("receiveShort", 2),
          ("unknownDLCI", 5),
          ("unknownError", 1))
    )


_IbmfrErrType_Type.__name__ = "Integer32"
_IbmfrErrType_Object = MibTableColumn
ibmfrErrType = _IbmfrErrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 3, 1, 2),
    _IbmfrErrType_Type()
)
ibmfrErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrErrType.setStatus("mandatory")
_IbmfrErrData_Type = OctetString
_IbmfrErrData_Object = MibTableColumn
ibmfrErrData = _IbmfrErrData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 3, 1, 3),
    _IbmfrErrData_Type()
)
ibmfrErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrErrData.setStatus("mandatory")
_IbmfrErrTime_Type = TimeTicks
_IbmfrErrTime_Object = MibTableColumn
ibmfrErrTime = _IbmfrErrTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 8, 3, 1, 4),
    _IbmfrErrTime_Type()
)
ibmfrErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrErrTime.setStatus("mandatory")
_Ibmdls_ObjectIdentity = ObjectIdentity
ibmdls = _Ibmdls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9)
)


class _IbmdlsVirtualRingSegmentNumber_Type(Integer32):
    """Custom type ibmdlsVirtualRingSegmentNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IbmdlsVirtualRingSegmentNumber_Type.__name__ = "Integer32"
_IbmdlsVirtualRingSegmentNumber_Object = MibScalar
ibmdlsVirtualRingSegmentNumber = _IbmdlsVirtualRingSegmentNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 1),
    _IbmdlsVirtualRingSegmentNumber_Type()
)
ibmdlsVirtualRingSegmentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsVirtualRingSegmentNumber.setStatus("mandatory")


class _IbmdlsFrameFilterType_Type(Integer32):
    """Custom type ibmdlsFrameFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmdlsFrameFilterType_Type.__name__ = "Integer32"
_IbmdlsFrameFilterType_Object = MibScalar
ibmdlsFrameFilterType = _IbmdlsFrameFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 2),
    _IbmdlsFrameFilterType_Type()
)
ibmdlsFrameFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsFrameFilterType.setStatus("mandatory")


class _IbmdlsNameFilterType_Type(Integer32):
    """Custom type ibmdlsNameFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmdlsNameFilterType_Type.__name__ = "Integer32"
_IbmdlsNameFilterType_Object = MibScalar
ibmdlsNameFilterType = _IbmdlsNameFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 3),
    _IbmdlsNameFilterType_Type()
)
ibmdlsNameFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsNameFilterType.setStatus("mandatory")
_IbmdlsRouterTable_Object = MibTable
ibmdlsRouterTable = _IbmdlsRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4)
)
if mibBuilder.loadTexts:
    ibmdlsRouterTable.setStatus("mandatory")
_IbmdlsRouterEntry_Object = MibTableRow
ibmdlsRouterEntry = _IbmdlsRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1)
)
ibmdlsRouterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsRouterAddress"),
)
if mibBuilder.loadTexts:
    ibmdlsRouterEntry.setStatus("mandatory")
_IbmdlsRouterAddress_Type = IpAddress
_IbmdlsRouterAddress_Object = MibTableColumn
ibmdlsRouterAddress = _IbmdlsRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 1),
    _IbmdlsRouterAddress_Type()
)
ibmdlsRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterAddress.setStatus("mandatory")


class _IbmdlsRouterStatus_Type(Integer32):
    """Custom type ibmdlsRouterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmdlsRouterStatus_Type.__name__ = "Integer32"
_IbmdlsRouterStatus_Object = MibTableColumn
ibmdlsRouterStatus = _IbmdlsRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 2),
    _IbmdlsRouterStatus_Type()
)
ibmdlsRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterStatus.setStatus("mandatory")


class _IbmdlsRouterDefinedBy_Type(Integer32):
    """Custom type ibmdlsRouterDefinedBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 2),
          ("user", 1))
    )


_IbmdlsRouterDefinedBy_Type.__name__ = "Integer32"
_IbmdlsRouterDefinedBy_Object = MibTableColumn
ibmdlsRouterDefinedBy = _IbmdlsRouterDefinedBy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 3),
    _IbmdlsRouterDefinedBy_Type()
)
ibmdlsRouterDefinedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterDefinedBy.setStatus("mandatory")
_IbmdlsRouterInFrames_Type = Counter32
_IbmdlsRouterInFrames_Object = MibTableColumn
ibmdlsRouterInFrames = _IbmdlsRouterInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 4),
    _IbmdlsRouterInFrames_Type()
)
ibmdlsRouterInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterInFrames.setStatus("mandatory")
_IbmdlsRouterOutFrames_Type = Counter32
_IbmdlsRouterOutFrames_Object = MibTableColumn
ibmdlsRouterOutFrames = _IbmdlsRouterOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 5),
    _IbmdlsRouterOutFrames_Type()
)
ibmdlsRouterOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterOutFrames.setStatus("mandatory")
_IbmdlsLocalFrameFilterTable_Object = MibTable
ibmdlsLocalFrameFilterTable = _IbmdlsLocalFrameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5)
)
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterTable.setStatus("mandatory")
_IbmdlsLocalFrameFilterEntry_Object = MibTableRow
ibmdlsLocalFrameFilterEntry = _IbmdlsLocalFrameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1)
)
ibmdlsLocalFrameFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsLocalFrameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterEntry.setStatus("mandatory")


class _IbmdlsLocalFrameFilterID_Type(Integer32):
    """Custom type ibmdlsLocalFrameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsLocalFrameFilterID_Type.__name__ = "Integer32"
_IbmdlsLocalFrameFilterID_Object = MibTableColumn
ibmdlsLocalFrameFilterID = _IbmdlsLocalFrameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 1),
    _IbmdlsLocalFrameFilterID_Type()
)
ibmdlsLocalFrameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterID.setStatus("mandatory")


class _IbmdlsLocalFrameFilterSrcAddress_Type(OctetString):
    """Custom type ibmdlsLocalFrameFilterSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsLocalFrameFilterSrcAddress_Type.__name__ = "OctetString"
_IbmdlsLocalFrameFilterSrcAddress_Object = MibTableColumn
ibmdlsLocalFrameFilterSrcAddress = _IbmdlsLocalFrameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 2),
    _IbmdlsLocalFrameFilterSrcAddress_Type()
)
ibmdlsLocalFrameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterSrcAddress.setStatus("mandatory")


class _IbmdlsLocalFrameFilterSrcMask_Type(OctetString):
    """Custom type ibmdlsLocalFrameFilterSrcMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsLocalFrameFilterSrcMask_Type.__name__ = "OctetString"
_IbmdlsLocalFrameFilterSrcMask_Object = MibTableColumn
ibmdlsLocalFrameFilterSrcMask = _IbmdlsLocalFrameFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 3),
    _IbmdlsLocalFrameFilterSrcMask_Type()
)
ibmdlsLocalFrameFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterSrcMask.setStatus("mandatory")


class _IbmdlsLocalFrameFilterDestAddress_Type(OctetString):
    """Custom type ibmdlsLocalFrameFilterDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsLocalFrameFilterDestAddress_Type.__name__ = "OctetString"
_IbmdlsLocalFrameFilterDestAddress_Object = MibTableColumn
ibmdlsLocalFrameFilterDestAddress = _IbmdlsLocalFrameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 4),
    _IbmdlsLocalFrameFilterDestAddress_Type()
)
ibmdlsLocalFrameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterDestAddress.setStatus("mandatory")


class _IbmdlsLocalFrameFilterDestMask_Type(OctetString):
    """Custom type ibmdlsLocalFrameFilterDestMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsLocalFrameFilterDestMask_Type.__name__ = "OctetString"
_IbmdlsLocalFrameFilterDestMask_Object = MibTableColumn
ibmdlsLocalFrameFilterDestMask = _IbmdlsLocalFrameFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 5),
    _IbmdlsLocalFrameFilterDestMask_Type()
)
ibmdlsLocalFrameFilterDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterDestMask.setStatus("mandatory")
_IbmdlsRemoteFrameFilterTable_Object = MibTable
ibmdlsRemoteFrameFilterTable = _IbmdlsRemoteFrameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6)
)
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterTable.setStatus("mandatory")
_IbmdlsRemoteFrameFilterEntry_Object = MibTableRow
ibmdlsRemoteFrameFilterEntry = _IbmdlsRemoteFrameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1)
)
ibmdlsRemoteFrameFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsRemoteFrameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterEntry.setStatus("mandatory")


class _IbmdlsRemoteFrameFilterID_Type(Integer32):
    """Custom type ibmdlsRemoteFrameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsRemoteFrameFilterID_Type.__name__ = "Integer32"
_IbmdlsRemoteFrameFilterID_Object = MibTableColumn
ibmdlsRemoteFrameFilterID = _IbmdlsRemoteFrameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 1),
    _IbmdlsRemoteFrameFilterID_Type()
)
ibmdlsRemoteFrameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterID.setStatus("mandatory")


class _IbmdlsRemoteFrameFilterSrcAddress_Type(OctetString):
    """Custom type ibmdlsRemoteFrameFilterSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsRemoteFrameFilterSrcAddress_Type.__name__ = "OctetString"
_IbmdlsRemoteFrameFilterSrcAddress_Object = MibTableColumn
ibmdlsRemoteFrameFilterSrcAddress = _IbmdlsRemoteFrameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 2),
    _IbmdlsRemoteFrameFilterSrcAddress_Type()
)
ibmdlsRemoteFrameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterSrcAddress.setStatus("mandatory")


class _IbmdlsRemoteFrameFilterSrcMask_Type(OctetString):
    """Custom type ibmdlsRemoteFrameFilterSrcMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsRemoteFrameFilterSrcMask_Type.__name__ = "OctetString"
_IbmdlsRemoteFrameFilterSrcMask_Object = MibTableColumn
ibmdlsRemoteFrameFilterSrcMask = _IbmdlsRemoteFrameFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 3),
    _IbmdlsRemoteFrameFilterSrcMask_Type()
)
ibmdlsRemoteFrameFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterSrcMask.setStatus("mandatory")


class _IbmdlsRemoteFrameFilterDestAddress_Type(OctetString):
    """Custom type ibmdlsRemoteFrameFilterDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsRemoteFrameFilterDestAddress_Type.__name__ = "OctetString"
_IbmdlsRemoteFrameFilterDestAddress_Object = MibTableColumn
ibmdlsRemoteFrameFilterDestAddress = _IbmdlsRemoteFrameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 4),
    _IbmdlsRemoteFrameFilterDestAddress_Type()
)
ibmdlsRemoteFrameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterDestAddress.setStatus("mandatory")


class _IbmdlsRemoteFrameFilterDestMask_Type(OctetString):
    """Custom type ibmdlsRemoteFrameFilterDestMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsRemoteFrameFilterDestMask_Type.__name__ = "OctetString"
_IbmdlsRemoteFrameFilterDestMask_Object = MibTableColumn
ibmdlsRemoteFrameFilterDestMask = _IbmdlsRemoteFrameFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 5),
    _IbmdlsRemoteFrameFilterDestMask_Type()
)
ibmdlsRemoteFrameFilterDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterDestMask.setStatus("mandatory")
_IbmdlsLocalNameFilterTable_Object = MibTable
ibmdlsLocalNameFilterTable = _IbmdlsLocalNameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7)
)
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterTable.setStatus("mandatory")
_IbmdlsLocalNameFilterEntry_Object = MibTableRow
ibmdlsLocalNameFilterEntry = _IbmdlsLocalNameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1)
)
ibmdlsLocalNameFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsLocalNameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterEntry.setStatus("mandatory")


class _IbmdlsLocalNameFilterID_Type(Integer32):
    """Custom type ibmdlsLocalNameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsLocalNameFilterID_Type.__name__ = "Integer32"
_IbmdlsLocalNameFilterID_Object = MibTableColumn
ibmdlsLocalNameFilterID = _IbmdlsLocalNameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 1),
    _IbmdlsLocalNameFilterID_Type()
)
ibmdlsLocalNameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterID.setStatus("mandatory")


class _IbmdlsLocalNameFilterSrcAddress_Type(DisplayString):
    """Custom type ibmdlsLocalNameFilterSrcAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsLocalNameFilterSrcAddress_Type.__name__ = "DisplayString"
_IbmdlsLocalNameFilterSrcAddress_Object = MibTableColumn
ibmdlsLocalNameFilterSrcAddress = _IbmdlsLocalNameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 2),
    _IbmdlsLocalNameFilterSrcAddress_Type()
)
ibmdlsLocalNameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterSrcAddress.setStatus("mandatory")


class _IbmdlsLocalNameFilterDestAddress_Type(DisplayString):
    """Custom type ibmdlsLocalNameFilterDestAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsLocalNameFilterDestAddress_Type.__name__ = "DisplayString"
_IbmdlsLocalNameFilterDestAddress_Object = MibTableColumn
ibmdlsLocalNameFilterDestAddress = _IbmdlsLocalNameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 3),
    _IbmdlsLocalNameFilterDestAddress_Type()
)
ibmdlsLocalNameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterDestAddress.setStatus("mandatory")
_IbmdlsRemoteNameFilterTable_Object = MibTable
ibmdlsRemoteNameFilterTable = _IbmdlsRemoteNameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8)
)
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterTable.setStatus("mandatory")
_IbmdlsRemoteNameFilterEntry_Object = MibTableRow
ibmdlsRemoteNameFilterEntry = _IbmdlsRemoteNameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1)
)
ibmdlsRemoteNameFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsRemoteNameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterEntry.setStatus("mandatory")


class _IbmdlsRemoteNameFilterID_Type(Integer32):
    """Custom type ibmdlsRemoteNameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsRemoteNameFilterID_Type.__name__ = "Integer32"
_IbmdlsRemoteNameFilterID_Object = MibTableColumn
ibmdlsRemoteNameFilterID = _IbmdlsRemoteNameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 1),
    _IbmdlsRemoteNameFilterID_Type()
)
ibmdlsRemoteNameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterID.setStatus("mandatory")


class _IbmdlsRemoteNameFilterSrcAddress_Type(DisplayString):
    """Custom type ibmdlsRemoteNameFilterSrcAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsRemoteNameFilterSrcAddress_Type.__name__ = "DisplayString"
_IbmdlsRemoteNameFilterSrcAddress_Object = MibTableColumn
ibmdlsRemoteNameFilterSrcAddress = _IbmdlsRemoteNameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 2),
    _IbmdlsRemoteNameFilterSrcAddress_Type()
)
ibmdlsRemoteNameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterSrcAddress.setStatus("mandatory")


class _IbmdlsRemoteNameFilterDestAddress_Type(DisplayString):
    """Custom type ibmdlsRemoteNameFilterDestAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsRemoteNameFilterDestAddress_Type.__name__ = "DisplayString"
_IbmdlsRemoteNameFilterDestAddress_Object = MibTableColumn
ibmdlsRemoteNameFilterDestAddress = _IbmdlsRemoteNameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 3),
    _IbmdlsRemoteNameFilterDestAddress_Type()
)
ibmdlsRemoteNameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterDestAddress.setStatus("mandatory")
_IbmdlsDefaultDestTable_Object = MibTable
ibmdlsDefaultDestTable = _IbmdlsDefaultDestTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9)
)
if mibBuilder.loadTexts:
    ibmdlsDefaultDestTable.setStatus("mandatory")
_IbmdlsDefaultDestEntry_Object = MibTableRow
ibmdlsDefaultDestEntry = _IbmdlsDefaultDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1)
)
ibmdlsDefaultDestEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsDefaultDestAddress"),
)
if mibBuilder.loadTexts:
    ibmdlsDefaultDestEntry.setStatus("mandatory")


class _IbmdlsDefaultDestAddress_Type(OctetString):
    """Custom type ibmdlsDefaultDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsDefaultDestAddress_Type.__name__ = "OctetString"
_IbmdlsDefaultDestAddress_Object = MibTableColumn
ibmdlsDefaultDestAddress = _IbmdlsDefaultDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1, 1),
    _IbmdlsDefaultDestAddress_Type()
)
ibmdlsDefaultDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultDestAddress.setStatus("mandatory")
_IbmdlsDefaultRouterAddress_Type = IpAddress
_IbmdlsDefaultRouterAddress_Object = MibTableColumn
ibmdlsDefaultRouterAddress = _IbmdlsDefaultRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1, 2),
    _IbmdlsDefaultRouterAddress_Type()
)
ibmdlsDefaultRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultRouterAddress.setStatus("mandatory")
_IbmdlsDefaultNBDestTable_Object = MibTable
ibmdlsDefaultNBDestTable = _IbmdlsDefaultNBDestTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10)
)
if mibBuilder.loadTexts:
    ibmdlsDefaultNBDestTable.setStatus("mandatory")
_IbmdlsDefaultNBDestEntry_Object = MibTableRow
ibmdlsDefaultNBDestEntry = _IbmdlsDefaultNBDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1)
)
ibmdlsDefaultNBDestEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsDefaultNBDestName"),
)
if mibBuilder.loadTexts:
    ibmdlsDefaultNBDestEntry.setStatus("mandatory")


class _IbmdlsDefaultNBDestName_Type(DisplayString):
    """Custom type ibmdlsDefaultNBDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsDefaultNBDestName_Type.__name__ = "DisplayString"
_IbmdlsDefaultNBDestName_Object = MibTableColumn
ibmdlsDefaultNBDestName = _IbmdlsDefaultNBDestName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1, 1),
    _IbmdlsDefaultNBDestName_Type()
)
ibmdlsDefaultNBDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultNBDestName.setStatus("mandatory")
_IbmdlsDefaultNBRouterAddress_Type = IpAddress
_IbmdlsDefaultNBRouterAddress_Object = MibTableColumn
ibmdlsDefaultNBRouterAddress = _IbmdlsDefaultNBRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1, 2),
    _IbmdlsDefaultNBRouterAddress_Type()
)
ibmdlsDefaultNBRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultNBRouterAddress.setStatus("mandatory")
_IbmdlsStationTable_Object = MibTable
ibmdlsStationTable = _IbmdlsStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11)
)
if mibBuilder.loadTexts:
    ibmdlsStationTable.setStatus("mandatory")
_IbmdlsStationEntry_Object = MibTableRow
ibmdlsStationEntry = _IbmdlsStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1)
)
ibmdlsStationEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsStationIfIndex"),
    (0, "IBM6611-MIB", "ibmdlsStationAddress"),
)
if mibBuilder.loadTexts:
    ibmdlsStationEntry.setStatus("mandatory")
_IbmdlsStationIfIndex_Type = Integer32
_IbmdlsStationIfIndex_Object = MibTableColumn
ibmdlsStationIfIndex = _IbmdlsStationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 1),
    _IbmdlsStationIfIndex_Type()
)
ibmdlsStationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationIfIndex.setStatus("mandatory")


class _IbmdlsStationAddress_Type(Integer32):
    """Custom type ibmdlsStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmdlsStationAddress_Type.__name__ = "Integer32"
_IbmdlsStationAddress_Object = MibTableColumn
ibmdlsStationAddress = _IbmdlsStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 2),
    _IbmdlsStationAddress_Type()
)
ibmdlsStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationAddress.setStatus("mandatory")


class _IbmdlsStationTransmitWindowCount_Type(Integer32):
    """Custom type ibmdlsStationTransmitWindowCount based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IbmdlsStationTransmitWindowCount_Type.__name__ = "Integer32"
_IbmdlsStationTransmitWindowCount_Object = MibTableColumn
ibmdlsStationTransmitWindowCount = _IbmdlsStationTransmitWindowCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 3),
    _IbmdlsStationTransmitWindowCount_Type()
)
ibmdlsStationTransmitWindowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationTransmitWindowCount.setStatus("mandatory")


class _IbmdlsStationRetransmitCount_Type(Integer32):
    """Custom type ibmdlsStationRetransmitCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_IbmdlsStationRetransmitCount_Type.__name__ = "Integer32"
_IbmdlsStationRetransmitCount_Object = MibTableColumn
ibmdlsStationRetransmitCount = _IbmdlsStationRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 4),
    _IbmdlsStationRetransmitCount_Type()
)
ibmdlsStationRetransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationRetransmitCount.setStatus("mandatory")


class _IbmdlsStationRetransmitThreshold_Type(Integer32):
    """Custom type ibmdlsStationRetransmitThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsStationRetransmitThreshold_Type.__name__ = "Integer32"
_IbmdlsStationRetransmitThreshold_Object = MibTableColumn
ibmdlsStationRetransmitThreshold = _IbmdlsStationRetransmitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 5),
    _IbmdlsStationRetransmitThreshold_Type()
)
ibmdlsStationRetransmitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationRetransmitThreshold.setStatus("mandatory")


class _IbmdlsStationForceDisconnectTimeout_Type(Integer32):
    """Custom type ibmdlsStationForceDisconnectTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_IbmdlsStationForceDisconnectTimeout_Type.__name__ = "Integer32"
_IbmdlsStationForceDisconnectTimeout_Object = MibTableColumn
ibmdlsStationForceDisconnectTimeout = _IbmdlsStationForceDisconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 6),
    _IbmdlsStationForceDisconnectTimeout_Type()
)
ibmdlsStationForceDisconnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationForceDisconnectTimeout.setStatus("mandatory")


class _IbmdlsStationMaxIfieldSize_Type(Integer32):
    """Custom type ibmdlsStationMaxIfieldSize based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(265, 30729),
    )


_IbmdlsStationMaxIfieldSize_Type.__name__ = "Integer32"
_IbmdlsStationMaxIfieldSize_Object = MibTableColumn
ibmdlsStationMaxIfieldSize = _IbmdlsStationMaxIfieldSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 7),
    _IbmdlsStationMaxIfieldSize_Type()
)
ibmdlsStationMaxIfieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationMaxIfieldSize.setStatus("mandatory")


class _IbmdlsStationPrimaryRepollTimeout_Type(Integer32):
    """Custom type ibmdlsStationPrimaryRepollTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_IbmdlsStationPrimaryRepollTimeout_Type.__name__ = "Integer32"
_IbmdlsStationPrimaryRepollTimeout_Object = MibTableColumn
ibmdlsStationPrimaryRepollTimeout = _IbmdlsStationPrimaryRepollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 8),
    _IbmdlsStationPrimaryRepollTimeout_Type()
)
ibmdlsStationPrimaryRepollTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimaryRepollTimeout.setStatus("mandatory")


class _IbmdlsStationPrimaryRepollCount_Type(Integer32):
    """Custom type ibmdlsStationPrimaryRepollCount based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_IbmdlsStationPrimaryRepollCount_Type.__name__ = "Integer32"
_IbmdlsStationPrimaryRepollCount_Object = MibTableColumn
ibmdlsStationPrimaryRepollCount = _IbmdlsStationPrimaryRepollCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 9),
    _IbmdlsStationPrimaryRepollCount_Type()
)
ibmdlsStationPrimaryRepollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimaryRepollCount.setStatus("mandatory")


class _IbmdlsStationPrimaryRepollThreshold_Type(Integer32):
    """Custom type ibmdlsStationPrimaryRepollThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsStationPrimaryRepollThreshold_Type.__name__ = "Integer32"
_IbmdlsStationPrimaryRepollThreshold_Object = MibTableColumn
ibmdlsStationPrimaryRepollThreshold = _IbmdlsStationPrimaryRepollThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 10),
    _IbmdlsStationPrimaryRepollThreshold_Type()
)
ibmdlsStationPrimaryRepollThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimaryRepollThreshold.setStatus("mandatory")


class _IbmdlsStationPrimarySlowListTimeout_Type(Integer32):
    """Custom type ibmdlsStationPrimarySlowListTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IbmdlsStationPrimarySlowListTimeout_Type.__name__ = "Integer32"
_IbmdlsStationPrimarySlowListTimeout_Object = MibTableColumn
ibmdlsStationPrimarySlowListTimeout = _IbmdlsStationPrimarySlowListTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 11),
    _IbmdlsStationPrimarySlowListTimeout_Type()
)
ibmdlsStationPrimarySlowListTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimarySlowListTimeout.setStatus("mandatory")


class _IbmdlsStationSrcAddress_Type(OctetString):
    """Custom type ibmdlsStationSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsStationSrcAddress_Type.__name__ = "OctetString"
_IbmdlsStationSrcAddress_Object = MibTableColumn
ibmdlsStationSrcAddress = _IbmdlsStationSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 12),
    _IbmdlsStationSrcAddress_Type()
)
ibmdlsStationSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationSrcAddress.setStatus("mandatory")


class _IbmdlsStationDestAddress_Type(OctetString):
    """Custom type ibmdlsStationDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsStationDestAddress_Type.__name__ = "OctetString"
_IbmdlsStationDestAddress_Object = MibTableColumn
ibmdlsStationDestAddress = _IbmdlsStationDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 13),
    _IbmdlsStationDestAddress_Type()
)
ibmdlsStationDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationDestAddress.setStatus("mandatory")
_IbmdlsCirTable_Object = MibTable
ibmdlsCirTable = _IbmdlsCirTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12)
)
if mibBuilder.loadTexts:
    ibmdlsCirTable.setStatus("mandatory")
_IbmdlsCirEntry_Object = MibTableRow
ibmdlsCirEntry = _IbmdlsCirEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1)
)
ibmdlsCirEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdlsCirIfIndex"),
    (0, "IBM6611-MIB", "ibmdlsCirSrcAddress"),
    (0, "IBM6611-MIB", "ibmdlsCirSrcSap"),
    (0, "IBM6611-MIB", "ibmdlsCirDestAddress"),
    (0, "IBM6611-MIB", "ibmdlsCirDestSap"),
)
if mibBuilder.loadTexts:
    ibmdlsCirEntry.setStatus("mandatory")
_IbmdlsCirIfIndex_Type = Integer32
_IbmdlsCirIfIndex_Object = MibTableColumn
ibmdlsCirIfIndex = _IbmdlsCirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 1),
    _IbmdlsCirIfIndex_Type()
)
ibmdlsCirIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirIfIndex.setStatus("mandatory")


class _IbmdlsCirSrcAddress_Type(OctetString):
    """Custom type ibmdlsCirSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsCirSrcAddress_Type.__name__ = "OctetString"
_IbmdlsCirSrcAddress_Object = MibTableColumn
ibmdlsCirSrcAddress = _IbmdlsCirSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 2),
    _IbmdlsCirSrcAddress_Type()
)
ibmdlsCirSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirSrcAddress.setStatus("mandatory")
_IbmdlsCirSrcSap_Type = Integer32
_IbmdlsCirSrcSap_Object = MibTableColumn
ibmdlsCirSrcSap = _IbmdlsCirSrcSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 3),
    _IbmdlsCirSrcSap_Type()
)
ibmdlsCirSrcSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirSrcSap.setStatus("mandatory")


class _IbmdlsCirDestAddress_Type(OctetString):
    """Custom type ibmdlsCirDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdlsCirDestAddress_Type.__name__ = "OctetString"
_IbmdlsCirDestAddress_Object = MibTableColumn
ibmdlsCirDestAddress = _IbmdlsCirDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 4),
    _IbmdlsCirDestAddress_Type()
)
ibmdlsCirDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirDestAddress.setStatus("mandatory")
_IbmdlsCirDestSap_Type = Integer32
_IbmdlsCirDestSap_Object = MibTableColumn
ibmdlsCirDestSap = _IbmdlsCirDestSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 5),
    _IbmdlsCirDestSap_Type()
)
ibmdlsCirDestSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirDestSap.setStatus("mandatory")
_IbmdlsCirPartnerRouterAddress_Type = IpAddress
_IbmdlsCirPartnerRouterAddress_Object = MibTableColumn
ibmdlsCirPartnerRouterAddress = _IbmdlsCirPartnerRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 6),
    _IbmdlsCirPartnerRouterAddress_Type()
)
ibmdlsCirPartnerRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirPartnerRouterAddress.setStatus("mandatory")


class _IbmdlsCirLocalLinkState_Type(Integer32):
    """Custom type ibmdlsCirLocalLinkState based on Integer32"""
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
        *(("closing", 3),
          ("inactive", 4),
          ("opened", 2),
          ("opening", 1))
    )


_IbmdlsCirLocalLinkState_Type.__name__ = "Integer32"
_IbmdlsCirLocalLinkState_Object = MibTableColumn
ibmdlsCirLocalLinkState = _IbmdlsCirLocalLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 7),
    _IbmdlsCirLocalLinkState_Type()
)
ibmdlsCirLocalLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkState.setStatus("mandatory")


class _IbmdlsCirLocalLinkSubState_Type(Integer32):
    """Custom type ibmdlsCirLocalLinkSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("calling", 1),
          ("contacted", 3),
          ("listening", 2),
          ("localBusy", 4),
          ("remoteBusy", 5))
    )


_IbmdlsCirLocalLinkSubState_Type.__name__ = "Integer32"
_IbmdlsCirLocalLinkSubState_Object = MibTableColumn
ibmdlsCirLocalLinkSubState = _IbmdlsCirLocalLinkSubState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 8),
    _IbmdlsCirLocalLinkSubState_Type()
)
ibmdlsCirLocalLinkSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkSubState.setStatus("mandatory")


class _IbmdlsCirLocalLinkRouting_Type(OctetString):
    """Custom type ibmdlsCirLocalLinkRouting based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 18),
    )


_IbmdlsCirLocalLinkRouting_Type.__name__ = "OctetString"
_IbmdlsCirLocalLinkRouting_Object = MibTableColumn
ibmdlsCirLocalLinkRouting = _IbmdlsCirLocalLinkRouting_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 9),
    _IbmdlsCirLocalLinkRouting_Type()
)
ibmdlsCirLocalLinkRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkRouting.setStatus("mandatory")
_IbmdlsCirLocalLinkTestCmdsSent_Type = Counter32
_IbmdlsCirLocalLinkTestCmdsSent_Object = MibTableColumn
ibmdlsCirLocalLinkTestCmdsSent = _IbmdlsCirLocalLinkTestCmdsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 10),
    _IbmdlsCirLocalLinkTestCmdsSent_Type()
)
ibmdlsCirLocalLinkTestCmdsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkTestCmdsSent.setStatus("mandatory")
_IbmdlsCirLocalLinkTestCmdsFail_Type = Counter32
_IbmdlsCirLocalLinkTestCmdsFail_Object = MibTableColumn
ibmdlsCirLocalLinkTestCmdsFail = _IbmdlsCirLocalLinkTestCmdsFail_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 11),
    _IbmdlsCirLocalLinkTestCmdsFail_Type()
)
ibmdlsCirLocalLinkTestCmdsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkTestCmdsFail.setStatus("mandatory")
_IbmdlsCirLocalLinkTestCmdsRcv_Type = Counter32
_IbmdlsCirLocalLinkTestCmdsRcv_Object = MibTableColumn
ibmdlsCirLocalLinkTestCmdsRcv = _IbmdlsCirLocalLinkTestCmdsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 12),
    _IbmdlsCirLocalLinkTestCmdsRcv_Type()
)
ibmdlsCirLocalLinkTestCmdsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkTestCmdsRcv.setStatus("mandatory")
_IbmdlsCirLocalLinkDataPktSent_Type = Counter32
_IbmdlsCirLocalLinkDataPktSent_Object = MibTableColumn
ibmdlsCirLocalLinkDataPktSent = _IbmdlsCirLocalLinkDataPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 13),
    _IbmdlsCirLocalLinkDataPktSent_Type()
)
ibmdlsCirLocalLinkDataPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkDataPktSent.setStatus("mandatory")
_IbmdlsCirLocalLinkDataPktResent_Type = Counter32
_IbmdlsCirLocalLinkDataPktResent_Object = MibTableColumn
ibmdlsCirLocalLinkDataPktResent = _IbmdlsCirLocalLinkDataPktResent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 14),
    _IbmdlsCirLocalLinkDataPktResent_Type()
)
ibmdlsCirLocalLinkDataPktResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkDataPktResent.setStatus("mandatory")
_IbmdlsCirLocalLinkMaxContResent_Type = Counter32
_IbmdlsCirLocalLinkMaxContResent_Object = MibTableColumn
ibmdlsCirLocalLinkMaxContResent = _IbmdlsCirLocalLinkMaxContResent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 15),
    _IbmdlsCirLocalLinkMaxContResent_Type()
)
ibmdlsCirLocalLinkMaxContResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkMaxContResent.setStatus("mandatory")
_IbmdlsCirLocalLinkDataPktRcv_Type = Counter32
_IbmdlsCirLocalLinkDataPktRcv_Object = MibTableColumn
ibmdlsCirLocalLinkDataPktRcv = _IbmdlsCirLocalLinkDataPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 16),
    _IbmdlsCirLocalLinkDataPktRcv_Type()
)
ibmdlsCirLocalLinkDataPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkDataPktRcv.setStatus("mandatory")
_IbmdlsCirLocalLinkInvalidPktRcv_Type = Counter32
_IbmdlsCirLocalLinkInvalidPktRcv_Object = MibTableColumn
ibmdlsCirLocalLinkInvalidPktRcv = _IbmdlsCirLocalLinkInvalidPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 17),
    _IbmdlsCirLocalLinkInvalidPktRcv_Type()
)
ibmdlsCirLocalLinkInvalidPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkInvalidPktRcv.setStatus("mandatory")
_IbmdlsCirLocalLinkAdpRcvErr_Type = Counter32
_IbmdlsCirLocalLinkAdpRcvErr_Object = MibTableColumn
ibmdlsCirLocalLinkAdpRcvErr = _IbmdlsCirLocalLinkAdpRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 18),
    _IbmdlsCirLocalLinkAdpRcvErr_Type()
)
ibmdlsCirLocalLinkAdpRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkAdpRcvErr.setStatus("mandatory")
_IbmdlsCirLocalLinkAdpSendErr_Type = Counter32
_IbmdlsCirLocalLinkAdpSendErr_Object = MibTableColumn
ibmdlsCirLocalLinkAdpSendErr = _IbmdlsCirLocalLinkAdpSendErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 19),
    _IbmdlsCirLocalLinkAdpSendErr_Type()
)
ibmdlsCirLocalLinkAdpSendErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkAdpSendErr.setStatus("mandatory")
_IbmdlsCirLocalLinkRcvInactiveTimeouts_Type = Counter32
_IbmdlsCirLocalLinkRcvInactiveTimeouts_Object = MibTableColumn
ibmdlsCirLocalLinkRcvInactiveTimeouts = _IbmdlsCirLocalLinkRcvInactiveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 20),
    _IbmdlsCirLocalLinkRcvInactiveTimeouts_Type()
)
ibmdlsCirLocalLinkRcvInactiveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkRcvInactiveTimeouts.setStatus("mandatory")
_IbmdlsCirLocalLinkCmdPollsSent_Type = Counter32
_IbmdlsCirLocalLinkCmdPollsSent_Object = MibTableColumn
ibmdlsCirLocalLinkCmdPollsSent = _IbmdlsCirLocalLinkCmdPollsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 21),
    _IbmdlsCirLocalLinkCmdPollsSent_Type()
)
ibmdlsCirLocalLinkCmdPollsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkCmdPollsSent.setStatus("mandatory")
_IbmdlsCirLocalLinkCmdRepollsSent_Type = Counter32
_IbmdlsCirLocalLinkCmdRepollsSent_Object = MibTableColumn
ibmdlsCirLocalLinkCmdRepollsSent = _IbmdlsCirLocalLinkCmdRepollsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 22),
    _IbmdlsCirLocalLinkCmdRepollsSent_Type()
)
ibmdlsCirLocalLinkCmdRepollsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkCmdRepollsSent.setStatus("mandatory")
_IbmdlsCirLocalLinkCmdContRepolls_Type = Counter32
_IbmdlsCirLocalLinkCmdContRepolls_Object = MibTableColumn
ibmdlsCirLocalLinkCmdContRepolls = _IbmdlsCirLocalLinkCmdContRepolls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 23),
    _IbmdlsCirLocalLinkCmdContRepolls_Type()
)
ibmdlsCirLocalLinkCmdContRepolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkCmdContRepolls.setStatus("mandatory")


class _IbmdlsCirLocalAddress_Type(Integer32):
    """Custom type ibmdlsCirLocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destinationIsLocal", 2),
          ("sourceIsLocal", 1))
    )


_IbmdlsCirLocalAddress_Type.__name__ = "Integer32"
_IbmdlsCirLocalAddress_Object = MibTableColumn
ibmdlsCirLocalAddress = _IbmdlsCirLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 24),
    _IbmdlsCirLocalAddress_Type()
)
ibmdlsCirLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalAddress.setStatus("mandatory")


class _IbmdlsCirLocalConnectionState_Type(Integer32):
    """Custom type ibmdlsCirLocalConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connected", 5),
          ("contactPending", 2),
          ("contacted", 3),
          ("discontactPending", 4),
          ("discontacted", 1))
    )


_IbmdlsCirLocalConnectionState_Type.__name__ = "Integer32"
_IbmdlsCirLocalConnectionState_Object = MibTableColumn
ibmdlsCirLocalConnectionState = _IbmdlsCirLocalConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 25),
    _IbmdlsCirLocalConnectionState_Type()
)
ibmdlsCirLocalConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalConnectionState.setStatus("mandatory")
_Ibmppp_ObjectIdentity = ObjectIdentity
ibmppp = _Ibmppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10)
)
_IbmpppLinkControlTable_Object = MibTable
ibmpppLinkControlTable = _IbmpppLinkControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1)
)
if mibBuilder.loadTexts:
    ibmpppLinkControlTable.setStatus("mandatory")
_IbmpppLinkControlEntry_Object = MibTableRow
ibmpppLinkControlEntry = _IbmpppLinkControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1)
)
ibmpppLinkControlEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmpppLinkControlIndex"),
)
if mibBuilder.loadTexts:
    ibmpppLinkControlEntry.setStatus("mandatory")
_IbmpppLinkControlIndex_Type = Integer32
_IbmpppLinkControlIndex_Object = MibTableColumn
ibmpppLinkControlIndex = _IbmpppLinkControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 1),
    _IbmpppLinkControlIndex_Type()
)
ibmpppLinkControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkControlIndex.setStatus("mandatory")


class _IbmpppLinkCRCSize_Type(Integer32):
    """Custom type ibmpppLinkCRCSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ppp-crc-16", 16),
          ("ppp-crc-32", 32))
    )


_IbmpppLinkCRCSize_Type.__name__ = "Integer32"
_IbmpppLinkCRCSize_Object = MibTableColumn
ibmpppLinkCRCSize = _IbmpppLinkCRCSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 2),
    _IbmpppLinkCRCSize_Type()
)
ibmpppLinkCRCSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkCRCSize.setStatus("mandatory")
_IbmpppLinkRestartTimerValue_Type = Integer32
_IbmpppLinkRestartTimerValue_Object = MibTableColumn
ibmpppLinkRestartTimerValue = _IbmpppLinkRestartTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 3),
    _IbmpppLinkRestartTimerValue_Type()
)
ibmpppLinkRestartTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkRestartTimerValue.setStatus("mandatory")
_IbmpppLinkMaxRestarts_Type = Integer32
_IbmpppLinkMaxRestarts_Object = MibTableColumn
ibmpppLinkMaxRestarts = _IbmpppLinkMaxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 4),
    _IbmpppLinkMaxRestarts_Type()
)
ibmpppLinkMaxRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkMaxRestarts.setStatus("mandatory")
_IbmpppLinkLocalMRU_Type = Integer32
_IbmpppLinkLocalMRU_Object = MibTableColumn
ibmpppLinkLocalMRU = _IbmpppLinkLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 5),
    _IbmpppLinkLocalMRU_Type()
)
ibmpppLinkLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLocalMRU.setStatus("mandatory")
_IbmpppLinkRemoteMRU_Type = Integer32
_IbmpppLinkRemoteMRU_Object = MibTableColumn
ibmpppLinkRemoteMRU = _IbmpppLinkRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 6),
    _IbmpppLinkRemoteMRU_Type()
)
ibmpppLinkRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkRemoteMRU.setStatus("mandatory")


class _IbmpppLinkLocalACCMap_Type(OctetString):
    """Custom type ibmpppLinkLocalACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmpppLinkLocalACCMap_Type.__name__ = "OctetString"
_IbmpppLinkLocalACCMap_Object = MibTableColumn
ibmpppLinkLocalACCMap = _IbmpppLinkLocalACCMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 7),
    _IbmpppLinkLocalACCMap_Type()
)
ibmpppLinkLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLocalACCMap.setStatus("mandatory")


class _IbmpppLinkRemoteACCMap_Type(OctetString):
    """Custom type ibmpppLinkRemoteACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmpppLinkRemoteACCMap_Type.__name__ = "OctetString"
_IbmpppLinkRemoteACCMap_Object = MibTableColumn
ibmpppLinkRemoteACCMap = _IbmpppLinkRemoteACCMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 8),
    _IbmpppLinkRemoteACCMap_Type()
)
ibmpppLinkRemoteACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkRemoteACCMap.setStatus("mandatory")
_IbmpppLinkMagicLoopCount_Type = Integer32
_IbmpppLinkMagicLoopCount_Object = MibTableColumn
ibmpppLinkMagicLoopCount = _IbmpppLinkMagicLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 9),
    _IbmpppLinkMagicLoopCount_Type()
)
ibmpppLinkMagicLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkMagicLoopCount.setStatus("mandatory")


class _IbmpppLinkCommand_Type(Integer32):
    """Custom type ibmpppLinkCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("no-op", 1))
    )


_IbmpppLinkCommand_Type.__name__ = "Integer32"
_IbmpppLinkCommand_Object = MibTableColumn
ibmpppLinkCommand = _IbmpppLinkCommand_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 1, 1, 10),
    _IbmpppLinkCommand_Type()
)
ibmpppLinkCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkCommand.setStatus("mandatory")
_IbmpppLinkStatusTable_Object = MibTable
ibmpppLinkStatusTable = _IbmpppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2)
)
if mibBuilder.loadTexts:
    ibmpppLinkStatusTable.setStatus("mandatory")
_IbmpppLinkStatusEntry_Object = MibTableRow
ibmpppLinkStatusEntry = _IbmpppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1)
)
ibmpppLinkStatusEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmpppLinkStatusIndex"),
)
if mibBuilder.loadTexts:
    ibmpppLinkStatusEntry.setStatus("mandatory")
_IbmpppLinkStatusIndex_Type = Integer32
_IbmpppLinkStatusIndex_Object = MibTableColumn
ibmpppLinkStatusIndex = _IbmpppLinkStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 1),
    _IbmpppLinkStatusIndex_Type()
)
ibmpppLinkStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkStatusIndex.setStatus("mandatory")
_IbmpppLinkVersion_Type = Integer32
_IbmpppLinkVersion_Object = MibTableColumn
ibmpppLinkVersion = _IbmpppLinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 2),
    _IbmpppLinkVersion_Type()
)
ibmpppLinkVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkVersion.setStatus("mandatory")


class _IbmpppLinkCurrentState_Type(Integer32):
    """Custom type ibmpppLinkCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ackrecvd", 4),
          ("acksent", 5),
          ("closed", 1),
          ("closing", 7),
          ("listen", 2),
          ("open", 6),
          ("reqsent", 3))
    )


_IbmpppLinkCurrentState_Type.__name__ = "Integer32"
_IbmpppLinkCurrentState_Object = MibTableColumn
ibmpppLinkCurrentState = _IbmpppLinkCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 3),
    _IbmpppLinkCurrentState_Type()
)
ibmpppLinkCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkCurrentState.setStatus("mandatory")


class _IbmpppLinkPreviousState_Type(Integer32):
    """Custom type ibmpppLinkPreviousState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ackrecvd", 4),
          ("acksent", 5),
          ("closed", 1),
          ("closing", 7),
          ("listen", 2),
          ("open", 6),
          ("reqsent", 3))
    )


_IbmpppLinkPreviousState_Type.__name__ = "Integer32"
_IbmpppLinkPreviousState_Object = MibTableColumn
ibmpppLinkPreviousState = _IbmpppLinkPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 4),
    _IbmpppLinkPreviousState_Type()
)
ibmpppLinkPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkPreviousState.setStatus("mandatory")
_IbmpppLinkChangeTime_Type = TimeTicks
_IbmpppLinkChangeTime_Object = MibTableColumn
ibmpppLinkChangeTime = _IbmpppLinkChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 5),
    _IbmpppLinkChangeTime_Type()
)
ibmpppLinkChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkChangeTime.setStatus("mandatory")
_IbmpppLinkMagicNumber_Type = Integer32
_IbmpppLinkMagicNumber_Object = MibTableColumn
ibmpppLinkMagicNumber = _IbmpppLinkMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 6),
    _IbmpppLinkMagicNumber_Type()
)
ibmpppLinkMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkMagicNumber.setStatus("mandatory")
_IbmpppLinkLocalQualityPeriod_Type = Integer32
_IbmpppLinkLocalQualityPeriod_Object = MibTableColumn
ibmpppLinkLocalQualityPeriod = _IbmpppLinkLocalQualityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 7),
    _IbmpppLinkLocalQualityPeriod_Type()
)
ibmpppLinkLocalQualityPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLocalQualityPeriod.setStatus("mandatory")
_IbmpppLinkRemoteQualityPeriod_Type = Integer32
_IbmpppLinkRemoteQualityPeriod_Object = MibTableColumn
ibmpppLinkRemoteQualityPeriod = _IbmpppLinkRemoteQualityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 8),
    _IbmpppLinkRemoteQualityPeriod_Type()
)
ibmpppLinkRemoteQualityPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkRemoteQualityPeriod.setStatus("mandatory")


class _IbmpppLinkProtocolCompression_Type(Integer32):
    """Custom type ibmpppLinkProtocolCompression based on Integer32"""
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
        *(("none", 4),
          ("receive-and-send", 3),
          ("receive-only", 1),
          ("send-only", 2))
    )


_IbmpppLinkProtocolCompression_Type.__name__ = "Integer32"
_IbmpppLinkProtocolCompression_Object = MibTableColumn
ibmpppLinkProtocolCompression = _IbmpppLinkProtocolCompression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 9),
    _IbmpppLinkProtocolCompression_Type()
)
ibmpppLinkProtocolCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkProtocolCompression.setStatus("mandatory")


class _IbmpppLinkACCompression_Type(Integer32):
    """Custom type ibmpppLinkACCompression based on Integer32"""
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
        *(("none", 4),
          ("receive-and-send", 3),
          ("receive-only", 1),
          ("send-only", 2))
    )


_IbmpppLinkACCompression_Type.__name__ = "Integer32"
_IbmpppLinkACCompression_Object = MibTableColumn
ibmpppLinkACCompression = _IbmpppLinkACCompression_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 10),
    _IbmpppLinkACCompression_Type()
)
ibmpppLinkACCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkACCompression.setStatus("mandatory")
_IbmpppLinkMeasurementsValid_Type = Integer32
_IbmpppLinkMeasurementsValid_Object = MibTableColumn
ibmpppLinkMeasurementsValid = _IbmpppLinkMeasurementsValid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 11),
    _IbmpppLinkMeasurementsValid_Type()
)
ibmpppLinkMeasurementsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkMeasurementsValid.setStatus("mandatory")


class _IbmpppLinkQuality_Type(Integer32):
    """Custom type ibmpppLinkQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_IbmpppLinkQuality_Type.__name__ = "Integer32"
_IbmpppLinkQuality_Object = MibTableColumn
ibmpppLinkQuality = _IbmpppLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 12),
    _IbmpppLinkQuality_Type()
)
ibmpppLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkQuality.setStatus("mandatory")
_IbmpppLinkPhysical_Type = ObjectIdentifier
_IbmpppLinkPhysical_Object = MibTableColumn
ibmpppLinkPhysical = _IbmpppLinkPhysical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 2, 1, 13),
    _IbmpppLinkPhysical_Type()
)
ibmpppLinkPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkPhysical.setStatus("mandatory")
_IbmpppLinkErrorsTable_Object = MibTable
ibmpppLinkErrorsTable = _IbmpppLinkErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3)
)
if mibBuilder.loadTexts:
    ibmpppLinkErrorsTable.setStatus("mandatory")
_IbmpppLinkErrorsEntry_Object = MibTableRow
ibmpppLinkErrorsEntry = _IbmpppLinkErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1)
)
ibmpppLinkErrorsEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmpppLinkErrorsIndex"),
)
if mibBuilder.loadTexts:
    ibmpppLinkErrorsEntry.setStatus("mandatory")
_IbmpppLinkErrorsIndex_Type = Integer32
_IbmpppLinkErrorsIndex_Object = MibTableColumn
ibmpppLinkErrorsIndex = _IbmpppLinkErrorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 1),
    _IbmpppLinkErrorsIndex_Type()
)
ibmpppLinkErrorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkErrorsIndex.setStatus("mandatory")
_IbmpppLinkBadAddresses_Type = Counter32
_IbmpppLinkBadAddresses_Object = MibTableColumn
ibmpppLinkBadAddresses = _IbmpppLinkBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 2),
    _IbmpppLinkBadAddresses_Type()
)
ibmpppLinkBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkBadAddresses.setStatus("mandatory")
_IbmpppLinkLastBadAddress_Type = OctetString
_IbmpppLinkLastBadAddress_Object = MibTableColumn
ibmpppLinkLastBadAddress = _IbmpppLinkLastBadAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 3),
    _IbmpppLinkLastBadAddress_Type()
)
ibmpppLinkLastBadAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastBadAddress.setStatus("mandatory")
_IbmpppLinkBadControls_Type = Counter32
_IbmpppLinkBadControls_Object = MibTableColumn
ibmpppLinkBadControls = _IbmpppLinkBadControls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 4),
    _IbmpppLinkBadControls_Type()
)
ibmpppLinkBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkBadControls.setStatus("mandatory")
_IbmpppLinkLastBadControl_Type = OctetString
_IbmpppLinkLastBadControl_Object = MibTableColumn
ibmpppLinkLastBadControl = _IbmpppLinkLastBadControl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 5),
    _IbmpppLinkLastBadControl_Type()
)
ibmpppLinkLastBadControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastBadControl.setStatus("mandatory")
_IbmpppLinkLastUnknownProtocol_Type = OctetString
_IbmpppLinkLastUnknownProtocol_Object = MibTableColumn
ibmpppLinkLastUnknownProtocol = _IbmpppLinkLastUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 6),
    _IbmpppLinkLastUnknownProtocol_Type()
)
ibmpppLinkLastUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastUnknownProtocol.setStatus("mandatory")
_IbmpppLinkInvalidProtocols_Type = Counter32
_IbmpppLinkInvalidProtocols_Object = MibTableColumn
ibmpppLinkInvalidProtocols = _IbmpppLinkInvalidProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 7),
    _IbmpppLinkInvalidProtocols_Type()
)
ibmpppLinkInvalidProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkInvalidProtocols.setStatus("mandatory")
_IbmpppLinkLastInvalidProtocol_Type = OctetString
_IbmpppLinkLastInvalidProtocol_Object = MibTableColumn
ibmpppLinkLastInvalidProtocol = _IbmpppLinkLastInvalidProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 8),
    _IbmpppLinkLastInvalidProtocol_Type()
)
ibmpppLinkLastInvalidProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastInvalidProtocol.setStatus("mandatory")
_IbmpppLinkPacketTooLongs_Type = Counter32
_IbmpppLinkPacketTooLongs_Object = MibTableColumn
ibmpppLinkPacketTooLongs = _IbmpppLinkPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 9),
    _IbmpppLinkPacketTooLongs_Type()
)
ibmpppLinkPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkPacketTooLongs.setStatus("mandatory")
_IbmpppLinkBadCRCs_Type = Counter32
_IbmpppLinkBadCRCs_Object = MibTableColumn
ibmpppLinkBadCRCs = _IbmpppLinkBadCRCs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 10),
    _IbmpppLinkBadCRCs_Type()
)
ibmpppLinkBadCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkBadCRCs.setStatus("mandatory")
_IbmpppLinkConfigTimeouts_Type = Counter32
_IbmpppLinkConfigTimeouts_Object = MibTableColumn
ibmpppLinkConfigTimeouts = _IbmpppLinkConfigTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 11),
    _IbmpppLinkConfigTimeouts_Type()
)
ibmpppLinkConfigTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkConfigTimeouts.setStatus("mandatory")
_IbmpppLinkTerminateTimeouts_Type = Counter32
_IbmpppLinkTerminateTimeouts_Object = MibTableColumn
ibmpppLinkTerminateTimeouts = _IbmpppLinkTerminateTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 3, 1, 12),
    _IbmpppLinkTerminateTimeouts_Type()
)
ibmpppLinkTerminateTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkTerminateTimeouts.setStatus("mandatory")
_IbmpppLinkQualityTable_Object = MibTable
ibmpppLinkQualityTable = _IbmpppLinkQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4)
)
if mibBuilder.loadTexts:
    ibmpppLinkQualityTable.setStatus("mandatory")
_IbmpppLinkQualityEntry_Object = MibTableRow
ibmpppLinkQualityEntry = _IbmpppLinkQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1)
)
ibmpppLinkQualityEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmpppLinkQualityIndex"),
)
if mibBuilder.loadTexts:
    ibmpppLinkQualityEntry.setStatus("mandatory")
_IbmpppLinkQualityIndex_Type = Integer32
_IbmpppLinkQualityIndex_Object = MibTableColumn
ibmpppLinkQualityIndex = _IbmpppLinkQualityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 1),
    _IbmpppLinkQualityIndex_Type()
)
ibmpppLinkQualityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkQualityIndex.setStatus("mandatory")
_IbmpppLinkInTxLQRs_Type = Counter32
_IbmpppLinkInTxLQRs_Object = MibTableColumn
ibmpppLinkInTxLQRs = _IbmpppLinkInTxLQRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 2),
    _IbmpppLinkInTxLQRs_Type()
)
ibmpppLinkInTxLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkInTxLQRs.setStatus("mandatory")
_IbmpppLinkInTxPackets_Type = Counter32
_IbmpppLinkInTxPackets_Object = MibTableColumn
ibmpppLinkInTxPackets = _IbmpppLinkInTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 3),
    _IbmpppLinkInTxPackets_Type()
)
ibmpppLinkInTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkInTxPackets.setStatus("mandatory")
_IbmpppLinkLastOutTxPackets_Type = Counter32
_IbmpppLinkLastOutTxPackets_Object = MibTableColumn
ibmpppLinkLastOutTxPackets = _IbmpppLinkLastOutTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 4),
    _IbmpppLinkLastOutTxPackets_Type()
)
ibmpppLinkLastOutTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastOutTxPackets.setStatus("mandatory")
_IbmpppLinkInTxOctets_Type = Counter32
_IbmpppLinkInTxOctets_Object = MibTableColumn
ibmpppLinkInTxOctets = _IbmpppLinkInTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 5),
    _IbmpppLinkInTxOctets_Type()
)
ibmpppLinkInTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkInTxOctets.setStatus("mandatory")
_IbmpppLinkLastOutTxOctets_Type = Counter32
_IbmpppLinkLastOutTxOctets_Object = MibTableColumn
ibmpppLinkLastOutTxOctets = _IbmpppLinkLastOutTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 6),
    _IbmpppLinkLastOutTxOctets_Type()
)
ibmpppLinkLastOutTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastOutTxOctets.setStatus("mandatory")
_IbmpppLinkInRxPackets_Type = Counter32
_IbmpppLinkInRxPackets_Object = MibTableColumn
ibmpppLinkInRxPackets = _IbmpppLinkInRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 7),
    _IbmpppLinkInRxPackets_Type()
)
ibmpppLinkInRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkInRxPackets.setStatus("mandatory")
_IbmpppLinkLastInRxPackets_Type = Counter32
_IbmpppLinkLastInRxPackets_Object = MibTableColumn
ibmpppLinkLastInRxPackets = _IbmpppLinkLastInRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 8),
    _IbmpppLinkLastInRxPackets_Type()
)
ibmpppLinkLastInRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastInRxPackets.setStatus("mandatory")
_IbmpppLinkInRxOctets_Type = Counter32
_IbmpppLinkInRxOctets_Object = MibTableColumn
ibmpppLinkInRxOctets = _IbmpppLinkInRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 9),
    _IbmpppLinkInRxOctets_Type()
)
ibmpppLinkInRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkInRxOctets.setStatus("mandatory")
_IbmpppLinkLastInRxOctets_Type = Counter32
_IbmpppLinkLastInRxOctets_Object = MibTableColumn
ibmpppLinkLastInRxOctets = _IbmpppLinkLastInRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 4, 1, 10),
    _IbmpppLinkLastInRxOctets_Type()
)
ibmpppLinkLastInRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLinkLastInRxOctets.setStatus("mandatory")
_IbmpppProtocolTables_ObjectIdentity = ObjectIdentity
ibmpppProtocolTables = _IbmpppProtocolTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5)
)
_IbmpppIPTable_Object = MibTable
ibmpppIPTable = _IbmpppIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1)
)
if mibBuilder.loadTexts:
    ibmpppIPTable.setStatus("mandatory")
_IbmpppIPEntry_Object = MibTableRow
ibmpppIPEntry = _IbmpppIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1, 1)
)
ibmpppIPEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmpppIPLinkNumber"),
)
if mibBuilder.loadTexts:
    ibmpppIPEntry.setStatus("mandatory")
_IbmpppIPLinkNumber_Type = Integer32
_IbmpppIPLinkNumber_Object = MibTableColumn
ibmpppIPLinkNumber = _IbmpppIPLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1, 1, 1),
    _IbmpppIPLinkNumber_Type()
)
ibmpppIPLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPLinkNumber.setStatus("mandatory")
_IbmpppIPRejects_Type = Counter32
_IbmpppIPRejects_Object = MibTableColumn
ibmpppIPRejects = _IbmpppIPRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1, 1, 2),
    _IbmpppIPRejects_Type()
)
ibmpppIPRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPRejects.setStatus("mandatory")
_IbmpppIPInPackets_Type = Counter32
_IbmpppIPInPackets_Object = MibTableColumn
ibmpppIPInPackets = _IbmpppIPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1, 1, 3),
    _IbmpppIPInPackets_Type()
)
ibmpppIPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPInPackets.setStatus("mandatory")
_IbmpppIPInOctets_Type = Counter32
_IbmpppIPInOctets_Object = MibTableColumn
ibmpppIPInOctets = _IbmpppIPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1, 1, 4),
    _IbmpppIPInOctets_Type()
)
ibmpppIPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPInOctets.setStatus("mandatory")
_IbmpppIPOutPackets_Type = Counter32
_IbmpppIPOutPackets_Object = MibTableColumn
ibmpppIPOutPackets = _IbmpppIPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1, 1, 5),
    _IbmpppIPOutPackets_Type()
)
ibmpppIPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPOutPackets.setStatus("mandatory")
_IbmpppIPOutOctets_Type = Counter32
_IbmpppIPOutOctets_Object = MibTableColumn
ibmpppIPOutOctets = _IbmpppIPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 1, 1, 6),
    _IbmpppIPOutOctets_Type()
)
ibmpppIPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPOutOctets.setStatus("mandatory")
_IbmpppIPCPTable_Object = MibTable
ibmpppIPCPTable = _IbmpppIPCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2)
)
if mibBuilder.loadTexts:
    ibmpppIPCPTable.setStatus("mandatory")
_IbmpppIPCPEntry_Object = MibTableRow
ibmpppIPCPEntry = _IbmpppIPCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1)
)
ibmpppIPCPEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmpppIPCPLinkNumber"),
)
if mibBuilder.loadTexts:
    ibmpppIPCPEntry.setStatus("mandatory")
_IbmpppIPCPLinkNumber_Type = Integer32
_IbmpppIPCPLinkNumber_Object = MibTableColumn
ibmpppIPCPLinkNumber = _IbmpppIPCPLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1, 1),
    _IbmpppIPCPLinkNumber_Type()
)
ibmpppIPCPLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPCPLinkNumber.setStatus("mandatory")
_IbmpppIPCPRejects_Type = Counter32
_IbmpppIPCPRejects_Object = MibTableColumn
ibmpppIPCPRejects = _IbmpppIPCPRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1, 2),
    _IbmpppIPCPRejects_Type()
)
ibmpppIPCPRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPCPRejects.setStatus("mandatory")
_IbmpppIPCPInPackets_Type = Counter32
_IbmpppIPCPInPackets_Object = MibTableColumn
ibmpppIPCPInPackets = _IbmpppIPCPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1, 3),
    _IbmpppIPCPInPackets_Type()
)
ibmpppIPCPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPCPInPackets.setStatus("mandatory")
_IbmpppIPCPInOctets_Type = Counter32
_IbmpppIPCPInOctets_Object = MibTableColumn
ibmpppIPCPInOctets = _IbmpppIPCPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1, 4),
    _IbmpppIPCPInOctets_Type()
)
ibmpppIPCPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPCPInOctets.setStatus("mandatory")
_IbmpppIPCPOutPackets_Type = Counter32
_IbmpppIPCPOutPackets_Object = MibTableColumn
ibmpppIPCPOutPackets = _IbmpppIPCPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1, 5),
    _IbmpppIPCPOutPackets_Type()
)
ibmpppIPCPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPCPOutPackets.setStatus("mandatory")
_IbmpppIPCPOutOctets_Type = Counter32
_IbmpppIPCPOutOctets_Object = MibTableColumn
ibmpppIPCPOutOctets = _IbmpppIPCPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1, 6),
    _IbmpppIPCPOutOctets_Type()
)
ibmpppIPCPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPCPOutOctets.setStatus("mandatory")


class _IbmpppIPCPCompressionType_Type(Integer32):
    """Custom type ibmpppIPCPCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("van-jacobson-compressed-tcp", 2))
    )


_IbmpppIPCPCompressionType_Type.__name__ = "Integer32"
_IbmpppIPCPCompressionType_Object = MibTableColumn
ibmpppIPCPCompressionType = _IbmpppIPCPCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 2, 1, 7),
    _IbmpppIPCPCompressionType_Type()
)
ibmpppIPCPCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppIPCPCompressionType.setStatus("mandatory")
_IbmpppLCPTable_Object = MibTable
ibmpppLCPTable = _IbmpppLCPTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3)
)
if mibBuilder.loadTexts:
    ibmpppLCPTable.setStatus("mandatory")
_IbmpppLCPEntry_Object = MibTableRow
ibmpppLCPEntry = _IbmpppLCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1)
)
ibmpppLCPEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmpppLCPLinkNumber"),
)
if mibBuilder.loadTexts:
    ibmpppLCPEntry.setStatus("mandatory")
_IbmpppLCPLinkNumber_Type = Integer32
_IbmpppLCPLinkNumber_Object = MibTableColumn
ibmpppLCPLinkNumber = _IbmpppLCPLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 1),
    _IbmpppLCPLinkNumber_Type()
)
ibmpppLCPLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPLinkNumber.setStatus("mandatory")
_IbmpppLCPRejects_Type = Counter32
_IbmpppLCPRejects_Object = MibTableColumn
ibmpppLCPRejects = _IbmpppLCPRejects_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 2),
    _IbmpppLCPRejects_Type()
)
ibmpppLCPRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPRejects.setStatus("mandatory")
_IbmpppLCPInPackets_Type = Counter32
_IbmpppLCPInPackets_Object = MibTableColumn
ibmpppLCPInPackets = _IbmpppLCPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 3),
    _IbmpppLCPInPackets_Type()
)
ibmpppLCPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInPackets.setStatus("mandatory")
_IbmpppLCPInOctets_Type = Counter32
_IbmpppLCPInOctets_Object = MibTableColumn
ibmpppLCPInOctets = _IbmpppLCPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 4),
    _IbmpppLCPInOctets_Type()
)
ibmpppLCPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInOctets.setStatus("mandatory")
_IbmpppLCPOutPackets_Type = Counter32
_IbmpppLCPOutPackets_Object = MibTableColumn
ibmpppLCPOutPackets = _IbmpppLCPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 5),
    _IbmpppLCPOutPackets_Type()
)
ibmpppLCPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutPackets.setStatus("mandatory")
_IbmpppLCPOutOctets_Type = Counter32
_IbmpppLCPOutOctets_Object = MibTableColumn
ibmpppLCPOutOctets = _IbmpppLCPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 6),
    _IbmpppLCPOutOctets_Type()
)
ibmpppLCPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutOctets.setStatus("mandatory")
_IbmpppLCPOutCRs_Type = Counter32
_IbmpppLCPOutCRs_Object = MibTableColumn
ibmpppLCPOutCRs = _IbmpppLCPOutCRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 7),
    _IbmpppLCPOutCRs_Type()
)
ibmpppLCPOutCRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutCRs.setStatus("mandatory")
_IbmpppLCPInCRs_Type = Counter32
_IbmpppLCPInCRs_Object = MibTableColumn
ibmpppLCPInCRs = _IbmpppLCPInCRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 8),
    _IbmpppLCPInCRs_Type()
)
ibmpppLCPInCRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInCRs.setStatus("mandatory")
_IbmpppLCPOutCAs_Type = Counter32
_IbmpppLCPOutCAs_Object = MibTableColumn
ibmpppLCPOutCAs = _IbmpppLCPOutCAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 9),
    _IbmpppLCPOutCAs_Type()
)
ibmpppLCPOutCAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutCAs.setStatus("mandatory")
_IbmpppLCPInCAs_Type = Counter32
_IbmpppLCPInCAs_Object = MibTableColumn
ibmpppLCPInCAs = _IbmpppLCPInCAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 10),
    _IbmpppLCPInCAs_Type()
)
ibmpppLCPInCAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInCAs.setStatus("mandatory")
_IbmpppLCPOutCNs_Type = Counter32
_IbmpppLCPOutCNs_Object = MibTableColumn
ibmpppLCPOutCNs = _IbmpppLCPOutCNs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 11),
    _IbmpppLCPOutCNs_Type()
)
ibmpppLCPOutCNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutCNs.setStatus("mandatory")
_IbmpppLCPInCNs_Type = Counter32
_IbmpppLCPInCNs_Object = MibTableColumn
ibmpppLCPInCNs = _IbmpppLCPInCNs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 12),
    _IbmpppLCPInCNs_Type()
)
ibmpppLCPInCNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInCNs.setStatus("mandatory")
_IbmpppLCPOutCRejs_Type = Counter32
_IbmpppLCPOutCRejs_Object = MibTableColumn
ibmpppLCPOutCRejs = _IbmpppLCPOutCRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 13),
    _IbmpppLCPOutCRejs_Type()
)
ibmpppLCPOutCRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutCRejs.setStatus("mandatory")
_IbmpppLCPInCRejs_Type = Counter32
_IbmpppLCPInCRejs_Object = MibTableColumn
ibmpppLCPInCRejs = _IbmpppLCPInCRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 14),
    _IbmpppLCPInCRejs_Type()
)
ibmpppLCPInCRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInCRejs.setStatus("mandatory")
_IbmpppLCPOutTRs_Type = Counter32
_IbmpppLCPOutTRs_Object = MibTableColumn
ibmpppLCPOutTRs = _IbmpppLCPOutTRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 15),
    _IbmpppLCPOutTRs_Type()
)
ibmpppLCPOutTRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutTRs.setStatus("mandatory")
_IbmpppLCPInTRs_Type = Counter32
_IbmpppLCPInTRs_Object = MibTableColumn
ibmpppLCPInTRs = _IbmpppLCPInTRs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 16),
    _IbmpppLCPInTRs_Type()
)
ibmpppLCPInTRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInTRs.setStatus("mandatory")
_IbmpppLCPOutTAs_Type = Counter32
_IbmpppLCPOutTAs_Object = MibTableColumn
ibmpppLCPOutTAs = _IbmpppLCPOutTAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 17),
    _IbmpppLCPOutTAs_Type()
)
ibmpppLCPOutTAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutTAs.setStatus("mandatory")
_IbmpppLCPInTAs_Type = Counter32
_IbmpppLCPInTAs_Object = MibTableColumn
ibmpppLCPInTAs = _IbmpppLCPInTAs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 18),
    _IbmpppLCPInTAs_Type()
)
ibmpppLCPInTAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInTAs.setStatus("mandatory")
_IbmpppLCPOutCodeRejs_Type = Counter32
_IbmpppLCPOutCodeRejs_Object = MibTableColumn
ibmpppLCPOutCodeRejs = _IbmpppLCPOutCodeRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 19),
    _IbmpppLCPOutCodeRejs_Type()
)
ibmpppLCPOutCodeRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutCodeRejs.setStatus("mandatory")
_IbmpppLCPInCodeRejs_Type = Counter32
_IbmpppLCPInCodeRejs_Object = MibTableColumn
ibmpppLCPInCodeRejs = _IbmpppLCPInCodeRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 20),
    _IbmpppLCPInCodeRejs_Type()
)
ibmpppLCPInCodeRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInCodeRejs.setStatus("mandatory")
_IbmpppLCPOutEchoReqs_Type = Counter32
_IbmpppLCPOutEchoReqs_Object = MibTableColumn
ibmpppLCPOutEchoReqs = _IbmpppLCPOutEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 21),
    _IbmpppLCPOutEchoReqs_Type()
)
ibmpppLCPOutEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutEchoReqs.setStatus("mandatory")
_IbmpppLCPInEchoReqs_Type = Counter32
_IbmpppLCPInEchoReqs_Object = MibTableColumn
ibmpppLCPInEchoReqs = _IbmpppLCPInEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 22),
    _IbmpppLCPInEchoReqs_Type()
)
ibmpppLCPInEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInEchoReqs.setStatus("mandatory")
_IbmpppLCPOutEchoReps_Type = Counter32
_IbmpppLCPOutEchoReps_Object = MibTableColumn
ibmpppLCPOutEchoReps = _IbmpppLCPOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 23),
    _IbmpppLCPOutEchoReps_Type()
)
ibmpppLCPOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutEchoReps.setStatus("mandatory")
_IbmpppLCPInEchoReps_Type = Counter32
_IbmpppLCPInEchoReps_Object = MibTableColumn
ibmpppLCPInEchoReps = _IbmpppLCPInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 24),
    _IbmpppLCPInEchoReps_Type()
)
ibmpppLCPInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInEchoReps.setStatus("mandatory")
_IbmpppLCPOutDiscReqs_Type = Counter32
_IbmpppLCPOutDiscReqs_Object = MibTableColumn
ibmpppLCPOutDiscReqs = _IbmpppLCPOutDiscReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 25),
    _IbmpppLCPOutDiscReqs_Type()
)
ibmpppLCPOutDiscReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPOutDiscReqs.setStatus("mandatory")
_IbmpppLCPInDiscReqs_Type = Counter32
_IbmpppLCPInDiscReqs_Object = MibTableColumn
ibmpppLCPInDiscReqs = _IbmpppLCPInDiscReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 10, 5, 3, 1, 26),
    _IbmpppLCPInDiscReqs_Type()
)
ibmpppLCPInDiscReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmpppLCPInDiscReqs.setStatus("mandatory")
_Ibmxns_ObjectIdentity = ObjectIdentity
ibmxns = _Ibmxns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11)
)


class _IbmxnsidpForwarding_Type(Integer32):
    """Custom type ibmxnsidpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_IbmxnsidpForwarding_Type.__name__ = "Integer32"
_IbmxnsidpForwarding_Object = MibScalar
ibmxnsidpForwarding = _IbmxnsidpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 1),
    _IbmxnsidpForwarding_Type()
)
ibmxnsidpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpForwarding.setStatus("mandatory")
_IbmxnsConfigTable_Object = MibTable
ibmxnsConfigTable = _IbmxnsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 4)
)
if mibBuilder.loadTexts:
    ibmxnsConfigTable.setStatus("mandatory")
_IbmxnsConfigEntry_Object = MibTableRow
ibmxnsConfigEntry = _IbmxnsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 4, 1)
)
ibmxnsConfigEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmxnsPortIfIndex"),
)
if mibBuilder.loadTexts:
    ibmxnsConfigEntry.setStatus("mandatory")
_IbmxnsPortIfIndex_Type = Integer32
_IbmxnsPortIfIndex_Object = MibTableColumn
ibmxnsPortIfIndex = _IbmxnsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 4, 1, 1),
    _IbmxnsPortIfIndex_Type()
)
ibmxnsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsPortIfIndex.setStatus("mandatory")


class _IbmxnsPortStatus_Type(Integer32):
    """Custom type ibmxnsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IbmxnsPortStatus_Type.__name__ = "Integer32"
_IbmxnsPortStatus_Object = MibTableColumn
ibmxnsPortStatus = _IbmxnsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 4, 1, 2),
    _IbmxnsPortStatus_Type()
)
ibmxnsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsPortStatus.setStatus("mandatory")


class _IbmxnsidpChecksum_Type(Integer32):
    """Custom type ibmxnsidpChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("header", 2),
          ("off", 1),
          ("packet", 3))
    )


_IbmxnsidpChecksum_Type.__name__ = "Integer32"
_IbmxnsidpChecksum_Object = MibTableColumn
ibmxnsidpChecksum = _IbmxnsidpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 4, 1, 3),
    _IbmxnsidpChecksum_Type()
)
ibmxnsidpChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpChecksum.setStatus("mandatory")


class _IbmxnsErrpActive_Type(Integer32):
    """Custom type ibmxnsErrpActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suppressed", 2))
    )


_IbmxnsErrpActive_Type.__name__ = "Integer32"
_IbmxnsErrpActive_Object = MibTableColumn
ibmxnsErrpActive = _IbmxnsErrpActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 4, 1, 4),
    _IbmxnsErrpActive_Type()
)
ibmxnsErrpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrpActive.setStatus("mandatory")


class _IbmxnsLoopbackActive_Type(Integer32):
    """Custom type ibmxnsLoopbackActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware-loopback-active", 2),
          ("software-loopback-active", 1))
    )


_IbmxnsLoopbackActive_Type.__name__ = "Integer32"
_IbmxnsLoopbackActive_Object = MibTableColumn
ibmxnsLoopbackActive = _IbmxnsLoopbackActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 4, 1, 5),
    _IbmxnsLoopbackActive_Type()
)
ibmxnsLoopbackActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsLoopbackActive.setStatus("mandatory")
_IbmxnsidpInReceives_Type = Counter32
_IbmxnsidpInReceives_Object = MibScalar
ibmxnsidpInReceives = _IbmxnsidpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 5),
    _IbmxnsidpInReceives_Type()
)
ibmxnsidpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpInReceives.setStatus("mandatory")
_IbmxnsidpBcastInReceives_Type = Counter32
_IbmxnsidpBcastInReceives_Object = MibScalar
ibmxnsidpBcastInReceives = _IbmxnsidpBcastInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 6),
    _IbmxnsidpBcastInReceives_Type()
)
ibmxnsidpBcastInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpBcastInReceives.setStatus("mandatory")
_IbmxnsidpMcastInReceives_Type = Counter32
_IbmxnsidpMcastInReceives_Object = MibScalar
ibmxnsidpMcastInReceives = _IbmxnsidpMcastInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 7),
    _IbmxnsidpMcastInReceives_Type()
)
ibmxnsidpMcastInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpMcastInReceives.setStatus("mandatory")
_IbmxnsidpInDiscards_Type = Counter32
_IbmxnsidpInDiscards_Object = MibScalar
ibmxnsidpInDiscards = _IbmxnsidpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 8),
    _IbmxnsidpInDiscards_Type()
)
ibmxnsidpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpInDiscards.setStatus("mandatory")
_IbmxnsidpOutRequests_Type = Counter32
_IbmxnsidpOutRequests_Object = MibScalar
ibmxnsidpOutRequests = _IbmxnsidpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 11),
    _IbmxnsidpOutRequests_Type()
)
ibmxnsidpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpOutRequests.setStatus("mandatory")
_IbmxnsidpBcastOutRequests_Type = Counter32
_IbmxnsidpBcastOutRequests_Object = MibScalar
ibmxnsidpBcastOutRequests = _IbmxnsidpBcastOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 12),
    _IbmxnsidpBcastOutRequests_Type()
)
ibmxnsidpBcastOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpBcastOutRequests.setStatus("mandatory")
_IbmxnsidpMcastOutRequests_Type = Counter32
_IbmxnsidpMcastOutRequests_Object = MibScalar
ibmxnsidpMcastOutRequests = _IbmxnsidpMcastOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 13),
    _IbmxnsidpMcastOutRequests_Type()
)
ibmxnsidpMcastOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpMcastOutRequests.setStatus("mandatory")
_IbmxnsidpForwDatagrams_Type = Counter32
_IbmxnsidpForwDatagrams_Object = MibScalar
ibmxnsidpForwDatagrams = _IbmxnsidpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 14),
    _IbmxnsidpForwDatagrams_Type()
)
ibmxnsidpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpForwDatagrams.setStatus("mandatory")
_IbmxnsidpOutDiscards_Type = Counter32
_IbmxnsidpOutDiscards_Object = MibScalar
ibmxnsidpOutDiscards = _IbmxnsidpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 15),
    _IbmxnsidpOutDiscards_Type()
)
ibmxnsidpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpOutDiscards.setStatus("mandatory")
_IbmxnsidpOutNoRoutes_Type = Counter32
_IbmxnsidpOutNoRoutes_Object = MibScalar
ibmxnsidpOutNoRoutes = _IbmxnsidpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 16),
    _IbmxnsidpOutNoRoutes_Type()
)
ibmxnsidpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpOutNoRoutes.setStatus("mandatory")
_IbmxnsidpRoutingDiscards_Type = Counter32
_IbmxnsidpRoutingDiscards_Object = MibScalar
ibmxnsidpRoutingDiscards = _IbmxnsidpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 17),
    _IbmxnsidpRoutingDiscards_Type()
)
ibmxnsidpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpRoutingDiscards.setStatus("mandatory")
_IbmxnsidpZeroDirBcast_Type = Counter32
_IbmxnsidpZeroDirBcast_Object = MibScalar
ibmxnsidpZeroDirBcast = _IbmxnsidpZeroDirBcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 19),
    _IbmxnsidpZeroDirBcast_Type()
)
ibmxnsidpZeroDirBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpZeroDirBcast.setStatus("mandatory")
_IbmxnsidpTooSmall_Type = Counter32
_IbmxnsidpTooSmall_Object = MibScalar
ibmxnsidpTooSmall = _IbmxnsidpTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 20),
    _IbmxnsidpTooSmall_Type()
)
ibmxnsidpTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpTooSmall.setStatus("mandatory")
_IbmxnsidpBadLen_Type = Counter32
_IbmxnsidpBadLen_Object = MibScalar
ibmxnsidpBadLen = _IbmxnsidpBadLen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 21),
    _IbmxnsidpBadLen_Type()
)
ibmxnsidpBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpBadLen.setStatus("mandatory")
_IbmxnsidpBadSum_Type = Counter32
_IbmxnsidpBadSum_Object = MibScalar
ibmxnsidpBadSum = _IbmxnsidpBadSum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 22),
    _IbmxnsidpBadSum_Type()
)
ibmxnsidpBadSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpBadSum.setStatus("mandatory")
_IbmxnsidpBadTTL_Type = Counter32
_IbmxnsidpBadTTL_Object = MibScalar
ibmxnsidpBadTTL = _IbmxnsidpBadTTL_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 23),
    _IbmxnsidpBadTTL_Type()
)
ibmxnsidpBadTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsidpBadTTL.setStatus("mandatory")
_IbmxnsErrUnspec_Type = Counter32
_IbmxnsErrUnspec_Object = MibScalar
ibmxnsErrUnspec = _IbmxnsErrUnspec_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 24),
    _IbmxnsErrUnspec_Type()
)
ibmxnsErrUnspec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrUnspec.setStatus("mandatory")
_IbmxnsErrChecksum_Type = Counter32
_IbmxnsErrChecksum_Object = MibScalar
ibmxnsErrChecksum = _IbmxnsErrChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 25),
    _IbmxnsErrChecksum_Type()
)
ibmxnsErrChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrChecksum.setStatus("mandatory")
_IbmxnsErrUnreach_Type = Counter32
_IbmxnsErrUnreach_Object = MibScalar
ibmxnsErrUnreach = _IbmxnsErrUnreach_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 26),
    _IbmxnsErrUnreach_Type()
)
ibmxnsErrUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrUnreach.setStatus("mandatory")
_IbmxnsErrTTLExpired_Type = Counter32
_IbmxnsErrTTLExpired_Object = MibScalar
ibmxnsErrTTLExpired = _IbmxnsErrTTLExpired_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 27),
    _IbmxnsErrTTLExpired_Type()
)
ibmxnsErrTTLExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrTTLExpired.setStatus("mandatory")
_IbmxnsErrTooBig_Type = Counter32
_IbmxnsErrTooBig_Object = MibScalar
ibmxnsErrTooBig = _IbmxnsErrTooBig_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 28),
    _IbmxnsErrTooBig_Type()
)
ibmxnsErrTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrTooBig.setStatus("mandatory")
_IbmxnsErrResources_Type = Counter32
_IbmxnsErrResources_Object = MibScalar
ibmxnsErrResources = _IbmxnsErrResources_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 29),
    _IbmxnsErrResources_Type()
)
ibmxnsErrResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrResources.setStatus("mandatory")
_IbmxnsErrCongWarn_Type = Counter32
_IbmxnsErrCongWarn_Object = MibScalar
ibmxnsErrCongWarn = _IbmxnsErrCongWarn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 30),
    _IbmxnsErrCongWarn_Type()
)
ibmxnsErrCongWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrCongWarn.setStatus("mandatory")
_IbmxnsErrCongDiscard_Type = Counter32
_IbmxnsErrCongDiscard_Object = MibScalar
ibmxnsErrCongDiscard = _IbmxnsErrCongDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 31),
    _IbmxnsErrCongDiscard_Type()
)
ibmxnsErrCongDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrCongDiscard.setStatus("mandatory")
_IbmxnsErrSquelched_Type = Counter32
_IbmxnsErrSquelched_Object = MibScalar
ibmxnsErrSquelched = _IbmxnsErrSquelched_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 32),
    _IbmxnsErrSquelched_Type()
)
ibmxnsErrSquelched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrSquelched.setStatus("mandatory")
_IbmxnsErrOutMsgs_Type = Counter32
_IbmxnsErrOutMsgs_Object = MibScalar
ibmxnsErrOutMsgs = _IbmxnsErrOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 33),
    _IbmxnsErrOutMsgs_Type()
)
ibmxnsErrOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsErrOutMsgs.setStatus("mandatory")
_IbmxnsAddrTable_Object = MibTable
ibmxnsAddrTable = _IbmxnsAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 34)
)
if mibBuilder.loadTexts:
    ibmxnsAddrTable.setStatus("mandatory")
_IbmxnsAddrEntry_Object = MibTableRow
ibmxnsAddrEntry = _IbmxnsAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 34, 1)
)
ibmxnsAddrEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmxnsAddrAddress"),
)
if mibBuilder.loadTexts:
    ibmxnsAddrEntry.setStatus("mandatory")


class _IbmxnsAddrAddress_Type(OctetString):
    """Custom type ibmxnsAddrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_IbmxnsAddrAddress_Type.__name__ = "OctetString"
_IbmxnsAddrAddress_Object = MibTableColumn
ibmxnsAddrAddress = _IbmxnsAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 34, 1, 1),
    _IbmxnsAddrAddress_Type()
)
ibmxnsAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsAddrAddress.setStatus("mandatory")
_IbmxnsAddrIfIndex_Type = Integer32
_IbmxnsAddrIfIndex_Object = MibTableColumn
ibmxnsAddrIfIndex = _IbmxnsAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 34, 1, 2),
    _IbmxnsAddrIfIndex_Type()
)
ibmxnsAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsAddrIfIndex.setStatus("mandatory")
_IbmxnsRouteTable_Object = MibTable
ibmxnsRouteTable = _IbmxnsRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 35)
)
if mibBuilder.loadTexts:
    ibmxnsRouteTable.setStatus("mandatory")
_IbmxnsRouteEntry_Object = MibTableRow
ibmxnsRouteEntry = _IbmxnsRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 35, 1)
)
ibmxnsRouteEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmxnsRouteDest"),
)
if mibBuilder.loadTexts:
    ibmxnsRouteEntry.setStatus("mandatory")


class _IbmxnsRouteDest_Type(OctetString):
    """Custom type ibmxnsRouteDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_IbmxnsRouteDest_Type.__name__ = "OctetString"
_IbmxnsRouteDest_Object = MibTableColumn
ibmxnsRouteDest = _IbmxnsRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 35, 1, 1),
    _IbmxnsRouteDest_Type()
)
ibmxnsRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsRouteDest.setStatus("mandatory")
_IbmxnsRouteIfIndex_Type = Integer32
_IbmxnsRouteIfIndex_Object = MibTableColumn
ibmxnsRouteIfIndex = _IbmxnsRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 35, 1, 2),
    _IbmxnsRouteIfIndex_Type()
)
ibmxnsRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsRouteIfIndex.setStatus("mandatory")


class _IbmxnsRouteNextHop_Type(OctetString):
    """Custom type ibmxnsRouteNextHop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmxnsRouteNextHop_Type.__name__ = "OctetString"
_IbmxnsRouteNextHop_Object = MibTableColumn
ibmxnsRouteNextHop = _IbmxnsRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 35, 1, 3),
    _IbmxnsRouteNextHop_Type()
)
ibmxnsRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsRouteNextHop.setStatus("mandatory")
_IbmxnsRouteMetric_Type = Integer32
_IbmxnsRouteMetric_Object = MibTableColumn
ibmxnsRouteMetric = _IbmxnsRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 35, 1, 4),
    _IbmxnsRouteMetric_Type()
)
ibmxnsRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsRouteMetric.setStatus("mandatory")
_IbmxnsRouteUse_Type = Counter32
_IbmxnsRouteUse_Object = MibTableColumn
ibmxnsRouteUse = _IbmxnsRouteUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 35, 1, 5),
    _IbmxnsRouteUse_Type()
)
ibmxnsRouteUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsRouteUse.setStatus("mandatory")
_IbmxnsFilterTable_Object = MibTable
ibmxnsFilterTable = _IbmxnsFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36)
)
if mibBuilder.loadTexts:
    ibmxnsFilterTable.setStatus("mandatory")
_IbmxnsFilterEntry_Object = MibTableRow
ibmxnsFilterEntry = _IbmxnsFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1)
)
ibmxnsFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmxnsFilterIfIndex"),
    (0, "IBM6611-MIB", "ibmxnsFilterNumber"),
)
if mibBuilder.loadTexts:
    ibmxnsFilterEntry.setStatus("mandatory")
_IbmxnsFilterIfIndex_Type = Integer32
_IbmxnsFilterIfIndex_Object = MibTableColumn
ibmxnsFilterIfIndex = _IbmxnsFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1, 1),
    _IbmxnsFilterIfIndex_Type()
)
ibmxnsFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsFilterIfIndex.setStatus("mandatory")
_IbmxnsFilterNumber_Type = Integer32
_IbmxnsFilterNumber_Object = MibTableColumn
ibmxnsFilterNumber = _IbmxnsFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1, 2),
    _IbmxnsFilterNumber_Type()
)
ibmxnsFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsFilterNumber.setStatus("mandatory")


class _IbmxnsFilterValue_Type(OctetString):
    """Custom type ibmxnsFilterValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_IbmxnsFilterValue_Type.__name__ = "OctetString"
_IbmxnsFilterValue_Object = MibTableColumn
ibmxnsFilterValue = _IbmxnsFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1, 3),
    _IbmxnsFilterValue_Type()
)
ibmxnsFilterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsFilterValue.setStatus("mandatory")


class _IbmxnsFilterMask_Type(OctetString):
    """Custom type ibmxnsFilterMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_IbmxnsFilterMask_Type.__name__ = "OctetString"
_IbmxnsFilterMask_Object = MibTableColumn
ibmxnsFilterMask = _IbmxnsFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1, 4),
    _IbmxnsFilterMask_Type()
)
ibmxnsFilterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsFilterMask.setStatus("mandatory")


class _IbmxnsFilterType_Type(Integer32):
    """Custom type ibmxnsFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmxnsFilterType_Type.__name__ = "Integer32"
_IbmxnsFilterType_Object = MibTableColumn
ibmxnsFilterType = _IbmxnsFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1, 5),
    _IbmxnsFilterType_Type()
)
ibmxnsFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsFilterType.setStatus("mandatory")


class _IbmxnsFilterHCCompare_Type(Integer32):
    """Custom type ibmxnsFilterHCCompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equal", 4),
          ("greater-than", 6),
          ("greater-than-equal", 5),
          ("less-than", 2),
          ("less-than-equal", 3),
          ("none", 1))
    )


_IbmxnsFilterHCCompare_Type.__name__ = "Integer32"
_IbmxnsFilterHCCompare_Object = MibTableColumn
ibmxnsFilterHCCompare = _IbmxnsFilterHCCompare_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1, 6),
    _IbmxnsFilterHCCompare_Type()
)
ibmxnsFilterHCCompare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsFilterHCCompare.setStatus("mandatory")
_IbmxnsFilterUse_Type = Counter32
_IbmxnsFilterUse_Object = MibTableColumn
ibmxnsFilterUse = _IbmxnsFilterUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 11, 36, 1, 7),
    _IbmxnsFilterUse_Type()
)
ibmxnsFilterUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmxnsFilterUse.setStatus("mandatory")
_Ibmipx_ObjectIdentity = ObjectIdentity
ibmipx = _Ibmipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12)
)


class _IbmipxidpForwarding_Type(Integer32):
    """Custom type ibmipxidpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_IbmipxidpForwarding_Type.__name__ = "Integer32"
_IbmipxidpForwarding_Object = MibScalar
ibmipxidpForwarding = _IbmipxidpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 1),
    _IbmipxidpForwarding_Type()
)
ibmipxidpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpForwarding.setStatus("mandatory")
_IbmipxConfigTable_Object = MibTable
ibmipxConfigTable = _IbmipxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 4)
)
if mibBuilder.loadTexts:
    ibmipxConfigTable.setStatus("mandatory")
_IbmipxConfigEntry_Object = MibTableRow
ibmipxConfigEntry = _IbmipxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 4, 1)
)
ibmipxConfigEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipxPortIfIndex"),
)
if mibBuilder.loadTexts:
    ibmipxConfigEntry.setStatus("mandatory")
_IbmipxPortIfIndex_Type = Integer32
_IbmipxPortIfIndex_Object = MibTableColumn
ibmipxPortIfIndex = _IbmipxPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 4, 1, 1),
    _IbmipxPortIfIndex_Type()
)
ibmipxPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxPortIfIndex.setStatus("mandatory")


class _IbmipxPortStatus_Type(Integer32):
    """Custom type ibmipxPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IbmipxPortStatus_Type.__name__ = "Integer32"
_IbmipxPortStatus_Object = MibTableColumn
ibmipxPortStatus = _IbmipxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 4, 1, 2),
    _IbmipxPortStatus_Type()
)
ibmipxPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxPortStatus.setStatus("mandatory")


class _IbmipxidpChecksum_Type(Integer32):
    """Custom type ibmipxidpChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("header", 2),
          ("off", 1),
          ("packet", 3))
    )


_IbmipxidpChecksum_Type.__name__ = "Integer32"
_IbmipxidpChecksum_Object = MibTableColumn
ibmipxidpChecksum = _IbmipxidpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 4, 1, 3),
    _IbmipxidpChecksum_Type()
)
ibmipxidpChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpChecksum.setStatus("mandatory")


class _IbmipxLoopbackActive_Type(Integer32):
    """Custom type ibmipxLoopbackActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware-loopback-active", 2),
          ("software-loopback-active", 1))
    )


_IbmipxLoopbackActive_Type.__name__ = "Integer32"
_IbmipxLoopbackActive_Object = MibTableColumn
ibmipxLoopbackActive = _IbmipxLoopbackActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 4, 1, 5),
    _IbmipxLoopbackActive_Type()
)
ibmipxLoopbackActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxLoopbackActive.setStatus("mandatory")
_IbmipxidpInReceives_Type = Counter32
_IbmipxidpInReceives_Object = MibScalar
ibmipxidpInReceives = _IbmipxidpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 5),
    _IbmipxidpInReceives_Type()
)
ibmipxidpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpInReceives.setStatus("mandatory")
_IbmipxidpBcastInReceives_Type = Counter32
_IbmipxidpBcastInReceives_Object = MibScalar
ibmipxidpBcastInReceives = _IbmipxidpBcastInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 6),
    _IbmipxidpBcastInReceives_Type()
)
ibmipxidpBcastInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpBcastInReceives.setStatus("mandatory")
_IbmipxidpInDiscards_Type = Counter32
_IbmipxidpInDiscards_Object = MibScalar
ibmipxidpInDiscards = _IbmipxidpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 8),
    _IbmipxidpInDiscards_Type()
)
ibmipxidpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpInDiscards.setStatus("mandatory")
_IbmipxidpInAddrErrors_Type = Counter32
_IbmipxidpInAddrErrors_Object = MibScalar
ibmipxidpInAddrErrors = _IbmipxidpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 10),
    _IbmipxidpInAddrErrors_Type()
)
ibmipxidpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpInAddrErrors.setStatus("mandatory")
_IbmipxidpOutRequests_Type = Counter32
_IbmipxidpOutRequests_Object = MibScalar
ibmipxidpOutRequests = _IbmipxidpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 11),
    _IbmipxidpOutRequests_Type()
)
ibmipxidpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpOutRequests.setStatus("mandatory")
_IbmipxidpBcastOutRequests_Type = Counter32
_IbmipxidpBcastOutRequests_Object = MibScalar
ibmipxidpBcastOutRequests = _IbmipxidpBcastOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 12),
    _IbmipxidpBcastOutRequests_Type()
)
ibmipxidpBcastOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpBcastOutRequests.setStatus("mandatory")
_IbmipxidpForwDatagrams_Type = Counter32
_IbmipxidpForwDatagrams_Object = MibScalar
ibmipxidpForwDatagrams = _IbmipxidpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 14),
    _IbmipxidpForwDatagrams_Type()
)
ibmipxidpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpForwDatagrams.setStatus("mandatory")
_IbmipxidpOutDiscards_Type = Counter32
_IbmipxidpOutDiscards_Object = MibScalar
ibmipxidpOutDiscards = _IbmipxidpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 15),
    _IbmipxidpOutDiscards_Type()
)
ibmipxidpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpOutDiscards.setStatus("mandatory")
_IbmipxidpOutNoRoutes_Type = Counter32
_IbmipxidpOutNoRoutes_Object = MibScalar
ibmipxidpOutNoRoutes = _IbmipxidpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 16),
    _IbmipxidpOutNoRoutes_Type()
)
ibmipxidpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpOutNoRoutes.setStatus("mandatory")
_IbmipxidpRoutingDiscards_Type = Counter32
_IbmipxidpRoutingDiscards_Object = MibScalar
ibmipxidpRoutingDiscards = _IbmipxidpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 17),
    _IbmipxidpRoutingDiscards_Type()
)
ibmipxidpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpRoutingDiscards.setStatus("mandatory")
_IbmipxidpZeroDirBcast_Type = Counter32
_IbmipxidpZeroDirBcast_Object = MibScalar
ibmipxidpZeroDirBcast = _IbmipxidpZeroDirBcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 19),
    _IbmipxidpZeroDirBcast_Type()
)
ibmipxidpZeroDirBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpZeroDirBcast.setStatus("mandatory")
_IbmipxidpTooSmall_Type = Counter32
_IbmipxidpTooSmall_Object = MibScalar
ibmipxidpTooSmall = _IbmipxidpTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 20),
    _IbmipxidpTooSmall_Type()
)
ibmipxidpTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpTooSmall.setStatus("mandatory")
_IbmipxidpBadLen_Type = Counter32
_IbmipxidpBadLen_Object = MibScalar
ibmipxidpBadLen = _IbmipxidpBadLen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 21),
    _IbmipxidpBadLen_Type()
)
ibmipxidpBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpBadLen.setStatus("mandatory")
_IbmipxidpBadSum_Type = Counter32
_IbmipxidpBadSum_Object = MibScalar
ibmipxidpBadSum = _IbmipxidpBadSum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 22),
    _IbmipxidpBadSum_Type()
)
ibmipxidpBadSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpBadSum.setStatus("mandatory")
_IbmipxidpBadTTL_Type = Counter32
_IbmipxidpBadTTL_Object = MibScalar
ibmipxidpBadTTL = _IbmipxidpBadTTL_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 23),
    _IbmipxidpBadTTL_Type()
)
ibmipxidpBadTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxidpBadTTL.setStatus("mandatory")
_IbmipxAddrTable_Object = MibTable
ibmipxAddrTable = _IbmipxAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 34)
)
if mibBuilder.loadTexts:
    ibmipxAddrTable.setStatus("mandatory")
_IbmipxAddrEntry_Object = MibTableRow
ibmipxAddrEntry = _IbmipxAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 34, 1)
)
ibmipxAddrEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipxAddrAddress"),
)
if mibBuilder.loadTexts:
    ibmipxAddrEntry.setStatus("mandatory")


class _IbmipxAddrAddress_Type(OctetString):
    """Custom type ibmipxAddrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_IbmipxAddrAddress_Type.__name__ = "OctetString"
_IbmipxAddrAddress_Object = MibTableColumn
ibmipxAddrAddress = _IbmipxAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 34, 1, 1),
    _IbmipxAddrAddress_Type()
)
ibmipxAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxAddrAddress.setStatus("mandatory")
_IbmipxAddrIfIndex_Type = Integer32
_IbmipxAddrIfIndex_Object = MibTableColumn
ibmipxAddrIfIndex = _IbmipxAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 34, 1, 2),
    _IbmipxAddrIfIndex_Type()
)
ibmipxAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxAddrIfIndex.setStatus("mandatory")
_IbmipxRouteTable_Object = MibTable
ibmipxRouteTable = _IbmipxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 35)
)
if mibBuilder.loadTexts:
    ibmipxRouteTable.setStatus("mandatory")
_IbmipxRouteEntry_Object = MibTableRow
ibmipxRouteEntry = _IbmipxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 35, 1)
)
ibmipxRouteEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipxRouteDest"),
)
if mibBuilder.loadTexts:
    ibmipxRouteEntry.setStatus("mandatory")


class _IbmipxRouteDest_Type(OctetString):
    """Custom type ibmipxRouteDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_IbmipxRouteDest_Type.__name__ = "OctetString"
_IbmipxRouteDest_Object = MibTableColumn
ibmipxRouteDest = _IbmipxRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 35, 1, 1),
    _IbmipxRouteDest_Type()
)
ibmipxRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxRouteDest.setStatus("mandatory")
_IbmipxRouteIfIndex_Type = Integer32
_IbmipxRouteIfIndex_Object = MibTableColumn
ibmipxRouteIfIndex = _IbmipxRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 35, 1, 2),
    _IbmipxRouteIfIndex_Type()
)
ibmipxRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxRouteIfIndex.setStatus("mandatory")


class _IbmipxRouteNextHop_Type(OctetString):
    """Custom type ibmipxRouteNextHop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmipxRouteNextHop_Type.__name__ = "OctetString"
_IbmipxRouteNextHop_Object = MibTableColumn
ibmipxRouteNextHop = _IbmipxRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 35, 1, 3),
    _IbmipxRouteNextHop_Type()
)
ibmipxRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxRouteNextHop.setStatus("mandatory")
_IbmipxRouteMetric_Type = Integer32
_IbmipxRouteMetric_Object = MibTableColumn
ibmipxRouteMetric = _IbmipxRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 35, 1, 4),
    _IbmipxRouteMetric_Type()
)
ibmipxRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxRouteMetric.setStatus("mandatory")
_IbmipxRouteUse_Type = Counter32
_IbmipxRouteUse_Object = MibTableColumn
ibmipxRouteUse = _IbmipxRouteUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 35, 1, 5),
    _IbmipxRouteUse_Type()
)
ibmipxRouteUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxRouteUse.setStatus("mandatory")
_IbmipxFilterTable_Object = MibTable
ibmipxFilterTable = _IbmipxFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36)
)
if mibBuilder.loadTexts:
    ibmipxFilterTable.setStatus("mandatory")
_IbmipxFilterEntry_Object = MibTableRow
ibmipxFilterEntry = _IbmipxFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1)
)
ibmipxFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipxFilterIfIndex"),
    (0, "IBM6611-MIB", "ibmipxFilterNumber"),
)
if mibBuilder.loadTexts:
    ibmipxFilterEntry.setStatus("mandatory")
_IbmipxFilterIfIndex_Type = Integer32
_IbmipxFilterIfIndex_Object = MibTableColumn
ibmipxFilterIfIndex = _IbmipxFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1, 1),
    _IbmipxFilterIfIndex_Type()
)
ibmipxFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxFilterIfIndex.setStatus("mandatory")
_IbmipxFilterNumber_Type = Integer32
_IbmipxFilterNumber_Object = MibTableColumn
ibmipxFilterNumber = _IbmipxFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1, 2),
    _IbmipxFilterNumber_Type()
)
ibmipxFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxFilterNumber.setStatus("mandatory")


class _IbmipxFilterValue_Type(OctetString):
    """Custom type ibmipxFilterValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_IbmipxFilterValue_Type.__name__ = "OctetString"
_IbmipxFilterValue_Object = MibTableColumn
ibmipxFilterValue = _IbmipxFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1, 3),
    _IbmipxFilterValue_Type()
)
ibmipxFilterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxFilterValue.setStatus("mandatory")


class _IbmipxFilterMask_Type(OctetString):
    """Custom type ibmipxFilterMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_IbmipxFilterMask_Type.__name__ = "OctetString"
_IbmipxFilterMask_Object = MibTableColumn
ibmipxFilterMask = _IbmipxFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1, 4),
    _IbmipxFilterMask_Type()
)
ibmipxFilterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxFilterMask.setStatus("mandatory")


class _IbmipxFilterType_Type(Integer32):
    """Custom type ibmipxFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmipxFilterType_Type.__name__ = "Integer32"
_IbmipxFilterType_Object = MibTableColumn
ibmipxFilterType = _IbmipxFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1, 5),
    _IbmipxFilterType_Type()
)
ibmipxFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxFilterType.setStatus("mandatory")


class _IbmipxFilterHCCompare_Type(Integer32):
    """Custom type ibmipxFilterHCCompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equal", 4),
          ("greater-than", 6),
          ("greater-than-equal", 5),
          ("less-than", 2),
          ("less-than-equal", 3),
          ("none", 1))
    )


_IbmipxFilterHCCompare_Type.__name__ = "Integer32"
_IbmipxFilterHCCompare_Object = MibTableColumn
ibmipxFilterHCCompare = _IbmipxFilterHCCompare_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1, 6),
    _IbmipxFilterHCCompare_Type()
)
ibmipxFilterHCCompare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxFilterHCCompare.setStatus("mandatory")
_IbmipxFilterUse_Type = Counter32
_IbmipxFilterUse_Object = MibTableColumn
ibmipxFilterUse = _IbmipxFilterUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 36, 1, 7),
    _IbmipxFilterUse_Type()
)
ibmipxFilterUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxFilterUse.setStatus("mandatory")
_IbmipxsapStatInRequests_Type = Counter32
_IbmipxsapStatInRequests_Object = MibScalar
ibmipxsapStatInRequests = _IbmipxsapStatInRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 37),
    _IbmipxsapStatInRequests_Type()
)
ibmipxsapStatInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapStatInRequests.setStatus("mandatory")
_IbmipxsapStatOutRequests_Type = Counter32
_IbmipxsapStatOutRequests_Object = MibScalar
ibmipxsapStatOutRequests = _IbmipxsapStatOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 38),
    _IbmipxsapStatOutRequests_Type()
)
ibmipxsapStatOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapStatOutRequests.setStatus("mandatory")
_IbmipxsapStatInResponses_Type = Counter32
_IbmipxsapStatInResponses_Object = MibScalar
ibmipxsapStatInResponses = _IbmipxsapStatInResponses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 39),
    _IbmipxsapStatInResponses_Type()
)
ibmipxsapStatInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapStatInResponses.setStatus("mandatory")
_IbmipxsapStatOutResponses_Type = Counter32
_IbmipxsapStatOutResponses_Object = MibScalar
ibmipxsapStatOutResponses = _IbmipxsapStatOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 40),
    _IbmipxsapStatOutResponses_Type()
)
ibmipxsapStatOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapStatOutResponses.setStatus("mandatory")
_IbmipxsapStatInErrors_Type = Counter32
_IbmipxsapStatInErrors_Object = MibScalar
ibmipxsapStatInErrors = _IbmipxsapStatInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 41),
    _IbmipxsapStatInErrors_Type()
)
ibmipxsapStatInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapStatInErrors.setStatus("mandatory")
_IbmipxsapStatOutDiscards_Type = Counter32
_IbmipxsapStatOutDiscards_Object = MibScalar
ibmipxsapStatOutDiscards = _IbmipxsapStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 42),
    _IbmipxsapStatOutDiscards_Type()
)
ibmipxsapStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapStatOutDiscards.setStatus("mandatory")
_IbmipxsapServerTable_Object = MibTable
ibmipxsapServerTable = _IbmipxsapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43)
)
if mibBuilder.loadTexts:
    ibmipxsapServerTable.setStatus("mandatory")
_IbmipxsapServerEntry_Object = MibTableRow
ibmipxsapServerEntry = _IbmipxsapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1)
)
ibmipxsapServerEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipxsapServerType"),
    (0, "IBM6611-MIB", "ibmipxsapServerNet"),
    (0, "IBM6611-MIB", "ibmipxsapServerHost"),
    (0, "IBM6611-MIB", "ibmipxsapServerSocket"),
    (0, "IBM6611-MIB", "ibmipxsapServerIndex"),
)
if mibBuilder.loadTexts:
    ibmipxsapServerEntry.setStatus("mandatory")
_IbmipxsapServerType_Type = Integer32
_IbmipxsapServerType_Object = MibTableColumn
ibmipxsapServerType = _IbmipxsapServerType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 1),
    _IbmipxsapServerType_Type()
)
ibmipxsapServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerType.setStatus("mandatory")


class _IbmipxsapServerNet_Type(OctetString):
    """Custom type ibmipxsapServerNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmipxsapServerNet_Type.__name__ = "OctetString"
_IbmipxsapServerNet_Object = MibTableColumn
ibmipxsapServerNet = _IbmipxsapServerNet_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 2),
    _IbmipxsapServerNet_Type()
)
ibmipxsapServerNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerNet.setStatus("mandatory")


class _IbmipxsapServerHost_Type(OctetString):
    """Custom type ibmipxsapServerHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmipxsapServerHost_Type.__name__ = "OctetString"
_IbmipxsapServerHost_Object = MibTableColumn
ibmipxsapServerHost = _IbmipxsapServerHost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 3),
    _IbmipxsapServerHost_Type()
)
ibmipxsapServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerHost.setStatus("mandatory")
_IbmipxsapServerSocket_Type = Integer32
_IbmipxsapServerSocket_Object = MibTableColumn
ibmipxsapServerSocket = _IbmipxsapServerSocket_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 4),
    _IbmipxsapServerSocket_Type()
)
ibmipxsapServerSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerSocket.setStatus("mandatory")
_IbmipxsapServerName_Type = DisplayString
_IbmipxsapServerName_Object = MibTableColumn
ibmipxsapServerName = _IbmipxsapServerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 5),
    _IbmipxsapServerName_Type()
)
ibmipxsapServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerName.setStatus("mandatory")
_IbmipxsapServerAge_Type = Integer32
_IbmipxsapServerAge_Object = MibTableColumn
ibmipxsapServerAge = _IbmipxsapServerAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 6),
    _IbmipxsapServerAge_Type()
)
ibmipxsapServerAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerAge.setStatus("mandatory")
_IbmipxsapServerHops_Type = Integer32
_IbmipxsapServerHops_Object = MibTableColumn
ibmipxsapServerHops = _IbmipxsapServerHops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 7),
    _IbmipxsapServerHops_Type()
)
ibmipxsapServerHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerHops.setStatus("mandatory")
_IbmipxsapServerIfIndex_Type = Integer32
_IbmipxsapServerIfIndex_Object = MibTableColumn
ibmipxsapServerIfIndex = _IbmipxsapServerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 8),
    _IbmipxsapServerIfIndex_Type()
)
ibmipxsapServerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerIfIndex.setStatus("mandatory")
_IbmipxsapServerIndex_Type = Integer32
_IbmipxsapServerIndex_Object = MibTableColumn
ibmipxsapServerIndex = _IbmipxsapServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 9),
    _IbmipxsapServerIndex_Type()
)
ibmipxsapServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerIndex.setStatus("mandatory")
_IbmipxsapServerRequestsFiltered_Type = Counter32
_IbmipxsapServerRequestsFiltered_Object = MibTableColumn
ibmipxsapServerRequestsFiltered = _IbmipxsapServerRequestsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 12, 43, 1, 10),
    _IbmipxsapServerRequestsFiltered_Type()
)
ibmipxsapServerRequestsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipxsapServerRequestsFiltered.setStatus("mandatory")
_Ibmappn_ObjectIdentity = ObjectIdentity
ibmappn = _Ibmappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13)
)
_IbmappnNode_ObjectIdentity = ObjectIdentity
ibmappnNode = _IbmappnNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1)
)
_IbmappnGeneralInfoAndCaps_ObjectIdentity = ObjectIdentity
ibmappnGeneralInfoAndCaps = _IbmappnGeneralInfoAndCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1)
)


class _IbmappnNodeCpName_Type(DisplayString):
    """Custom type ibmappnNodeCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNodeCpName_Type.__name__ = "DisplayString"
_IbmappnNodeCpName_Object = MibScalar
ibmappnNodeCpName = _IbmappnNodeCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 1),
    _IbmappnNodeCpName_Type()
)
ibmappnNodeCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeCpName.setStatus("mandatory")


class _IbmappnNodeNetid_Type(DisplayString):
    """Custom type ibmappnNodeNetid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeNetid_Type.__name__ = "DisplayString"
_IbmappnNodeNetid_Object = MibScalar
ibmappnNodeNetid = _IbmappnNodeNetid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 2),
    _IbmappnNodeNetid_Type()
)
ibmappnNodeNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNetid.setStatus("mandatory")


class _IbmappnNodeBlockNum_Type(DisplayString):
    """Custom type ibmappnNodeBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IbmappnNodeBlockNum_Type.__name__ = "DisplayString"
_IbmappnNodeBlockNum_Object = MibScalar
ibmappnNodeBlockNum = _IbmappnNodeBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 3),
    _IbmappnNodeBlockNum_Type()
)
ibmappnNodeBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeBlockNum.setStatus("mandatory")


class _IbmappnNodeIdNum_Type(DisplayString):
    """Custom type ibmappnNodeIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_IbmappnNodeIdNum_Type.__name__ = "DisplayString"
_IbmappnNodeIdNum_Object = MibScalar
ibmappnNodeIdNum = _IbmappnNodeIdNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 4),
    _IbmappnNodeIdNum_Type()
)
ibmappnNodeIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeIdNum.setStatus("mandatory")


class _IbmappnNodeType_Type(Integer32):
    """Custom type ibmappnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endNode", 2),
          ("len", 4),
          ("networkNode", 1))
    )


_IbmappnNodeType_Type.__name__ = "Integer32"
_IbmappnNodeType_Object = MibScalar
ibmappnNodeType = _IbmappnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 5),
    _IbmappnNodeType_Type()
)
ibmappnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeType.setStatus("mandatory")
_IbmappnNodeUpTime_Type = TimeTicks
_IbmappnNodeUpTime_Object = MibScalar
ibmappnNodeUpTime = _IbmappnNodeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 6),
    _IbmappnNodeUpTime_Type()
)
ibmappnNodeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeUpTime.setStatus("mandatory")


class _IbmappnNodeNegotLs_Type(Integer32):
    """Custom type ibmappnNodeNegotLs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeNegotLs_Type.__name__ = "Integer32"
_IbmappnNodeNegotLs_Object = MibScalar
ibmappnNodeNegotLs = _IbmappnNodeNegotLs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 7),
    _IbmappnNodeNegotLs_Type()
)
ibmappnNodeNegotLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNegotLs.setStatus("mandatory")


class _IbmappnNodeSegReasm_Type(Integer32):
    """Custom type ibmappnNodeSegReasm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeSegReasm_Type.__name__ = "Integer32"
_IbmappnNodeSegReasm_Object = MibScalar
ibmappnNodeSegReasm = _IbmappnNodeSegReasm_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 8),
    _IbmappnNodeSegReasm_Type()
)
ibmappnNodeSegReasm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeSegReasm.setStatus("mandatory")


class _IbmappnNodeBindReasm_Type(Integer32):
    """Custom type ibmappnNodeBindReasm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeBindReasm_Type.__name__ = "Integer32"
_IbmappnNodeBindReasm_Object = MibScalar
ibmappnNodeBindReasm = _IbmappnNodeBindReasm_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 9),
    _IbmappnNodeBindReasm_Type()
)
ibmappnNodeBindReasm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeBindReasm.setStatus("mandatory")


class _IbmappnNodeParallelTg_Type(Integer32):
    """Custom type ibmappnNodeParallelTg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeParallelTg_Type.__name__ = "Integer32"
_IbmappnNodeParallelTg_Object = MibScalar
ibmappnNodeParallelTg = _IbmappnNodeParallelTg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 10),
    _IbmappnNodeParallelTg_Type()
)
ibmappnNodeParallelTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeParallelTg.setStatus("mandatory")


class _IbmappnNodeService_Type(Integer32):
    """Custom type ibmappnNodeService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeService_Type.__name__ = "Integer32"
_IbmappnNodeService_Object = MibScalar
ibmappnNodeService = _IbmappnNodeService_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 11),
    _IbmappnNodeService_Type()
)
ibmappnNodeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeService.setStatus("mandatory")


class _IbmappnNodeAdaptiveBindPacing_Type(Integer32):
    """Custom type ibmappnNodeAdaptiveBindPacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeAdaptiveBindPacing_Type.__name__ = "Integer32"
_IbmappnNodeAdaptiveBindPacing_Object = MibScalar
ibmappnNodeAdaptiveBindPacing = _IbmappnNodeAdaptiveBindPacing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 12),
    _IbmappnNodeAdaptiveBindPacing_Type()
)
ibmappnNodeAdaptiveBindPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeAdaptiveBindPacing.setStatus("mandatory")
_IbmappnNnUniqueInfoAndCaps_ObjectIdentity = ObjectIdentity
ibmappnNnUniqueInfoAndCaps = _IbmappnNnUniqueInfoAndCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2)
)


class _IbmappnNodeNnRcvRegChar_Type(Integer32):
    """Custom type ibmappnNodeNnRcvRegChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeNnRcvRegChar_Type.__name__ = "Integer32"
_IbmappnNodeNnRcvRegChar_Object = MibScalar
ibmappnNodeNnRcvRegChar = _IbmappnNodeNnRcvRegChar_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 1),
    _IbmappnNodeNnRcvRegChar_Type()
)
ibmappnNodeNnRcvRegChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnRcvRegChar.setStatus("mandatory")


class _IbmappnNodeNnGateway_Type(Integer32):
    """Custom type ibmappnNodeNnGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeNnGateway_Type.__name__ = "Integer32"
_IbmappnNodeNnGateway_Object = MibScalar
ibmappnNodeNnGateway = _IbmappnNodeNnGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 2),
    _IbmappnNodeNnGateway_Type()
)
ibmappnNodeNnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnGateway.setStatus("mandatory")


class _IbmappnNodeNnCentralDirectory_Type(Integer32):
    """Custom type ibmappnNodeNnCentralDirectory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeNnCentralDirectory_Type.__name__ = "Integer32"
_IbmappnNodeNnCentralDirectory_Object = MibScalar
ibmappnNodeNnCentralDirectory = _IbmappnNodeNnCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 3),
    _IbmappnNodeNnCentralDirectory_Type()
)
ibmappnNodeNnCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnCentralDirectory.setStatus("mandatory")


class _IbmappnNodeNnTreeCache_Type(Integer32):
    """Custom type ibmappnNodeNnTreeCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeNnTreeCache_Type.__name__ = "Integer32"
_IbmappnNodeNnTreeCache_Object = MibScalar
ibmappnNodeNnTreeCache = _IbmappnNodeNnTreeCache_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 4),
    _IbmappnNodeNnTreeCache_Type()
)
ibmappnNodeNnTreeCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnTreeCache.setStatus("mandatory")


class _IbmappnNodeNnTreeUpdate_Type(Integer32):
    """Custom type ibmappnNodeNnTreeUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeNnTreeUpdate_Type.__name__ = "Integer32"
_IbmappnNodeNnTreeUpdate_Object = MibScalar
ibmappnNodeNnTreeUpdate = _IbmappnNodeNnTreeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 5),
    _IbmappnNodeNnTreeUpdate_Type()
)
ibmappnNodeNnTreeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnTreeUpdate.setStatus("mandatory")
_IbmappnNodeNnRouteAddResist_Type = Integer32
_IbmappnNodeNnRouteAddResist_Object = MibScalar
ibmappnNodeNnRouteAddResist = _IbmappnNodeNnRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 6),
    _IbmappnNodeNnRouteAddResist_Type()
)
ibmappnNodeNnRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnRouteAddResist.setStatus("mandatory")


class _IbmappnNodeNnIsr_Type(Integer32):
    """Custom type ibmappnNodeNnIsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeNnIsr_Type.__name__ = "Integer32"
_IbmappnNodeNnIsr_Object = MibScalar
ibmappnNodeNnIsr = _IbmappnNodeNnIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 7),
    _IbmappnNodeNnIsr_Type()
)
ibmappnNodeNnIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnIsr.setStatus("mandatory")


class _IbmappnNodeNnFrsn_Type(Integer32):
    """Custom type ibmappnNodeNnFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNodeNnFrsn_Type.__name__ = "Integer32"
_IbmappnNodeNnFrsn_Object = MibScalar
ibmappnNodeNnFrsn = _IbmappnNodeNnFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 8),
    _IbmappnNodeNnFrsn_Type()
)
ibmappnNodeNnFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnFrsn.setStatus("mandatory")
_IbmappnEnUniqueCaps_ObjectIdentity = ObjectIdentity
ibmappnEnUniqueCaps = _IbmappnEnUniqueCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3)
)


class _IbmappnNodeEnSegGen_Type(Integer32):
    """Custom type ibmappnNodeEnSegGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeEnSegGen_Type.__name__ = "Integer32"
_IbmappnNodeEnSegGen_Object = MibScalar
ibmappnNodeEnSegGen = _IbmappnNodeEnSegGen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 1),
    _IbmappnNodeEnSegGen_Type()
)
ibmappnNodeEnSegGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnSegGen.setStatus("mandatory")


class _IbmappnNodeEnModeCosMap_Type(Integer32):
    """Custom type ibmappnNodeEnModeCosMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeEnModeCosMap_Type.__name__ = "Integer32"
_IbmappnNodeEnModeCosMap_Object = MibScalar
ibmappnNodeEnModeCosMap = _IbmappnNodeEnModeCosMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 2),
    _IbmappnNodeEnModeCosMap_Type()
)
ibmappnNodeEnModeCosMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnModeCosMap.setStatus("mandatory")


class _IbmappnNodeEnLocateCdinit_Type(Integer32):
    """Custom type ibmappnNodeEnLocateCdinit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeEnLocateCdinit_Type.__name__ = "Integer32"
_IbmappnNodeEnLocateCdinit_Object = MibScalar
ibmappnNodeEnLocateCdinit = _IbmappnNodeEnLocateCdinit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 3),
    _IbmappnNodeEnLocateCdinit_Type()
)
ibmappnNodeEnLocateCdinit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnLocateCdinit.setStatus("mandatory")


class _IbmappnNodeEnSendRegNames_Type(Integer32):
    """Custom type ibmappnNodeEnSendRegNames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeEnSendRegNames_Type.__name__ = "Integer32"
_IbmappnNodeEnSendRegNames_Object = MibScalar
ibmappnNodeEnSendRegNames = _IbmappnNodeEnSendRegNames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 4),
    _IbmappnNodeEnSendRegNames_Type()
)
ibmappnNodeEnSendRegNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnSendRegNames.setStatus("mandatory")


class _IbmappnNodeEnSendRegChar_Type(Integer32):
    """Custom type ibmappnNodeEnSendRegChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeEnSendRegChar_Type.__name__ = "Integer32"
_IbmappnNodeEnSendRegChar_Object = MibScalar
ibmappnNodeEnSendRegChar = _IbmappnNodeEnSendRegChar_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 5),
    _IbmappnNodeEnSendRegChar_Type()
)
ibmappnNodeEnSendRegChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnSendRegChar.setStatus("mandatory")
_IbmappnPortInformation_ObjectIdentity = ObjectIdentity
ibmappnPortInformation = _IbmappnPortInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4)
)
_IbmappnNodePortTable_Object = MibTable
ibmappnNodePortTable = _IbmappnNodePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ibmappnNodePortTable.setStatus("mandatory")
_IbmappnNodePortEntry_Object = MibTableRow
ibmappnNodePortEntry = _IbmappnNodePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1)
)
ibmappnNodePortEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodePortName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortEntry.setStatus("mandatory")


class _IbmappnNodePortName_Type(DisplayString):
    """Custom type ibmappnNodePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortName_Type.__name__ = "DisplayString"
_IbmappnNodePortName_Object = MibTableColumn
ibmappnNodePortName = _IbmappnNodePortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 1),
    _IbmappnNodePortName_Type()
)
ibmappnNodePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortName.setStatus("mandatory")


class _IbmappnNodePortState_Type(Integer32):
    """Custom type ibmappnNodePortState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodePortState_Type.__name__ = "Integer32"
_IbmappnNodePortState_Object = MibTableColumn
ibmappnNodePortState = _IbmappnNodePortState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 2),
    _IbmappnNodePortState_Type()
)
ibmappnNodePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnNodePortState.setStatus("mandatory")


class _IbmappnNodePortDlcType_Type(Integer32):
    """Custom type ibmappnNodePortDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenRing", 6))
    )


_IbmappnNodePortDlcType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcType_Object = MibTableColumn
ibmappnNodePortDlcType = _IbmappnNodePortDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 3),
    _IbmappnNodePortDlcType_Type()
)
ibmappnNodePortDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcType.setStatus("mandatory")


class _IbmappnNodePortPortType_Type(Integer32):
    """Custom type ibmappnNodePortPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("sharedAccessFacilities", 3),
          ("switched", 2))
    )


_IbmappnNodePortPortType_Type.__name__ = "Integer32"
_IbmappnNodePortPortType_Object = MibTableColumn
ibmappnNodePortPortType = _IbmappnNodePortPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 4),
    _IbmappnNodePortPortType_Type()
)
ibmappnNodePortPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortPortType.setStatus("mandatory")


class _IbmappnNodePortSIMRIM_Type(Integer32):
    """Custom type ibmappnNodePortSIMRIM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodePortSIMRIM_Type.__name__ = "Integer32"
_IbmappnNodePortSIMRIM_Object = MibTableColumn
ibmappnNodePortSIMRIM = _IbmappnNodePortSIMRIM_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 5),
    _IbmappnNodePortSIMRIM_Type()
)
ibmappnNodePortSIMRIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortSIMRIM.setStatus("mandatory")


class _IbmappnNodePortLsRole_Type(Integer32):
    """Custom type ibmappnNodePortLsRole based on Integer32"""
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
        *(("abm", 4),
          ("negotiable", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_IbmappnNodePortLsRole_Type.__name__ = "Integer32"
_IbmappnNodePortLsRole_Object = MibTableColumn
ibmappnNodePortLsRole = _IbmappnNodePortLsRole_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 6),
    _IbmappnNodePortLsRole_Type()
)
ibmappnNodePortLsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortLsRole.setStatus("mandatory")
_IbmappnNodePortMaxRcvBtuSize_Type = Integer32
_IbmappnNodePortMaxRcvBtuSize_Object = MibTableColumn
ibmappnNodePortMaxRcvBtuSize = _IbmappnNodePortMaxRcvBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 7),
    _IbmappnNodePortMaxRcvBtuSize_Type()
)
ibmappnNodePortMaxRcvBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortMaxRcvBtuSize.setStatus("mandatory")
_IbmappnNodePortMaxIframeWindow_Type = Integer32
_IbmappnNodePortMaxIframeWindow_Object = MibTableColumn
ibmappnNodePortMaxIframeWindow = _IbmappnNodePortMaxIframeWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 8),
    _IbmappnNodePortMaxIframeWindow_Type()
)
ibmappnNodePortMaxIframeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortMaxIframeWindow.setStatus("mandatory")
_IbmappnNodePortDefLsGoodXids_Type = Counter32
_IbmappnNodePortDefLsGoodXids_Object = MibTableColumn
ibmappnNodePortDefLsGoodXids = _IbmappnNodePortDefLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 9),
    _IbmappnNodePortDefLsGoodXids_Type()
)
ibmappnNodePortDefLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDefLsGoodXids.setStatus("mandatory")
_IbmappnNodePortDefLsBadXids_Type = Counter32
_IbmappnNodePortDefLsBadXids_Object = MibTableColumn
ibmappnNodePortDefLsBadXids = _IbmappnNodePortDefLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 10),
    _IbmappnNodePortDefLsBadXids_Type()
)
ibmappnNodePortDefLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDefLsBadXids.setStatus("mandatory")
_IbmappnNodePortDynLsGoodXids_Type = Counter32
_IbmappnNodePortDynLsGoodXids_Object = MibTableColumn
ibmappnNodePortDynLsGoodXids = _IbmappnNodePortDynLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 11),
    _IbmappnNodePortDynLsGoodXids_Type()
)
ibmappnNodePortDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDynLsGoodXids.setStatus("mandatory")
_IbmappnNodePortDynLsBadXids_Type = Counter32
_IbmappnNodePortDynLsBadXids_Object = MibTableColumn
ibmappnNodePortDynLsBadXids = _IbmappnNodePortDynLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 12),
    _IbmappnNodePortDynLsBadXids_Type()
)
ibmappnNodePortDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDynLsBadXids.setStatus("mandatory")
_IbmappnNodePortSpecific_Type = ObjectIdentifier
_IbmappnNodePortSpecific_Object = MibTableColumn
ibmappnNodePortSpecific = _IbmappnNodePortSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 13),
    _IbmappnNodePortSpecific_Type()
)
ibmappnNodePortSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortSpecific.setStatus("mandatory")
_IbmappnNodePortIpTable_Object = MibTable
ibmappnNodePortIpTable = _IbmappnNodePortIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ibmappnNodePortIpTable.setStatus("mandatory")
_IbmappnNodePortIpEntry_Object = MibTableRow
ibmappnNodePortIpEntry = _IbmappnNodePortIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2, 1)
)
ibmappnNodePortIpEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodePortIpName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortIpEntry.setStatus("mandatory")


class _IbmappnNodePortIpName_Type(DisplayString):
    """Custom type ibmappnNodePortIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortIpName_Type.__name__ = "DisplayString"
_IbmappnNodePortIpName_Object = MibTableColumn
ibmappnNodePortIpName = _IbmappnNodePortIpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2, 1, 1),
    _IbmappnNodePortIpName_Type()
)
ibmappnNodePortIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortIpName.setStatus("mandatory")
_IbmappnNodePortIpPortNum_Type = Integer32
_IbmappnNodePortIpPortNum_Object = MibTableColumn
ibmappnNodePortIpPortNum = _IbmappnNodePortIpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2, 1, 2),
    _IbmappnNodePortIpPortNum_Type()
)
ibmappnNodePortIpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortIpPortNum.setStatus("mandatory")
_IbmappnNodePortDlsTable_Object = MibTable
ibmappnNodePortDlsTable = _IbmappnNodePortDlsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlsTable.setStatus("mandatory")
_IbmappnNodePortDlsEntry_Object = MibTableRow
ibmappnNodePortDlsEntry = _IbmappnNodePortDlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1)
)
ibmappnNodePortDlsEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodePortDlsName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlsEntry.setStatus("mandatory")


class _IbmappnNodePortDlsName_Type(DisplayString):
    """Custom type ibmappnNodePortDlsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortDlsName_Type.__name__ = "DisplayString"
_IbmappnNodePortDlsName_Object = MibTableColumn
ibmappnNodePortDlsName = _IbmappnNodePortDlsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1, 1),
    _IbmappnNodePortDlsName_Type()
)
ibmappnNodePortDlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlsName.setStatus("mandatory")


class _IbmappnNodePortDlsMac_Type(OctetString):
    """Custom type ibmappnNodePortDlsMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodePortDlsMac_Type.__name__ = "OctetString"
_IbmappnNodePortDlsMac_Object = MibTableColumn
ibmappnNodePortDlsMac = _IbmappnNodePortDlsMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1, 2),
    _IbmappnNodePortDlsMac_Type()
)
ibmappnNodePortDlsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlsMac.setStatus("mandatory")


class _IbmappnNodePortDlsSap_Type(OctetString):
    """Custom type ibmappnNodePortDlsSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodePortDlsSap_Type.__name__ = "OctetString"
_IbmappnNodePortDlsSap_Object = MibTableColumn
ibmappnNodePortDlsSap = _IbmappnNodePortDlsSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1, 3),
    _IbmappnNodePortDlsSap_Type()
)
ibmappnNodePortDlsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlsSap.setStatus("mandatory")
_IbmappnNodePortTrTable_Object = MibTable
ibmappnNodePortTrTable = _IbmappnNodePortTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ibmappnNodePortTrTable.setStatus("mandatory")
_IbmappnNodePortTrEntry_Object = MibTableRow
ibmappnNodePortTrEntry = _IbmappnNodePortTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1)
)
ibmappnNodePortTrEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodePortTrName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortTrEntry.setStatus("mandatory")


class _IbmappnNodePortTrName_Type(DisplayString):
    """Custom type ibmappnNodePortTrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortTrName_Type.__name__ = "DisplayString"
_IbmappnNodePortTrName_Object = MibTableColumn
ibmappnNodePortTrName = _IbmappnNodePortTrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1, 1),
    _IbmappnNodePortTrName_Type()
)
ibmappnNodePortTrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortTrName.setStatus("mandatory")


class _IbmappnNodePortTrMac_Type(OctetString):
    """Custom type ibmappnNodePortTrMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodePortTrMac_Type.__name__ = "OctetString"
_IbmappnNodePortTrMac_Object = MibTableColumn
ibmappnNodePortTrMac = _IbmappnNodePortTrMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1, 2),
    _IbmappnNodePortTrMac_Type()
)
ibmappnNodePortTrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortTrMac.setStatus("mandatory")


class _IbmappnNodePortTrSap_Type(OctetString):
    """Custom type ibmappnNodePortTrSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodePortTrSap_Type.__name__ = "OctetString"
_IbmappnNodePortTrSap_Object = MibTableColumn
ibmappnNodePortTrSap = _IbmappnNodePortTrSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1, 3),
    _IbmappnNodePortTrSap_Type()
)
ibmappnNodePortTrSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortTrSap.setStatus("mandatory")
_IbmappnNodePortDlcTraceTable_Object = MibTable
ibmappnNodePortDlcTraceTable = _IbmappnNodePortDlcTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTraceTable.setStatus("mandatory")
_IbmappnNodePortDlcTraceEntry_Object = MibTableRow
ibmappnNodePortDlcTraceEntry = _IbmappnNodePortDlcTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1)
)
ibmappnNodePortDlcTraceEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodePortDlcTracPortName"),
    (0, "IBM6611-MIB", "ibmappnNodePortDlcTracIndex"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTraceEntry.setStatus("mandatory")
_IbmappnNodePortDlcTracPortName_Type = DisplayString
_IbmappnNodePortDlcTracPortName_Object = MibTableColumn
ibmappnNodePortDlcTracPortName = _IbmappnNodePortDlcTracPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 1),
    _IbmappnNodePortDlcTracPortName_Type()
)
ibmappnNodePortDlcTracPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracPortName.setStatus("mandatory")
_IbmappnNodePortDlcTracIndex_Type = Integer32
_IbmappnNodePortDlcTracIndex_Object = MibTableColumn
ibmappnNodePortDlcTracIndex = _IbmappnNodePortDlcTracIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 2),
    _IbmappnNodePortDlcTracIndex_Type()
)
ibmappnNodePortDlcTracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracIndex.setStatus("mandatory")


class _IbmappnNodePortDlcTracDlcType_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenRing", 6))
    )


_IbmappnNodePortDlcTracDlcType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracDlcType_Object = MibTableColumn
ibmappnNodePortDlcTracDlcType = _IbmappnNodePortDlcTracDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 3),
    _IbmappnNodePortDlcTracDlcType_Type()
)
ibmappnNodePortDlcTracDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracDlcType.setStatus("mandatory")
_IbmappnNodePortDlcTracLocalAddr_Type = DisplayString
_IbmappnNodePortDlcTracLocalAddr_Object = MibTableColumn
ibmappnNodePortDlcTracLocalAddr = _IbmappnNodePortDlcTracLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 4),
    _IbmappnNodePortDlcTracLocalAddr_Type()
)
ibmappnNodePortDlcTracLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracLocalAddr.setStatus("mandatory")
_IbmappnNodePortDlcTracRemoteAddr_Type = DisplayString
_IbmappnNodePortDlcTracRemoteAddr_Object = MibTableColumn
ibmappnNodePortDlcTracRemoteAddr = _IbmappnNodePortDlcTracRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 5),
    _IbmappnNodePortDlcTracRemoteAddr_Type()
)
ibmappnNodePortDlcTracRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracRemoteAddr.setStatus("mandatory")


class _IbmappnNodePortDlcTracMsgType_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 4),
          ("indication", 5),
          ("other", 1),
          ("request", 3),
          ("response", 6),
          ("unknown", 2))
    )


_IbmappnNodePortDlcTracMsgType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracMsgType_Object = MibTableColumn
ibmappnNodePortDlcTracMsgType = _IbmappnNodePortDlcTracMsgType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 6),
    _IbmappnNodePortDlcTracMsgType_Type()
)
ibmappnNodePortDlcTracMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracMsgType.setStatus("mandatory")


class _IbmappnNodePortDlcTracCmdType_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracCmdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2012,
              2013,
              2014,
              2015,
              2016,
              2017,
              2018,
              2019,
              2020,
              2021,
              2022,
              2023,
              2024,
              2025,
              2026,
              2027,
              2028,
              2029,
              4122,
              4123,
              4124,
              6001,
              6002,
              6003,
              6004,
              6005,
              6006,
              6007,
              6008,
              6009,
              6010,
              6012,
              6013,
              6014,
              6015,
              6016,
              6017,
              6018,
              6019,
              6020,
              6021,
              6022,
              6023,
              6024,
              6025,
              6026,
              6027,
              6028,
              6029)
        )
    )
    namedValues = NamedValues(
        *(("alterSap", 23),
          ("contFrame", 8),
          ("contedFrame", 9),
          ("curFrame", 3),
          ("dgrmFrame", 6),
          ("dlsIpm", 4124),
          ("dlsTestReq", 4122),
          ("dlsTestRsp", 4123),
          ("enterBusy", 12),
          ("exitBusy", 13),
          ("gnetFrame", 20),
          ("haltFrame", 14),
          ("haltLsNow", 25),
          ("iFrame", 10),
          ("iamOkay", 29),
          ("icrFrame", 4),
          ("ipAlterSap", 2023),
          ("ipContFrame", 2008),
          ("ipContedFrame", 2009),
          ("ipCurFrame", 2003),
          ("ipDgrmFrame", 2006),
          ("ipEnterBusy", 2012),
          ("ipExitBusy", 2013),
          ("ipGnetFrame", 2020),
          ("ipHaltFrame", 2014),
          ("ipHaltLsNow", 2025),
          ("ipIFrame", 2010),
          ("ipIamOkay", 2029),
          ("ipIcrFrame", 2004),
          ("ipLsHalted", 2015),
          ("ipLsRestarted", 2017),
          ("ipMibLsFrame", 2028),
          ("ipNetBioAnq", 2026),
          ("ipNetBioAnr", 2027),
          ("ipNetBioSnq", 2018),
          ("ipNetBioSnr", 2019),
          ("ipNetdFrame", 2021),
          ("ipOobFrame", 2022),
          ("ipRespAck", 2005),
          ("ipRespFrame", 2002),
          ("ipRestartLs", 2016),
          ("ipTestFrame", 2001),
          ("ipTestRsp", 2024),
          ("ipXidFrame", 2007),
          ("lsHalted", 15),
          ("lsRestarted", 17),
          ("mibLsFrame", 28),
          ("netBioAnq", 26),
          ("netBioAnr", 27),
          ("netBioSnq", 18),
          ("netBioSnr", 19),
          ("netdFrame", 21),
          ("oobFrame", 22),
          ("respAck", 5),
          ("respFrame", 2),
          ("restartLs", 16),
          ("testFrame", 1),
          ("testRsp", 24),
          ("trAlterSap", 6023),
          ("trContFrame", 6008),
          ("trContedFrame", 6009),
          ("trCurFrame", 6003),
          ("trDgrmFrame", 6006),
          ("trEnterBusy", 6012),
          ("trExitBusy", 6013),
          ("trGnetFrame", 6020),
          ("trHaltFrame", 6014),
          ("trHaltLsNow", 6025),
          ("trIFrame", 6010),
          ("trIamOkay", 6029),
          ("trIcrFrame", 6004),
          ("trLsHalted", 6015),
          ("trLsRestarted", 6017),
          ("trMibLsFrame", 6028),
          ("trNetBioAnq", 6026),
          ("trNetBioAnr", 6027),
          ("trNetBioSnq", 6018),
          ("trNetBioSnr", 6019),
          ("trNetdFrame", 6021),
          ("trOobFrame", 6022),
          ("trRespAck", 6005),
          ("trRespFrame", 6002),
          ("trRestartLs", 6016),
          ("trTestFrame", 6001),
          ("trTestRsp", 6024),
          ("trXidFrame", 6007),
          ("xidFrame", 7))
    )


_IbmappnNodePortDlcTracCmdType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracCmdType_Object = MibTableColumn
ibmappnNodePortDlcTracCmdType = _IbmappnNodePortDlcTracCmdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 7),
    _IbmappnNodePortDlcTracCmdType_Type()
)
ibmappnNodePortDlcTracCmdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracCmdType.setStatus("mandatory")


class _IbmappnNodePortDlcTracUseWan_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracUseWan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 2),
          ("other", 1),
          ("useLan", 5),
          ("useUnknown", 3),
          ("useWan", 4))
    )


_IbmappnNodePortDlcTracUseWan_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracUseWan_Object = MibTableColumn
ibmappnNodePortDlcTracUseWan = _IbmappnNodePortDlcTracUseWan_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 8),
    _IbmappnNodePortDlcTracUseWan_Type()
)
ibmappnNodePortDlcTracUseWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracUseWan.setStatus("mandatory")
_IbmappnLinkStationInformation_ObjectIdentity = ObjectIdentity
ibmappnLinkStationInformation = _IbmappnLinkStationInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5)
)
_IbmappnNodeLsTable_Object = MibTable
ibmappnNodeLsTable = _IbmappnNodeLsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsTable.setStatus("mandatory")
_IbmappnNodeLsEntry_Object = MibTableRow
ibmappnNodeLsEntry = _IbmappnNodeLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1)
)
ibmappnNodeLsEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodeLsName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsEntry.setStatus("mandatory")


class _IbmappnNodeLsName_Type(DisplayString):
    """Custom type ibmappnNodeLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsName_Type.__name__ = "DisplayString"
_IbmappnNodeLsName_Object = MibTableColumn
ibmappnNodeLsName = _IbmappnNodeLsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 1),
    _IbmappnNodeLsName_Type()
)
ibmappnNodeLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsName.setStatus("mandatory")


class _IbmappnNodeLsPortName_Type(DisplayString):
    """Custom type ibmappnNodeLsPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsPortName_Type.__name__ = "DisplayString"
_IbmappnNodeLsPortName_Object = MibTableColumn
ibmappnNodeLsPortName = _IbmappnNodeLsPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 2),
    _IbmappnNodeLsPortName_Type()
)
ibmappnNodeLsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsPortName.setStatus("mandatory")


class _IbmappnNodeLsDlcType_Type(Integer32):
    """Custom type ibmappnNodeLsDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenRing", 6))
    )


_IbmappnNodeLsDlcType_Type.__name__ = "Integer32"
_IbmappnNodeLsDlcType_Object = MibTableColumn
ibmappnNodeLsDlcType = _IbmappnNodeLsDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 3),
    _IbmappnNodeLsDlcType_Type()
)
ibmappnNodeLsDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDlcType.setStatus("mandatory")


class _IbmappnNodeLsDynamic_Type(Integer32):
    """Custom type ibmappnNodeLsDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeLsDynamic_Type.__name__ = "Integer32"
_IbmappnNodeLsDynamic_Object = MibTableColumn
ibmappnNodeLsDynamic = _IbmappnNodeLsDynamic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 4),
    _IbmappnNodeLsDynamic_Type()
)
ibmappnNodeLsDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDynamic.setStatus("mandatory")


class _IbmappnNodeLsState_Type(Integer32):
    """Custom type ibmappnNodeLsState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsState_Type.__name__ = "Integer32"
_IbmappnNodeLsState_Object = MibTableColumn
ibmappnNodeLsState = _IbmappnNodeLsState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 5),
    _IbmappnNodeLsState_Type()
)
ibmappnNodeLsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnNodeLsState.setStatus("mandatory")


class _IbmappnNodeLsCpName_Type(DisplayString):
    """Custom type ibmappnNodeLsCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNodeLsCpName_Type.__name__ = "DisplayString"
_IbmappnNodeLsCpName_Object = MibTableColumn
ibmappnNodeLsCpName = _IbmappnNodeLsCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 6),
    _IbmappnNodeLsCpName_Type()
)
ibmappnNodeLsCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCpName.setStatus("mandatory")
_IbmappnNodeLsTgNum_Type = Integer32
_IbmappnNodeLsTgNum_Object = MibTableColumn
ibmappnNodeLsTgNum = _IbmappnNodeLsTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 7),
    _IbmappnNodeLsTgNum_Type()
)
ibmappnNodeLsTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTgNum.setStatus("mandatory")


class _IbmappnNodeLsLimResource_Type(Integer32):
    """Custom type ibmappnNodeLsLimResource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeLsLimResource_Type.__name__ = "Integer32"
_IbmappnNodeLsLimResource_Object = MibTableColumn
ibmappnNodeLsLimResource = _IbmappnNodeLsLimResource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 8),
    _IbmappnNodeLsLimResource_Type()
)
ibmappnNodeLsLimResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLimResource.setStatus("mandatory")


class _IbmappnNodeLsMigration_Type(Integer32):
    """Custom type ibmappnNodeLsMigration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeLsMigration_Type.__name__ = "Integer32"
_IbmappnNodeLsMigration_Object = MibTableColumn
ibmappnNodeLsMigration = _IbmappnNodeLsMigration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 9),
    _IbmappnNodeLsMigration_Type()
)
ibmappnNodeLsMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMigration.setStatus("mandatory")


class _IbmappnNodeLsBlockNum_Type(DisplayString):
    """Custom type ibmappnNodeLsBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IbmappnNodeLsBlockNum_Type.__name__ = "DisplayString"
_IbmappnNodeLsBlockNum_Object = MibTableColumn
ibmappnNodeLsBlockNum = _IbmappnNodeLsBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 10),
    _IbmappnNodeLsBlockNum_Type()
)
ibmappnNodeLsBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsBlockNum.setStatus("mandatory")


class _IbmappnNodeLsIdNum_Type(DisplayString):
    """Custom type ibmappnNodeLsIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_IbmappnNodeLsIdNum_Type.__name__ = "DisplayString"
_IbmappnNodeLsIdNum_Object = MibTableColumn
ibmappnNodeLsIdNum = _IbmappnNodeLsIdNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 11),
    _IbmappnNodeLsIdNum_Type()
)
ibmappnNodeLsIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsIdNum.setStatus("mandatory")


class _IbmappnNodeLsCpCpSession_Type(Integer32):
    """Custom type ibmappnNodeLsCpCpSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNodeLsCpCpSession_Type.__name__ = "Integer32"
_IbmappnNodeLsCpCpSession_Object = MibTableColumn
ibmappnNodeLsCpCpSession = _IbmappnNodeLsCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 12),
    _IbmappnNodeLsCpCpSession_Type()
)
ibmappnNodeLsCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCpCpSession.setStatus("mandatory")
_IbmappnNodeLsTargetPacingCount_Type = Integer32
_IbmappnNodeLsTargetPacingCount_Object = MibTableColumn
ibmappnNodeLsTargetPacingCount = _IbmappnNodeLsTargetPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 13),
    _IbmappnNodeLsTargetPacingCount_Type()
)
ibmappnNodeLsTargetPacingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTargetPacingCount.setStatus("mandatory")
_IbmappnNodeLsMaxSendBtuSize_Type = Integer32
_IbmappnNodeLsMaxSendBtuSize_Object = MibTableColumn
ibmappnNodeLsMaxSendBtuSize = _IbmappnNodeLsMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 14),
    _IbmappnNodeLsMaxSendBtuSize_Type()
)
ibmappnNodeLsMaxSendBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMaxSendBtuSize.setStatus("mandatory")
_IbmappnNodeLsEffCap_Type = Integer32
_IbmappnNodeLsEffCap_Object = MibTableColumn
ibmappnNodeLsEffCap = _IbmappnNodeLsEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 15),
    _IbmappnNodeLsEffCap_Type()
)
ibmappnNodeLsEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsEffCap.setStatus("mandatory")


class _IbmappnNodeLsConnCost_Type(Integer32):
    """Custom type ibmappnNodeLsConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsConnCost_Type.__name__ = "Integer32"
_IbmappnNodeLsConnCost_Object = MibTableColumn
ibmappnNodeLsConnCost = _IbmappnNodeLsConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 16),
    _IbmappnNodeLsConnCost_Type()
)
ibmappnNodeLsConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsConnCost.setStatus("mandatory")


class _IbmappnNodeLsByteCost_Type(Integer32):
    """Custom type ibmappnNodeLsByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsByteCost_Type.__name__ = "Integer32"
_IbmappnNodeLsByteCost_Object = MibTableColumn
ibmappnNodeLsByteCost = _IbmappnNodeLsByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 17),
    _IbmappnNodeLsByteCost_Type()
)
ibmappnNodeLsByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsByteCost.setStatus("mandatory")


class _IbmappnNodeLsSecurity_Type(Integer32):
    """Custom type ibmappnNodeLsSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnNodeLsSecurity_Type.__name__ = "Integer32"
_IbmappnNodeLsSecurity_Object = MibTableColumn
ibmappnNodeLsSecurity = _IbmappnNodeLsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 18),
    _IbmappnNodeLsSecurity_Type()
)
ibmappnNodeLsSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsSecurity.setStatus("mandatory")


class _IbmappnNodeLsDelay_Type(Integer32):
    """Custom type ibmappnNodeLsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 1),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnNodeLsDelay_Type.__name__ = "Integer32"
_IbmappnNodeLsDelay_Object = MibTableColumn
ibmappnNodeLsDelay = _IbmappnNodeLsDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 19),
    _IbmappnNodeLsDelay_Type()
)
ibmappnNodeLsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDelay.setStatus("mandatory")


class _IbmappnNodeLsUsr1_Type(Integer32):
    """Custom type ibmappnNodeLsUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsUsr1_Type.__name__ = "Integer32"
_IbmappnNodeLsUsr1_Object = MibTableColumn
ibmappnNodeLsUsr1 = _IbmappnNodeLsUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 20),
    _IbmappnNodeLsUsr1_Type()
)
ibmappnNodeLsUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsUsr1.setStatus("mandatory")


class _IbmappnNodeLsUsr2_Type(Integer32):
    """Custom type ibmappnNodeLsUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsUsr2_Type.__name__ = "Integer32"
_IbmappnNodeLsUsr2_Object = MibTableColumn
ibmappnNodeLsUsr2 = _IbmappnNodeLsUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 21),
    _IbmappnNodeLsUsr2_Type()
)
ibmappnNodeLsUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsUsr2.setStatus("mandatory")


class _IbmappnNodeLsUsr3_Type(Integer32):
    """Custom type ibmappnNodeLsUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsUsr3_Type.__name__ = "Integer32"
_IbmappnNodeLsUsr3_Object = MibTableColumn
ibmappnNodeLsUsr3 = _IbmappnNodeLsUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 22),
    _IbmappnNodeLsUsr3_Type()
)
ibmappnNodeLsUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsUsr3.setStatus("mandatory")
_IbmappnNodeLsInXidBytes_Type = Counter32
_IbmappnNodeLsInXidBytes_Object = MibTableColumn
ibmappnNodeLsInXidBytes = _IbmappnNodeLsInXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 23),
    _IbmappnNodeLsInXidBytes_Type()
)
ibmappnNodeLsInXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInXidBytes.setStatus("mandatory")
_IbmappnNodeLsInMsgBytes_Type = Counter32
_IbmappnNodeLsInMsgBytes_Object = MibTableColumn
ibmappnNodeLsInMsgBytes = _IbmappnNodeLsInMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 24),
    _IbmappnNodeLsInMsgBytes_Type()
)
ibmappnNodeLsInMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInMsgBytes.setStatus("mandatory")
_IbmappnNodeLsInXidFrames_Type = Counter32
_IbmappnNodeLsInXidFrames_Object = MibTableColumn
ibmappnNodeLsInXidFrames = _IbmappnNodeLsInXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 25),
    _IbmappnNodeLsInXidFrames_Type()
)
ibmappnNodeLsInXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInXidFrames.setStatus("mandatory")
_IbmappnNodeLsInMsgFrames_Type = Counter32
_IbmappnNodeLsInMsgFrames_Object = MibTableColumn
ibmappnNodeLsInMsgFrames = _IbmappnNodeLsInMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 26),
    _IbmappnNodeLsInMsgFrames_Type()
)
ibmappnNodeLsInMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInMsgFrames.setStatus("mandatory")
_IbmappnNodeLsOutXidBytes_Type = Counter32
_IbmappnNodeLsOutXidBytes_Object = MibTableColumn
ibmappnNodeLsOutXidBytes = _IbmappnNodeLsOutXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 27),
    _IbmappnNodeLsOutXidBytes_Type()
)
ibmappnNodeLsOutXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutXidBytes.setStatus("mandatory")
_IbmappnNodeLsOutMsgBytes_Type = Counter32
_IbmappnNodeLsOutMsgBytes_Object = MibTableColumn
ibmappnNodeLsOutMsgBytes = _IbmappnNodeLsOutMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 28),
    _IbmappnNodeLsOutMsgBytes_Type()
)
ibmappnNodeLsOutMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutMsgBytes.setStatus("mandatory")
_IbmappnNodeLsOutXidFrames_Type = Counter32
_IbmappnNodeLsOutXidFrames_Object = MibTableColumn
ibmappnNodeLsOutXidFrames = _IbmappnNodeLsOutXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 29),
    _IbmappnNodeLsOutXidFrames_Type()
)
ibmappnNodeLsOutXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutXidFrames.setStatus("mandatory")
_IbmappnNodeLsOutMsgFrames_Type = Counter32
_IbmappnNodeLsOutMsgFrames_Object = MibTableColumn
ibmappnNodeLsOutMsgFrames = _IbmappnNodeLsOutMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 30),
    _IbmappnNodeLsOutMsgFrames_Type()
)
ibmappnNodeLsOutMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutMsgFrames.setStatus("mandatory")
_IbmappnNodeLsEchoRsps_Type = Counter32
_IbmappnNodeLsEchoRsps_Object = MibTableColumn
ibmappnNodeLsEchoRsps = _IbmappnNodeLsEchoRsps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 31),
    _IbmappnNodeLsEchoRsps_Type()
)
ibmappnNodeLsEchoRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsEchoRsps.setStatus("mandatory")
_IbmappnNodeLsCurrentDelay_Type = Integer32
_IbmappnNodeLsCurrentDelay_Object = MibTableColumn
ibmappnNodeLsCurrentDelay = _IbmappnNodeLsCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 32),
    _IbmappnNodeLsCurrentDelay_Type()
)
ibmappnNodeLsCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCurrentDelay.setStatus("mandatory")
_IbmappnNodeLsMaxDelay_Type = Integer32
_IbmappnNodeLsMaxDelay_Object = MibTableColumn
ibmappnNodeLsMaxDelay = _IbmappnNodeLsMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 33),
    _IbmappnNodeLsMaxDelay_Type()
)
ibmappnNodeLsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMaxDelay.setStatus("mandatory")
_IbmappnNodeLsMinDelay_Type = Integer32
_IbmappnNodeLsMinDelay_Object = MibTableColumn
ibmappnNodeLsMinDelay = _IbmappnNodeLsMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 34),
    _IbmappnNodeLsMinDelay_Type()
)
ibmappnNodeLsMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMinDelay.setStatus("mandatory")
_IbmappnNodeLsMaxDelayTime_Type = TimeTicks
_IbmappnNodeLsMaxDelayTime_Object = MibTableColumn
ibmappnNodeLsMaxDelayTime = _IbmappnNodeLsMaxDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 35),
    _IbmappnNodeLsMaxDelayTime_Type()
)
ibmappnNodeLsMaxDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMaxDelayTime.setStatus("mandatory")
_IbmappnNodeLsGoodXids_Type = Counter32
_IbmappnNodeLsGoodXids_Object = MibTableColumn
ibmappnNodeLsGoodXids = _IbmappnNodeLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 36),
    _IbmappnNodeLsGoodXids_Type()
)
ibmappnNodeLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsGoodXids.setStatus("mandatory")
_IbmappnNodeLsBadXids_Type = Counter32
_IbmappnNodeLsBadXids_Object = MibTableColumn
ibmappnNodeLsBadXids = _IbmappnNodeLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 37),
    _IbmappnNodeLsBadXids_Type()
)
ibmappnNodeLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsBadXids.setStatus("mandatory")
_IbmappnNodeLsSpecific_Type = ObjectIdentifier
_IbmappnNodeLsSpecific_Object = MibTableColumn
ibmappnNodeLsSpecific = _IbmappnNodeLsSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 38),
    _IbmappnNodeLsSpecific_Type()
)
ibmappnNodeLsSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsSpecific.setStatus("mandatory")


class _IbmappnNodeLsSubState_Type(Integer32):
    """Custom type ibmappnNodeLsSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("inactive", 1),
          ("pendDeact", 15),
          ("pendRcvConnInd", 12),
          ("pendSendConnRsp", 13),
          ("pendXidExch", 3),
          ("sentActAs", 4),
          ("sentConnReq", 11),
          ("sentConnRsp", 14),
          ("sentCreateTg", 10),
          ("sentDeactAsOrd", 7),
          ("sentDestroyTg", 9),
          ("sentDiscOrd", 8),
          ("sentReqOpnstn", 2),
          ("sentSetMode", 5))
    )


_IbmappnNodeLsSubState_Type.__name__ = "Integer32"
_IbmappnNodeLsSubState_Object = MibTableColumn
ibmappnNodeLsSubState = _IbmappnNodeLsSubState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 39),
    _IbmappnNodeLsSubState_Type()
)
ibmappnNodeLsSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsSubState.setStatus("mandatory")
_IbmappnNodeLsStartTime_Type = TimeTicks
_IbmappnNodeLsStartTime_Object = MibTableColumn
ibmappnNodeLsStartTime = _IbmappnNodeLsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 40),
    _IbmappnNodeLsStartTime_Type()
)
ibmappnNodeLsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStartTime.setStatus("mandatory")
_IbmappnNodeLsActiveTime_Type = TimeTicks
_IbmappnNodeLsActiveTime_Object = MibTableColumn
ibmappnNodeLsActiveTime = _IbmappnNodeLsActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 41),
    _IbmappnNodeLsActiveTime_Type()
)
ibmappnNodeLsActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsActiveTime.setStatus("mandatory")
_IbmappnNodeLsCurrentStateTime_Type = TimeTicks
_IbmappnNodeLsCurrentStateTime_Object = MibTableColumn
ibmappnNodeLsCurrentStateTime = _IbmappnNodeLsCurrentStateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 42),
    _IbmappnNodeLsCurrentStateTime_Type()
)
ibmappnNodeLsCurrentStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCurrentStateTime.setStatus("mandatory")
_IbmappnNodeLsIpTable_Object = MibTable
ibmappnNodeLsIpTable = _IbmappnNodeLsIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsIpTable.setStatus("mandatory")
_IbmappnNodeLsIpEntry_Object = MibTableRow
ibmappnNodeLsIpEntry = _IbmappnNodeLsIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1)
)
ibmappnNodeLsIpEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodeLsIpName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsIpEntry.setStatus("mandatory")


class _IbmappnNodeLsIpName_Type(DisplayString):
    """Custom type ibmappnNodeLsIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsIpName_Type.__name__ = "DisplayString"
_IbmappnNodeLsIpName_Object = MibTableColumn
ibmappnNodeLsIpName = _IbmappnNodeLsIpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 1),
    _IbmappnNodeLsIpName_Type()
)
ibmappnNodeLsIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsIpName.setStatus("mandatory")


class _IbmappnNodeLsIpState_Type(Integer32):
    """Custom type ibmappnNodeLsIpState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsIpState_Type.__name__ = "Integer32"
_IbmappnNodeLsIpState_Object = MibTableColumn
ibmappnNodeLsIpState = _IbmappnNodeLsIpState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 2),
    _IbmappnNodeLsIpState_Type()
)
ibmappnNodeLsIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsIpState.setStatus("mandatory")
_IbmappnNodeLsLocalIpAddr_Type = IpAddress
_IbmappnNodeLsLocalIpAddr_Object = MibTableColumn
ibmappnNodeLsLocalIpAddr = _IbmappnNodeLsLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 3),
    _IbmappnNodeLsLocalIpAddr_Type()
)
ibmappnNodeLsLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalIpAddr.setStatus("mandatory")
_IbmappnNodeLsLocalIpPortNum_Type = Integer32
_IbmappnNodeLsLocalIpPortNum_Object = MibTableColumn
ibmappnNodeLsLocalIpPortNum = _IbmappnNodeLsLocalIpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 4),
    _IbmappnNodeLsLocalIpPortNum_Type()
)
ibmappnNodeLsLocalIpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalIpPortNum.setStatus("mandatory")
_IbmappnNodeLsRemoteIpAddr_Type = IpAddress
_IbmappnNodeLsRemoteIpAddr_Object = MibTableColumn
ibmappnNodeLsRemoteIpAddr = _IbmappnNodeLsRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 5),
    _IbmappnNodeLsRemoteIpAddr_Type()
)
ibmappnNodeLsRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteIpAddr.setStatus("mandatory")
_IbmappnNodeLsRemoteIpPortNum_Type = Integer32
_IbmappnNodeLsRemoteIpPortNum_Object = MibTableColumn
ibmappnNodeLsRemoteIpPortNum = _IbmappnNodeLsRemoteIpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 6),
    _IbmappnNodeLsRemoteIpPortNum_Type()
)
ibmappnNodeLsRemoteIpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteIpPortNum.setStatus("mandatory")
_IbmappnNodeLsDlsTable_Object = MibTable
ibmappnNodeLsDlsTable = _IbmappnNodeLsDlsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsTable.setStatus("mandatory")
_IbmappnNodeLsDlsEntry_Object = MibTableRow
ibmappnNodeLsDlsEntry = _IbmappnNodeLsDlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1)
)
ibmappnNodeLsDlsEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodeLsDlsName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsEntry.setStatus("mandatory")


class _IbmappnNodeLsDlsName_Type(DisplayString):
    """Custom type ibmappnNodeLsDlsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsDlsName_Type.__name__ = "DisplayString"
_IbmappnNodeLsDlsName_Object = MibTableColumn
ibmappnNodeLsDlsName = _IbmappnNodeLsDlsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 1),
    _IbmappnNodeLsDlsName_Type()
)
ibmappnNodeLsDlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsName.setStatus("mandatory")


class _IbmappnNodeLsDlsState_Type(Integer32):
    """Custom type ibmappnNodeLsDlsState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsDlsState_Type.__name__ = "Integer32"
_IbmappnNodeLsDlsState_Object = MibTableColumn
ibmappnNodeLsDlsState = _IbmappnNodeLsDlsState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 2),
    _IbmappnNodeLsDlsState_Type()
)
ibmappnNodeLsDlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsState.setStatus("mandatory")


class _IbmappnNodeLsLocalDlsMac_Type(OctetString):
    """Custom type ibmappnNodeLsLocalDlsMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsLocalDlsMac_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalDlsMac_Object = MibTableColumn
ibmappnNodeLsLocalDlsMac = _IbmappnNodeLsLocalDlsMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 3),
    _IbmappnNodeLsLocalDlsMac_Type()
)
ibmappnNodeLsLocalDlsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalDlsMac.setStatus("mandatory")


class _IbmappnNodeLsLocalDlsSap_Type(OctetString):
    """Custom type ibmappnNodeLsLocalDlsSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsLocalDlsSap_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalDlsSap_Object = MibTableColumn
ibmappnNodeLsLocalDlsSap = _IbmappnNodeLsLocalDlsSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 4),
    _IbmappnNodeLsLocalDlsSap_Type()
)
ibmappnNodeLsLocalDlsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalDlsSap.setStatus("mandatory")


class _IbmappnNodeLsRemoteDlsMac_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteDlsMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsRemoteDlsMac_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteDlsMac_Object = MibTableColumn
ibmappnNodeLsRemoteDlsMac = _IbmappnNodeLsRemoteDlsMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 5),
    _IbmappnNodeLsRemoteDlsMac_Type()
)
ibmappnNodeLsRemoteDlsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteDlsMac.setStatus("mandatory")


class _IbmappnNodeLsRemoteDlsSap_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteDlsSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsRemoteDlsSap_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteDlsSap_Object = MibTableColumn
ibmappnNodeLsRemoteDlsSap = _IbmappnNodeLsRemoteDlsSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 6),
    _IbmappnNodeLsRemoteDlsSap_Type()
)
ibmappnNodeLsRemoteDlsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteDlsSap.setStatus("mandatory")
_IbmappnNodeLsTrTable_Object = MibTable
ibmappnNodeLsTrTable = _IbmappnNodeLsTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsTrTable.setStatus("mandatory")
_IbmappnNodeLsTrEntry_Object = MibTableRow
ibmappnNodeLsTrEntry = _IbmappnNodeLsTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1)
)
ibmappnNodeLsTrEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodeLsTrName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsTrEntry.setStatus("mandatory")


class _IbmappnNodeLsTrName_Type(DisplayString):
    """Custom type ibmappnNodeLsTrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsTrName_Type.__name__ = "DisplayString"
_IbmappnNodeLsTrName_Object = MibTableColumn
ibmappnNodeLsTrName = _IbmappnNodeLsTrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 1),
    _IbmappnNodeLsTrName_Type()
)
ibmappnNodeLsTrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTrName.setStatus("mandatory")


class _IbmappnNodeLsTrState_Type(Integer32):
    """Custom type ibmappnNodeLsTrState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsTrState_Type.__name__ = "Integer32"
_IbmappnNodeLsTrState_Object = MibTableColumn
ibmappnNodeLsTrState = _IbmappnNodeLsTrState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 2),
    _IbmappnNodeLsTrState_Type()
)
ibmappnNodeLsTrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTrState.setStatus("mandatory")


class _IbmappnNodeLsLocalTrMac_Type(OctetString):
    """Custom type ibmappnNodeLsLocalTrMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsLocalTrMac_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalTrMac_Object = MibTableColumn
ibmappnNodeLsLocalTrMac = _IbmappnNodeLsLocalTrMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 3),
    _IbmappnNodeLsLocalTrMac_Type()
)
ibmappnNodeLsLocalTrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalTrMac.setStatus("mandatory")


class _IbmappnNodeLsLocalTrSap_Type(OctetString):
    """Custom type ibmappnNodeLsLocalTrSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsLocalTrSap_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalTrSap_Object = MibTableColumn
ibmappnNodeLsLocalTrSap = _IbmappnNodeLsLocalTrSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 4),
    _IbmappnNodeLsLocalTrSap_Type()
)
ibmappnNodeLsLocalTrSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalTrSap.setStatus("mandatory")


class _IbmappnNodeLsRemoteTrMac_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteTrMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsRemoteTrMac_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteTrMac_Object = MibTableColumn
ibmappnNodeLsRemoteTrMac = _IbmappnNodeLsRemoteTrMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 5),
    _IbmappnNodeLsRemoteTrMac_Type()
)
ibmappnNodeLsRemoteTrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteTrMac.setStatus("mandatory")


class _IbmappnNodeLsRemoteTrSap_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteTrSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsRemoteTrSap_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteTrSap_Object = MibTableColumn
ibmappnNodeLsRemoteTrSap = _IbmappnNodeLsRemoteTrSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 6),
    _IbmappnNodeLsRemoteTrSap_Type()
)
ibmappnNodeLsRemoteTrSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteTrSap.setStatus("mandatory")
_IbmappnNodeLsStatusTable_Object = MibTable
ibmappnNodeLsStatusTable = _IbmappnNodeLsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusTable.setStatus("mandatory")
_IbmappnNodeLsStatusEntry_Object = MibTableRow
ibmappnNodeLsStatusEntry = _IbmappnNodeLsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1)
)
ibmappnNodeLsStatusEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNodeLsStatusIndex"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusEntry.setStatus("mandatory")
_IbmappnNodeLsStatusIndex_Type = Integer32
_IbmappnNodeLsStatusIndex_Object = MibTableColumn
ibmappnNodeLsStatusIndex = _IbmappnNodeLsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 1),
    _IbmappnNodeLsStatusIndex_Type()
)
ibmappnNodeLsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusIndex.setStatus("mandatory")
_IbmappnNodeLsStatusTime_Type = TimeTicks
_IbmappnNodeLsStatusTime_Object = MibTableColumn
ibmappnNodeLsStatusTime = _IbmappnNodeLsStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 2),
    _IbmappnNodeLsStatusTime_Type()
)
ibmappnNodeLsStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusTime.setStatus("mandatory")


class _IbmappnNodeLsStatusLsName_Type(DisplayString):
    """Custom type ibmappnNodeLsStatusLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNodeLsStatusLsName_Type.__name__ = "DisplayString"
_IbmappnNodeLsStatusLsName_Object = MibTableColumn
ibmappnNodeLsStatusLsName = _IbmappnNodeLsStatusLsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 3),
    _IbmappnNodeLsStatusLsName_Type()
)
ibmappnNodeLsStatusLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusLsName.setStatus("mandatory")


class _IbmappnNodeLsStatusCpName_Type(DisplayString):
    """Custom type ibmappnNodeLsStatusCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 18),
    )


_IbmappnNodeLsStatusCpName_Type.__name__ = "DisplayString"
_IbmappnNodeLsStatusCpName_Object = MibTableColumn
ibmappnNodeLsStatusCpName = _IbmappnNodeLsStatusCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 4),
    _IbmappnNodeLsStatusCpName_Type()
)
ibmappnNodeLsStatusCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusCpName.setStatus("mandatory")
_IbmappnNodeLsStatusNodeId_Type = OctetString
_IbmappnNodeLsStatusNodeId_Object = MibTableColumn
ibmappnNodeLsStatusNodeId = _IbmappnNodeLsStatusNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 5),
    _IbmappnNodeLsStatusNodeId_Type()
)
ibmappnNodeLsStatusNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusNodeId.setStatus("mandatory")


class _IbmappnNodeLsStatusTgNum_Type(Integer32):
    """Custom type ibmappnNodeLsStatusTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IbmappnNodeLsStatusTgNum_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusTgNum_Object = MibTableColumn
ibmappnNodeLsStatusTgNum = _IbmappnNodeLsStatusTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 6),
    _IbmappnNodeLsStatusTgNum_Type()
)
ibmappnNodeLsStatusTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusTgNum.setStatus("mandatory")
_IbmappnNodeLsStatusGeneralSense_Type = OctetString
_IbmappnNodeLsStatusGeneralSense_Object = MibTableColumn
ibmappnNodeLsStatusGeneralSense = _IbmappnNodeLsStatusGeneralSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 7),
    _IbmappnNodeLsStatusGeneralSense_Type()
)
ibmappnNodeLsStatusGeneralSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusGeneralSense.setStatus("mandatory")


class _IbmappnNodeLsStatusNofRetry_Type(Integer32):
    """Custom type ibmappnNodeLsStatusNofRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noretry", 2),
          ("retry", 1))
    )


_IbmappnNodeLsStatusNofRetry_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusNofRetry_Object = MibTableColumn
ibmappnNodeLsStatusNofRetry = _IbmappnNodeLsStatusNofRetry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 8),
    _IbmappnNodeLsStatusNofRetry_Type()
)
ibmappnNodeLsStatusNofRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusNofRetry.setStatus("mandatory")
_IbmappnNodeLsStatusEndSense_Type = OctetString
_IbmappnNodeLsStatusEndSense_Object = MibTableColumn
ibmappnNodeLsStatusEndSense = _IbmappnNodeLsStatusEndSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 9),
    _IbmappnNodeLsStatusEndSense_Type()
)
ibmappnNodeLsStatusEndSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusEndSense.setStatus("mandatory")
_IbmappnNodeLsStatusXidLocalSense_Type = OctetString
_IbmappnNodeLsStatusXidLocalSense_Object = MibTableColumn
ibmappnNodeLsStatusXidLocalSense = _IbmappnNodeLsStatusXidLocalSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 10),
    _IbmappnNodeLsStatusXidLocalSense_Type()
)
ibmappnNodeLsStatusXidLocalSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidLocalSense.setStatus("mandatory")
_IbmappnNodeLsStatusXidRemoteSense_Type = OctetString
_IbmappnNodeLsStatusXidRemoteSense_Object = MibTableColumn
ibmappnNodeLsStatusXidRemoteSense = _IbmappnNodeLsStatusXidRemoteSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 11),
    _IbmappnNodeLsStatusXidRemoteSense_Type()
)
ibmappnNodeLsStatusXidRemoteSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidRemoteSense.setStatus("mandatory")


class _IbmappnNodeLsStatusXidByteInError_Type(Integer32):
    """Custom type ibmappnNodeLsStatusXidByteInError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1000
        )
    )
    namedValues = NamedValues(
        ("na", 1000)
    )


_IbmappnNodeLsStatusXidByteInError_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusXidByteInError_Object = MibTableColumn
ibmappnNodeLsStatusXidByteInError = _IbmappnNodeLsStatusXidByteInError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 12),
    _IbmappnNodeLsStatusXidByteInError_Type()
)
ibmappnNodeLsStatusXidByteInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidByteInError.setStatus("mandatory")


class _IbmappnNodeLsStatusXidBitInError_Type(Integer32):
    """Custom type ibmappnNodeLsStatusXidBitInError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("na", 8)
    )


_IbmappnNodeLsStatusXidBitInError_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusXidBitInError_Object = MibTableColumn
ibmappnNodeLsStatusXidBitInError = _IbmappnNodeLsStatusXidBitInError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 13),
    _IbmappnNodeLsStatusXidBitInError_Type()
)
ibmappnNodeLsStatusXidBitInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidBitInError.setStatus("mandatory")


class _IbmappnNodeLsStatusDlcType_Type(Integer32):
    """Custom type ibmappnNodeLsStatusDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tr", 6))
    )


_IbmappnNodeLsStatusDlcType_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusDlcType_Object = MibTableColumn
ibmappnNodeLsStatusDlcType = _IbmappnNodeLsStatusDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 14),
    _IbmappnNodeLsStatusDlcType_Type()
)
ibmappnNodeLsStatusDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusDlcType.setStatus("mandatory")
_IbmappnNodeLsStatusLocalAddr_Type = DisplayString
_IbmappnNodeLsStatusLocalAddr_Object = MibTableColumn
ibmappnNodeLsStatusLocalAddr = _IbmappnNodeLsStatusLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 15),
    _IbmappnNodeLsStatusLocalAddr_Type()
)
ibmappnNodeLsStatusLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusLocalAddr.setStatus("mandatory")
_IbmappnNodeLsStatusRemoteAddr_Type = DisplayString
_IbmappnNodeLsStatusRemoteAddr_Object = MibTableColumn
ibmappnNodeLsStatusRemoteAddr = _IbmappnNodeLsStatusRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 16),
    _IbmappnNodeLsStatusRemoteAddr_Type()
)
ibmappnNodeLsStatusRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusRemoteAddr.setStatus("mandatory")
_IbmappnSnmpInformation_ObjectIdentity = ObjectIdentity
ibmappnSnmpInformation = _IbmappnSnmpInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6)
)
_IbmappnSnmpInPkts_Type = Counter32
_IbmappnSnmpInPkts_Object = MibScalar
ibmappnSnmpInPkts = _IbmappnSnmpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 1),
    _IbmappnSnmpInPkts_Type()
)
ibmappnSnmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInPkts.setStatus("mandatory")
_IbmappnSnmpInGetRequests_Type = Counter32
_IbmappnSnmpInGetRequests_Object = MibScalar
ibmappnSnmpInGetRequests = _IbmappnSnmpInGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 2),
    _IbmappnSnmpInGetRequests_Type()
)
ibmappnSnmpInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetRequests.setStatus("mandatory")
_IbmappnSnmpInGetNexts_Type = Counter32
_IbmappnSnmpInGetNexts_Object = MibScalar
ibmappnSnmpInGetNexts = _IbmappnSnmpInGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 3),
    _IbmappnSnmpInGetNexts_Type()
)
ibmappnSnmpInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetNexts.setStatus("mandatory")
_IbmappnSnmpInSetRequests_Type = Counter32
_IbmappnSnmpInSetRequests_Object = MibScalar
ibmappnSnmpInSetRequests = _IbmappnSnmpInSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 4),
    _IbmappnSnmpInSetRequests_Type()
)
ibmappnSnmpInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInSetRequests.setStatus("mandatory")
_IbmappnSnmpInTotalVars_Type = Counter32
_IbmappnSnmpInTotalVars_Object = MibScalar
ibmappnSnmpInTotalVars = _IbmappnSnmpInTotalVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 5),
    _IbmappnSnmpInTotalVars_Type()
)
ibmappnSnmpInTotalVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInTotalVars.setStatus("mandatory")
_IbmappnSnmpInGetVars_Type = Counter32
_IbmappnSnmpInGetVars_Object = MibScalar
ibmappnSnmpInGetVars = _IbmappnSnmpInGetVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 6),
    _IbmappnSnmpInGetVars_Type()
)
ibmappnSnmpInGetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetVars.setStatus("mandatory")
_IbmappnSnmpInGetNextVars_Type = Counter32
_IbmappnSnmpInGetNextVars_Object = MibScalar
ibmappnSnmpInGetNextVars = _IbmappnSnmpInGetNextVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 7),
    _IbmappnSnmpInGetNextVars_Type()
)
ibmappnSnmpInGetNextVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetNextVars.setStatus("mandatory")
_IbmappnSnmpInSetVars_Type = Counter32
_IbmappnSnmpInSetVars_Object = MibScalar
ibmappnSnmpInSetVars = _IbmappnSnmpInSetVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 8),
    _IbmappnSnmpInSetVars_Type()
)
ibmappnSnmpInSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInSetVars.setStatus("mandatory")
_IbmappnSnmpOutNoSuchNames_Type = Counter32
_IbmappnSnmpOutNoSuchNames_Object = MibScalar
ibmappnSnmpOutNoSuchNames = _IbmappnSnmpOutNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 9),
    _IbmappnSnmpOutNoSuchNames_Type()
)
ibmappnSnmpOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpOutNoSuchNames.setStatus("mandatory")
_IbmappnSnmpOutGenErrs_Type = Counter32
_IbmappnSnmpOutGenErrs_Object = MibScalar
ibmappnSnmpOutGenErrs = _IbmappnSnmpOutGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 10),
    _IbmappnSnmpOutGenErrs_Type()
)
ibmappnSnmpOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpOutGenErrs.setStatus("mandatory")
_IbmappnMemoryUse_ObjectIdentity = ObjectIdentity
ibmappnMemoryUse = _IbmappnMemoryUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7)
)
_IbmappnMemorySize_Type = Integer32
_IbmappnMemorySize_Object = MibScalar
ibmappnMemorySize = _IbmappnMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 1),
    _IbmappnMemorySize_Type()
)
ibmappnMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemorySize.setStatus("mandatory")
_IbmappnMemoryUsed_Type = Integer32
_IbmappnMemoryUsed_Object = MibScalar
ibmappnMemoryUsed = _IbmappnMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 2),
    _IbmappnMemoryUsed_Type()
)
ibmappnMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryUsed.setStatus("mandatory")
_IbmappnMemoryWarnThresh_Type = Integer32
_IbmappnMemoryWarnThresh_Object = MibScalar
ibmappnMemoryWarnThresh = _IbmappnMemoryWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 3),
    _IbmappnMemoryWarnThresh_Type()
)
ibmappnMemoryWarnThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryWarnThresh.setStatus("mandatory")
_IbmappnMemoryCritThresh_Type = Integer32
_IbmappnMemoryCritThresh_Object = MibScalar
ibmappnMemoryCritThresh = _IbmappnMemoryCritThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 4),
    _IbmappnMemoryCritThresh_Type()
)
ibmappnMemoryCritThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryCritThresh.setStatus("mandatory")
_IbmappnXidInformation_ObjectIdentity = ObjectIdentity
ibmappnXidInformation = _IbmappnXidInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8)
)
_IbmappnNodeDefLsGoodXids_Type = Counter32
_IbmappnNodeDefLsGoodXids_Object = MibScalar
ibmappnNodeDefLsGoodXids = _IbmappnNodeDefLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 1),
    _IbmappnNodeDefLsGoodXids_Type()
)
ibmappnNodeDefLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDefLsGoodXids.setStatus("mandatory")
_IbmappnNodeDefLsBadXids_Type = Counter32
_IbmappnNodeDefLsBadXids_Object = MibScalar
ibmappnNodeDefLsBadXids = _IbmappnNodeDefLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 2),
    _IbmappnNodeDefLsBadXids_Type()
)
ibmappnNodeDefLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDefLsBadXids.setStatus("mandatory")
_IbmappnNodeDynLsGoodXids_Type = Counter32
_IbmappnNodeDynLsGoodXids_Object = MibScalar
ibmappnNodeDynLsGoodXids = _IbmappnNodeDynLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 3),
    _IbmappnNodeDynLsGoodXids_Type()
)
ibmappnNodeDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDynLsGoodXids.setStatus("mandatory")
_IbmappnNodeDynLsBadXids_Type = Counter32
_IbmappnNodeDynLsBadXids_Object = MibScalar
ibmappnNodeDynLsBadXids = _IbmappnNodeDynLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 4),
    _IbmappnNodeDynLsBadXids_Type()
)
ibmappnNodeDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDynLsBadXids.setStatus("mandatory")
_IbmappnNn_ObjectIdentity = ObjectIdentity
ibmappnNn = _IbmappnNn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2)
)
_IbmappnNnTopo_ObjectIdentity = ObjectIdentity
ibmappnNnTopo = _IbmappnNnTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1)
)
_IbmappnNnTopoMaxNodes_Type = Integer32
_IbmappnNnTopoMaxNodes_Object = MibScalar
ibmappnNnTopoMaxNodes = _IbmappnNnTopoMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 1),
    _IbmappnNnTopoMaxNodes_Type()
)
ibmappnNnTopoMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoMaxNodes.setStatus("mandatory")
_IbmappnNnTopoCurNumNodes_Type = Gauge32
_IbmappnNnTopoCurNumNodes_Object = MibScalar
ibmappnNnTopoCurNumNodes = _IbmappnNnTopoCurNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 2),
    _IbmappnNnTopoCurNumNodes_Type()
)
ibmappnNnTopoCurNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoCurNumNodes.setStatus("mandatory")
_IbmappnNnTopoInTdus_Type = Counter32
_IbmappnNnTopoInTdus_Object = MibScalar
ibmappnNnTopoInTdus = _IbmappnNnTopoInTdus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 3),
    _IbmappnNnTopoInTdus_Type()
)
ibmappnNnTopoInTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoInTdus.setStatus("mandatory")
_IbmappnNnTopoOutTdus_Type = Counter32
_IbmappnNnTopoOutTdus_Object = MibScalar
ibmappnNnTopoOutTdus = _IbmappnNnTopoOutTdus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 4),
    _IbmappnNnTopoOutTdus_Type()
)
ibmappnNnTopoOutTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoOutTdus.setStatus("mandatory")
_IbmappnNnTopoNodeLowRsns_Type = Counter32
_IbmappnNnTopoNodeLowRsns_Object = MibScalar
ibmappnNnTopoNodeLowRsns = _IbmappnNnTopoNodeLowRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 5),
    _IbmappnNnTopoNodeLowRsns_Type()
)
ibmappnNnTopoNodeLowRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeLowRsns.setStatus("mandatory")
_IbmappnNnTopoNodeEqualRsns_Type = Counter32
_IbmappnNnTopoNodeEqualRsns_Object = MibScalar
ibmappnNnTopoNodeEqualRsns = _IbmappnNnTopoNodeEqualRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 6),
    _IbmappnNnTopoNodeEqualRsns_Type()
)
ibmappnNnTopoNodeEqualRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeEqualRsns.setStatus("mandatory")
_IbmappnNnTopoNodeGoodHighRsns_Type = Counter32
_IbmappnNnTopoNodeGoodHighRsns_Object = MibScalar
ibmappnNnTopoNodeGoodHighRsns = _IbmappnNnTopoNodeGoodHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 7),
    _IbmappnNnTopoNodeGoodHighRsns_Type()
)
ibmappnNnTopoNodeGoodHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeGoodHighRsns.setStatus("mandatory")
_IbmappnNnTopoNodeBadHighRsns_Type = Counter32
_IbmappnNnTopoNodeBadHighRsns_Object = MibScalar
ibmappnNnTopoNodeBadHighRsns = _IbmappnNnTopoNodeBadHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 8),
    _IbmappnNnTopoNodeBadHighRsns_Type()
)
ibmappnNnTopoNodeBadHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeBadHighRsns.setStatus("mandatory")
_IbmappnNnTopoNodeStateUpdates_Type = Counter32
_IbmappnNnTopoNodeStateUpdates_Object = MibScalar
ibmappnNnTopoNodeStateUpdates = _IbmappnNnTopoNodeStateUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 9),
    _IbmappnNnTopoNodeStateUpdates_Type()
)
ibmappnNnTopoNodeStateUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeStateUpdates.setStatus("mandatory")
_IbmappnNnTopoNodeErrors_Type = Counter32
_IbmappnNnTopoNodeErrors_Object = MibScalar
ibmappnNnTopoNodeErrors = _IbmappnNnTopoNodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 10),
    _IbmappnNnTopoNodeErrors_Type()
)
ibmappnNnTopoNodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeErrors.setStatus("mandatory")
_IbmappnNnTopoNodeTimerUpdates_Type = Counter32
_IbmappnNnTopoNodeTimerUpdates_Object = MibScalar
ibmappnNnTopoNodeTimerUpdates = _IbmappnNnTopoNodeTimerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 11),
    _IbmappnNnTopoNodeTimerUpdates_Type()
)
ibmappnNnTopoNodeTimerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeTimerUpdates.setStatus("mandatory")
_IbmappnNnTopoNodePurges_Type = Counter32
_IbmappnNnTopoNodePurges_Object = MibScalar
ibmappnNnTopoNodePurges = _IbmappnNnTopoNodePurges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 12),
    _IbmappnNnTopoNodePurges_Type()
)
ibmappnNnTopoNodePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodePurges.setStatus("mandatory")
_IbmappnNnTopoTgLowRsns_Type = Counter32
_IbmappnNnTopoTgLowRsns_Object = MibScalar
ibmappnNnTopoTgLowRsns = _IbmappnNnTopoTgLowRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 13),
    _IbmappnNnTopoTgLowRsns_Type()
)
ibmappnNnTopoTgLowRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgLowRsns.setStatus("mandatory")
_IbmappnNnTopoTgEqualRsns_Type = Counter32
_IbmappnNnTopoTgEqualRsns_Object = MibScalar
ibmappnNnTopoTgEqualRsns = _IbmappnNnTopoTgEqualRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 14),
    _IbmappnNnTopoTgEqualRsns_Type()
)
ibmappnNnTopoTgEqualRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgEqualRsns.setStatus("mandatory")
_IbmappnNnTopoTgGoodHighRsns_Type = Counter32
_IbmappnNnTopoTgGoodHighRsns_Object = MibScalar
ibmappnNnTopoTgGoodHighRsns = _IbmappnNnTopoTgGoodHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 15),
    _IbmappnNnTopoTgGoodHighRsns_Type()
)
ibmappnNnTopoTgGoodHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgGoodHighRsns.setStatus("mandatory")
_IbmappnNnTopoTgBadHighRsns_Type = Counter32
_IbmappnNnTopoTgBadHighRsns_Object = MibScalar
ibmappnNnTopoTgBadHighRsns = _IbmappnNnTopoTgBadHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 16),
    _IbmappnNnTopoTgBadHighRsns_Type()
)
ibmappnNnTopoTgBadHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgBadHighRsns.setStatus("mandatory")
_IbmappnNnTopoTgStateUpdates_Type = Counter32
_IbmappnNnTopoTgStateUpdates_Object = MibScalar
ibmappnNnTopoTgStateUpdates = _IbmappnNnTopoTgStateUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 17),
    _IbmappnNnTopoTgStateUpdates_Type()
)
ibmappnNnTopoTgStateUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgStateUpdates.setStatus("mandatory")
_IbmappnNnTopoTgErrors_Type = Counter32
_IbmappnNnTopoTgErrors_Object = MibScalar
ibmappnNnTopoTgErrors = _IbmappnNnTopoTgErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 18),
    _IbmappnNnTopoTgErrors_Type()
)
ibmappnNnTopoTgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgErrors.setStatus("mandatory")
_IbmappnNnTopoTgTimerUpdates_Type = Counter32
_IbmappnNnTopoTgTimerUpdates_Object = MibScalar
ibmappnNnTopoTgTimerUpdates = _IbmappnNnTopoTgTimerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 19),
    _IbmappnNnTopoTgTimerUpdates_Type()
)
ibmappnNnTopoTgTimerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgTimerUpdates.setStatus("mandatory")
_IbmappnNnTopoTgPurges_Type = Counter32
_IbmappnNnTopoTgPurges_Object = MibScalar
ibmappnNnTopoTgPurges = _IbmappnNnTopoTgPurges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 20),
    _IbmappnNnTopoTgPurges_Type()
)
ibmappnNnTopoTgPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgPurges.setStatus("mandatory")
_IbmappnNnTopoTotalRouteCalcs_Type = Counter32
_IbmappnNnTopoTotalRouteCalcs_Object = MibScalar
ibmappnNnTopoTotalRouteCalcs = _IbmappnNnTopoTotalRouteCalcs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 21),
    _IbmappnNnTopoTotalRouteCalcs_Type()
)
ibmappnNnTopoTotalRouteCalcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTotalRouteCalcs.setStatus("mandatory")
_IbmappnNnTopoTotalRouteRejs_Type = Counter32
_IbmappnNnTopoTotalRouteRejs_Object = MibScalar
ibmappnNnTopoTotalRouteRejs = _IbmappnNnTopoTotalRouteRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 22),
    _IbmappnNnTopoTotalRouteRejs_Type()
)
ibmappnNnTopoTotalRouteRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTotalRouteRejs.setStatus("mandatory")
_IbmappnNnTopoRouteTable_Object = MibTable
ibmappnNnTopoRouteTable = _IbmappnNnTopoRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23)
)
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteTable.setStatus("mandatory")
_IbmappnNnTopoRouteEntry_Object = MibTableRow
ibmappnNnTopoRouteEntry = _IbmappnNnTopoRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1)
)
ibmappnNnTopoRouteEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNnTopoRouteCos"),
)
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteEntry.setStatus("mandatory")
_IbmappnNnTopoRouteCos_Type = DisplayString
_IbmappnNnTopoRouteCos_Object = MibTableColumn
ibmappnNnTopoRouteCos = _IbmappnNnTopoRouteCos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 1),
    _IbmappnNnTopoRouteCos_Type()
)
ibmappnNnTopoRouteCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteCos.setStatus("mandatory")
_IbmappnNnTopoRouteTrees_Type = Counter32
_IbmappnNnTopoRouteTrees_Object = MibTableColumn
ibmappnNnTopoRouteTrees = _IbmappnNnTopoRouteTrees_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 2),
    _IbmappnNnTopoRouteTrees_Type()
)
ibmappnNnTopoRouteTrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteTrees.setStatus("mandatory")
_IbmappnNnTopoRouteCalcs_Type = Counter32
_IbmappnNnTopoRouteCalcs_Object = MibTableColumn
ibmappnNnTopoRouteCalcs = _IbmappnNnTopoRouteCalcs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 3),
    _IbmappnNnTopoRouteCalcs_Type()
)
ibmappnNnTopoRouteCalcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteCalcs.setStatus("mandatory")
_IbmappnNnTopoRouteRejs_Type = Counter32
_IbmappnNnTopoRouteRejs_Object = MibTableColumn
ibmappnNnTopoRouteRejs = _IbmappnNnTopoRouteRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 4),
    _IbmappnNnTopoRouteRejs_Type()
)
ibmappnNnTopoRouteRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteRejs.setStatus("mandatory")
_IbmappnNnAdjNodeTable_Object = MibTable
ibmappnNnAdjNodeTable = _IbmappnNnAdjNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2)
)
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeTable.setStatus("mandatory")
_IbmappnNnAdjNodeEntry_Object = MibTableRow
ibmappnNnAdjNodeEntry = _IbmappnNnAdjNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1)
)
ibmappnNnAdjNodeEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNnAdjNodeAdjName"),
)
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeEntry.setStatus("mandatory")


class _IbmappnNnAdjNodeAdjName_Type(DisplayString):
    """Custom type ibmappnNnAdjNodeAdjName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnAdjNodeAdjName_Type.__name__ = "DisplayString"
_IbmappnNnAdjNodeAdjName_Object = MibTableColumn
ibmappnNnAdjNodeAdjName = _IbmappnNnAdjNodeAdjName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 1),
    _IbmappnNnAdjNodeAdjName_Type()
)
ibmappnNnAdjNodeAdjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeAdjName.setStatus("mandatory")


class _IbmappnNnAdjNodeCpCpSessStatus_Type(Integer32):
    """Custom type ibmappnNnAdjNodeCpCpSessStatus based on Integer32"""
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
        *(("active", 1),
          ("conLoserActive", 2),
          ("conWinnerActive", 3),
          ("inactive", 4))
    )


_IbmappnNnAdjNodeCpCpSessStatus_Type.__name__ = "Integer32"
_IbmappnNnAdjNodeCpCpSessStatus_Object = MibTableColumn
ibmappnNnAdjNodeCpCpSessStatus = _IbmappnNnAdjNodeCpCpSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 2),
    _IbmappnNnAdjNodeCpCpSessStatus_Type()
)
ibmappnNnAdjNodeCpCpSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeCpCpSessStatus.setStatus("mandatory")
_IbmappnNnAdjNodeOutOfSeqTdus_Type = Gauge32
_IbmappnNnAdjNodeOutOfSeqTdus_Object = MibTableColumn
ibmappnNnAdjNodeOutOfSeqTdus = _IbmappnNnAdjNodeOutOfSeqTdus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 3),
    _IbmappnNnAdjNodeOutOfSeqTdus_Type()
)
ibmappnNnAdjNodeOutOfSeqTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeOutOfSeqTdus.setStatus("mandatory")


class _IbmappnNnAdjNodeLastFrsnSent_Type(Integer32):
    """Custom type ibmappnNnAdjNodeLastFrsnSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnAdjNodeLastFrsnSent_Type.__name__ = "Integer32"
_IbmappnNnAdjNodeLastFrsnSent_Object = MibTableColumn
ibmappnNnAdjNodeLastFrsnSent = _IbmappnNnAdjNodeLastFrsnSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 4),
    _IbmappnNnAdjNodeLastFrsnSent_Type()
)
ibmappnNnAdjNodeLastFrsnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeLastFrsnSent.setStatus("mandatory")


class _IbmappnNnAdjNodeLastFrsnRcvd_Type(Integer32):
    """Custom type ibmappnNnAdjNodeLastFrsnRcvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnAdjNodeLastFrsnRcvd_Type.__name__ = "Integer32"
_IbmappnNnAdjNodeLastFrsnRcvd_Object = MibTableColumn
ibmappnNnAdjNodeLastFrsnRcvd = _IbmappnNnAdjNodeLastFrsnRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 5),
    _IbmappnNnAdjNodeLastFrsnRcvd_Type()
)
ibmappnNnAdjNodeLastFrsnRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeLastFrsnRcvd.setStatus("mandatory")
_IbmappnNnTopology_ObjectIdentity = ObjectIdentity
ibmappnNnTopology = _IbmappnNnTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3)
)
_IbmappnNnTopologyTable_Object = MibTable
ibmappnNnTopologyTable = _IbmappnNnTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyTable.setStatus("mandatory")
_IbmappnNnTopologyEntry_Object = MibTableRow
ibmappnNnTopologyEntry = _IbmappnNnTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1)
)
ibmappnNnTopologyEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNnNodeName"),
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyEntry.setStatus("mandatory")


class _IbmappnNnNodeName_Type(DisplayString):
    """Custom type ibmappnNnNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnNodeName_Type.__name__ = "DisplayString"
_IbmappnNnNodeName_Object = MibTableColumn
ibmappnNnNodeName = _IbmappnNnNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 1),
    _IbmappnNnNodeName_Type()
)
ibmappnNnNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeName.setStatus("mandatory")


class _IbmappnNnNodeFrsn_Type(Integer32):
    """Custom type ibmappnNnNodeFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnNodeFrsn_Type.__name__ = "Integer32"
_IbmappnNnNodeFrsn_Object = MibTableColumn
ibmappnNnNodeFrsn = _IbmappnNnNodeFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 2),
    _IbmappnNnNodeFrsn_Type()
)
ibmappnNnNodeFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFrsn.setStatus("mandatory")


class _IbmappnNnNodeEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnNodeEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnNodeEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnNodeEntryTimeLeft_Object = MibTableColumn
ibmappnNnNodeEntryTimeLeft = _IbmappnNnNodeEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 3),
    _IbmappnNnNodeEntryTimeLeft_Type()
)
ibmappnNnNodeEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeEntryTimeLeft.setStatus("mandatory")


class _IbmappnNnNodeType_Type(Integer32):
    """Custom type ibmappnNnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networknode", 1),
          ("virtualnode", 3))
    )


_IbmappnNnNodeType_Type.__name__ = "Integer32"
_IbmappnNnNodeType_Object = MibTableColumn
ibmappnNnNodeType = _IbmappnNnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 4),
    _IbmappnNnNodeType_Type()
)
ibmappnNnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeType.setStatus("mandatory")
_IbmappnNnNodeRsn_Type = Integer32
_IbmappnNnNodeRsn_Object = MibTableColumn
ibmappnNnNodeRsn = _IbmappnNnNodeRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 5),
    _IbmappnNnNodeRsn_Type()
)
ibmappnNnNodeRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeRsn.setStatus("mandatory")
_IbmappnNnNodeRouteAddResist_Type = Integer32
_IbmappnNnNodeRouteAddResist_Object = MibTableColumn
ibmappnNnNodeRouteAddResist = _IbmappnNnNodeRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 6),
    _IbmappnNnNodeRouteAddResist_Type()
)
ibmappnNnNodeRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeRouteAddResist.setStatus("mandatory")


class _IbmappnNnNodeCongested_Type(Integer32):
    """Custom type ibmappnNnNodeCongested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeCongested_Type.__name__ = "Integer32"
_IbmappnNnNodeCongested_Object = MibTableColumn
ibmappnNnNodeCongested = _IbmappnNnNodeCongested_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 7),
    _IbmappnNnNodeCongested_Type()
)
ibmappnNnNodeCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeCongested.setStatus("mandatory")


class _IbmappnNnNodeIsrDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeIsrDepleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeIsrDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeIsrDepleted_Object = MibTableColumn
ibmappnNnNodeIsrDepleted = _IbmappnNnNodeIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 8),
    _IbmappnNnNodeIsrDepleted_Type()
)
ibmappnNnNodeIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeIsrDepleted.setStatus("mandatory")


class _IbmappnNnNodeEndptDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeEndptDepleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeEndptDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeEndptDepleted_Object = MibTableColumn
ibmappnNnNodeEndptDepleted = _IbmappnNnNodeEndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 9),
    _IbmappnNnNodeEndptDepleted_Type()
)
ibmappnNnNodeEndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeEndptDepleted.setStatus("mandatory")


class _IbmappnNnNodeQuiescing_Type(Integer32):
    """Custom type ibmappnNnNodeQuiescing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeQuiescing_Type.__name__ = "Integer32"
_IbmappnNnNodeQuiescing_Object = MibTableColumn
ibmappnNnNodeQuiescing = _IbmappnNnNodeQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 10),
    _IbmappnNnNodeQuiescing_Type()
)
ibmappnNnNodeQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeQuiescing.setStatus("mandatory")


class _IbmappnNnNodeGateway_Type(Integer32):
    """Custom type ibmappnNnNodeGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeGateway_Type.__name__ = "Integer32"
_IbmappnNnNodeGateway_Object = MibTableColumn
ibmappnNnNodeGateway = _IbmappnNnNodeGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 11),
    _IbmappnNnNodeGateway_Type()
)
ibmappnNnNodeGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeGateway.setStatus("mandatory")


class _IbmappnNnNodeCentralDirectory_Type(Integer32):
    """Custom type ibmappnNnNodeCentralDirectory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeCentralDirectory_Type.__name__ = "Integer32"
_IbmappnNnNodeCentralDirectory_Object = MibTableColumn
ibmappnNnNodeCentralDirectory = _IbmappnNnNodeCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 12),
    _IbmappnNnNodeCentralDirectory_Type()
)
ibmappnNnNodeCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeCentralDirectory.setStatus("mandatory")


class _IbmappnNnNodeIsr_Type(Integer32):
    """Custom type ibmappnNnNodeIsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeIsr_Type.__name__ = "Integer32"
_IbmappnNnNodeIsr_Object = MibTableColumn
ibmappnNnNodeIsr = _IbmappnNnNodeIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 13),
    _IbmappnNnNodeIsr_Type()
)
ibmappnNnNodeIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeIsr.setStatus("mandatory")


class _IbmappnNnNodeChainSupport_Type(Integer32):
    """Custom type ibmappnNnNodeChainSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeChainSupport_Type.__name__ = "Integer32"
_IbmappnNnNodeChainSupport_Object = MibTableColumn
ibmappnNnNodeChainSupport = _IbmappnNnNodeChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 14),
    _IbmappnNnNodeChainSupport_Type()
)
ibmappnNnNodeChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeChainSupport.setStatus("mandatory")
_IbmappnNnTgTopologyTable_Object = MibTable
ibmappnNnTgTopologyTable = _IbmappnNnTgTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyTable.setStatus("mandatory")
_IbmappnNnTgTopologyEntry_Object = MibTableRow
ibmappnNnTgTopologyEntry = _IbmappnNnTgTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1)
)
ibmappnNnTgTopologyEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNnTgOwner"),
    (0, "IBM6611-MIB", "ibmappnNnTgDest"),
    (0, "IBM6611-MIB", "ibmappnNnTgNum"),
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyEntry.setStatus("mandatory")


class _IbmappnNnTgOwner_Type(DisplayString):
    """Custom type ibmappnNnTgOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgOwner_Type.__name__ = "DisplayString"
_IbmappnNnTgOwner_Object = MibTableColumn
ibmappnNnTgOwner = _IbmappnNnTgOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 1),
    _IbmappnNnTgOwner_Type()
)
ibmappnNnTgOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgOwner.setStatus("mandatory")


class _IbmappnNnTgDest_Type(DisplayString):
    """Custom type ibmappnNnTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgDest_Type.__name__ = "DisplayString"
_IbmappnNnTgDest_Object = MibTableColumn
ibmappnNnTgDest = _IbmappnNnTgDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 2),
    _IbmappnNnTgDest_Type()
)
ibmappnNnTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDest.setStatus("mandatory")


class _IbmappnNnTgNum_Type(Integer32):
    """Custom type ibmappnNnTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgNum_Type.__name__ = "Integer32"
_IbmappnNnTgNum_Object = MibTableColumn
ibmappnNnTgNum = _IbmappnNnTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 3),
    _IbmappnNnTgNum_Type()
)
ibmappnNnTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgNum.setStatus("mandatory")


class _IbmappnNnTgFrsn_Type(Integer32):
    """Custom type ibmappnNnTgFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgFrsn_Type.__name__ = "Integer32"
_IbmappnNnTgFrsn_Object = MibTableColumn
ibmappnNnTgFrsn = _IbmappnNnTgFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 4),
    _IbmappnNnTgFrsn_Type()
)
ibmappnNnTgFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFrsn.setStatus("mandatory")


class _IbmappnNnTgEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnTgEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnTgEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnTgEntryTimeLeft_Object = MibTableColumn
ibmappnNnTgEntryTimeLeft = _IbmappnNnTgEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 5),
    _IbmappnNnTgEntryTimeLeft_Type()
)
ibmappnNnTgEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgEntryTimeLeft.setStatus("mandatory")


class _IbmappnNnTgDestVirtual_Type(Integer32):
    """Custom type ibmappnNnTgDestVirtual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgDestVirtual_Type.__name__ = "Integer32"
_IbmappnNnTgDestVirtual_Object = MibTableColumn
ibmappnNnTgDestVirtual = _IbmappnNnTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 6),
    _IbmappnNnTgDestVirtual_Type()
)
ibmappnNnTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDestVirtual.setStatus("mandatory")


class _IbmappnNnTgDlcData_Type(OctetString):
    """Custom type ibmappnNnTgDlcData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_IbmappnNnTgDlcData_Type.__name__ = "OctetString"
_IbmappnNnTgDlcData_Object = MibTableColumn
ibmappnNnTgDlcData = _IbmappnNnTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 7),
    _IbmappnNnTgDlcData_Type()
)
ibmappnNnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDlcData.setStatus("mandatory")
_IbmappnNnTgRsn_Type = Integer32
_IbmappnNnTgRsn_Object = MibTableColumn
ibmappnNnTgRsn = _IbmappnNnTgRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 8),
    _IbmappnNnTgRsn_Type()
)
ibmappnNnTgRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgRsn.setStatus("mandatory")


class _IbmappnNnTgOperational_Type(Integer32):
    """Custom type ibmappnNnTgOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgOperational_Type.__name__ = "Integer32"
_IbmappnNnTgOperational_Object = MibTableColumn
ibmappnNnTgOperational = _IbmappnNnTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 9),
    _IbmappnNnTgOperational_Type()
)
ibmappnNnTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgOperational.setStatus("mandatory")


class _IbmappnNnTgQuiescing_Type(Integer32):
    """Custom type ibmappnNnTgQuiescing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgQuiescing_Type.__name__ = "Integer32"
_IbmappnNnTgQuiescing_Object = MibTableColumn
ibmappnNnTgQuiescing = _IbmappnNnTgQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 10),
    _IbmappnNnTgQuiescing_Type()
)
ibmappnNnTgQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgQuiescing.setStatus("mandatory")


class _IbmappnNnTgCpCpSession_Type(Integer32):
    """Custom type ibmappnNnTgCpCpSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgCpCpSession_Type.__name__ = "Integer32"
_IbmappnNnTgCpCpSession_Object = MibTableColumn
ibmappnNnTgCpCpSession = _IbmappnNnTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 11),
    _IbmappnNnTgCpCpSession_Type()
)
ibmappnNnTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgCpCpSession.setStatus("mandatory")
_IbmappnNnTgEffCap_Type = Integer32
_IbmappnNnTgEffCap_Object = MibTableColumn
ibmappnNnTgEffCap = _IbmappnNnTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 12),
    _IbmappnNnTgEffCap_Type()
)
ibmappnNnTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgEffCap.setStatus("mandatory")


class _IbmappnNnTgConnCost_Type(Integer32):
    """Custom type ibmappnNnTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgConnCost_Type.__name__ = "Integer32"
_IbmappnNnTgConnCost_Object = MibTableColumn
ibmappnNnTgConnCost = _IbmappnNnTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 13),
    _IbmappnNnTgConnCost_Type()
)
ibmappnNnTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgConnCost.setStatus("mandatory")


class _IbmappnNnTgByteCost_Type(Integer32):
    """Custom type ibmappnNnTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgByteCost_Type.__name__ = "Integer32"
_IbmappnNnTgByteCost_Object = MibTableColumn
ibmappnNnTgByteCost = _IbmappnNnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 14),
    _IbmappnNnTgByteCost_Type()
)
ibmappnNnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgByteCost.setStatus("mandatory")


class _IbmappnNnTgSecurity_Type(Integer32):
    """Custom type ibmappnNnTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnNnTgSecurity_Type.__name__ = "Integer32"
_IbmappnNnTgSecurity_Object = MibTableColumn
ibmappnNnTgSecurity = _IbmappnNnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 15),
    _IbmappnNnTgSecurity_Type()
)
ibmappnNnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgSecurity.setStatus("mandatory")


class _IbmappnNnTgDelay_Type(Integer32):
    """Custom type ibmappnNnTgDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 1),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnNnTgDelay_Type.__name__ = "Integer32"
_IbmappnNnTgDelay_Object = MibTableColumn
ibmappnNnTgDelay = _IbmappnNnTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 16),
    _IbmappnNnTgDelay_Type()
)
ibmappnNnTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDelay.setStatus("mandatory")


class _IbmappnNnTgModemClass_Type(Integer32):
    """Custom type ibmappnNnTgModemClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgModemClass_Type.__name__ = "Integer32"
_IbmappnNnTgModemClass_Object = MibTableColumn
ibmappnNnTgModemClass = _IbmappnNnTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 17),
    _IbmappnNnTgModemClass_Type()
)
ibmappnNnTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgModemClass.setStatus("mandatory")


class _IbmappnNnTgUsr1_Type(Integer32):
    """Custom type ibmappnNnTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgUsr1_Type.__name__ = "Integer32"
_IbmappnNnTgUsr1_Object = MibTableColumn
ibmappnNnTgUsr1 = _IbmappnNnTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 18),
    _IbmappnNnTgUsr1_Type()
)
ibmappnNnTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgUsr1.setStatus("mandatory")


class _IbmappnNnTgUsr2_Type(Integer32):
    """Custom type ibmappnNnTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgUsr2_Type.__name__ = "Integer32"
_IbmappnNnTgUsr2_Object = MibTableColumn
ibmappnNnTgUsr2 = _IbmappnNnTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 19),
    _IbmappnNnTgUsr2_Type()
)
ibmappnNnTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgUsr2.setStatus("mandatory")


class _IbmappnNnTgUsr3_Type(Integer32):
    """Custom type ibmappnNnTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgUsr3_Type.__name__ = "Integer32"
_IbmappnNnTgUsr3_Object = MibTableColumn
ibmappnNnTgUsr3 = _IbmappnNnTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 20),
    _IbmappnNnTgUsr3_Type()
)
ibmappnNnTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgUsr3.setStatus("mandatory")
_IbmappnNnTopologyFRTable_Object = MibTable
ibmappnNnTopologyFRTable = _IbmappnNnTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyFRTable.setStatus("mandatory")
_IbmappnNnTopologyFREntry_Object = MibTableRow
ibmappnNnTopologyFREntry = _IbmappnNnTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1)
)
ibmappnNnTopologyFREntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNnNodeFRFrsn"),
    (0, "IBM6611-MIB", "ibmappnNnNodeFRName"),
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyFREntry.setStatus("mandatory")


class _IbmappnNnNodeFRName_Type(DisplayString):
    """Custom type ibmappnNnNodeFRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnNodeFRName_Type.__name__ = "DisplayString"
_IbmappnNnNodeFRName_Object = MibTableColumn
ibmappnNnNodeFRName = _IbmappnNnNodeFRName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 1),
    _IbmappnNnNodeFRName_Type()
)
ibmappnNnNodeFRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRName.setStatus("mandatory")


class _IbmappnNnNodeFRFrsn_Type(Integer32):
    """Custom type ibmappnNnNodeFRFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnNodeFRFrsn_Type.__name__ = "Integer32"
_IbmappnNnNodeFRFrsn_Object = MibTableColumn
ibmappnNnNodeFRFrsn = _IbmappnNnNodeFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 2),
    _IbmappnNnNodeFRFrsn_Type()
)
ibmappnNnNodeFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRFrsn.setStatus("mandatory")


class _IbmappnNnNodeFREntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnNodeFREntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnNodeFREntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnNodeFREntryTimeLeft_Object = MibTableColumn
ibmappnNnNodeFREntryTimeLeft = _IbmappnNnNodeFREntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 3),
    _IbmappnNnNodeFREntryTimeLeft_Type()
)
ibmappnNnNodeFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFREntryTimeLeft.setStatus("mandatory")


class _IbmappnNnNodeFRType_Type(Integer32):
    """Custom type ibmappnNnNodeFRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networknode", 1),
          ("virtualnode", 3))
    )


_IbmappnNnNodeFRType_Type.__name__ = "Integer32"
_IbmappnNnNodeFRType_Object = MibTableColumn
ibmappnNnNodeFRType = _IbmappnNnNodeFRType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 4),
    _IbmappnNnNodeFRType_Type()
)
ibmappnNnNodeFRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRType.setStatus("mandatory")
_IbmappnNnNodeFRRsn_Type = Integer32
_IbmappnNnNodeFRRsn_Object = MibTableColumn
ibmappnNnNodeFRRsn = _IbmappnNnNodeFRRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 5),
    _IbmappnNnNodeFRRsn_Type()
)
ibmappnNnNodeFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRRsn.setStatus("mandatory")
_IbmappnNnNodeFRRouteAddResist_Type = Integer32
_IbmappnNnNodeFRRouteAddResist_Object = MibTableColumn
ibmappnNnNodeFRRouteAddResist = _IbmappnNnNodeFRRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 6),
    _IbmappnNnNodeFRRouteAddResist_Type()
)
ibmappnNnNodeFRRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRRouteAddResist.setStatus("mandatory")


class _IbmappnNnNodeFRCongested_Type(Integer32):
    """Custom type ibmappnNnNodeFRCongested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFRCongested_Type.__name__ = "Integer32"
_IbmappnNnNodeFRCongested_Object = MibTableColumn
ibmappnNnNodeFRCongested = _IbmappnNnNodeFRCongested_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 7),
    _IbmappnNnNodeFRCongested_Type()
)
ibmappnNnNodeFRCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRCongested.setStatus("mandatory")


class _IbmappnNnNodeFRIsrDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeFRIsrDepleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFRIsrDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeFRIsrDepleted_Object = MibTableColumn
ibmappnNnNodeFRIsrDepleted = _IbmappnNnNodeFRIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 8),
    _IbmappnNnNodeFRIsrDepleted_Type()
)
ibmappnNnNodeFRIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRIsrDepleted.setStatus("mandatory")


class _IbmappnNnNodeFREndptDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeFREndptDepleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFREndptDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeFREndptDepleted_Object = MibTableColumn
ibmappnNnNodeFREndptDepleted = _IbmappnNnNodeFREndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 9),
    _IbmappnNnNodeFREndptDepleted_Type()
)
ibmappnNnNodeFREndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFREndptDepleted.setStatus("mandatory")


class _IbmappnNnNodeFRQuiescing_Type(Integer32):
    """Custom type ibmappnNnNodeFRQuiescing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFRQuiescing_Type.__name__ = "Integer32"
_IbmappnNnNodeFRQuiescing_Object = MibTableColumn
ibmappnNnNodeFRQuiescing = _IbmappnNnNodeFRQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 10),
    _IbmappnNnNodeFRQuiescing_Type()
)
ibmappnNnNodeFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRQuiescing.setStatus("mandatory")


class _IbmappnNnNodeFRGateway_Type(Integer32):
    """Custom type ibmappnNnNodeFRGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFRGateway_Type.__name__ = "Integer32"
_IbmappnNnNodeFRGateway_Object = MibTableColumn
ibmappnNnNodeFRGateway = _IbmappnNnNodeFRGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 11),
    _IbmappnNnNodeFRGateway_Type()
)
ibmappnNnNodeFRGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRGateway.setStatus("mandatory")


class _IbmappnNnNodeFRCentralDirectory_Type(Integer32):
    """Custom type ibmappnNnNodeFRCentralDirectory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFRCentralDirectory_Type.__name__ = "Integer32"
_IbmappnNnNodeFRCentralDirectory_Object = MibTableColumn
ibmappnNnNodeFRCentralDirectory = _IbmappnNnNodeFRCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 12),
    _IbmappnNnNodeFRCentralDirectory_Type()
)
ibmappnNnNodeFRCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRCentralDirectory.setStatus("mandatory")


class _IbmappnNnNodeFRIsr_Type(Integer32):
    """Custom type ibmappnNnNodeFRIsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFRIsr_Type.__name__ = "Integer32"
_IbmappnNnNodeFRIsr_Object = MibTableColumn
ibmappnNnNodeFRIsr = _IbmappnNnNodeFRIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 13),
    _IbmappnNnNodeFRIsr_Type()
)
ibmappnNnNodeFRIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRIsr.setStatus("mandatory")


class _IbmappnNnNodeFRChainSupport_Type(Integer32):
    """Custom type ibmappnNnNodeFRChainSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnNodeFRChainSupport_Type.__name__ = "Integer32"
_IbmappnNnNodeFRChainSupport_Object = MibTableColumn
ibmappnNnNodeFRChainSupport = _IbmappnNnNodeFRChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 14),
    _IbmappnNnNodeFRChainSupport_Type()
)
ibmappnNnNodeFRChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRChainSupport.setStatus("mandatory")
_IbmappnNnTgTopologyFRTable_Object = MibTable
ibmappnNnTgTopologyFRTable = _IbmappnNnTgTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4)
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyFRTable.setStatus("mandatory")
_IbmappnNnTgTopologyFREntry_Object = MibTableRow
ibmappnNnTgTopologyFREntry = _IbmappnNnTgTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1)
)
ibmappnNnTgTopologyFREntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnNnTgFRFrsn"),
    (0, "IBM6611-MIB", "ibmappnNnTgFROwner"),
    (0, "IBM6611-MIB", "ibmappnNnTgFRDest"),
    (0, "IBM6611-MIB", "ibmappnNnTgFRNum"),
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyFREntry.setStatus("mandatory")


class _IbmappnNnTgFROwner_Type(DisplayString):
    """Custom type ibmappnNnTgFROwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgFROwner_Type.__name__ = "DisplayString"
_IbmappnNnTgFROwner_Object = MibTableColumn
ibmappnNnTgFROwner = _IbmappnNnTgFROwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 1),
    _IbmappnNnTgFROwner_Type()
)
ibmappnNnTgFROwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFROwner.setStatus("mandatory")


class _IbmappnNnTgFRDest_Type(DisplayString):
    """Custom type ibmappnNnTgFRDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgFRDest_Type.__name__ = "DisplayString"
_IbmappnNnTgFRDest_Object = MibTableColumn
ibmappnNnTgFRDest = _IbmappnNnTgFRDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 2),
    _IbmappnNnTgFRDest_Type()
)
ibmappnNnTgFRDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDest.setStatus("mandatory")


class _IbmappnNnTgFRNum_Type(Integer32):
    """Custom type ibmappnNnTgFRNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRNum_Type.__name__ = "Integer32"
_IbmappnNnTgFRNum_Object = MibTableColumn
ibmappnNnTgFRNum = _IbmappnNnTgFRNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 3),
    _IbmappnNnTgFRNum_Type()
)
ibmappnNnTgFRNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRNum.setStatus("mandatory")


class _IbmappnNnTgFRFrsn_Type(Integer32):
    """Custom type ibmappnNnTgFRFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgFRFrsn_Type.__name__ = "Integer32"
_IbmappnNnTgFRFrsn_Object = MibTableColumn
ibmappnNnTgFRFrsn = _IbmappnNnTgFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 4),
    _IbmappnNnTgFRFrsn_Type()
)
ibmappnNnTgFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRFrsn.setStatus("mandatory")


class _IbmappnNnTgFREntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnTgFREntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnTgFREntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnTgFREntryTimeLeft_Object = MibTableColumn
ibmappnNnTgFREntryTimeLeft = _IbmappnNnTgFREntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 5),
    _IbmappnNnTgFREntryTimeLeft_Type()
)
ibmappnNnTgFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFREntryTimeLeft.setStatus("mandatory")


class _IbmappnNnTgFRDestVirtual_Type(Integer32):
    """Custom type ibmappnNnTgFRDestVirtual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgFRDestVirtual_Type.__name__ = "Integer32"
_IbmappnNnTgFRDestVirtual_Object = MibTableColumn
ibmappnNnTgFRDestVirtual = _IbmappnNnTgFRDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 6),
    _IbmappnNnTgFRDestVirtual_Type()
)
ibmappnNnTgFRDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDestVirtual.setStatus("mandatory")


class _IbmappnNnTgFRDlcData_Type(OctetString):
    """Custom type ibmappnNnTgFRDlcData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_IbmappnNnTgFRDlcData_Type.__name__ = "OctetString"
_IbmappnNnTgFRDlcData_Object = MibTableColumn
ibmappnNnTgFRDlcData = _IbmappnNnTgFRDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 7),
    _IbmappnNnTgFRDlcData_Type()
)
ibmappnNnTgFRDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDlcData.setStatus("mandatory")
_IbmappnNnTgFRRsn_Type = Integer32
_IbmappnNnTgFRRsn_Object = MibTableColumn
ibmappnNnTgFRRsn = _IbmappnNnTgFRRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 8),
    _IbmappnNnTgFRRsn_Type()
)
ibmappnNnTgFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRRsn.setStatus("mandatory")


class _IbmappnNnTgFROperational_Type(Integer32):
    """Custom type ibmappnNnTgFROperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgFROperational_Type.__name__ = "Integer32"
_IbmappnNnTgFROperational_Object = MibTableColumn
ibmappnNnTgFROperational = _IbmappnNnTgFROperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 9),
    _IbmappnNnTgFROperational_Type()
)
ibmappnNnTgFROperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFROperational.setStatus("mandatory")


class _IbmappnNnTgFRQuiescing_Type(Integer32):
    """Custom type ibmappnNnTgFRQuiescing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgFRQuiescing_Type.__name__ = "Integer32"
_IbmappnNnTgFRQuiescing_Object = MibTableColumn
ibmappnNnTgFRQuiescing = _IbmappnNnTgFRQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 10),
    _IbmappnNnTgFRQuiescing_Type()
)
ibmappnNnTgFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRQuiescing.setStatus("mandatory")


class _IbmappnNnTgFRCpCpSession_Type(Integer32):
    """Custom type ibmappnNnTgFRCpCpSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnNnTgFRCpCpSession_Type.__name__ = "Integer32"
_IbmappnNnTgFRCpCpSession_Object = MibTableColumn
ibmappnNnTgFRCpCpSession = _IbmappnNnTgFRCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 11),
    _IbmappnNnTgFRCpCpSession_Type()
)
ibmappnNnTgFRCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRCpCpSession.setStatus("mandatory")
_IbmappnNnTgFREffCap_Type = Integer32
_IbmappnNnTgFREffCap_Object = MibTableColumn
ibmappnNnTgFREffCap = _IbmappnNnTgFREffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 12),
    _IbmappnNnTgFREffCap_Type()
)
ibmappnNnTgFREffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFREffCap.setStatus("mandatory")


class _IbmappnNnTgFRConnCost_Type(Integer32):
    """Custom type ibmappnNnTgFRConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRConnCost_Type.__name__ = "Integer32"
_IbmappnNnTgFRConnCost_Object = MibTableColumn
ibmappnNnTgFRConnCost = _IbmappnNnTgFRConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 13),
    _IbmappnNnTgFRConnCost_Type()
)
ibmappnNnTgFRConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRConnCost.setStatus("mandatory")


class _IbmappnNnTgFRByteCost_Type(Integer32):
    """Custom type ibmappnNnTgFRByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRByteCost_Type.__name__ = "Integer32"
_IbmappnNnTgFRByteCost_Object = MibTableColumn
ibmappnNnTgFRByteCost = _IbmappnNnTgFRByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 14),
    _IbmappnNnTgFRByteCost_Type()
)
ibmappnNnTgFRByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRByteCost.setStatus("mandatory")


class _IbmappnNnTgFRSecurity_Type(Integer32):
    """Custom type ibmappnNnTgFRSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnNnTgFRSecurity_Type.__name__ = "Integer32"
_IbmappnNnTgFRSecurity_Object = MibTableColumn
ibmappnNnTgFRSecurity = _IbmappnNnTgFRSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 15),
    _IbmappnNnTgFRSecurity_Type()
)
ibmappnNnTgFRSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRSecurity.setStatus("mandatory")


class _IbmappnNnTgFRDelay_Type(Integer32):
    """Custom type ibmappnNnTgFRDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 1),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnNnTgFRDelay_Type.__name__ = "Integer32"
_IbmappnNnTgFRDelay_Object = MibTableColumn
ibmappnNnTgFRDelay = _IbmappnNnTgFRDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 16),
    _IbmappnNnTgFRDelay_Type()
)
ibmappnNnTgFRDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDelay.setStatus("mandatory")


class _IbmappnNnTgFRModemClass_Type(Integer32):
    """Custom type ibmappnNnTgFRModemClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgFRModemClass_Type.__name__ = "Integer32"
_IbmappnNnTgFRModemClass_Object = MibTableColumn
ibmappnNnTgFRModemClass = _IbmappnNnTgFRModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 17),
    _IbmappnNnTgFRModemClass_Type()
)
ibmappnNnTgFRModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRModemClass.setStatus("mandatory")


class _IbmappnNnTgFRUsr1_Type(Integer32):
    """Custom type ibmappnNnTgFRUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRUsr1_Type.__name__ = "Integer32"
_IbmappnNnTgFRUsr1_Object = MibTableColumn
ibmappnNnTgFRUsr1 = _IbmappnNnTgFRUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 18),
    _IbmappnNnTgFRUsr1_Type()
)
ibmappnNnTgFRUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRUsr1.setStatus("mandatory")


class _IbmappnNnTgFRUsr2_Type(Integer32):
    """Custom type ibmappnNnTgFRUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRUsr2_Type.__name__ = "Integer32"
_IbmappnNnTgFRUsr2_Object = MibTableColumn
ibmappnNnTgFRUsr2 = _IbmappnNnTgFRUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 19),
    _IbmappnNnTgFRUsr2_Type()
)
ibmappnNnTgFRUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRUsr2.setStatus("mandatory")


class _IbmappnNnTgFRUsr3_Type(Integer32):
    """Custom type ibmappnNnTgFRUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRUsr3_Type.__name__ = "Integer32"
_IbmappnNnTgFRUsr3_Object = MibTableColumn
ibmappnNnTgFRUsr3 = _IbmappnNnTgFRUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 20),
    _IbmappnNnTgFRUsr3_Type()
)
ibmappnNnTgFRUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRUsr3.setStatus("mandatory")
_IbmappnLocalTopology_ObjectIdentity = ObjectIdentity
ibmappnLocalTopology = _IbmappnLocalTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3)
)
_IbmappnLocalThisNode_ObjectIdentity = ObjectIdentity
ibmappnLocalThisNode = _IbmappnLocalThisNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1)
)
_IbmappnLocalGeneral_ObjectIdentity = ObjectIdentity
ibmappnLocalGeneral = _IbmappnLocalGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 1)
)


class _IbmappnLocalNodeName_Type(DisplayString):
    """Custom type ibmappnLocalNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalNodeName_Type.__name__ = "DisplayString"
_IbmappnLocalNodeName_Object = MibScalar
ibmappnLocalNodeName = _IbmappnLocalNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 1, 1),
    _IbmappnLocalNodeName_Type()
)
ibmappnLocalNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNodeName.setStatus("mandatory")


class _IbmappnLocalNodeType_Type(Integer32):
    """Custom type ibmappnLocalNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endnode", 2),
          ("len", 4),
          ("networknode", 1))
    )


_IbmappnLocalNodeType_Type.__name__ = "Integer32"
_IbmappnLocalNodeType_Object = MibScalar
ibmappnLocalNodeType = _IbmappnLocalNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 1, 2),
    _IbmappnLocalNodeType_Type()
)
ibmappnLocalNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNodeType.setStatus("mandatory")
_IbmappnLocalNnSpecific_ObjectIdentity = ObjectIdentity
ibmappnLocalNnSpecific = _IbmappnLocalNnSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2)
)
_IbmappnLocalNnRsn_Type = Integer32
_IbmappnLocalNnRsn_Object = MibScalar
ibmappnLocalNnRsn = _IbmappnLocalNnRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 1),
    _IbmappnLocalNnRsn_Type()
)
ibmappnLocalNnRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnRsn.setStatus("mandatory")
_IbmappnLocalNnRouteAddResist_Type = Integer32
_IbmappnLocalNnRouteAddResist_Object = MibScalar
ibmappnLocalNnRouteAddResist = _IbmappnLocalNnRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 2),
    _IbmappnLocalNnRouteAddResist_Type()
)
ibmappnLocalNnRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnRouteAddResist.setStatus("mandatory")


class _IbmappnLocalNnCongested_Type(Integer32):
    """Custom type ibmappnLocalNnCongested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnCongested_Type.__name__ = "Integer32"
_IbmappnLocalNnCongested_Object = MibScalar
ibmappnLocalNnCongested = _IbmappnLocalNnCongested_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 3),
    _IbmappnLocalNnCongested_Type()
)
ibmappnLocalNnCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnCongested.setStatus("mandatory")


class _IbmappnLocalNnIsrDepleted_Type(Integer32):
    """Custom type ibmappnLocalNnIsrDepleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnIsrDepleted_Type.__name__ = "Integer32"
_IbmappnLocalNnIsrDepleted_Object = MibScalar
ibmappnLocalNnIsrDepleted = _IbmappnLocalNnIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 4),
    _IbmappnLocalNnIsrDepleted_Type()
)
ibmappnLocalNnIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnIsrDepleted.setStatus("mandatory")


class _IbmappnLocalNnEndptDepleted_Type(Integer32):
    """Custom type ibmappnLocalNnEndptDepleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnEndptDepleted_Type.__name__ = "Integer32"
_IbmappnLocalNnEndptDepleted_Object = MibScalar
ibmappnLocalNnEndptDepleted = _IbmappnLocalNnEndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 5),
    _IbmappnLocalNnEndptDepleted_Type()
)
ibmappnLocalNnEndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnEndptDepleted.setStatus("mandatory")


class _IbmappnLocalNnQuiescing_Type(Integer32):
    """Custom type ibmappnLocalNnQuiescing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnQuiescing_Type.__name__ = "Integer32"
_IbmappnLocalNnQuiescing_Object = MibScalar
ibmappnLocalNnQuiescing = _IbmappnLocalNnQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 6),
    _IbmappnLocalNnQuiescing_Type()
)
ibmappnLocalNnQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnQuiescing.setStatus("mandatory")


class _IbmappnLocalNnGateway_Type(Integer32):
    """Custom type ibmappnLocalNnGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnGateway_Type.__name__ = "Integer32"
_IbmappnLocalNnGateway_Object = MibScalar
ibmappnLocalNnGateway = _IbmappnLocalNnGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 7),
    _IbmappnLocalNnGateway_Type()
)
ibmappnLocalNnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnGateway.setStatus("mandatory")


class _IbmappnLocalNnCentralDirectory_Type(Integer32):
    """Custom type ibmappnLocalNnCentralDirectory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnCentralDirectory_Type.__name__ = "Integer32"
_IbmappnLocalNnCentralDirectory_Object = MibScalar
ibmappnLocalNnCentralDirectory = _IbmappnLocalNnCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 8),
    _IbmappnLocalNnCentralDirectory_Type()
)
ibmappnLocalNnCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnCentralDirectory.setStatus("mandatory")


class _IbmappnLocalNnIsr_Type(Integer32):
    """Custom type ibmappnLocalNnIsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnIsr_Type.__name__ = "Integer32"
_IbmappnLocalNnIsr_Object = MibScalar
ibmappnLocalNnIsr = _IbmappnLocalNnIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 9),
    _IbmappnLocalNnIsr_Type()
)
ibmappnLocalNnIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnIsr.setStatus("mandatory")


class _IbmappnLocalNnChainSupport_Type(Integer32):
    """Custom type ibmappnLocalNnChainSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalNnChainSupport_Type.__name__ = "Integer32"
_IbmappnLocalNnChainSupport_Object = MibScalar
ibmappnLocalNnChainSupport = _IbmappnLocalNnChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 10),
    _IbmappnLocalNnChainSupport_Type()
)
ibmappnLocalNnChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnChainSupport.setStatus("mandatory")
_IbmappnLocalNnFrsn_Type = Integer32
_IbmappnLocalNnFrsn_Object = MibScalar
ibmappnLocalNnFrsn = _IbmappnLocalNnFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 11),
    _IbmappnLocalNnFrsn_Type()
)
ibmappnLocalNnFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnFrsn.setStatus("mandatory")
_IbmappnLocalTg_ObjectIdentity = ObjectIdentity
ibmappnLocalTg = _IbmappnLocalTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3)
)
_IbmappnLocalTgTable_Object = MibTable
ibmappnLocalTgTable = _IbmappnLocalTgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ibmappnLocalTgTable.setStatus("mandatory")
_IbmappnLocalTgEntry_Object = MibTableRow
ibmappnLocalTgEntry = _IbmappnLocalTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1)
)
ibmappnLocalTgEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnLocalTgDest"),
    (0, "IBM6611-MIB", "ibmappnLocalTgNum"),
)
if mibBuilder.loadTexts:
    ibmappnLocalTgEntry.setStatus("mandatory")


class _IbmappnLocalTgDest_Type(DisplayString):
    """Custom type ibmappnLocalTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalTgDest_Type.__name__ = "DisplayString"
_IbmappnLocalTgDest_Object = MibTableColumn
ibmappnLocalTgDest = _IbmappnLocalTgDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 1),
    _IbmappnLocalTgDest_Type()
)
ibmappnLocalTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDest.setStatus("mandatory")
_IbmappnLocalTgNum_Type = Integer32
_IbmappnLocalTgNum_Object = MibTableColumn
ibmappnLocalTgNum = _IbmappnLocalTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 2),
    _IbmappnLocalTgNum_Type()
)
ibmappnLocalTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgNum.setStatus("mandatory")


class _IbmappnLocalTgDestVirtual_Type(Integer32):
    """Custom type ibmappnLocalTgDestVirtual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalTgDestVirtual_Type.__name__ = "Integer32"
_IbmappnLocalTgDestVirtual_Object = MibTableColumn
ibmappnLocalTgDestVirtual = _IbmappnLocalTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 3),
    _IbmappnLocalTgDestVirtual_Type()
)
ibmappnLocalTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDestVirtual.setStatus("mandatory")


class _IbmappnLocalTgDlcData_Type(OctetString):
    """Custom type ibmappnLocalTgDlcData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_IbmappnLocalTgDlcData_Type.__name__ = "OctetString"
_IbmappnLocalTgDlcData_Object = MibTableColumn
ibmappnLocalTgDlcData = _IbmappnLocalTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 4),
    _IbmappnLocalTgDlcData_Type()
)
ibmappnLocalTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDlcData.setStatus("mandatory")
_IbmappnLocalTgRsn_Type = Integer32
_IbmappnLocalTgRsn_Object = MibTableColumn
ibmappnLocalTgRsn = _IbmappnLocalTgRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 5),
    _IbmappnLocalTgRsn_Type()
)
ibmappnLocalTgRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgRsn.setStatus("mandatory")


class _IbmappnLocalTgQuiescing_Type(Integer32):
    """Custom type ibmappnLocalTgQuiescing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalTgQuiescing_Type.__name__ = "Integer32"
_IbmappnLocalTgQuiescing_Object = MibTableColumn
ibmappnLocalTgQuiescing = _IbmappnLocalTgQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 6),
    _IbmappnLocalTgQuiescing_Type()
)
ibmappnLocalTgQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgQuiescing.setStatus("mandatory")


class _IbmappnLocalTgOperational_Type(Integer32):
    """Custom type ibmappnLocalTgOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalTgOperational_Type.__name__ = "Integer32"
_IbmappnLocalTgOperational_Object = MibTableColumn
ibmappnLocalTgOperational = _IbmappnLocalTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 7),
    _IbmappnLocalTgOperational_Type()
)
ibmappnLocalTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgOperational.setStatus("mandatory")


class _IbmappnLocalTgCpCpSession_Type(Integer32):
    """Custom type ibmappnLocalTgCpCpSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalTgCpCpSession_Type.__name__ = "Integer32"
_IbmappnLocalTgCpCpSession_Object = MibTableColumn
ibmappnLocalTgCpCpSession = _IbmappnLocalTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 8),
    _IbmappnLocalTgCpCpSession_Type()
)
ibmappnLocalTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgCpCpSession.setStatus("mandatory")
_IbmappnLocalTgEffCap_Type = Integer32
_IbmappnLocalTgEffCap_Object = MibTableColumn
ibmappnLocalTgEffCap = _IbmappnLocalTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 9),
    _IbmappnLocalTgEffCap_Type()
)
ibmappnLocalTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgEffCap.setStatus("mandatory")


class _IbmappnLocalTgConnCost_Type(Integer32):
    """Custom type ibmappnLocalTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgConnCost_Type.__name__ = "Integer32"
_IbmappnLocalTgConnCost_Object = MibTableColumn
ibmappnLocalTgConnCost = _IbmappnLocalTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 10),
    _IbmappnLocalTgConnCost_Type()
)
ibmappnLocalTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgConnCost.setStatus("mandatory")


class _IbmappnLocalTgByteCost_Type(Integer32):
    """Custom type ibmappnLocalTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgByteCost_Type.__name__ = "Integer32"
_IbmappnLocalTgByteCost_Object = MibTableColumn
ibmappnLocalTgByteCost = _IbmappnLocalTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 11),
    _IbmappnLocalTgByteCost_Type()
)
ibmappnLocalTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgByteCost.setStatus("mandatory")


class _IbmappnLocalTgSecurity_Type(Integer32):
    """Custom type ibmappnLocalTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnLocalTgSecurity_Type.__name__ = "Integer32"
_IbmappnLocalTgSecurity_Object = MibTableColumn
ibmappnLocalTgSecurity = _IbmappnLocalTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 12),
    _IbmappnLocalTgSecurity_Type()
)
ibmappnLocalTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgSecurity.setStatus("mandatory")


class _IbmappnLocalTgDelay_Type(Integer32):
    """Custom type ibmappnLocalTgDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 1),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnLocalTgDelay_Type.__name__ = "Integer32"
_IbmappnLocalTgDelay_Object = MibTableColumn
ibmappnLocalTgDelay = _IbmappnLocalTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 13),
    _IbmappnLocalTgDelay_Type()
)
ibmappnLocalTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDelay.setStatus("mandatory")
_IbmappnLocalTgModemClass_Type = Integer32
_IbmappnLocalTgModemClass_Object = MibTableColumn
ibmappnLocalTgModemClass = _IbmappnLocalTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 14),
    _IbmappnLocalTgModemClass_Type()
)
ibmappnLocalTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgModemClass.setStatus("mandatory")


class _IbmappnLocalTgUsr1_Type(Integer32):
    """Custom type ibmappnLocalTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgUsr1_Type.__name__ = "Integer32"
_IbmappnLocalTgUsr1_Object = MibTableColumn
ibmappnLocalTgUsr1 = _IbmappnLocalTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 15),
    _IbmappnLocalTgUsr1_Type()
)
ibmappnLocalTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgUsr1.setStatus("mandatory")


class _IbmappnLocalTgUsr2_Type(Integer32):
    """Custom type ibmappnLocalTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgUsr2_Type.__name__ = "Integer32"
_IbmappnLocalTgUsr2_Object = MibTableColumn
ibmappnLocalTgUsr2 = _IbmappnLocalTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 16),
    _IbmappnLocalTgUsr2_Type()
)
ibmappnLocalTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgUsr2.setStatus("mandatory")


class _IbmappnLocalTgUsr3_Type(Integer32):
    """Custom type ibmappnLocalTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgUsr3_Type.__name__ = "Integer32"
_IbmappnLocalTgUsr3_Object = MibTableColumn
ibmappnLocalTgUsr3 = _IbmappnLocalTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 17),
    _IbmappnLocalTgUsr3_Type()
)
ibmappnLocalTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgUsr3.setStatus("mandatory")
_IbmappnLocalEnTopology_ObjectIdentity = ObjectIdentity
ibmappnLocalEnTopology = _IbmappnLocalEnTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2)
)
_IbmappnLocalEnTable_Object = MibTable
ibmappnLocalEnTable = _IbmappnLocalEnTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ibmappnLocalEnTable.setStatus("mandatory")
_IbmappnLocalEnEntry_Object = MibTableRow
ibmappnLocalEnEntry = _IbmappnLocalEnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1)
)
ibmappnLocalEnEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnLocalEnName"),
)
if mibBuilder.loadTexts:
    ibmappnLocalEnEntry.setStatus("mandatory")


class _IbmappnLocalEnName_Type(DisplayString):
    """Custom type ibmappnLocalEnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalEnName_Type.__name__ = "DisplayString"
_IbmappnLocalEnName_Object = MibTableColumn
ibmappnLocalEnName = _IbmappnLocalEnName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1, 1),
    _IbmappnLocalEnName_Type()
)
ibmappnLocalEnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnName.setStatus("mandatory")


class _IbmappnLocalEnEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnLocalEnEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnLocalEnEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnLocalEnEntryTimeLeft_Object = MibTableColumn
ibmappnLocalEnEntryTimeLeft = _IbmappnLocalEnEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1, 2),
    _IbmappnLocalEnEntryTimeLeft_Type()
)
ibmappnLocalEnEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnEntryTimeLeft.setStatus("mandatory")


class _IbmappnLocalEnType_Type(Integer32):
    """Custom type ibmappnLocalEnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endnode", 2),
          ("len", 4))
    )


_IbmappnLocalEnType_Type.__name__ = "Integer32"
_IbmappnLocalEnType_Object = MibTableColumn
ibmappnLocalEnType = _IbmappnLocalEnType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1, 3),
    _IbmappnLocalEnType_Type()
)
ibmappnLocalEnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnType.setStatus("mandatory")
_IbmappnLocalEnTgTable_Object = MibTable
ibmappnLocalEnTgTable = _IbmappnLocalEnTgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ibmappnLocalEnTgTable.setStatus("mandatory")
_IbmappnLocalEnTgEntry_Object = MibTableRow
ibmappnLocalEnTgEntry = _IbmappnLocalEnTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1)
)
ibmappnLocalEnTgEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnLocalEnTgOrigin"),
    (0, "IBM6611-MIB", "ibmappnLocalEnTgDest"),
    (0, "IBM6611-MIB", "ibmappnLocalEnTgNum"),
)
if mibBuilder.loadTexts:
    ibmappnLocalEnTgEntry.setStatus("mandatory")


class _IbmappnLocalEnTgOrigin_Type(DisplayString):
    """Custom type ibmappnLocalEnTgOrigin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalEnTgOrigin_Type.__name__ = "DisplayString"
_IbmappnLocalEnTgOrigin_Object = MibTableColumn
ibmappnLocalEnTgOrigin = _IbmappnLocalEnTgOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 1),
    _IbmappnLocalEnTgOrigin_Type()
)
ibmappnLocalEnTgOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgOrigin.setStatus("mandatory")


class _IbmappnLocalEnTgDest_Type(DisplayString):
    """Custom type ibmappnLocalEnTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalEnTgDest_Type.__name__ = "DisplayString"
_IbmappnLocalEnTgDest_Object = MibTableColumn
ibmappnLocalEnTgDest = _IbmappnLocalEnTgDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 2),
    _IbmappnLocalEnTgDest_Type()
)
ibmappnLocalEnTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDest.setStatus("mandatory")
_IbmappnLocalEnTgNum_Type = Integer32
_IbmappnLocalEnTgNum_Object = MibTableColumn
ibmappnLocalEnTgNum = _IbmappnLocalEnTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 3),
    _IbmappnLocalEnTgNum_Type()
)
ibmappnLocalEnTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgNum.setStatus("mandatory")


class _IbmappnLocalEnTgEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnLocalEnTgEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnLocalEnTgEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnLocalEnTgEntryTimeLeft_Object = MibTableColumn
ibmappnLocalEnTgEntryTimeLeft = _IbmappnLocalEnTgEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 4),
    _IbmappnLocalEnTgEntryTimeLeft_Type()
)
ibmappnLocalEnTgEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgEntryTimeLeft.setStatus("mandatory")


class _IbmappnLocalEnTgDestVirtual_Type(Integer32):
    """Custom type ibmappnLocalEnTgDestVirtual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalEnTgDestVirtual_Type.__name__ = "Integer32"
_IbmappnLocalEnTgDestVirtual_Object = MibTableColumn
ibmappnLocalEnTgDestVirtual = _IbmappnLocalEnTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 5),
    _IbmappnLocalEnTgDestVirtual_Type()
)
ibmappnLocalEnTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDestVirtual.setStatus("mandatory")
_IbmappnLocalEnTgDlcData_Type = OctetString
_IbmappnLocalEnTgDlcData_Object = MibTableColumn
ibmappnLocalEnTgDlcData = _IbmappnLocalEnTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 6),
    _IbmappnLocalEnTgDlcData_Type()
)
ibmappnLocalEnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDlcData.setStatus("mandatory")


class _IbmappnLocalEnTgOperational_Type(Integer32):
    """Custom type ibmappnLocalEnTgOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalEnTgOperational_Type.__name__ = "Integer32"
_IbmappnLocalEnTgOperational_Object = MibTableColumn
ibmappnLocalEnTgOperational = _IbmappnLocalEnTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 7),
    _IbmappnLocalEnTgOperational_Type()
)
ibmappnLocalEnTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgOperational.setStatus("mandatory")


class _IbmappnLocalEnTgCpCpSession_Type(Integer32):
    """Custom type ibmappnLocalEnTgCpCpSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnLocalEnTgCpCpSession_Type.__name__ = "Integer32"
_IbmappnLocalEnTgCpCpSession_Object = MibTableColumn
ibmappnLocalEnTgCpCpSession = _IbmappnLocalEnTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 8),
    _IbmappnLocalEnTgCpCpSession_Type()
)
ibmappnLocalEnTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgCpCpSession.setStatus("mandatory")
_IbmappnLocalEnTgEffCap_Type = Integer32
_IbmappnLocalEnTgEffCap_Object = MibTableColumn
ibmappnLocalEnTgEffCap = _IbmappnLocalEnTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 9),
    _IbmappnLocalEnTgEffCap_Type()
)
ibmappnLocalEnTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgEffCap.setStatus("mandatory")


class _IbmappnLocalEnTgConnCost_Type(Integer32):
    """Custom type ibmappnLocalEnTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgConnCost_Type.__name__ = "Integer32"
_IbmappnLocalEnTgConnCost_Object = MibTableColumn
ibmappnLocalEnTgConnCost = _IbmappnLocalEnTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 10),
    _IbmappnLocalEnTgConnCost_Type()
)
ibmappnLocalEnTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgConnCost.setStatus("mandatory")


class _IbmappnLocalEnTgByteCost_Type(Integer32):
    """Custom type ibmappnLocalEnTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgByteCost_Type.__name__ = "Integer32"
_IbmappnLocalEnTgByteCost_Object = MibTableColumn
ibmappnLocalEnTgByteCost = _IbmappnLocalEnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 11),
    _IbmappnLocalEnTgByteCost_Type()
)
ibmappnLocalEnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgByteCost.setStatus("mandatory")


class _IbmappnLocalEnTgSecurity_Type(Integer32):
    """Custom type ibmappnLocalEnTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnLocalEnTgSecurity_Type.__name__ = "Integer32"
_IbmappnLocalEnTgSecurity_Object = MibTableColumn
ibmappnLocalEnTgSecurity = _IbmappnLocalEnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 12),
    _IbmappnLocalEnTgSecurity_Type()
)
ibmappnLocalEnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgSecurity.setStatus("mandatory")


class _IbmappnLocalEnTgDelay_Type(Integer32):
    """Custom type ibmappnLocalEnTgDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 1),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnLocalEnTgDelay_Type.__name__ = "Integer32"
_IbmappnLocalEnTgDelay_Object = MibTableColumn
ibmappnLocalEnTgDelay = _IbmappnLocalEnTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 13),
    _IbmappnLocalEnTgDelay_Type()
)
ibmappnLocalEnTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDelay.setStatus("mandatory")


class _IbmappnLocalEnTgModemClass_Type(Integer32):
    """Custom type ibmappnLocalEnTgModemClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnLocalEnTgModemClass_Type.__name__ = "Integer32"
_IbmappnLocalEnTgModemClass_Object = MibTableColumn
ibmappnLocalEnTgModemClass = _IbmappnLocalEnTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 14),
    _IbmappnLocalEnTgModemClass_Type()
)
ibmappnLocalEnTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgModemClass.setStatus("mandatory")


class _IbmappnLocalEnTgUsr1_Type(Integer32):
    """Custom type ibmappnLocalEnTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgUsr1_Type.__name__ = "Integer32"
_IbmappnLocalEnTgUsr1_Object = MibTableColumn
ibmappnLocalEnTgUsr1 = _IbmappnLocalEnTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 15),
    _IbmappnLocalEnTgUsr1_Type()
)
ibmappnLocalEnTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgUsr1.setStatus("mandatory")


class _IbmappnLocalEnTgUsr2_Type(Integer32):
    """Custom type ibmappnLocalEnTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgUsr2_Type.__name__ = "Integer32"
_IbmappnLocalEnTgUsr2_Object = MibTableColumn
ibmappnLocalEnTgUsr2 = _IbmappnLocalEnTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 16),
    _IbmappnLocalEnTgUsr2_Type()
)
ibmappnLocalEnTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgUsr2.setStatus("mandatory")


class _IbmappnLocalEnTgUsr3_Type(Integer32):
    """Custom type ibmappnLocalEnTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgUsr3_Type.__name__ = "Integer32"
_IbmappnLocalEnTgUsr3_Object = MibTableColumn
ibmappnLocalEnTgUsr3 = _IbmappnLocalEnTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 17),
    _IbmappnLocalEnTgUsr3_Type()
)
ibmappnLocalEnTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgUsr3.setStatus("mandatory")
_IbmappnDir_ObjectIdentity = ObjectIdentity
ibmappnDir = _IbmappnDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5)
)
_IbmappnDirPerf_ObjectIdentity = ObjectIdentity
ibmappnDirPerf = _IbmappnDirPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1)
)
_IbmappnDirMaxCaches_Type = Integer32
_IbmappnDirMaxCaches_Object = MibScalar
ibmappnDirMaxCaches = _IbmappnDirMaxCaches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 1),
    _IbmappnDirMaxCaches_Type()
)
ibmappnDirMaxCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirMaxCaches.setStatus("mandatory")
_IbmappnDirCurCaches_Type = Gauge32
_IbmappnDirCurCaches_Object = MibScalar
ibmappnDirCurCaches = _IbmappnDirCurCaches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 2),
    _IbmappnDirCurCaches_Type()
)
ibmappnDirCurCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirCurCaches.setStatus("mandatory")
_IbmappnDirCurHomeEntries_Type = Gauge32
_IbmappnDirCurHomeEntries_Object = MibScalar
ibmappnDirCurHomeEntries = _IbmappnDirCurHomeEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 3),
    _IbmappnDirCurHomeEntries_Type()
)
ibmappnDirCurHomeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirCurHomeEntries.setStatus("mandatory")
_IbmappnDirRegEntries_Type = Gauge32
_IbmappnDirRegEntries_Object = MibScalar
ibmappnDirRegEntries = _IbmappnDirRegEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 4),
    _IbmappnDirRegEntries_Type()
)
ibmappnDirRegEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirRegEntries.setStatus("mandatory")
_IbmappnDirInLocates_Type = Counter32
_IbmappnDirInLocates_Object = MibScalar
ibmappnDirInLocates = _IbmappnDirInLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 5),
    _IbmappnDirInLocates_Type()
)
ibmappnDirInLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirInLocates.setStatus("mandatory")
_IbmappnDirInBcastLocates_Type = Counter32
_IbmappnDirInBcastLocates_Object = MibScalar
ibmappnDirInBcastLocates = _IbmappnDirInBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 6),
    _IbmappnDirInBcastLocates_Type()
)
ibmappnDirInBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirInBcastLocates.setStatus("mandatory")
_IbmappnDirOutLocates_Type = Counter32
_IbmappnDirOutLocates_Object = MibScalar
ibmappnDirOutLocates = _IbmappnDirOutLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 7),
    _IbmappnDirOutLocates_Type()
)
ibmappnDirOutLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirOutLocates.setStatus("mandatory")
_IbmappnDirOutBcastLocates_Type = Counter32
_IbmappnDirOutBcastLocates_Object = MibScalar
ibmappnDirOutBcastLocates = _IbmappnDirOutBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 8),
    _IbmappnDirOutBcastLocates_Type()
)
ibmappnDirOutBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirOutBcastLocates.setStatus("mandatory")
_IbmappnDirNotFoundLocates_Type = Counter32
_IbmappnDirNotFoundLocates_Object = MibScalar
ibmappnDirNotFoundLocates = _IbmappnDirNotFoundLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 9),
    _IbmappnDirNotFoundLocates_Type()
)
ibmappnDirNotFoundLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirNotFoundLocates.setStatus("mandatory")
_IbmappnDirNotFoundBcastLocates_Type = Counter32
_IbmappnDirNotFoundBcastLocates_Object = MibScalar
ibmappnDirNotFoundBcastLocates = _IbmappnDirNotFoundBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 10),
    _IbmappnDirNotFoundBcastLocates_Type()
)
ibmappnDirNotFoundBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirNotFoundBcastLocates.setStatus("mandatory")
_IbmappnDirLocateOutstands_Type = Gauge32
_IbmappnDirLocateOutstands_Object = MibScalar
ibmappnDirLocateOutstands = _IbmappnDirLocateOutstands_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 11),
    _IbmappnDirLocateOutstands_Type()
)
ibmappnDirLocateOutstands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLocateOutstands.setStatus("mandatory")
_IbmappnDirTable_Object = MibTable
ibmappnDirTable = _IbmappnDirTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2)
)
if mibBuilder.loadTexts:
    ibmappnDirTable.setStatus("mandatory")
_IbmappnDirEntry_Object = MibTableRow
ibmappnDirEntry = _IbmappnDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1)
)
ibmappnDirEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnDirLuName"),
)
if mibBuilder.loadTexts:
    ibmappnDirEntry.setStatus("mandatory")


class _IbmappnDirLuName_Type(DisplayString):
    """Custom type ibmappnDirLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnDirLuName_Type.__name__ = "DisplayString"
_IbmappnDirLuName_Object = MibTableColumn
ibmappnDirLuName = _IbmappnDirLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 1),
    _IbmappnDirLuName_Type()
)
ibmappnDirLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLuName.setStatus("mandatory")


class _IbmappnDirServerName_Type(DisplayString):
    """Custom type ibmappnDirServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnDirServerName_Type.__name__ = "DisplayString"
_IbmappnDirServerName_Object = MibTableColumn
ibmappnDirServerName = _IbmappnDirServerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 2),
    _IbmappnDirServerName_Type()
)
ibmappnDirServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirServerName.setStatus("mandatory")


class _IbmappnDirLuOwnerName_Type(DisplayString):
    """Custom type ibmappnDirLuOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnDirLuOwnerName_Type.__name__ = "DisplayString"
_IbmappnDirLuOwnerName_Object = MibTableColumn
ibmappnDirLuOwnerName = _IbmappnDirLuOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 3),
    _IbmappnDirLuOwnerName_Type()
)
ibmappnDirLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLuOwnerName.setStatus("mandatory")


class _IbmappnDirLuLocation_Type(Integer32):
    """Custom type ibmappnDirLuLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("local", 1),
          ("xdomain", 3))
    )


_IbmappnDirLuLocation_Type.__name__ = "Integer32"
_IbmappnDirLuLocation_Object = MibTableColumn
ibmappnDirLuLocation = _IbmappnDirLuLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 4),
    _IbmappnDirLuLocation_Type()
)
ibmappnDirLuLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLuLocation.setStatus("mandatory")


class _IbmappnDirType_Type(Integer32):
    """Custom type ibmappnDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cache", 2),
          ("home", 1),
          ("registered", 3))
    )


_IbmappnDirType_Type.__name__ = "Integer32"
_IbmappnDirType_Object = MibTableColumn
ibmappnDirType = _IbmappnDirType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 5),
    _IbmappnDirType_Type()
)
ibmappnDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirType.setStatus("mandatory")


class _IbmappnDirWildCard_Type(Integer32):
    """Custom type ibmappnDirWildCard based on Integer32"""
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
        *(("explicit-entry", 2),
          ("full-wildcard", 4),
          ("other", 1),
          ("partial-wildcard", 3))
    )


_IbmappnDirWildCard_Type.__name__ = "Integer32"
_IbmappnDirWildCard_Object = MibTableColumn
ibmappnDirWildCard = _IbmappnDirWildCard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 6),
    _IbmappnDirWildCard_Type()
)
ibmappnDirWildCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirWildCard.setStatus("mandatory")
_IbmappnCos_ObjectIdentity = ObjectIdentity
ibmappnCos = _IbmappnCos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6)
)
_IbmappnCosModeTable_Object = MibTable
ibmappnCosModeTable = _IbmappnCosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1)
)
if mibBuilder.loadTexts:
    ibmappnCosModeTable.setStatus("mandatory")
_IbmappnCosModeEntry_Object = MibTableRow
ibmappnCosModeEntry = _IbmappnCosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1, 1)
)
ibmappnCosModeEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnCosModeName"),
)
if mibBuilder.loadTexts:
    ibmappnCosModeEntry.setStatus("mandatory")


class _IbmappnCosModeName_Type(DisplayString):
    """Custom type ibmappnCosModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosModeName_Type.__name__ = "DisplayString"
_IbmappnCosModeName_Object = MibTableColumn
ibmappnCosModeName = _IbmappnCosModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1, 1, 1),
    _IbmappnCosModeName_Type()
)
ibmappnCosModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosModeName.setStatus("mandatory")


class _IbmappnCosModeCosName_Type(DisplayString):
    """Custom type ibmappnCosModeCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosModeCosName_Type.__name__ = "DisplayString"
_IbmappnCosModeCosName_Object = MibTableColumn
ibmappnCosModeCosName = _IbmappnCosModeCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1, 1, 2),
    _IbmappnCosModeCosName_Type()
)
ibmappnCosModeCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosModeCosName.setStatus("mandatory")
_IbmappnCosNameTable_Object = MibTable
ibmappnCosNameTable = _IbmappnCosNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2)
)
if mibBuilder.loadTexts:
    ibmappnCosNameTable.setStatus("mandatory")
_IbmappnCosNameEntry_Object = MibTableRow
ibmappnCosNameEntry = _IbmappnCosNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2, 1)
)
ibmappnCosNameEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnCosName"),
)
if mibBuilder.loadTexts:
    ibmappnCosNameEntry.setStatus("mandatory")


class _IbmappnCosName_Type(DisplayString):
    """Custom type ibmappnCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosName_Type.__name__ = "DisplayString"
_IbmappnCosName_Object = MibTableColumn
ibmappnCosName = _IbmappnCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2, 1, 1),
    _IbmappnCosName_Type()
)
ibmappnCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosName.setStatus("mandatory")


class _IbmappnCosTransPriority_Type(Integer32):
    """Custom type ibmappnCosTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_IbmappnCosTransPriority_Type.__name__ = "Integer32"
_IbmappnCosTransPriority_Object = MibTableColumn
ibmappnCosTransPriority = _IbmappnCosTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2, 1, 2),
    _IbmappnCosTransPriority_Type()
)
ibmappnCosTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTransPriority.setStatus("mandatory")
_IbmappnCosNodeRowTable_Object = MibTable
ibmappnCosNodeRowTable = _IbmappnCosNodeRowTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3)
)
if mibBuilder.loadTexts:
    ibmappnCosNodeRowTable.setStatus("mandatory")
_IbmappnCosNodeRowEntry_Object = MibTableRow
ibmappnCosNodeRowEntry = _IbmappnCosNodeRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1)
)
ibmappnCosNodeRowEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnCosNodeRowName"),
    (0, "IBM6611-MIB", "ibmappnCosNodeRowIndex"),
)
if mibBuilder.loadTexts:
    ibmappnCosNodeRowEntry.setStatus("mandatory")


class _IbmappnCosNodeRowName_Type(DisplayString):
    """Custom type ibmappnCosNodeRowName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosNodeRowName_Type.__name__ = "DisplayString"
_IbmappnCosNodeRowName_Object = MibTableColumn
ibmappnCosNodeRowName = _IbmappnCosNodeRowName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 1),
    _IbmappnCosNodeRowName_Type()
)
ibmappnCosNodeRowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowName.setStatus("mandatory")


class _IbmappnCosNodeRowIndex_Type(Integer32):
    """Custom type ibmappnCosNodeRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosNodeRowIndex_Type.__name__ = "Integer32"
_IbmappnCosNodeRowIndex_Object = MibTableColumn
ibmappnCosNodeRowIndex = _IbmappnCosNodeRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 2),
    _IbmappnCosNodeRowIndex_Type()
)
ibmappnCosNodeRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowIndex.setStatus("mandatory")
_IbmappnCosNodeRowWgt_Type = DisplayString
_IbmappnCosNodeRowWgt_Object = MibTableColumn
ibmappnCosNodeRowWgt = _IbmappnCosNodeRowWgt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 3),
    _IbmappnCosNodeRowWgt_Type()
)
ibmappnCosNodeRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowWgt.setStatus("mandatory")


class _IbmappnCosNodeRowResistMin_Type(Integer32):
    """Custom type ibmappnCosNodeRowResistMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosNodeRowResistMin_Type.__name__ = "Integer32"
_IbmappnCosNodeRowResistMin_Object = MibTableColumn
ibmappnCosNodeRowResistMin = _IbmappnCosNodeRowResistMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 4),
    _IbmappnCosNodeRowResistMin_Type()
)
ibmappnCosNodeRowResistMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowResistMin.setStatus("mandatory")


class _IbmappnCosNodeRowResistMax_Type(Integer32):
    """Custom type ibmappnCosNodeRowResistMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosNodeRowResistMax_Type.__name__ = "Integer32"
_IbmappnCosNodeRowResistMax_Object = MibTableColumn
ibmappnCosNodeRowResistMax = _IbmappnCosNodeRowResistMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 5),
    _IbmappnCosNodeRowResistMax_Type()
)
ibmappnCosNodeRowResistMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowResistMax.setStatus("mandatory")


class _IbmappnCosNodeRowMinCongestAllow_Type(Integer32):
    """Custom type ibmappnCosNodeRowMinCongestAllow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnCosNodeRowMinCongestAllow_Type.__name__ = "Integer32"
_IbmappnCosNodeRowMinCongestAllow_Object = MibTableColumn
ibmappnCosNodeRowMinCongestAllow = _IbmappnCosNodeRowMinCongestAllow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 6),
    _IbmappnCosNodeRowMinCongestAllow_Type()
)
ibmappnCosNodeRowMinCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowMinCongestAllow.setStatus("mandatory")


class _IbmappnCosNodeRowMaxCongestAllow_Type(Integer32):
    """Custom type ibmappnCosNodeRowMaxCongestAllow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappnCosNodeRowMaxCongestAllow_Type.__name__ = "Integer32"
_IbmappnCosNodeRowMaxCongestAllow_Object = MibTableColumn
ibmappnCosNodeRowMaxCongestAllow = _IbmappnCosNodeRowMaxCongestAllow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 7),
    _IbmappnCosNodeRowMaxCongestAllow_Type()
)
ibmappnCosNodeRowMaxCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowMaxCongestAllow.setStatus("mandatory")
_IbmappnCosTgRowTable_Object = MibTable
ibmappnCosTgRowTable = _IbmappnCosTgRowTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4)
)
if mibBuilder.loadTexts:
    ibmappnCosTgRowTable.setStatus("mandatory")
_IbmappnCosTgRowEntry_Object = MibTableRow
ibmappnCosTgRowEntry = _IbmappnCosTgRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1)
)
ibmappnCosTgRowEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnCosTgRowName"),
    (0, "IBM6611-MIB", "ibmappnCosTgRowIndex"),
)
if mibBuilder.loadTexts:
    ibmappnCosTgRowEntry.setStatus("mandatory")


class _IbmappnCosTgRowName_Type(DisplayString):
    """Custom type ibmappnCosTgRowName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosTgRowName_Type.__name__ = "DisplayString"
_IbmappnCosTgRowName_Object = MibTableColumn
ibmappnCosTgRowName = _IbmappnCosTgRowName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 1),
    _IbmappnCosTgRowName_Type()
)
ibmappnCosTgRowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowName.setStatus("mandatory")


class _IbmappnCosTgRowIndex_Type(Integer32):
    """Custom type ibmappnCosTgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowIndex_Type.__name__ = "Integer32"
_IbmappnCosTgRowIndex_Object = MibTableColumn
ibmappnCosTgRowIndex = _IbmappnCosTgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 2),
    _IbmappnCosTgRowIndex_Type()
)
ibmappnCosTgRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowIndex.setStatus("mandatory")
_IbmappnCosTgRowWgt_Type = DisplayString
_IbmappnCosTgRowWgt_Object = MibTableColumn
ibmappnCosTgRowWgt = _IbmappnCosTgRowWgt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 3),
    _IbmappnCosTgRowWgt_Type()
)
ibmappnCosTgRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowWgt.setStatus("mandatory")
_IbmappnCosTgRowEffCapMin_Type = Integer32
_IbmappnCosTgRowEffCapMin_Object = MibTableColumn
ibmappnCosTgRowEffCapMin = _IbmappnCosTgRowEffCapMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 4),
    _IbmappnCosTgRowEffCapMin_Type()
)
ibmappnCosTgRowEffCapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowEffCapMin.setStatus("mandatory")
_IbmappnCosTgRowEffCapMax_Type = Integer32
_IbmappnCosTgRowEffCapMax_Object = MibTableColumn
ibmappnCosTgRowEffCapMax = _IbmappnCosTgRowEffCapMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 5),
    _IbmappnCosTgRowEffCapMax_Type()
)
ibmappnCosTgRowEffCapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowEffCapMax.setStatus("mandatory")


class _IbmappnCosTgRowConnCostMin_Type(Integer32):
    """Custom type ibmappnCosTgRowConnCostMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowConnCostMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowConnCostMin_Object = MibTableColumn
ibmappnCosTgRowConnCostMin = _IbmappnCosTgRowConnCostMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 6),
    _IbmappnCosTgRowConnCostMin_Type()
)
ibmappnCosTgRowConnCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowConnCostMin.setStatus("mandatory")


class _IbmappnCosTgRowConnCostMax_Type(Integer32):
    """Custom type ibmappnCosTgRowConnCostMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowConnCostMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowConnCostMax_Object = MibTableColumn
ibmappnCosTgRowConnCostMax = _IbmappnCosTgRowConnCostMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 7),
    _IbmappnCosTgRowConnCostMax_Type()
)
ibmappnCosTgRowConnCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowConnCostMax.setStatus("mandatory")


class _IbmappnCosTgRowByteCostMin_Type(Integer32):
    """Custom type ibmappnCosTgRowByteCostMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowByteCostMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowByteCostMin_Object = MibTableColumn
ibmappnCosTgRowByteCostMin = _IbmappnCosTgRowByteCostMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 8),
    _IbmappnCosTgRowByteCostMin_Type()
)
ibmappnCosTgRowByteCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowByteCostMin.setStatus("mandatory")


class _IbmappnCosTgRowByteCostMax_Type(Integer32):
    """Custom type ibmappnCosTgRowByteCostMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowByteCostMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowByteCostMax_Object = MibTableColumn
ibmappnCosTgRowByteCostMax = _IbmappnCosTgRowByteCostMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 9),
    _IbmappnCosTgRowByteCostMax_Type()
)
ibmappnCosTgRowByteCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowByteCostMax.setStatus("mandatory")


class _IbmappnCosTgRowSecurityMin_Type(Integer32):
    """Custom type ibmappnCosTgRowSecurityMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnCosTgRowSecurityMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowSecurityMin_Object = MibTableColumn
ibmappnCosTgRowSecurityMin = _IbmappnCosTgRowSecurityMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 10),
    _IbmappnCosTgRowSecurityMin_Type()
)
ibmappnCosTgRowSecurityMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowSecurityMin.setStatus("mandatory")


class _IbmappnCosTgRowSecurityMax_Type(Integer32):
    """Custom type ibmappnCosTgRowSecurityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnCosTgRowSecurityMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowSecurityMax_Object = MibTableColumn
ibmappnCosTgRowSecurityMax = _IbmappnCosTgRowSecurityMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 11),
    _IbmappnCosTgRowSecurityMax_Type()
)
ibmappnCosTgRowSecurityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowSecurityMax.setStatus("mandatory")


class _IbmappnCosTgRowDelayMin_Type(Integer32):
    """Custom type ibmappnCosTgRowDelayMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 1),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnCosTgRowDelayMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowDelayMin_Object = MibTableColumn
ibmappnCosTgRowDelayMin = _IbmappnCosTgRowDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 12),
    _IbmappnCosTgRowDelayMin_Type()
)
ibmappnCosTgRowDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowDelayMin.setStatus("mandatory")


class _IbmappnCosTgRowDelayMax_Type(Integer32):
    """Custom type ibmappnCosTgRowDelayMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 1),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnCosTgRowDelayMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowDelayMax_Object = MibTableColumn
ibmappnCosTgRowDelayMax = _IbmappnCosTgRowDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 13),
    _IbmappnCosTgRowDelayMax_Type()
)
ibmappnCosTgRowDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowDelayMax.setStatus("mandatory")


class _IbmappnCosTgRowUsr1Min_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr1Min_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr1Min_Object = MibTableColumn
ibmappnCosTgRowUsr1Min = _IbmappnCosTgRowUsr1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 14),
    _IbmappnCosTgRowUsr1Min_Type()
)
ibmappnCosTgRowUsr1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr1Min.setStatus("mandatory")


class _IbmappnCosTgRowUsr1Max_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr1Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr1Max_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr1Max_Object = MibTableColumn
ibmappnCosTgRowUsr1Max = _IbmappnCosTgRowUsr1Max_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 15),
    _IbmappnCosTgRowUsr1Max_Type()
)
ibmappnCosTgRowUsr1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr1Max.setStatus("mandatory")


class _IbmappnCosTgRowUsr2Min_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr2Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr2Min_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr2Min_Object = MibTableColumn
ibmappnCosTgRowUsr2Min = _IbmappnCosTgRowUsr2Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 16),
    _IbmappnCosTgRowUsr2Min_Type()
)
ibmappnCosTgRowUsr2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr2Min.setStatus("mandatory")


class _IbmappnCosTgRowUsr2Max_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr2Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr2Max_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr2Max_Object = MibTableColumn
ibmappnCosTgRowUsr2Max = _IbmappnCosTgRowUsr2Max_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 17),
    _IbmappnCosTgRowUsr2Max_Type()
)
ibmappnCosTgRowUsr2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr2Max.setStatus("mandatory")


class _IbmappnCosTgRowUsr3Min_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr3Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr3Min_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr3Min_Object = MibTableColumn
ibmappnCosTgRowUsr3Min = _IbmappnCosTgRowUsr3Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 18),
    _IbmappnCosTgRowUsr3Min_Type()
)
ibmappnCosTgRowUsr3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr3Min.setStatus("mandatory")


class _IbmappnCosTgRowUsr3Max_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr3Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr3Max_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr3Max_Object = MibTableColumn
ibmappnCosTgRowUsr3Max = _IbmappnCosTgRowUsr3Max_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 19),
    _IbmappnCosTgRowUsr3Max_Type()
)
ibmappnCosTgRowUsr3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr3Max.setStatus("mandatory")
_IbmappnSession_ObjectIdentity = ObjectIdentity
ibmappnSession = _IbmappnSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7)
)
_IbmappnSessGeneral_ObjectIdentity = ObjectIdentity
ibmappnSessGeneral = _IbmappnSessGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 1)
)
_IbmappnSessEndPoint_ObjectIdentity = ObjectIdentity
ibmappnSessEndPoint = _IbmappnSessEndPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2)
)
_IbmappcInformation_ObjectIdentity = ObjectIdentity
ibmappcInformation = _IbmappcInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1)
)
_IbmappcInGlobal_ObjectIdentity = ObjectIdentity
ibmappcInGlobal = _IbmappcInGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 1)
)


class _IbmappcInGlobeStatus_Type(Integer32):
    """Custom type ibmappcInGlobeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmappcInGlobeStatus_Type.__name__ = "Integer32"
_IbmappcInGlobeStatus_Object = MibScalar
ibmappcInGlobeStatus = _IbmappcInGlobeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 1, 1),
    _IbmappcInGlobeStatus_Type()
)
ibmappcInGlobeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappcInGlobeStatus.setStatus("mandatory")


class _IbmappcInGlobeRscv_Type(Integer32):
    """Custom type ibmappcInGlobeRscv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmappcInGlobeRscv_Type.__name__ = "Integer32"
_IbmappcInGlobeRscv_Object = MibScalar
ibmappcInGlobeRscv = _IbmappcInGlobeRscv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 1, 2),
    _IbmappcInGlobeRscv_Type()
)
ibmappcInGlobeRscv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappcInGlobeRscv.setStatus("mandatory")
_IbmappcInGlobeRscvTime_Type = TimeTicks
_IbmappcInGlobeRscvTime_Object = MibScalar
ibmappcInGlobeRscvTime = _IbmappcInGlobeRscvTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 1, 3),
    _IbmappcInGlobeRscvTime_Type()
)
ibmappcInGlobeRscvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInGlobeRscvTime.setStatus("mandatory")


class _IbmappcInGlobeCtrStatus_Type(Integer32):
    """Custom type ibmappcInGlobeCtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmappcInGlobeCtrStatus_Type.__name__ = "Integer32"
_IbmappcInGlobeCtrStatus_Object = MibScalar
ibmappcInGlobeCtrStatus = _IbmappcInGlobeCtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 1, 4),
    _IbmappcInGlobeCtrStatus_Type()
)
ibmappcInGlobeCtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappcInGlobeCtrStatus.setStatus("mandatory")
_IbmappcInGlobeCtrStatusTime_Type = TimeTicks
_IbmappcInGlobeCtrStatusTime_Object = MibScalar
ibmappcInGlobeCtrStatusTime = _IbmappcInGlobeCtrStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 1, 5),
    _IbmappcInGlobeCtrStatusTime_Type()
)
ibmappcInGlobeCtrStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInGlobeCtrStatusTime.setStatus("mandatory")
_IbmappcInGlobeActSess_Type = Gauge32
_IbmappcInGlobeActSess_Object = MibScalar
ibmappcInGlobeActSess = _IbmappcInGlobeActSess_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 1, 6),
    _IbmappcInGlobeActSess_Type()
)
ibmappcInGlobeActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInGlobeActSess.setStatus("mandatory")
_IbmappcInLluTable_Object = MibTable
ibmappcInLluTable = _IbmappcInLluTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibmappcInLluTable.setStatus("mandatory")
_IbmappcInLluEntry_Object = MibTableRow
ibmappcInLluEntry = _IbmappcInLluEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1)
)
ibmappcInLluEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappcInLluLuName"),
)
if mibBuilder.loadTexts:
    ibmappcInLluEntry.setStatus("mandatory")


class _IbmappcInLluLuName_Type(DisplayString):
    """Custom type ibmappcInLluLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInLluLuName_Type.__name__ = "DisplayString"
_IbmappcInLluLuName_Object = MibTableColumn
ibmappcInLluLuName = _IbmappcInLluLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1, 1),
    _IbmappcInLluLuName_Type()
)
ibmappcInLluLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLluLuName.setStatus("mandatory")


class _IbmappcInLluDefType_Type(Integer32):
    """Custom type ibmappcInLluDefType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("sysdef", 1))
    )


_IbmappcInLluDefType_Type.__name__ = "Integer32"
_IbmappcInLluDefType_Object = MibTableColumn
ibmappcInLluDefType = _IbmappcInLluDefType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1, 2),
    _IbmappcInLluDefType_Type()
)
ibmappcInLluDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLluDefType.setStatus("mandatory")
_IbmappcInLluSessLimit_Type = Integer32
_IbmappcInLluSessLimit_Object = MibTableColumn
ibmappcInLluSessLimit = _IbmappcInLluSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1, 3),
    _IbmappcInLluSessLimit_Type()
)
ibmappcInLluSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLluSessLimit.setStatus("mandatory")


class _IbmappcInLluBindRspMayQ_Type(Integer32):
    """Custom type ibmappcInLluBindRspMayQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLluBindRspMayQ_Type.__name__ = "Integer32"
_IbmappcInLluBindRspMayQ_Object = MibTableColumn
ibmappcInLluBindRspMayQ = _IbmappcInLluBindRspMayQ_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1, 4),
    _IbmappcInLluBindRspMayQ_Type()
)
ibmappcInLluBindRspMayQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLluBindRspMayQ.setStatus("mandatory")


class _IbmappcInLluDefaultLu_Type(Integer32):
    """Custom type ibmappcInLluDefaultLu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLluDefaultLu_Type.__name__ = "Integer32"
_IbmappcInLluDefaultLu_Object = MibTableColumn
ibmappcInLluDefaultLu = _IbmappcInLluDefaultLu_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1, 5),
    _IbmappcInLluDefaultLu_Type()
)
ibmappcInLluDefaultLu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLluDefaultLu.setStatus("mandatory")


class _IbmappcInLluCntlPtLu_Type(Integer32):
    """Custom type ibmappcInLluCntlPtLu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLluCntlPtLu_Type.__name__ = "Integer32"
_IbmappcInLluCntlPtLu_Object = MibTableColumn
ibmappcInLluCntlPtLu = _IbmappcInLluCntlPtLu_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1, 6),
    _IbmappcInLluCntlPtLu_Type()
)
ibmappcInLluCntlPtLu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLluCntlPtLu.setStatus("mandatory")
_IbmappcInLluCurActSess_Type = Gauge32
_IbmappcInLluCurActSess_Object = MibTableColumn
ibmappcInLluCurActSess = _IbmappcInLluCurActSess_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 2, 1, 7),
    _IbmappcInLluCurActSess_Type()
)
ibmappcInLluCurActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLluCurActSess.setStatus("mandatory")
_IbmappcInRluTable_Object = MibTable
ibmappcInRluTable = _IbmappcInRluTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ibmappcInRluTable.setStatus("mandatory")
_IbmappcInRluEntry_Object = MibTableRow
ibmappcInRluEntry = _IbmappcInRluEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1)
)
ibmappcInRluEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappcInRluLocLuName"),
    (0, "IBM6611-MIB", "ibmappcInRluParLuName"),
)
if mibBuilder.loadTexts:
    ibmappcInRluEntry.setStatus("mandatory")


class _IbmappcInRluLocLuName_Type(DisplayString):
    """Custom type ibmappcInRluLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInRluLocLuName_Type.__name__ = "DisplayString"
_IbmappcInRluLocLuName_Object = MibTableColumn
ibmappcInRluLocLuName = _IbmappcInRluLocLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 1),
    _IbmappcInRluLocLuName_Type()
)
ibmappcInRluLocLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluLocLuName.setStatus("mandatory")


class _IbmappcInRluParLuName_Type(DisplayString):
    """Custom type ibmappcInRluParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInRluParLuName_Type.__name__ = "DisplayString"
_IbmappcInRluParLuName_Object = MibTableColumn
ibmappcInRluParLuName = _IbmappcInRluParLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 2),
    _IbmappcInRluParLuName_Type()
)
ibmappcInRluParLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluParLuName.setStatus("mandatory")


class _IbmappcInRluParLuLocName_Type(DisplayString):
    """Custom type ibmappcInRluParLuLocName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInRluParLuLocName_Type.__name__ = "DisplayString"
_IbmappcInRluParLuLocName_Object = MibTableColumn
ibmappcInRluParLuLocName = _IbmappcInRluParLuLocName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 3),
    _IbmappcInRluParLuLocName_Type()
)
ibmappcInRluParLuLocName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluParLuLocName.setStatus("mandatory")


class _IbmappcInRluDefType_Type(Integer32):
    """Custom type ibmappcInRluDefType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("sysdef", 1))
    )


_IbmappcInRluDefType_Type.__name__ = "Integer32"
_IbmappcInRluDefType_Object = MibTableColumn
ibmappcInRluDefType = _IbmappcInRluDefType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 4),
    _IbmappcInRluDefType_Type()
)
ibmappcInRluDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluDefType.setStatus("mandatory")


class _IbmappcInRluDefParaSessSup_Type(Integer32):
    """Custom type ibmappcInRluDefParaSessSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluDefParaSessSup_Type.__name__ = "Integer32"
_IbmappcInRluDefParaSessSup_Object = MibTableColumn
ibmappcInRluDefParaSessSup = _IbmappcInRluDefParaSessSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 5),
    _IbmappcInRluDefParaSessSup_Type()
)
ibmappcInRluDefParaSessSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluDefParaSessSup.setStatus("mandatory")


class _IbmappcInRluDefCnosSup_Type(Integer32):
    """Custom type ibmappcInRluDefCnosSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluDefCnosSup_Type.__name__ = "Integer32"
_IbmappcInRluDefCnosSup_Object = MibTableColumn
ibmappcInRluDefCnosSup = _IbmappcInRluDefCnosSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 6),
    _IbmappcInRluDefCnosSup_Type()
)
ibmappcInRluDefCnosSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluDefCnosSup.setStatus("mandatory")


class _IbmappcInRluDefAllVerSup_Type(Integer32):
    """Custom type ibmappcInRluDefAllVerSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluDefAllVerSup_Type.__name__ = "Integer32"
_IbmappcInRluDefAllVerSup_Object = MibTableColumn
ibmappcInRluDefAllVerSup = _IbmappcInRluDefAllVerSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 7),
    _IbmappcInRluDefAllVerSup_Type()
)
ibmappcInRluDefAllVerSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluDefAllVerSup.setStatus("mandatory")


class _IbmappcInRluDefAttSecSup_Type(Integer32):
    """Custom type ibmappcInRluDefAttSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluDefAttSecSup_Type.__name__ = "Integer32"
_IbmappcInRluDefAttSecSup_Object = MibTableColumn
ibmappcInRluDefAttSecSup = _IbmappcInRluDefAttSecSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 8),
    _IbmappcInRluDefAttSecSup_Type()
)
ibmappcInRluDefAttSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluDefAttSecSup.setStatus("mandatory")


class _IbmappcInRluDefSessSecSup_Type(Integer32):
    """Custom type ibmappcInRluDefSessSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluDefSessSecSup_Type.__name__ = "Integer32"
_IbmappcInRluDefSessSecSup_Object = MibTableColumn
ibmappcInRluDefSessSecSup = _IbmappcInRluDefSessSecSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 9),
    _IbmappcInRluDefSessSecSup_Type()
)
ibmappcInRluDefSessSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluDefSessSecSup.setStatus("mandatory")


class _IbmappcInRluDefEnhanSecSup_Type(Integer32):
    """Custom type ibmappcInRluDefEnhanSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 2),
          ("level2", 3),
          ("none", 1))
    )


_IbmappcInRluDefEnhanSecSup_Type.__name__ = "Integer32"
_IbmappcInRluDefEnhanSecSup_Object = MibTableColumn
ibmappcInRluDefEnhanSecSup = _IbmappcInRluDefEnhanSecSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 10),
    _IbmappcInRluDefEnhanSecSup_Type()
)
ibmappcInRluDefEnhanSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluDefEnhanSecSup.setStatus("mandatory")


class _IbmappcInRluActType_Type(Integer32):
    """Custom type ibmappcInRluActType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_IbmappcInRluActType_Type.__name__ = "Integer32"
_IbmappcInRluActType_Object = MibTableColumn
ibmappcInRluActType = _IbmappcInRluActType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 11),
    _IbmappcInRluActType_Type()
)
ibmappcInRluActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluActType.setStatus("mandatory")


class _IbmappcInRluActParaSessSup_Type(Integer32):
    """Custom type ibmappcInRluActParaSessSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluActParaSessSup_Type.__name__ = "Integer32"
_IbmappcInRluActParaSessSup_Object = MibTableColumn
ibmappcInRluActParaSessSup = _IbmappcInRluActParaSessSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 12),
    _IbmappcInRluActParaSessSup_Type()
)
ibmappcInRluActParaSessSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluActParaSessSup.setStatus("mandatory")


class _IbmappcInRluActCnosSup_Type(Integer32):
    """Custom type ibmappcInRluActCnosSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluActCnosSup_Type.__name__ = "Integer32"
_IbmappcInRluActCnosSup_Object = MibTableColumn
ibmappcInRluActCnosSup = _IbmappcInRluActCnosSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 13),
    _IbmappcInRluActCnosSup_Type()
)
ibmappcInRluActCnosSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluActCnosSup.setStatus("mandatory")


class _IbmappcInRluActAllVerSup_Type(Integer32):
    """Custom type ibmappcInRluActAllVerSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluActAllVerSup_Type.__name__ = "Integer32"
_IbmappcInRluActAllVerSup_Object = MibTableColumn
ibmappcInRluActAllVerSup = _IbmappcInRluActAllVerSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 14),
    _IbmappcInRluActAllVerSup_Type()
)
ibmappcInRluActAllVerSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluActAllVerSup.setStatus("mandatory")


class _IbmappcInRluActAttSecSup_Type(Integer32):
    """Custom type ibmappcInRluActAttSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluActAttSecSup_Type.__name__ = "Integer32"
_IbmappcInRluActAttSecSup_Object = MibTableColumn
ibmappcInRluActAttSecSup = _IbmappcInRluActAttSecSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 15),
    _IbmappcInRluActAttSecSup_Type()
)
ibmappcInRluActAttSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluActAttSecSup.setStatus("mandatory")


class _IbmappcInRluActSessSecSup_Type(Integer32):
    """Custom type ibmappcInRluActSessSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInRluActSessSecSup_Type.__name__ = "Integer32"
_IbmappcInRluActSessSecSup_Object = MibTableColumn
ibmappcInRluActSessSecSup = _IbmappcInRluActSessSecSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 16),
    _IbmappcInRluActSessSecSup_Type()
)
ibmappcInRluActSessSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluActSessSecSup.setStatus("mandatory")


class _IbmappcInRluActEnhanSecSup_Type(Integer32):
    """Custom type ibmappcInRluActEnhanSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 2),
          ("level2", 3),
          ("none", 1))
    )


_IbmappcInRluActEnhanSecSup_Type.__name__ = "Integer32"
_IbmappcInRluActEnhanSecSup_Object = MibTableColumn
ibmappcInRluActEnhanSecSup = _IbmappcInRluActEnhanSecSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 3, 1, 17),
    _IbmappcInRluActEnhanSecSup_Type()
)
ibmappcInRluActEnhanSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInRluActEnhanSecSup.setStatus("mandatory")
_IbmappcInMdTable_Object = MibTable
ibmappcInMdTable = _IbmappcInMdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ibmappcInMdTable.setStatus("mandatory")
_IbmappcInMdEntry_Object = MibTableRow
ibmappcInMdEntry = _IbmappcInMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1)
)
ibmappcInMdEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappcInMdLluName"),
    (0, "IBM6611-MIB", "ibmappcInMdRluName"),
    (0, "IBM6611-MIB", "ibmappcInMdModeName"),
)
if mibBuilder.loadTexts:
    ibmappcInMdEntry.setStatus("mandatory")


class _IbmappcInMdLluName_Type(DisplayString):
    """Custom type ibmappcInMdLluName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInMdLluName_Type.__name__ = "DisplayString"
_IbmappcInMdLluName_Object = MibTableColumn
ibmappcInMdLluName = _IbmappcInMdLluName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 1),
    _IbmappcInMdLluName_Type()
)
ibmappcInMdLluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdLluName.setStatus("mandatory")


class _IbmappcInMdRluName_Type(DisplayString):
    """Custom type ibmappcInMdRluName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInMdRluName_Type.__name__ = "DisplayString"
_IbmappcInMdRluName_Object = MibTableColumn
ibmappcInMdRluName = _IbmappcInMdRluName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 2),
    _IbmappcInMdRluName_Type()
)
ibmappcInMdRluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdRluName.setStatus("mandatory")


class _IbmappcInMdModeName_Type(DisplayString):
    """Custom type ibmappcInMdModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappcInMdModeName_Type.__name__ = "DisplayString"
_IbmappcInMdModeName_Object = MibTableColumn
ibmappcInMdModeName = _IbmappcInMdModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 3),
    _IbmappcInMdModeName_Type()
)
ibmappcInMdModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdModeName.setStatus("mandatory")


class _IbmappcInMdDefType_Type(Integer32):
    """Custom type ibmappcInMdDefType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("sysdef", 1))
    )


_IbmappcInMdDefType_Type.__name__ = "Integer32"
_IbmappcInMdDefType_Object = MibTableColumn
ibmappcInMdDefType = _IbmappcInMdDefType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 4),
    _IbmappcInMdDefType_Type()
)
ibmappcInMdDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdDefType.setStatus("mandatory")


class _IbmappcInMdSessEndTpName_Type(DisplayString):
    """Custom type ibmappcInMdSessEndTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IbmappcInMdSessEndTpName_Type.__name__ = "DisplayString"
_IbmappcInMdSessEndTpName_Object = MibTableColumn
ibmappcInMdSessEndTpName = _IbmappcInMdSessEndTpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 5),
    _IbmappcInMdSessEndTpName_Type()
)
ibmappcInMdSessEndTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdSessEndTpName.setStatus("mandatory")
_IbmappcInMdSessLimit_Type = Integer32
_IbmappcInMdSessLimit_Object = MibTableColumn
ibmappcInMdSessLimit = _IbmappcInMdSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 6),
    _IbmappcInMdSessLimit_Type()
)
ibmappcInMdSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdSessLimit.setStatus("mandatory")
_IbmappcInMdMaxSessLimit_Type = Integer32
_IbmappcInMdMaxSessLimit_Object = MibTableColumn
ibmappcInMdMaxSessLimit = _IbmappcInMdMaxSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 7),
    _IbmappcInMdMaxSessLimit_Type()
)
ibmappcInMdMaxSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdMaxSessLimit.setStatus("mandatory")
_IbmappcInMdAutoActLimit_Type = Integer32
_IbmappcInMdAutoActLimit_Object = MibTableColumn
ibmappcInMdAutoActLimit = _IbmappcInMdAutoActLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 8),
    _IbmappcInMdAutoActLimit_Type()
)
ibmappcInMdAutoActLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdAutoActLimit.setStatus("mandatory")


class _IbmappcInMdDrainSelf_Type(Integer32):
    """Custom type ibmappcInMdDrainSelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInMdDrainSelf_Type.__name__ = "Integer32"
_IbmappcInMdDrainSelf_Object = MibTableColumn
ibmappcInMdDrainSelf = _IbmappcInMdDrainSelf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 9),
    _IbmappcInMdDrainSelf_Type()
)
ibmappcInMdDrainSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdDrainSelf.setStatus("mandatory")


class _IbmappcInMdDrainPart_Type(Integer32):
    """Custom type ibmappcInMdDrainPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInMdDrainPart_Type.__name__ = "Integer32"
_IbmappcInMdDrainPart_Object = MibTableColumn
ibmappcInMdDrainPart = _IbmappcInMdDrainPart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 10),
    _IbmappcInMdDrainPart_Type()
)
ibmappcInMdDrainPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdDrainPart.setStatus("mandatory")
_IbmappcInMdMinCwinLimit_Type = Integer32
_IbmappcInMdMinCwinLimit_Object = MibTableColumn
ibmappcInMdMinCwinLimit = _IbmappcInMdMinCwinLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 11),
    _IbmappcInMdMinCwinLimit_Type()
)
ibmappcInMdMinCwinLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdMinCwinLimit.setStatus("mandatory")
_IbmappcInMdMinClosLimit_Type = Integer32
_IbmappcInMdMinClosLimit_Object = MibTableColumn
ibmappcInMdMinClosLimit = _IbmappcInMdMinClosLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 12),
    _IbmappcInMdMinClosLimit_Type()
)
ibmappcInMdMinClosLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdMinClosLimit.setStatus("mandatory")
_IbmappcInMdRecvPacWinSz_Type = Integer32
_IbmappcInMdRecvPacWinSz_Object = MibTableColumn
ibmappcInMdRecvPacWinSz = _IbmappcInMdRecvPacWinSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 13),
    _IbmappcInMdRecvPacWinSz_Type()
)
ibmappcInMdRecvPacWinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdRecvPacWinSz.setStatus("mandatory")
_IbmappcInMdSendPacWinSz_Type = Integer32
_IbmappcInMdSendPacWinSz_Object = MibTableColumn
ibmappcInMdSendPacWinSz = _IbmappcInMdSendPacWinSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 14),
    _IbmappcInMdSendPacWinSz_Type()
)
ibmappcInMdSendPacWinSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdSendPacWinSz.setStatus("mandatory")
_IbmappcInMdPrefRecvRuSz_Type = Integer32
_IbmappcInMdPrefRecvRuSz_Object = MibTableColumn
ibmappcInMdPrefRecvRuSz = _IbmappcInMdPrefRecvRuSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 15),
    _IbmappcInMdPrefRecvRuSz_Type()
)
ibmappcInMdPrefRecvRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdPrefRecvRuSz.setStatus("mandatory")
_IbmappcInMdPrefSendRuSz_Type = Integer32
_IbmappcInMdPrefSendRuSz_Object = MibTableColumn
ibmappcInMdPrefSendRuSz = _IbmappcInMdPrefSendRuSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 16),
    _IbmappcInMdPrefSendRuSz_Type()
)
ibmappcInMdPrefSendRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdPrefSendRuSz.setStatus("mandatory")
_IbmappcInMdRecvRuSzUpBnd_Type = Integer32
_IbmappcInMdRecvRuSzUpBnd_Object = MibTableColumn
ibmappcInMdRecvRuSzUpBnd = _IbmappcInMdRecvRuSzUpBnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 17),
    _IbmappcInMdRecvRuSzUpBnd_Type()
)
ibmappcInMdRecvRuSzUpBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdRecvRuSzUpBnd.setStatus("mandatory")
_IbmappcInMdSendRuSzUpBnd_Type = Integer32
_IbmappcInMdSendRuSzUpBnd_Object = MibTableColumn
ibmappcInMdSendRuSzUpBnd = _IbmappcInMdSendRuSzUpBnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 18),
    _IbmappcInMdSendRuSzUpBnd_Type()
)
ibmappcInMdSendRuSzUpBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdSendRuSzUpBnd.setStatus("mandatory")
_IbmappcInMdRecvRuSzLoBnd_Type = Integer32
_IbmappcInMdRecvRuSzLoBnd_Object = MibTableColumn
ibmappcInMdRecvRuSzLoBnd = _IbmappcInMdRecvRuSzLoBnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 19),
    _IbmappcInMdRecvRuSzLoBnd_Type()
)
ibmappcInMdRecvRuSzLoBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdRecvRuSzLoBnd.setStatus("mandatory")
_IbmappcInMdSendRuSzLoBnd_Type = Integer32
_IbmappcInMdSendRuSzLoBnd_Object = MibTableColumn
ibmappcInMdSendRuSzLoBnd = _IbmappcInMdSendRuSzLoBnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 20),
    _IbmappcInMdSendRuSzLoBnd_Type()
)
ibmappcInMdSendRuSzLoBnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdSendRuSzLoBnd.setStatus("mandatory")


class _IbmappcInMdDfSyncLvl_Type(Integer32):
    """Custom type ibmappcInMdDfSyncLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 2),
          ("none", 1),
          ("syncPoint", 3))
    )


_IbmappcInMdDfSyncLvl_Type.__name__ = "Integer32"
_IbmappcInMdDfSyncLvl_Object = MibTableColumn
ibmappcInMdDfSyncLvl = _IbmappcInMdDfSyncLvl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 21),
    _IbmappcInMdDfSyncLvl_Type()
)
ibmappcInMdDfSyncLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdDfSyncLvl.setStatus("mandatory")


class _IbmappcInMdAcSyncLvl_Type(Integer32):
    """Custom type ibmappcInMdAcSyncLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 2),
          ("none", 1),
          ("syncPoint", 3))
    )


_IbmappcInMdAcSyncLvl_Type.__name__ = "Integer32"
_IbmappcInMdAcSyncLvl_Object = MibTableColumn
ibmappcInMdAcSyncLvl = _IbmappcInMdAcSyncLvl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 22),
    _IbmappcInMdAcSyncLvl_Type()
)
ibmappcInMdAcSyncLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdAcSyncLvl.setStatus("mandatory")


class _IbmappcInMdDfCrypto_Type(Integer32):
    """Custom type ibmappcInMdDfCrypto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInMdDfCrypto_Type.__name__ = "Integer32"
_IbmappcInMdDfCrypto_Object = MibTableColumn
ibmappcInMdDfCrypto = _IbmappcInMdDfCrypto_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 23),
    _IbmappcInMdDfCrypto_Type()
)
ibmappcInMdDfCrypto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdDfCrypto.setStatus("mandatory")


class _IbmappcInMdAcCrypto_Type(Integer32):
    """Custom type ibmappcInMdAcCrypto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInMdAcCrypto_Type.__name__ = "Integer32"
_IbmappcInMdAcCrypto_Object = MibTableColumn
ibmappcInMdAcCrypto = _IbmappcInMdAcCrypto_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 24),
    _IbmappcInMdAcCrypto_Type()
)
ibmappcInMdAcCrypto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdAcCrypto.setStatus("mandatory")


class _IbmappcInMdReinit_Type(Integer32):
    """Custom type ibmappcInMdReinit based on Integer32"""
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
        *(("operatorControlled", 1),
          ("primaryOnly", 2),
          ("primaryOrSecondary", 4),
          ("secondaryOnly", 3))
    )


_IbmappcInMdReinit_Type.__name__ = "Integer32"
_IbmappcInMdReinit_Object = MibTableColumn
ibmappcInMdReinit = _IbmappcInMdReinit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 25),
    _IbmappcInMdReinit_Type()
)
ibmappcInMdReinit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdReinit.setStatus("mandatory")


class _IbmappcInMdAltCode_Type(Integer32):
    """Custom type ibmappcInMdAltCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInMdAltCode_Type.__name__ = "Integer32"
_IbmappcInMdAltCode_Object = MibTableColumn
ibmappcInMdAltCode = _IbmappcInMdAltCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 26),
    _IbmappcInMdAltCode_Type()
)
ibmappcInMdAltCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdAltCode.setStatus("mandatory")
_IbmappcInMdActCwin_Type = Gauge32
_IbmappcInMdActCwin_Object = MibTableColumn
ibmappcInMdActCwin = _IbmappcInMdActCwin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 27),
    _IbmappcInMdActCwin_Type()
)
ibmappcInMdActCwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdActCwin.setStatus("mandatory")
_IbmappcInMdActClos_Type = Gauge32
_IbmappcInMdActClos_Object = MibTableColumn
ibmappcInMdActClos = _IbmappcInMdActClos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 28),
    _IbmappcInMdActClos_Type()
)
ibmappcInMdActClos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdActClos.setStatus("mandatory")
_IbmappcInMdPndCwin_Type = Gauge32
_IbmappcInMdPndCwin_Object = MibTableColumn
ibmappcInMdPndCwin = _IbmappcInMdPndCwin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 29),
    _IbmappcInMdPndCwin_Type()
)
ibmappcInMdPndCwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdPndCwin.setStatus("mandatory")
_IbmappcInMdPndClos_Type = Gauge32
_IbmappcInMdPndClos_Object = MibTableColumn
ibmappcInMdPndClos = _IbmappcInMdPndClos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 30),
    _IbmappcInMdPndClos_Type()
)
ibmappcInMdPndClos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdPndClos.setStatus("mandatory")
_IbmappcInMdPtmCwin_Type = Gauge32
_IbmappcInMdPtmCwin_Object = MibTableColumn
ibmappcInMdPtmCwin = _IbmappcInMdPtmCwin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 31),
    _IbmappcInMdPtmCwin_Type()
)
ibmappcInMdPtmCwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdPtmCwin.setStatus("mandatory")
_IbmappcInMdPtmClos_Type = Gauge32
_IbmappcInMdPtmClos_Object = MibTableColumn
ibmappcInMdPtmClos = _IbmappcInMdPtmClos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 32),
    _IbmappcInMdPtmClos_Type()
)
ibmappcInMdPtmClos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdPtmClos.setStatus("mandatory")
_IbmappcInMdFreeSessLst_Type = Gauge32
_IbmappcInMdFreeSessLst_Object = MibTableColumn
ibmappcInMdFreeSessLst = _IbmappcInMdFreeSessLst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 33),
    _IbmappcInMdFreeSessLst_Type()
)
ibmappcInMdFreeSessLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdFreeSessLst.setStatus("mandatory")
_IbmappcInMdWaitReqLst_Type = Gauge32
_IbmappcInMdWaitReqLst_Object = MibTableColumn
ibmappcInMdWaitReqLst = _IbmappcInMdWaitReqLst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 4, 1, 34),
    _IbmappcInMdWaitReqLst_Type()
)
ibmappcInMdWaitReqLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInMdWaitReqLst.setStatus("mandatory")
_IbmappcInLtpTable_Object = MibTable
ibmappcInLtpTable = _IbmappcInLtpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ibmappcInLtpTable.setStatus("mandatory")
_IbmappcInLtpEntry_Object = MibTableRow
ibmappcInLtpEntry = _IbmappcInLtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1)
)
ibmappcInLtpEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappcInLtpLuName"),
    (0, "IBM6611-MIB", "ibmappcInLtpTpName"),
)
if mibBuilder.loadTexts:
    ibmappcInLtpEntry.setStatus("mandatory")


class _IbmappcInLtpLuName_Type(DisplayString):
    """Custom type ibmappcInLtpLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInLtpLuName_Type.__name__ = "DisplayString"
_IbmappcInLtpLuName_Object = MibTableColumn
ibmappcInLtpLuName = _IbmappcInLtpLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 1),
    _IbmappcInLtpLuName_Type()
)
ibmappcInLtpLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpLuName.setStatus("mandatory")


class _IbmappcInLtpTpName_Type(DisplayString):
    """Custom type ibmappcInLtpTpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IbmappcInLtpTpName_Type.__name__ = "DisplayString"
_IbmappcInLtpTpName_Object = MibTableColumn
ibmappcInLtpTpName = _IbmappcInLtpTpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 2),
    _IbmappcInLtpTpName_Type()
)
ibmappcInLtpTpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpTpName.setStatus("mandatory")


class _IbmappcInLtpDefType_Type(Integer32):
    """Custom type ibmappcInLtpDefType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("sysdef", 1))
    )


_IbmappcInLtpDefType_Type.__name__ = "Integer32"
_IbmappcInLtpDefType_Object = MibTableColumn
ibmappcInLtpDefType = _IbmappcInLtpDefType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 3),
    _IbmappcInLtpDefType_Type()
)
ibmappcInLtpDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpDefType.setStatus("mandatory")


class _IbmappcInLtpSyncLvl_Type(Integer32):
    """Custom type ibmappcInLtpSyncLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 2),
          ("none", 1),
          ("syncPoint", 3))
    )


_IbmappcInLtpSyncLvl_Type.__name__ = "Integer32"
_IbmappcInLtpSyncLvl_Object = MibTableColumn
ibmappcInLtpSyncLvl = _IbmappcInLtpSyncLvl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 4),
    _IbmappcInLtpSyncLvl_Type()
)
ibmappcInLtpSyncLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpSyncLvl.setStatus("mandatory")
_IbmappcInLtpInstLmt_Type = Integer32
_IbmappcInLtpInstLmt_Object = MibTableColumn
ibmappcInLtpInstLmt = _IbmappcInLtpInstLmt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 5),
    _IbmappcInLtpInstLmt_Type()
)
ibmappcInLtpInstLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpInstLmt.setStatus("mandatory")
_IbmappcInLtpInstNum_Type = Gauge32
_IbmappcInLtpInstNum_Object = MibTableColumn
ibmappcInLtpInstNum = _IbmappcInLtpInstNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 6),
    _IbmappcInLtpInstNum_Type()
)
ibmappcInLtpInstNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpInstNum.setStatus("mandatory")


class _IbmappcInLtpStatus_Type(Integer32):
    """Custom type ibmappcInLtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("permDisabled", 3),
          ("tempDisabled", 2))
    )


_IbmappcInLtpStatus_Type.__name__ = "Integer32"
_IbmappcInLtpStatus_Object = MibTableColumn
ibmappcInLtpStatus = _IbmappcInLtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 7),
    _IbmappcInLtpStatus_Type()
)
ibmappcInLtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpStatus.setStatus("mandatory")


class _IbmappcInLtpLongRun_Type(Integer32):
    """Custom type ibmappcInLtpLongRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpLongRun_Type.__name__ = "Integer32"
_IbmappcInLtpLongRun_Object = MibTableColumn
ibmappcInLtpLongRun = _IbmappcInLtpLongRun_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 8),
    _IbmappcInLtpLongRun_Type()
)
ibmappcInLtpLongRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpLongRun.setStatus("mandatory")


class _IbmappcInLtpPfCnos_Type(Integer32):
    """Custom type ibmappcInLtpPfCnos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpPfCnos_Type.__name__ = "Integer32"
_IbmappcInLtpPfCnos_Object = MibTableColumn
ibmappcInLtpPfCnos = _IbmappcInLtpPfCnos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 9),
    _IbmappcInLtpPfCnos_Type()
)
ibmappcInLtpPfCnos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpPfCnos.setStatus("mandatory")


class _IbmappcInLtpPfSessCntl_Type(Integer32):
    """Custom type ibmappcInLtpPfSessCntl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpPfSessCntl_Type.__name__ = "Integer32"
_IbmappcInLtpPfSessCntl_Object = MibTableColumn
ibmappcInLtpPfSessCntl = _IbmappcInLtpPfSessCntl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 10),
    _IbmappcInLtpPfSessCntl_Type()
)
ibmappcInLtpPfSessCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpPfSessCntl.setStatus("mandatory")


class _IbmappcInLtpPfDefine_Type(Integer32):
    """Custom type ibmappcInLtpPfDefine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpPfDefine_Type.__name__ = "Integer32"
_IbmappcInLtpPfDefine_Object = MibTableColumn
ibmappcInLtpPfDefine = _IbmappcInLtpPfDefine_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 11),
    _IbmappcInLtpPfDefine_Type()
)
ibmappcInLtpPfDefine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpPfDefine.setStatus("mandatory")


class _IbmappcInLtpPfDisplay_Type(Integer32):
    """Custom type ibmappcInLtpPfDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpPfDisplay_Type.__name__ = "Integer32"
_IbmappcInLtpPfDisplay_Object = MibTableColumn
ibmappcInLtpPfDisplay = _IbmappcInLtpPfDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 12),
    _IbmappcInLtpPfDisplay_Type()
)
ibmappcInLtpPfDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpPfDisplay.setStatus("mandatory")


class _IbmappcInLtpPfAllocSer_Type(Integer32):
    """Custom type ibmappcInLtpPfAllocSer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpPfAllocSer_Type.__name__ = "Integer32"
_IbmappcInLtpPfAllocSer_Object = MibTableColumn
ibmappcInLtpPfAllocSer = _IbmappcInLtpPfAllocSer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 13),
    _IbmappcInLtpPfAllocSer_Type()
)
ibmappcInLtpPfAllocSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpPfAllocSer.setStatus("mandatory")


class _IbmappcInLtpRescSup_Type(Integer32):
    """Custom type ibmappcInLtpRescSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allConv", 3),
          ("basicConv", 1),
          ("mappedConv", 2))
    )


_IbmappcInLtpRescSup_Type.__name__ = "Integer32"
_IbmappcInLtpRescSup_Object = MibTableColumn
ibmappcInLtpRescSup = _IbmappcInLtpRescSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 14),
    _IbmappcInLtpRescSup_Type()
)
ibmappcInLtpRescSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpRescSup.setStatus("mandatory")


class _IbmappcInLtpRecoSup_Type(Integer32):
    """Custom type ibmappcInLtpRecoSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpRecoSup_Type.__name__ = "Integer32"
_IbmappcInLtpRecoSup_Object = MibTableColumn
ibmappcInLtpRecoSup = _IbmappcInLtpRecoSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 15),
    _IbmappcInLtpRecoSup_Type()
)
ibmappcInLtpRecoSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpRecoSup.setStatus("mandatory")


class _IbmappcInLtpSecReq_Type(Integer32):
    """Custom type ibmappcInLtpSecReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpSecReq_Type.__name__ = "Integer32"
_IbmappcInLtpSecReq_Object = MibTableColumn
ibmappcInLtpSecReq = _IbmappcInLtpSecReq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 16),
    _IbmappcInLtpSecReq_Type()
)
ibmappcInLtpSecReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpSecReq.setStatus("mandatory")


class _IbmappcInLtpSecLvl_Type(Integer32):
    """Custom type ibmappcInLtpSecLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAdditional", 1),
          ("specificProfiles", 3),
          ("specificUserLus", 5),
          ("specificUserProfLus", 6),
          ("specificUserProfiles", 4),
          ("specificUsers", 2))
    )


_IbmappcInLtpSecLvl_Type.__name__ = "Integer32"
_IbmappcInLtpSecLvl_Object = MibTableColumn
ibmappcInLtpSecLvl = _IbmappcInLtpSecLvl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 17),
    _IbmappcInLtpSecLvl_Type()
)
ibmappcInLtpSecLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpSecLvl.setStatus("mandatory")


class _IbmappcInLtpVerPip_Type(Integer32):
    """Custom type ibmappcInLtpVerPip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IbmappcInLtpVerPip_Type.__name__ = "Integer32"
_IbmappcInLtpVerPip_Object = MibTableColumn
ibmappcInLtpVerPip = _IbmappcInLtpVerPip_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 18),
    _IbmappcInLtpVerPip_Type()
)
ibmappcInLtpVerPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpVerPip.setStatus("mandatory")
_IbmappcInLtpPipSubNum_Type = Integer32
_IbmappcInLtpPipSubNum_Object = MibTableColumn
ibmappcInLtpPipSubNum = _IbmappcInLtpPipSubNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 5, 1, 19),
    _IbmappcInLtpPipSubNum_Type()
)
ibmappcInLtpPipSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInLtpPipSubNum.setStatus("mandatory")
_IbmappcInSsTable_Object = MibTable
ibmappcInSsTable = _IbmappcInSsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ibmappcInSsTable.setStatus("mandatory")
_IbmappcInSsEntry_Object = MibTableRow
ibmappcInSsEntry = _IbmappcInSsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1)
)
ibmappcInSsEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappcInSsFqLuName"),
    (0, "IBM6611-MIB", "ibmappcInSsPcid"),
)
if mibBuilder.loadTexts:
    ibmappcInSsEntry.setStatus("mandatory")


class _IbmappcInSsFqLuName_Type(DisplayString):
    """Custom type ibmappcInSsFqLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInSsFqLuName_Type.__name__ = "DisplayString"
_IbmappcInSsFqLuName_Object = MibTableColumn
ibmappcInSsFqLuName = _IbmappcInSsFqLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 1),
    _IbmappcInSsFqLuName_Type()
)
ibmappcInSsFqLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsFqLuName.setStatus("mandatory")


class _IbmappcInSsPcid_Type(OctetString):
    """Custom type ibmappcInSsPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbmappcInSsPcid_Type.__name__ = "OctetString"
_IbmappcInSsPcid_Object = MibTableColumn
ibmappcInSsPcid = _IbmappcInSsPcid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 2),
    _IbmappcInSsPcid_Type()
)
ibmappcInSsPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsPcid.setStatus("mandatory")


class _IbmappcInSsPluName_Type(DisplayString):
    """Custom type ibmappcInSsPluName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInSsPluName_Type.__name__ = "DisplayString"
_IbmappcInSsPluName_Object = MibTableColumn
ibmappcInSsPluName = _IbmappcInSsPluName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 3),
    _IbmappcInSsPluName_Type()
)
ibmappcInSsPluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsPluName.setStatus("mandatory")


class _IbmappcInSsSluName_Type(DisplayString):
    """Custom type ibmappcInSsSluName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInSsSluName_Type.__name__ = "DisplayString"
_IbmappcInSsSluName_Object = MibTableColumn
ibmappcInSsSluName = _IbmappcInSsSluName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 4),
    _IbmappcInSsSluName_Type()
)
ibmappcInSsSluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSluName.setStatus("mandatory")


class _IbmappcInSsModeName_Type(DisplayString):
    """Custom type ibmappcInSsModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappcInSsModeName_Type.__name__ = "DisplayString"
_IbmappcInSsModeName_Object = MibTableColumn
ibmappcInSsModeName = _IbmappcInSsModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 5),
    _IbmappcInSsModeName_Type()
)
ibmappcInSsModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsModeName.setStatus("mandatory")


class _IbmappcInSsCosName_Type(DisplayString):
    """Custom type ibmappcInSsCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappcInSsCosName_Type.__name__ = "DisplayString"
_IbmappcInSsCosName_Object = MibTableColumn
ibmappcInSsCosName = _IbmappcInSsCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 6),
    _IbmappcInSsCosName_Type()
)
ibmappcInSsCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsCosName.setStatus("mandatory")


class _IbmappcInSsSessType_Type(Integer32):
    """Custom type ibmappcInSsSessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("lu62", 1)
    )


_IbmappcInSsSessType_Type.__name__ = "Integer32"
_IbmappcInSsSessType_Object = MibTableColumn
ibmappcInSsSessType = _IbmappcInSsSessType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 7),
    _IbmappcInSsSessType_Type()
)
ibmappcInSsSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSessType.setStatus("mandatory")


class _IbmappcInSsSessState_Type(Integer32):
    """Custom type ibmappcInSsSessState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappcInSsSessState_Type.__name__ = "Integer32"
_IbmappcInSsSessState_Object = MibTableColumn
ibmappcInSsSessState = _IbmappcInSsSessState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 8),
    _IbmappcInSsSessState_Type()
)
ibmappcInSsSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSessState.setStatus("mandatory")
_IbmappcInSsTransPriority_Type = Integer32
_IbmappcInSsTransPriority_Object = MibTableColumn
ibmappcInSsTransPriority = _IbmappcInSsTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 9),
    _IbmappcInSsTransPriority_Type()
)
ibmappcInSsTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsTransPriority.setStatus("mandatory")


class _IbmappcInSsPaceType_Type(Integer32):
    """Custom type ibmappcInSsPaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("fixed", 2),
          ("none", 1))
    )


_IbmappcInSsPaceType_Type.__name__ = "Integer32"
_IbmappcInSsPaceType_Object = MibTableColumn
ibmappcInSsPaceType = _IbmappcInSsPaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 10),
    _IbmappcInSsPaceType_Type()
)
ibmappcInSsPaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsPaceType.setStatus("mandatory")
_IbmappcInSsSendMaxRuSz_Type = Integer32
_IbmappcInSsSendMaxRuSz_Object = MibTableColumn
ibmappcInSsSendMaxRuSz = _IbmappcInSsSendMaxRuSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 11),
    _IbmappcInSsSendMaxRuSz_Type()
)
ibmappcInSsSendMaxRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSendMaxRuSz.setStatus("mandatory")
_IbmappcInSsRecvMaxRuSz_Type = Integer32
_IbmappcInSsRecvMaxRuSz_Object = MibTableColumn
ibmappcInSsRecvMaxRuSz = _IbmappcInSsRecvMaxRuSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 12),
    _IbmappcInSsRecvMaxRuSz_Type()
)
ibmappcInSsRecvMaxRuSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsRecvMaxRuSz.setStatus("mandatory")


class _IbmappcInSsEnhanceSecSup_Type(Integer32):
    """Custom type ibmappcInSsEnhanceSecSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 2),
          ("level2", 3),
          ("none", 1))
    )


_IbmappcInSsEnhanceSecSup_Type.__name__ = "Integer32"
_IbmappcInSsEnhanceSecSup_Object = MibTableColumn
ibmappcInSsEnhanceSecSup = _IbmappcInSsEnhanceSecSup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 13),
    _IbmappcInSsEnhanceSecSup_Type()
)
ibmappcInSsEnhanceSecSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsEnhanceSecSup.setStatus("mandatory")


class _IbmappcInSsSendPacingType_Type(Integer32):
    """Custom type ibmappcInSsSendPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("fixed", 2),
          ("none", 1))
    )


_IbmappcInSsSendPacingType_Type.__name__ = "Integer32"
_IbmappcInSsSendPacingType_Object = MibTableColumn
ibmappcInSsSendPacingType = _IbmappcInSsSendPacingType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 14),
    _IbmappcInSsSendPacingType_Type()
)
ibmappcInSsSendPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSendPacingType.setStatus("mandatory")
_IbmappcInSsSendRpc_Type = Gauge32
_IbmappcInSsSendRpc_Object = MibTableColumn
ibmappcInSsSendRpc = _IbmappcInSsSendRpc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 15),
    _IbmappcInSsSendRpc_Type()
)
ibmappcInSsSendRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSendRpc.setStatus("mandatory")
_IbmappcInSsSendNxWndwSize_Type = Gauge32
_IbmappcInSsSendNxWndwSize_Object = MibTableColumn
ibmappcInSsSendNxWndwSize = _IbmappcInSsSendNxWndwSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 16),
    _IbmappcInSsSendNxWndwSize_Type()
)
ibmappcInSsSendNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSendNxWndwSize.setStatus("mandatory")


class _IbmappcInSsRecvPacingType_Type(Integer32):
    """Custom type ibmappcInSsRecvPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("fixed", 2),
          ("none", 1))
    )


_IbmappcInSsRecvPacingType_Type.__name__ = "Integer32"
_IbmappcInSsRecvPacingType_Object = MibTableColumn
ibmappcInSsRecvPacingType = _IbmappcInSsRecvPacingType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 17),
    _IbmappcInSsRecvPacingType_Type()
)
ibmappcInSsRecvPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsRecvPacingType.setStatus("mandatory")
_IbmappcInSsRecvRpc_Type = Gauge32
_IbmappcInSsRecvRpc_Object = MibTableColumn
ibmappcInSsRecvRpc = _IbmappcInSsRecvRpc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 18),
    _IbmappcInSsRecvRpc_Type()
)
ibmappcInSsRecvRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsRecvRpc.setStatus("mandatory")
_IbmappcInSsRecvNxWndwSize_Type = Gauge32
_IbmappcInSsRecvNxWndwSize_Object = MibTableColumn
ibmappcInSsRecvNxWndwSize = _IbmappcInSsRecvNxWndwSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 19),
    _IbmappcInSsRecvNxWndwSize_Type()
)
ibmappcInSsRecvNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsRecvNxWndwSize.setStatus("mandatory")
_IbmappcInSsSessStartTime_Type = TimeTicks
_IbmappcInSsSessStartTime_Object = MibTableColumn
ibmappcInSsSessStartTime = _IbmappcInSsSessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 20),
    _IbmappcInSsSessStartTime_Type()
)
ibmappcInSsSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSessStartTime.setStatus("mandatory")
_IbmappcInSsSessUpTime_Type = TimeTicks
_IbmappcInSsSessUpTime_Object = MibTableColumn
ibmappcInSsSessUpTime = _IbmappcInSsSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 21),
    _IbmappcInSsSessUpTime_Type()
)
ibmappcInSsSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsSessUpTime.setStatus("mandatory")
_IbmappcInSsCtrUpTime_Type = TimeTicks
_IbmappcInSsCtrUpTime_Object = MibTableColumn
ibmappcInSsCtrUpTime = _IbmappcInSsCtrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 22),
    _IbmappcInSsCtrUpTime_Type()
)
ibmappcInSsCtrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsCtrUpTime.setStatus("mandatory")
_IbmappcInSsP2SFmdPius_Type = Counter32
_IbmappcInSsP2SFmdPius_Object = MibTableColumn
ibmappcInSsP2SFmdPius = _IbmappcInSsP2SFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 23),
    _IbmappcInSsP2SFmdPius_Type()
)
ibmappcInSsP2SFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsP2SFmdPius.setStatus("mandatory")
_IbmappcInSsS2PFmdPius_Type = Counter32
_IbmappcInSsS2PFmdPius_Object = MibTableColumn
ibmappcInSsS2PFmdPius = _IbmappcInSsS2PFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 24),
    _IbmappcInSsS2PFmdPius_Type()
)
ibmappcInSsS2PFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsS2PFmdPius.setStatus("mandatory")
_IbmappcInSsP2SNonFmdPius_Type = Counter32
_IbmappcInSsP2SNonFmdPius_Object = MibTableColumn
ibmappcInSsP2SNonFmdPius = _IbmappcInSsP2SNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 25),
    _IbmappcInSsP2SNonFmdPius_Type()
)
ibmappcInSsP2SNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsP2SNonFmdPius.setStatus("mandatory")
_IbmappcInSsS2PNonFmdPius_Type = Counter32
_IbmappcInSsS2PNonFmdPius_Object = MibTableColumn
ibmappcInSsS2PNonFmdPius = _IbmappcInSsS2PNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 26),
    _IbmappcInSsS2PNonFmdPius_Type()
)
ibmappcInSsS2PNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsS2PNonFmdPius.setStatus("mandatory")
_IbmappcInSsP2SFmdBytes_Type = Counter32
_IbmappcInSsP2SFmdBytes_Object = MibTableColumn
ibmappcInSsP2SFmdBytes = _IbmappcInSsP2SFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 27),
    _IbmappcInSsP2SFmdBytes_Type()
)
ibmappcInSsP2SFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsP2SFmdBytes.setStatus("mandatory")
_IbmappcInSsS2PFmdBytes_Type = Counter32
_IbmappcInSsS2PFmdBytes_Object = MibTableColumn
ibmappcInSsS2PFmdBytes = _IbmappcInSsS2PFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 28),
    _IbmappcInSsS2PFmdBytes_Type()
)
ibmappcInSsS2PFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsS2PFmdBytes.setStatus("mandatory")
_IbmappcInSsP2SNonFmdBytes_Type = Counter32
_IbmappcInSsP2SNonFmdBytes_Object = MibTableColumn
ibmappcInSsP2SNonFmdBytes = _IbmappcInSsP2SNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 29),
    _IbmappcInSsP2SNonFmdBytes_Type()
)
ibmappcInSsP2SNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsP2SNonFmdBytes.setStatus("mandatory")
_IbmappcInSsS2PNonFmdBytes_Type = Counter32
_IbmappcInSsS2PNonFmdBytes_Object = MibTableColumn
ibmappcInSsS2PNonFmdBytes = _IbmappcInSsS2PNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 30),
    _IbmappcInSsS2PNonFmdBytes_Type()
)
ibmappcInSsS2PNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsS2PNonFmdBytes.setStatus("mandatory")
_IbmappcInSsRscv_Type = OctetString
_IbmappcInSsRscv_Object = MibTableColumn
ibmappcInSsRscv = _IbmappcInSsRscv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 6, 1, 31),
    _IbmappcInSsRscv_Type()
)
ibmappcInSsRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsRscv.setStatus("mandatory")
_IbmappcInSsStatusTable_Object = MibTable
ibmappcInSsStatusTable = _IbmappcInSsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ibmappcInSsStatusTable.setStatus("mandatory")
_IbmappcInSsStatusEntry_Object = MibTableRow
ibmappcInSsStatusEntry = _IbmappcInSsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1)
)
ibmappcInSsStatusEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappcInSsStatusIndex"),
)
if mibBuilder.loadTexts:
    ibmappcInSsStatusEntry.setStatus("mandatory")
_IbmappcInSsStatusIndex_Type = Integer32
_IbmappcInSsStatusIndex_Object = MibTableColumn
ibmappcInSsStatusIndex = _IbmappcInSsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 1),
    _IbmappcInSsStatusIndex_Type()
)
ibmappcInSsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusIndex.setStatus("mandatory")
_IbmappcInSsStatusTime_Type = TimeTicks
_IbmappcInSsStatusTime_Object = MibTableColumn
ibmappcInSsStatusTime = _IbmappcInSsStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 2),
    _IbmappcInSsStatusTime_Type()
)
ibmappcInSsStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusTime.setStatus("mandatory")


class _IbmappcInSsStatusType_Type(Integer32):
    """Custom type ibmappcInSsStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("recvNegBindRsp", 1),
          ("sendNegBindRsp", 2),
          ("sessActRejected", 3),
          ("unbindReceived", 5),
          ("unbindSent", 4))
    )


_IbmappcInSsStatusType_Type.__name__ = "Integer32"
_IbmappcInSsStatusType_Object = MibTableColumn
ibmappcInSsStatusType = _IbmappcInSsStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 3),
    _IbmappcInSsStatusType_Type()
)
ibmappcInSsStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusType.setStatus("mandatory")


class _IbmappcInSsStatusLocLuName_Type(DisplayString):
    """Custom type ibmappcInSsStatusLocLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInSsStatusLocLuName_Type.__name__ = "DisplayString"
_IbmappcInSsStatusLocLuName_Object = MibTableColumn
ibmappcInSsStatusLocLuName = _IbmappcInSsStatusLocLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 4),
    _IbmappcInSsStatusLocLuName_Type()
)
ibmappcInSsStatusLocLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusLocLuName.setStatus("mandatory")


class _IbmappcInSsStatusParLuName_Type(DisplayString):
    """Custom type ibmappcInSsStatusParLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappcInSsStatusParLuName_Type.__name__ = "DisplayString"
_IbmappcInSsStatusParLuName_Object = MibTableColumn
ibmappcInSsStatusParLuName = _IbmappcInSsStatusParLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 5),
    _IbmappcInSsStatusParLuName_Type()
)
ibmappcInSsStatusParLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusParLuName.setStatus("mandatory")


class _IbmappcInSsStatusModeName_Type(DisplayString):
    """Custom type ibmappcInSsStatusModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappcInSsStatusModeName_Type.__name__ = "DisplayString"
_IbmappcInSsStatusModeName_Object = MibTableColumn
ibmappcInSsStatusModeName = _IbmappcInSsStatusModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 6),
    _IbmappcInSsStatusModeName_Type()
)
ibmappcInSsStatusModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusModeName.setStatus("mandatory")


class _IbmappcInSsStatusUnbindType_Type(OctetString):
    """Custom type ibmappcInSsStatusUnbindType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappcInSsStatusUnbindType_Type.__name__ = "OctetString"
_IbmappcInSsStatusUnbindType_Object = MibTableColumn
ibmappcInSsStatusUnbindType = _IbmappcInSsStatusUnbindType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 7),
    _IbmappcInSsStatusUnbindType_Type()
)
ibmappcInSsStatusUnbindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusUnbindType.setStatus("mandatory")


class _IbmappcInSsStatusSenseCode_Type(OctetString):
    """Custom type ibmappcInSsStatusSenseCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmappcInSsStatusSenseCode_Type.__name__ = "OctetString"
_IbmappcInSsStatusSenseCode_Object = MibTableColumn
ibmappcInSsStatusSenseCode = _IbmappcInSsStatusSenseCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 8),
    _IbmappcInSsStatusSenseCode_Type()
)
ibmappcInSsStatusSenseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusSenseCode.setStatus("mandatory")


class _IbmappcInSsStatusComponentId_Type(DisplayString):
    """Custom type ibmappcInSsStatusComponentId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappcInSsStatusComponentId_Type.__name__ = "DisplayString"
_IbmappcInSsStatusComponentId_Object = MibTableColumn
ibmappcInSsStatusComponentId = _IbmappcInSsStatusComponentId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 9),
    _IbmappcInSsStatusComponentId_Type()
)
ibmappcInSsStatusComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusComponentId.setStatus("mandatory")


class _IbmappcInSsStatusDetectModule_Type(DisplayString):
    """Custom type ibmappcInSsStatusDetectModule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappcInSsStatusDetectModule_Type.__name__ = "DisplayString"
_IbmappcInSsStatusDetectModule_Object = MibTableColumn
ibmappcInSsStatusDetectModule = _IbmappcInSsStatusDetectModule_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 2, 1, 7, 1, 10),
    _IbmappcInSsStatusDetectModule_Type()
)
ibmappcInSsStatusDetectModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappcInSsStatusDetectModule.setStatus("mandatory")
_IbmappnSessIntermediate_ObjectIdentity = ObjectIdentity
ibmappnSessIntermediate = _IbmappnSessIntermediate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3)
)
_IbmappnIsInformation_ObjectIdentity = ObjectIdentity
ibmappnIsInformation = _IbmappnIsInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1)
)
_IbmappnIsInGlobal_ObjectIdentity = ObjectIdentity
ibmappnIsInGlobal = _IbmappnIsInGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 1)
)


class _IbmappnIsInGlobeStatus_Type(Integer32):
    """Custom type ibmappnIsInGlobeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmappnIsInGlobeStatus_Type.__name__ = "Integer32"
_IbmappnIsInGlobeStatus_Object = MibScalar
ibmappnIsInGlobeStatus = _IbmappnIsInGlobeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 1, 1),
    _IbmappnIsInGlobeStatus_Type()
)
ibmappnIsInGlobeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsInGlobeStatus.setStatus("mandatory")


class _IbmappnIsInGlobeRscv_Type(Integer32):
    """Custom type ibmappnIsInGlobeRscv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmappnIsInGlobeRscv_Type.__name__ = "Integer32"
_IbmappnIsInGlobeRscv_Object = MibScalar
ibmappnIsInGlobeRscv = _IbmappnIsInGlobeRscv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 1, 2),
    _IbmappnIsInGlobeRscv_Type()
)
ibmappnIsInGlobeRscv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsInGlobeRscv.setStatus("mandatory")
_IbmappnIsInGlobeRscvTime_Type = TimeTicks
_IbmappnIsInGlobeRscvTime_Object = MibScalar
ibmappnIsInGlobeRscvTime = _IbmappnIsInGlobeRscvTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 1, 3),
    _IbmappnIsInGlobeRscvTime_Type()
)
ibmappnIsInGlobeRscvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInGlobeRscvTime.setStatus("mandatory")


class _IbmappnIsInGlobeCtrStatus_Type(Integer32):
    """Custom type ibmappnIsInGlobeCtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmappnIsInGlobeCtrStatus_Type.__name__ = "Integer32"
_IbmappnIsInGlobeCtrStatus_Object = MibScalar
ibmappnIsInGlobeCtrStatus = _IbmappnIsInGlobeCtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 1, 4),
    _IbmappnIsInGlobeCtrStatus_Type()
)
ibmappnIsInGlobeCtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsInGlobeCtrStatus.setStatus("mandatory")
_IbmappnIsInGlobeCtrStatusTime_Type = TimeTicks
_IbmappnIsInGlobeCtrStatusTime_Object = MibScalar
ibmappnIsInGlobeCtrStatusTime = _IbmappnIsInGlobeCtrStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 1, 5),
    _IbmappnIsInGlobeCtrStatusTime_Type()
)
ibmappnIsInGlobeCtrStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInGlobeCtrStatusTime.setStatus("mandatory")
_IbmappnIsInTable_Object = MibTable
ibmappnIsInTable = _IbmappnIsInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibmappnIsInTable.setStatus("mandatory")
_IbmappnIsInEntry_Object = MibTableRow
ibmappnIsInEntry = _IbmappnIsInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1)
)
ibmappnIsInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnIsInFqLuName"),
    (0, "IBM6611-MIB", "ibmappnIsInPcid"),
)
if mibBuilder.loadTexts:
    ibmappnIsInEntry.setStatus("mandatory")


class _IbmappnIsInFqLuName_Type(DisplayString):
    """Custom type ibmappnIsInFqLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsInFqLuName_Type.__name__ = "DisplayString"
_IbmappnIsInFqLuName_Object = MibTableColumn
ibmappnIsInFqLuName = _IbmappnIsInFqLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 1),
    _IbmappnIsInFqLuName_Type()
)
ibmappnIsInFqLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInFqLuName.setStatus("mandatory")


class _IbmappnIsInPcid_Type(OctetString):
    """Custom type ibmappnIsInPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbmappnIsInPcid_Type.__name__ = "OctetString"
_IbmappnIsInPcid_Object = MibTableColumn
ibmappnIsInPcid = _IbmappnIsInPcid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 2),
    _IbmappnIsInPcid_Type()
)
ibmappnIsInPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPcid.setStatus("mandatory")


class _IbmappnIsInPriLuName_Type(DisplayString):
    """Custom type ibmappnIsInPriLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsInPriLuName_Type.__name__ = "DisplayString"
_IbmappnIsInPriLuName_Object = MibTableColumn
ibmappnIsInPriLuName = _IbmappnIsInPriLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 3),
    _IbmappnIsInPriLuName_Type()
)
ibmappnIsInPriLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPriLuName.setStatus("mandatory")


class _IbmappnIsInSecLuName_Type(DisplayString):
    """Custom type ibmappnIsInSecLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsInSecLuName_Type.__name__ = "DisplayString"
_IbmappnIsInSecLuName_Object = MibTableColumn
ibmappnIsInSecLuName = _IbmappnIsInSecLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 4),
    _IbmappnIsInSecLuName_Type()
)
ibmappnIsInSecLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSecLuName.setStatus("mandatory")


class _IbmappnIsInModeName_Type(DisplayString):
    """Custom type ibmappnIsInModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnIsInModeName_Type.__name__ = "DisplayString"
_IbmappnIsInModeName_Object = MibTableColumn
ibmappnIsInModeName = _IbmappnIsInModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 5),
    _IbmappnIsInModeName_Type()
)
ibmappnIsInModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInModeName.setStatus("mandatory")


class _IbmappnIsInCosName_Type(DisplayString):
    """Custom type ibmappnIsInCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnIsInCosName_Type.__name__ = "DisplayString"
_IbmappnIsInCosName_Object = MibTableColumn
ibmappnIsInCosName = _IbmappnIsInCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 6),
    _IbmappnIsInCosName_Type()
)
ibmappnIsInCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInCosName.setStatus("mandatory")
_IbmappnIsInTransPriority_Type = Integer32
_IbmappnIsInTransPriority_Object = MibTableColumn
ibmappnIsInTransPriority = _IbmappnIsInTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 7),
    _IbmappnIsInTransPriority_Type()
)
ibmappnIsInTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInTransPriority.setStatus("mandatory")


class _IbmappnIsInSessType_Type(Integer32):
    """Custom type ibmappnIsInSessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lu0thru3", 2),
          ("lu62", 1))
    )


_IbmappnIsInSessType_Type.__name__ = "Integer32"
_IbmappnIsInSessType_Object = MibTableColumn
ibmappnIsInSessType = _IbmappnIsInSessType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 8),
    _IbmappnIsInSessType_Type()
)
ibmappnIsInSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSessType.setStatus("mandatory")


class _IbmappnIsInSessState_Type(Integer32):
    """Custom type ibmappnIsInSessState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnIsInSessState_Type.__name__ = "Integer32"
_IbmappnIsInSessState_Object = MibTableColumn
ibmappnIsInSessState = _IbmappnIsInSessState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 9),
    _IbmappnIsInSessState_Type()
)
ibmappnIsInSessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsInSessState.setStatus("mandatory")
_IbmappnIsInSessStartTime_Type = TimeTicks
_IbmappnIsInSessStartTime_Object = MibTableColumn
ibmappnIsInSessStartTime = _IbmappnIsInSessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 10),
    _IbmappnIsInSessStartTime_Type()
)
ibmappnIsInSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSessStartTime.setStatus("mandatory")
_IbmappnIsInSessUpTime_Type = TimeTicks
_IbmappnIsInSessUpTime_Object = MibTableColumn
ibmappnIsInSessUpTime = _IbmappnIsInSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 11),
    _IbmappnIsInSessUpTime_Type()
)
ibmappnIsInSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSessUpTime.setStatus("mandatory")
_IbmappnIsInCtrUpTime_Type = TimeTicks
_IbmappnIsInCtrUpTime_Object = MibTableColumn
ibmappnIsInCtrUpTime = _IbmappnIsInCtrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 12),
    _IbmappnIsInCtrUpTime_Type()
)
ibmappnIsInCtrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInCtrUpTime.setStatus("mandatory")
_IbmappnIsInP2SFmdPius_Type = Counter32
_IbmappnIsInP2SFmdPius_Object = MibTableColumn
ibmappnIsInP2SFmdPius = _IbmappnIsInP2SFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 13),
    _IbmappnIsInP2SFmdPius_Type()
)
ibmappnIsInP2SFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInP2SFmdPius.setStatus("mandatory")
_IbmappnIsInS2PFmdPius_Type = Counter32
_IbmappnIsInS2PFmdPius_Object = MibTableColumn
ibmappnIsInS2PFmdPius = _IbmappnIsInS2PFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 14),
    _IbmappnIsInS2PFmdPius_Type()
)
ibmappnIsInS2PFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInS2PFmdPius.setStatus("mandatory")
_IbmappnIsInP2SNonFmdPius_Type = Counter32
_IbmappnIsInP2SNonFmdPius_Object = MibTableColumn
ibmappnIsInP2SNonFmdPius = _IbmappnIsInP2SNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 15),
    _IbmappnIsInP2SNonFmdPius_Type()
)
ibmappnIsInP2SNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInP2SNonFmdPius.setStatus("mandatory")
_IbmappnIsInS2PNonFmdPius_Type = Counter32
_IbmappnIsInS2PNonFmdPius_Object = MibTableColumn
ibmappnIsInS2PNonFmdPius = _IbmappnIsInS2PNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 16),
    _IbmappnIsInS2PNonFmdPius_Type()
)
ibmappnIsInS2PNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInS2PNonFmdPius.setStatus("mandatory")
_IbmappnIsInP2SFmdBytes_Type = Counter32
_IbmappnIsInP2SFmdBytes_Object = MibTableColumn
ibmappnIsInP2SFmdBytes = _IbmappnIsInP2SFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 17),
    _IbmappnIsInP2SFmdBytes_Type()
)
ibmappnIsInP2SFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInP2SFmdBytes.setStatus("mandatory")
_IbmappnIsInS2PFmdBytes_Type = Counter32
_IbmappnIsInS2PFmdBytes_Object = MibTableColumn
ibmappnIsInS2PFmdBytes = _IbmappnIsInS2PFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 18),
    _IbmappnIsInS2PFmdBytes_Type()
)
ibmappnIsInS2PFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInS2PFmdBytes.setStatus("mandatory")
_IbmappnIsInP2SNonFmdBytes_Type = Counter32
_IbmappnIsInP2SNonFmdBytes_Object = MibTableColumn
ibmappnIsInP2SNonFmdBytes = _IbmappnIsInP2SNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 19),
    _IbmappnIsInP2SNonFmdBytes_Type()
)
ibmappnIsInP2SNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInP2SNonFmdBytes.setStatus("mandatory")
_IbmappnIsInS2PNonFmdBytes_Type = Counter32
_IbmappnIsInS2PNonFmdBytes_Object = MibTableColumn
ibmappnIsInS2PNonFmdBytes = _IbmappnIsInS2PNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 20),
    _IbmappnIsInS2PNonFmdBytes_Type()
)
ibmappnIsInS2PNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInS2PNonFmdBytes.setStatus("mandatory")


class _IbmappnIsInPsAdjCpName_Type(DisplayString):
    """Custom type ibmappnIsInPsAdjCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsInPsAdjCpName_Type.__name__ = "DisplayString"
_IbmappnIsInPsAdjCpName_Object = MibTableColumn
ibmappnIsInPsAdjCpName = _IbmappnIsInPsAdjCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 21),
    _IbmappnIsInPsAdjCpName_Type()
)
ibmappnIsInPsAdjCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsAdjCpName.setStatus("mandatory")
_IbmappnIsInPsAdjTgNum_Type = Integer32
_IbmappnIsInPsAdjTgNum_Object = MibTableColumn
ibmappnIsInPsAdjTgNum = _IbmappnIsInPsAdjTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 22),
    _IbmappnIsInPsAdjTgNum_Type()
)
ibmappnIsInPsAdjTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsAdjTgNum.setStatus("mandatory")
_IbmappnIsInPsSendMaxBtuSize_Type = Integer32
_IbmappnIsInPsSendMaxBtuSize_Object = MibTableColumn
ibmappnIsInPsSendMaxBtuSize = _IbmappnIsInPsSendMaxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 23),
    _IbmappnIsInPsSendMaxBtuSize_Type()
)
ibmappnIsInPsSendMaxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsSendMaxBtuSize.setStatus("mandatory")


class _IbmappnIsInPsSendPacingType_Type(Integer32):
    """Custom type ibmappnIsInPsSendPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_IbmappnIsInPsSendPacingType_Type.__name__ = "Integer32"
_IbmappnIsInPsSendPacingType_Object = MibTableColumn
ibmappnIsInPsSendPacingType = _IbmappnIsInPsSendPacingType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 24),
    _IbmappnIsInPsSendPacingType_Type()
)
ibmappnIsInPsSendPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsSendPacingType.setStatus("mandatory")
_IbmappnIsInPsSendRpc_Type = Gauge32
_IbmappnIsInPsSendRpc_Object = MibTableColumn
ibmappnIsInPsSendRpc = _IbmappnIsInPsSendRpc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 25),
    _IbmappnIsInPsSendRpc_Type()
)
ibmappnIsInPsSendRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsSendRpc.setStatus("mandatory")
_IbmappnIsInPsSendNxWndwSize_Type = Gauge32
_IbmappnIsInPsSendNxWndwSize_Object = MibTableColumn
ibmappnIsInPsSendNxWndwSize = _IbmappnIsInPsSendNxWndwSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 26),
    _IbmappnIsInPsSendNxWndwSize_Type()
)
ibmappnIsInPsSendNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsSendNxWndwSize.setStatus("mandatory")


class _IbmappnIsInPsRecvPacingType_Type(Integer32):
    """Custom type ibmappnIsInPsRecvPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_IbmappnIsInPsRecvPacingType_Type.__name__ = "Integer32"
_IbmappnIsInPsRecvPacingType_Object = MibTableColumn
ibmappnIsInPsRecvPacingType = _IbmappnIsInPsRecvPacingType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 27),
    _IbmappnIsInPsRecvPacingType_Type()
)
ibmappnIsInPsRecvPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsRecvPacingType.setStatus("mandatory")
_IbmappnIsInPsRecvRpc_Type = Gauge32
_IbmappnIsInPsRecvRpc_Object = MibTableColumn
ibmappnIsInPsRecvRpc = _IbmappnIsInPsRecvRpc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 28),
    _IbmappnIsInPsRecvRpc_Type()
)
ibmappnIsInPsRecvRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsRecvRpc.setStatus("mandatory")
_IbmappnIsInPsRecvNxWndwSize_Type = Gauge32
_IbmappnIsInPsRecvNxWndwSize_Object = MibTableColumn
ibmappnIsInPsRecvNxWndwSize = _IbmappnIsInPsRecvNxWndwSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 29),
    _IbmappnIsInPsRecvNxWndwSize_Type()
)
ibmappnIsInPsRecvNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInPsRecvNxWndwSize.setStatus("mandatory")


class _IbmappnIsInSsAdjCpName_Type(DisplayString):
    """Custom type ibmappnIsInSsAdjCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsInSsAdjCpName_Type.__name__ = "DisplayString"
_IbmappnIsInSsAdjCpName_Object = MibTableColumn
ibmappnIsInSsAdjCpName = _IbmappnIsInSsAdjCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 30),
    _IbmappnIsInSsAdjCpName_Type()
)
ibmappnIsInSsAdjCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsAdjCpName.setStatus("mandatory")
_IbmappnIsInSsAdjTgNum_Type = Integer32
_IbmappnIsInSsAdjTgNum_Object = MibTableColumn
ibmappnIsInSsAdjTgNum = _IbmappnIsInSsAdjTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 31),
    _IbmappnIsInSsAdjTgNum_Type()
)
ibmappnIsInSsAdjTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsAdjTgNum.setStatus("mandatory")
_IbmappnIsInSsSendMaxBtuSize_Type = Integer32
_IbmappnIsInSsSendMaxBtuSize_Object = MibTableColumn
ibmappnIsInSsSendMaxBtuSize = _IbmappnIsInSsSendMaxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 32),
    _IbmappnIsInSsSendMaxBtuSize_Type()
)
ibmappnIsInSsSendMaxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsSendMaxBtuSize.setStatus("mandatory")


class _IbmappnIsInSsSendPacingType_Type(Integer32):
    """Custom type ibmappnIsInSsSendPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_IbmappnIsInSsSendPacingType_Type.__name__ = "Integer32"
_IbmappnIsInSsSendPacingType_Object = MibTableColumn
ibmappnIsInSsSendPacingType = _IbmappnIsInSsSendPacingType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 33),
    _IbmappnIsInSsSendPacingType_Type()
)
ibmappnIsInSsSendPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsSendPacingType.setStatus("mandatory")
_IbmappnIsInSsSendRpc_Type = Gauge32
_IbmappnIsInSsSendRpc_Object = MibTableColumn
ibmappnIsInSsSendRpc = _IbmappnIsInSsSendRpc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 34),
    _IbmappnIsInSsSendRpc_Type()
)
ibmappnIsInSsSendRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsSendRpc.setStatus("mandatory")
_IbmappnIsInSsSendNxWndwSize_Type = Gauge32
_IbmappnIsInSsSendNxWndwSize_Object = MibTableColumn
ibmappnIsInSsSendNxWndwSize = _IbmappnIsInSsSendNxWndwSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 35),
    _IbmappnIsInSsSendNxWndwSize_Type()
)
ibmappnIsInSsSendNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsSendNxWndwSize.setStatus("mandatory")


class _IbmappnIsInSsRecvPacingType_Type(Integer32):
    """Custom type ibmappnIsInSsRecvPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_IbmappnIsInSsRecvPacingType_Type.__name__ = "Integer32"
_IbmappnIsInSsRecvPacingType_Object = MibTableColumn
ibmappnIsInSsRecvPacingType = _IbmappnIsInSsRecvPacingType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 36),
    _IbmappnIsInSsRecvPacingType_Type()
)
ibmappnIsInSsRecvPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsRecvPacingType.setStatus("mandatory")
_IbmappnIsInSsRecvRpc_Type = Gauge32
_IbmappnIsInSsRecvRpc_Object = MibTableColumn
ibmappnIsInSsRecvRpc = _IbmappnIsInSsRecvRpc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 37),
    _IbmappnIsInSsRecvRpc_Type()
)
ibmappnIsInSsRecvRpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsRecvRpc.setStatus("mandatory")
_IbmappnIsInSsRecvNxWndwSize_Type = Gauge32
_IbmappnIsInSsRecvNxWndwSize_Object = MibTableColumn
ibmappnIsInSsRecvNxWndwSize = _IbmappnIsInSsRecvNxWndwSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 38),
    _IbmappnIsInSsRecvNxWndwSize_Type()
)
ibmappnIsInSsRecvNxWndwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInSsRecvNxWndwSize.setStatus("mandatory")
_IbmappnIsInRouteInfo_Type = OctetString
_IbmappnIsInRouteInfo_Object = MibTableColumn
ibmappnIsInRouteInfo = _IbmappnIsInRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 1, 2, 1, 39),
    _IbmappnIsInRouteInfo_Type()
)
ibmappnIsInRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsInRouteInfo.setStatus("mandatory")
_IbmappnIsAccounting_ObjectIdentity = ObjectIdentity
ibmappnIsAccounting = _IbmappnIsAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2)
)
_IbmappnIsAcGlobal_ObjectIdentity = ObjectIdentity
ibmappnIsAcGlobal = _IbmappnIsAcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1)
)


class _IbmappnIsAcGlobeStatus_Type(Integer32):
    """Custom type ibmappnIsAcGlobeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeButFull", 3),
          ("activeNotFull", 2),
          ("notActive", 1))
    )


_IbmappnIsAcGlobeStatus_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeStatus_Object = MibScalar
ibmappnIsAcGlobeStatus = _IbmappnIsAcGlobeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 1),
    _IbmappnIsAcGlobeStatus_Type()
)
ibmappnIsAcGlobeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeStatus.setStatus("mandatory")
_IbmappnIsAcGlobeByteThresh_Type = Integer32
_IbmappnIsAcGlobeByteThresh_Object = MibScalar
ibmappnIsAcGlobeByteThresh = _IbmappnIsAcGlobeByteThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 2),
    _IbmappnIsAcGlobeByteThresh_Type()
)
ibmappnIsAcGlobeByteThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeByteThresh.setStatus("mandatory")


class _IbmappnIsAcGlobeCheckPt_Type(Integer32):
    """Custom type ibmappnIsAcGlobeCheckPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("yes", 2))
    )


_IbmappnIsAcGlobeCheckPt_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeCheckPt_Object = MibScalar
ibmappnIsAcGlobeCheckPt = _IbmappnIsAcGlobeCheckPt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 3),
    _IbmappnIsAcGlobeCheckPt_Type()
)
ibmappnIsAcGlobeCheckPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeCheckPt.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcSecs_Type = Integer32
_IbmappnIsAcGlobeMgrUtcSecs_Object = MibScalar
ibmappnIsAcGlobeMgrUtcSecs = _IbmappnIsAcGlobeMgrUtcSecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 4),
    _IbmappnIsAcGlobeMgrUtcSecs_Type()
)
ibmappnIsAcGlobeMgrUtcSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcSecs.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcMins_Type = Integer32
_IbmappnIsAcGlobeMgrUtcMins_Object = MibScalar
ibmappnIsAcGlobeMgrUtcMins = _IbmappnIsAcGlobeMgrUtcMins_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 5),
    _IbmappnIsAcGlobeMgrUtcMins_Type()
)
ibmappnIsAcGlobeMgrUtcMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcMins.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcHours_Type = Integer32
_IbmappnIsAcGlobeMgrUtcHours_Object = MibScalar
ibmappnIsAcGlobeMgrUtcHours = _IbmappnIsAcGlobeMgrUtcHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 6),
    _IbmappnIsAcGlobeMgrUtcHours_Type()
)
ibmappnIsAcGlobeMgrUtcHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcHours.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcMdays_Type = Integer32
_IbmappnIsAcGlobeMgrUtcMdays_Object = MibScalar
ibmappnIsAcGlobeMgrUtcMdays = _IbmappnIsAcGlobeMgrUtcMdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 7),
    _IbmappnIsAcGlobeMgrUtcMdays_Type()
)
ibmappnIsAcGlobeMgrUtcMdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcMdays.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcMonths_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 12),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_IbmappnIsAcGlobeMgrUtcMonths_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcMonths_Object = MibScalar
ibmappnIsAcGlobeMgrUtcMonths = _IbmappnIsAcGlobeMgrUtcMonths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 8),
    _IbmappnIsAcGlobeMgrUtcMonths_Type()
)
ibmappnIsAcGlobeMgrUtcMonths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcMonths.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcYears_Type = Integer32
_IbmappnIsAcGlobeMgrUtcYears_Object = MibScalar
ibmappnIsAcGlobeMgrUtcYears = _IbmappnIsAcGlobeMgrUtcYears_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 9),
    _IbmappnIsAcGlobeMgrUtcYears_Type()
)
ibmappnIsAcGlobeMgrUtcYears.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcYears.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcWdays_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcWdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_IbmappnIsAcGlobeMgrUtcWdays_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcWdays_Object = MibScalar
ibmappnIsAcGlobeMgrUtcWdays = _IbmappnIsAcGlobeMgrUtcWdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 10),
    _IbmappnIsAcGlobeMgrUtcWdays_Type()
)
ibmappnIsAcGlobeMgrUtcWdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcWdays.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcYdays_Type = Integer32
_IbmappnIsAcGlobeMgrUtcYdays_Object = MibScalar
ibmappnIsAcGlobeMgrUtcYdays = _IbmappnIsAcGlobeMgrUtcYdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 11),
    _IbmappnIsAcGlobeMgrUtcYdays_Type()
)
ibmappnIsAcGlobeMgrUtcYdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcYdays.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcIsdst_Type = Integer32
_IbmappnIsAcGlobeMgrUtcIsdst_Object = MibScalar
ibmappnIsAcGlobeMgrUtcIsdst = _IbmappnIsAcGlobeMgrUtcIsdst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 12),
    _IbmappnIsAcGlobeMgrUtcIsdst_Type()
)
ibmappnIsAcGlobeMgrUtcIsdst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcIsdst.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrName_Type(DisplayString):
    """Custom type ibmappnIsAcGlobeMgrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcGlobeMgrName_Type.__name__ = "DisplayString"
_IbmappnIsAcGlobeMgrName_Object = MibScalar
ibmappnIsAcGlobeMgrName = _IbmappnIsAcGlobeMgrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 13),
    _IbmappnIsAcGlobeMgrName_Type()
)
ibmappnIsAcGlobeMgrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrName.setStatus("mandatory")
_IbmappnIsAcBtypeTable_Object = MibTable
ibmappnIsAcBtypeTable = _IbmappnIsAcBtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeTable.setStatus("mandatory")
_IbmappnIsAcBtypeEntry_Object = MibTableRow
ibmappnIsAcBtypeEntry = _IbmappnIsAcBtypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1)
)
ibmappnIsAcBtypeEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnIsAcBtypeMedia"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeEntry.setStatus("mandatory")


class _IbmappnIsAcBtypeMedia_Type(Integer32):
    """Custom type ibmappnIsAcBtypeMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dasd", 2),
          ("memory", 1))
    )


_IbmappnIsAcBtypeMedia_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeMedia_Object = MibTableColumn
ibmappnIsAcBtypeMedia = _IbmappnIsAcBtypeMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 1),
    _IbmappnIsAcBtypeMedia_Type()
)
ibmappnIsAcBtypeMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeMedia.setStatus("mandatory")


class _IbmappnIsAcBtypeActive_Type(Integer32):
    """Custom type ibmappnIsAcBtypeActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IbmappnIsAcBtypeActive_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeActive_Object = MibTableColumn
ibmappnIsAcBtypeActive = _IbmappnIsAcBtypeActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 2),
    _IbmappnIsAcBtypeActive_Type()
)
ibmappnIsAcBtypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeActive.setStatus("mandatory")
_IbmappnIsAcBtypeDirName_Type = DisplayString
_IbmappnIsAcBtypeDirName_Object = MibTableColumn
ibmappnIsAcBtypeDirName = _IbmappnIsAcBtypeDirName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 3),
    _IbmappnIsAcBtypeDirName_Type()
)
ibmappnIsAcBtypeDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeDirName.setStatus("mandatory")
_IbmappnIsAcBtypePrdMaxBufs_Type = Integer32
_IbmappnIsAcBtypePrdMaxBufs_Object = MibTableColumn
ibmappnIsAcBtypePrdMaxBufs = _IbmappnIsAcBtypePrdMaxBufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 4),
    _IbmappnIsAcBtypePrdMaxBufs_Type()
)
ibmappnIsAcBtypePrdMaxBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypePrdMaxBufs.setStatus("mandatory")
_IbmappnIsAcBtypeMaxBufs_Type = Integer32
_IbmappnIsAcBtypeMaxBufs_Object = MibTableColumn
ibmappnIsAcBtypeMaxBufs = _IbmappnIsAcBtypeMaxBufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 5),
    _IbmappnIsAcBtypeMaxBufs_Type()
)
ibmappnIsAcBtypeMaxBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeMaxBufs.setStatus("mandatory")
_IbmappnIsAcBtypeCurBufs_Type = Gauge32
_IbmappnIsAcBtypeCurBufs_Object = MibTableColumn
ibmappnIsAcBtypeCurBufs = _IbmappnIsAcBtypeCurBufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 6),
    _IbmappnIsAcBtypeCurBufs_Type()
)
ibmappnIsAcBtypeCurBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeCurBufs.setStatus("mandatory")
_IbmappnIsAcBtypePrdRecPerBuf_Type = Integer32
_IbmappnIsAcBtypePrdRecPerBuf_Object = MibTableColumn
ibmappnIsAcBtypePrdRecPerBuf = _IbmappnIsAcBtypePrdRecPerBuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 7),
    _IbmappnIsAcBtypePrdRecPerBuf_Type()
)
ibmappnIsAcBtypePrdRecPerBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypePrdRecPerBuf.setStatus("mandatory")
_IbmappnIsAcBtypeRecPerBuf_Type = Integer32
_IbmappnIsAcBtypeRecPerBuf_Object = MibTableColumn
ibmappnIsAcBtypeRecPerBuf = _IbmappnIsAcBtypeRecPerBuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 8),
    _IbmappnIsAcBtypeRecPerBuf_Type()
)
ibmappnIsAcBtypeRecPerBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeRecPerBuf.setStatus("mandatory")


class _IbmappnIsAcBtypeRecFormat_Type(Integer32):
    """Custom type ibmappnIsAcBtypeRecFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_IbmappnIsAcBtypeRecFormat_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeRecFormat_Object = MibTableColumn
ibmappnIsAcBtypeRecFormat = _IbmappnIsAcBtypeRecFormat_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 9),
    _IbmappnIsAcBtypeRecFormat_Type()
)
ibmappnIsAcBtypeRecFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeRecFormat.setStatus("mandatory")


class _IbmappnIsAcBtypeFullAction_Type(Integer32):
    """Custom type ibmappnIsAcBtypeFullAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halt", 1),
          ("wrap", 2))
    )


_IbmappnIsAcBtypeFullAction_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeFullAction_Object = MibTableColumn
ibmappnIsAcBtypeFullAction = _IbmappnIsAcBtypeFullAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 10),
    _IbmappnIsAcBtypeFullAction_Type()
)
ibmappnIsAcBtypeFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullAction.setStatus("mandatory")
_IbmappnIsAcBtypeFullTime_Type = TimeTicks
_IbmappnIsAcBtypeFullTime_Object = MibTableColumn
ibmappnIsAcBtypeFullTime = _IbmappnIsAcBtypeFullTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 11),
    _IbmappnIsAcBtypeFullTime_Type()
)
ibmappnIsAcBtypeFullTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullTime.setStatus("mandatory")


class _IbmappnIsAcBtypeFullReason_Type(Integer32):
    """Custom type ibmappnIsAcBtypeFullReason based on Integer32"""
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
        *(("ioErrors", 4),
          ("logicallyFull", 3),
          ("notFull", 1),
          ("physicallyFull", 2))
    )


_IbmappnIsAcBtypeFullReason_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeFullReason_Object = MibTableColumn
ibmappnIsAcBtypeFullReason = _IbmappnIsAcBtypeFullReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 12),
    _IbmappnIsAcBtypeFullReason_Type()
)
ibmappnIsAcBtypeFullReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullReason.setStatus("mandatory")
_IbmappnIsAcBtypeFullWraps_Type = Integer32
_IbmappnIsAcBtypeFullWraps_Object = MibTableColumn
ibmappnIsAcBtypeFullWraps = _IbmappnIsAcBtypeFullWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 13),
    _IbmappnIsAcBtypeFullWraps_Type()
)
ibmappnIsAcBtypeFullWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullWraps.setStatus("mandatory")
_IbmappnIsAcBtypeFullLosts_Type = Integer32
_IbmappnIsAcBtypeFullLosts_Object = MibTableColumn
ibmappnIsAcBtypeFullLosts = _IbmappnIsAcBtypeFullLosts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 14),
    _IbmappnIsAcBtypeFullLosts_Type()
)
ibmappnIsAcBtypeFullLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullLosts.setStatus("mandatory")
_IbmappnIsAcBtypeErrorWraps_Type = Integer32
_IbmappnIsAcBtypeErrorWraps_Object = MibTableColumn
ibmappnIsAcBtypeErrorWraps = _IbmappnIsAcBtypeErrorWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 15),
    _IbmappnIsAcBtypeErrorWraps_Type()
)
ibmappnIsAcBtypeErrorWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeErrorWraps.setStatus("mandatory")
_IbmappnIsAcBtypeErrorLosts_Type = Integer32
_IbmappnIsAcBtypeErrorLosts_Object = MibTableColumn
ibmappnIsAcBtypeErrorLosts = _IbmappnIsAcBtypeErrorLosts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 16),
    _IbmappnIsAcBtypeErrorLosts_Type()
)
ibmappnIsAcBtypeErrorLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeErrorLosts.setStatus("mandatory")
_IbmappnIsAcBtypeCheckPts_Type = Integer32
_IbmappnIsAcBtypeCheckPts_Object = MibTableColumn
ibmappnIsAcBtypeCheckPts = _IbmappnIsAcBtypeCheckPts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 17),
    _IbmappnIsAcBtypeCheckPts_Type()
)
ibmappnIsAcBtypeCheckPts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeCheckPts.setStatus("mandatory")
_IbmappnIsAcBtypePurges_Type = Integer32
_IbmappnIsAcBtypePurges_Object = MibTableColumn
ibmappnIsAcBtypePurges = _IbmappnIsAcBtypePurges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 18),
    _IbmappnIsAcBtypePurges_Type()
)
ibmappnIsAcBtypePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypePurges.setStatus("mandatory")
_IbmappnIsAcBtypeDeletes_Type = Integer32
_IbmappnIsAcBtypeDeletes_Object = MibTableColumn
ibmappnIsAcBtypeDeletes = _IbmappnIsAcBtypeDeletes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 19),
    _IbmappnIsAcBtypeDeletes_Type()
)
ibmappnIsAcBtypeDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeDeletes.setStatus("mandatory")
_IbmappnIsAcBtypeResets_Type = Integer32
_IbmappnIsAcBtypeResets_Object = MibTableColumn
ibmappnIsAcBtypeResets = _IbmappnIsAcBtypeResets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 20),
    _IbmappnIsAcBtypeResets_Type()
)
ibmappnIsAcBtypeResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeResets.setStatus("mandatory")


class _IbmappnIsAcBtypeClearStats_Type(Integer32):
    """Custom type ibmappnIsAcBtypeClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("yes", 2))
    )


_IbmappnIsAcBtypeClearStats_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeClearStats_Object = MibTableColumn
ibmappnIsAcBtypeClearStats = _IbmappnIsAcBtypeClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 21),
    _IbmappnIsAcBtypeClearStats_Type()
)
ibmappnIsAcBtypeClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeClearStats.setStatus("mandatory")
_IbmappnIsAcBufTable_Object = MibTable
ibmappnIsAcBufTable = _IbmappnIsAcBufTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ibmappnIsAcBufTable.setStatus("mandatory")
_IbmappnIsAcBufEntry_Object = MibTableRow
ibmappnIsAcBufEntry = _IbmappnIsAcBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1)
)
ibmappnIsAcBufEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnIsAcBufMedia"),
    (0, "IBM6611-MIB", "ibmappnIsAcBufNumber"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcBufEntry.setStatus("mandatory")


class _IbmappnIsAcBufMedia_Type(Integer32):
    """Custom type ibmappnIsAcBufMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dasd", 2),
          ("memory", 1))
    )


_IbmappnIsAcBufMedia_Type.__name__ = "Integer32"
_IbmappnIsAcBufMedia_Object = MibTableColumn
ibmappnIsAcBufMedia = _IbmappnIsAcBufMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 1),
    _IbmappnIsAcBufMedia_Type()
)
ibmappnIsAcBufMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufMedia.setStatus("mandatory")
_IbmappnIsAcBufNumber_Type = Integer32
_IbmappnIsAcBufNumber_Object = MibTableColumn
ibmappnIsAcBufNumber = _IbmappnIsAcBufNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 2),
    _IbmappnIsAcBufNumber_Type()
)
ibmappnIsAcBufNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufNumber.setStatus("mandatory")


class _IbmappnIsAcBufState_Type(Integer32):
    """Custom type ibmappnIsAcBufState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("complete", 1),
          ("purge", 3))
    )


_IbmappnIsAcBufState_Type.__name__ = "Integer32"
_IbmappnIsAcBufState_Object = MibTableColumn
ibmappnIsAcBufState = _IbmappnIsAcBufState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 3),
    _IbmappnIsAcBufState_Type()
)
ibmappnIsAcBufState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBufState.setStatus("mandatory")


class _IbmappnIsAcBufRecFormat_Type(Integer32):
    """Custom type ibmappnIsAcBufRecFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_IbmappnIsAcBufRecFormat_Type.__name__ = "Integer32"
_IbmappnIsAcBufRecFormat_Object = MibTableColumn
ibmappnIsAcBufRecFormat = _IbmappnIsAcBufRecFormat_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 4),
    _IbmappnIsAcBufRecFormat_Type()
)
ibmappnIsAcBufRecFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufRecFormat.setStatus("mandatory")
_IbmappnIsAcBufMaxRecords_Type = Integer32
_IbmappnIsAcBufMaxRecords_Object = MibTableColumn
ibmappnIsAcBufMaxRecords = _IbmappnIsAcBufMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 5),
    _IbmappnIsAcBufMaxRecords_Type()
)
ibmappnIsAcBufMaxRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufMaxRecords.setStatus("mandatory")
_IbmappnIsAcBufOldestIndex_Type = Integer32
_IbmappnIsAcBufOldestIndex_Object = MibTableColumn
ibmappnIsAcBufOldestIndex = _IbmappnIsAcBufOldestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 6),
    _IbmappnIsAcBufOldestIndex_Type()
)
ibmappnIsAcBufOldestIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBufOldestIndex.setStatus("mandatory")
_IbmappnIsAcBufNewestIndex_Type = Integer32
_IbmappnIsAcBufNewestIndex_Object = MibTableColumn
ibmappnIsAcBufNewestIndex = _IbmappnIsAcBufNewestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 7),
    _IbmappnIsAcBufNewestIndex_Type()
)
ibmappnIsAcBufNewestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufNewestIndex.setStatus("mandatory")
_IbmappnIsAcBufName_Type = DisplayString
_IbmappnIsAcBufName_Object = MibTableColumn
ibmappnIsAcBufName = _IbmappnIsAcBufName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 8),
    _IbmappnIsAcBufName_Type()
)
ibmappnIsAcBufName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufName.setStatus("mandatory")
_IbmappnIsAcTimeTable_Object = MibTable
ibmappnIsAcTimeTable = _IbmappnIsAcTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4)
)
if mibBuilder.loadTexts:
    ibmappnIsAcTimeTable.setStatus("mandatory")
_IbmappnIsAcTimeEntry_Object = MibTableRow
ibmappnIsAcTimeEntry = _IbmappnIsAcTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1)
)
ibmappnIsAcTimeEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnIsAcTimeIndex"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcTimeEntry.setStatus("mandatory")
_IbmappnIsAcTimeIndex_Type = Integer32
_IbmappnIsAcTimeIndex_Object = MibTableColumn
ibmappnIsAcTimeIndex = _IbmappnIsAcTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 1),
    _IbmappnIsAcTimeIndex_Type()
)
ibmappnIsAcTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeIndex.setStatus("mandatory")


class _IbmappnIsAcTimeEntryType_Type(Integer32):
    """Custom type ibmappnIsAcTimeEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("createdMedia", 3),
          ("endCollection", 2),
          ("managerSetTime", 6),
          ("recordFormatChanged", 7),
          ("startCollection", 1),
          ("timeChange", 5),
          ("timeReference", 8),
          ("wrappedMedia", 4))
    )


_IbmappnIsAcTimeEntryType_Type.__name__ = "Integer32"
_IbmappnIsAcTimeEntryType_Object = MibTableColumn
ibmappnIsAcTimeEntryType = _IbmappnIsAcTimeEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 2),
    _IbmappnIsAcTimeEntryType_Type()
)
ibmappnIsAcTimeEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeEntryType.setStatus("mandatory")


class _IbmappnIsAcTimeForMedia_Type(Integer32):
    """Custom type ibmappnIsAcTimeForMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("allMedias", 99),
          ("dasdMedia", 2),
          ("memoryMedia", 1))
    )


_IbmappnIsAcTimeForMedia_Type.__name__ = "Integer32"
_IbmappnIsAcTimeForMedia_Object = MibTableColumn
ibmappnIsAcTimeForMedia = _IbmappnIsAcTimeForMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 3),
    _IbmappnIsAcTimeForMedia_Type()
)
ibmappnIsAcTimeForMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeForMedia.setStatus("mandatory")
_IbmappnIsAcTimeRecTime_Type = TimeTicks
_IbmappnIsAcTimeRecTime_Object = MibTableColumn
ibmappnIsAcTimeRecTime = _IbmappnIsAcTimeRecTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 4),
    _IbmappnIsAcTimeRecTime_Type()
)
ibmappnIsAcTimeRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeRecTime.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcSecs_Type = Integer32
_IbmappnIsAcTimeAgtUtcSecs_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcSecs = _IbmappnIsAcTimeAgtUtcSecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 5),
    _IbmappnIsAcTimeAgtUtcSecs_Type()
)
ibmappnIsAcTimeAgtUtcSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcSecs.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcMins_Type = Integer32
_IbmappnIsAcTimeAgtUtcMins_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcMins = _IbmappnIsAcTimeAgtUtcMins_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 6),
    _IbmappnIsAcTimeAgtUtcMins_Type()
)
ibmappnIsAcTimeAgtUtcMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcMins.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcHours_Type = Integer32
_IbmappnIsAcTimeAgtUtcHours_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcHours = _IbmappnIsAcTimeAgtUtcHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 7),
    _IbmappnIsAcTimeAgtUtcHours_Type()
)
ibmappnIsAcTimeAgtUtcHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcHours.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcMdays_Type = Integer32
_IbmappnIsAcTimeAgtUtcMdays_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcMdays = _IbmappnIsAcTimeAgtUtcMdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 8),
    _IbmappnIsAcTimeAgtUtcMdays_Type()
)
ibmappnIsAcTimeAgtUtcMdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcMdays.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcMonths_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 12),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_IbmappnIsAcTimeAgtUtcMonths_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcMonths_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcMonths = _IbmappnIsAcTimeAgtUtcMonths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 9),
    _IbmappnIsAcTimeAgtUtcMonths_Type()
)
ibmappnIsAcTimeAgtUtcMonths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcMonths.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcYears_Type = Integer32
_IbmappnIsAcTimeAgtUtcYears_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcYears = _IbmappnIsAcTimeAgtUtcYears_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 10),
    _IbmappnIsAcTimeAgtUtcYears_Type()
)
ibmappnIsAcTimeAgtUtcYears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcYears.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcWdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcWdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_IbmappnIsAcTimeAgtUtcWdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcWdays_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcWdays = _IbmappnIsAcTimeAgtUtcWdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 11),
    _IbmappnIsAcTimeAgtUtcWdays_Type()
)
ibmappnIsAcTimeAgtUtcWdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcWdays.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcYdays_Type = Integer32
_IbmappnIsAcTimeAgtUtcYdays_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcYdays = _IbmappnIsAcTimeAgtUtcYdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 12),
    _IbmappnIsAcTimeAgtUtcYdays_Type()
)
ibmappnIsAcTimeAgtUtcYdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcYdays.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcIsdst_Type = Integer32
_IbmappnIsAcTimeAgtUtcIsdst_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcIsdst = _IbmappnIsAcTimeAgtUtcIsdst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 13),
    _IbmappnIsAcTimeAgtUtcIsdst_Type()
)
ibmappnIsAcTimeAgtUtcIsdst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcIsdst.setStatus("mandatory")


class _IbmappnIsAcTimeAgtName_Type(DisplayString):
    """Custom type ibmappnIsAcTimeAgtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcTimeAgtName_Type.__name__ = "DisplayString"
_IbmappnIsAcTimeAgtName_Object = MibTableColumn
ibmappnIsAcTimeAgtName = _IbmappnIsAcTimeAgtName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 14),
    _IbmappnIsAcTimeAgtName_Type()
)
ibmappnIsAcTimeAgtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtName.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcSecs_Type = Integer32
_IbmappnIsAcTimeMgrUtcSecs_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcSecs = _IbmappnIsAcTimeMgrUtcSecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 15),
    _IbmappnIsAcTimeMgrUtcSecs_Type()
)
ibmappnIsAcTimeMgrUtcSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcSecs.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcMins_Type = Integer32
_IbmappnIsAcTimeMgrUtcMins_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcMins = _IbmappnIsAcTimeMgrUtcMins_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 16),
    _IbmappnIsAcTimeMgrUtcMins_Type()
)
ibmappnIsAcTimeMgrUtcMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcMins.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcHours_Type = Integer32
_IbmappnIsAcTimeMgrUtcHours_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcHours = _IbmappnIsAcTimeMgrUtcHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 17),
    _IbmappnIsAcTimeMgrUtcHours_Type()
)
ibmappnIsAcTimeMgrUtcHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcHours.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcMdays_Type = Integer32
_IbmappnIsAcTimeMgrUtcMdays_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcMdays = _IbmappnIsAcTimeMgrUtcMdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 18),
    _IbmappnIsAcTimeMgrUtcMdays_Type()
)
ibmappnIsAcTimeMgrUtcMdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcMdays.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcMonths_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 12),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_IbmappnIsAcTimeMgrUtcMonths_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcMonths_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcMonths = _IbmappnIsAcTimeMgrUtcMonths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 19),
    _IbmappnIsAcTimeMgrUtcMonths_Type()
)
ibmappnIsAcTimeMgrUtcMonths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcMonths.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcYears_Type = Integer32
_IbmappnIsAcTimeMgrUtcYears_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcYears = _IbmappnIsAcTimeMgrUtcYears_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 20),
    _IbmappnIsAcTimeMgrUtcYears_Type()
)
ibmappnIsAcTimeMgrUtcYears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcYears.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcWdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcWdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_IbmappnIsAcTimeMgrUtcWdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcWdays_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcWdays = _IbmappnIsAcTimeMgrUtcWdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 21),
    _IbmappnIsAcTimeMgrUtcWdays_Type()
)
ibmappnIsAcTimeMgrUtcWdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcWdays.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcYdays_Type = Integer32
_IbmappnIsAcTimeMgrUtcYdays_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcYdays = _IbmappnIsAcTimeMgrUtcYdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 22),
    _IbmappnIsAcTimeMgrUtcYdays_Type()
)
ibmappnIsAcTimeMgrUtcYdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcYdays.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcIsdst_Type = Integer32
_IbmappnIsAcTimeMgrUtcIsdst_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcIsdst = _IbmappnIsAcTimeMgrUtcIsdst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 23),
    _IbmappnIsAcTimeMgrUtcIsdst_Type()
)
ibmappnIsAcTimeMgrUtcIsdst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcIsdst.setStatus("mandatory")


class _IbmappnIsAcTimeMgrName_Type(DisplayString):
    """Custom type ibmappnIsAcTimeMgrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IbmappnIsAcTimeMgrName_Type.__name__ = "DisplayString"
_IbmappnIsAcTimeMgrName_Object = MibTableColumn
ibmappnIsAcTimeMgrName = _IbmappnIsAcTimeMgrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 24),
    _IbmappnIsAcTimeMgrName_Type()
)
ibmappnIsAcTimeMgrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrName.setStatus("mandatory")


class _IbmappnIsAcTimeMgrTimeValid_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrTimeValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notvalid", 1),
          ("valid", 2))
    )


_IbmappnIsAcTimeMgrTimeValid_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrTimeValid_Object = MibTableColumn
ibmappnIsAcTimeMgrTimeValid = _IbmappnIsAcTimeMgrTimeValid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 25),
    _IbmappnIsAcTimeMgrTimeValid_Type()
)
ibmappnIsAcTimeMgrTimeValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrTimeValid.setStatus("mandatory")
_IbmappnIsAcDataTable_Object = MibTable
ibmappnIsAcDataTable = _IbmappnIsAcDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5)
)
if mibBuilder.loadTexts:
    ibmappnIsAcDataTable.setStatus("mandatory")
_IbmappnIsAcDataEntry_Object = MibTableRow
ibmappnIsAcDataEntry = _IbmappnIsAcDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1)
)
ibmappnIsAcDataEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmappnIsAcIndex"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcDataEntry.setStatus("mandatory")
_IbmappnIsAcIndex_Type = Integer32
_IbmappnIsAcIndex_Object = MibTableColumn
ibmappnIsAcIndex = _IbmappnIsAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 1),
    _IbmappnIsAcIndex_Type()
)
ibmappnIsAcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcIndex.setStatus("mandatory")


class _IbmappnIsAcEntryType_Type(Integer32):
    """Custom type ibmappnIsAcEntryType based on Integer32"""
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
        *(("checkpointEntry", 4),
          ("endEntry", 2),
          ("startEntry", 1),
          ("thresholdEntry", 3))
    )


_IbmappnIsAcEntryType_Type.__name__ = "Integer32"
_IbmappnIsAcEntryType_Object = MibTableColumn
ibmappnIsAcEntryType = _IbmappnIsAcEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 2),
    _IbmappnIsAcEntryType_Type()
)
ibmappnIsAcEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcEntryType.setStatus("mandatory")
_IbmappnIsAcRecTime_Type = TimeTicks
_IbmappnIsAcRecTime_Object = MibTableColumn
ibmappnIsAcRecTime = _IbmappnIsAcRecTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 3),
    _IbmappnIsAcRecTime_Type()
)
ibmappnIsAcRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcRecTime.setStatus("mandatory")


class _IbmappnIsAcFqLuName_Type(DisplayString):
    """Custom type ibmappnIsAcFqLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcFqLuName_Type.__name__ = "DisplayString"
_IbmappnIsAcFqLuName_Object = MibTableColumn
ibmappnIsAcFqLuName = _IbmappnIsAcFqLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 4),
    _IbmappnIsAcFqLuName_Type()
)
ibmappnIsAcFqLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcFqLuName.setStatus("mandatory")


class _IbmappnIsAcPcid_Type(OctetString):
    """Custom type ibmappnIsAcPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbmappnIsAcPcid_Type.__name__ = "OctetString"
_IbmappnIsAcPcid_Object = MibTableColumn
ibmappnIsAcPcid = _IbmappnIsAcPcid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 5),
    _IbmappnIsAcPcid_Type()
)
ibmappnIsAcPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcPcid.setStatus("mandatory")


class _IbmappnIsAcPriLuName_Type(DisplayString):
    """Custom type ibmappnIsAcPriLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcPriLuName_Type.__name__ = "DisplayString"
_IbmappnIsAcPriLuName_Object = MibTableColumn
ibmappnIsAcPriLuName = _IbmappnIsAcPriLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 6),
    _IbmappnIsAcPriLuName_Type()
)
ibmappnIsAcPriLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcPriLuName.setStatus("mandatory")


class _IbmappnIsAcSecLuName_Type(DisplayString):
    """Custom type ibmappnIsAcSecLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcSecLuName_Type.__name__ = "DisplayString"
_IbmappnIsAcSecLuName_Object = MibTableColumn
ibmappnIsAcSecLuName = _IbmappnIsAcSecLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 7),
    _IbmappnIsAcSecLuName_Type()
)
ibmappnIsAcSecLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSecLuName.setStatus("mandatory")


class _IbmappnIsAcModeName_Type(DisplayString):
    """Custom type ibmappnIsAcModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnIsAcModeName_Type.__name__ = "DisplayString"
_IbmappnIsAcModeName_Object = MibTableColumn
ibmappnIsAcModeName = _IbmappnIsAcModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 8),
    _IbmappnIsAcModeName_Type()
)
ibmappnIsAcModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcModeName.setStatus("mandatory")


class _IbmappnIsAcCosName_Type(DisplayString):
    """Custom type ibmappnIsAcCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnIsAcCosName_Type.__name__ = "DisplayString"
_IbmappnIsAcCosName_Object = MibTableColumn
ibmappnIsAcCosName = _IbmappnIsAcCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 9),
    _IbmappnIsAcCosName_Type()
)
ibmappnIsAcCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcCosName.setStatus("mandatory")


class _IbmappnIsAcTransPriority_Type(Integer32):
    """Custom type ibmappnIsAcTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_IbmappnIsAcTransPriority_Type.__name__ = "Integer32"
_IbmappnIsAcTransPriority_Object = MibTableColumn
ibmappnIsAcTransPriority = _IbmappnIsAcTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 10),
    _IbmappnIsAcTransPriority_Type()
)
ibmappnIsAcTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTransPriority.setStatus("mandatory")


class _IbmappnIsAcSessType_Type(Integer32):
    """Custom type ibmappnIsAcSessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lu0thru3", 2),
          ("lu62", 1))
    )


_IbmappnIsAcSessType_Type.__name__ = "Integer32"
_IbmappnIsAcSessType_Object = MibTableColumn
ibmappnIsAcSessType = _IbmappnIsAcSessType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 11),
    _IbmappnIsAcSessType_Type()
)
ibmappnIsAcSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessType.setStatus("mandatory")


class _IbmappnIsAcSessState_Type(Integer32):
    """Custom type ibmappnIsAcSessState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnIsAcSessState_Type.__name__ = "Integer32"
_IbmappnIsAcSessState_Object = MibTableColumn
ibmappnIsAcSessState = _IbmappnIsAcSessState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 12),
    _IbmappnIsAcSessState_Type()
)
ibmappnIsAcSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessState.setStatus("mandatory")
_IbmappnIsAcSessStartTime_Type = TimeTicks
_IbmappnIsAcSessStartTime_Object = MibTableColumn
ibmappnIsAcSessStartTime = _IbmappnIsAcSessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 13),
    _IbmappnIsAcSessStartTime_Type()
)
ibmappnIsAcSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessStartTime.setStatus("mandatory")
_IbmappnIsAcSessUpTime_Type = TimeTicks
_IbmappnIsAcSessUpTime_Object = MibTableColumn
ibmappnIsAcSessUpTime = _IbmappnIsAcSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 14),
    _IbmappnIsAcSessUpTime_Type()
)
ibmappnIsAcSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessUpTime.setStatus("mandatory")
_IbmappnIsAcCtrUpTime_Type = TimeTicks
_IbmappnIsAcCtrUpTime_Object = MibTableColumn
ibmappnIsAcCtrUpTime = _IbmappnIsAcCtrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 15),
    _IbmappnIsAcCtrUpTime_Type()
)
ibmappnIsAcCtrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcCtrUpTime.setStatus("mandatory")


class _IbmappnIsAcEndReason_Type(OctetString):
    """Custom type ibmappnIsAcEndReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmappnIsAcEndReason_Type.__name__ = "OctetString"
_IbmappnIsAcEndReason_Object = MibTableColumn
ibmappnIsAcEndReason = _IbmappnIsAcEndReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 16),
    _IbmappnIsAcEndReason_Type()
)
ibmappnIsAcEndReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcEndReason.setStatus("mandatory")
_IbmappnIsAcP2SFmdPius_Type = Counter32
_IbmappnIsAcP2SFmdPius_Object = MibTableColumn
ibmappnIsAcP2SFmdPius = _IbmappnIsAcP2SFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 17),
    _IbmappnIsAcP2SFmdPius_Type()
)
ibmappnIsAcP2SFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SFmdPius.setStatus("mandatory")
_IbmappnIsAcS2PFmdPius_Type = Counter32
_IbmappnIsAcS2PFmdPius_Object = MibTableColumn
ibmappnIsAcS2PFmdPius = _IbmappnIsAcS2PFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 18),
    _IbmappnIsAcS2PFmdPius_Type()
)
ibmappnIsAcS2PFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PFmdPius.setStatus("mandatory")
_IbmappnIsAcP2SNonFmdPius_Type = Counter32
_IbmappnIsAcP2SNonFmdPius_Object = MibTableColumn
ibmappnIsAcP2SNonFmdPius = _IbmappnIsAcP2SNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 19),
    _IbmappnIsAcP2SNonFmdPius_Type()
)
ibmappnIsAcP2SNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SNonFmdPius.setStatus("mandatory")
_IbmappnIsAcS2PNonFmdPius_Type = Counter32
_IbmappnIsAcS2PNonFmdPius_Object = MibTableColumn
ibmappnIsAcS2PNonFmdPius = _IbmappnIsAcS2PNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 20),
    _IbmappnIsAcS2PNonFmdPius_Type()
)
ibmappnIsAcS2PNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PNonFmdPius.setStatus("mandatory")
_IbmappnIsAcP2SFmdBytes_Type = Counter32
_IbmappnIsAcP2SFmdBytes_Object = MibTableColumn
ibmappnIsAcP2SFmdBytes = _IbmappnIsAcP2SFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 21),
    _IbmappnIsAcP2SFmdBytes_Type()
)
ibmappnIsAcP2SFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SFmdBytes.setStatus("mandatory")
_IbmappnIsAcS2PFmdBytes_Type = Counter32
_IbmappnIsAcS2PFmdBytes_Object = MibTableColumn
ibmappnIsAcS2PFmdBytes = _IbmappnIsAcS2PFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 22),
    _IbmappnIsAcS2PFmdBytes_Type()
)
ibmappnIsAcS2PFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PFmdBytes.setStatus("mandatory")
_IbmappnIsAcP2SNonFmdBytes_Type = Counter32
_IbmappnIsAcP2SNonFmdBytes_Object = MibTableColumn
ibmappnIsAcP2SNonFmdBytes = _IbmappnIsAcP2SNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 23),
    _IbmappnIsAcP2SNonFmdBytes_Type()
)
ibmappnIsAcP2SNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SNonFmdBytes.setStatus("mandatory")
_IbmappnIsAcS2PNonFmdBytes_Type = Counter32
_IbmappnIsAcS2PNonFmdBytes_Object = MibTableColumn
ibmappnIsAcS2PNonFmdBytes = _IbmappnIsAcS2PNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 24),
    _IbmappnIsAcS2PNonFmdBytes_Type()
)
ibmappnIsAcS2PNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PNonFmdBytes.setStatus("mandatory")
_IbmappnIsAcRouteInfo_Type = OctetString
_IbmappnIsAcRouteInfo_Object = MibTableColumn
ibmappnIsAcRouteInfo = _IbmappnIsAcRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 25),
    _IbmappnIsAcRouteInfo_Type()
)
ibmappnIsAcRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcRouteInfo.setStatus("mandatory")
_IbmappnConversation_ObjectIdentity = ObjectIdentity
ibmappnConversation = _IbmappnConversation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 8)
)
_IbmappnConvGeneral_ObjectIdentity = ObjectIdentity
ibmappnConvGeneral = _IbmappnConvGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 8, 1)
)
_IbmappnConvEndPoint_ObjectIdentity = ObjectIdentity
ibmappnConvEndPoint = _IbmappnConvEndPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 8, 2)
)
_Ibmrpq_ObjectIdentity = ObjectIdentity
ibmrpq = _Ibmrpq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 14)
)
_Ibmtb_ObjectIdentity = ObjectIdentity
ibmtb = _Ibmtb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15)
)
_Ibmdot1dBase_ObjectIdentity = ObjectIdentity
ibmdot1dBase = _Ibmdot1dBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1)
)


class _Ibmdot1dBaseBridgeAddress_Type(OctetString):
    """Custom type ibmdot1dBaseBridgeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ibmdot1dBaseBridgeAddress_Type.__name__ = "OctetString"
_Ibmdot1dBaseBridgeAddress_Object = MibScalar
ibmdot1dBaseBridgeAddress = _Ibmdot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 1),
    _Ibmdot1dBaseBridgeAddress_Type()
)
ibmdot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBaseBridgeAddress.setStatus("mandatory")
_Ibmdot1dBaseNumPorts_Type = Integer32
_Ibmdot1dBaseNumPorts_Object = MibScalar
ibmdot1dBaseNumPorts = _Ibmdot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 2),
    _Ibmdot1dBaseNumPorts_Type()
)
ibmdot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBaseNumPorts.setStatus("mandatory")


class _Ibmdot1dBaseType_Type(Integer32):
    """Custom type ibmdot1dBaseType based on Integer32"""
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
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_Ibmdot1dBaseType_Type.__name__ = "Integer32"
_Ibmdot1dBaseType_Object = MibScalar
ibmdot1dBaseType = _Ibmdot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 3),
    _Ibmdot1dBaseType_Type()
)
ibmdot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBaseType.setStatus("mandatory")
_Ibmdot1dBasePortTable_Object = MibTable
ibmdot1dBasePortTable = _Ibmdot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 4)
)
if mibBuilder.loadTexts:
    ibmdot1dBasePortTable.setStatus("mandatory")
_Ibmdot1dBasePortEntry_Object = MibTableRow
ibmdot1dBasePortEntry = _Ibmdot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 4, 1)
)
ibmdot1dBasePortEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdot1dBasePort"),
)
if mibBuilder.loadTexts:
    ibmdot1dBasePortEntry.setStatus("mandatory")
_Ibmdot1dBasePort_Type = Integer32
_Ibmdot1dBasePort_Object = MibTableColumn
ibmdot1dBasePort = _Ibmdot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 4, 1, 1),
    _Ibmdot1dBasePort_Type()
)
ibmdot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBasePort.setStatus("mandatory")
_Ibmdot1dBasePortIfIndex_Type = Integer32
_Ibmdot1dBasePortIfIndex_Object = MibTableColumn
ibmdot1dBasePortIfIndex = _Ibmdot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 4, 1, 2),
    _Ibmdot1dBasePortIfIndex_Type()
)
ibmdot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBasePortIfIndex.setStatus("mandatory")
_Ibmdot1dBasePortCircuit_Type = ObjectIdentifier
_Ibmdot1dBasePortCircuit_Object = MibTableColumn
ibmdot1dBasePortCircuit = _Ibmdot1dBasePortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 4, 1, 3),
    _Ibmdot1dBasePortCircuit_Type()
)
ibmdot1dBasePortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBasePortCircuit.setStatus("mandatory")
_Ibmdot1dBasePortDelayExceededDiscards_Type = Counter32
_Ibmdot1dBasePortDelayExceededDiscards_Object = MibTableColumn
ibmdot1dBasePortDelayExceededDiscards = _Ibmdot1dBasePortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 4, 1, 4),
    _Ibmdot1dBasePortDelayExceededDiscards_Type()
)
ibmdot1dBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBasePortDelayExceededDiscards.setStatus("mandatory")
_Ibmdot1dBasePortMtuExceededDiscards_Type = Counter32
_Ibmdot1dBasePortMtuExceededDiscards_Object = MibTableColumn
ibmdot1dBasePortMtuExceededDiscards = _Ibmdot1dBasePortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 1, 4, 1, 5),
    _Ibmdot1dBasePortMtuExceededDiscards_Type()
)
ibmdot1dBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dBasePortMtuExceededDiscards.setStatus("mandatory")
_Ibmdot1dStp_ObjectIdentity = ObjectIdentity
ibmdot1dStp = _Ibmdot1dStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2)
)


class _Ibmdot1dStpProtocolSpecification_Type(Integer32):
    """Custom type ibmdot1dStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_Ibmdot1dStpProtocolSpecification_Type.__name__ = "Integer32"
_Ibmdot1dStpProtocolSpecification_Object = MibScalar
ibmdot1dStpProtocolSpecification = _Ibmdot1dStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 1),
    _Ibmdot1dStpProtocolSpecification_Type()
)
ibmdot1dStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpProtocolSpecification.setStatus("mandatory")


class _Ibmdot1dStpPriority_Type(Integer32):
    """Custom type ibmdot1dStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ibmdot1dStpPriority_Type.__name__ = "Integer32"
_Ibmdot1dStpPriority_Object = MibScalar
ibmdot1dStpPriority = _Ibmdot1dStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 2),
    _Ibmdot1dStpPriority_Type()
)
ibmdot1dStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStpPriority.setStatus("mandatory")
_Ibmdot1dStpTimeSinceTopologyChange_Type = TimeTicks
_Ibmdot1dStpTimeSinceTopologyChange_Object = MibScalar
ibmdot1dStpTimeSinceTopologyChange = _Ibmdot1dStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 3),
    _Ibmdot1dStpTimeSinceTopologyChange_Type()
)
ibmdot1dStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpTimeSinceTopologyChange.setStatus("mandatory")
_Ibmdot1dStpTopChanges_Type = Counter32
_Ibmdot1dStpTopChanges_Object = MibScalar
ibmdot1dStpTopChanges = _Ibmdot1dStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 4),
    _Ibmdot1dStpTopChanges_Type()
)
ibmdot1dStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpTopChanges.setStatus("mandatory")


class _Ibmdot1dStpDesignatedRoot_Type(OctetString):
    """Custom type ibmdot1dStpDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ibmdot1dStpDesignatedRoot_Type.__name__ = "OctetString"
_Ibmdot1dStpDesignatedRoot_Object = MibScalar
ibmdot1dStpDesignatedRoot = _Ibmdot1dStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 5),
    _Ibmdot1dStpDesignatedRoot_Type()
)
ibmdot1dStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpDesignatedRoot.setStatus("mandatory")
_Ibmdot1dStpRootCost_Type = Integer32
_Ibmdot1dStpRootCost_Object = MibScalar
ibmdot1dStpRootCost = _Ibmdot1dStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 6),
    _Ibmdot1dStpRootCost_Type()
)
ibmdot1dStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpRootCost.setStatus("mandatory")
_Ibmdot1dStpRootPort_Type = Integer32
_Ibmdot1dStpRootPort_Object = MibScalar
ibmdot1dStpRootPort = _Ibmdot1dStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 7),
    _Ibmdot1dStpRootPort_Type()
)
ibmdot1dStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpRootPort.setStatus("mandatory")
_Ibmdot1dStpMaxAge_Type = Integer32
_Ibmdot1dStpMaxAge_Object = MibScalar
ibmdot1dStpMaxAge = _Ibmdot1dStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 8),
    _Ibmdot1dStpMaxAge_Type()
)
ibmdot1dStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpMaxAge.setStatus("mandatory")
_Ibmdot1dStpHelloTime_Type = Integer32
_Ibmdot1dStpHelloTime_Object = MibScalar
ibmdot1dStpHelloTime = _Ibmdot1dStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 9),
    _Ibmdot1dStpHelloTime_Type()
)
ibmdot1dStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpHelloTime.setStatus("mandatory")
_Ibmdot1dStpHoldTime_Type = Integer32
_Ibmdot1dStpHoldTime_Object = MibScalar
ibmdot1dStpHoldTime = _Ibmdot1dStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 10),
    _Ibmdot1dStpHoldTime_Type()
)
ibmdot1dStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpHoldTime.setStatus("mandatory")
_Ibmdot1dStpForwardDelay_Type = Integer32
_Ibmdot1dStpForwardDelay_Object = MibScalar
ibmdot1dStpForwardDelay = _Ibmdot1dStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 11),
    _Ibmdot1dStpForwardDelay_Type()
)
ibmdot1dStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpForwardDelay.setStatus("mandatory")
_Ibmdot1dStpBridgeMaxAge_Type = Integer32
_Ibmdot1dStpBridgeMaxAge_Object = MibScalar
ibmdot1dStpBridgeMaxAge = _Ibmdot1dStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 12),
    _Ibmdot1dStpBridgeMaxAge_Type()
)
ibmdot1dStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStpBridgeMaxAge.setStatus("mandatory")
_Ibmdot1dStpBridgeHelloTime_Type = Integer32
_Ibmdot1dStpBridgeHelloTime_Object = MibScalar
ibmdot1dStpBridgeHelloTime = _Ibmdot1dStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 13),
    _Ibmdot1dStpBridgeHelloTime_Type()
)
ibmdot1dStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStpBridgeHelloTime.setStatus("mandatory")
_Ibmdot1dStpBridgeForwardDelay_Type = Integer32
_Ibmdot1dStpBridgeForwardDelay_Object = MibScalar
ibmdot1dStpBridgeForwardDelay = _Ibmdot1dStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 14),
    _Ibmdot1dStpBridgeForwardDelay_Type()
)
ibmdot1dStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStpBridgeForwardDelay.setStatus("mandatory")
_Ibmdot1dStpPortTable_Object = MibTable
ibmdot1dStpPortTable = _Ibmdot1dStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15)
)
if mibBuilder.loadTexts:
    ibmdot1dStpPortTable.setStatus("mandatory")
_Ibmdot1dStpPortEntry_Object = MibTableRow
ibmdot1dStpPortEntry = _Ibmdot1dStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1)
)
ibmdot1dStpPortEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdot1dStpPort"),
)
if mibBuilder.loadTexts:
    ibmdot1dStpPortEntry.setStatus("mandatory")
_Ibmdot1dStpPort_Type = Integer32
_Ibmdot1dStpPort_Object = MibTableColumn
ibmdot1dStpPort = _Ibmdot1dStpPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 1),
    _Ibmdot1dStpPort_Type()
)
ibmdot1dStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpPort.setStatus("mandatory")


class _Ibmdot1dStpPortPriority_Type(Integer32):
    """Custom type ibmdot1dStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ibmdot1dStpPortPriority_Type.__name__ = "Integer32"
_Ibmdot1dStpPortPriority_Object = MibTableColumn
ibmdot1dStpPortPriority = _Ibmdot1dStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 2),
    _Ibmdot1dStpPortPriority_Type()
)
ibmdot1dStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStpPortPriority.setStatus("mandatory")


class _Ibmdot1dStpPortState_Type(Integer32):
    """Custom type ibmdot1dStpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_Ibmdot1dStpPortState_Type.__name__ = "Integer32"
_Ibmdot1dStpPortState_Object = MibTableColumn
ibmdot1dStpPortState = _Ibmdot1dStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 3),
    _Ibmdot1dStpPortState_Type()
)
ibmdot1dStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpPortState.setStatus("mandatory")


class _Ibmdot1dStpPortEnable_Type(Integer32):
    """Custom type ibmdot1dStpPortEnable based on Integer32"""
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


_Ibmdot1dStpPortEnable_Type.__name__ = "Integer32"
_Ibmdot1dStpPortEnable_Object = MibTableColumn
ibmdot1dStpPortEnable = _Ibmdot1dStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 4),
    _Ibmdot1dStpPortEnable_Type()
)
ibmdot1dStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStpPortEnable.setStatus("mandatory")


class _Ibmdot1dStpPortPathCost_Type(Integer32):
    """Custom type ibmdot1dStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ibmdot1dStpPortPathCost_Type.__name__ = "Integer32"
_Ibmdot1dStpPortPathCost_Object = MibTableColumn
ibmdot1dStpPortPathCost = _Ibmdot1dStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 5),
    _Ibmdot1dStpPortPathCost_Type()
)
ibmdot1dStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStpPortPathCost.setStatus("mandatory")


class _Ibmdot1dStpPortDesignatedRoot_Type(OctetString):
    """Custom type ibmdot1dStpPortDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ibmdot1dStpPortDesignatedRoot_Type.__name__ = "OctetString"
_Ibmdot1dStpPortDesignatedRoot_Object = MibTableColumn
ibmdot1dStpPortDesignatedRoot = _Ibmdot1dStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 6),
    _Ibmdot1dStpPortDesignatedRoot_Type()
)
ibmdot1dStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpPortDesignatedRoot.setStatus("mandatory")
_Ibmdot1dStpPortDesignatedCost_Type = Integer32
_Ibmdot1dStpPortDesignatedCost_Object = MibTableColumn
ibmdot1dStpPortDesignatedCost = _Ibmdot1dStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 7),
    _Ibmdot1dStpPortDesignatedCost_Type()
)
ibmdot1dStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpPortDesignatedCost.setStatus("mandatory")


class _Ibmdot1dStpPortDesignatedBridge_Type(OctetString):
    """Custom type ibmdot1dStpPortDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ibmdot1dStpPortDesignatedBridge_Type.__name__ = "OctetString"
_Ibmdot1dStpPortDesignatedBridge_Object = MibTableColumn
ibmdot1dStpPortDesignatedBridge = _Ibmdot1dStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 8),
    _Ibmdot1dStpPortDesignatedBridge_Type()
)
ibmdot1dStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpPortDesignatedBridge.setStatus("mandatory")


class _Ibmdot1dStpPortDesignatedPort_Type(OctetString):
    """Custom type ibmdot1dStpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Ibmdot1dStpPortDesignatedPort_Type.__name__ = "OctetString"
_Ibmdot1dStpPortDesignatedPort_Object = MibTableColumn
ibmdot1dStpPortDesignatedPort = _Ibmdot1dStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 9),
    _Ibmdot1dStpPortDesignatedPort_Type()
)
ibmdot1dStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpPortDesignatedPort.setStatus("mandatory")
_Ibmdot1dStpPortForwardTransitions_Type = Counter32
_Ibmdot1dStpPortForwardTransitions_Object = MibTableColumn
ibmdot1dStpPortForwardTransitions = _Ibmdot1dStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 2, 15, 1, 10),
    _Ibmdot1dStpPortForwardTransitions_Type()
)
ibmdot1dStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dStpPortForwardTransitions.setStatus("mandatory")
_Ibmdot1dTp_ObjectIdentity = ObjectIdentity
ibmdot1dTp = _Ibmdot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3)
)
_Ibmdot1dTpLearnedEntryDiscards_Type = Counter32
_Ibmdot1dTpLearnedEntryDiscards_Object = MibScalar
ibmdot1dTpLearnedEntryDiscards = _Ibmdot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 1),
    _Ibmdot1dTpLearnedEntryDiscards_Type()
)
ibmdot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpLearnedEntryDiscards.setStatus("mandatory")
_Ibmdot1dTpAgingTime_Type = Integer32
_Ibmdot1dTpAgingTime_Object = MibScalar
ibmdot1dTpAgingTime = _Ibmdot1dTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 2),
    _Ibmdot1dTpAgingTime_Type()
)
ibmdot1dTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dTpAgingTime.setStatus("mandatory")
_Ibmdot1dTpFdbTable_Object = MibTable
ibmdot1dTpFdbTable = _Ibmdot1dTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 3)
)
if mibBuilder.loadTexts:
    ibmdot1dTpFdbTable.setStatus("mandatory")
_Ibmdot1dTpFdbEntry_Object = MibTableRow
ibmdot1dTpFdbEntry = _Ibmdot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 3, 1)
)
ibmdot1dTpFdbEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    ibmdot1dTpFdbEntry.setStatus("mandatory")


class _Ibmdot1dTpFdbAddress_Type(OctetString):
    """Custom type ibmdot1dTpFdbAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ibmdot1dTpFdbAddress_Type.__name__ = "OctetString"
_Ibmdot1dTpFdbAddress_Object = MibTableColumn
ibmdot1dTpFdbAddress = _Ibmdot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 3, 1, 1),
    _Ibmdot1dTpFdbAddress_Type()
)
ibmdot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpFdbAddress.setStatus("mandatory")
_Ibmdot1dTpFdbPort_Type = Integer32
_Ibmdot1dTpFdbPort_Object = MibTableColumn
ibmdot1dTpFdbPort = _Ibmdot1dTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 3, 1, 2),
    _Ibmdot1dTpFdbPort_Type()
)
ibmdot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpFdbPort.setStatus("mandatory")


class _Ibmdot1dTpFdbStatus_Type(Integer32):
    """Custom type ibmdot1dTpFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_Ibmdot1dTpFdbStatus_Type.__name__ = "Integer32"
_Ibmdot1dTpFdbStatus_Object = MibTableColumn
ibmdot1dTpFdbStatus = _Ibmdot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 3, 1, 3),
    _Ibmdot1dTpFdbStatus_Type()
)
ibmdot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpFdbStatus.setStatus("mandatory")
_Ibmdot1dTpPortTable_Object = MibTable
ibmdot1dTpPortTable = _Ibmdot1dTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 4)
)
if mibBuilder.loadTexts:
    ibmdot1dTpPortTable.setStatus("mandatory")
_Ibmdot1dTpPortEntry_Object = MibTableRow
ibmdot1dTpPortEntry = _Ibmdot1dTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 4, 1)
)
ibmdot1dTpPortEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdot1dTpPort"),
)
if mibBuilder.loadTexts:
    ibmdot1dTpPortEntry.setStatus("mandatory")
_Ibmdot1dTpPort_Type = Integer32
_Ibmdot1dTpPort_Object = MibTableColumn
ibmdot1dTpPort = _Ibmdot1dTpPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 4, 1, 1),
    _Ibmdot1dTpPort_Type()
)
ibmdot1dTpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpPort.setStatus("mandatory")
_Ibmdot1dTpPortMaxInfo_Type = Integer32
_Ibmdot1dTpPortMaxInfo_Object = MibTableColumn
ibmdot1dTpPortMaxInfo = _Ibmdot1dTpPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 4, 1, 2),
    _Ibmdot1dTpPortMaxInfo_Type()
)
ibmdot1dTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpPortMaxInfo.setStatus("mandatory")
_Ibmdot1dTpPortInFrames_Type = Counter32
_Ibmdot1dTpPortInFrames_Object = MibTableColumn
ibmdot1dTpPortInFrames = _Ibmdot1dTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 4, 1, 3),
    _Ibmdot1dTpPortInFrames_Type()
)
ibmdot1dTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpPortInFrames.setStatus("mandatory")
_Ibmdot1dTpPortOutFrames_Type = Counter32
_Ibmdot1dTpPortOutFrames_Object = MibTableColumn
ibmdot1dTpPortOutFrames = _Ibmdot1dTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 4, 1, 4),
    _Ibmdot1dTpPortOutFrames_Type()
)
ibmdot1dTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpPortOutFrames.setStatus("mandatory")
_Ibmdot1dTpPortInDiscards_Type = Counter32
_Ibmdot1dTpPortInDiscards_Object = MibTableColumn
ibmdot1dTpPortInDiscards = _Ibmdot1dTpPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 3, 4, 1, 5),
    _Ibmdot1dTpPortInDiscards_Type()
)
ibmdot1dTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdot1dTpPortInDiscards.setStatus("mandatory")
_Ibmdot1dStatic_ObjectIdentity = ObjectIdentity
ibmdot1dStatic = _Ibmdot1dStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 4)
)
_Ibmdot1dStaticTable_Object = MibTable
ibmdot1dStaticTable = _Ibmdot1dStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 4, 1)
)
if mibBuilder.loadTexts:
    ibmdot1dStaticTable.setStatus("mandatory")
_Ibmdot1dStaticEntry_Object = MibTableRow
ibmdot1dStaticEntry = _Ibmdot1dStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 4, 1, 1)
)
ibmdot1dStaticEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdot1dStaticAddress"),
    (0, "IBM6611-MIB", "ibmdot1dStaticReceivePort"),
)
if mibBuilder.loadTexts:
    ibmdot1dStaticEntry.setStatus("mandatory")


class _Ibmdot1dStaticAddress_Type(OctetString):
    """Custom type ibmdot1dStaticAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ibmdot1dStaticAddress_Type.__name__ = "OctetString"
_Ibmdot1dStaticAddress_Object = MibTableColumn
ibmdot1dStaticAddress = _Ibmdot1dStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 4, 1, 1, 1),
    _Ibmdot1dStaticAddress_Type()
)
ibmdot1dStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStaticAddress.setStatus("mandatory")
_Ibmdot1dStaticReceivePort_Type = Integer32
_Ibmdot1dStaticReceivePort_Object = MibTableColumn
ibmdot1dStaticReceivePort = _Ibmdot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 4, 1, 1, 2),
    _Ibmdot1dStaticReceivePort_Type()
)
ibmdot1dStaticReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStaticReceivePort.setStatus("mandatory")
_Ibmdot1dStaticAllowedToGoTo_Type = OctetString
_Ibmdot1dStaticAllowedToGoTo_Object = MibTableColumn
ibmdot1dStaticAllowedToGoTo = _Ibmdot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 4, 1, 1, 3),
    _Ibmdot1dStaticAllowedToGoTo_Type()
)
ibmdot1dStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStaticAllowedToGoTo.setStatus("mandatory")


class _Ibmdot1dStaticStatus_Type(Integer32):
    """Custom type ibmdot1dStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Ibmdot1dStaticStatus_Type.__name__ = "Integer32"
_Ibmdot1dStaticStatus_Object = MibTableColumn
ibmdot1dStaticStatus = _Ibmdot1dStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 4, 1, 1, 4),
    _Ibmdot1dStaticStatus_Type()
)
ibmdot1dStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmdot1dStaticStatus.setStatus("mandatory")
_IbmtbMACAddressFilters_ObjectIdentity = ObjectIdentity
ibmtbMACAddressFilters = _IbmtbMACAddressFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5)
)
_IbmtbmacFiltInfoTable_Object = MibTable
ibmtbmacFiltInfoTable = _IbmtbmacFiltInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 1)
)
if mibBuilder.loadTexts:
    ibmtbmacFiltInfoTable.setStatus("mandatory")
_IbmtbmacFiltInfoEntry_Object = MibTableRow
ibmtbmacFiltInfoEntry = _IbmtbmacFiltInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 1, 1)
)
ibmtbmacFiltInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbmacFiltIfIndex"),
)
if mibBuilder.loadTexts:
    ibmtbmacFiltInfoEntry.setStatus("mandatory")
_IbmtbmacFiltIfIndex_Type = Integer32
_IbmtbmacFiltIfIndex_Object = MibTableColumn
ibmtbmacFiltIfIndex = _IbmtbmacFiltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 1, 1, 1),
    _IbmtbmacFiltIfIndex_Type()
)
ibmtbmacFiltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltIfIndex.setStatus("mandatory")


class _IbmtbmacFiltInFilterType_Type(Integer32):
    """Custom type ibmtbmacFiltInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmtbmacFiltInFilterType_Type.__name__ = "Integer32"
_IbmtbmacFiltInFilterType_Object = MibTableColumn
ibmtbmacFiltInFilterType = _IbmtbmacFiltInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 1, 1, 2),
    _IbmtbmacFiltInFilterType_Type()
)
ibmtbmacFiltInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltInFilterType.setStatus("mandatory")


class _IbmtbmacFiltOutFilterType_Type(Integer32):
    """Custom type ibmtbmacFiltOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmtbmacFiltOutFilterType_Type.__name__ = "Integer32"
_IbmtbmacFiltOutFilterType_Object = MibTableColumn
ibmtbmacFiltOutFilterType = _IbmtbmacFiltOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 1, 1, 3),
    _IbmtbmacFiltOutFilterType_Type()
)
ibmtbmacFiltOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltOutFilterType.setStatus("mandatory")
_IbmtbmacFiltInNotForwarded_Type = Counter32
_IbmtbmacFiltInNotForwarded_Object = MibTableColumn
ibmtbmacFiltInNotForwarded = _IbmtbmacFiltInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 1, 1, 4),
    _IbmtbmacFiltInNotForwarded_Type()
)
ibmtbmacFiltInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltInNotForwarded.setStatus("mandatory")
_IbmtbmacFiltOutNotForwarded_Type = Counter32
_IbmtbmacFiltOutNotForwarded_Object = MibTableColumn
ibmtbmacFiltOutNotForwarded = _IbmtbmacFiltOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 1, 1, 5),
    _IbmtbmacFiltOutNotForwarded_Type()
)
ibmtbmacFiltOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltOutNotForwarded.setStatus("mandatory")
_IbmtbmacFiltInTable_Object = MibTable
ibmtbmacFiltInTable = _IbmtbmacFiltInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 2)
)
if mibBuilder.loadTexts:
    ibmtbmacFiltInTable.setStatus("mandatory")
_IbmtbmacFiltInEntry_Object = MibTableRow
ibmtbmacFiltInEntry = _IbmtbmacFiltInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 2, 1)
)
ibmtbmacFiltInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbmacFiltInIfIndex"),
    (0, "IBM6611-MIB", "ibmtbmacFiltInSrcAddress"),
    (0, "IBM6611-MIB", "ibmtbmacFiltInDestAddress"),
)
if mibBuilder.loadTexts:
    ibmtbmacFiltInEntry.setStatus("mandatory")
_IbmtbmacFiltInIfIndex_Type = Integer32
_IbmtbmacFiltInIfIndex_Object = MibTableColumn
ibmtbmacFiltInIfIndex = _IbmtbmacFiltInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 2, 1, 1),
    _IbmtbmacFiltInIfIndex_Type()
)
ibmtbmacFiltInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltInIfIndex.setStatus("mandatory")


class _IbmtbmacFiltInSrcAddress_Type(OctetString):
    """Custom type ibmtbmacFiltInSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltInSrcAddress_Type.__name__ = "OctetString"
_IbmtbmacFiltInSrcAddress_Object = MibTableColumn
ibmtbmacFiltInSrcAddress = _IbmtbmacFiltInSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 2, 1, 2),
    _IbmtbmacFiltInSrcAddress_Type()
)
ibmtbmacFiltInSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltInSrcAddress.setStatus("mandatory")


class _IbmtbmacFiltInSrcMask_Type(OctetString):
    """Custom type ibmtbmacFiltInSrcMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltInSrcMask_Type.__name__ = "OctetString"
_IbmtbmacFiltInSrcMask_Object = MibTableColumn
ibmtbmacFiltInSrcMask = _IbmtbmacFiltInSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 2, 1, 3),
    _IbmtbmacFiltInSrcMask_Type()
)
ibmtbmacFiltInSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltInSrcMask.setStatus("mandatory")


class _IbmtbmacFiltInDestAddress_Type(OctetString):
    """Custom type ibmtbmacFiltInDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltInDestAddress_Type.__name__ = "OctetString"
_IbmtbmacFiltInDestAddress_Object = MibTableColumn
ibmtbmacFiltInDestAddress = _IbmtbmacFiltInDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 2, 1, 4),
    _IbmtbmacFiltInDestAddress_Type()
)
ibmtbmacFiltInDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltInDestAddress.setStatus("mandatory")


class _IbmtbmacFiltInDestMask_Type(OctetString):
    """Custom type ibmtbmacFiltInDestMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltInDestMask_Type.__name__ = "OctetString"
_IbmtbmacFiltInDestMask_Object = MibTableColumn
ibmtbmacFiltInDestMask = _IbmtbmacFiltInDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 2, 1, 5),
    _IbmtbmacFiltInDestMask_Type()
)
ibmtbmacFiltInDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltInDestMask.setStatus("mandatory")
_IbmtbmacFiltOutTable_Object = MibTable
ibmtbmacFiltOutTable = _IbmtbmacFiltOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 3)
)
if mibBuilder.loadTexts:
    ibmtbmacFiltOutTable.setStatus("mandatory")
_IbmtbmacFiltOutEntry_Object = MibTableRow
ibmtbmacFiltOutEntry = _IbmtbmacFiltOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 3, 1)
)
ibmtbmacFiltOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbmacFiltOutIfIndex"),
    (0, "IBM6611-MIB", "ibmtbmacFiltOutSrcAddress"),
    (0, "IBM6611-MIB", "ibmtbmacFiltOutDestAddress"),
)
if mibBuilder.loadTexts:
    ibmtbmacFiltOutEntry.setStatus("mandatory")
_IbmtbmacFiltOutIfIndex_Type = Integer32
_IbmtbmacFiltOutIfIndex_Object = MibTableColumn
ibmtbmacFiltOutIfIndex = _IbmtbmacFiltOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 3, 1, 1),
    _IbmtbmacFiltOutIfIndex_Type()
)
ibmtbmacFiltOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltOutIfIndex.setStatus("mandatory")


class _IbmtbmacFiltOutSrcAddress_Type(OctetString):
    """Custom type ibmtbmacFiltOutSrcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltOutSrcAddress_Type.__name__ = "OctetString"
_IbmtbmacFiltOutSrcAddress_Object = MibTableColumn
ibmtbmacFiltOutSrcAddress = _IbmtbmacFiltOutSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 3, 1, 2),
    _IbmtbmacFiltOutSrcAddress_Type()
)
ibmtbmacFiltOutSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltOutSrcAddress.setStatus("mandatory")


class _IbmtbmacFiltOutSrcMask_Type(OctetString):
    """Custom type ibmtbmacFiltOutSrcMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltOutSrcMask_Type.__name__ = "OctetString"
_IbmtbmacFiltOutSrcMask_Object = MibTableColumn
ibmtbmacFiltOutSrcMask = _IbmtbmacFiltOutSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 3, 1, 3),
    _IbmtbmacFiltOutSrcMask_Type()
)
ibmtbmacFiltOutSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltOutSrcMask.setStatus("mandatory")


class _IbmtbmacFiltOutDestAddress_Type(OctetString):
    """Custom type ibmtbmacFiltOutDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltOutDestAddress_Type.__name__ = "OctetString"
_IbmtbmacFiltOutDestAddress_Object = MibTableColumn
ibmtbmacFiltOutDestAddress = _IbmtbmacFiltOutDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 3, 1, 4),
    _IbmtbmacFiltOutDestAddress_Type()
)
ibmtbmacFiltOutDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltOutDestAddress.setStatus("mandatory")


class _IbmtbmacFiltOutDestMask_Type(OctetString):
    """Custom type ibmtbmacFiltOutDestMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmtbmacFiltOutDestMask_Type.__name__ = "OctetString"
_IbmtbmacFiltOutDestMask_Object = MibTableColumn
ibmtbmacFiltOutDestMask = _IbmtbmacFiltOutDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 5, 3, 1, 5),
    _IbmtbmacFiltOutDestMask_Type()
)
ibmtbmacFiltOutDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbmacFiltOutDestMask.setStatus("mandatory")
_IbmtbSAPFilters_ObjectIdentity = ObjectIdentity
ibmtbSAPFilters = _IbmtbSAPFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6)
)
_IbmtbsapFiltInfoTable_Object = MibTable
ibmtbsapFiltInfoTable = _IbmtbsapFiltInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6, 1)
)
if mibBuilder.loadTexts:
    ibmtbsapFiltInfoTable.setStatus("mandatory")
_IbmtbsapFiltInfoEntry_Object = MibTableRow
ibmtbsapFiltInfoEntry = _IbmtbsapFiltInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6, 1, 1)
)
ibmtbsapFiltInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbsapFiltIfIndex"),
)
if mibBuilder.loadTexts:
    ibmtbsapFiltInfoEntry.setStatus("mandatory")
_IbmtbsapFiltIfIndex_Type = Integer32
_IbmtbsapFiltIfIndex_Object = MibTableColumn
ibmtbsapFiltIfIndex = _IbmtbsapFiltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6, 1, 1, 1),
    _IbmtbsapFiltIfIndex_Type()
)
ibmtbsapFiltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbsapFiltIfIndex.setStatus("mandatory")


class _IbmtbsapFiltIn_Type(OctetString):
    """Custom type ibmtbsapFiltIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbmtbsapFiltIn_Type.__name__ = "OctetString"
_IbmtbsapFiltIn_Object = MibTableColumn
ibmtbsapFiltIn = _IbmtbsapFiltIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6, 1, 1, 2),
    _IbmtbsapFiltIn_Type()
)
ibmtbsapFiltIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbsapFiltIn.setStatus("mandatory")


class _IbmtbsapFiltOut_Type(OctetString):
    """Custom type ibmtbsapFiltOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbmtbsapFiltOut_Type.__name__ = "OctetString"
_IbmtbsapFiltOut_Object = MibTableColumn
ibmtbsapFiltOut = _IbmtbsapFiltOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6, 1, 1, 3),
    _IbmtbsapFiltOut_Type()
)
ibmtbsapFiltOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbsapFiltOut.setStatus("mandatory")
_IbmtbsapFiltInNotForwarded_Type = Counter32
_IbmtbsapFiltInNotForwarded_Object = MibTableColumn
ibmtbsapFiltInNotForwarded = _IbmtbsapFiltInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6, 1, 1, 4),
    _IbmtbsapFiltInNotForwarded_Type()
)
ibmtbsapFiltInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbsapFiltInNotForwarded.setStatus("mandatory")
_IbmtbsapFiltOutNotForwarded_Type = Counter32
_IbmtbsapFiltOutNotForwarded_Object = MibTableColumn
ibmtbsapFiltOutNotForwarded = _IbmtbsapFiltOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 6, 1, 1, 5),
    _IbmtbsapFiltOutNotForwarded_Type()
)
ibmtbsapFiltOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbsapFiltOutNotForwarded.setStatus("mandatory")
_IbmtbEthTypeFilters_ObjectIdentity = ObjectIdentity
ibmtbEthTypeFilters = _IbmtbEthTypeFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7)
)
_IbmtbEthTypeFiltInfoTable_Object = MibTable
ibmtbEthTypeFiltInfoTable = _IbmtbEthTypeFiltInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 1)
)
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInfoTable.setStatus("mandatory")
_IbmtbEthTypeFiltInfoEntry_Object = MibTableRow
ibmtbEthTypeFiltInfoEntry = _IbmtbEthTypeFiltInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 1, 1)
)
ibmtbEthTypeFiltInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbEthTypeFiltIfIndex"),
)
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInfoEntry.setStatus("mandatory")
_IbmtbEthTypeFiltIfIndex_Type = Integer32
_IbmtbEthTypeFiltIfIndex_Object = MibTableColumn
ibmtbEthTypeFiltIfIndex = _IbmtbEthTypeFiltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 1, 1, 1),
    _IbmtbEthTypeFiltIfIndex_Type()
)
ibmtbEthTypeFiltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltIfIndex.setStatus("mandatory")


class _IbmtbEthTypeFiltInFilterType_Type(Integer32):
    """Custom type ibmtbEthTypeFiltInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmtbEthTypeFiltInFilterType_Type.__name__ = "Integer32"
_IbmtbEthTypeFiltInFilterType_Object = MibTableColumn
ibmtbEthTypeFiltInFilterType = _IbmtbEthTypeFiltInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 1, 1, 2),
    _IbmtbEthTypeFiltInFilterType_Type()
)
ibmtbEthTypeFiltInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInFilterType.setStatus("mandatory")


class _IbmtbEthTypeFiltOutFilterType_Type(Integer32):
    """Custom type ibmtbEthTypeFiltOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmtbEthTypeFiltOutFilterType_Type.__name__ = "Integer32"
_IbmtbEthTypeFiltOutFilterType_Object = MibTableColumn
ibmtbEthTypeFiltOutFilterType = _IbmtbEthTypeFiltOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 1, 1, 3),
    _IbmtbEthTypeFiltOutFilterType_Type()
)
ibmtbEthTypeFiltOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltOutFilterType.setStatus("mandatory")
_IbmtbEthTypeFiltInNotForwarded_Type = Counter32
_IbmtbEthTypeFiltInNotForwarded_Object = MibTableColumn
ibmtbEthTypeFiltInNotForwarded = _IbmtbEthTypeFiltInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 1, 1, 4),
    _IbmtbEthTypeFiltInNotForwarded_Type()
)
ibmtbEthTypeFiltInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInNotForwarded.setStatus("mandatory")
_IbmtbEthTypeFiltOutNotForwarded_Type = Counter32
_IbmtbEthTypeFiltOutNotForwarded_Object = MibTableColumn
ibmtbEthTypeFiltOutNotForwarded = _IbmtbEthTypeFiltOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 1, 1, 5),
    _IbmtbEthTypeFiltOutNotForwarded_Type()
)
ibmtbEthTypeFiltOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltOutNotForwarded.setStatus("mandatory")
_IbmtbEthTypeFiltInTable_Object = MibTable
ibmtbEthTypeFiltInTable = _IbmtbEthTypeFiltInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 2)
)
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInTable.setStatus("mandatory")
_IbmtbEthTypeFiltInEntry_Object = MibTableRow
ibmtbEthTypeFiltInEntry = _IbmtbEthTypeFiltInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 2, 1)
)
ibmtbEthTypeFiltInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbEthTypeFiltInIfIndex"),
    (0, "IBM6611-MIB", "ibmtbEthTypeFiltInValue"),
)
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInEntry.setStatus("mandatory")
_IbmtbEthTypeFiltInIfIndex_Type = Integer32
_IbmtbEthTypeFiltInIfIndex_Object = MibTableColumn
ibmtbEthTypeFiltInIfIndex = _IbmtbEthTypeFiltInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 2, 1, 1),
    _IbmtbEthTypeFiltInIfIndex_Type()
)
ibmtbEthTypeFiltInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInIfIndex.setStatus("mandatory")


class _IbmtbEthTypeFiltInValue_Type(OctetString):
    """Custom type ibmtbEthTypeFiltInValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmtbEthTypeFiltInValue_Type.__name__ = "OctetString"
_IbmtbEthTypeFiltInValue_Object = MibTableColumn
ibmtbEthTypeFiltInValue = _IbmtbEthTypeFiltInValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 2, 1, 2),
    _IbmtbEthTypeFiltInValue_Type()
)
ibmtbEthTypeFiltInValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInValue.setStatus("mandatory")


class _IbmtbEthTypeFiltInMask_Type(OctetString):
    """Custom type ibmtbEthTypeFiltInMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmtbEthTypeFiltInMask_Type.__name__ = "OctetString"
_IbmtbEthTypeFiltInMask_Object = MibTableColumn
ibmtbEthTypeFiltInMask = _IbmtbEthTypeFiltInMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 2, 1, 3),
    _IbmtbEthTypeFiltInMask_Type()
)
ibmtbEthTypeFiltInMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltInMask.setStatus("mandatory")
_IbmtbEthTypeFiltOutTable_Object = MibTable
ibmtbEthTypeFiltOutTable = _IbmtbEthTypeFiltOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 3)
)
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltOutTable.setStatus("mandatory")
_IbmtbEthTypeFiltOutEntry_Object = MibTableRow
ibmtbEthTypeFiltOutEntry = _IbmtbEthTypeFiltOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 3, 1)
)
ibmtbEthTypeFiltOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbEthTypeFiltOutIfIndex"),
    (0, "IBM6611-MIB", "ibmtbEthTypeFiltOutValue"),
)
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltOutEntry.setStatus("mandatory")
_IbmtbEthTypeFiltOutIfIndex_Type = Integer32
_IbmtbEthTypeFiltOutIfIndex_Object = MibTableColumn
ibmtbEthTypeFiltOutIfIndex = _IbmtbEthTypeFiltOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 3, 1, 1),
    _IbmtbEthTypeFiltOutIfIndex_Type()
)
ibmtbEthTypeFiltOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltOutIfIndex.setStatus("mandatory")


class _IbmtbEthTypeFiltOutValue_Type(OctetString):
    """Custom type ibmtbEthTypeFiltOutValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmtbEthTypeFiltOutValue_Type.__name__ = "OctetString"
_IbmtbEthTypeFiltOutValue_Object = MibTableColumn
ibmtbEthTypeFiltOutValue = _IbmtbEthTypeFiltOutValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 3, 1, 2),
    _IbmtbEthTypeFiltOutValue_Type()
)
ibmtbEthTypeFiltOutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltOutValue.setStatus("mandatory")


class _IbmtbEthTypeFiltOutMask_Type(OctetString):
    """Custom type ibmtbEthTypeFiltOutMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmtbEthTypeFiltOutMask_Type.__name__ = "OctetString"
_IbmtbEthTypeFiltOutMask_Object = MibTableColumn
ibmtbEthTypeFiltOutMask = _IbmtbEthTypeFiltOutMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 7, 3, 1, 3),
    _IbmtbEthTypeFiltOutMask_Type()
)
ibmtbEthTypeFiltOutMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbEthTypeFiltOutMask.setStatus("mandatory")
_IbmtbWindowFilters_ObjectIdentity = ObjectIdentity
ibmtbWindowFilters = _IbmtbWindowFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8)
)
_IbmtbwinFiltInfoTable_Object = MibTable
ibmtbwinFiltInfoTable = _IbmtbwinFiltInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 1)
)
if mibBuilder.loadTexts:
    ibmtbwinFiltInfoTable.setStatus("mandatory")
_IbmtbwinFiltInfoEntry_Object = MibTableRow
ibmtbwinFiltInfoEntry = _IbmtbwinFiltInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 1, 1)
)
ibmtbwinFiltInfoEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbwinFiltIfIndex"),
)
if mibBuilder.loadTexts:
    ibmtbwinFiltInfoEntry.setStatus("mandatory")
_IbmtbwinFiltIfIndex_Type = Integer32
_IbmtbwinFiltIfIndex_Object = MibTableColumn
ibmtbwinFiltIfIndex = _IbmtbwinFiltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 1, 1, 1),
    _IbmtbwinFiltIfIndex_Type()
)
ibmtbwinFiltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltIfIndex.setStatus("mandatory")


class _IbmtbwinFiltInFilterType_Type(Integer32):
    """Custom type ibmtbwinFiltInFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmtbwinFiltInFilterType_Type.__name__ = "Integer32"
_IbmtbwinFiltInFilterType_Object = MibTableColumn
ibmtbwinFiltInFilterType = _IbmtbwinFiltInFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 1, 1, 2),
    _IbmtbwinFiltInFilterType_Type()
)
ibmtbwinFiltInFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInFilterType.setStatus("mandatory")


class _IbmtbwinFiltOutFilterType_Type(Integer32):
    """Custom type ibmtbwinFiltOutFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_IbmtbwinFiltOutFilterType_Type.__name__ = "Integer32"
_IbmtbwinFiltOutFilterType_Object = MibTableColumn
ibmtbwinFiltOutFilterType = _IbmtbwinFiltOutFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 1, 1, 3),
    _IbmtbwinFiltOutFilterType_Type()
)
ibmtbwinFiltOutFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutFilterType.setStatus("mandatory")
_IbmtbwinFiltInNotForwarded_Type = Counter32
_IbmtbwinFiltInNotForwarded_Object = MibTableColumn
ibmtbwinFiltInNotForwarded = _IbmtbwinFiltInNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 1, 1, 4),
    _IbmtbwinFiltInNotForwarded_Type()
)
ibmtbwinFiltInNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInNotForwarded.setStatus("mandatory")
_IbmtbwinFiltOutNotForwarded_Type = Counter32
_IbmtbwinFiltOutNotForwarded_Object = MibTableColumn
ibmtbwinFiltOutNotForwarded = _IbmtbwinFiltOutNotForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 1, 1, 5),
    _IbmtbwinFiltOutNotForwarded_Type()
)
ibmtbwinFiltOutNotForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutNotForwarded.setStatus("mandatory")
_IbmtbwinFiltInTable_Object = MibTable
ibmtbwinFiltInTable = _IbmtbwinFiltInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2)
)
if mibBuilder.loadTexts:
    ibmtbwinFiltInTable.setStatus("mandatory")
_IbmtbwinFiltInEntry_Object = MibTableRow
ibmtbwinFiltInEntry = _IbmtbwinFiltInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1)
)
ibmtbwinFiltInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbwinFiltInIfIndex"),
    (0, "IBM6611-MIB", "ibmtbwinFiltInId"),
    (0, "IBM6611-MIB", "ibmtbwinFiltInContents"),
)
if mibBuilder.loadTexts:
    ibmtbwinFiltInEntry.setStatus("mandatory")
_IbmtbwinFiltInIfIndex_Type = Integer32
_IbmtbwinFiltInIfIndex_Object = MibTableColumn
ibmtbwinFiltInIfIndex = _IbmtbwinFiltInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1, 1),
    _IbmtbwinFiltInIfIndex_Type()
)
ibmtbwinFiltInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInIfIndex.setStatus("mandatory")
_IbmtbwinFiltInContents_Type = OctetString
_IbmtbwinFiltInContents_Object = MibTableColumn
ibmtbwinFiltInContents = _IbmtbwinFiltInContents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1, 2),
    _IbmtbwinFiltInContents_Type()
)
ibmtbwinFiltInContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInContents.setStatus("mandatory")
_IbmtbwinFiltInMaskString_Type = OctetString
_IbmtbwinFiltInMaskString_Object = MibTableColumn
ibmtbwinFiltInMaskString = _IbmtbwinFiltInMaskString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1, 3),
    _IbmtbwinFiltInMaskString_Type()
)
ibmtbwinFiltInMaskString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInMaskString.setStatus("mandatory")
_IbmtbwinFiltInOffsetStart_Type = DisplayString
_IbmtbwinFiltInOffsetStart_Object = MibTableColumn
ibmtbwinFiltInOffsetStart = _IbmtbwinFiltInOffsetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1, 4),
    _IbmtbwinFiltInOffsetStart_Type()
)
ibmtbwinFiltInOffsetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInOffsetStart.setStatus("mandatory")


class _IbmtbwinFiltInNumBytes_Type(OctetString):
    """Custom type ibmtbwinFiltInNumBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmtbwinFiltInNumBytes_Type.__name__ = "OctetString"
_IbmtbwinFiltInNumBytes_Object = MibTableColumn
ibmtbwinFiltInNumBytes = _IbmtbwinFiltInNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1, 5),
    _IbmtbwinFiltInNumBytes_Type()
)
ibmtbwinFiltInNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInNumBytes.setStatus("mandatory")


class _IbmtbwinFiltInOffset_Type(OctetString):
    """Custom type ibmtbwinFiltInOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmtbwinFiltInOffset_Type.__name__ = "OctetString"
_IbmtbwinFiltInOffset_Object = MibTableColumn
ibmtbwinFiltInOffset = _IbmtbwinFiltInOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1, 6),
    _IbmtbwinFiltInOffset_Type()
)
ibmtbwinFiltInOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInOffset.setStatus("mandatory")
_IbmtbwinFiltInId_Type = Integer32
_IbmtbwinFiltInId_Object = MibTableColumn
ibmtbwinFiltInId = _IbmtbwinFiltInId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 2, 1, 7),
    _IbmtbwinFiltInId_Type()
)
ibmtbwinFiltInId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltInId.setStatus("mandatory")
_IbmtbwinFiltOutTable_Object = MibTable
ibmtbwinFiltOutTable = _IbmtbwinFiltOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3)
)
if mibBuilder.loadTexts:
    ibmtbwinFiltOutTable.setStatus("mandatory")
_IbmtbwinFiltOutEntry_Object = MibTableRow
ibmtbwinFiltOutEntry = _IbmtbwinFiltOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1)
)
ibmtbwinFiltOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbwinFiltOutIfIndex"),
    (0, "IBM6611-MIB", "ibmtbwinFiltOutId"),
    (0, "IBM6611-MIB", "ibmtbwinFiltOutContents"),
)
if mibBuilder.loadTexts:
    ibmtbwinFiltOutEntry.setStatus("mandatory")
_IbmtbwinFiltOutIfIndex_Type = Integer32
_IbmtbwinFiltOutIfIndex_Object = MibTableColumn
ibmtbwinFiltOutIfIndex = _IbmtbwinFiltOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1, 1),
    _IbmtbwinFiltOutIfIndex_Type()
)
ibmtbwinFiltOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutIfIndex.setStatus("mandatory")
_IbmtbwinFiltOutContents_Type = OctetString
_IbmtbwinFiltOutContents_Object = MibTableColumn
ibmtbwinFiltOutContents = _IbmtbwinFiltOutContents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1, 2),
    _IbmtbwinFiltOutContents_Type()
)
ibmtbwinFiltOutContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutContents.setStatus("mandatory")
_IbmtbwinFiltOutMaskString_Type = OctetString
_IbmtbwinFiltOutMaskString_Object = MibTableColumn
ibmtbwinFiltOutMaskString = _IbmtbwinFiltOutMaskString_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1, 3),
    _IbmtbwinFiltOutMaskString_Type()
)
ibmtbwinFiltOutMaskString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutMaskString.setStatus("mandatory")
_IbmtbwinFiltOutOffsetStart_Type = DisplayString
_IbmtbwinFiltOutOffsetStart_Object = MibTableColumn
ibmtbwinFiltOutOffsetStart = _IbmtbwinFiltOutOffsetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1, 4),
    _IbmtbwinFiltOutOffsetStart_Type()
)
ibmtbwinFiltOutOffsetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutOffsetStart.setStatus("mandatory")


class _IbmtbwinFiltOutNumBytes_Type(OctetString):
    """Custom type ibmtbwinFiltOutNumBytes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmtbwinFiltOutNumBytes_Type.__name__ = "OctetString"
_IbmtbwinFiltOutNumBytes_Object = MibTableColumn
ibmtbwinFiltOutNumBytes = _IbmtbwinFiltOutNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1, 5),
    _IbmtbwinFiltOutNumBytes_Type()
)
ibmtbwinFiltOutNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutNumBytes.setStatus("mandatory")


class _IbmtbwinFiltOutOffset_Type(OctetString):
    """Custom type ibmtbwinFiltOutOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmtbwinFiltOutOffset_Type.__name__ = "OctetString"
_IbmtbwinFiltOutOffset_Object = MibTableColumn
ibmtbwinFiltOutOffset = _IbmtbwinFiltOutOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1, 6),
    _IbmtbwinFiltOutOffset_Type()
)
ibmtbwinFiltOutOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutOffset.setStatus("mandatory")
_IbmtbwinFiltOutId_Type = Integer32
_IbmtbwinFiltOutId_Object = MibTableColumn
ibmtbwinFiltOutId = _IbmtbwinFiltOutId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 8, 3, 1, 7),
    _IbmtbwinFiltOutId_Type()
)
ibmtbwinFiltOutId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbwinFiltOutId.setStatus("mandatory")
_IbmtbFiltOrderTable_ObjectIdentity = ObjectIdentity
ibmtbFiltOrderTable = _IbmtbFiltOrderTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9)
)
_IbmtbFiltOrderInTable_Object = MibTable
ibmtbFiltOrderInTable = _IbmtbFiltOrderInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 1)
)
if mibBuilder.loadTexts:
    ibmtbFiltOrderInTable.setStatus("mandatory")
_IbmtbFiltOrderInEntry_Object = MibTableRow
ibmtbFiltOrderInEntry = _IbmtbFiltOrderInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 1, 1)
)
ibmtbFiltOrderInEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbFiltOrderInPriority"),
)
if mibBuilder.loadTexts:
    ibmtbFiltOrderInEntry.setStatus("mandatory")
_IbmtbFiltOrderInIfIndex_Type = Integer32
_IbmtbFiltOrderInIfIndex_Object = MibTableColumn
ibmtbFiltOrderInIfIndex = _IbmtbFiltOrderInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 1, 1, 1),
    _IbmtbFiltOrderInIfIndex_Type()
)
ibmtbFiltOrderInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbFiltOrderInIfIndex.setStatus("mandatory")
_IbmtbFiltOrderInPriority_Type = Integer32
_IbmtbFiltOrderInPriority_Object = MibTableColumn
ibmtbFiltOrderInPriority = _IbmtbFiltOrderInPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 1, 1, 2),
    _IbmtbFiltOrderInPriority_Type()
)
ibmtbFiltOrderInPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbFiltOrderInPriority.setStatus("mandatory")
_IbmtbFiltOrderInName_Type = DisplayString
_IbmtbFiltOrderInName_Object = MibTableColumn
ibmtbFiltOrderInName = _IbmtbFiltOrderInName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 1, 1, 3),
    _IbmtbFiltOrderInName_Type()
)
ibmtbFiltOrderInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbFiltOrderInName.setStatus("mandatory")
_IbmtbFiltOrderOutTable_Object = MibTable
ibmtbFiltOrderOutTable = _IbmtbFiltOrderOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 2)
)
if mibBuilder.loadTexts:
    ibmtbFiltOrderOutTable.setStatus("mandatory")
_IbmtbFiltOrderOutEntry_Object = MibTableRow
ibmtbFiltOrderOutEntry = _IbmtbFiltOrderOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 2, 1)
)
ibmtbFiltOrderOutEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmtbFiltOrderOutPriority"),
)
if mibBuilder.loadTexts:
    ibmtbFiltOrderOutEntry.setStatus("mandatory")
_IbmtbFiltOrderOutIfIndex_Type = Integer32
_IbmtbFiltOrderOutIfIndex_Object = MibTableColumn
ibmtbFiltOrderOutIfIndex = _IbmtbFiltOrderOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 2, 1, 1),
    _IbmtbFiltOrderOutIfIndex_Type()
)
ibmtbFiltOrderOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbFiltOrderOutIfIndex.setStatus("mandatory")
_IbmtbFiltOrderOutPriority_Type = Integer32
_IbmtbFiltOrderOutPriority_Object = MibTableColumn
ibmtbFiltOrderOutPriority = _IbmtbFiltOrderOutPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 2, 1, 2),
    _IbmtbFiltOrderOutPriority_Type()
)
ibmtbFiltOrderOutPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbFiltOrderOutPriority.setStatus("mandatory")
_IbmtbFiltOrderOutName_Type = DisplayString
_IbmtbFiltOrderOutName_Object = MibTableColumn
ibmtbFiltOrderOutName = _IbmtbFiltOrderOutName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 15, 9, 2, 1, 3),
    _IbmtbFiltOrderOutName_Type()
)
ibmtbFiltOrderOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmtbFiltOrderOutName.setStatus("mandatory")
_Ibmapple_ObjectIdentity = ObjectIdentity
ibmapple = _Ibmapple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16)
)
_IbmSelectNet_ObjectIdentity = ObjectIdentity
ibmSelectNet = _IbmSelectNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1)
)
_IbmSelectNetTable_Object = MibTable
ibmSelectNetTable = _IbmSelectNetTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    ibmSelectNetTable.setStatus("mandatory")
_IbmSelectNetEntry_Object = MibTableRow
ibmSelectNetEntry = _IbmSelectNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1, 1, 1)
)
ibmSelectNetEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmSelectNetIndex"),
)
if mibBuilder.loadTexts:
    ibmSelectNetEntry.setStatus("mandatory")
_IbmSelectNetIndex_Type = Integer32
_IbmSelectNetIndex_Object = MibTableColumn
ibmSelectNetIndex = _IbmSelectNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1, 1, 1, 1),
    _IbmSelectNetIndex_Type()
)
ibmSelectNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetIndex.setStatus("mandatory")
_IbmSelectNetZone_Type = OctetString
_IbmSelectNetZone_Object = MibTableColumn
ibmSelectNetZone = _IbmSelectNetZone_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1, 1, 1, 2),
    _IbmSelectNetZone_Type()
)
ibmSelectNetZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetZone.setStatus("mandatory")


class _IbmSelectNetNetStart_Type(OctetString):
    """Custom type ibmSelectNetNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmSelectNetNetStart_Type.__name__ = "OctetString"
_IbmSelectNetNetStart_Object = MibTableColumn
ibmSelectNetNetStart = _IbmSelectNetNetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1, 1, 1, 3),
    _IbmSelectNetNetStart_Type()
)
ibmSelectNetNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetNetStart.setStatus("mandatory")


class _IbmSelectNetNetEnd_Type(OctetString):
    """Custom type ibmSelectNetNetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmSelectNetNetEnd_Type.__name__ = "OctetString"
_IbmSelectNetNetEnd_Object = MibTableColumn
ibmSelectNetNetEnd = _IbmSelectNetNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1, 1, 1, 4),
    _IbmSelectNetNetEnd_Type()
)
ibmSelectNetNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetNetEnd.setStatus("mandatory")


class _IbmSelectNetInterfaceNetStart_Type(OctetString):
    """Custom type ibmSelectNetInterfaceNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmSelectNetInterfaceNetStart_Type.__name__ = "OctetString"
_IbmSelectNetInterfaceNetStart_Object = MibTableColumn
ibmSelectNetInterfaceNetStart = _IbmSelectNetInterfaceNetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 1, 1, 1, 5),
    _IbmSelectNetInterfaceNetStart_Type()
)
ibmSelectNetInterfaceNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetInterfaceNetStart.setStatus("mandatory")
_IbmnbpFilter_ObjectIdentity = ObjectIdentity
ibmnbpFilter = _IbmnbpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 2)
)
_IbmnbpFilterPacketsFiltered_Type = Counter32
_IbmnbpFilterPacketsFiltered_Object = MibScalar
ibmnbpFilterPacketsFiltered = _IbmnbpFilterPacketsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 2, 1),
    _IbmnbpFilterPacketsFiltered_Type()
)
ibmnbpFilterPacketsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnbpFilterPacketsFiltered.setStatus("mandatory")
_IbmnbpFilterPacketsSent_Type = Counter32
_IbmnbpFilterPacketsSent_Object = MibScalar
ibmnbpFilterPacketsSent = _IbmnbpFilterPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 2, 2),
    _IbmnbpFilterPacketsSent_Type()
)
ibmnbpFilterPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmnbpFilterPacketsSent.setStatus("mandatory")
_IbmatportFilter_ObjectIdentity = ObjectIdentity
ibmatportFilter = _IbmatportFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 3)
)
_IbmatportFilterTable_Object = MibTable
ibmatportFilterTable = _IbmatportFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    ibmatportFilterTable.setStatus("mandatory")
_IbmatportFilterEntry_Object = MibTableRow
ibmatportFilterEntry = _IbmatportFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 3, 1, 1)
)
ibmatportFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmatportFilterIndex"),
    (0, "IBM6611-MIB", "ibmatportFilterNetStart"),
)
if mibBuilder.loadTexts:
    ibmatportFilterEntry.setStatus("mandatory")
_IbmatportFilterIndex_Type = Integer32
_IbmatportFilterIndex_Object = MibTableColumn
ibmatportFilterIndex = _IbmatportFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 3, 1, 1, 1),
    _IbmatportFilterIndex_Type()
)
ibmatportFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmatportFilterIndex.setStatus("mandatory")


class _IbmatportFilterNetStart_Type(OctetString):
    """Custom type ibmatportFilterNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmatportFilterNetStart_Type.__name__ = "OctetString"
_IbmatportFilterNetStart_Object = MibTableColumn
ibmatportFilterNetStart = _IbmatportFilterNetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 3, 1, 1, 2),
    _IbmatportFilterNetStart_Type()
)
ibmatportFilterNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmatportFilterNetStart.setStatus("mandatory")


class _IbmatportFilterNetEnd_Type(OctetString):
    """Custom type ibmatportFilterNetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmatportFilterNetEnd_Type.__name__ = "OctetString"
_IbmatportFilterNetEnd_Object = MibTableColumn
ibmatportFilterNetEnd = _IbmatportFilterNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 3, 1, 1, 3),
    _IbmatportFilterNetEnd_Type()
)
ibmatportFilterNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmatportFilterNetEnd.setStatus("mandatory")
_IbmSelectNetFilter_ObjectIdentity = ObjectIdentity
ibmSelectNetFilter = _IbmSelectNetFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 4)
)
_IbmSelectNetFilterTable_Object = MibTable
ibmSelectNetFilterTable = _IbmSelectNetFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    ibmSelectNetFilterTable.setStatus("mandatory")
_IbmSelectNetFilterEntry_Object = MibTableRow
ibmSelectNetFilterEntry = _IbmSelectNetFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 4, 1, 1)
)
ibmSelectNetFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmSelectNetFilterIndex"),
    (0, "IBM6611-MIB", "ibmSelectNetFilterNetStart"),
)
if mibBuilder.loadTexts:
    ibmSelectNetFilterEntry.setStatus("mandatory")
_IbmSelectNetFilterIndex_Type = Integer32
_IbmSelectNetFilterIndex_Object = MibTableColumn
ibmSelectNetFilterIndex = _IbmSelectNetFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 4, 1, 1, 1),
    _IbmSelectNetFilterIndex_Type()
)
ibmSelectNetFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetFilterIndex.setStatus("mandatory")


class _IbmSelectNetFilterNetStart_Type(OctetString):
    """Custom type ibmSelectNetFilterNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmSelectNetFilterNetStart_Type.__name__ = "OctetString"
_IbmSelectNetFilterNetStart_Object = MibTableColumn
ibmSelectNetFilterNetStart = _IbmSelectNetFilterNetStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 4, 1, 1, 2),
    _IbmSelectNetFilterNetStart_Type()
)
ibmSelectNetFilterNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetFilterNetStart.setStatus("mandatory")


class _IbmSelectNetFilterNetEnd_Type(OctetString):
    """Custom type ibmSelectNetFilterNetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmSelectNetFilterNetEnd_Type.__name__ = "OctetString"
_IbmSelectNetFilterNetEnd_Object = MibTableColumn
ibmSelectNetFilterNetEnd = _IbmSelectNetFilterNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 16, 4, 1, 1, 3),
    _IbmSelectNetFilterNetEnd_Type()
)
ibmSelectNetFilterNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSelectNetFilterNetEnd.setStatus("mandatory")
_Ibmdec_ObjectIdentity = ObjectIdentity
ibmdec = _Ibmdec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17)
)


class _IbmdecAllRoutersFuncAddr_Type(OctetString):
    """Custom type ibmdecAllRoutersFuncAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdecAllRoutersFuncAddr_Type.__name__ = "OctetString"
_IbmdecAllRoutersFuncAddr_Object = MibScalar
ibmdecAllRoutersFuncAddr = _IbmdecAllRoutersFuncAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 1),
    _IbmdecAllRoutersFuncAddr_Type()
)
ibmdecAllRoutersFuncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecAllRoutersFuncAddr.setStatus("mandatory")


class _IbmdecAllEndNodesFuncAddr_Type(OctetString):
    """Custom type ibmdecAllEndNodesFuncAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmdecAllEndNodesFuncAddr_Type.__name__ = "OctetString"
_IbmdecAllEndNodesFuncAddr_Object = MibScalar
ibmdecAllEndNodesFuncAddr = _IbmdecAllEndNodesFuncAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 2),
    _IbmdecAllEndNodesFuncAddr_Type()
)
ibmdecAllEndNodesFuncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecAllEndNodesFuncAddr.setStatus("mandatory")


class _IbmdecSplitHorPoisonRev_Type(Integer32):
    """Custom type ibmdecSplitHorPoisonRev based on Integer32"""
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


_IbmdecSplitHorPoisonRev_Type.__name__ = "Integer32"
_IbmdecSplitHorPoisonRev_Object = MibScalar
ibmdecSplitHorPoisonRev = _IbmdecSplitHorPoisonRev_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 3),
    _IbmdecSplitHorPoisonRev_Type()
)
ibmdecSplitHorPoisonRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecSplitHorPoisonRev.setStatus("mandatory")


class _IbmdecNodeType_Type(Integer32):
    """Custom type ibmdecNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("area", 3),
          ("area-IV-Prime", 6),
          ("nonrouting-III", 2),
          ("nonrouting-IV", 5),
          ("nonrouting-IV-Prime", 8),
          ("routing-III", 1),
          ("routing-IV", 4),
          ("routing-IV-Prime", 7))
    )


_IbmdecNodeType_Type.__name__ = "Integer32"
_IbmdecNodeType_Object = MibScalar
ibmdecNodeType = _IbmdecNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 4),
    _IbmdecNodeType_Type()
)
ibmdecNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecNodeType.setStatus("mandatory")
_IbmdecLANCircuitTable_Object = MibTable
ibmdecLANCircuitTable = _IbmdecLANCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 5)
)
if mibBuilder.loadTexts:
    ibmdecLANCircuitTable.setStatus("mandatory")
_IbmdecLANCircuitEntry_Object = MibTableRow
ibmdecLANCircuitEntry = _IbmdecLANCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 5, 1)
)
ibmdecLANCircuitEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmdecLANCircuitIndex"),
)
if mibBuilder.loadTexts:
    ibmdecLANCircuitEntry.setStatus("mandatory")
_IbmdecLANCircuitIndex_Type = Integer32
_IbmdecLANCircuitIndex_Object = MibTableColumn
ibmdecLANCircuitIndex = _IbmdecLANCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 5, 1, 1),
    _IbmdecLANCircuitIndex_Type()
)
ibmdecLANCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecLANCircuitIndex.setStatus("mandatory")


class _IbmdecLANCircuitType_Type(Integer32):
    """Custom type ibmdecLANCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ama", 2),
          ("bilingual", 1),
          ("phaseIV", 3))
    )


_IbmdecLANCircuitType_Type.__name__ = "Integer32"
_IbmdecLANCircuitType_Object = MibTableColumn
ibmdecLANCircuitType = _IbmdecLANCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 5, 1, 2),
    _IbmdecLANCircuitType_Type()
)
ibmdecLANCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecLANCircuitType.setStatus("mandatory")


class _IbmdecLANCircuitSourceRoute_Type(Integer32):
    """Custom type ibmdecLANCircuitSourceRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notapplicable", 3))
    )


_IbmdecLANCircuitSourceRoute_Type.__name__ = "Integer32"
_IbmdecLANCircuitSourceRoute_Object = MibTableColumn
ibmdecLANCircuitSourceRoute = _IbmdecLANCircuitSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 5, 1, 3),
    _IbmdecLANCircuitSourceRoute_Type()
)
ibmdecLANCircuitSourceRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecLANCircuitSourceRoute.setStatus("mandatory")


class _IbmdecLANCircuitAddrType_Type(Integer32):
    """Custom type ibmdecLANCircuitAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decnet", 1),
          ("hardware", 2),
          ("user", 3))
    )


_IbmdecLANCircuitAddrType_Type.__name__ = "Integer32"
_IbmdecLANCircuitAddrType_Object = MibTableColumn
ibmdecLANCircuitAddrType = _IbmdecLANCircuitAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 17, 5, 1, 4),
    _IbmdecLANCircuitAddrType_Type()
)
ibmdecLANCircuitAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdecLANCircuitAddrType.setStatus("mandatory")
_Ibmvines_ObjectIdentity = ObjectIdentity
ibmvines = _Ibmvines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18)
)
_IbmvSysConfig_ObjectIdentity = ObjectIdentity
ibmvSysConfig = _IbmvSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 1)
)


class _IbmvSysRtr_Type(Integer32):
    """Custom type ibmvSysRtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvSysRtr_Type.__name__ = "Integer32"
_IbmvSysRtr_Object = MibScalar
ibmvSysRtr = _IbmvSysRtr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 1, 1),
    _IbmvSysRtr_Type()
)
ibmvSysRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvSysRtr.setStatus("mandatory")
_IbmvRouterName_Type = DisplayString
_IbmvRouterName_Object = MibScalar
ibmvRouterName = _IbmvRouterName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 1, 2),
    _IbmvRouterName_Type()
)
ibmvRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRouterName.setStatus("mandatory")
_IbmvRouterNetid_Type = Integer32
_IbmvRouterNetid_Object = MibScalar
ibmvRouterNetid = _IbmvRouterNetid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 1, 3),
    _IbmvRouterNetid_Type()
)
ibmvRouterNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRouterNetid.setStatus("mandatory")
_IbmvIP_ObjectIdentity = ObjectIdentity
ibmvIP = _IbmvIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2)
)
_IbmvipTotalIn_Type = Counter32
_IbmvipTotalIn_Object = MibScalar
ibmvipTotalIn = _IbmvipTotalIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 1),
    _IbmvipTotalIn_Type()
)
ibmvipTotalIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipTotalIn.setStatus("mandatory")
_IbmvipTotalOut_Type = Counter32
_IbmvipTotalOut_Object = MibScalar
ibmvipTotalOut = _IbmvipTotalOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 2),
    _IbmvipTotalOut_Type()
)
ibmvipTotalOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipTotalOut.setStatus("mandatory")
_IbmvipRouted_Type = Counter32
_IbmvipRouted_Object = MibScalar
ibmvipRouted = _IbmvipRouted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 3),
    _IbmvipRouted_Type()
)
ibmvipRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipRouted.setStatus("mandatory")
_IbmvipBcast_Type = Counter32
_IbmvipBcast_Object = MibScalar
ibmvipBcast = _IbmvipBcast_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 4),
    _IbmvipBcast_Type()
)
ibmvipBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipBcast.setStatus("mandatory")
_IbmvipInReceives_Type = Counter32
_IbmvipInReceives_Object = MibScalar
ibmvipInReceives = _IbmvipInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 5),
    _IbmvipInReceives_Type()
)
ibmvipInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipInReceives.setStatus("mandatory")
_IbmvipBcastInReceives_Type = Counter32
_IbmvipBcastInReceives_Object = MibScalar
ibmvipBcastInReceives = _IbmvipBcastInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 6),
    _IbmvipBcastInReceives_Type()
)
ibmvipBcastInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipBcastInReceives.setStatus("mandatory")
_IbmvipBad_Type = Counter32
_IbmvipBad_Object = MibScalar
ibmvipBad = _IbmvipBad_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 7),
    _IbmvipBad_Type()
)
ibmvipBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipBad.setStatus("mandatory")
_IbmvipBadHeaders_Type = Counter32
_IbmvipBadHeaders_Object = MibScalar
ibmvipBadHeaders = _IbmvipBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 8),
    _IbmvipBadHeaders_Type()
)
ibmvipBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipBadHeaders.setStatus("mandatory")
_IbmvipTooSmalls_Type = Counter32
_IbmvipTooSmalls_Object = MibScalar
ibmvipTooSmalls = _IbmvipTooSmalls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 9),
    _IbmvipTooSmalls_Type()
)
ibmvipTooSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipTooSmalls.setStatus("mandatory")
_IbmvipBadLens_Type = Counter32
_IbmvipBadLens_Object = MibScalar
ibmvipBadLens = _IbmvipBadLens_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 10),
    _IbmvipBadLens_Type()
)
ibmvipBadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipBadLens.setStatus("mandatory")
_IbmvipBadSums_Type = Counter32
_IbmvipBadSums_Object = MibScalar
ibmvipBadSums = _IbmvipBadSums_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 11),
    _IbmvipBadSums_Type()
)
ibmvipBadSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipBadSums.setStatus("mandatory")
_IbmvipInDiscards_Type = Counter32
_IbmvipInDiscards_Object = MibScalar
ibmvipInDiscards = _IbmvipInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 12),
    _IbmvipInDiscards_Type()
)
ibmvipInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipInDiscards.setStatus("mandatory")
_IbmvipZeroHops_Type = Counter32
_IbmvipZeroHops_Object = MibScalar
ibmvipZeroHops = _IbmvipZeroHops_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 13),
    _IbmvipZeroHops_Type()
)
ibmvipZeroHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipZeroHops.setStatus("mandatory")
_IbmvipOutNoRoutes_Type = Counter32
_IbmvipOutNoRoutes_Object = MibScalar
ibmvipOutNoRoutes = _IbmvipOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 2, 14),
    _IbmvipOutNoRoutes_Type()
)
ibmvipOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvipOutNoRoutes.setStatus("mandatory")
_IbmvNeighbor_ObjectIdentity = ObjectIdentity
ibmvNeighbor = _IbmvNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3)
)
_IbmvARP_ObjectIdentity = ObjectIdentity
ibmvARP = _IbmvARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 1)
)
_IbmvarpQueryReqs_Type = Counter32
_IbmvarpQueryReqs_Object = MibScalar
ibmvarpQueryReqs = _IbmvarpQueryReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 1, 1),
    _IbmvarpQueryReqs_Type()
)
ibmvarpQueryReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvarpQueryReqs.setStatus("mandatory")
_IbmvarpServiceResps_Type = Counter32
_IbmvarpServiceResps_Object = MibScalar
ibmvarpServiceResps = _IbmvarpServiceResps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 1, 2),
    _IbmvarpServiceResps_Type()
)
ibmvarpServiceResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvarpServiceResps.setStatus("mandatory")
_IbmvarpAssignReqs_Type = Counter32
_IbmvarpAssignReqs_Object = MibScalar
ibmvarpAssignReqs = _IbmvarpAssignReqs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 1, 3),
    _IbmvarpAssignReqs_Type()
)
ibmvarpAssignReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvarpAssignReqs.setStatus("mandatory")
_IbmvarpAssignResps_Type = Counter32
_IbmvarpAssignResps_Object = MibScalar
ibmvarpAssignResps = _IbmvarpAssignResps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 1, 4),
    _IbmvarpAssignResps_Type()
)
ibmvarpAssignResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvarpAssignResps.setStatus("mandatory")
_IbmvarpHeaderError_Type = Counter32
_IbmvarpHeaderError_Object = MibScalar
ibmvarpHeaderError = _IbmvarpHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 1, 5),
    _IbmvarpHeaderError_Type()
)
ibmvarpHeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvarpHeaderError.setStatus("mandatory")
_IbmvNbrNumber_Type = Integer32
_IbmvNbrNumber_Object = MibScalar
ibmvNbrNumber = _IbmvNbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 2),
    _IbmvNbrNumber_Type()
)
ibmvNbrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrNumber.setStatus("mandatory")
_IbmvNbrTable_Object = MibTable
ibmvNbrTable = _IbmvNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3)
)
if mibBuilder.loadTexts:
    ibmvNbrTable.setStatus("mandatory")
_IbmvNbrEntry_Object = MibTableRow
ibmvNbrEntry = _IbmvNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1)
)
ibmvNbrEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvNbrNetid"),
    (0, "IBM6611-MIB", "ibmvNbrSubNetid"),
    (0, "IBM6611-MIB", "ibmvNbrIfType"),
    (0, "IBM6611-MIB", "ibmvNbrLocSlot"),
    (0, "IBM6611-MIB", "ibmvNbrLocPort"),
)
if mibBuilder.loadTexts:
    ibmvNbrEntry.setStatus("mandatory")
_IbmvNbrNetid_Type = OctetString
_IbmvNbrNetid_Object = MibTableColumn
ibmvNbrNetid = _IbmvNbrNetid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 1),
    _IbmvNbrNetid_Type()
)
ibmvNbrNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrNetid.setStatus("mandatory")
_IbmvNbrSubNetid_Type = OctetString
_IbmvNbrSubNetid_Object = MibTableColumn
ibmvNbrSubNetid = _IbmvNbrSubNetid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 2),
    _IbmvNbrSubNetid_Type()
)
ibmvNbrSubNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrSubNetid.setStatus("mandatory")


class _IbmvNbrType_Type(Integer32):
    """Custom type ibmvNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("workstation", 2))
    )


_IbmvNbrType_Type.__name__ = "Integer32"
_IbmvNbrType_Object = MibTableColumn
ibmvNbrType = _IbmvNbrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 3),
    _IbmvNbrType_Type()
)
ibmvNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrType.setStatus("mandatory")


class _IbmvNbrIfType_Type(Integer32):
    """Custom type ibmvNbrIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("basicISDN", 20),
          ("cept", 19),
          ("ddn-x25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("frame-relay", 32),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("loopback", 24),
          ("nsip", 27),
          ("other", 1),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("starLan", 11),
          ("ultra", 29))
    )


_IbmvNbrIfType_Type.__name__ = "Integer32"
_IbmvNbrIfType_Object = MibTableColumn
ibmvNbrIfType = _IbmvNbrIfType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 4),
    _IbmvNbrIfType_Type()
)
ibmvNbrIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrIfType.setStatus("mandatory")
_IbmvNbrRemAddress_Type = OctetString
_IbmvNbrRemAddress_Object = MibTableColumn
ibmvNbrRemAddress = _IbmvNbrRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 5),
    _IbmvNbrRemAddress_Type()
)
ibmvNbrRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrRemAddress.setStatus("mandatory")
_IbmvNbrLocAddress_Type = OctetString
_IbmvNbrLocAddress_Object = MibTableColumn
ibmvNbrLocAddress = _IbmvNbrLocAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 6),
    _IbmvNbrLocAddress_Type()
)
ibmvNbrLocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrLocAddress.setStatus("mandatory")


class _IbmvNbrLocSlot_Type(Integer32):
    """Custom type ibmvNbrLocSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IbmvNbrLocSlot_Type.__name__ = "Integer32"
_IbmvNbrLocSlot_Object = MibTableColumn
ibmvNbrLocSlot = _IbmvNbrLocSlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 7),
    _IbmvNbrLocSlot_Type()
)
ibmvNbrLocSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrLocSlot.setStatus("mandatory")


class _IbmvNbrLocPort_Type(Integer32):
    """Custom type ibmvNbrLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IbmvNbrLocPort_Type.__name__ = "Integer32"
_IbmvNbrLocPort_Object = MibTableColumn
ibmvNbrLocPort = _IbmvNbrLocPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 8),
    _IbmvNbrLocPort_Type()
)
ibmvNbrLocPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrLocPort.setStatus("mandatory")
_IbmvNbrAging_Type = Integer32
_IbmvNbrAging_Object = MibTableColumn
ibmvNbrAging = _IbmvNbrAging_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 9),
    _IbmvNbrAging_Type()
)
ibmvNbrAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrAging.setStatus("mandatory")


class _IbmvNbrFlags_Type(Integer32):
    """Custom type ibmvNbrFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonpermanent", 2),
          ("permanent", 1))
    )


_IbmvNbrFlags_Type.__name__ = "Integer32"
_IbmvNbrFlags_Object = MibTableColumn
ibmvNbrFlags = _IbmvNbrFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 10),
    _IbmvNbrFlags_Type()
)
ibmvNbrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrFlags.setStatus("mandatory")
_IbmvNbrRIF_Type = OctetString
_IbmvNbrRIF_Object = MibTableColumn
ibmvNbrRIF = _IbmvNbrRIF_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 11),
    _IbmvNbrRIF_Type()
)
ibmvNbrRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrRIF.setStatus("mandatory")
_IbmvNbrIfIndex_Type = Integer32
_IbmvNbrIfIndex_Object = MibTableColumn
ibmvNbrIfIndex = _IbmvNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 12),
    _IbmvNbrIfIndex_Type()
)
ibmvNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrIfIndex.setStatus("mandatory")
_IbmvNbrMetric_Type = Integer32
_IbmvNbrMetric_Object = MibTableColumn
ibmvNbrMetric = _IbmvNbrMetric_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 3, 3, 1, 13),
    _IbmvNbrMetric_Type()
)
ibmvNbrMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvNbrMetric.setStatus("mandatory")
_IbmvRouting_ObjectIdentity = ObjectIdentity
ibmvRouting = _IbmvRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4)
)
_IbmvRtConfig_ObjectIdentity = ObjectIdentity
ibmvRtConfig = _IbmvRtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1)
)
_IbmvRtCfgMax_Type = Integer32
_IbmvRtCfgMax_Object = MibScalar
ibmvRtCfgMax = _IbmvRtCfgMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 1),
    _IbmvRtCfgMax_Type()
)
ibmvRtCfgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgMax.setStatus("mandatory")


class _IbmvRtCfgInFlt_Type(Integer32):
    """Custom type ibmvRtCfgInFlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvRtCfgInFlt_Type.__name__ = "Integer32"
_IbmvRtCfgInFlt_Object = MibScalar
ibmvRtCfgInFlt = _IbmvRtCfgInFlt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 2),
    _IbmvRtCfgInFlt_Type()
)
ibmvRtCfgInFlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgInFlt.setStatus("mandatory")
_IbmvRtCfgInFltNum_Type = Integer32
_IbmvRtCfgInFltNum_Object = MibScalar
ibmvRtCfgInFltNum = _IbmvRtCfgInFltNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 3),
    _IbmvRtCfgInFltNum_Type()
)
ibmvRtCfgInFltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgInFltNum.setStatus("mandatory")
_IbmvRtCfgInFltTable_Object = MibTable
ibmvRtCfgInFltTable = _IbmvRtCfgInFltTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ibmvRtCfgInFltTable.setStatus("mandatory")
_IbmvRtCfgInFltEntry_Object = MibTableRow
ibmvRtCfgInFltEntry = _IbmvRtCfgInFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 4, 1)
)
ibmvRtCfgInFltEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvRtCfgInFltNetID"),
    (0, "IBM6611-MIB", "ibmvRtCfgInFltIfIndex"),
)
if mibBuilder.loadTexts:
    ibmvRtCfgInFltEntry.setStatus("mandatory")
_IbmvRtCfgInFltNetID_Type = OctetString
_IbmvRtCfgInFltNetID_Object = MibTableColumn
ibmvRtCfgInFltNetID = _IbmvRtCfgInFltNetID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 4, 1, 1),
    _IbmvRtCfgInFltNetID_Type()
)
ibmvRtCfgInFltNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgInFltNetID.setStatus("mandatory")
_IbmvRtCfgInFltIfIndex_Type = Integer32
_IbmvRtCfgInFltIfIndex_Object = MibTableColumn
ibmvRtCfgInFltIfIndex = _IbmvRtCfgInFltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 4, 1, 2),
    _IbmvRtCfgInFltIfIndex_Type()
)
ibmvRtCfgInFltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgInFltIfIndex.setStatus("mandatory")


class _IbmvRtCfgInFltMode_Type(Integer32):
    """Custom type ibmvRtCfgInFltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IbmvRtCfgInFltMode_Type.__name__ = "Integer32"
_IbmvRtCfgInFltMode_Object = MibTableColumn
ibmvRtCfgInFltMode = _IbmvRtCfgInFltMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 4, 1, 3),
    _IbmvRtCfgInFltMode_Type()
)
ibmvRtCfgInFltMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgInFltMode.setStatus("mandatory")
_IbmvRtCfgInFltUses_Type = Counter32
_IbmvRtCfgInFltUses_Object = MibTableColumn
ibmvRtCfgInFltUses = _IbmvRtCfgInFltUses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 4, 1, 4),
    _IbmvRtCfgInFltUses_Type()
)
ibmvRtCfgInFltUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgInFltUses.setStatus("mandatory")


class _IbmvRtCfgOutFlt_Type(Integer32):
    """Custom type ibmvRtCfgOutFlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvRtCfgOutFlt_Type.__name__ = "Integer32"
_IbmvRtCfgOutFlt_Object = MibScalar
ibmvRtCfgOutFlt = _IbmvRtCfgOutFlt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 5),
    _IbmvRtCfgOutFlt_Type()
)
ibmvRtCfgOutFlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgOutFlt.setStatus("mandatory")
_IbmvRtCfgOutFltNum_Type = Integer32
_IbmvRtCfgOutFltNum_Object = MibScalar
ibmvRtCfgOutFltNum = _IbmvRtCfgOutFltNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 6),
    _IbmvRtCfgOutFltNum_Type()
)
ibmvRtCfgOutFltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgOutFltNum.setStatus("mandatory")
_IbmvRtCfgOutFltTable_Object = MibTable
ibmvRtCfgOutFltTable = _IbmvRtCfgOutFltTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 7)
)
if mibBuilder.loadTexts:
    ibmvRtCfgOutFltTable.setStatus("mandatory")
_IbmvRtCfgOutFltEntry_Object = MibTableRow
ibmvRtCfgOutFltEntry = _IbmvRtCfgOutFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 7, 1)
)
ibmvRtCfgOutFltEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvRtCfgOutFltNetID"),
    (0, "IBM6611-MIB", "ibmvRtCfgOutFltIfIndex"),
)
if mibBuilder.loadTexts:
    ibmvRtCfgOutFltEntry.setStatus("mandatory")
_IbmvRtCfgOutFltNetID_Type = OctetString
_IbmvRtCfgOutFltNetID_Object = MibTableColumn
ibmvRtCfgOutFltNetID = _IbmvRtCfgOutFltNetID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 7, 1, 1),
    _IbmvRtCfgOutFltNetID_Type()
)
ibmvRtCfgOutFltNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgOutFltNetID.setStatus("mandatory")
_IbmvRtCfgOutFltIfIndex_Type = Integer32
_IbmvRtCfgOutFltIfIndex_Object = MibTableColumn
ibmvRtCfgOutFltIfIndex = _IbmvRtCfgOutFltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 7, 1, 2),
    _IbmvRtCfgOutFltIfIndex_Type()
)
ibmvRtCfgOutFltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgOutFltIfIndex.setStatus("mandatory")


class _IbmvRtCfgOutFltMode_Type(Integer32):
    """Custom type ibmvRtCfgOutFltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IbmvRtCfgOutFltMode_Type.__name__ = "Integer32"
_IbmvRtCfgOutFltMode_Object = MibTableColumn
ibmvRtCfgOutFltMode = _IbmvRtCfgOutFltMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 7, 1, 3),
    _IbmvRtCfgOutFltMode_Type()
)
ibmvRtCfgOutFltMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgOutFltMode.setStatus("mandatory")
_IbmvRtCfgOutFltUses_Type = Counter32
_IbmvRtCfgOutFltUses_Object = MibTableColumn
ibmvRtCfgOutFltUses = _IbmvRtCfgOutFltUses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 7, 1, 4),
    _IbmvRtCfgOutFltUses_Type()
)
ibmvRtCfgOutFltUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgOutFltUses.setStatus("mandatory")


class _IbmvRtCfgFlt_Type(Integer32):
    """Custom type ibmvRtCfgFlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvRtCfgFlt_Type.__name__ = "Integer32"
_IbmvRtCfgFlt_Object = MibScalar
ibmvRtCfgFlt = _IbmvRtCfgFlt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 8),
    _IbmvRtCfgFlt_Type()
)
ibmvRtCfgFlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgFlt.setStatus("mandatory")
_IbmvRtCfgFltNum_Type = Integer32
_IbmvRtCfgFltNum_Object = MibScalar
ibmvRtCfgFltNum = _IbmvRtCfgFltNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 9),
    _IbmvRtCfgFltNum_Type()
)
ibmvRtCfgFltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgFltNum.setStatus("mandatory")
_IbmvRtCfgFltTable_Object = MibTable
ibmvRtCfgFltTable = _IbmvRtCfgFltTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 10)
)
if mibBuilder.loadTexts:
    ibmvRtCfgFltTable.setStatus("mandatory")
_IbmvRtCfgFltEntry_Object = MibTableRow
ibmvRtCfgFltEntry = _IbmvRtCfgFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 10, 1)
)
ibmvRtCfgFltEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvRtCfgFltNetID"),
)
if mibBuilder.loadTexts:
    ibmvRtCfgFltEntry.setStatus("mandatory")
_IbmvRtCfgFltNetID_Type = OctetString
_IbmvRtCfgFltNetID_Object = MibTableColumn
ibmvRtCfgFltNetID = _IbmvRtCfgFltNetID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 10, 1, 1),
    _IbmvRtCfgFltNetID_Type()
)
ibmvRtCfgFltNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgFltNetID.setStatus("mandatory")


class _IbmvRtCfgFltMode_Type(Integer32):
    """Custom type ibmvRtCfgFltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IbmvRtCfgFltMode_Type.__name__ = "Integer32"
_IbmvRtCfgFltMode_Object = MibTableColumn
ibmvRtCfgFltMode = _IbmvRtCfgFltMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 10, 1, 2),
    _IbmvRtCfgFltMode_Type()
)
ibmvRtCfgFltMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgFltMode.setStatus("mandatory")
_IbmvRtCfgFltUses_Type = Counter32
_IbmvRtCfgFltUses_Object = MibTableColumn
ibmvRtCfgFltUses = _IbmvRtCfgFltUses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 1, 10, 1, 3),
    _IbmvRtCfgFltUses_Type()
)
ibmvRtCfgFltUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtCfgFltUses.setStatus("mandatory")
_IbmvRTP_ObjectIdentity = ObjectIdentity
ibmvRTP = _IbmvRTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2)
)
_IbmvrtpUpdSents_Type = Counter32
_IbmvrtpUpdSents_Object = MibScalar
ibmvrtpUpdSents = _IbmvrtpUpdSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 1),
    _IbmvrtpUpdSents_Type()
)
ibmvrtpUpdSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpUpdSents.setStatus("mandatory")
_IbmvrtpUpdRecs_Type = Counter32
_IbmvrtpUpdRecs_Object = MibScalar
ibmvrtpUpdRecs = _IbmvrtpUpdRecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 2),
    _IbmvrtpUpdRecs_Type()
)
ibmvrtpUpdRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpUpdRecs.setStatus("mandatory")
_IbmvrtpReqSents_Type = Counter32
_IbmvrtpReqSents_Object = MibScalar
ibmvrtpReqSents = _IbmvrtpReqSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 3),
    _IbmvrtpReqSents_Type()
)
ibmvrtpReqSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpReqSents.setStatus("mandatory")
_IbmvrtpReqRecs_Type = Counter32
_IbmvrtpReqRecs_Object = MibScalar
ibmvrtpReqRecs = _IbmvrtpReqRecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 4),
    _IbmvrtpReqRecs_Type()
)
ibmvrtpReqRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpReqRecs.setStatus("mandatory")
_IbmvrtpResSents_Type = Counter32
_IbmvrtpResSents_Object = MibScalar
ibmvrtpResSents = _IbmvrtpResSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 5),
    _IbmvrtpResSents_Type()
)
ibmvrtpResSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpResSents.setStatus("mandatory")
_IbmvrtpResRecs_Type = Counter32
_IbmvrtpResRecs_Object = MibScalar
ibmvrtpResRecs = _IbmvrtpResRecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 6),
    _IbmvrtpResRecs_Type()
)
ibmvrtpResRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpResRecs.setStatus("mandatory")
_IbmvrtpRedSents_Type = Counter32
_IbmvrtpRedSents_Object = MibScalar
ibmvrtpRedSents = _IbmvrtpRedSents_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 7),
    _IbmvrtpRedSents_Type()
)
ibmvrtpRedSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpRedSents.setStatus("mandatory")
_IbmvrtpRedRecs_Type = Counter32
_IbmvrtpRedRecs_Object = MibScalar
ibmvrtpRedRecs = _IbmvrtpRedRecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 8),
    _IbmvrtpRedRecs_Type()
)
ibmvrtpRedRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpRedRecs.setStatus("mandatory")
_IbmvrtpHeaderError_Type = Counter32
_IbmvrtpHeaderError_Object = MibScalar
ibmvrtpHeaderError = _IbmvrtpHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 2, 9),
    _IbmvrtpHeaderError_Type()
)
ibmvrtpHeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvrtpHeaderError.setStatus("mandatory")
_IbmvRtNumber_Type = Integer32
_IbmvRtNumber_Object = MibScalar
ibmvRtNumber = _IbmvRtNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 3),
    _IbmvRtNumber_Type()
)
ibmvRtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtNumber.setStatus("mandatory")
_IbmvRtTable_Object = MibTable
ibmvRtTable = _IbmvRtTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4)
)
if mibBuilder.loadTexts:
    ibmvRtTable.setStatus("mandatory")
_IbmvRtEntry_Object = MibTableRow
ibmvRtEntry = _IbmvRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4, 1)
)
ibmvRtEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvRtNetid"),
)
if mibBuilder.loadTexts:
    ibmvRtEntry.setStatus("mandatory")
_IbmvRtNetid_Type = OctetString
_IbmvRtNetid_Object = MibTableColumn
ibmvRtNetid = _IbmvRtNetid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4, 1, 1),
    _IbmvRtNetid_Type()
)
ibmvRtNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtNetid.setStatus("mandatory")
_IbmvRtMetric_Type = Integer32
_IbmvRtMetric_Object = MibTableColumn
ibmvRtMetric = _IbmvRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4, 1, 2),
    _IbmvRtMetric_Type()
)
ibmvRtMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtMetric.setStatus("mandatory")
_IbmvRtIdle_Type = Integer32
_IbmvRtIdle_Object = MibTableColumn
ibmvRtIdle = _IbmvRtIdle_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4, 1, 3),
    _IbmvRtIdle_Type()
)
ibmvRtIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtIdle.setStatus("mandatory")
_IbmvRtGateNetid_Type = OctetString
_IbmvRtGateNetid_Object = MibTableColumn
ibmvRtGateNetid = _IbmvRtGateNetid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4, 1, 4),
    _IbmvRtGateNetid_Type()
)
ibmvRtGateNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtGateNetid.setStatus("mandatory")
_IbmvRtIfIndex_Type = Integer32
_IbmvRtIfIndex_Object = MibTableColumn
ibmvRtIfIndex = _IbmvRtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4, 1, 5),
    _IbmvRtIfIndex_Type()
)
ibmvRtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtIfIndex.setStatus("mandatory")


class _IbmvRtState_Type(Integer32):
    """Custom type ibmvRtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonpermanent", 2),
          ("permanent", 1))
    )


_IbmvRtState_Type.__name__ = "Integer32"
_IbmvRtState_Object = MibTableColumn
ibmvRtState = _IbmvRtState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 4, 4, 1, 6),
    _IbmvRtState_Type()
)
ibmvRtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvRtState.setStatus("mandatory")
_IbmvICP_ObjectIdentity = ObjectIdentity
ibmvICP = _IbmvICP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 5)
)
_IbmvicpExcGens_Type = Counter32
_IbmvicpExcGens_Object = MibScalar
ibmvicpExcGens = _IbmvicpExcGens_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 5, 1),
    _IbmvicpExcGens_Type()
)
ibmvicpExcGens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvicpExcGens.setStatus("mandatory")
_IbmvicpMetricGens_Type = Counter32
_IbmvicpMetricGens_Object = MibScalar
ibmvicpMetricGens = _IbmvicpMetricGens_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 5, 2),
    _IbmvicpMetricGens_Type()
)
ibmvicpMetricGens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvicpMetricGens.setStatus("mandatory")
_IbmvicpHeaderError_Type = Counter32
_IbmvicpHeaderError_Object = MibScalar
ibmvicpHeaderError = _IbmvicpHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 5, 3),
    _IbmvicpHeaderError_Type()
)
ibmvicpHeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvicpHeaderError.setStatus("mandatory")
_IbmvFRP_ObjectIdentity = ObjectIdentity
ibmvFRP = _IbmvFRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 6)
)
_IbmvFRPreassembles_Type = Counter32
_IbmvFRPreassembles_Object = MibScalar
ibmvFRPreassembles = _IbmvFRPreassembles_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 6, 1),
    _IbmvFRPreassembles_Type()
)
ibmvFRPreassembles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFRPreassembles.setStatus("mandatory")
_IbmvFRPfragsReassembled_Type = Counter32
_IbmvFRPfragsReassembled_Object = MibScalar
ibmvFRPfragsReassembled = _IbmvFRPfragsReassembled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 6, 2),
    _IbmvFRPfragsReassembled_Type()
)
ibmvFRPfragsReassembled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFRPfragsReassembled.setStatus("mandatory")
_IbmvFRPreasFails_Type = Counter32
_IbmvFRPreasFails_Object = MibScalar
ibmvFRPreasFails = _IbmvFRPreasFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 6, 3),
    _IbmvFRPreasFails_Type()
)
ibmvFRPreasFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFRPreasFails.setStatus("mandatory")
_IbmvFRPfragmented_Type = Counter32
_IbmvFRPfragmented_Object = MibScalar
ibmvFRPfragmented = _IbmvFRPfragmented_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 6, 4),
    _IbmvFRPfragmented_Type()
)
ibmvFRPfragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFRPfragmented.setStatus("mandatory")
_IbmvFRPfrgCreated_Type = Counter32
_IbmvFRPfrgCreated_Object = MibScalar
ibmvFRPfrgCreated = _IbmvFRPfrgCreated_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 6, 5),
    _IbmvFRPfrgCreated_Type()
)
ibmvFRPfrgCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFRPfrgCreated.setStatus("mandatory")
_IbmvFRPfrgFails_Type = Counter32
_IbmvFRPfrgFails_Object = MibScalar
ibmvFRPfrgFails = _IbmvFRPfrgFails_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 6, 6),
    _IbmvFRPfrgFails_Type()
)
ibmvFRPfrgFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFRPfrgFails.setStatus("mandatory")
_IbmvInterface_ObjectIdentity = ObjectIdentity
ibmvInterface = _IbmvInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7)
)
_IbmvPortCfgTable_Object = MibTable
ibmvPortCfgTable = _IbmvPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1)
)
if mibBuilder.loadTexts:
    ibmvPortCfgTable.setStatus("mandatory")
_IbmvPortCfgEntry_Object = MibTableRow
ibmvPortCfgEntry = _IbmvPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1)
)
ibmvPortCfgEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvPortCfgIfIndex"),
)
if mibBuilder.loadTexts:
    ibmvPortCfgEntry.setStatus("mandatory")
_IbmvPortCfgIfIndex_Type = Integer32
_IbmvPortCfgIfIndex_Object = MibTableColumn
ibmvPortCfgIfIndex = _IbmvPortCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 1),
    _IbmvPortCfgIfIndex_Type()
)
ibmvPortCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgIfIndex.setStatus("mandatory")


class _IbmvPortCfgARP_Type(Integer32):
    """Custom type ibmvPortCfgARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvPortCfgARP_Type.__name__ = "Integer32"
_IbmvPortCfgARP_Object = MibTableColumn
ibmvPortCfgARP = _IbmvPortCfgARP_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 2),
    _IbmvPortCfgARP_Type()
)
ibmvPortCfgARP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgARP.setStatus("mandatory")


class _IbmvPortCfgServ_Type(Integer32):
    """Custom type ibmvPortCfgServ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvPortCfgServ_Type.__name__ = "Integer32"
_IbmvPortCfgServ_Object = MibTableColumn
ibmvPortCfgServ = _IbmvPortCfgServ_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 3),
    _IbmvPortCfgServ_Type()
)
ibmvPortCfgServ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgServ.setStatus("mandatory")
_IbmvPortCfgHCtoServ_Type = Integer32
_IbmvPortCfgHCtoServ_Object = MibTableColumn
ibmvPortCfgHCtoServ = _IbmvPortCfgHCtoServ_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 4),
    _IbmvPortCfgHCtoServ_Type()
)
ibmvPortCfgHCtoServ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgHCtoServ.setStatus("mandatory")


class _IbmvPortCfgPerUpdate_Type(Integer32):
    """Custom type ibmvPortCfgPerUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("na", 3))
    )


_IbmvPortCfgPerUpdate_Type.__name__ = "Integer32"
_IbmvPortCfgPerUpdate_Object = MibTableColumn
ibmvPortCfgPerUpdate = _IbmvPortCfgPerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 5),
    _IbmvPortCfgPerUpdate_Type()
)
ibmvPortCfgPerUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgPerUpdate.setStatus("mandatory")
_IbmvPortCfgMetric_Type = Integer32
_IbmvPortCfgMetric_Object = MibTableColumn
ibmvPortCfgMetric = _IbmvPortCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 6),
    _IbmvPortCfgMetric_Type()
)
ibmvPortCfgMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgMetric.setStatus("mandatory")


class _IbmvPortCfgTR_Type(Integer32):
    """Custom type ibmvPortCfgTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("snap", 2),
          ("vines-tr", 3))
    )


_IbmvPortCfgTR_Type.__name__ = "Integer32"
_IbmvPortCfgTR_Object = MibTableColumn
ibmvPortCfgTR = _IbmvPortCfgTR_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 7),
    _IbmvPortCfgTR_Type()
)
ibmvPortCfgTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgTR.setStatus("mandatory")


class _IbmvPortCfgEN_Type(Integer32):
    """Custom type ibmvPortCfgEN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("snap", 2),
          ("v2", 3))
    )


_IbmvPortCfgEN_Type.__name__ = "Integer32"
_IbmvPortCfgEN_Object = MibTableColumn
ibmvPortCfgEN = _IbmvPortCfgEN_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 8),
    _IbmvPortCfgEN_Type()
)
ibmvPortCfgEN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgEN.setStatus("mandatory")


class _IbmvPortCfgInFlt_Type(Integer32):
    """Custom type ibmvPortCfgInFlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvPortCfgInFlt_Type.__name__ = "Integer32"
_IbmvPortCfgInFlt_Object = MibTableColumn
ibmvPortCfgInFlt = _IbmvPortCfgInFlt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 9),
    _IbmvPortCfgInFlt_Type()
)
ibmvPortCfgInFlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgInFlt.setStatus("mandatory")
_IbmvPortCfgInFltNum_Type = Integer32
_IbmvPortCfgInFltNum_Object = MibTableColumn
ibmvPortCfgInFltNum = _IbmvPortCfgInFltNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 10),
    _IbmvPortCfgInFltNum_Type()
)
ibmvPortCfgInFltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgInFltNum.setStatus("mandatory")


class _IbmvPortCfgOutFlt_Type(Integer32):
    """Custom type ibmvPortCfgOutFlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmvPortCfgOutFlt_Type.__name__ = "Integer32"
_IbmvPortCfgOutFlt_Object = MibTableColumn
ibmvPortCfgOutFlt = _IbmvPortCfgOutFlt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 11),
    _IbmvPortCfgOutFlt_Type()
)
ibmvPortCfgOutFlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgOutFlt.setStatus("mandatory")
_IbmvPortCfgOutFltNum_Type = Integer32
_IbmvPortCfgOutFltNum_Object = MibTableColumn
ibmvPortCfgOutFltNum = _IbmvPortCfgOutFltNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 1, 1, 12),
    _IbmvPortCfgOutFltNum_Type()
)
ibmvPortCfgOutFltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvPortCfgOutFltNum.setStatus("mandatory")
_IbmvFltTable_Object = MibTable
ibmvFltTable = _IbmvFltTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2)
)
if mibBuilder.loadTexts:
    ibmvFltTable.setStatus("mandatory")
_IbmvFltEntry_Object = MibTableRow
ibmvFltEntry = _IbmvFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1)
)
ibmvFltEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvFltIfIndex"),
    (0, "IBM6611-MIB", "ibmvFltNo"),
)
if mibBuilder.loadTexts:
    ibmvFltEntry.setStatus("mandatory")
_IbmvFltIfIndex_Type = Integer32
_IbmvFltIfIndex_Object = MibTableColumn
ibmvFltIfIndex = _IbmvFltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 1),
    _IbmvFltIfIndex_Type()
)
ibmvFltIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltIfIndex.setStatus("mandatory")
_IbmvFltNo_Type = Integer32
_IbmvFltNo_Object = MibTableColumn
ibmvFltNo = _IbmvFltNo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 2),
    _IbmvFltNo_Type()
)
ibmvFltNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltNo.setStatus("mandatory")


class _IbmvFltMode_Type(Integer32):
    """Custom type ibmvFltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_IbmvFltMode_Type.__name__ = "Integer32"
_IbmvFltMode_Object = MibTableColumn
ibmvFltMode = _IbmvFltMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 3),
    _IbmvFltMode_Type()
)
ibmvFltMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltMode.setStatus("mandatory")


class _IbmvFltValue_Type(OctetString):
    """Custom type ibmvFltValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_IbmvFltValue_Type.__name__ = "OctetString"
_IbmvFltValue_Object = MibTableColumn
ibmvFltValue = _IbmvFltValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 4),
    _IbmvFltValue_Type()
)
ibmvFltValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltValue.setStatus("mandatory")


class _IbmvFltMask_Type(OctetString):
    """Custom type ibmvFltMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_IbmvFltMask_Type.__name__ = "OctetString"
_IbmvFltMask_Object = MibTableColumn
ibmvFltMask = _IbmvFltMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 5),
    _IbmvFltMask_Type()
)
ibmvFltMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltMask.setStatus("mandatory")


class _IbmvFltType_Type(Integer32):
    """Custom type ibmvFltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IbmvFltType_Type.__name__ = "Integer32"
_IbmvFltType_Object = MibTableColumn
ibmvFltType = _IbmvFltType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 6),
    _IbmvFltType_Type()
)
ibmvFltType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltType.setStatus("mandatory")


class _IbmvFltHCCompare_Type(Integer32):
    """Custom type ibmvFltHCCompare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("greater-than", 5),
          ("greater-than-equal", 4),
          ("less-than", 1),
          ("less-than-equal", 2),
          ("na", 6))
    )


_IbmvFltHCCompare_Type.__name__ = "Integer32"
_IbmvFltHCCompare_Object = MibTableColumn
ibmvFltHCCompare = _IbmvFltHCCompare_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 7),
    _IbmvFltHCCompare_Type()
)
ibmvFltHCCompare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltHCCompare.setStatus("mandatory")
_IbmvFltUses_Type = Counter32
_IbmvFltUses_Object = MibTableColumn
ibmvFltUses = _IbmvFltUses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 2, 1, 8),
    _IbmvFltUses_Type()
)
ibmvFltUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvFltUses.setStatus("mandatory")
_IbmvifNumber_Type = Integer32
_IbmvifNumber_Object = MibScalar
ibmvifNumber = _IbmvifNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 3),
    _IbmvifNumber_Type()
)
ibmvifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifNumber.setStatus("mandatory")
_IbmvifTable_Object = MibTable
ibmvifTable = _IbmvifTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4)
)
if mibBuilder.loadTexts:
    ibmvifTable.setStatus("mandatory")
_IbmvifEntry_Object = MibTableRow
ibmvifEntry = _IbmvifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1)
)
ibmvifEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmvifSlot"),
    (0, "IBM6611-MIB", "ibmvifPort"),
)
if mibBuilder.loadTexts:
    ibmvifEntry.setStatus("mandatory")


class _IbmvifSlot_Type(Integer32):
    """Custom type ibmvifSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IbmvifSlot_Type.__name__ = "Integer32"
_IbmvifSlot_Object = MibTableColumn
ibmvifSlot = _IbmvifSlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 1),
    _IbmvifSlot_Type()
)
ibmvifSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifSlot.setStatus("mandatory")


class _IbmvifPort_Type(Integer32):
    """Custom type ibmvifPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IbmvifPort_Type.__name__ = "Integer32"
_IbmvifPort_Object = MibTableColumn
ibmvifPort = _IbmvifPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 2),
    _IbmvifPort_Type()
)
ibmvifPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifPort.setStatus("mandatory")
_IbmvifDescr_Type = DisplayString
_IbmvifDescr_Object = MibTableColumn
ibmvifDescr = _IbmvifDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 3),
    _IbmvifDescr_Type()
)
ibmvifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifDescr.setStatus("mandatory")
_IbmvifAddress_Type = OctetString
_IbmvifAddress_Object = MibTableColumn
ibmvifAddress = _IbmvifAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 4),
    _IbmvifAddress_Type()
)
ibmvifAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifAddress.setStatus("mandatory")
_IbmvifInPkts_Type = Counter32
_IbmvifInPkts_Object = MibTableColumn
ibmvifInPkts = _IbmvifInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 5),
    _IbmvifInPkts_Type()
)
ibmvifInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifInPkts.setStatus("mandatory")
_IbmvifInErrs_Type = Counter32
_IbmvifInErrs_Object = MibTableColumn
ibmvifInErrs = _IbmvifInErrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 6),
    _IbmvifInErrs_Type()
)
ibmvifInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifInErrs.setStatus("mandatory")
_IbmvifOutPkts_Type = Counter32
_IbmvifOutPkts_Object = MibTableColumn
ibmvifOutPkts = _IbmvifOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 7),
    _IbmvifOutPkts_Type()
)
ibmvifOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifOutPkts.setStatus("mandatory")
_IbmvifOutErrs_Type = Counter32
_IbmvifOutErrs_Object = MibTableColumn
ibmvifOutErrs = _IbmvifOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 18, 7, 4, 1, 8),
    _IbmvifOutErrs_Type()
)
ibmvifOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmvifOutErrs.setStatus("mandatory")
_Ibminterfaces_ObjectIdentity = ObjectIdentity
ibminterfaces = _Ibminterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19)
)
_Ibmipext_ObjectIdentity = ObjectIdentity
ibmipext = _Ibmipext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1)
)
_IbmipPtyQueueEnableTable_Object = MibTable
ibmipPtyQueueEnableTable = _IbmipPtyQueueEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    ibmipPtyQueueEnableTable.setStatus("mandatory")
_IbmipPtyQueueEnableEntry_Object = MibTableRow
ibmipPtyQueueEnableEntry = _IbmipPtyQueueEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 1, 1)
)
ibmipPtyQueueEnableEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipPtyQueueEnableIfIndex"),
)
if mibBuilder.loadTexts:
    ibmipPtyQueueEnableEntry.setStatus("mandatory")


class _IbmipPtyQueueEnableIfIndex_Type(Integer32):
    """Custom type ibmipPtyQueueEnableIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmipPtyQueueEnableIfIndex_Type.__name__ = "Integer32"
_IbmipPtyQueueEnableIfIndex_Object = MibTableColumn
ibmipPtyQueueEnableIfIndex = _IbmipPtyQueueEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 1, 1, 1),
    _IbmipPtyQueueEnableIfIndex_Type()
)
ibmipPtyQueueEnableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPtyQueueEnableIfIndex.setStatus("mandatory")


class _IbmipPtyQueueEnable_Type(Integer32):
    """Custom type ibmipPtyQueueEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmipPtyQueueEnable_Type.__name__ = "Integer32"
_IbmipPtyQueueEnable_Object = MibTableColumn
ibmipPtyQueueEnable = _IbmipPtyQueueEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 1, 1, 2),
    _IbmipPtyQueueEnable_Type()
)
ibmipPtyQueueEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPtyQueueEnable.setStatus("mandatory")


class _IbmipPtyQueueDefault_Type(Integer32):
    """Custom type ibmipPtyQueueDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_IbmipPtyQueueDefault_Type.__name__ = "Integer32"
_IbmipPtyQueueDefault_Object = MibTableColumn
ibmipPtyQueueDefault = _IbmipPtyQueueDefault_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 1, 1, 3),
    _IbmipPtyQueueDefault_Type()
)
ibmipPtyQueueDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPtyQueueDefault.setStatus("mandatory")
_IbmipPtyQueueTable_Object = MibTable
ibmipPtyQueueTable = _IbmipPtyQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 2)
)
if mibBuilder.loadTexts:
    ibmipPtyQueueTable.setStatus("mandatory")
_IbmipPtyQueueEntry_Object = MibTableRow
ibmipPtyQueueEntry = _IbmipPtyQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 2, 1)
)
ibmipPtyQueueEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipPtyQueueIfIndex"),
    (0, "IBM6611-MIB", "ibmipPtyQueuePort"),
    (0, "IBM6611-MIB", "ibmipPtyQueueType"),
)
if mibBuilder.loadTexts:
    ibmipPtyQueueEntry.setStatus("mandatory")


class _IbmipPtyQueueIfIndex_Type(Integer32):
    """Custom type ibmipPtyQueueIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmipPtyQueueIfIndex_Type.__name__ = "Integer32"
_IbmipPtyQueueIfIndex_Object = MibTableColumn
ibmipPtyQueueIfIndex = _IbmipPtyQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 2, 1, 1),
    _IbmipPtyQueueIfIndex_Type()
)
ibmipPtyQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPtyQueueIfIndex.setStatus("mandatory")


class _IbmipPtyQueuePort_Type(Integer32):
    """Custom type ibmipPtyQueuePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmipPtyQueuePort_Type.__name__ = "Integer32"
_IbmipPtyQueuePort_Object = MibTableColumn
ibmipPtyQueuePort = _IbmipPtyQueuePort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 2, 1, 2),
    _IbmipPtyQueuePort_Type()
)
ibmipPtyQueuePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPtyQueuePort.setStatus("mandatory")


class _IbmipPtyQueueType_Type(Integer32):
    """Custom type ibmipPtyQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_IbmipPtyQueueType_Type.__name__ = "Integer32"
_IbmipPtyQueueType_Object = MibTableColumn
ibmipPtyQueueType = _IbmipPtyQueueType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 2, 1, 3),
    _IbmipPtyQueueType_Type()
)
ibmipPtyQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPtyQueueType.setStatus("mandatory")


class _IbmipPtyQueueNumber_Type(Integer32):
    """Custom type ibmipPtyQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_IbmipPtyQueueNumber_Type.__name__ = "Integer32"
_IbmipPtyQueueNumber_Object = MibTableColumn
ibmipPtyQueueNumber = _IbmipPtyQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 2, 1, 4),
    _IbmipPtyQueueNumber_Type()
)
ibmipPtyQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPtyQueueNumber.setStatus("mandatory")
_IbmipFilterTable_Object = MibTable
ibmipFilterTable = _IbmipFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3)
)
if mibBuilder.loadTexts:
    ibmipFilterTable.setStatus("mandatory")
_IbmipFilterEntry_Object = MibTableRow
ibmipFilterEntry = _IbmipFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1)
)
ibmipFilterEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipFilterIfIndex"),
    (0, "IBM6611-MIB", "ibmipFilterId"),
)
if mibBuilder.loadTexts:
    ibmipFilterEntry.setStatus("mandatory")


class _IbmipFilterIfIndex_Type(Integer32):
    """Custom type ibmipFilterIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmipFilterIfIndex_Type.__name__ = "Integer32"
_IbmipFilterIfIndex_Object = MibTableColumn
ibmipFilterIfIndex = _IbmipFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 1),
    _IbmipFilterIfIndex_Type()
)
ibmipFilterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterIfIndex.setStatus("mandatory")


class _IbmipFilterId_Type(Integer32):
    """Custom type ibmipFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_IbmipFilterId_Type.__name__ = "Integer32"
_IbmipFilterId_Object = MibTableColumn
ibmipFilterId = _IbmipFilterId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 2),
    _IbmipFilterId_Type()
)
ibmipFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterId.setStatus("mandatory")


class _IbmipFilterScope_Type(Integer32):
    """Custom type ibmipFilterScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 2),
          ("system", 1))
    )


_IbmipFilterScope_Type.__name__ = "Integer32"
_IbmipFilterScope_Object = MibTableColumn
ibmipFilterScope = _IbmipFilterScope_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 3),
    _IbmipFilterScope_Type()
)
ibmipFilterScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterScope.setStatus("mandatory")


class _IbmipFilterType_Type(Integer32):
    """Custom type ibmipFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("singular", 1))
    )


_IbmipFilterType_Type.__name__ = "Integer32"
_IbmipFilterType_Object = MibTableColumn
ibmipFilterType = _IbmipFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 4),
    _IbmipFilterType_Type()
)
ibmipFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterType.setStatus("mandatory")


class _IbmipPermitDeny_Type(Integer32):
    """Custom type ibmipPermitDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IbmipPermitDeny_Type.__name__ = "Integer32"
_IbmipPermitDeny_Object = MibTableColumn
ibmipPermitDeny = _IbmipPermitDeny_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 5),
    _IbmipPermitDeny_Type()
)
ibmipPermitDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipPermitDeny.setStatus("mandatory")
_IbmipFilterAddr1_Type = IpAddress
_IbmipFilterAddr1_Object = MibTableColumn
ibmipFilterAddr1 = _IbmipFilterAddr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 6),
    _IbmipFilterAddr1_Type()
)
ibmipFilterAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterAddr1.setStatus("mandatory")
_IbmipFilterMask1_Type = IpAddress
_IbmipFilterMask1_Object = MibTableColumn
ibmipFilterMask1 = _IbmipFilterMask1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 7),
    _IbmipFilterMask1_Type()
)
ibmipFilterMask1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterMask1.setStatus("mandatory")
_IbmipFilterAddr2_Type = IpAddress
_IbmipFilterAddr2_Object = MibTableColumn
ibmipFilterAddr2 = _IbmipFilterAddr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 8),
    _IbmipFilterAddr2_Type()
)
ibmipFilterAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterAddr2.setStatus("mandatory")
_IbmipFilterMask2_Type = IpAddress
_IbmipFilterMask2_Object = MibTableColumn
ibmipFilterMask2 = _IbmipFilterMask2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 3, 1, 9),
    _IbmipFilterMask2_Type()
)
ibmipFilterMask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterMask2.setStatus("mandatory")
_IbmipFilterExtTable_Object = MibTable
ibmipFilterExtTable = _IbmipFilterExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 4)
)
if mibBuilder.loadTexts:
    ibmipFilterExtTable.setStatus("mandatory")
_IbmipFilterExtEntry_Object = MibTableRow
ibmipFilterExtEntry = _IbmipFilterExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 4, 1)
)
ibmipFilterExtEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmipFilterExtIfIndex"),
    (0, "IBM6611-MIB", "ibmipFilterExtFilterId"),
    (0, "IBM6611-MIB", "ibmipFilterExtValue"),
    (0, "IBM6611-MIB", "ibmipFilterExtProtocol"),
)
if mibBuilder.loadTexts:
    ibmipFilterExtEntry.setStatus("mandatory")


class _IbmipFilterExtIfIndex_Type(Integer32):
    """Custom type ibmipFilterExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmipFilterExtIfIndex_Type.__name__ = "Integer32"
_IbmipFilterExtIfIndex_Object = MibTableColumn
ibmipFilterExtIfIndex = _IbmipFilterExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 4, 1, 1),
    _IbmipFilterExtIfIndex_Type()
)
ibmipFilterExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterExtIfIndex.setStatus("mandatory")


class _IbmipFilterExtFilterId_Type(Integer32):
    """Custom type ibmipFilterExtFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_IbmipFilterExtFilterId_Type.__name__ = "Integer32"
_IbmipFilterExtFilterId_Object = MibTableColumn
ibmipFilterExtFilterId = _IbmipFilterExtFilterId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 4, 1, 2),
    _IbmipFilterExtFilterId_Type()
)
ibmipFilterExtFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterExtFilterId.setStatus("mandatory")


class _IbmipFilterExtValue_Type(Integer32):
    """Custom type ibmipFilterExtValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmipFilterExtValue_Type.__name__ = "Integer32"
_IbmipFilterExtValue_Object = MibTableColumn
ibmipFilterExtValue = _IbmipFilterExtValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 4, 1, 3),
    _IbmipFilterExtValue_Type()
)
ibmipFilterExtValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterExtValue.setStatus("mandatory")


class _IbmipFilterExtProtocol_Type(Integer32):
    """Custom type ibmipFilterExtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tcpudp", 2))
    )


_IbmipFilterExtProtocol_Type.__name__ = "Integer32"
_IbmipFilterExtProtocol_Object = MibTableColumn
ibmipFilterExtProtocol = _IbmipFilterExtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 1, 4, 1, 4),
    _IbmipFilterExtProtocol_Type()
)
ibmipFilterExtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmipFilterExtProtocol.setStatus("mandatory")
_Ibmptyqueue_ObjectIdentity = ObjectIdentity
ibmptyqueue = _Ibmptyqueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2)
)
_IbmPtyQueueingTable_Object = MibTable
ibmPtyQueueingTable = _IbmPtyQueueingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2, 1)
)
if mibBuilder.loadTexts:
    ibmPtyQueueingTable.setStatus("mandatory")
_IbmPtyQueueingEntry_Object = MibTableRow
ibmPtyQueueingEntry = _IbmPtyQueueingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2, 1, 1)
)
ibmPtyQueueingEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmPtyQueueingIfIndex"),
    (0, "IBM6611-MIB", "ibmPtyQueueingQnum"),
)
if mibBuilder.loadTexts:
    ibmPtyQueueingEntry.setStatus("mandatory")


class _IbmPtyQueueingIfIndex_Type(Integer32):
    """Custom type ibmPtyQueueingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmPtyQueueingIfIndex_Type.__name__ = "Integer32"
_IbmPtyQueueingIfIndex_Object = MibTableColumn
ibmPtyQueueingIfIndex = _IbmPtyQueueingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2, 1, 1, 1),
    _IbmPtyQueueingIfIndex_Type()
)
ibmPtyQueueingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmPtyQueueingIfIndex.setStatus("mandatory")


class _IbmPtyQueueingQnum_Type(Integer32):
    """Custom type ibmPtyQueueingQnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_IbmPtyQueueingQnum_Type.__name__ = "Integer32"
_IbmPtyQueueingQnum_Object = MibTableColumn
ibmPtyQueueingQnum = _IbmPtyQueueingQnum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2, 1, 1, 2),
    _IbmPtyQueueingQnum_Type()
)
ibmPtyQueueingQnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmPtyQueueingQnum.setStatus("mandatory")


class _IbmPtyQueueingLBA_Type(Integer32):
    """Custom type ibmPtyQueueingLBA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmPtyQueueingLBA_Type.__name__ = "Integer32"
_IbmPtyQueueingLBA_Object = MibTableColumn
ibmPtyQueueingLBA = _IbmPtyQueueingLBA_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2, 1, 1, 3),
    _IbmPtyQueueingLBA_Type()
)
ibmPtyQueueingLBA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmPtyQueueingLBA.setStatus("mandatory")
_IbmPtyQueueingQBR_Type = Integer32
_IbmPtyQueueingQBR_Object = MibTableColumn
ibmPtyQueueingQBR = _IbmPtyQueueingQBR_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2, 1, 1, 4),
    _IbmPtyQueueingQBR_Type()
)
ibmPtyQueueingQBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmPtyQueueingQBR.setStatus("mandatory")
_IbmPtyQueueingDiscards_Type = Counter32
_IbmPtyQueueingDiscards_Object = MibTableColumn
ibmPtyQueueingDiscards = _IbmPtyQueueingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 2, 1, 1, 5),
    _IbmPtyQueueingDiscards_Type()
)
ibmPtyQueueingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmPtyQueueingDiscards.setStatus("mandatory")
_IbmTG_ObjectIdentity = ObjectIdentity
ibmTG = _IbmTG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3)
)
_IbmTGTable_Object = MibTable
ibmTGTable = _IbmTGTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3, 1)
)
if mibBuilder.loadTexts:
    ibmTGTable.setStatus("mandatory")
_IbmTGEntry_Object = MibTableRow
ibmTGEntry = _IbmTGEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3, 1, 1)
)
ibmTGEntry.setIndexNames(
    (0, "IBM6611-MIB", "ibmTGProtocol"),
    (0, "IBM6611-MIB", "ibmTGIfIndex"),
)
if mibBuilder.loadTexts:
    ibmTGEntry.setStatus("mandatory")


class _IbmTGProtocol_Type(Integer32):
    """Custom type ibmTGProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2048
        )
    )
    namedValues = NamedValues(
        ("ip", 2048)
    )


_IbmTGProtocol_Type.__name__ = "Integer32"
_IbmTGProtocol_Object = MibTableColumn
ibmTGProtocol = _IbmTGProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3, 1, 1, 1),
    _IbmTGProtocol_Type()
)
ibmTGProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTGProtocol.setStatus("mandatory")


class _IbmTGIfIndex_Type(Integer32):
    """Custom type ibmTGIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmTGIfIndex_Type.__name__ = "Integer32"
_IbmTGIfIndex_Object = MibTableColumn
ibmTGIfIndex = _IbmTGIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3, 1, 1, 2),
    _IbmTGIfIndex_Type()
)
ibmTGIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTGIfIndex.setStatus("mandatory")


class _IbmTGEnable_Type(Integer32):
    """Custom type ibmTGEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IbmTGEnable_Type.__name__ = "Integer32"
_IbmTGEnable_Object = MibTableColumn
ibmTGEnable = _IbmTGEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3, 1, 1, 3),
    _IbmTGEnable_Type()
)
ibmTGEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTGEnable.setStatus("mandatory")


class _IbmTGGroupName_Type(DisplayString):
    """Custom type ibmTGGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmTGGroupName_Type.__name__ = "DisplayString"
_IbmTGGroupName_Object = MibTableColumn
ibmTGGroupName = _IbmTGGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3, 1, 1, 4),
    _IbmTGGroupName_Type()
)
ibmTGGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTGGroupName.setStatus("mandatory")
_IbmTGSwitchOuts_Type = Counter32
_IbmTGSwitchOuts_Object = MibTableColumn
ibmTGSwitchOuts = _IbmTGSwitchOuts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 19, 3, 1, 1, 5),
    _IbmTGSwitchOuts_Type()
)
ibmTGSwitchOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmTGSwitchOuts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM6611-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm6611": ibm6611,
       "ibmSubagents": ibmSubagents,
       "ibmChipSets": ibmChipSets,
       "ibmChipSetIntel": ibmChipSetIntel,
       "ibmChipSetIntel82596B": ibmChipSetIntel82596B,
       "ibmChipSetIBM": ibmChipSetIBM,
       "ibmChipSetIBM8025A": ibmChipSetIBM8025A,
       "ibmChipSetIBM8025B": ibmChipSetIBM8025B,
       "ibmChipSetSignetics": ibmChipSetSignetics,
       "ibmChipSetSigneticsSCN68562": ibmChipSetSigneticsSCN68562,
       "ibmDSUs": ibmDSUs,
       "cylink": cylink,
       "cylinkStatusTable": cylinkStatusTable,
       "cylinkStatusEntry": cylinkStatusEntry,
       "cylinkIndex": cylinkIndex,
       "cylinkLinkState": cylinkLinkState,
       "cylinkLoopback": cylinkLoopback,
       "cylinkQRSS": cylinkQRSS,
       "cylinkConfigTable": cylinkConfigTable,
       "cylinkConfigEntry": cylinkConfigEntry,
       "cylinkConfigIndex": cylinkConfigIndex,
       "cylinkSerialNumber": cylinkSerialNumber,
       "cylinkSoftwareVersion": cylinkSoftwareVersion,
       "cylinkDTEFraming": cylinkDTEFraming,
       "cylinkNetworkFraming": cylinkNetworkFraming,
       "cylinkDTEDS1Mode": cylinkDTEDS1Mode,
       "cylinkNetworkDS1Mode": cylinkNetworkDS1Mode,
       "cylinkOnesResponsibility": cylinkOnesResponsibility,
       "cylinkOnesControl": cylinkOnesControl,
       "cylinkZeroProtection": cylinkZeroProtection,
       "cylinkClockSource": cylinkClockSource,
       "cylinkClockFrequency": cylinkClockFrequency,
       "cylinkClockBackup": cylinkClockBackup,
       "cylinkDIUFrequency": cylinkDIUFrequency,
       "cylinkDIUTiming": cylinkDIUTiming,
       "cylinkDialoutCapability": cylinkDialoutCapability,
       "cylinkDialoutHoldoff": cylinkDialoutHoldoff,
       "cylinkPrimaryPhone": cylinkPrimaryPhone,
       "cylinkSecondaryPhone": cylinkSecondaryPhone,
       "cylinkAlarmRepeatTime": cylinkAlarmRepeatTime,
       "cylinkESThreshold": cylinkESThreshold,
       "cylinkSecondaryContact": cylinkSecondaryContact,
       "ibmsystem": ibmsystem,
       "ibmMainProcessorLoadTable": ibmMainProcessorLoadTable,
       "ibmMainProcessorLoadEntry": ibmMainProcessorLoadEntry,
       "ibmMainProcessorLoadIndex": ibmMainProcessorLoadIndex,
       "ibmMainProcessorLoad": ibmMainProcessorLoad,
       "ibmswvpd": ibmswvpd,
       "swVpdTable": swVpdTable,
       "swVpdEntry": swVpdEntry,
       "swvpdIndex": swvpdIndex,
       "swvpdName": swvpdName,
       "swvpdPtfName": swvpdPtfName,
       "swvpdVerId": swvpdVerId,
       "swvpdRelId": swvpdRelId,
       "swvpdModId": swvpdModId,
       "swvpdFixId": swvpdFixId,
       "swvpdState": swvpdState,
       "swvpdAction": swvpdAction,
       "swvpdPath": swvpdPath,
       "swvpdDateTime": swvpdDateTime,
       "ibmmaint": ibmmaint,
       "ibmmaintShutdown": ibmmaintShutdown,
       "ibmsysInfo": ibmsysInfo,
       "ibmsysMBUFs": ibmsysMBUFs,
       "ibmsysMBUFsInUses": ibmsysMBUFsInUses,
       "ibmsysMBUFsKbytes": ibmsysMBUFsKbytes,
       "ibmsysMBUFsPercents": ibmsysMBUFsPercents,
       "ibmsysMBUFsDeniedRequests": ibmsysMBUFsDeniedRequests,
       "ibmsysMBUFsDelayedRequests": ibmsysMBUFsDelayedRequests,
       "ibmsysPageSpace": ibmsysPageSpace,
       "ibmsysPageSpaceTotal": ibmsysPageSpaceTotal,
       "ibmsysPageSpaceInUse": ibmsysPageSpaceInUse,
       "ibmsysRealMem": ibmsysRealMem,
       "ibmsysRealMemSize": ibmsysRealMemSize,
       "ibmsysRealMemInUse": ibmsysRealMemInUse,
       "ibmsysRealMemFree": ibmsysRealMemFree,
       "ibmicmp": ibmicmp,
       "ibmsnmp": ibmsnmp,
       "ibmTrapNum": ibmTrapNum,
       "ibmTrapThrottleCount": ibmTrapThrottleCount,
       "ibmTrapThrottleId": ibmTrapThrottleId,
       "ibmTrapThrottleTime": ibmTrapThrottleTime,
       "ibmbridge": ibmbridge,
       "ibmbridgeMACAddressFilters": ibmbridgeMACAddressFilters,
       "ibmmacAddrFilterInfoTable": ibmmacAddrFilterInfoTable,
       "ibmmacAddrFilterInfoEntry": ibmmacAddrFilterInfoEntry,
       "ibmmacAddrFilterIfIndex": ibmmacAddrFilterIfIndex,
       "ibmmacAddrFilterInBcastType": ibmmacAddrFilterInBcastType,
       "ibmmacAddrFilterOutBcastType": ibmmacAddrFilterOutBcastType,
       "ibmmacAddrFilterInFilterType": ibmmacAddrFilterInFilterType,
       "ibmmacAddrFilterOutFilterType": ibmmacAddrFilterOutFilterType,
       "ibmmacAddrFilterInNotForwarded": ibmmacAddrFilterInNotForwarded,
       "ibmmacAddrFilterOutNotForwarded": ibmmacAddrFilterOutNotForwarded,
       "ibmmacAddrFilterType": ibmmacAddrFilterType,
       "ibmmacAddrFilterInTable": ibmmacAddrFilterInTable,
       "ibmmacAddrFilterInEntry": ibmmacAddrFilterInEntry,
       "ibmmacAddrFilterInIfIndex": ibmmacAddrFilterInIfIndex,
       "ibmmacAddrFilterInSrcAddress": ibmmacAddrFilterInSrcAddress,
       "ibmmacAddrFilterInSrcMask": ibmmacAddrFilterInSrcMask,
       "ibmmacAddrFilterInDestAddress": ibmmacAddrFilterInDestAddress,
       "ibmmacAddrFilterInDestMask": ibmmacAddrFilterInDestMask,
       "ibmmacAddrFilterInType": ibmmacAddrFilterInType,
       "ibmmacAddrFilterOutTable": ibmmacAddrFilterOutTable,
       "ibmmacAddrFilterOutEntry": ibmmacAddrFilterOutEntry,
       "ibmmacAddrFilterOutIfIndex": ibmmacAddrFilterOutIfIndex,
       "ibmmacAddrFilterOutSrcAddress": ibmmacAddrFilterOutSrcAddress,
       "ibmmacAddrFilterOutSrcMask": ibmmacAddrFilterOutSrcMask,
       "ibmmacAddrFilterOutDestAddress": ibmmacAddrFilterOutDestAddress,
       "ibmmacAddrFilterOutDestMask": ibmmacAddrFilterOutDestMask,
       "ibmmacAddrFilterOutType": ibmmacAddrFilterOutType,
       "ibmbridgeSAPFilters": ibmbridgeSAPFilters,
       "ibmsapFilterInfoTable": ibmsapFilterInfoTable,
       "ibmsapFilterInfoEntry": ibmsapFilterInfoEntry,
       "ibmsapFilterIfIndex": ibmsapFilterIfIndex,
       "ibmsapFilterInBcastType": ibmsapFilterInBcastType,
       "ibmsapFilterOutBcastType": ibmsapFilterOutBcastType,
       "ibmsapFilterIn": ibmsapFilterIn,
       "ibmsapFilterOut": ibmsapFilterOut,
       "ibmsapFilterInNotForwarded": ibmsapFilterInNotForwarded,
       "ibmsapFilterOutNotForwarded": ibmsapFilterOutNotForwarded,
       "ibmsapFilterType": ibmsapFilterType,
       "ibmbridgeSNAPFilters": ibmbridgeSNAPFilters,
       "ibmsnapFilterInfoTable": ibmsnapFilterInfoTable,
       "ibmsnapFilterInfoEntry": ibmsnapFilterInfoEntry,
       "ibmsnapFilterIfIndex": ibmsnapFilterIfIndex,
       "ibmsnapFilterInFilterType": ibmsnapFilterInFilterType,
       "ibmsnapFilterOutFilterType": ibmsnapFilterOutFilterType,
       "ibmsnapFilterInNotForwarded": ibmsnapFilterInNotForwarded,
       "ibmsnapFilterOutNotForwarded": ibmsnapFilterOutNotForwarded,
       "ibmsnapFilterType": ibmsnapFilterType,
       "ibmsnapFilterInTable": ibmsnapFilterInTable,
       "ibmsnapFilterInEntry": ibmsnapFilterInEntry,
       "ibmsnapFilterInIfIndex": ibmsnapFilterInIfIndex,
       "ibmsnapFilterInValue": ibmsnapFilterInValue,
       "ibmsnapFilterInMask": ibmsnapFilterInMask,
       "ibmsnapFilterInType": ibmsnapFilterInType,
       "ibmsnapFilterOutTable": ibmsnapFilterOutTable,
       "ibmsnapFilterOutEntry": ibmsnapFilterOutEntry,
       "ibmsnapFilterOutIfIndex": ibmsnapFilterOutIfIndex,
       "ibmsnapFilterOutValue": ibmsnapFilterOutValue,
       "ibmsnapFilterOutMask": ibmsnapFilterOutMask,
       "ibmsnapFilterOutType": ibmsnapFilterOutType,
       "ibmbridgeRingFilters": ibmbridgeRingFilters,
       "ibmringFilterInfoTable": ibmringFilterInfoTable,
       "ibmringFilterInfoEntry": ibmringFilterInfoEntry,
       "ibmringFilterIfIndex": ibmringFilterIfIndex,
       "ibmringFilterInBcastType": ibmringFilterInBcastType,
       "ibmringFilterOutBcastType": ibmringFilterOutBcastType,
       "ibmringFilterInFilterType": ibmringFilterInFilterType,
       "ibmringFilterOutFilterType": ibmringFilterOutFilterType,
       "ibmringFilterInNotForwarded": ibmringFilterInNotForwarded,
       "ibmringFilterOutNotForwarded": ibmringFilterOutNotForwarded,
       "ibmringFilterInTable": ibmringFilterInTable,
       "ibmringFilterInEntry": ibmringFilterInEntry,
       "ibmringFilterInIfIndex": ibmringFilterInIfIndex,
       "ibmringFilterInNumber": ibmringFilterInNumber,
       "ibmringFilterInMask": ibmringFilterInMask,
       "ibmringFilterOutTable": ibmringFilterOutTable,
       "ibmringFilterOutEntry": ibmringFilterOutEntry,
       "ibmringFilterOutIfIndex": ibmringFilterOutIfIndex,
       "ibmringFilterOutNumber": ibmringFilterOutNumber,
       "ibmringFilterOutMask": ibmringFilterOutMask,
       "ibmbridgeHopCountFilters": ibmbridgeHopCountFilters,
       "ibmhopCountFilterInfoTable": ibmhopCountFilterInfoTable,
       "ibmhopCountFilterInfoEntry": ibmhopCountFilterInfoEntry,
       "ibmhopCountFilterIfIndex": ibmhopCountFilterIfIndex,
       "ibmhopCountFilterBcastType": ibmhopCountFilterBcastType,
       "ibmhopCountFilterCount": ibmhopCountFilterCount,
       "ibmbridgeWindowFilters": ibmbridgeWindowFilters,
       "ibmwindowFilterInfoTable": ibmwindowFilterInfoTable,
       "ibmwindowFilterInfoEntry": ibmwindowFilterInfoEntry,
       "ibmwindowFilterIfIndex": ibmwindowFilterIfIndex,
       "ibmwindowFilterInBcastType": ibmwindowFilterInBcastType,
       "ibmwindowFilterOutBcastType": ibmwindowFilterOutBcastType,
       "ibmwindowFilterInFilterType": ibmwindowFilterInFilterType,
       "ibmwindowFilterOutFilterType": ibmwindowFilterOutFilterType,
       "ibmwindowFilterInNotForwarded": ibmwindowFilterInNotForwarded,
       "ibmwindowFilterOutNotForwarded": ibmwindowFilterOutNotForwarded,
       "ibmwindowFilterType": ibmwindowFilterType,
       "ibmwindowFilterInTable": ibmwindowFilterInTable,
       "ibmwindowFilterInEntry": ibmwindowFilterInEntry,
       "ibmwindowFilterInIfIndex": ibmwindowFilterInIfIndex,
       "ibmwindowFilterInContents": ibmwindowFilterInContents,
       "ibmwindowFilterInMaskString": ibmwindowFilterInMaskString,
       "ibmwindowFilterInOffsetStart": ibmwindowFilterInOffsetStart,
       "ibmwindowFilterInNumBytes": ibmwindowFilterInNumBytes,
       "ibmwindowFilterInOffset": ibmwindowFilterInOffset,
       "ibmwindowFilterInId": ibmwindowFilterInId,
       "ibmwindowFilterInType": ibmwindowFilterInType,
       "ibmwindowFilterOutTable": ibmwindowFilterOutTable,
       "ibmwindowFilterOutEntry": ibmwindowFilterOutEntry,
       "ibmwindowFilterOutIfIndex": ibmwindowFilterOutIfIndex,
       "ibmwindowFilterOutContents": ibmwindowFilterOutContents,
       "ibmwindowFilterOutMaskString": ibmwindowFilterOutMaskString,
       "ibmwindowFilterOutOffsetStart": ibmwindowFilterOutOffsetStart,
       "ibmwindowFilterOutNumBytes": ibmwindowFilterOutNumBytes,
       "ibmwindowFilterOutOffset": ibmwindowFilterOutOffset,
       "ibmwindowFilterOutId": ibmwindowFilterOutId,
       "ibmwindowFilterOutType": ibmwindowFilterOutType,
       "ibmbridgeFiltOrderTable": ibmbridgeFiltOrderTable,
       "ibmFiltOrderInTable": ibmFiltOrderInTable,
       "ibmFiltOrderInEntry": ibmFiltOrderInEntry,
       "ibmFiltOrderInIfIndex": ibmFiltOrderInIfIndex,
       "ibmFiltOrderInPriority": ibmFiltOrderInPriority,
       "ibmFiltOrderInName": ibmFiltOrderInName,
       "ibmFiltOrderInType": ibmFiltOrderInType,
       "ibmFiltOrderOutTable": ibmFiltOrderOutTable,
       "ibmFiltOrderOutEntry": ibmFiltOrderOutEntry,
       "ibmFiltOrderOutIfIndex": ibmFiltOrderOutIfIndex,
       "ibmFiltOrderOutPriority": ibmFiltOrderOutPriority,
       "ibmFiltOrderOutName": ibmFiltOrderOutName,
       "ibmFiltOrderOutType": ibmFiltOrderOutType,
       "ibmbridgeRIFFilters": ibmbridgeRIFFilters,
       "ibmRIFFilterInfoTable": ibmRIFFilterInfoTable,
       "ibmRIFFilterInfoEntry": ibmRIFFilterInfoEntry,
       "ibmRIFFilterIfIndex": ibmRIFFilterIfIndex,
       "ibmRIFFilterInBcastType": ibmRIFFilterInBcastType,
       "ibmRIFFilterOutBcastType": ibmRIFFilterOutBcastType,
       "ibmRIFFilterInFilterType": ibmRIFFilterInFilterType,
       "ibmRIFFilterOutFilterType": ibmRIFFilterOutFilterType,
       "ibmRIFFilterInNotForwarded": ibmRIFFilterInNotForwarded,
       "ibmRIFFilterOutNotForwarded": ibmRIFFilterOutNotForwarded,
       "ibmRIFFilterInTable": ibmRIFFilterInTable,
       "ibmRIFFilterInEntry": ibmRIFFilterInEntry,
       "ibmRIFFilterInIfIndex": ibmRIFFilterInIfIndex,
       "ibmRIFFilterInRingNumber": ibmRIFFilterInRingNumber,
       "ibmRIFFilterInRingMask": ibmRIFFilterInRingMask,
       "ibmRIFFilterInBridgeNumber": ibmRIFFilterInBridgeNumber,
       "ibmRIFFilterInBridgeMask": ibmRIFFilterInBridgeMask,
       "ibmRIFFilterInRouteDesignator": ibmRIFFilterInRouteDesignator,
       "ibmRIFFilterOutTable": ibmRIFFilterOutTable,
       "ibmRIFFilterOutEntry": ibmRIFFilterOutEntry,
       "ibmRIFFilterOutIfIndex": ibmRIFFilterOutIfIndex,
       "ibmRIFFilterOutRingNumber": ibmRIFFilterOutRingNumber,
       "ibmRIFFilterOutRingMask": ibmRIFFilterOutRingMask,
       "ibmRIFFilterOutBridgeNumber": ibmRIFFilterOutBridgeNumber,
       "ibmRIFFilterOutBridgeMask": ibmRIFFilterOutBridgeMask,
       "ibmRIFFilterOutRouteDesignator": ibmRIFFilterOutRouteDesignator,
       "ibmfr": ibmfr,
       "ibmfrDlcmiTable": ibmfrDlcmiTable,
       "ibmfrDlcmiEntry": ibmfrDlcmiEntry,
       "ibmfrDlcmiIfIndex": ibmfrDlcmiIfIndex,
       "ibmfrDlcmiState": ibmfrDlcmiState,
       "ibmfrDlcmiAddress": ibmfrDlcmiAddress,
       "ibmfrDlcmiAddressLen": ibmfrDlcmiAddressLen,
       "ibmfrDlcmiPollingInterval": ibmfrDlcmiPollingInterval,
       "ibmfrDlcmiFullEnquiryInterval": ibmfrDlcmiFullEnquiryInterval,
       "ibmfrDlcmiErrorThreshold": ibmfrDlcmiErrorThreshold,
       "ibmfrDlcmiMonitoredEvents": ibmfrDlcmiMonitoredEvents,
       "ibmfrDlcmiMaxSupportedVCs": ibmfrDlcmiMaxSupportedVCs,
       "ibmfrDlcmiMulticast": ibmfrDlcmiMulticast,
       "ibmfrCircuitTable": ibmfrCircuitTable,
       "ibmfrCircuitEntry": ibmfrCircuitEntry,
       "ibmfrCircuitIfIndex": ibmfrCircuitIfIndex,
       "ibmfrCircuitDlci": ibmfrCircuitDlci,
       "ibmfrCircuitState": ibmfrCircuitState,
       "ibmfrCircuitReceivedFECNs": ibmfrCircuitReceivedFECNs,
       "ibmfrCircuitReceivedBECNs": ibmfrCircuitReceivedBECNs,
       "ibmfrCircuitSentFrames": ibmfrCircuitSentFrames,
       "ibmfrCircuitSentOctets": ibmfrCircuitSentOctets,
       "ibmfrCircuitReceivedFrames": ibmfrCircuitReceivedFrames,
       "ibmfrCircuitReceivedOctets": ibmfrCircuitReceivedOctets,
       "ibmfrCircuitCreationTime": ibmfrCircuitCreationTime,
       "ibmfrCircuitLastTimeChange": ibmfrCircuitLastTimeChange,
       "ibmfrCircuitCommittedBurst": ibmfrCircuitCommittedBurst,
       "ibmfrCircuitExcessBurst": ibmfrCircuitExcessBurst,
       "ibmfrCircuitThroughput": ibmfrCircuitThroughput,
       "ibmfrErrTable": ibmfrErrTable,
       "ibmfrErrEntry": ibmfrErrEntry,
       "ibmfrErrIfIndex": ibmfrErrIfIndex,
       "ibmfrErrType": ibmfrErrType,
       "ibmfrErrData": ibmfrErrData,
       "ibmfrErrTime": ibmfrErrTime,
       "ibmdls": ibmdls,
       "ibmdlsVirtualRingSegmentNumber": ibmdlsVirtualRingSegmentNumber,
       "ibmdlsFrameFilterType": ibmdlsFrameFilterType,
       "ibmdlsNameFilterType": ibmdlsNameFilterType,
       "ibmdlsRouterTable": ibmdlsRouterTable,
       "ibmdlsRouterEntry": ibmdlsRouterEntry,
       "ibmdlsRouterAddress": ibmdlsRouterAddress,
       "ibmdlsRouterStatus": ibmdlsRouterStatus,
       "ibmdlsRouterDefinedBy": ibmdlsRouterDefinedBy,
       "ibmdlsRouterInFrames": ibmdlsRouterInFrames,
       "ibmdlsRouterOutFrames": ibmdlsRouterOutFrames,
       "ibmdlsLocalFrameFilterTable": ibmdlsLocalFrameFilterTable,
       "ibmdlsLocalFrameFilterEntry": ibmdlsLocalFrameFilterEntry,
       "ibmdlsLocalFrameFilterID": ibmdlsLocalFrameFilterID,
       "ibmdlsLocalFrameFilterSrcAddress": ibmdlsLocalFrameFilterSrcAddress,
       "ibmdlsLocalFrameFilterSrcMask": ibmdlsLocalFrameFilterSrcMask,
       "ibmdlsLocalFrameFilterDestAddress": ibmdlsLocalFrameFilterDestAddress,
       "ibmdlsLocalFrameFilterDestMask": ibmdlsLocalFrameFilterDestMask,
       "ibmdlsRemoteFrameFilterTable": ibmdlsRemoteFrameFilterTable,
       "ibmdlsRemoteFrameFilterEntry": ibmdlsRemoteFrameFilterEntry,
       "ibmdlsRemoteFrameFilterID": ibmdlsRemoteFrameFilterID,
       "ibmdlsRemoteFrameFilterSrcAddress": ibmdlsRemoteFrameFilterSrcAddress,
       "ibmdlsRemoteFrameFilterSrcMask": ibmdlsRemoteFrameFilterSrcMask,
       "ibmdlsRemoteFrameFilterDestAddress": ibmdlsRemoteFrameFilterDestAddress,
       "ibmdlsRemoteFrameFilterDestMask": ibmdlsRemoteFrameFilterDestMask,
       "ibmdlsLocalNameFilterTable": ibmdlsLocalNameFilterTable,
       "ibmdlsLocalNameFilterEntry": ibmdlsLocalNameFilterEntry,
       "ibmdlsLocalNameFilterID": ibmdlsLocalNameFilterID,
       "ibmdlsLocalNameFilterSrcAddress": ibmdlsLocalNameFilterSrcAddress,
       "ibmdlsLocalNameFilterDestAddress": ibmdlsLocalNameFilterDestAddress,
       "ibmdlsRemoteNameFilterTable": ibmdlsRemoteNameFilterTable,
       "ibmdlsRemoteNameFilterEntry": ibmdlsRemoteNameFilterEntry,
       "ibmdlsRemoteNameFilterID": ibmdlsRemoteNameFilterID,
       "ibmdlsRemoteNameFilterSrcAddress": ibmdlsRemoteNameFilterSrcAddress,
       "ibmdlsRemoteNameFilterDestAddress": ibmdlsRemoteNameFilterDestAddress,
       "ibmdlsDefaultDestTable": ibmdlsDefaultDestTable,
       "ibmdlsDefaultDestEntry": ibmdlsDefaultDestEntry,
       "ibmdlsDefaultDestAddress": ibmdlsDefaultDestAddress,
       "ibmdlsDefaultRouterAddress": ibmdlsDefaultRouterAddress,
       "ibmdlsDefaultNBDestTable": ibmdlsDefaultNBDestTable,
       "ibmdlsDefaultNBDestEntry": ibmdlsDefaultNBDestEntry,
       "ibmdlsDefaultNBDestName": ibmdlsDefaultNBDestName,
       "ibmdlsDefaultNBRouterAddress": ibmdlsDefaultNBRouterAddress,
       "ibmdlsStationTable": ibmdlsStationTable,
       "ibmdlsStationEntry": ibmdlsStationEntry,
       "ibmdlsStationIfIndex": ibmdlsStationIfIndex,
       "ibmdlsStationAddress": ibmdlsStationAddress,
       "ibmdlsStationTransmitWindowCount": ibmdlsStationTransmitWindowCount,
       "ibmdlsStationRetransmitCount": ibmdlsStationRetransmitCount,
       "ibmdlsStationRetransmitThreshold": ibmdlsStationRetransmitThreshold,
       "ibmdlsStationForceDisconnectTimeout": ibmdlsStationForceDisconnectTimeout,
       "ibmdlsStationMaxIfieldSize": ibmdlsStationMaxIfieldSize,
       "ibmdlsStationPrimaryRepollTimeout": ibmdlsStationPrimaryRepollTimeout,
       "ibmdlsStationPrimaryRepollCount": ibmdlsStationPrimaryRepollCount,
       "ibmdlsStationPrimaryRepollThreshold": ibmdlsStationPrimaryRepollThreshold,
       "ibmdlsStationPrimarySlowListTimeout": ibmdlsStationPrimarySlowListTimeout,
       "ibmdlsStationSrcAddress": ibmdlsStationSrcAddress,
       "ibmdlsStationDestAddress": ibmdlsStationDestAddress,
       "ibmdlsCirTable": ibmdlsCirTable,
       "ibmdlsCirEntry": ibmdlsCirEntry,
       "ibmdlsCirIfIndex": ibmdlsCirIfIndex,
       "ibmdlsCirSrcAddress": ibmdlsCirSrcAddress,
       "ibmdlsCirSrcSap": ibmdlsCirSrcSap,
       "ibmdlsCirDestAddress": ibmdlsCirDestAddress,
       "ibmdlsCirDestSap": ibmdlsCirDestSap,
       "ibmdlsCirPartnerRouterAddress": ibmdlsCirPartnerRouterAddress,
       "ibmdlsCirLocalLinkState": ibmdlsCirLocalLinkState,
       "ibmdlsCirLocalLinkSubState": ibmdlsCirLocalLinkSubState,
       "ibmdlsCirLocalLinkRouting": ibmdlsCirLocalLinkRouting,
       "ibmdlsCirLocalLinkTestCmdsSent": ibmdlsCirLocalLinkTestCmdsSent,
       "ibmdlsCirLocalLinkTestCmdsFail": ibmdlsCirLocalLinkTestCmdsFail,
       "ibmdlsCirLocalLinkTestCmdsRcv": ibmdlsCirLocalLinkTestCmdsRcv,
       "ibmdlsCirLocalLinkDataPktSent": ibmdlsCirLocalLinkDataPktSent,
       "ibmdlsCirLocalLinkDataPktResent": ibmdlsCirLocalLinkDataPktResent,
       "ibmdlsCirLocalLinkMaxContResent": ibmdlsCirLocalLinkMaxContResent,
       "ibmdlsCirLocalLinkDataPktRcv": ibmdlsCirLocalLinkDataPktRcv,
       "ibmdlsCirLocalLinkInvalidPktRcv": ibmdlsCirLocalLinkInvalidPktRcv,
       "ibmdlsCirLocalLinkAdpRcvErr": ibmdlsCirLocalLinkAdpRcvErr,
       "ibmdlsCirLocalLinkAdpSendErr": ibmdlsCirLocalLinkAdpSendErr,
       "ibmdlsCirLocalLinkRcvInactiveTimeouts": ibmdlsCirLocalLinkRcvInactiveTimeouts,
       "ibmdlsCirLocalLinkCmdPollsSent": ibmdlsCirLocalLinkCmdPollsSent,
       "ibmdlsCirLocalLinkCmdRepollsSent": ibmdlsCirLocalLinkCmdRepollsSent,
       "ibmdlsCirLocalLinkCmdContRepolls": ibmdlsCirLocalLinkCmdContRepolls,
       "ibmdlsCirLocalAddress": ibmdlsCirLocalAddress,
       "ibmdlsCirLocalConnectionState": ibmdlsCirLocalConnectionState,
       "ibmppp": ibmppp,
       "ibmpppLinkControlTable": ibmpppLinkControlTable,
       "ibmpppLinkControlEntry": ibmpppLinkControlEntry,
       "ibmpppLinkControlIndex": ibmpppLinkControlIndex,
       "ibmpppLinkCRCSize": ibmpppLinkCRCSize,
       "ibmpppLinkRestartTimerValue": ibmpppLinkRestartTimerValue,
       "ibmpppLinkMaxRestarts": ibmpppLinkMaxRestarts,
       "ibmpppLinkLocalMRU": ibmpppLinkLocalMRU,
       "ibmpppLinkRemoteMRU": ibmpppLinkRemoteMRU,
       "ibmpppLinkLocalACCMap": ibmpppLinkLocalACCMap,
       "ibmpppLinkRemoteACCMap": ibmpppLinkRemoteACCMap,
       "ibmpppLinkMagicLoopCount": ibmpppLinkMagicLoopCount,
       "ibmpppLinkCommand": ibmpppLinkCommand,
       "ibmpppLinkStatusTable": ibmpppLinkStatusTable,
       "ibmpppLinkStatusEntry": ibmpppLinkStatusEntry,
       "ibmpppLinkStatusIndex": ibmpppLinkStatusIndex,
       "ibmpppLinkVersion": ibmpppLinkVersion,
       "ibmpppLinkCurrentState": ibmpppLinkCurrentState,
       "ibmpppLinkPreviousState": ibmpppLinkPreviousState,
       "ibmpppLinkChangeTime": ibmpppLinkChangeTime,
       "ibmpppLinkMagicNumber": ibmpppLinkMagicNumber,
       "ibmpppLinkLocalQualityPeriod": ibmpppLinkLocalQualityPeriod,
       "ibmpppLinkRemoteQualityPeriod": ibmpppLinkRemoteQualityPeriod,
       "ibmpppLinkProtocolCompression": ibmpppLinkProtocolCompression,
       "ibmpppLinkACCompression": ibmpppLinkACCompression,
       "ibmpppLinkMeasurementsValid": ibmpppLinkMeasurementsValid,
       "ibmpppLinkQuality": ibmpppLinkQuality,
       "ibmpppLinkPhysical": ibmpppLinkPhysical,
       "ibmpppLinkErrorsTable": ibmpppLinkErrorsTable,
       "ibmpppLinkErrorsEntry": ibmpppLinkErrorsEntry,
       "ibmpppLinkErrorsIndex": ibmpppLinkErrorsIndex,
       "ibmpppLinkBadAddresses": ibmpppLinkBadAddresses,
       "ibmpppLinkLastBadAddress": ibmpppLinkLastBadAddress,
       "ibmpppLinkBadControls": ibmpppLinkBadControls,
       "ibmpppLinkLastBadControl": ibmpppLinkLastBadControl,
       "ibmpppLinkLastUnknownProtocol": ibmpppLinkLastUnknownProtocol,
       "ibmpppLinkInvalidProtocols": ibmpppLinkInvalidProtocols,
       "ibmpppLinkLastInvalidProtocol": ibmpppLinkLastInvalidProtocol,
       "ibmpppLinkPacketTooLongs": ibmpppLinkPacketTooLongs,
       "ibmpppLinkBadCRCs": ibmpppLinkBadCRCs,
       "ibmpppLinkConfigTimeouts": ibmpppLinkConfigTimeouts,
       "ibmpppLinkTerminateTimeouts": ibmpppLinkTerminateTimeouts,
       "ibmpppLinkQualityTable": ibmpppLinkQualityTable,
       "ibmpppLinkQualityEntry": ibmpppLinkQualityEntry,
       "ibmpppLinkQualityIndex": ibmpppLinkQualityIndex,
       "ibmpppLinkInTxLQRs": ibmpppLinkInTxLQRs,
       "ibmpppLinkInTxPackets": ibmpppLinkInTxPackets,
       "ibmpppLinkLastOutTxPackets": ibmpppLinkLastOutTxPackets,
       "ibmpppLinkInTxOctets": ibmpppLinkInTxOctets,
       "ibmpppLinkLastOutTxOctets": ibmpppLinkLastOutTxOctets,
       "ibmpppLinkInRxPackets": ibmpppLinkInRxPackets,
       "ibmpppLinkLastInRxPackets": ibmpppLinkLastInRxPackets,
       "ibmpppLinkInRxOctets": ibmpppLinkInRxOctets,
       "ibmpppLinkLastInRxOctets": ibmpppLinkLastInRxOctets,
       "ibmpppProtocolTables": ibmpppProtocolTables,
       "ibmpppIPTable": ibmpppIPTable,
       "ibmpppIPEntry": ibmpppIPEntry,
       "ibmpppIPLinkNumber": ibmpppIPLinkNumber,
       "ibmpppIPRejects": ibmpppIPRejects,
       "ibmpppIPInPackets": ibmpppIPInPackets,
       "ibmpppIPInOctets": ibmpppIPInOctets,
       "ibmpppIPOutPackets": ibmpppIPOutPackets,
       "ibmpppIPOutOctets": ibmpppIPOutOctets,
       "ibmpppIPCPTable": ibmpppIPCPTable,
       "ibmpppIPCPEntry": ibmpppIPCPEntry,
       "ibmpppIPCPLinkNumber": ibmpppIPCPLinkNumber,
       "ibmpppIPCPRejects": ibmpppIPCPRejects,
       "ibmpppIPCPInPackets": ibmpppIPCPInPackets,
       "ibmpppIPCPInOctets": ibmpppIPCPInOctets,
       "ibmpppIPCPOutPackets": ibmpppIPCPOutPackets,
       "ibmpppIPCPOutOctets": ibmpppIPCPOutOctets,
       "ibmpppIPCPCompressionType": ibmpppIPCPCompressionType,
       "ibmpppLCPTable": ibmpppLCPTable,
       "ibmpppLCPEntry": ibmpppLCPEntry,
       "ibmpppLCPLinkNumber": ibmpppLCPLinkNumber,
       "ibmpppLCPRejects": ibmpppLCPRejects,
       "ibmpppLCPInPackets": ibmpppLCPInPackets,
       "ibmpppLCPInOctets": ibmpppLCPInOctets,
       "ibmpppLCPOutPackets": ibmpppLCPOutPackets,
       "ibmpppLCPOutOctets": ibmpppLCPOutOctets,
       "ibmpppLCPOutCRs": ibmpppLCPOutCRs,
       "ibmpppLCPInCRs": ibmpppLCPInCRs,
       "ibmpppLCPOutCAs": ibmpppLCPOutCAs,
       "ibmpppLCPInCAs": ibmpppLCPInCAs,
       "ibmpppLCPOutCNs": ibmpppLCPOutCNs,
       "ibmpppLCPInCNs": ibmpppLCPInCNs,
       "ibmpppLCPOutCRejs": ibmpppLCPOutCRejs,
       "ibmpppLCPInCRejs": ibmpppLCPInCRejs,
       "ibmpppLCPOutTRs": ibmpppLCPOutTRs,
       "ibmpppLCPInTRs": ibmpppLCPInTRs,
       "ibmpppLCPOutTAs": ibmpppLCPOutTAs,
       "ibmpppLCPInTAs": ibmpppLCPInTAs,
       "ibmpppLCPOutCodeRejs": ibmpppLCPOutCodeRejs,
       "ibmpppLCPInCodeRejs": ibmpppLCPInCodeRejs,
       "ibmpppLCPOutEchoReqs": ibmpppLCPOutEchoReqs,
       "ibmpppLCPInEchoReqs": ibmpppLCPInEchoReqs,
       "ibmpppLCPOutEchoReps": ibmpppLCPOutEchoReps,
       "ibmpppLCPInEchoReps": ibmpppLCPInEchoReps,
       "ibmpppLCPOutDiscReqs": ibmpppLCPOutDiscReqs,
       "ibmpppLCPInDiscReqs": ibmpppLCPInDiscReqs,
       "ibmxns": ibmxns,
       "ibmxnsidpForwarding": ibmxnsidpForwarding,
       "ibmxnsConfigTable": ibmxnsConfigTable,
       "ibmxnsConfigEntry": ibmxnsConfigEntry,
       "ibmxnsPortIfIndex": ibmxnsPortIfIndex,
       "ibmxnsPortStatus": ibmxnsPortStatus,
       "ibmxnsidpChecksum": ibmxnsidpChecksum,
       "ibmxnsErrpActive": ibmxnsErrpActive,
       "ibmxnsLoopbackActive": ibmxnsLoopbackActive,
       "ibmxnsidpInReceives": ibmxnsidpInReceives,
       "ibmxnsidpBcastInReceives": ibmxnsidpBcastInReceives,
       "ibmxnsidpMcastInReceives": ibmxnsidpMcastInReceives,
       "ibmxnsidpInDiscards": ibmxnsidpInDiscards,
       "ibmxnsidpOutRequests": ibmxnsidpOutRequests,
       "ibmxnsidpBcastOutRequests": ibmxnsidpBcastOutRequests,
       "ibmxnsidpMcastOutRequests": ibmxnsidpMcastOutRequests,
       "ibmxnsidpForwDatagrams": ibmxnsidpForwDatagrams,
       "ibmxnsidpOutDiscards": ibmxnsidpOutDiscards,
       "ibmxnsidpOutNoRoutes": ibmxnsidpOutNoRoutes,
       "ibmxnsidpRoutingDiscards": ibmxnsidpRoutingDiscards,
       "ibmxnsidpZeroDirBcast": ibmxnsidpZeroDirBcast,
       "ibmxnsidpTooSmall": ibmxnsidpTooSmall,
       "ibmxnsidpBadLen": ibmxnsidpBadLen,
       "ibmxnsidpBadSum": ibmxnsidpBadSum,
       "ibmxnsidpBadTTL": ibmxnsidpBadTTL,
       "ibmxnsErrUnspec": ibmxnsErrUnspec,
       "ibmxnsErrChecksum": ibmxnsErrChecksum,
       "ibmxnsErrUnreach": ibmxnsErrUnreach,
       "ibmxnsErrTTLExpired": ibmxnsErrTTLExpired,
       "ibmxnsErrTooBig": ibmxnsErrTooBig,
       "ibmxnsErrResources": ibmxnsErrResources,
       "ibmxnsErrCongWarn": ibmxnsErrCongWarn,
       "ibmxnsErrCongDiscard": ibmxnsErrCongDiscard,
       "ibmxnsErrSquelched": ibmxnsErrSquelched,
       "ibmxnsErrOutMsgs": ibmxnsErrOutMsgs,
       "ibmxnsAddrTable": ibmxnsAddrTable,
       "ibmxnsAddrEntry": ibmxnsAddrEntry,
       "ibmxnsAddrAddress": ibmxnsAddrAddress,
       "ibmxnsAddrIfIndex": ibmxnsAddrIfIndex,
       "ibmxnsRouteTable": ibmxnsRouteTable,
       "ibmxnsRouteEntry": ibmxnsRouteEntry,
       "ibmxnsRouteDest": ibmxnsRouteDest,
       "ibmxnsRouteIfIndex": ibmxnsRouteIfIndex,
       "ibmxnsRouteNextHop": ibmxnsRouteNextHop,
       "ibmxnsRouteMetric": ibmxnsRouteMetric,
       "ibmxnsRouteUse": ibmxnsRouteUse,
       "ibmxnsFilterTable": ibmxnsFilterTable,
       "ibmxnsFilterEntry": ibmxnsFilterEntry,
       "ibmxnsFilterIfIndex": ibmxnsFilterIfIndex,
       "ibmxnsFilterNumber": ibmxnsFilterNumber,
       "ibmxnsFilterValue": ibmxnsFilterValue,
       "ibmxnsFilterMask": ibmxnsFilterMask,
       "ibmxnsFilterType": ibmxnsFilterType,
       "ibmxnsFilterHCCompare": ibmxnsFilterHCCompare,
       "ibmxnsFilterUse": ibmxnsFilterUse,
       "ibmipx": ibmipx,
       "ibmipxidpForwarding": ibmipxidpForwarding,
       "ibmipxConfigTable": ibmipxConfigTable,
       "ibmipxConfigEntry": ibmipxConfigEntry,
       "ibmipxPortIfIndex": ibmipxPortIfIndex,
       "ibmipxPortStatus": ibmipxPortStatus,
       "ibmipxidpChecksum": ibmipxidpChecksum,
       "ibmipxLoopbackActive": ibmipxLoopbackActive,
       "ibmipxidpInReceives": ibmipxidpInReceives,
       "ibmipxidpBcastInReceives": ibmipxidpBcastInReceives,
       "ibmipxidpInDiscards": ibmipxidpInDiscards,
       "ibmipxidpInAddrErrors": ibmipxidpInAddrErrors,
       "ibmipxidpOutRequests": ibmipxidpOutRequests,
       "ibmipxidpBcastOutRequests": ibmipxidpBcastOutRequests,
       "ibmipxidpForwDatagrams": ibmipxidpForwDatagrams,
       "ibmipxidpOutDiscards": ibmipxidpOutDiscards,
       "ibmipxidpOutNoRoutes": ibmipxidpOutNoRoutes,
       "ibmipxidpRoutingDiscards": ibmipxidpRoutingDiscards,
       "ibmipxidpZeroDirBcast": ibmipxidpZeroDirBcast,
       "ibmipxidpTooSmall": ibmipxidpTooSmall,
       "ibmipxidpBadLen": ibmipxidpBadLen,
       "ibmipxidpBadSum": ibmipxidpBadSum,
       "ibmipxidpBadTTL": ibmipxidpBadTTL,
       "ibmipxAddrTable": ibmipxAddrTable,
       "ibmipxAddrEntry": ibmipxAddrEntry,
       "ibmipxAddrAddress": ibmipxAddrAddress,
       "ibmipxAddrIfIndex": ibmipxAddrIfIndex,
       "ibmipxRouteTable": ibmipxRouteTable,
       "ibmipxRouteEntry": ibmipxRouteEntry,
       "ibmipxRouteDest": ibmipxRouteDest,
       "ibmipxRouteIfIndex": ibmipxRouteIfIndex,
       "ibmipxRouteNextHop": ibmipxRouteNextHop,
       "ibmipxRouteMetric": ibmipxRouteMetric,
       "ibmipxRouteUse": ibmipxRouteUse,
       "ibmipxFilterTable": ibmipxFilterTable,
       "ibmipxFilterEntry": ibmipxFilterEntry,
       "ibmipxFilterIfIndex": ibmipxFilterIfIndex,
       "ibmipxFilterNumber": ibmipxFilterNumber,
       "ibmipxFilterValue": ibmipxFilterValue,
       "ibmipxFilterMask": ibmipxFilterMask,
       "ibmipxFilterType": ibmipxFilterType,
       "ibmipxFilterHCCompare": ibmipxFilterHCCompare,
       "ibmipxFilterUse": ibmipxFilterUse,
       "ibmipxsapStatInRequests": ibmipxsapStatInRequests,
       "ibmipxsapStatOutRequests": ibmipxsapStatOutRequests,
       "ibmipxsapStatInResponses": ibmipxsapStatInResponses,
       "ibmipxsapStatOutResponses": ibmipxsapStatOutResponses,
       "ibmipxsapStatInErrors": ibmipxsapStatInErrors,
       "ibmipxsapStatOutDiscards": ibmipxsapStatOutDiscards,
       "ibmipxsapServerTable": ibmipxsapServerTable,
       "ibmipxsapServerEntry": ibmipxsapServerEntry,
       "ibmipxsapServerType": ibmipxsapServerType,
       "ibmipxsapServerNet": ibmipxsapServerNet,
       "ibmipxsapServerHost": ibmipxsapServerHost,
       "ibmipxsapServerSocket": ibmipxsapServerSocket,
       "ibmipxsapServerName": ibmipxsapServerName,
       "ibmipxsapServerAge": ibmipxsapServerAge,
       "ibmipxsapServerHops": ibmipxsapServerHops,
       "ibmipxsapServerIfIndex": ibmipxsapServerIfIndex,
       "ibmipxsapServerIndex": ibmipxsapServerIndex,
       "ibmipxsapServerRequestsFiltered": ibmipxsapServerRequestsFiltered,
       "ibmappn": ibmappn,
       "ibmappnNode": ibmappnNode,
       "ibmappnGeneralInfoAndCaps": ibmappnGeneralInfoAndCaps,
       "ibmappnNodeCpName": ibmappnNodeCpName,
       "ibmappnNodeNetid": ibmappnNodeNetid,
       "ibmappnNodeBlockNum": ibmappnNodeBlockNum,
       "ibmappnNodeIdNum": ibmappnNodeIdNum,
       "ibmappnNodeType": ibmappnNodeType,
       "ibmappnNodeUpTime": ibmappnNodeUpTime,
       "ibmappnNodeNegotLs": ibmappnNodeNegotLs,
       "ibmappnNodeSegReasm": ibmappnNodeSegReasm,
       "ibmappnNodeBindReasm": ibmappnNodeBindReasm,
       "ibmappnNodeParallelTg": ibmappnNodeParallelTg,
       "ibmappnNodeService": ibmappnNodeService,
       "ibmappnNodeAdaptiveBindPacing": ibmappnNodeAdaptiveBindPacing,
       "ibmappnNnUniqueInfoAndCaps": ibmappnNnUniqueInfoAndCaps,
       "ibmappnNodeNnRcvRegChar": ibmappnNodeNnRcvRegChar,
       "ibmappnNodeNnGateway": ibmappnNodeNnGateway,
       "ibmappnNodeNnCentralDirectory": ibmappnNodeNnCentralDirectory,
       "ibmappnNodeNnTreeCache": ibmappnNodeNnTreeCache,
       "ibmappnNodeNnTreeUpdate": ibmappnNodeNnTreeUpdate,
       "ibmappnNodeNnRouteAddResist": ibmappnNodeNnRouteAddResist,
       "ibmappnNodeNnIsr": ibmappnNodeNnIsr,
       "ibmappnNodeNnFrsn": ibmappnNodeNnFrsn,
       "ibmappnEnUniqueCaps": ibmappnEnUniqueCaps,
       "ibmappnNodeEnSegGen": ibmappnNodeEnSegGen,
       "ibmappnNodeEnModeCosMap": ibmappnNodeEnModeCosMap,
       "ibmappnNodeEnLocateCdinit": ibmappnNodeEnLocateCdinit,
       "ibmappnNodeEnSendRegNames": ibmappnNodeEnSendRegNames,
       "ibmappnNodeEnSendRegChar": ibmappnNodeEnSendRegChar,
       "ibmappnPortInformation": ibmappnPortInformation,
       "ibmappnNodePortTable": ibmappnNodePortTable,
       "ibmappnNodePortEntry": ibmappnNodePortEntry,
       "ibmappnNodePortName": ibmappnNodePortName,
       "ibmappnNodePortState": ibmappnNodePortState,
       "ibmappnNodePortDlcType": ibmappnNodePortDlcType,
       "ibmappnNodePortPortType": ibmappnNodePortPortType,
       "ibmappnNodePortSIMRIM": ibmappnNodePortSIMRIM,
       "ibmappnNodePortLsRole": ibmappnNodePortLsRole,
       "ibmappnNodePortMaxRcvBtuSize": ibmappnNodePortMaxRcvBtuSize,
       "ibmappnNodePortMaxIframeWindow": ibmappnNodePortMaxIframeWindow,
       "ibmappnNodePortDefLsGoodXids": ibmappnNodePortDefLsGoodXids,
       "ibmappnNodePortDefLsBadXids": ibmappnNodePortDefLsBadXids,
       "ibmappnNodePortDynLsGoodXids": ibmappnNodePortDynLsGoodXids,
       "ibmappnNodePortDynLsBadXids": ibmappnNodePortDynLsBadXids,
       "ibmappnNodePortSpecific": ibmappnNodePortSpecific,
       "ibmappnNodePortIpTable": ibmappnNodePortIpTable,
       "ibmappnNodePortIpEntry": ibmappnNodePortIpEntry,
       "ibmappnNodePortIpName": ibmappnNodePortIpName,
       "ibmappnNodePortIpPortNum": ibmappnNodePortIpPortNum,
       "ibmappnNodePortDlsTable": ibmappnNodePortDlsTable,
       "ibmappnNodePortDlsEntry": ibmappnNodePortDlsEntry,
       "ibmappnNodePortDlsName": ibmappnNodePortDlsName,
       "ibmappnNodePortDlsMac": ibmappnNodePortDlsMac,
       "ibmappnNodePortDlsSap": ibmappnNodePortDlsSap,
       "ibmappnNodePortTrTable": ibmappnNodePortTrTable,
       "ibmappnNodePortTrEntry": ibmappnNodePortTrEntry,
       "ibmappnNodePortTrName": ibmappnNodePortTrName,
       "ibmappnNodePortTrMac": ibmappnNodePortTrMac,
       "ibmappnNodePortTrSap": ibmappnNodePortTrSap,
       "ibmappnNodePortDlcTraceTable": ibmappnNodePortDlcTraceTable,
       "ibmappnNodePortDlcTraceEntry": ibmappnNodePortDlcTraceEntry,
       "ibmappnNodePortDlcTracPortName": ibmappnNodePortDlcTracPortName,
       "ibmappnNodePortDlcTracIndex": ibmappnNodePortDlcTracIndex,
       "ibmappnNodePortDlcTracDlcType": ibmappnNodePortDlcTracDlcType,
       "ibmappnNodePortDlcTracLocalAddr": ibmappnNodePortDlcTracLocalAddr,
       "ibmappnNodePortDlcTracRemoteAddr": ibmappnNodePortDlcTracRemoteAddr,
       "ibmappnNodePortDlcTracMsgType": ibmappnNodePortDlcTracMsgType,
       "ibmappnNodePortDlcTracCmdType": ibmappnNodePortDlcTracCmdType,
       "ibmappnNodePortDlcTracUseWan": ibmappnNodePortDlcTracUseWan,
       "ibmappnLinkStationInformation": ibmappnLinkStationInformation,
       "ibmappnNodeLsTable": ibmappnNodeLsTable,
       "ibmappnNodeLsEntry": ibmappnNodeLsEntry,
       "ibmappnNodeLsName": ibmappnNodeLsName,
       "ibmappnNodeLsPortName": ibmappnNodeLsPortName,
       "ibmappnNodeLsDlcType": ibmappnNodeLsDlcType,
       "ibmappnNodeLsDynamic": ibmappnNodeLsDynamic,
       "ibmappnNodeLsState": ibmappnNodeLsState,
       "ibmappnNodeLsCpName": ibmappnNodeLsCpName,
       "ibmappnNodeLsTgNum": ibmappnNodeLsTgNum,
       "ibmappnNodeLsLimResource": ibmappnNodeLsLimResource,
       "ibmappnNodeLsMigration": ibmappnNodeLsMigration,
       "ibmappnNodeLsBlockNum": ibmappnNodeLsBlockNum,
       "ibmappnNodeLsIdNum": ibmappnNodeLsIdNum,
       "ibmappnNodeLsCpCpSession": ibmappnNodeLsCpCpSession,
       "ibmappnNodeLsTargetPacingCount": ibmappnNodeLsTargetPacingCount,
       "ibmappnNodeLsMaxSendBtuSize": ibmappnNodeLsMaxSendBtuSize,
       "ibmappnNodeLsEffCap": ibmappnNodeLsEffCap,
       "ibmappnNodeLsConnCost": ibmappnNodeLsConnCost,
       "ibmappnNodeLsByteCost": ibmappnNodeLsByteCost,
       "ibmappnNodeLsSecurity": ibmappnNodeLsSecurity,
       "ibmappnNodeLsDelay": ibmappnNodeLsDelay,
       "ibmappnNodeLsUsr1": ibmappnNodeLsUsr1,
       "ibmappnNodeLsUsr2": ibmappnNodeLsUsr2,
       "ibmappnNodeLsUsr3": ibmappnNodeLsUsr3,
       "ibmappnNodeLsInXidBytes": ibmappnNodeLsInXidBytes,
       "ibmappnNodeLsInMsgBytes": ibmappnNodeLsInMsgBytes,
       "ibmappnNodeLsInXidFrames": ibmappnNodeLsInXidFrames,
       "ibmappnNodeLsInMsgFrames": ibmappnNodeLsInMsgFrames,
       "ibmappnNodeLsOutXidBytes": ibmappnNodeLsOutXidBytes,
       "ibmappnNodeLsOutMsgBytes": ibmappnNodeLsOutMsgBytes,
       "ibmappnNodeLsOutXidFrames": ibmappnNodeLsOutXidFrames,
       "ibmappnNodeLsOutMsgFrames": ibmappnNodeLsOutMsgFrames,
       "ibmappnNodeLsEchoRsps": ibmappnNodeLsEchoRsps,
       "ibmappnNodeLsCurrentDelay": ibmappnNodeLsCurrentDelay,
       "ibmappnNodeLsMaxDelay": ibmappnNodeLsMaxDelay,
       "ibmappnNodeLsMinDelay": ibmappnNodeLsMinDelay,
       "ibmappnNodeLsMaxDelayTime": ibmappnNodeLsMaxDelayTime,
       "ibmappnNodeLsGoodXids": ibmappnNodeLsGoodXids,
       "ibmappnNodeLsBadXids": ibmappnNodeLsBadXids,
       "ibmappnNodeLsSpecific": ibmappnNodeLsSpecific,
       "ibmappnNodeLsSubState": ibmappnNodeLsSubState,
       "ibmappnNodeLsStartTime": ibmappnNodeLsStartTime,
       "ibmappnNodeLsActiveTime": ibmappnNodeLsActiveTime,
       "ibmappnNodeLsCurrentStateTime": ibmappnNodeLsCurrentStateTime,
       "ibmappnNodeLsIpTable": ibmappnNodeLsIpTable,
       "ibmappnNodeLsIpEntry": ibmappnNodeLsIpEntry,
       "ibmappnNodeLsIpName": ibmappnNodeLsIpName,
       "ibmappnNodeLsIpState": ibmappnNodeLsIpState,
       "ibmappnNodeLsLocalIpAddr": ibmappnNodeLsLocalIpAddr,
       "ibmappnNodeLsLocalIpPortNum": ibmappnNodeLsLocalIpPortNum,
       "ibmappnNodeLsRemoteIpAddr": ibmappnNodeLsRemoteIpAddr,
       "ibmappnNodeLsRemoteIpPortNum": ibmappnNodeLsRemoteIpPortNum,
       "ibmappnNodeLsDlsTable": ibmappnNodeLsDlsTable,
       "ibmappnNodeLsDlsEntry": ibmappnNodeLsDlsEntry,
       "ibmappnNodeLsDlsName": ibmappnNodeLsDlsName,
       "ibmappnNodeLsDlsState": ibmappnNodeLsDlsState,
       "ibmappnNodeLsLocalDlsMac": ibmappnNodeLsLocalDlsMac,
       "ibmappnNodeLsLocalDlsSap": ibmappnNodeLsLocalDlsSap,
       "ibmappnNodeLsRemoteDlsMac": ibmappnNodeLsRemoteDlsMac,
       "ibmappnNodeLsRemoteDlsSap": ibmappnNodeLsRemoteDlsSap,
       "ibmappnNodeLsTrTable": ibmappnNodeLsTrTable,
       "ibmappnNodeLsTrEntry": ibmappnNodeLsTrEntry,
       "ibmappnNodeLsTrName": ibmappnNodeLsTrName,
       "ibmappnNodeLsTrState": ibmappnNodeLsTrState,
       "ibmappnNodeLsLocalTrMac": ibmappnNodeLsLocalTrMac,
       "ibmappnNodeLsLocalTrSap": ibmappnNodeLsLocalTrSap,
       "ibmappnNodeLsRemoteTrMac": ibmappnNodeLsRemoteTrMac,
       "ibmappnNodeLsRemoteTrSap": ibmappnNodeLsRemoteTrSap,
       "ibmappnNodeLsStatusTable": ibmappnNodeLsStatusTable,
       "ibmappnNodeLsStatusEntry": ibmappnNodeLsStatusEntry,
       "ibmappnNodeLsStatusIndex": ibmappnNodeLsStatusIndex,
       "ibmappnNodeLsStatusTime": ibmappnNodeLsStatusTime,
       "ibmappnNodeLsStatusLsName": ibmappnNodeLsStatusLsName,
       "ibmappnNodeLsStatusCpName": ibmappnNodeLsStatusCpName,
       "ibmappnNodeLsStatusNodeId": ibmappnNodeLsStatusNodeId,
       "ibmappnNodeLsStatusTgNum": ibmappnNodeLsStatusTgNum,
       "ibmappnNodeLsStatusGeneralSense": ibmappnNodeLsStatusGeneralSense,
       "ibmappnNodeLsStatusNofRetry": ibmappnNodeLsStatusNofRetry,
       "ibmappnNodeLsStatusEndSense": ibmappnNodeLsStatusEndSense,
       "ibmappnNodeLsStatusXidLocalSense": ibmappnNodeLsStatusXidLocalSense,
       "ibmappnNodeLsStatusXidRemoteSense": ibmappnNodeLsStatusXidRemoteSense,
       "ibmappnNodeLsStatusXidByteInError": ibmappnNodeLsStatusXidByteInError,
       "ibmappnNodeLsStatusXidBitInError": ibmappnNodeLsStatusXidBitInError,
       "ibmappnNodeLsStatusDlcType": ibmappnNodeLsStatusDlcType,
       "ibmappnNodeLsStatusLocalAddr": ibmappnNodeLsStatusLocalAddr,
       "ibmappnNodeLsStatusRemoteAddr": ibmappnNodeLsStatusRemoteAddr,
       "ibmappnSnmpInformation": ibmappnSnmpInformation,
       "ibmappnSnmpInPkts": ibmappnSnmpInPkts,
       "ibmappnSnmpInGetRequests": ibmappnSnmpInGetRequests,
       "ibmappnSnmpInGetNexts": ibmappnSnmpInGetNexts,
       "ibmappnSnmpInSetRequests": ibmappnSnmpInSetRequests,
       "ibmappnSnmpInTotalVars": ibmappnSnmpInTotalVars,
       "ibmappnSnmpInGetVars": ibmappnSnmpInGetVars,
       "ibmappnSnmpInGetNextVars": ibmappnSnmpInGetNextVars,
       "ibmappnSnmpInSetVars": ibmappnSnmpInSetVars,
       "ibmappnSnmpOutNoSuchNames": ibmappnSnmpOutNoSuchNames,
       "ibmappnSnmpOutGenErrs": ibmappnSnmpOutGenErrs,
       "ibmappnMemoryUse": ibmappnMemoryUse,
       "ibmappnMemorySize": ibmappnMemorySize,
       "ibmappnMemoryUsed": ibmappnMemoryUsed,
       "ibmappnMemoryWarnThresh": ibmappnMemoryWarnThresh,
       "ibmappnMemoryCritThresh": ibmappnMemoryCritThresh,
       "ibmappnXidInformation": ibmappnXidInformation,
       "ibmappnNodeDefLsGoodXids": ibmappnNodeDefLsGoodXids,
       "ibmappnNodeDefLsBadXids": ibmappnNodeDefLsBadXids,
       "ibmappnNodeDynLsGoodXids": ibmappnNodeDynLsGoodXids,
       "ibmappnNodeDynLsBadXids": ibmappnNodeDynLsBadXids,
       "ibmappnNn": ibmappnNn,
       "ibmappnNnTopo": ibmappnNnTopo,
       "ibmappnNnTopoMaxNodes": ibmappnNnTopoMaxNodes,
       "ibmappnNnTopoCurNumNodes": ibmappnNnTopoCurNumNodes,
       "ibmappnNnTopoInTdus": ibmappnNnTopoInTdus,
       "ibmappnNnTopoOutTdus": ibmappnNnTopoOutTdus,
       "ibmappnNnTopoNodeLowRsns": ibmappnNnTopoNodeLowRsns,
       "ibmappnNnTopoNodeEqualRsns": ibmappnNnTopoNodeEqualRsns,
       "ibmappnNnTopoNodeGoodHighRsns": ibmappnNnTopoNodeGoodHighRsns,
       "ibmappnNnTopoNodeBadHighRsns": ibmappnNnTopoNodeBadHighRsns,
       "ibmappnNnTopoNodeStateUpdates": ibmappnNnTopoNodeStateUpdates,
       "ibmappnNnTopoNodeErrors": ibmappnNnTopoNodeErrors,
       "ibmappnNnTopoNodeTimerUpdates": ibmappnNnTopoNodeTimerUpdates,
       "ibmappnNnTopoNodePurges": ibmappnNnTopoNodePurges,
       "ibmappnNnTopoTgLowRsns": ibmappnNnTopoTgLowRsns,
       "ibmappnNnTopoTgEqualRsns": ibmappnNnTopoTgEqualRsns,
       "ibmappnNnTopoTgGoodHighRsns": ibmappnNnTopoTgGoodHighRsns,
       "ibmappnNnTopoTgBadHighRsns": ibmappnNnTopoTgBadHighRsns,
       "ibmappnNnTopoTgStateUpdates": ibmappnNnTopoTgStateUpdates,
       "ibmappnNnTopoTgErrors": ibmappnNnTopoTgErrors,
       "ibmappnNnTopoTgTimerUpdates": ibmappnNnTopoTgTimerUpdates,
       "ibmappnNnTopoTgPurges": ibmappnNnTopoTgPurges,
       "ibmappnNnTopoTotalRouteCalcs": ibmappnNnTopoTotalRouteCalcs,
       "ibmappnNnTopoTotalRouteRejs": ibmappnNnTopoTotalRouteRejs,
       "ibmappnNnTopoRouteTable": ibmappnNnTopoRouteTable,
       "ibmappnNnTopoRouteEntry": ibmappnNnTopoRouteEntry,
       "ibmappnNnTopoRouteCos": ibmappnNnTopoRouteCos,
       "ibmappnNnTopoRouteTrees": ibmappnNnTopoRouteTrees,
       "ibmappnNnTopoRouteCalcs": ibmappnNnTopoRouteCalcs,
       "ibmappnNnTopoRouteRejs": ibmappnNnTopoRouteRejs,
       "ibmappnNnAdjNodeTable": ibmappnNnAdjNodeTable,
       "ibmappnNnAdjNodeEntry": ibmappnNnAdjNodeEntry,
       "ibmappnNnAdjNodeAdjName": ibmappnNnAdjNodeAdjName,
       "ibmappnNnAdjNodeCpCpSessStatus": ibmappnNnAdjNodeCpCpSessStatus,
       "ibmappnNnAdjNodeOutOfSeqTdus": ibmappnNnAdjNodeOutOfSeqTdus,
       "ibmappnNnAdjNodeLastFrsnSent": ibmappnNnAdjNodeLastFrsnSent,
       "ibmappnNnAdjNodeLastFrsnRcvd": ibmappnNnAdjNodeLastFrsnRcvd,
       "ibmappnNnTopology": ibmappnNnTopology,
       "ibmappnNnTopologyTable": ibmappnNnTopologyTable,
       "ibmappnNnTopologyEntry": ibmappnNnTopologyEntry,
       "ibmappnNnNodeName": ibmappnNnNodeName,
       "ibmappnNnNodeFrsn": ibmappnNnNodeFrsn,
       "ibmappnNnNodeEntryTimeLeft": ibmappnNnNodeEntryTimeLeft,
       "ibmappnNnNodeType": ibmappnNnNodeType,
       "ibmappnNnNodeRsn": ibmappnNnNodeRsn,
       "ibmappnNnNodeRouteAddResist": ibmappnNnNodeRouteAddResist,
       "ibmappnNnNodeCongested": ibmappnNnNodeCongested,
       "ibmappnNnNodeIsrDepleted": ibmappnNnNodeIsrDepleted,
       "ibmappnNnNodeEndptDepleted": ibmappnNnNodeEndptDepleted,
       "ibmappnNnNodeQuiescing": ibmappnNnNodeQuiescing,
       "ibmappnNnNodeGateway": ibmappnNnNodeGateway,
       "ibmappnNnNodeCentralDirectory": ibmappnNnNodeCentralDirectory,
       "ibmappnNnNodeIsr": ibmappnNnNodeIsr,
       "ibmappnNnNodeChainSupport": ibmappnNnNodeChainSupport,
       "ibmappnNnTgTopologyTable": ibmappnNnTgTopologyTable,
       "ibmappnNnTgTopologyEntry": ibmappnNnTgTopologyEntry,
       "ibmappnNnTgOwner": ibmappnNnTgOwner,
       "ibmappnNnTgDest": ibmappnNnTgDest,
       "ibmappnNnTgNum": ibmappnNnTgNum,
       "ibmappnNnTgFrsn": ibmappnNnTgFrsn,
       "ibmappnNnTgEntryTimeLeft": ibmappnNnTgEntryTimeLeft,
       "ibmappnNnTgDestVirtual": ibmappnNnTgDestVirtual,
       "ibmappnNnTgDlcData": ibmappnNnTgDlcData,
       "ibmappnNnTgRsn": ibmappnNnTgRsn,
       "ibmappnNnTgOperational": ibmappnNnTgOperational,
       "ibmappnNnTgQuiescing": ibmappnNnTgQuiescing,
       "ibmappnNnTgCpCpSession": ibmappnNnTgCpCpSession,
       "ibmappnNnTgEffCap": ibmappnNnTgEffCap,
       "ibmappnNnTgConnCost": ibmappnNnTgConnCost,
       "ibmappnNnTgByteCost": ibmappnNnTgByteCost,
       "ibmappnNnTgSecurity": ibmappnNnTgSecurity,
       "ibmappnNnTgDelay": ibmappnNnTgDelay,
       "ibmappnNnTgModemClass": ibmappnNnTgModemClass,
       "ibmappnNnTgUsr1": ibmappnNnTgUsr1,
       "ibmappnNnTgUsr2": ibmappnNnTgUsr2,
       "ibmappnNnTgUsr3": ibmappnNnTgUsr3,
       "ibmappnNnTopologyFRTable": ibmappnNnTopologyFRTable,
       "ibmappnNnTopologyFREntry": ibmappnNnTopologyFREntry,
       "ibmappnNnNodeFRName": ibmappnNnNodeFRName,
       "ibmappnNnNodeFRFrsn": ibmappnNnNodeFRFrsn,
       "ibmappnNnNodeFREntryTimeLeft": ibmappnNnNodeFREntryTimeLeft,
       "ibmappnNnNodeFRType": ibmappnNnNodeFRType,
       "ibmappnNnNodeFRRsn": ibmappnNnNodeFRRsn,
       "ibmappnNnNodeFRRouteAddResist": ibmappnNnNodeFRRouteAddResist,
       "ibmappnNnNodeFRCongested": ibmappnNnNodeFRCongested,
       "ibmappnNnNodeFRIsrDepleted": ibmappnNnNodeFRIsrDepleted,
       "ibmappnNnNodeFREndptDepleted": ibmappnNnNodeFREndptDepleted,
       "ibmappnNnNodeFRQuiescing": ibmappnNnNodeFRQuiescing,
       "ibmappnNnNodeFRGateway": ibmappnNnNodeFRGateway,
       "ibmappnNnNodeFRCentralDirectory": ibmappnNnNodeFRCentralDirectory,
       "ibmappnNnNodeFRIsr": ibmappnNnNodeFRIsr,
       "ibmappnNnNodeFRChainSupport": ibmappnNnNodeFRChainSupport,
       "ibmappnNnTgTopologyFRTable": ibmappnNnTgTopologyFRTable,
       "ibmappnNnTgTopologyFREntry": ibmappnNnTgTopologyFREntry,
       "ibmappnNnTgFROwner": ibmappnNnTgFROwner,
       "ibmappnNnTgFRDest": ibmappnNnTgFRDest,
       "ibmappnNnTgFRNum": ibmappnNnTgFRNum,
       "ibmappnNnTgFRFrsn": ibmappnNnTgFRFrsn,
       "ibmappnNnTgFREntryTimeLeft": ibmappnNnTgFREntryTimeLeft,
       "ibmappnNnTgFRDestVirtual": ibmappnNnTgFRDestVirtual,
       "ibmappnNnTgFRDlcData": ibmappnNnTgFRDlcData,
       "ibmappnNnTgFRRsn": ibmappnNnTgFRRsn,
       "ibmappnNnTgFROperational": ibmappnNnTgFROperational,
       "ibmappnNnTgFRQuiescing": ibmappnNnTgFRQuiescing,
       "ibmappnNnTgFRCpCpSession": ibmappnNnTgFRCpCpSession,
       "ibmappnNnTgFREffCap": ibmappnNnTgFREffCap,
       "ibmappnNnTgFRConnCost": ibmappnNnTgFRConnCost,
       "ibmappnNnTgFRByteCost": ibmappnNnTgFRByteCost,
       "ibmappnNnTgFRSecurity": ibmappnNnTgFRSecurity,
       "ibmappnNnTgFRDelay": ibmappnNnTgFRDelay,
       "ibmappnNnTgFRModemClass": ibmappnNnTgFRModemClass,
       "ibmappnNnTgFRUsr1": ibmappnNnTgFRUsr1,
       "ibmappnNnTgFRUsr2": ibmappnNnTgFRUsr2,
       "ibmappnNnTgFRUsr3": ibmappnNnTgFRUsr3,
       "ibmappnLocalTopology": ibmappnLocalTopology,
       "ibmappnLocalThisNode": ibmappnLocalThisNode,
       "ibmappnLocalGeneral": ibmappnLocalGeneral,
       "ibmappnLocalNodeName": ibmappnLocalNodeName,
       "ibmappnLocalNodeType": ibmappnLocalNodeType,
       "ibmappnLocalNnSpecific": ibmappnLocalNnSpecific,
       "ibmappnLocalNnRsn": ibmappnLocalNnRsn,
       "ibmappnLocalNnRouteAddResist": ibmappnLocalNnRouteAddResist,
       "ibmappnLocalNnCongested": ibmappnLocalNnCongested,
       "ibmappnLocalNnIsrDepleted": ibmappnLocalNnIsrDepleted,
       "ibmappnLocalNnEndptDepleted": ibmappnLocalNnEndptDepleted,
       "ibmappnLocalNnQuiescing": ibmappnLocalNnQuiescing,
       "ibmappnLocalNnGateway": ibmappnLocalNnGateway,
       "ibmappnLocalNnCentralDirectory": ibmappnLocalNnCentralDirectory,
       "ibmappnLocalNnIsr": ibmappnLocalNnIsr,
       "ibmappnLocalNnChainSupport": ibmappnLocalNnChainSupport,
       "ibmappnLocalNnFrsn": ibmappnLocalNnFrsn,
       "ibmappnLocalTg": ibmappnLocalTg,
       "ibmappnLocalTgTable": ibmappnLocalTgTable,
       "ibmappnLocalTgEntry": ibmappnLocalTgEntry,
       "ibmappnLocalTgDest": ibmappnLocalTgDest,
       "ibmappnLocalTgNum": ibmappnLocalTgNum,
       "ibmappnLocalTgDestVirtual": ibmappnLocalTgDestVirtual,
       "ibmappnLocalTgDlcData": ibmappnLocalTgDlcData,
       "ibmappnLocalTgRsn": ibmappnLocalTgRsn,
       "ibmappnLocalTgQuiescing": ibmappnLocalTgQuiescing,
       "ibmappnLocalTgOperational": ibmappnLocalTgOperational,
       "ibmappnLocalTgCpCpSession": ibmappnLocalTgCpCpSession,
       "ibmappnLocalTgEffCap": ibmappnLocalTgEffCap,
       "ibmappnLocalTgConnCost": ibmappnLocalTgConnCost,
       "ibmappnLocalTgByteCost": ibmappnLocalTgByteCost,
       "ibmappnLocalTgSecurity": ibmappnLocalTgSecurity,
       "ibmappnLocalTgDelay": ibmappnLocalTgDelay,
       "ibmappnLocalTgModemClass": ibmappnLocalTgModemClass,
       "ibmappnLocalTgUsr1": ibmappnLocalTgUsr1,
       "ibmappnLocalTgUsr2": ibmappnLocalTgUsr2,
       "ibmappnLocalTgUsr3": ibmappnLocalTgUsr3,
       "ibmappnLocalEnTopology": ibmappnLocalEnTopology,
       "ibmappnLocalEnTable": ibmappnLocalEnTable,
       "ibmappnLocalEnEntry": ibmappnLocalEnEntry,
       "ibmappnLocalEnName": ibmappnLocalEnName,
       "ibmappnLocalEnEntryTimeLeft": ibmappnLocalEnEntryTimeLeft,
       "ibmappnLocalEnType": ibmappnLocalEnType,
       "ibmappnLocalEnTgTable": ibmappnLocalEnTgTable,
       "ibmappnLocalEnTgEntry": ibmappnLocalEnTgEntry,
       "ibmappnLocalEnTgOrigin": ibmappnLocalEnTgOrigin,
       "ibmappnLocalEnTgDest": ibmappnLocalEnTgDest,
       "ibmappnLocalEnTgNum": ibmappnLocalEnTgNum,
       "ibmappnLocalEnTgEntryTimeLeft": ibmappnLocalEnTgEntryTimeLeft,
       "ibmappnLocalEnTgDestVirtual": ibmappnLocalEnTgDestVirtual,
       "ibmappnLocalEnTgDlcData": ibmappnLocalEnTgDlcData,
       "ibmappnLocalEnTgOperational": ibmappnLocalEnTgOperational,
       "ibmappnLocalEnTgCpCpSession": ibmappnLocalEnTgCpCpSession,
       "ibmappnLocalEnTgEffCap": ibmappnLocalEnTgEffCap,
       "ibmappnLocalEnTgConnCost": ibmappnLocalEnTgConnCost,
       "ibmappnLocalEnTgByteCost": ibmappnLocalEnTgByteCost,
       "ibmappnLocalEnTgSecurity": ibmappnLocalEnTgSecurity,
       "ibmappnLocalEnTgDelay": ibmappnLocalEnTgDelay,
       "ibmappnLocalEnTgModemClass": ibmappnLocalEnTgModemClass,
       "ibmappnLocalEnTgUsr1": ibmappnLocalEnTgUsr1,
       "ibmappnLocalEnTgUsr2": ibmappnLocalEnTgUsr2,
       "ibmappnLocalEnTgUsr3": ibmappnLocalEnTgUsr3,
       "ibmappnDir": ibmappnDir,
       "ibmappnDirPerf": ibmappnDirPerf,
       "ibmappnDirMaxCaches": ibmappnDirMaxCaches,
       "ibmappnDirCurCaches": ibmappnDirCurCaches,
       "ibmappnDirCurHomeEntries": ibmappnDirCurHomeEntries,
       "ibmappnDirRegEntries": ibmappnDirRegEntries,
       "ibmappnDirInLocates": ibmappnDirInLocates,
       "ibmappnDirInBcastLocates": ibmappnDirInBcastLocates,
       "ibmappnDirOutLocates": ibmappnDirOutLocates,
       "ibmappnDirOutBcastLocates": ibmappnDirOutBcastLocates,
       "ibmappnDirNotFoundLocates": ibmappnDirNotFoundLocates,
       "ibmappnDirNotFoundBcastLocates": ibmappnDirNotFoundBcastLocates,
       "ibmappnDirLocateOutstands": ibmappnDirLocateOutstands,
       "ibmappnDirTable": ibmappnDirTable,
       "ibmappnDirEntry": ibmappnDirEntry,
       "ibmappnDirLuName": ibmappnDirLuName,
       "ibmappnDirServerName": ibmappnDirServerName,
       "ibmappnDirLuOwnerName": ibmappnDirLuOwnerName,
       "ibmappnDirLuLocation": ibmappnDirLuLocation,
       "ibmappnDirType": ibmappnDirType,
       "ibmappnDirWildCard": ibmappnDirWildCard,
       "ibmappnCos": ibmappnCos,
       "ibmappnCosModeTable": ibmappnCosModeTable,
       "ibmappnCosModeEntry": ibmappnCosModeEntry,
       "ibmappnCosModeName": ibmappnCosModeName,
       "ibmappnCosModeCosName": ibmappnCosModeCosName,
       "ibmappnCosNameTable": ibmappnCosNameTable,
       "ibmappnCosNameEntry": ibmappnCosNameEntry,
       "ibmappnCosName": ibmappnCosName,
       "ibmappnCosTransPriority": ibmappnCosTransPriority,
       "ibmappnCosNodeRowTable": ibmappnCosNodeRowTable,
       "ibmappnCosNodeRowEntry": ibmappnCosNodeRowEntry,
       "ibmappnCosNodeRowName": ibmappnCosNodeRowName,
       "ibmappnCosNodeRowIndex": ibmappnCosNodeRowIndex,
       "ibmappnCosNodeRowWgt": ibmappnCosNodeRowWgt,
       "ibmappnCosNodeRowResistMin": ibmappnCosNodeRowResistMin,
       "ibmappnCosNodeRowResistMax": ibmappnCosNodeRowResistMax,
       "ibmappnCosNodeRowMinCongestAllow": ibmappnCosNodeRowMinCongestAllow,
       "ibmappnCosNodeRowMaxCongestAllow": ibmappnCosNodeRowMaxCongestAllow,
       "ibmappnCosTgRowTable": ibmappnCosTgRowTable,
       "ibmappnCosTgRowEntry": ibmappnCosTgRowEntry,
       "ibmappnCosTgRowName": ibmappnCosTgRowName,
       "ibmappnCosTgRowIndex": ibmappnCosTgRowIndex,
       "ibmappnCosTgRowWgt": ibmappnCosTgRowWgt,
       "ibmappnCosTgRowEffCapMin": ibmappnCosTgRowEffCapMin,
       "ibmappnCosTgRowEffCapMax": ibmappnCosTgRowEffCapMax,
       "ibmappnCosTgRowConnCostMin": ibmappnCosTgRowConnCostMin,
       "ibmappnCosTgRowConnCostMax": ibmappnCosTgRowConnCostMax,
       "ibmappnCosTgRowByteCostMin": ibmappnCosTgRowByteCostMin,
       "ibmappnCosTgRowByteCostMax": ibmappnCosTgRowByteCostMax,
       "ibmappnCosTgRowSecurityMin": ibmappnCosTgRowSecurityMin,
       "ibmappnCosTgRowSecurityMax": ibmappnCosTgRowSecurityMax,
       "ibmappnCosTgRowDelayMin": ibmappnCosTgRowDelayMin,
       "ibmappnCosTgRowDelayMax": ibmappnCosTgRowDelayMax,
       "ibmappnCosTgRowUsr1Min": ibmappnCosTgRowUsr1Min,
       "ibmappnCosTgRowUsr1Max": ibmappnCosTgRowUsr1Max,
       "ibmappnCosTgRowUsr2Min": ibmappnCosTgRowUsr2Min,
       "ibmappnCosTgRowUsr2Max": ibmappnCosTgRowUsr2Max,
       "ibmappnCosTgRowUsr3Min": ibmappnCosTgRowUsr3Min,
       "ibmappnCosTgRowUsr3Max": ibmappnCosTgRowUsr3Max,
       "ibmappnSession": ibmappnSession,
       "ibmappnSessGeneral": ibmappnSessGeneral,
       "ibmappnSessEndPoint": ibmappnSessEndPoint,
       "ibmappcInformation": ibmappcInformation,
       "ibmappcInGlobal": ibmappcInGlobal,
       "ibmappcInGlobeStatus": ibmappcInGlobeStatus,
       "ibmappcInGlobeRscv": ibmappcInGlobeRscv,
       "ibmappcInGlobeRscvTime": ibmappcInGlobeRscvTime,
       "ibmappcInGlobeCtrStatus": ibmappcInGlobeCtrStatus,
       "ibmappcInGlobeCtrStatusTime": ibmappcInGlobeCtrStatusTime,
       "ibmappcInGlobeActSess": ibmappcInGlobeActSess,
       "ibmappcInLluTable": ibmappcInLluTable,
       "ibmappcInLluEntry": ibmappcInLluEntry,
       "ibmappcInLluLuName": ibmappcInLluLuName,
       "ibmappcInLluDefType": ibmappcInLluDefType,
       "ibmappcInLluSessLimit": ibmappcInLluSessLimit,
       "ibmappcInLluBindRspMayQ": ibmappcInLluBindRspMayQ,
       "ibmappcInLluDefaultLu": ibmappcInLluDefaultLu,
       "ibmappcInLluCntlPtLu": ibmappcInLluCntlPtLu,
       "ibmappcInLluCurActSess": ibmappcInLluCurActSess,
       "ibmappcInRluTable": ibmappcInRluTable,
       "ibmappcInRluEntry": ibmappcInRluEntry,
       "ibmappcInRluLocLuName": ibmappcInRluLocLuName,
       "ibmappcInRluParLuName": ibmappcInRluParLuName,
       "ibmappcInRluParLuLocName": ibmappcInRluParLuLocName,
       "ibmappcInRluDefType": ibmappcInRluDefType,
       "ibmappcInRluDefParaSessSup": ibmappcInRluDefParaSessSup,
       "ibmappcInRluDefCnosSup": ibmappcInRluDefCnosSup,
       "ibmappcInRluDefAllVerSup": ibmappcInRluDefAllVerSup,
       "ibmappcInRluDefAttSecSup": ibmappcInRluDefAttSecSup,
       "ibmappcInRluDefSessSecSup": ibmappcInRluDefSessSecSup,
       "ibmappcInRluDefEnhanSecSup": ibmappcInRluDefEnhanSecSup,
       "ibmappcInRluActType": ibmappcInRluActType,
       "ibmappcInRluActParaSessSup": ibmappcInRluActParaSessSup,
       "ibmappcInRluActCnosSup": ibmappcInRluActCnosSup,
       "ibmappcInRluActAllVerSup": ibmappcInRluActAllVerSup,
       "ibmappcInRluActAttSecSup": ibmappcInRluActAttSecSup,
       "ibmappcInRluActSessSecSup": ibmappcInRluActSessSecSup,
       "ibmappcInRluActEnhanSecSup": ibmappcInRluActEnhanSecSup,
       "ibmappcInMdTable": ibmappcInMdTable,
       "ibmappcInMdEntry": ibmappcInMdEntry,
       "ibmappcInMdLluName": ibmappcInMdLluName,
       "ibmappcInMdRluName": ibmappcInMdRluName,
       "ibmappcInMdModeName": ibmappcInMdModeName,
       "ibmappcInMdDefType": ibmappcInMdDefType,
       "ibmappcInMdSessEndTpName": ibmappcInMdSessEndTpName,
       "ibmappcInMdSessLimit": ibmappcInMdSessLimit,
       "ibmappcInMdMaxSessLimit": ibmappcInMdMaxSessLimit,
       "ibmappcInMdAutoActLimit": ibmappcInMdAutoActLimit,
       "ibmappcInMdDrainSelf": ibmappcInMdDrainSelf,
       "ibmappcInMdDrainPart": ibmappcInMdDrainPart,
       "ibmappcInMdMinCwinLimit": ibmappcInMdMinCwinLimit,
       "ibmappcInMdMinClosLimit": ibmappcInMdMinClosLimit,
       "ibmappcInMdRecvPacWinSz": ibmappcInMdRecvPacWinSz,
       "ibmappcInMdSendPacWinSz": ibmappcInMdSendPacWinSz,
       "ibmappcInMdPrefRecvRuSz": ibmappcInMdPrefRecvRuSz,
       "ibmappcInMdPrefSendRuSz": ibmappcInMdPrefSendRuSz,
       "ibmappcInMdRecvRuSzUpBnd": ibmappcInMdRecvRuSzUpBnd,
       "ibmappcInMdSendRuSzUpBnd": ibmappcInMdSendRuSzUpBnd,
       "ibmappcInMdRecvRuSzLoBnd": ibmappcInMdRecvRuSzLoBnd,
       "ibmappcInMdSendRuSzLoBnd": ibmappcInMdSendRuSzLoBnd,
       "ibmappcInMdDfSyncLvl": ibmappcInMdDfSyncLvl,
       "ibmappcInMdAcSyncLvl": ibmappcInMdAcSyncLvl,
       "ibmappcInMdDfCrypto": ibmappcInMdDfCrypto,
       "ibmappcInMdAcCrypto": ibmappcInMdAcCrypto,
       "ibmappcInMdReinit": ibmappcInMdReinit,
       "ibmappcInMdAltCode": ibmappcInMdAltCode,
       "ibmappcInMdActCwin": ibmappcInMdActCwin,
       "ibmappcInMdActClos": ibmappcInMdActClos,
       "ibmappcInMdPndCwin": ibmappcInMdPndCwin,
       "ibmappcInMdPndClos": ibmappcInMdPndClos,
       "ibmappcInMdPtmCwin": ibmappcInMdPtmCwin,
       "ibmappcInMdPtmClos": ibmappcInMdPtmClos,
       "ibmappcInMdFreeSessLst": ibmappcInMdFreeSessLst,
       "ibmappcInMdWaitReqLst": ibmappcInMdWaitReqLst,
       "ibmappcInLtpTable": ibmappcInLtpTable,
       "ibmappcInLtpEntry": ibmappcInLtpEntry,
       "ibmappcInLtpLuName": ibmappcInLtpLuName,
       "ibmappcInLtpTpName": ibmappcInLtpTpName,
       "ibmappcInLtpDefType": ibmappcInLtpDefType,
       "ibmappcInLtpSyncLvl": ibmappcInLtpSyncLvl,
       "ibmappcInLtpInstLmt": ibmappcInLtpInstLmt,
       "ibmappcInLtpInstNum": ibmappcInLtpInstNum,
       "ibmappcInLtpStatus": ibmappcInLtpStatus,
       "ibmappcInLtpLongRun": ibmappcInLtpLongRun,
       "ibmappcInLtpPfCnos": ibmappcInLtpPfCnos,
       "ibmappcInLtpPfSessCntl": ibmappcInLtpPfSessCntl,
       "ibmappcInLtpPfDefine": ibmappcInLtpPfDefine,
       "ibmappcInLtpPfDisplay": ibmappcInLtpPfDisplay,
       "ibmappcInLtpPfAllocSer": ibmappcInLtpPfAllocSer,
       "ibmappcInLtpRescSup": ibmappcInLtpRescSup,
       "ibmappcInLtpRecoSup": ibmappcInLtpRecoSup,
       "ibmappcInLtpSecReq": ibmappcInLtpSecReq,
       "ibmappcInLtpSecLvl": ibmappcInLtpSecLvl,
       "ibmappcInLtpVerPip": ibmappcInLtpVerPip,
       "ibmappcInLtpPipSubNum": ibmappcInLtpPipSubNum,
       "ibmappcInSsTable": ibmappcInSsTable,
       "ibmappcInSsEntry": ibmappcInSsEntry,
       "ibmappcInSsFqLuName": ibmappcInSsFqLuName,
       "ibmappcInSsPcid": ibmappcInSsPcid,
       "ibmappcInSsPluName": ibmappcInSsPluName,
       "ibmappcInSsSluName": ibmappcInSsSluName,
       "ibmappcInSsModeName": ibmappcInSsModeName,
       "ibmappcInSsCosName": ibmappcInSsCosName,
       "ibmappcInSsSessType": ibmappcInSsSessType,
       "ibmappcInSsSessState": ibmappcInSsSessState,
       "ibmappcInSsTransPriority": ibmappcInSsTransPriority,
       "ibmappcInSsPaceType": ibmappcInSsPaceType,
       "ibmappcInSsSendMaxRuSz": ibmappcInSsSendMaxRuSz,
       "ibmappcInSsRecvMaxRuSz": ibmappcInSsRecvMaxRuSz,
       "ibmappcInSsEnhanceSecSup": ibmappcInSsEnhanceSecSup,
       "ibmappcInSsSendPacingType": ibmappcInSsSendPacingType,
       "ibmappcInSsSendRpc": ibmappcInSsSendRpc,
       "ibmappcInSsSendNxWndwSize": ibmappcInSsSendNxWndwSize,
       "ibmappcInSsRecvPacingType": ibmappcInSsRecvPacingType,
       "ibmappcInSsRecvRpc": ibmappcInSsRecvRpc,
       "ibmappcInSsRecvNxWndwSize": ibmappcInSsRecvNxWndwSize,
       "ibmappcInSsSessStartTime": ibmappcInSsSessStartTime,
       "ibmappcInSsSessUpTime": ibmappcInSsSessUpTime,
       "ibmappcInSsCtrUpTime": ibmappcInSsCtrUpTime,
       "ibmappcInSsP2SFmdPius": ibmappcInSsP2SFmdPius,
       "ibmappcInSsS2PFmdPius": ibmappcInSsS2PFmdPius,
       "ibmappcInSsP2SNonFmdPius": ibmappcInSsP2SNonFmdPius,
       "ibmappcInSsS2PNonFmdPius": ibmappcInSsS2PNonFmdPius,
       "ibmappcInSsP2SFmdBytes": ibmappcInSsP2SFmdBytes,
       "ibmappcInSsS2PFmdBytes": ibmappcInSsS2PFmdBytes,
       "ibmappcInSsP2SNonFmdBytes": ibmappcInSsP2SNonFmdBytes,
       "ibmappcInSsS2PNonFmdBytes": ibmappcInSsS2PNonFmdBytes,
       "ibmappcInSsRscv": ibmappcInSsRscv,
       "ibmappcInSsStatusTable": ibmappcInSsStatusTable,
       "ibmappcInSsStatusEntry": ibmappcInSsStatusEntry,
       "ibmappcInSsStatusIndex": ibmappcInSsStatusIndex,
       "ibmappcInSsStatusTime": ibmappcInSsStatusTime,
       "ibmappcInSsStatusType": ibmappcInSsStatusType,
       "ibmappcInSsStatusLocLuName": ibmappcInSsStatusLocLuName,
       "ibmappcInSsStatusParLuName": ibmappcInSsStatusParLuName,
       "ibmappcInSsStatusModeName": ibmappcInSsStatusModeName,
       "ibmappcInSsStatusUnbindType": ibmappcInSsStatusUnbindType,
       "ibmappcInSsStatusSenseCode": ibmappcInSsStatusSenseCode,
       "ibmappcInSsStatusComponentId": ibmappcInSsStatusComponentId,
       "ibmappcInSsStatusDetectModule": ibmappcInSsStatusDetectModule,
       "ibmappnSessIntermediate": ibmappnSessIntermediate,
       "ibmappnIsInformation": ibmappnIsInformation,
       "ibmappnIsInGlobal": ibmappnIsInGlobal,
       "ibmappnIsInGlobeStatus": ibmappnIsInGlobeStatus,
       "ibmappnIsInGlobeRscv": ibmappnIsInGlobeRscv,
       "ibmappnIsInGlobeRscvTime": ibmappnIsInGlobeRscvTime,
       "ibmappnIsInGlobeCtrStatus": ibmappnIsInGlobeCtrStatus,
       "ibmappnIsInGlobeCtrStatusTime": ibmappnIsInGlobeCtrStatusTime,
       "ibmappnIsInTable": ibmappnIsInTable,
       "ibmappnIsInEntry": ibmappnIsInEntry,
       "ibmappnIsInFqLuName": ibmappnIsInFqLuName,
       "ibmappnIsInPcid": ibmappnIsInPcid,
       "ibmappnIsInPriLuName": ibmappnIsInPriLuName,
       "ibmappnIsInSecLuName": ibmappnIsInSecLuName,
       "ibmappnIsInModeName": ibmappnIsInModeName,
       "ibmappnIsInCosName": ibmappnIsInCosName,
       "ibmappnIsInTransPriority": ibmappnIsInTransPriority,
       "ibmappnIsInSessType": ibmappnIsInSessType,
       "ibmappnIsInSessState": ibmappnIsInSessState,
       "ibmappnIsInSessStartTime": ibmappnIsInSessStartTime,
       "ibmappnIsInSessUpTime": ibmappnIsInSessUpTime,
       "ibmappnIsInCtrUpTime": ibmappnIsInCtrUpTime,
       "ibmappnIsInP2SFmdPius": ibmappnIsInP2SFmdPius,
       "ibmappnIsInS2PFmdPius": ibmappnIsInS2PFmdPius,
       "ibmappnIsInP2SNonFmdPius": ibmappnIsInP2SNonFmdPius,
       "ibmappnIsInS2PNonFmdPius": ibmappnIsInS2PNonFmdPius,
       "ibmappnIsInP2SFmdBytes": ibmappnIsInP2SFmdBytes,
       "ibmappnIsInS2PFmdBytes": ibmappnIsInS2PFmdBytes,
       "ibmappnIsInP2SNonFmdBytes": ibmappnIsInP2SNonFmdBytes,
       "ibmappnIsInS2PNonFmdBytes": ibmappnIsInS2PNonFmdBytes,
       "ibmappnIsInPsAdjCpName": ibmappnIsInPsAdjCpName,
       "ibmappnIsInPsAdjTgNum": ibmappnIsInPsAdjTgNum,
       "ibmappnIsInPsSendMaxBtuSize": ibmappnIsInPsSendMaxBtuSize,
       "ibmappnIsInPsSendPacingType": ibmappnIsInPsSendPacingType,
       "ibmappnIsInPsSendRpc": ibmappnIsInPsSendRpc,
       "ibmappnIsInPsSendNxWndwSize": ibmappnIsInPsSendNxWndwSize,
       "ibmappnIsInPsRecvPacingType": ibmappnIsInPsRecvPacingType,
       "ibmappnIsInPsRecvRpc": ibmappnIsInPsRecvRpc,
       "ibmappnIsInPsRecvNxWndwSize": ibmappnIsInPsRecvNxWndwSize,
       "ibmappnIsInSsAdjCpName": ibmappnIsInSsAdjCpName,
       "ibmappnIsInSsAdjTgNum": ibmappnIsInSsAdjTgNum,
       "ibmappnIsInSsSendMaxBtuSize": ibmappnIsInSsSendMaxBtuSize,
       "ibmappnIsInSsSendPacingType": ibmappnIsInSsSendPacingType,
       "ibmappnIsInSsSendRpc": ibmappnIsInSsSendRpc,
       "ibmappnIsInSsSendNxWndwSize": ibmappnIsInSsSendNxWndwSize,
       "ibmappnIsInSsRecvPacingType": ibmappnIsInSsRecvPacingType,
       "ibmappnIsInSsRecvRpc": ibmappnIsInSsRecvRpc,
       "ibmappnIsInSsRecvNxWndwSize": ibmappnIsInSsRecvNxWndwSize,
       "ibmappnIsInRouteInfo": ibmappnIsInRouteInfo,
       "ibmappnIsAccounting": ibmappnIsAccounting,
       "ibmappnIsAcGlobal": ibmappnIsAcGlobal,
       "ibmappnIsAcGlobeStatus": ibmappnIsAcGlobeStatus,
       "ibmappnIsAcGlobeByteThresh": ibmappnIsAcGlobeByteThresh,
       "ibmappnIsAcGlobeCheckPt": ibmappnIsAcGlobeCheckPt,
       "ibmappnIsAcGlobeMgrUtcSecs": ibmappnIsAcGlobeMgrUtcSecs,
       "ibmappnIsAcGlobeMgrUtcMins": ibmappnIsAcGlobeMgrUtcMins,
       "ibmappnIsAcGlobeMgrUtcHours": ibmappnIsAcGlobeMgrUtcHours,
       "ibmappnIsAcGlobeMgrUtcMdays": ibmappnIsAcGlobeMgrUtcMdays,
       "ibmappnIsAcGlobeMgrUtcMonths": ibmappnIsAcGlobeMgrUtcMonths,
       "ibmappnIsAcGlobeMgrUtcYears": ibmappnIsAcGlobeMgrUtcYears,
       "ibmappnIsAcGlobeMgrUtcWdays": ibmappnIsAcGlobeMgrUtcWdays,
       "ibmappnIsAcGlobeMgrUtcYdays": ibmappnIsAcGlobeMgrUtcYdays,
       "ibmappnIsAcGlobeMgrUtcIsdst": ibmappnIsAcGlobeMgrUtcIsdst,
       "ibmappnIsAcGlobeMgrName": ibmappnIsAcGlobeMgrName,
       "ibmappnIsAcBtypeTable": ibmappnIsAcBtypeTable,
       "ibmappnIsAcBtypeEntry": ibmappnIsAcBtypeEntry,
       "ibmappnIsAcBtypeMedia": ibmappnIsAcBtypeMedia,
       "ibmappnIsAcBtypeActive": ibmappnIsAcBtypeActive,
       "ibmappnIsAcBtypeDirName": ibmappnIsAcBtypeDirName,
       "ibmappnIsAcBtypePrdMaxBufs": ibmappnIsAcBtypePrdMaxBufs,
       "ibmappnIsAcBtypeMaxBufs": ibmappnIsAcBtypeMaxBufs,
       "ibmappnIsAcBtypeCurBufs": ibmappnIsAcBtypeCurBufs,
       "ibmappnIsAcBtypePrdRecPerBuf": ibmappnIsAcBtypePrdRecPerBuf,
       "ibmappnIsAcBtypeRecPerBuf": ibmappnIsAcBtypeRecPerBuf,
       "ibmappnIsAcBtypeRecFormat": ibmappnIsAcBtypeRecFormat,
       "ibmappnIsAcBtypeFullAction": ibmappnIsAcBtypeFullAction,
       "ibmappnIsAcBtypeFullTime": ibmappnIsAcBtypeFullTime,
       "ibmappnIsAcBtypeFullReason": ibmappnIsAcBtypeFullReason,
       "ibmappnIsAcBtypeFullWraps": ibmappnIsAcBtypeFullWraps,
       "ibmappnIsAcBtypeFullLosts": ibmappnIsAcBtypeFullLosts,
       "ibmappnIsAcBtypeErrorWraps": ibmappnIsAcBtypeErrorWraps,
       "ibmappnIsAcBtypeErrorLosts": ibmappnIsAcBtypeErrorLosts,
       "ibmappnIsAcBtypeCheckPts": ibmappnIsAcBtypeCheckPts,
       "ibmappnIsAcBtypePurges": ibmappnIsAcBtypePurges,
       "ibmappnIsAcBtypeDeletes": ibmappnIsAcBtypeDeletes,
       "ibmappnIsAcBtypeResets": ibmappnIsAcBtypeResets,
       "ibmappnIsAcBtypeClearStats": ibmappnIsAcBtypeClearStats,
       "ibmappnIsAcBufTable": ibmappnIsAcBufTable,
       "ibmappnIsAcBufEntry": ibmappnIsAcBufEntry,
       "ibmappnIsAcBufMedia": ibmappnIsAcBufMedia,
       "ibmappnIsAcBufNumber": ibmappnIsAcBufNumber,
       "ibmappnIsAcBufState": ibmappnIsAcBufState,
       "ibmappnIsAcBufRecFormat": ibmappnIsAcBufRecFormat,
       "ibmappnIsAcBufMaxRecords": ibmappnIsAcBufMaxRecords,
       "ibmappnIsAcBufOldestIndex": ibmappnIsAcBufOldestIndex,
       "ibmappnIsAcBufNewestIndex": ibmappnIsAcBufNewestIndex,
       "ibmappnIsAcBufName": ibmappnIsAcBufName,
       "ibmappnIsAcTimeTable": ibmappnIsAcTimeTable,
       "ibmappnIsAcTimeEntry": ibmappnIsAcTimeEntry,
       "ibmappnIsAcTimeIndex": ibmappnIsAcTimeIndex,
       "ibmappnIsAcTimeEntryType": ibmappnIsAcTimeEntryType,
       "ibmappnIsAcTimeForMedia": ibmappnIsAcTimeForMedia,
       "ibmappnIsAcTimeRecTime": ibmappnIsAcTimeRecTime,
       "ibmappnIsAcTimeAgtUtcSecs": ibmappnIsAcTimeAgtUtcSecs,
       "ibmappnIsAcTimeAgtUtcMins": ibmappnIsAcTimeAgtUtcMins,
       "ibmappnIsAcTimeAgtUtcHours": ibmappnIsAcTimeAgtUtcHours,
       "ibmappnIsAcTimeAgtUtcMdays": ibmappnIsAcTimeAgtUtcMdays,
       "ibmappnIsAcTimeAgtUtcMonths": ibmappnIsAcTimeAgtUtcMonths,
       "ibmappnIsAcTimeAgtUtcYears": ibmappnIsAcTimeAgtUtcYears,
       "ibmappnIsAcTimeAgtUtcWdays": ibmappnIsAcTimeAgtUtcWdays,
       "ibmappnIsAcTimeAgtUtcYdays": ibmappnIsAcTimeAgtUtcYdays,
       "ibmappnIsAcTimeAgtUtcIsdst": ibmappnIsAcTimeAgtUtcIsdst,
       "ibmappnIsAcTimeAgtName": ibmappnIsAcTimeAgtName,
       "ibmappnIsAcTimeMgrUtcSecs": ibmappnIsAcTimeMgrUtcSecs,
       "ibmappnIsAcTimeMgrUtcMins": ibmappnIsAcTimeMgrUtcMins,
       "ibmappnIsAcTimeMgrUtcHours": ibmappnIsAcTimeMgrUtcHours,
       "ibmappnIsAcTimeMgrUtcMdays": ibmappnIsAcTimeMgrUtcMdays,
       "ibmappnIsAcTimeMgrUtcMonths": ibmappnIsAcTimeMgrUtcMonths,
       "ibmappnIsAcTimeMgrUtcYears": ibmappnIsAcTimeMgrUtcYears,
       "ibmappnIsAcTimeMgrUtcWdays": ibmappnIsAcTimeMgrUtcWdays,
       "ibmappnIsAcTimeMgrUtcYdays": ibmappnIsAcTimeMgrUtcYdays,
       "ibmappnIsAcTimeMgrUtcIsdst": ibmappnIsAcTimeMgrUtcIsdst,
       "ibmappnIsAcTimeMgrName": ibmappnIsAcTimeMgrName,
       "ibmappnIsAcTimeMgrTimeValid": ibmappnIsAcTimeMgrTimeValid,
       "ibmappnIsAcDataTable": ibmappnIsAcDataTable,
       "ibmappnIsAcDataEntry": ibmappnIsAcDataEntry,
       "ibmappnIsAcIndex": ibmappnIsAcIndex,
       "ibmappnIsAcEntryType": ibmappnIsAcEntryType,
       "ibmappnIsAcRecTime": ibmappnIsAcRecTime,
       "ibmappnIsAcFqLuName": ibmappnIsAcFqLuName,
       "ibmappnIsAcPcid": ibmappnIsAcPcid,
       "ibmappnIsAcPriLuName": ibmappnIsAcPriLuName,
       "ibmappnIsAcSecLuName": ibmappnIsAcSecLuName,
       "ibmappnIsAcModeName": ibmappnIsAcModeName,
       "ibmappnIsAcCosName": ibmappnIsAcCosName,
       "ibmappnIsAcTransPriority": ibmappnIsAcTransPriority,
       "ibmappnIsAcSessType": ibmappnIsAcSessType,
       "ibmappnIsAcSessState": ibmappnIsAcSessState,
       "ibmappnIsAcSessStartTime": ibmappnIsAcSessStartTime,
       "ibmappnIsAcSessUpTime": ibmappnIsAcSessUpTime,
       "ibmappnIsAcCtrUpTime": ibmappnIsAcCtrUpTime,
       "ibmappnIsAcEndReason": ibmappnIsAcEndReason,
       "ibmappnIsAcP2SFmdPius": ibmappnIsAcP2SFmdPius,
       "ibmappnIsAcS2PFmdPius": ibmappnIsAcS2PFmdPius,
       "ibmappnIsAcP2SNonFmdPius": ibmappnIsAcP2SNonFmdPius,
       "ibmappnIsAcS2PNonFmdPius": ibmappnIsAcS2PNonFmdPius,
       "ibmappnIsAcP2SFmdBytes": ibmappnIsAcP2SFmdBytes,
       "ibmappnIsAcS2PFmdBytes": ibmappnIsAcS2PFmdBytes,
       "ibmappnIsAcP2SNonFmdBytes": ibmappnIsAcP2SNonFmdBytes,
       "ibmappnIsAcS2PNonFmdBytes": ibmappnIsAcS2PNonFmdBytes,
       "ibmappnIsAcRouteInfo": ibmappnIsAcRouteInfo,
       "ibmappnConversation": ibmappnConversation,
       "ibmappnConvGeneral": ibmappnConvGeneral,
       "ibmappnConvEndPoint": ibmappnConvEndPoint,
       "ibmrpq": ibmrpq,
       "ibmtb": ibmtb,
       "ibmdot1dBase": ibmdot1dBase,
       "ibmdot1dBaseBridgeAddress": ibmdot1dBaseBridgeAddress,
       "ibmdot1dBaseNumPorts": ibmdot1dBaseNumPorts,
       "ibmdot1dBaseType": ibmdot1dBaseType,
       "ibmdot1dBasePortTable": ibmdot1dBasePortTable,
       "ibmdot1dBasePortEntry": ibmdot1dBasePortEntry,
       "ibmdot1dBasePort": ibmdot1dBasePort,
       "ibmdot1dBasePortIfIndex": ibmdot1dBasePortIfIndex,
       "ibmdot1dBasePortCircuit": ibmdot1dBasePortCircuit,
       "ibmdot1dBasePortDelayExceededDiscards": ibmdot1dBasePortDelayExceededDiscards,
       "ibmdot1dBasePortMtuExceededDiscards": ibmdot1dBasePortMtuExceededDiscards,
       "ibmdot1dStp": ibmdot1dStp,
       "ibmdot1dStpProtocolSpecification": ibmdot1dStpProtocolSpecification,
       "ibmdot1dStpPriority": ibmdot1dStpPriority,
       "ibmdot1dStpTimeSinceTopologyChange": ibmdot1dStpTimeSinceTopologyChange,
       "ibmdot1dStpTopChanges": ibmdot1dStpTopChanges,
       "ibmdot1dStpDesignatedRoot": ibmdot1dStpDesignatedRoot,
       "ibmdot1dStpRootCost": ibmdot1dStpRootCost,
       "ibmdot1dStpRootPort": ibmdot1dStpRootPort,
       "ibmdot1dStpMaxAge": ibmdot1dStpMaxAge,
       "ibmdot1dStpHelloTime": ibmdot1dStpHelloTime,
       "ibmdot1dStpHoldTime": ibmdot1dStpHoldTime,
       "ibmdot1dStpForwardDelay": ibmdot1dStpForwardDelay,
       "ibmdot1dStpBridgeMaxAge": ibmdot1dStpBridgeMaxAge,
       "ibmdot1dStpBridgeHelloTime": ibmdot1dStpBridgeHelloTime,
       "ibmdot1dStpBridgeForwardDelay": ibmdot1dStpBridgeForwardDelay,
       "ibmdot1dStpPortTable": ibmdot1dStpPortTable,
       "ibmdot1dStpPortEntry": ibmdot1dStpPortEntry,
       "ibmdot1dStpPort": ibmdot1dStpPort,
       "ibmdot1dStpPortPriority": ibmdot1dStpPortPriority,
       "ibmdot1dStpPortState": ibmdot1dStpPortState,
       "ibmdot1dStpPortEnable": ibmdot1dStpPortEnable,
       "ibmdot1dStpPortPathCost": ibmdot1dStpPortPathCost,
       "ibmdot1dStpPortDesignatedRoot": ibmdot1dStpPortDesignatedRoot,
       "ibmdot1dStpPortDesignatedCost": ibmdot1dStpPortDesignatedCost,
       "ibmdot1dStpPortDesignatedBridge": ibmdot1dStpPortDesignatedBridge,
       "ibmdot1dStpPortDesignatedPort": ibmdot1dStpPortDesignatedPort,
       "ibmdot1dStpPortForwardTransitions": ibmdot1dStpPortForwardTransitions,
       "ibmdot1dTp": ibmdot1dTp,
       "ibmdot1dTpLearnedEntryDiscards": ibmdot1dTpLearnedEntryDiscards,
       "ibmdot1dTpAgingTime": ibmdot1dTpAgingTime,
       "ibmdot1dTpFdbTable": ibmdot1dTpFdbTable,
       "ibmdot1dTpFdbEntry": ibmdot1dTpFdbEntry,
       "ibmdot1dTpFdbAddress": ibmdot1dTpFdbAddress,
       "ibmdot1dTpFdbPort": ibmdot1dTpFdbPort,
       "ibmdot1dTpFdbStatus": ibmdot1dTpFdbStatus,
       "ibmdot1dTpPortTable": ibmdot1dTpPortTable,
       "ibmdot1dTpPortEntry": ibmdot1dTpPortEntry,
       "ibmdot1dTpPort": ibmdot1dTpPort,
       "ibmdot1dTpPortMaxInfo": ibmdot1dTpPortMaxInfo,
       "ibmdot1dTpPortInFrames": ibmdot1dTpPortInFrames,
       "ibmdot1dTpPortOutFrames": ibmdot1dTpPortOutFrames,
       "ibmdot1dTpPortInDiscards": ibmdot1dTpPortInDiscards,
       "ibmdot1dStatic": ibmdot1dStatic,
       "ibmdot1dStaticTable": ibmdot1dStaticTable,
       "ibmdot1dStaticEntry": ibmdot1dStaticEntry,
       "ibmdot1dStaticAddress": ibmdot1dStaticAddress,
       "ibmdot1dStaticReceivePort": ibmdot1dStaticReceivePort,
       "ibmdot1dStaticAllowedToGoTo": ibmdot1dStaticAllowedToGoTo,
       "ibmdot1dStaticStatus": ibmdot1dStaticStatus,
       "ibmtbMACAddressFilters": ibmtbMACAddressFilters,
       "ibmtbmacFiltInfoTable": ibmtbmacFiltInfoTable,
       "ibmtbmacFiltInfoEntry": ibmtbmacFiltInfoEntry,
       "ibmtbmacFiltIfIndex": ibmtbmacFiltIfIndex,
       "ibmtbmacFiltInFilterType": ibmtbmacFiltInFilterType,
       "ibmtbmacFiltOutFilterType": ibmtbmacFiltOutFilterType,
       "ibmtbmacFiltInNotForwarded": ibmtbmacFiltInNotForwarded,
       "ibmtbmacFiltOutNotForwarded": ibmtbmacFiltOutNotForwarded,
       "ibmtbmacFiltInTable": ibmtbmacFiltInTable,
       "ibmtbmacFiltInEntry": ibmtbmacFiltInEntry,
       "ibmtbmacFiltInIfIndex": ibmtbmacFiltInIfIndex,
       "ibmtbmacFiltInSrcAddress": ibmtbmacFiltInSrcAddress,
       "ibmtbmacFiltInSrcMask": ibmtbmacFiltInSrcMask,
       "ibmtbmacFiltInDestAddress": ibmtbmacFiltInDestAddress,
       "ibmtbmacFiltInDestMask": ibmtbmacFiltInDestMask,
       "ibmtbmacFiltOutTable": ibmtbmacFiltOutTable,
       "ibmtbmacFiltOutEntry": ibmtbmacFiltOutEntry,
       "ibmtbmacFiltOutIfIndex": ibmtbmacFiltOutIfIndex,
       "ibmtbmacFiltOutSrcAddress": ibmtbmacFiltOutSrcAddress,
       "ibmtbmacFiltOutSrcMask": ibmtbmacFiltOutSrcMask,
       "ibmtbmacFiltOutDestAddress": ibmtbmacFiltOutDestAddress,
       "ibmtbmacFiltOutDestMask": ibmtbmacFiltOutDestMask,
       "ibmtbSAPFilters": ibmtbSAPFilters,
       "ibmtbsapFiltInfoTable": ibmtbsapFiltInfoTable,
       "ibmtbsapFiltInfoEntry": ibmtbsapFiltInfoEntry,
       "ibmtbsapFiltIfIndex": ibmtbsapFiltIfIndex,
       "ibmtbsapFiltIn": ibmtbsapFiltIn,
       "ibmtbsapFiltOut": ibmtbsapFiltOut,
       "ibmtbsapFiltInNotForwarded": ibmtbsapFiltInNotForwarded,
       "ibmtbsapFiltOutNotForwarded": ibmtbsapFiltOutNotForwarded,
       "ibmtbEthTypeFilters": ibmtbEthTypeFilters,
       "ibmtbEthTypeFiltInfoTable": ibmtbEthTypeFiltInfoTable,
       "ibmtbEthTypeFiltInfoEntry": ibmtbEthTypeFiltInfoEntry,
       "ibmtbEthTypeFiltIfIndex": ibmtbEthTypeFiltIfIndex,
       "ibmtbEthTypeFiltInFilterType": ibmtbEthTypeFiltInFilterType,
       "ibmtbEthTypeFiltOutFilterType": ibmtbEthTypeFiltOutFilterType,
       "ibmtbEthTypeFiltInNotForwarded": ibmtbEthTypeFiltInNotForwarded,
       "ibmtbEthTypeFiltOutNotForwarded": ibmtbEthTypeFiltOutNotForwarded,
       "ibmtbEthTypeFiltInTable": ibmtbEthTypeFiltInTable,
       "ibmtbEthTypeFiltInEntry": ibmtbEthTypeFiltInEntry,
       "ibmtbEthTypeFiltInIfIndex": ibmtbEthTypeFiltInIfIndex,
       "ibmtbEthTypeFiltInValue": ibmtbEthTypeFiltInValue,
       "ibmtbEthTypeFiltInMask": ibmtbEthTypeFiltInMask,
       "ibmtbEthTypeFiltOutTable": ibmtbEthTypeFiltOutTable,
       "ibmtbEthTypeFiltOutEntry": ibmtbEthTypeFiltOutEntry,
       "ibmtbEthTypeFiltOutIfIndex": ibmtbEthTypeFiltOutIfIndex,
       "ibmtbEthTypeFiltOutValue": ibmtbEthTypeFiltOutValue,
       "ibmtbEthTypeFiltOutMask": ibmtbEthTypeFiltOutMask,
       "ibmtbWindowFilters": ibmtbWindowFilters,
       "ibmtbwinFiltInfoTable": ibmtbwinFiltInfoTable,
       "ibmtbwinFiltInfoEntry": ibmtbwinFiltInfoEntry,
       "ibmtbwinFiltIfIndex": ibmtbwinFiltIfIndex,
       "ibmtbwinFiltInFilterType": ibmtbwinFiltInFilterType,
       "ibmtbwinFiltOutFilterType": ibmtbwinFiltOutFilterType,
       "ibmtbwinFiltInNotForwarded": ibmtbwinFiltInNotForwarded,
       "ibmtbwinFiltOutNotForwarded": ibmtbwinFiltOutNotForwarded,
       "ibmtbwinFiltInTable": ibmtbwinFiltInTable,
       "ibmtbwinFiltInEntry": ibmtbwinFiltInEntry,
       "ibmtbwinFiltInIfIndex": ibmtbwinFiltInIfIndex,
       "ibmtbwinFiltInContents": ibmtbwinFiltInContents,
       "ibmtbwinFiltInMaskString": ibmtbwinFiltInMaskString,
       "ibmtbwinFiltInOffsetStart": ibmtbwinFiltInOffsetStart,
       "ibmtbwinFiltInNumBytes": ibmtbwinFiltInNumBytes,
       "ibmtbwinFiltInOffset": ibmtbwinFiltInOffset,
       "ibmtbwinFiltInId": ibmtbwinFiltInId,
       "ibmtbwinFiltOutTable": ibmtbwinFiltOutTable,
       "ibmtbwinFiltOutEntry": ibmtbwinFiltOutEntry,
       "ibmtbwinFiltOutIfIndex": ibmtbwinFiltOutIfIndex,
       "ibmtbwinFiltOutContents": ibmtbwinFiltOutContents,
       "ibmtbwinFiltOutMaskString": ibmtbwinFiltOutMaskString,
       "ibmtbwinFiltOutOffsetStart": ibmtbwinFiltOutOffsetStart,
       "ibmtbwinFiltOutNumBytes": ibmtbwinFiltOutNumBytes,
       "ibmtbwinFiltOutOffset": ibmtbwinFiltOutOffset,
       "ibmtbwinFiltOutId": ibmtbwinFiltOutId,
       "ibmtbFiltOrderTable": ibmtbFiltOrderTable,
       "ibmtbFiltOrderInTable": ibmtbFiltOrderInTable,
       "ibmtbFiltOrderInEntry": ibmtbFiltOrderInEntry,
       "ibmtbFiltOrderInIfIndex": ibmtbFiltOrderInIfIndex,
       "ibmtbFiltOrderInPriority": ibmtbFiltOrderInPriority,
       "ibmtbFiltOrderInName": ibmtbFiltOrderInName,
       "ibmtbFiltOrderOutTable": ibmtbFiltOrderOutTable,
       "ibmtbFiltOrderOutEntry": ibmtbFiltOrderOutEntry,
       "ibmtbFiltOrderOutIfIndex": ibmtbFiltOrderOutIfIndex,
       "ibmtbFiltOrderOutPriority": ibmtbFiltOrderOutPriority,
       "ibmtbFiltOrderOutName": ibmtbFiltOrderOutName,
       "ibmapple": ibmapple,
       "ibmSelectNet": ibmSelectNet,
       "ibmSelectNetTable": ibmSelectNetTable,
       "ibmSelectNetEntry": ibmSelectNetEntry,
       "ibmSelectNetIndex": ibmSelectNetIndex,
       "ibmSelectNetZone": ibmSelectNetZone,
       "ibmSelectNetNetStart": ibmSelectNetNetStart,
       "ibmSelectNetNetEnd": ibmSelectNetNetEnd,
       "ibmSelectNetInterfaceNetStart": ibmSelectNetInterfaceNetStart,
       "ibmnbpFilter": ibmnbpFilter,
       "ibmnbpFilterPacketsFiltered": ibmnbpFilterPacketsFiltered,
       "ibmnbpFilterPacketsSent": ibmnbpFilterPacketsSent,
       "ibmatportFilter": ibmatportFilter,
       "ibmatportFilterTable": ibmatportFilterTable,
       "ibmatportFilterEntry": ibmatportFilterEntry,
       "ibmatportFilterIndex": ibmatportFilterIndex,
       "ibmatportFilterNetStart": ibmatportFilterNetStart,
       "ibmatportFilterNetEnd": ibmatportFilterNetEnd,
       "ibmSelectNetFilter": ibmSelectNetFilter,
       "ibmSelectNetFilterTable": ibmSelectNetFilterTable,
       "ibmSelectNetFilterEntry": ibmSelectNetFilterEntry,
       "ibmSelectNetFilterIndex": ibmSelectNetFilterIndex,
       "ibmSelectNetFilterNetStart": ibmSelectNetFilterNetStart,
       "ibmSelectNetFilterNetEnd": ibmSelectNetFilterNetEnd,
       "ibmdec": ibmdec,
       "ibmdecAllRoutersFuncAddr": ibmdecAllRoutersFuncAddr,
       "ibmdecAllEndNodesFuncAddr": ibmdecAllEndNodesFuncAddr,
       "ibmdecSplitHorPoisonRev": ibmdecSplitHorPoisonRev,
       "ibmdecNodeType": ibmdecNodeType,
       "ibmdecLANCircuitTable": ibmdecLANCircuitTable,
       "ibmdecLANCircuitEntry": ibmdecLANCircuitEntry,
       "ibmdecLANCircuitIndex": ibmdecLANCircuitIndex,
       "ibmdecLANCircuitType": ibmdecLANCircuitType,
       "ibmdecLANCircuitSourceRoute": ibmdecLANCircuitSourceRoute,
       "ibmdecLANCircuitAddrType": ibmdecLANCircuitAddrType,
       "ibmvines": ibmvines,
       "ibmvSysConfig": ibmvSysConfig,
       "ibmvSysRtr": ibmvSysRtr,
       "ibmvRouterName": ibmvRouterName,
       "ibmvRouterNetid": ibmvRouterNetid,
       "ibmvIP": ibmvIP,
       "ibmvipTotalIn": ibmvipTotalIn,
       "ibmvipTotalOut": ibmvipTotalOut,
       "ibmvipRouted": ibmvipRouted,
       "ibmvipBcast": ibmvipBcast,
       "ibmvipInReceives": ibmvipInReceives,
       "ibmvipBcastInReceives": ibmvipBcastInReceives,
       "ibmvipBad": ibmvipBad,
       "ibmvipBadHeaders": ibmvipBadHeaders,
       "ibmvipTooSmalls": ibmvipTooSmalls,
       "ibmvipBadLens": ibmvipBadLens,
       "ibmvipBadSums": ibmvipBadSums,
       "ibmvipInDiscards": ibmvipInDiscards,
       "ibmvipZeroHops": ibmvipZeroHops,
       "ibmvipOutNoRoutes": ibmvipOutNoRoutes,
       "ibmvNeighbor": ibmvNeighbor,
       "ibmvARP": ibmvARP,
       "ibmvarpQueryReqs": ibmvarpQueryReqs,
       "ibmvarpServiceResps": ibmvarpServiceResps,
       "ibmvarpAssignReqs": ibmvarpAssignReqs,
       "ibmvarpAssignResps": ibmvarpAssignResps,
       "ibmvarpHeaderError": ibmvarpHeaderError,
       "ibmvNbrNumber": ibmvNbrNumber,
       "ibmvNbrTable": ibmvNbrTable,
       "ibmvNbrEntry": ibmvNbrEntry,
       "ibmvNbrNetid": ibmvNbrNetid,
       "ibmvNbrSubNetid": ibmvNbrSubNetid,
       "ibmvNbrType": ibmvNbrType,
       "ibmvNbrIfType": ibmvNbrIfType,
       "ibmvNbrRemAddress": ibmvNbrRemAddress,
       "ibmvNbrLocAddress": ibmvNbrLocAddress,
       "ibmvNbrLocSlot": ibmvNbrLocSlot,
       "ibmvNbrLocPort": ibmvNbrLocPort,
       "ibmvNbrAging": ibmvNbrAging,
       "ibmvNbrFlags": ibmvNbrFlags,
       "ibmvNbrRIF": ibmvNbrRIF,
       "ibmvNbrIfIndex": ibmvNbrIfIndex,
       "ibmvNbrMetric": ibmvNbrMetric,
       "ibmvRouting": ibmvRouting,
       "ibmvRtConfig": ibmvRtConfig,
       "ibmvRtCfgMax": ibmvRtCfgMax,
       "ibmvRtCfgInFlt": ibmvRtCfgInFlt,
       "ibmvRtCfgInFltNum": ibmvRtCfgInFltNum,
       "ibmvRtCfgInFltTable": ibmvRtCfgInFltTable,
       "ibmvRtCfgInFltEntry": ibmvRtCfgInFltEntry,
       "ibmvRtCfgInFltNetID": ibmvRtCfgInFltNetID,
       "ibmvRtCfgInFltIfIndex": ibmvRtCfgInFltIfIndex,
       "ibmvRtCfgInFltMode": ibmvRtCfgInFltMode,
       "ibmvRtCfgInFltUses": ibmvRtCfgInFltUses,
       "ibmvRtCfgOutFlt": ibmvRtCfgOutFlt,
       "ibmvRtCfgOutFltNum": ibmvRtCfgOutFltNum,
       "ibmvRtCfgOutFltTable": ibmvRtCfgOutFltTable,
       "ibmvRtCfgOutFltEntry": ibmvRtCfgOutFltEntry,
       "ibmvRtCfgOutFltNetID": ibmvRtCfgOutFltNetID,
       "ibmvRtCfgOutFltIfIndex": ibmvRtCfgOutFltIfIndex,
       "ibmvRtCfgOutFltMode": ibmvRtCfgOutFltMode,
       "ibmvRtCfgOutFltUses": ibmvRtCfgOutFltUses,
       "ibmvRtCfgFlt": ibmvRtCfgFlt,
       "ibmvRtCfgFltNum": ibmvRtCfgFltNum,
       "ibmvRtCfgFltTable": ibmvRtCfgFltTable,
       "ibmvRtCfgFltEntry": ibmvRtCfgFltEntry,
       "ibmvRtCfgFltNetID": ibmvRtCfgFltNetID,
       "ibmvRtCfgFltMode": ibmvRtCfgFltMode,
       "ibmvRtCfgFltUses": ibmvRtCfgFltUses,
       "ibmvRTP": ibmvRTP,
       "ibmvrtpUpdSents": ibmvrtpUpdSents,
       "ibmvrtpUpdRecs": ibmvrtpUpdRecs,
       "ibmvrtpReqSents": ibmvrtpReqSents,
       "ibmvrtpReqRecs": ibmvrtpReqRecs,
       "ibmvrtpResSents": ibmvrtpResSents,
       "ibmvrtpResRecs": ibmvrtpResRecs,
       "ibmvrtpRedSents": ibmvrtpRedSents,
       "ibmvrtpRedRecs": ibmvrtpRedRecs,
       "ibmvrtpHeaderError": ibmvrtpHeaderError,
       "ibmvRtNumber": ibmvRtNumber,
       "ibmvRtTable": ibmvRtTable,
       "ibmvRtEntry": ibmvRtEntry,
       "ibmvRtNetid": ibmvRtNetid,
       "ibmvRtMetric": ibmvRtMetric,
       "ibmvRtIdle": ibmvRtIdle,
       "ibmvRtGateNetid": ibmvRtGateNetid,
       "ibmvRtIfIndex": ibmvRtIfIndex,
       "ibmvRtState": ibmvRtState,
       "ibmvICP": ibmvICP,
       "ibmvicpExcGens": ibmvicpExcGens,
       "ibmvicpMetricGens": ibmvicpMetricGens,
       "ibmvicpHeaderError": ibmvicpHeaderError,
       "ibmvFRP": ibmvFRP,
       "ibmvFRPreassembles": ibmvFRPreassembles,
       "ibmvFRPfragsReassembled": ibmvFRPfragsReassembled,
       "ibmvFRPreasFails": ibmvFRPreasFails,
       "ibmvFRPfragmented": ibmvFRPfragmented,
       "ibmvFRPfrgCreated": ibmvFRPfrgCreated,
       "ibmvFRPfrgFails": ibmvFRPfrgFails,
       "ibmvInterface": ibmvInterface,
       "ibmvPortCfgTable": ibmvPortCfgTable,
       "ibmvPortCfgEntry": ibmvPortCfgEntry,
       "ibmvPortCfgIfIndex": ibmvPortCfgIfIndex,
       "ibmvPortCfgARP": ibmvPortCfgARP,
       "ibmvPortCfgServ": ibmvPortCfgServ,
       "ibmvPortCfgHCtoServ": ibmvPortCfgHCtoServ,
       "ibmvPortCfgPerUpdate": ibmvPortCfgPerUpdate,
       "ibmvPortCfgMetric": ibmvPortCfgMetric,
       "ibmvPortCfgTR": ibmvPortCfgTR,
       "ibmvPortCfgEN": ibmvPortCfgEN,
       "ibmvPortCfgInFlt": ibmvPortCfgInFlt,
       "ibmvPortCfgInFltNum": ibmvPortCfgInFltNum,
       "ibmvPortCfgOutFlt": ibmvPortCfgOutFlt,
       "ibmvPortCfgOutFltNum": ibmvPortCfgOutFltNum,
       "ibmvFltTable": ibmvFltTable,
       "ibmvFltEntry": ibmvFltEntry,
       "ibmvFltIfIndex": ibmvFltIfIndex,
       "ibmvFltNo": ibmvFltNo,
       "ibmvFltMode": ibmvFltMode,
       "ibmvFltValue": ibmvFltValue,
       "ibmvFltMask": ibmvFltMask,
       "ibmvFltType": ibmvFltType,
       "ibmvFltHCCompare": ibmvFltHCCompare,
       "ibmvFltUses": ibmvFltUses,
       "ibmvifNumber": ibmvifNumber,
       "ibmvifTable": ibmvifTable,
       "ibmvifEntry": ibmvifEntry,
       "ibmvifSlot": ibmvifSlot,
       "ibmvifPort": ibmvifPort,
       "ibmvifDescr": ibmvifDescr,
       "ibmvifAddress": ibmvifAddress,
       "ibmvifInPkts": ibmvifInPkts,
       "ibmvifInErrs": ibmvifInErrs,
       "ibmvifOutPkts": ibmvifOutPkts,
       "ibmvifOutErrs": ibmvifOutErrs,
       "ibminterfaces": ibminterfaces,
       "ibmipext": ibmipext,
       "ibmipPtyQueueEnableTable": ibmipPtyQueueEnableTable,
       "ibmipPtyQueueEnableEntry": ibmipPtyQueueEnableEntry,
       "ibmipPtyQueueEnableIfIndex": ibmipPtyQueueEnableIfIndex,
       "ibmipPtyQueueEnable": ibmipPtyQueueEnable,
       "ibmipPtyQueueDefault": ibmipPtyQueueDefault,
       "ibmipPtyQueueTable": ibmipPtyQueueTable,
       "ibmipPtyQueueEntry": ibmipPtyQueueEntry,
       "ibmipPtyQueueIfIndex": ibmipPtyQueueIfIndex,
       "ibmipPtyQueuePort": ibmipPtyQueuePort,
       "ibmipPtyQueueType": ibmipPtyQueueType,
       "ibmipPtyQueueNumber": ibmipPtyQueueNumber,
       "ibmipFilterTable": ibmipFilterTable,
       "ibmipFilterEntry": ibmipFilterEntry,
       "ibmipFilterIfIndex": ibmipFilterIfIndex,
       "ibmipFilterId": ibmipFilterId,
       "ibmipFilterScope": ibmipFilterScope,
       "ibmipFilterType": ibmipFilterType,
       "ibmipPermitDeny": ibmipPermitDeny,
       "ibmipFilterAddr1": ibmipFilterAddr1,
       "ibmipFilterMask1": ibmipFilterMask1,
       "ibmipFilterAddr2": ibmipFilterAddr2,
       "ibmipFilterMask2": ibmipFilterMask2,
       "ibmipFilterExtTable": ibmipFilterExtTable,
       "ibmipFilterExtEntry": ibmipFilterExtEntry,
       "ibmipFilterExtIfIndex": ibmipFilterExtIfIndex,
       "ibmipFilterExtFilterId": ibmipFilterExtFilterId,
       "ibmipFilterExtValue": ibmipFilterExtValue,
       "ibmipFilterExtProtocol": ibmipFilterExtProtocol,
       "ibmptyqueue": ibmptyqueue,
       "ibmPtyQueueingTable": ibmPtyQueueingTable,
       "ibmPtyQueueingEntry": ibmPtyQueueingEntry,
       "ibmPtyQueueingIfIndex": ibmPtyQueueingIfIndex,
       "ibmPtyQueueingQnum": ibmPtyQueueingQnum,
       "ibmPtyQueueingLBA": ibmPtyQueueingLBA,
       "ibmPtyQueueingQBR": ibmPtyQueueingQBR,
       "ibmPtyQueueingDiscards": ibmPtyQueueingDiscards,
       "ibmTG": ibmTG,
       "ibmTGTable": ibmTGTable,
       "ibmTGEntry": ibmTGEntry,
       "ibmTGProtocol": ibmTGProtocol,
       "ibmTGIfIndex": ibmTGIfIndex,
       "ibmTGEnable": ibmTGEnable,
       "ibmTGGroupName": ibmTGGroupName,
       "ibmTGSwitchOuts": ibmTGSwitchOuts}
)
