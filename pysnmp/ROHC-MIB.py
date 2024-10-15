# SNMP MIB module (ROHC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ROHC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:09 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rohcMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 112)
)
rohcMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RohcChannelIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class RohcChannelIdentifierOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class RohcCompressionRatio(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_RohcObjects_ObjectIdentity = ObjectIdentity
rohcObjects = _RohcObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 112, 1)
)
_RohcInstanceObjects_ObjectIdentity = ObjectIdentity
rohcInstanceObjects = _RohcInstanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 112, 1, 1)
)
_RohcChannelTable_Object = MibTable
rohcChannelTable = _RohcChannelTable_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rohcChannelTable.setStatus("current")
_RohcChannelEntry_Object = MibTableRow
rohcChannelEntry = _RohcChannelEntry_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1)
)
rohcChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ROHC-MIB", "rohcChannelID"),
)
if mibBuilder.loadTexts:
    rohcChannelEntry.setStatus("current")
_RohcChannelID_Type = RohcChannelIdentifier
_RohcChannelID_Object = MibTableColumn
rohcChannelID = _RohcChannelID_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 2),
    _RohcChannelID_Type()
)
rohcChannelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rohcChannelID.setStatus("current")


class _RohcChannelType_Type(Integer32):
    """Custom type rohcChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedFeedback", 3),
          ("notInUse", 1),
          ("rohc", 2))
    )


_RohcChannelType_Type.__name__ = "Integer32"
_RohcChannelType_Object = MibTableColumn
rohcChannelType = _RohcChannelType_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 3),
    _RohcChannelType_Type()
)
rohcChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcChannelType.setStatus("current")
_RohcChannelFeedbackFor_Type = RohcChannelIdentifierOrZero
_RohcChannelFeedbackFor_Object = MibTableColumn
rohcChannelFeedbackFor = _RohcChannelFeedbackFor_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 4),
    _RohcChannelFeedbackFor_Type()
)
rohcChannelFeedbackFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcChannelFeedbackFor.setStatus("current")
_RohcChannelDescr_Type = SnmpAdminString
_RohcChannelDescr_Object = MibTableColumn
rohcChannelDescr = _RohcChannelDescr_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 5),
    _RohcChannelDescr_Type()
)
rohcChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcChannelDescr.setStatus("current")


class _RohcChannelStatus_Type(Integer32):
    """Custom type rohcChannelStatus based on Integer32"""
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


_RohcChannelStatus_Type.__name__ = "Integer32"
_RohcChannelStatus_Object = MibTableColumn
rohcChannelStatus = _RohcChannelStatus_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 6),
    _RohcChannelStatus_Type()
)
rohcChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcChannelStatus.setStatus("current")
_RohcInstanceTable_Object = MibTable
rohcInstanceTable = _RohcInstanceTable_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rohcInstanceTable.setStatus("current")
_RohcInstanceEntry_Object = MibTableRow
rohcInstanceEntry = _RohcInstanceEntry_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1)
)
rohcInstanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ROHC-MIB", "rohcInstanceType"),
    (0, "ROHC-MIB", "rohcChannelID"),
)
if mibBuilder.loadTexts:
    rohcInstanceEntry.setStatus("current")


class _RohcInstanceType_Type(Integer32):
    """Custom type rohcInstanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compressor", 1),
          ("decompressor", 2))
    )


_RohcInstanceType_Type.__name__ = "Integer32"
_RohcInstanceType_Object = MibTableColumn
rohcInstanceType = _RohcInstanceType_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 2),
    _RohcInstanceType_Type()
)
rohcInstanceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rohcInstanceType.setStatus("current")
_RohcInstanceFBChannelID_Type = RohcChannelIdentifierOrZero
_RohcInstanceFBChannelID_Object = MibTableColumn
rohcInstanceFBChannelID = _RohcInstanceFBChannelID_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 4),
    _RohcInstanceFBChannelID_Type()
)
rohcInstanceFBChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceFBChannelID.setStatus("current")
_RohcInstanceVendor_Type = ObjectIdentifier
_RohcInstanceVendor_Object = MibTableColumn
rohcInstanceVendor = _RohcInstanceVendor_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 5),
    _RohcInstanceVendor_Type()
)
rohcInstanceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceVendor.setStatus("current")


class _RohcInstanceVersion_Type(SnmpAdminString):
    """Custom type rohcInstanceVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RohcInstanceVersion_Type.__name__ = "SnmpAdminString"
_RohcInstanceVersion_Object = MibTableColumn
rohcInstanceVersion = _RohcInstanceVersion_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 6),
    _RohcInstanceVersion_Type()
)
rohcInstanceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceVersion.setStatus("current")
_RohcInstanceDescr_Type = SnmpAdminString
_RohcInstanceDescr_Object = MibTableColumn
rohcInstanceDescr = _RohcInstanceDescr_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 7),
    _RohcInstanceDescr_Type()
)
rohcInstanceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceDescr.setStatus("current")
_RohcInstanceClockRes_Type = Unsigned32
_RohcInstanceClockRes_Object = MibTableColumn
rohcInstanceClockRes = _RohcInstanceClockRes_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 8),
    _RohcInstanceClockRes_Type()
)
rohcInstanceClockRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceClockRes.setStatus("current")
if mibBuilder.loadTexts:
    rohcInstanceClockRes.setUnits("milliseconds")


class _RohcInstanceMaxCID_Type(Unsigned32):
    """Custom type rohcInstanceMaxCID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_RohcInstanceMaxCID_Type.__name__ = "Unsigned32"
_RohcInstanceMaxCID_Object = MibTableColumn
rohcInstanceMaxCID = _RohcInstanceMaxCID_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 9),
    _RohcInstanceMaxCID_Type()
)
rohcInstanceMaxCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceMaxCID.setStatus("current")
_RohcInstanceLargeCIDs_Type = TruthValue
_RohcInstanceLargeCIDs_Object = MibTableColumn
rohcInstanceLargeCIDs = _RohcInstanceLargeCIDs_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 10),
    _RohcInstanceLargeCIDs_Type()
)
rohcInstanceLargeCIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceLargeCIDs.setStatus("current")
_RohcInstanceMRRU_Type = Unsigned32
_RohcInstanceMRRU_Object = MibTableColumn
rohcInstanceMRRU = _RohcInstanceMRRU_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 11),
    _RohcInstanceMRRU_Type()
)
rohcInstanceMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceMRRU.setStatus("current")


class _RohcInstanceContextStorageTime_Type(TimeInterval):
    """Custom type rohcInstanceContextStorageTime based on TimeInterval"""
    defaultValue = 360000


_RohcInstanceContextStorageTime_Object = MibTableColumn
rohcInstanceContextStorageTime = _RohcInstanceContextStorageTime_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 12),
    _RohcInstanceContextStorageTime_Type()
)
rohcInstanceContextStorageTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rohcInstanceContextStorageTime.setStatus("current")
if mibBuilder.loadTexts:
    rohcInstanceContextStorageTime.setUnits("centi-seconds")


class _RohcInstanceStatus_Type(Integer32):
    """Custom type rohcInstanceStatus based on Integer32"""
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


_RohcInstanceStatus_Type.__name__ = "Integer32"
_RohcInstanceStatus_Object = MibTableColumn
rohcInstanceStatus = _RohcInstanceStatus_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 13),
    _RohcInstanceStatus_Type()
)
rohcInstanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceStatus.setStatus("current")
_RohcInstanceContextsTotal_Type = Counter32
_RohcInstanceContextsTotal_Object = MibTableColumn
rohcInstanceContextsTotal = _RohcInstanceContextsTotal_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 14),
    _RohcInstanceContextsTotal_Type()
)
rohcInstanceContextsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceContextsTotal.setStatus("current")
_RohcInstanceContextsCurrent_Type = Unsigned32
_RohcInstanceContextsCurrent_Object = MibTableColumn
rohcInstanceContextsCurrent = _RohcInstanceContextsCurrent_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 15),
    _RohcInstanceContextsCurrent_Type()
)
rohcInstanceContextsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceContextsCurrent.setStatus("current")
_RohcInstancePackets_Type = Counter32
_RohcInstancePackets_Object = MibTableColumn
rohcInstancePackets = _RohcInstancePackets_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 16),
    _RohcInstancePackets_Type()
)
rohcInstancePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstancePackets.setStatus("current")
_RohcInstanceIRs_Type = Counter32
_RohcInstanceIRs_Object = MibTableColumn
rohcInstanceIRs = _RohcInstanceIRs_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 17),
    _RohcInstanceIRs_Type()
)
rohcInstanceIRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceIRs.setStatus("current")
_RohcInstanceIRDYNs_Type = Counter32
_RohcInstanceIRDYNs_Object = MibTableColumn
rohcInstanceIRDYNs = _RohcInstanceIRDYNs_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 18),
    _RohcInstanceIRDYNs_Type()
)
rohcInstanceIRDYNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceIRDYNs.setStatus("current")
_RohcInstanceFeedbacks_Type = Counter32
_RohcInstanceFeedbacks_Object = MibTableColumn
rohcInstanceFeedbacks = _RohcInstanceFeedbacks_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 19),
    _RohcInstanceFeedbacks_Type()
)
rohcInstanceFeedbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceFeedbacks.setStatus("current")
_RohcInstanceCompressionRatio_Type = RohcCompressionRatio
_RohcInstanceCompressionRatio_Object = MibTableColumn
rohcInstanceCompressionRatio = _RohcInstanceCompressionRatio_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 20),
    _RohcInstanceCompressionRatio_Type()
)
rohcInstanceCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcInstanceCompressionRatio.setStatus("current")
_RohcProfileTable_Object = MibTable
rohcProfileTable = _RohcProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rohcProfileTable.setStatus("current")
_RohcProfileEntry_Object = MibTableRow
rohcProfileEntry = _RohcProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1)
)
rohcProfileEntry.setIndexNames(
    (0, "ROHC-MIB", "rohcChannelID"),
    (0, "ROHC-MIB", "rohcProfile"),
)
if mibBuilder.loadTexts:
    rohcProfileEntry.setStatus("current")


class _RohcProfile_Type(Unsigned32):
    """Custom type rohcProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RohcProfile_Type.__name__ = "Unsigned32"
_RohcProfile_Object = MibTableColumn
rohcProfile = _RohcProfile_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 2),
    _RohcProfile_Type()
)
rohcProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rohcProfile.setStatus("current")
_RohcProfileVendor_Type = ObjectIdentifier
_RohcProfileVendor_Object = MibTableColumn
rohcProfileVendor = _RohcProfileVendor_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 3),
    _RohcProfileVendor_Type()
)
rohcProfileVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcProfileVendor.setStatus("current")


class _RohcProfileVersion_Type(SnmpAdminString):
    """Custom type rohcProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RohcProfileVersion_Type.__name__ = "SnmpAdminString"
_RohcProfileVersion_Object = MibTableColumn
rohcProfileVersion = _RohcProfileVersion_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 4),
    _RohcProfileVersion_Type()
)
rohcProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcProfileVersion.setStatus("current")
_RohcProfileDescr_Type = SnmpAdminString
_RohcProfileDescr_Object = MibTableColumn
rohcProfileDescr = _RohcProfileDescr_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 5),
    _RohcProfileDescr_Type()
)
rohcProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcProfileDescr.setStatus("current")
_RohcProfileNegotiated_Type = TruthValue
_RohcProfileNegotiated_Object = MibTableColumn
rohcProfileNegotiated = _RohcProfileNegotiated_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 6),
    _RohcProfileNegotiated_Type()
)
rohcProfileNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcProfileNegotiated.setStatus("current")
_RohcContextTable_Object = MibTable
rohcContextTable = _RohcContextTable_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2)
)
if mibBuilder.loadTexts:
    rohcContextTable.setStatus("current")
_RohcContextEntry_Object = MibTableRow
rohcContextEntry = _RohcContextEntry_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1)
)
rohcContextEntry.setIndexNames(
    (0, "ROHC-MIB", "rohcChannelID"),
    (0, "ROHC-MIB", "rohcContextCID"),
)
if mibBuilder.loadTexts:
    rohcContextEntry.setStatus("current")


class _RohcContextCID_Type(Unsigned32):
    """Custom type rohcContextCID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_RohcContextCID_Type.__name__ = "Unsigned32"
_RohcContextCID_Object = MibTableColumn
rohcContextCID = _RohcContextCID_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 2),
    _RohcContextCID_Type()
)
rohcContextCID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rohcContextCID.setStatus("current")


class _RohcContextCIDState_Type(Integer32):
    """Custom type rohcContextCIDState based on Integer32"""
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
        *(("active", 2),
          ("expired", 3),
          ("terminated", 4),
          ("unused", 1))
    )


_RohcContextCIDState_Type.__name__ = "Integer32"
_RohcContextCIDState_Object = MibTableColumn
rohcContextCIDState = _RohcContextCIDState_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 3),
    _RohcContextCIDState_Type()
)
rohcContextCIDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextCIDState.setStatus("current")


class _RohcContextProfile_Type(Unsigned32):
    """Custom type rohcContextProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RohcContextProfile_Type.__name__ = "Unsigned32"
_RohcContextProfile_Object = MibTableColumn
rohcContextProfile = _RohcContextProfile_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 4),
    _RohcContextProfile_Type()
)
rohcContextProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextProfile.setStatus("current")
_RohcContextDecompressorDepth_Type = Unsigned32
_RohcContextDecompressorDepth_Object = MibTableColumn
rohcContextDecompressorDepth = _RohcContextDecompressorDepth_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 5),
    _RohcContextDecompressorDepth_Type()
)
rohcContextDecompressorDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextDecompressorDepth.setStatus("current")
_RohcContextStorageTime_Type = TimeInterval
_RohcContextStorageTime_Object = MibTableColumn
rohcContextStorageTime = _RohcContextStorageTime_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 6),
    _RohcContextStorageTime_Type()
)
rohcContextStorageTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rohcContextStorageTime.setStatus("current")
if mibBuilder.loadTexts:
    rohcContextStorageTime.setUnits("centi-seconds")


class _RohcContextActivationTime_Type(DateAndTime):
    """Custom type rohcContextActivationTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_RohcContextActivationTime_Object = MibTableColumn
rohcContextActivationTime = _RohcContextActivationTime_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 7),
    _RohcContextActivationTime_Type()
)
rohcContextActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextActivationTime.setStatus("current")


class _RohcContextDeactivationTime_Type(DateAndTime):
    """Custom type rohcContextDeactivationTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_RohcContextDeactivationTime_Object = MibTableColumn
rohcContextDeactivationTime = _RohcContextDeactivationTime_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 8),
    _RohcContextDeactivationTime_Type()
)
rohcContextDeactivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextDeactivationTime.setStatus("current")
_RohcContextPackets_Type = Counter32
_RohcContextPackets_Object = MibTableColumn
rohcContextPackets = _RohcContextPackets_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 9),
    _RohcContextPackets_Type()
)
rohcContextPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextPackets.setStatus("current")
_RohcContextIRs_Type = Counter32
_RohcContextIRs_Object = MibTableColumn
rohcContextIRs = _RohcContextIRs_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 10),
    _RohcContextIRs_Type()
)
rohcContextIRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextIRs.setStatus("current")
_RohcContextIRDYNs_Type = Counter32
_RohcContextIRDYNs_Object = MibTableColumn
rohcContextIRDYNs = _RohcContextIRDYNs_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 11),
    _RohcContextIRDYNs_Type()
)
rohcContextIRDYNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextIRDYNs.setStatus("current")
_RohcContextFeedbacks_Type = Counter32
_RohcContextFeedbacks_Object = MibTableColumn
rohcContextFeedbacks = _RohcContextFeedbacks_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 12),
    _RohcContextFeedbacks_Type()
)
rohcContextFeedbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextFeedbacks.setStatus("current")
_RohcContextDecompressorFailures_Type = Counter32
_RohcContextDecompressorFailures_Object = MibTableColumn
rohcContextDecompressorFailures = _RohcContextDecompressorFailures_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 13),
    _RohcContextDecompressorFailures_Type()
)
rohcContextDecompressorFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextDecompressorFailures.setStatus("current")
_RohcContextDecompressorRepairs_Type = Counter32
_RohcContextDecompressorRepairs_Object = MibTableColumn
rohcContextDecompressorRepairs = _RohcContextDecompressorRepairs_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 14),
    _RohcContextDecompressorRepairs_Type()
)
rohcContextDecompressorRepairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextDecompressorRepairs.setStatus("current")
_RohcContextAllPacketsRatio_Type = RohcCompressionRatio
_RohcContextAllPacketsRatio_Object = MibTableColumn
rohcContextAllPacketsRatio = _RohcContextAllPacketsRatio_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 15),
    _RohcContextAllPacketsRatio_Type()
)
rohcContextAllPacketsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextAllPacketsRatio.setStatus("current")
_RohcContextAllHeadersRatio_Type = RohcCompressionRatio
_RohcContextAllHeadersRatio_Object = MibTableColumn
rohcContextAllHeadersRatio = _RohcContextAllHeadersRatio_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 16),
    _RohcContextAllHeadersRatio_Type()
)
rohcContextAllHeadersRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextAllHeadersRatio.setStatus("current")
_RohcContextAllPacketsMeanSize_Type = Unsigned32
_RohcContextAllPacketsMeanSize_Object = MibTableColumn
rohcContextAllPacketsMeanSize = _RohcContextAllPacketsMeanSize_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 17),
    _RohcContextAllPacketsMeanSize_Type()
)
rohcContextAllPacketsMeanSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextAllPacketsMeanSize.setStatus("current")
_RohcContextAllHeadersMeanSize_Type = Unsigned32
_RohcContextAllHeadersMeanSize_Object = MibTableColumn
rohcContextAllHeadersMeanSize = _RohcContextAllHeadersMeanSize_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 18),
    _RohcContextAllHeadersMeanSize_Type()
)
rohcContextAllHeadersMeanSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextAllHeadersMeanSize.setStatus("current")
_RohcContextLastPacketsRatio_Type = RohcCompressionRatio
_RohcContextLastPacketsRatio_Object = MibTableColumn
rohcContextLastPacketsRatio = _RohcContextLastPacketsRatio_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 19),
    _RohcContextLastPacketsRatio_Type()
)
rohcContextLastPacketsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextLastPacketsRatio.setStatus("current")
_RohcContextLastHeadersRatio_Type = RohcCompressionRatio
_RohcContextLastHeadersRatio_Object = MibTableColumn
rohcContextLastHeadersRatio = _RohcContextLastHeadersRatio_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 20),
    _RohcContextLastHeadersRatio_Type()
)
rohcContextLastHeadersRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextLastHeadersRatio.setStatus("current")
_RohcContextLastPacketsMeanSize_Type = Unsigned32
_RohcContextLastPacketsMeanSize_Object = MibTableColumn
rohcContextLastPacketsMeanSize = _RohcContextLastPacketsMeanSize_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 21),
    _RohcContextLastPacketsMeanSize_Type()
)
rohcContextLastPacketsMeanSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextLastPacketsMeanSize.setStatus("current")
_RohcContextLastHeadersMeanSize_Type = Unsigned32
_RohcContextLastHeadersMeanSize_Object = MibTableColumn
rohcContextLastHeadersMeanSize = _RohcContextLastHeadersMeanSize_Object(
    (1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 22),
    _RohcContextLastHeadersMeanSize_Type()
)
rohcContextLastHeadersMeanSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rohcContextLastHeadersMeanSize.setStatus("current")
_RohcConformance_ObjectIdentity = ObjectIdentity
rohcConformance = _RohcConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 112, 2)
)
_RohcCompliances_ObjectIdentity = ObjectIdentity
rohcCompliances = _RohcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 112, 2, 1)
)
_RohcGroups_ObjectIdentity = ObjectIdentity
rohcGroups = _RohcGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 112, 2, 2)
)

# Managed Objects groups

rohcInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 112, 2, 2, 2)
)
rohcInstanceGroup.setObjects(
      *(("ROHC-MIB", "rohcChannelType"),
        ("ROHC-MIB", "rohcChannelFeedbackFor"),
        ("ROHC-MIB", "rohcChannelDescr"),
        ("ROHC-MIB", "rohcChannelStatus"),
        ("ROHC-MIB", "rohcInstanceFBChannelID"),
        ("ROHC-MIB", "rohcInstanceVendor"),
        ("ROHC-MIB", "rohcInstanceVersion"),
        ("ROHC-MIB", "rohcInstanceDescr"),
        ("ROHC-MIB", "rohcInstanceClockRes"),
        ("ROHC-MIB", "rohcInstanceMaxCID"),
        ("ROHC-MIB", "rohcInstanceLargeCIDs"),
        ("ROHC-MIB", "rohcInstanceMRRU"),
        ("ROHC-MIB", "rohcInstanceStatus"),
        ("ROHC-MIB", "rohcProfileVendor"),
        ("ROHC-MIB", "rohcProfileVersion"),
        ("ROHC-MIB", "rohcProfileDescr"),
        ("ROHC-MIB", "rohcProfileNegotiated"))
)
if mibBuilder.loadTexts:
    rohcInstanceGroup.setStatus("current")

rohcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 112, 2, 2, 4)
)
rohcStatisticsGroup.setObjects(
      *(("ROHC-MIB", "rohcInstanceContextsTotal"),
        ("ROHC-MIB", "rohcInstanceContextsCurrent"),
        ("ROHC-MIB", "rohcInstancePackets"),
        ("ROHC-MIB", "rohcInstanceIRs"),
        ("ROHC-MIB", "rohcInstanceIRDYNs"),
        ("ROHC-MIB", "rohcInstanceFeedbacks"),
        ("ROHC-MIB", "rohcInstanceCompressionRatio"))
)
if mibBuilder.loadTexts:
    rohcStatisticsGroup.setStatus("current")

rohcContextGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 112, 2, 2, 5)
)
rohcContextGroup.setObjects(
      *(("ROHC-MIB", "rohcContextCIDState"),
        ("ROHC-MIB", "rohcContextProfile"),
        ("ROHC-MIB", "rohcContextDecompressorDepth"))
)
if mibBuilder.loadTexts:
    rohcContextGroup.setStatus("current")

rohcTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 112, 2, 2, 6)
)
rohcTimerGroup.setObjects(
      *(("ROHC-MIB", "rohcInstanceContextStorageTime"),
        ("ROHC-MIB", "rohcContextStorageTime"),
        ("ROHC-MIB", "rohcContextActivationTime"),
        ("ROHC-MIB", "rohcContextDeactivationTime"))
)
if mibBuilder.loadTexts:
    rohcTimerGroup.setStatus("current")

rohcContextStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 112, 2, 2, 7)
)
rohcContextStatisticsGroup.setObjects(
      *(("ROHC-MIB", "rohcContextPackets"),
        ("ROHC-MIB", "rohcContextIRs"),
        ("ROHC-MIB", "rohcContextIRDYNs"),
        ("ROHC-MIB", "rohcContextFeedbacks"),
        ("ROHC-MIB", "rohcContextDecompressorFailures"),
        ("ROHC-MIB", "rohcContextDecompressorRepairs"),
        ("ROHC-MIB", "rohcContextAllPacketsRatio"),
        ("ROHC-MIB", "rohcContextAllHeadersRatio"),
        ("ROHC-MIB", "rohcContextAllPacketsMeanSize"),
        ("ROHC-MIB", "rohcContextAllHeadersMeanSize"),
        ("ROHC-MIB", "rohcContextLastPacketsRatio"),
        ("ROHC-MIB", "rohcContextLastHeadersRatio"),
        ("ROHC-MIB", "rohcContextLastPacketsMeanSize"),
        ("ROHC-MIB", "rohcContextLastHeadersMeanSize"))
)
if mibBuilder.loadTexts:
    rohcContextStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rohcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 112, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rohcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROHC-MIB",
    **{"RohcChannelIdentifier": RohcChannelIdentifier,
       "RohcChannelIdentifierOrZero": RohcChannelIdentifierOrZero,
       "RohcCompressionRatio": RohcCompressionRatio,
       "rohcMIB": rohcMIB,
       "rohcObjects": rohcObjects,
       "rohcInstanceObjects": rohcInstanceObjects,
       "rohcChannelTable": rohcChannelTable,
       "rohcChannelEntry": rohcChannelEntry,
       "rohcChannelID": rohcChannelID,
       "rohcChannelType": rohcChannelType,
       "rohcChannelFeedbackFor": rohcChannelFeedbackFor,
       "rohcChannelDescr": rohcChannelDescr,
       "rohcChannelStatus": rohcChannelStatus,
       "rohcInstanceTable": rohcInstanceTable,
       "rohcInstanceEntry": rohcInstanceEntry,
       "rohcInstanceType": rohcInstanceType,
       "rohcInstanceFBChannelID": rohcInstanceFBChannelID,
       "rohcInstanceVendor": rohcInstanceVendor,
       "rohcInstanceVersion": rohcInstanceVersion,
       "rohcInstanceDescr": rohcInstanceDescr,
       "rohcInstanceClockRes": rohcInstanceClockRes,
       "rohcInstanceMaxCID": rohcInstanceMaxCID,
       "rohcInstanceLargeCIDs": rohcInstanceLargeCIDs,
       "rohcInstanceMRRU": rohcInstanceMRRU,
       "rohcInstanceContextStorageTime": rohcInstanceContextStorageTime,
       "rohcInstanceStatus": rohcInstanceStatus,
       "rohcInstanceContextsTotal": rohcInstanceContextsTotal,
       "rohcInstanceContextsCurrent": rohcInstanceContextsCurrent,
       "rohcInstancePackets": rohcInstancePackets,
       "rohcInstanceIRs": rohcInstanceIRs,
       "rohcInstanceIRDYNs": rohcInstanceIRDYNs,
       "rohcInstanceFeedbacks": rohcInstanceFeedbacks,
       "rohcInstanceCompressionRatio": rohcInstanceCompressionRatio,
       "rohcProfileTable": rohcProfileTable,
       "rohcProfileEntry": rohcProfileEntry,
       "rohcProfile": rohcProfile,
       "rohcProfileVendor": rohcProfileVendor,
       "rohcProfileVersion": rohcProfileVersion,
       "rohcProfileDescr": rohcProfileDescr,
       "rohcProfileNegotiated": rohcProfileNegotiated,
       "rohcContextTable": rohcContextTable,
       "rohcContextEntry": rohcContextEntry,
       "rohcContextCID": rohcContextCID,
       "rohcContextCIDState": rohcContextCIDState,
       "rohcContextProfile": rohcContextProfile,
       "rohcContextDecompressorDepth": rohcContextDecompressorDepth,
       "rohcContextStorageTime": rohcContextStorageTime,
       "rohcContextActivationTime": rohcContextActivationTime,
       "rohcContextDeactivationTime": rohcContextDeactivationTime,
       "rohcContextPackets": rohcContextPackets,
       "rohcContextIRs": rohcContextIRs,
       "rohcContextIRDYNs": rohcContextIRDYNs,
       "rohcContextFeedbacks": rohcContextFeedbacks,
       "rohcContextDecompressorFailures": rohcContextDecompressorFailures,
       "rohcContextDecompressorRepairs": rohcContextDecompressorRepairs,
       "rohcContextAllPacketsRatio": rohcContextAllPacketsRatio,
       "rohcContextAllHeadersRatio": rohcContextAllHeadersRatio,
       "rohcContextAllPacketsMeanSize": rohcContextAllPacketsMeanSize,
       "rohcContextAllHeadersMeanSize": rohcContextAllHeadersMeanSize,
       "rohcContextLastPacketsRatio": rohcContextLastPacketsRatio,
       "rohcContextLastHeadersRatio": rohcContextLastHeadersRatio,
       "rohcContextLastPacketsMeanSize": rohcContextLastPacketsMeanSize,
       "rohcContextLastHeadersMeanSize": rohcContextLastHeadersMeanSize,
       "rohcConformance": rohcConformance,
       "rohcCompliances": rohcCompliances,
       "rohcCompliance": rohcCompliance,
       "rohcGroups": rohcGroups,
       "rohcInstanceGroup": rohcInstanceGroup,
       "rohcStatisticsGroup": rohcStatisticsGroup,
       "rohcContextGroup": rohcContextGroup,
       "rohcTimerGroup": rohcTimerGroup,
       "rohcContextStatisticsGroup": rohcContextStatisticsGroup}
)
