# SNMP MIB module (SYMMCOMMONPTP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMCOMMONPTP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:47 2024
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

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

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

(EnableValue,
 symmPacketService) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "EnableValue",
    "symmPacketService")


# MODULE-IDENTITY

symmPTPv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1)
)
symmPTPv2.setRevisions(
        ("2018-07-31 06:20",)
)


# Types definitions



class PTPPROFILEVALUE(Integer32):
    """Custom type PTPPROFILEVALUE based on Integer32"""
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
        *(("profileDefault", 2),
          ("profileEthernetDefault", 5),
          ("profileHybrid", 3),
          ("profileITU8265one", 4),
          ("profileITU8275one", 6),
          ("profileITU8275two", 7),
          ("profileTelecom2008", 1))
    )





class PTPTIMESCALETYPE(Integer32):
    """Custom type PTPTIMESCALETYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arb", 2),
          ("auto", 1),
          ("ptp", 3))
    )





class PTPMGMTADDRTYPE(Integer32):
    """Custom type PTPMGMTADDRTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 0))
    )





class PTPTRANSPORTTYPE(Integer32):
    """Custom type PTPTRANSPORTTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ipv4", 2))
    )





class PTPADDRMODETYPE(Integer32):
    """Custom type PTPADDRMODETYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("multicasthybrid", 2),
          ("unicast", 0))
    )





class PORTSTATEVALUE(Integer32):
    """Custom type PORTSTATEVALUE based on Integer32"""
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





class G82751McAddrValue(Integer32):
    """Custom type G82751McAddrValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac011b19000000", 1),
          ("mac0180c200000e", 2))
    )





class VLANID(Integer32):
    """Custom type VLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Ptpv2Status_ObjectIdentity = ObjectIdentity
ptpv2Status = _Ptpv2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1)
)
_Ptpv2StatusTable_Object = MibTable
ptpv2StatusTable = _Ptpv2StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ptpv2StatusTable.setStatus("current")
_Ptpv2StatusEntry_Object = MibTableRow
ptpv2StatusEntry = _Ptpv2StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1)
)
ptpv2StatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPTP", "ptpv2StatusIndex"),
)
if mibBuilder.loadTexts:
    ptpv2StatusEntry.setStatus("current")


class _Ptpv2StatusIndex_Type(Integer32):
    """Custom type ptpv2StatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Ptpv2StatusIndex_Type.__name__ = "Integer32"
_Ptpv2StatusIndex_Object = MibTableColumn
ptpv2StatusIndex = _Ptpv2StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 1),
    _Ptpv2StatusIndex_Type()
)
ptpv2StatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpv2StatusIndex.setStatus("current")
_Ptpv2StatusPortEnable_Type = EnableValue
_Ptpv2StatusPortEnable_Object = MibTableColumn
ptpv2StatusPortEnable = _Ptpv2StatusPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 2),
    _Ptpv2StatusPortEnable_Type()
)
ptpv2StatusPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusPortEnable.setStatus("current")
_Ptpv2StatusClockID_Type = DisplayString
_Ptpv2StatusClockID_Object = MibTableColumn
ptpv2StatusClockID = _Ptpv2StatusClockID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 3),
    _Ptpv2StatusClockID_Type()
)
ptpv2StatusClockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusClockID.setStatus("current")
_Ptpv2StatusProfile_Type = PTPPROFILEVALUE
_Ptpv2StatusProfile_Object = MibTableColumn
ptpv2StatusProfile = _Ptpv2StatusProfile_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 4),
    _Ptpv2StatusProfile_Type()
)
ptpv2StatusProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusProfile.setStatus("current")
_Ptpv2StatusClockClass_Type = DisplayString
_Ptpv2StatusClockClass_Object = MibTableColumn
ptpv2StatusClockClass = _Ptpv2StatusClockClass_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 5),
    _Ptpv2StatusClockClass_Type()
)
ptpv2StatusClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusClockClass.setStatus("current")
_Ptpv2StatusClockAccuracy_Type = DisplayString
_Ptpv2StatusClockAccuracy_Object = MibTableColumn
ptpv2StatusClockAccuracy = _Ptpv2StatusClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 6),
    _Ptpv2StatusClockAccuracy_Type()
)
ptpv2StatusClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusClockAccuracy.setStatus("current")
_Ptpv2StatusTimescale_Type = PTPTIMESCALETYPE
_Ptpv2StatusTimescale_Object = MibTableColumn
ptpv2StatusTimescale = _Ptpv2StatusTimescale_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 7),
    _Ptpv2StatusTimescale_Type()
)
ptpv2StatusTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusTimescale.setStatus("current")


class _Ptpv2StatusNumClient_Type(Integer32):
    """Custom type ptpv2StatusNumClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Ptpv2StatusNumClient_Type.__name__ = "Integer32"
_Ptpv2StatusNumClient_Object = MibTableColumn
ptpv2StatusNumClient = _Ptpv2StatusNumClient_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 8),
    _Ptpv2StatusNumClient_Type()
)
ptpv2StatusNumClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusNumClient.setStatus("current")
_Ptpv2StatusClientLoad_Type = DisplayString
_Ptpv2StatusClientLoad_Object = MibTableColumn
ptpv2StatusClientLoad = _Ptpv2StatusClientLoad_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 1, 1, 9),
    _Ptpv2StatusClientLoad_Type()
)
ptpv2StatusClientLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2StatusClientLoad.setStatus("current")
_Ptpv2ClientDataTable_Object = MibTable
ptpv2ClientDataTable = _Ptpv2ClientDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ptpv2ClientDataTable.setStatus("current")
_Ptpv2ClientDataEntry_Object = MibTableRow
ptpv2ClientDataEntry = _Ptpv2ClientDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2, 1)
)
ptpv2ClientDataEntry.setIndexNames(
    (0, "SYMMCOMMONPTP", "ptpv2ClientDataIndex"),
)
if mibBuilder.loadTexts:
    ptpv2ClientDataEntry.setStatus("current")


class _Ptpv2ClientDataIndex_Type(Integer32):
    """Custom type ptpv2ClientDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_Ptpv2ClientDataIndex_Type.__name__ = "Integer32"
_Ptpv2ClientDataIndex_Object = MibTableColumn
ptpv2ClientDataIndex = _Ptpv2ClientDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2, 1, 1),
    _Ptpv2ClientDataIndex_Type()
)
ptpv2ClientDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2ClientDataIndex.setStatus("current")
_Ptpv2ClientData_Type = DisplayString
_Ptpv2ClientData_Object = MibTableColumn
ptpv2ClientData = _Ptpv2ClientData_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 1, 2, 1, 2),
    _Ptpv2ClientData_Type()
)
ptpv2ClientData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpv2ClientData.setStatus("current")
_Ptpv2Config_ObjectIdentity = ObjectIdentity
ptpv2Config = _Ptpv2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2)
)
_Ptpv2CommonTable_Object = MibTable
ptpv2CommonTable = _Ptpv2CommonTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ptpv2CommonTable.setStatus("current")
_Ptpv2CommonEntry_Object = MibTableRow
ptpv2CommonEntry = _Ptpv2CommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1)
)
ptpv2CommonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPTP", "ptpv2CommonIndex"),
)
if mibBuilder.loadTexts:
    ptpv2CommonEntry.setStatus("current")


class _Ptpv2CommonIndex_Type(Integer32):
    """Custom type ptpv2CommonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Ptpv2CommonIndex_Type.__name__ = "Integer32"
_Ptpv2CommonIndex_Object = MibTableColumn
ptpv2CommonIndex = _Ptpv2CommonIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 1),
    _Ptpv2CommonIndex_Type()
)
ptpv2CommonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpv2CommonIndex.setStatus("current")
_Ptpv2Profile_Type = PTPPROFILEVALUE
_Ptpv2Profile_Object = MibTableColumn
ptpv2Profile = _Ptpv2Profile_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 2),
    _Ptpv2Profile_Type()
)
ptpv2Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2Profile.setStatus("current")
_Ptpv2ClockID_Type = DisplayString
_Ptpv2ClockID_Object = MibTableColumn
ptpv2ClockID = _Ptpv2ClockID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 3),
    _Ptpv2ClockID_Type()
)
ptpv2ClockID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2ClockID.setStatus("current")


class _Ptpv2Priority1_Type(Unsigned32):
    """Custom type ptpv2Priority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ptpv2Priority1_Type.__name__ = "Unsigned32"
_Ptpv2Priority1_Object = MibTableColumn
ptpv2Priority1 = _Ptpv2Priority1_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 4),
    _Ptpv2Priority1_Type()
)
ptpv2Priority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2Priority1.setStatus("current")


class _Ptpv2Priority2_Type(Unsigned32):
    """Custom type ptpv2Priority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ptpv2Priority2_Type.__name__ = "Unsigned32"
_Ptpv2Priority2_Object = MibTableColumn
ptpv2Priority2 = _Ptpv2Priority2_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 5),
    _Ptpv2Priority2_Type()
)
ptpv2Priority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2Priority2.setStatus("current")


class _Ptpv2Domain_Type(Unsigned32):
    """Custom type ptpv2Domain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ptpv2Domain_Type.__name__ = "Unsigned32"
_Ptpv2Domain_Object = MibTableColumn
ptpv2Domain = _Ptpv2Domain_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 6),
    _Ptpv2Domain_Type()
)
ptpv2Domain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2Domain.setStatus("current")
_Ptpv2DSCPState_Type = EnableValue
_Ptpv2DSCPState_Object = MibTableColumn
ptpv2DSCPState = _Ptpv2DSCPState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 7),
    _Ptpv2DSCPState_Type()
)
ptpv2DSCPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2DSCPState.setStatus("current")


class _Ptpv2DSCPValue_Type(Unsigned32):
    """Custom type ptpv2DSCPValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Ptpv2DSCPValue_Type.__name__ = "Unsigned32"
_Ptpv2DSCPValue_Object = MibTableColumn
ptpv2DSCPValue = _Ptpv2DSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 8),
    _Ptpv2DSCPValue_Type()
)
ptpv2DSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2DSCPValue.setStatus("current")
_Ptpv2State_Type = EnableValue
_Ptpv2State_Object = MibTableColumn
ptpv2State = _Ptpv2State_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 9),
    _Ptpv2State_Type()
)
ptpv2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2State.setStatus("current")


class _Ptpv2MaxClient_Type(Integer32):
    """Custom type ptpv2MaxClient based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_Ptpv2MaxClient_Type.__name__ = "Integer32"
_Ptpv2MaxClient_Object = MibTableColumn
ptpv2MaxClient = _Ptpv2MaxClient_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 10),
    _Ptpv2MaxClient_Type()
)
ptpv2MaxClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MaxClient.setStatus("current")


class _Ptpv2AnnounceLimit_Type(Integer32):
    """Custom type ptpv2AnnounceLimit based on Integer32"""
    defaultValue = -3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 4),
    )


_Ptpv2AnnounceLimit_Type.__name__ = "Integer32"
_Ptpv2AnnounceLimit_Object = MibTableColumn
ptpv2AnnounceLimit = _Ptpv2AnnounceLimit_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 11),
    _Ptpv2AnnounceLimit_Type()
)
ptpv2AnnounceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2AnnounceLimit.setStatus("current")


class _Ptpv2SyncLimit_Type(Integer32):
    """Custom type ptpv2SyncLimit based on Integer32"""
    defaultValue = -7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_Ptpv2SyncLimit_Type.__name__ = "Integer32"
_Ptpv2SyncLimit_Object = MibTableColumn
ptpv2SyncLimit = _Ptpv2SyncLimit_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 12),
    _Ptpv2SyncLimit_Type()
)
ptpv2SyncLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2SyncLimit.setStatus("current")


class _Ptpv2DelayLimit_Type(Integer32):
    """Custom type ptpv2DelayLimit based on Integer32"""
    defaultValue = -7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_Ptpv2DelayLimit_Type.__name__ = "Integer32"
_Ptpv2DelayLimit_Object = MibTableColumn
ptpv2DelayLimit = _Ptpv2DelayLimit_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 13),
    _Ptpv2DelayLimit_Type()
)
ptpv2DelayLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2DelayLimit.setStatus("current")
_Ptpv2TwoStep_Type = EnableValue
_Ptpv2TwoStep_Object = MibTableColumn
ptpv2TwoStep = _Ptpv2TwoStep_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 14),
    _Ptpv2TwoStep_Type()
)
ptpv2TwoStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2TwoStep.setStatus("current")
_Ptpv2MgmtAddrMode_Type = PTPMGMTADDRTYPE
_Ptpv2MgmtAddrMode_Object = MibTableColumn
ptpv2MgmtAddrMode = _Ptpv2MgmtAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 15),
    _Ptpv2MgmtAddrMode_Type()
)
ptpv2MgmtAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MgmtAddrMode.setStatus("current")


class _Ptpv2TTL_Type(Unsigned32):
    """Custom type ptpv2TTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ptpv2TTL_Type.__name__ = "Unsigned32"
_Ptpv2TTL_Object = MibTableColumn
ptpv2TTL = _Ptpv2TTL_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 16),
    _Ptpv2TTL_Type()
)
ptpv2TTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2TTL.setStatus("current")
_Ptpv2AlternateGM_Type = EnableValue
_Ptpv2AlternateGM_Object = MibTableColumn
ptpv2AlternateGM = _Ptpv2AlternateGM_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 17),
    _Ptpv2AlternateGM_Type()
)
ptpv2AlternateGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2AlternateGM.setStatus("current")
_Ptpv2TimeScale_Type = PTPTIMESCALETYPE
_Ptpv2TimeScale_Object = MibTableColumn
ptpv2TimeScale = _Ptpv2TimeScale_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 18),
    _Ptpv2TimeScale_Type()
)
ptpv2TimeScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2TimeScale.setStatus("current")
_Ptpv2Dither_Type = EnableValue
_Ptpv2Dither_Object = MibTableColumn
ptpv2Dither = _Ptpv2Dither_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 19),
    _Ptpv2Dither_Type()
)
ptpv2Dither.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2Dither.setStatus("current")


class _Ptpv2ServiceLoadAlarmThreshold_Type(Integer32):
    """Custom type ptpv2ServiceLoadAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_Ptpv2ServiceLoadAlarmThreshold_Type.__name__ = "Integer32"
_Ptpv2ServiceLoadAlarmThreshold_Object = MibTableColumn
ptpv2ServiceLoadAlarmThreshold = _Ptpv2ServiceLoadAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 1, 1, 20),
    _Ptpv2ServiceLoadAlarmThreshold_Type()
)
ptpv2ServiceLoadAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2ServiceLoadAlarmThreshold.setStatus("current")
_Ptpv2UnicastTable_Object = MibTable
ptpv2UnicastTable = _Ptpv2UnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ptpv2UnicastTable.setStatus("current")
_Ptpv2UnicastEntry_Object = MibTableRow
ptpv2UnicastEntry = _Ptpv2UnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1)
)
ptpv2UnicastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPTP", "ptpv2UnicastIndex"),
)
if mibBuilder.loadTexts:
    ptpv2UnicastEntry.setStatus("current")


class _Ptpv2UnicastIndex_Type(Integer32):
    """Custom type ptpv2UnicastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Ptpv2UnicastIndex_Type.__name__ = "Integer32"
_Ptpv2UnicastIndex_Object = MibTableColumn
ptpv2UnicastIndex = _Ptpv2UnicastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 1),
    _Ptpv2UnicastIndex_Type()
)
ptpv2UnicastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpv2UnicastIndex.setStatus("current")
_Ptpv2UnicastNeg_Type = EnableValue
_Ptpv2UnicastNeg_Object = MibTableColumn
ptpv2UnicastNeg = _Ptpv2UnicastNeg_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 2),
    _Ptpv2UnicastNeg_Type()
)
ptpv2UnicastNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2UnicastNeg.setStatus("current")


class _Ptpv2UnicastLeaseDurLimit_Type(Integer32):
    """Custom type ptpv2UnicastLeaseDurLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_Ptpv2UnicastLeaseDurLimit_Type.__name__ = "Integer32"
_Ptpv2UnicastLeaseDurLimit_Object = MibTableColumn
ptpv2UnicastLeaseDurLimit = _Ptpv2UnicastLeaseDurLimit_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 3),
    _Ptpv2UnicastLeaseDurLimit_Type()
)
ptpv2UnicastLeaseDurLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2UnicastLeaseDurLimit.setStatus("current")
_Ptpv2UnicastInterfaceRateTLV_Type = EnableValue
_Ptpv2UnicastInterfaceRateTLV_Object = MibTableColumn
ptpv2UnicastInterfaceRateTLV = _Ptpv2UnicastInterfaceRateTLV_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 4),
    _Ptpv2UnicastInterfaceRateTLV_Type()
)
ptpv2UnicastInterfaceRateTLV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2UnicastInterfaceRateTLV.setStatus("current")


class _Ptpv2UnicastLeaseExtension_Type(Integer32):
    """Custom type ptpv2UnicastLeaseExtension based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Ptpv2UnicastLeaseExtension_Type.__name__ = "Integer32"
_Ptpv2UnicastLeaseExtension_Object = MibTableColumn
ptpv2UnicastLeaseExtension = _Ptpv2UnicastLeaseExtension_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 2, 1, 5),
    _Ptpv2UnicastLeaseExtension_Type()
)
ptpv2UnicastLeaseExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2UnicastLeaseExtension.setStatus("current")
_Ptpv2MulticastTable_Object = MibTable
ptpv2MulticastTable = _Ptpv2MulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ptpv2MulticastTable.setStatus("current")
_Ptpv2MulticastEntry_Object = MibTableRow
ptpv2MulticastEntry = _Ptpv2MulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1)
)
ptpv2MulticastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPTP", "ptpv2MulticastIndex"),
)
if mibBuilder.loadTexts:
    ptpv2MulticastEntry.setStatus("current")


class _Ptpv2MulticastIndex_Type(Integer32):
    """Custom type ptpv2MulticastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Ptpv2MulticastIndex_Type.__name__ = "Integer32"
_Ptpv2MulticastIndex_Object = MibTableColumn
ptpv2MulticastIndex = _Ptpv2MulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 1),
    _Ptpv2MulticastIndex_Type()
)
ptpv2MulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpv2MulticastIndex.setStatus("current")


class _Ptpv2MulticastAnnounceInt_Type(Integer32):
    """Custom type ptpv2MulticastAnnounceInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 4),
    )


_Ptpv2MulticastAnnounceInt_Type.__name__ = "Integer32"
_Ptpv2MulticastAnnounceInt_Object = MibTableColumn
ptpv2MulticastAnnounceInt = _Ptpv2MulticastAnnounceInt_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 2),
    _Ptpv2MulticastAnnounceInt_Type()
)
ptpv2MulticastAnnounceInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MulticastAnnounceInt.setStatus("current")


class _Ptpv2MulticastSyncInt_Type(Integer32):
    """Custom type ptpv2MulticastSyncInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_Ptpv2MulticastSyncInt_Type.__name__ = "Integer32"
_Ptpv2MulticastSyncInt_Object = MibTableColumn
ptpv2MulticastSyncInt = _Ptpv2MulticastSyncInt_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 3),
    _Ptpv2MulticastSyncInt_Type()
)
ptpv2MulticastSyncInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MulticastSyncInt.setStatus("current")


class _Ptpv2MulticastDelayInt_Type(Integer32):
    """Custom type ptpv2MulticastDelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_Ptpv2MulticastDelayInt_Type.__name__ = "Integer32"
_Ptpv2MulticastDelayInt_Object = MibTableColumn
ptpv2MulticastDelayInt = _Ptpv2MulticastDelayInt_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 4),
    _Ptpv2MulticastDelayInt_Type()
)
ptpv2MulticastDelayInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MulticastDelayInt.setStatus("current")


class _Ptpv2MulticastAnnoTimeout_Type(Integer32):
    """Custom type ptpv2MulticastAnnoTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Ptpv2MulticastAnnoTimeout_Type.__name__ = "Integer32"
_Ptpv2MulticastAnnoTimeout_Object = MibTableColumn
ptpv2MulticastAnnoTimeout = _Ptpv2MulticastAnnoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 5),
    _Ptpv2MulticastAnnoTimeout_Type()
)
ptpv2MulticastAnnoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MulticastAnnoTimeout.setStatus("current")


class _Ptpv2MulticastVlanId_Type(Integer32):
    """Custom type ptpv2MulticastVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Ptpv2MulticastVlanId_Type.__name__ = "Integer32"
_Ptpv2MulticastVlanId_Object = MibTableColumn
ptpv2MulticastVlanId = _Ptpv2MulticastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 6),
    _Ptpv2MulticastVlanId_Type()
)
ptpv2MulticastVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MulticastVlanId.setStatus("current")


class _Ptpv2MulticastClientTimeout_Type(Integer32):
    """Custom type ptpv2MulticastClientTimeout based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_Ptpv2MulticastClientTimeout_Type.__name__ = "Integer32"
_Ptpv2MulticastClientTimeout_Object = MibTableColumn
ptpv2MulticastClientTimeout = _Ptpv2MulticastClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 3, 1, 7),
    _Ptpv2MulticastClientTimeout_Type()
)
ptpv2MulticastClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2MulticastClientTimeout.setStatus("current")
_Ptpv2G82751Table_Object = MibTable
ptpv2G82751Table = _Ptpv2G82751Table_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ptpv2G82751Table.setStatus("current")
_Ptpv2G82751Entry_Object = MibTableRow
ptpv2G82751Entry = _Ptpv2G82751Entry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1)
)
ptpv2G82751Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPTP", "ptpv2G82751Index"),
)
if mibBuilder.loadTexts:
    ptpv2G82751Entry.setStatus("current")


class _Ptpv2G82751Index_Type(Integer32):
    """Custom type ptpv2G82751Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Ptpv2G82751Index_Type.__name__ = "Integer32"
_Ptpv2G82751Index_Object = MibTableColumn
ptpv2G82751Index = _Ptpv2G82751Index_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1, 1),
    _Ptpv2G82751Index_Type()
)
ptpv2G82751Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpv2G82751Index.setStatus("current")
_Ptpv2G82751MulticastAddr_Type = G82751McAddrValue
_Ptpv2G82751MulticastAddr_Object = MibTableColumn
ptpv2G82751MulticastAddr = _Ptpv2G82751MulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1, 2),
    _Ptpv2G82751MulticastAddr_Type()
)
ptpv2G82751MulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2G82751MulticastAddr.setStatus("current")


class _Ptpv2G82751LocalPriority_Type(Integer32):
    """Custom type ptpv2G82751LocalPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ptpv2G82751LocalPriority_Type.__name__ = "Integer32"
_Ptpv2G82751LocalPriority_Object = MibTableColumn
ptpv2G82751LocalPriority = _Ptpv2G82751LocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 4, 1, 3),
    _Ptpv2G82751LocalPriority_Type()
)
ptpv2G82751LocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2G82751LocalPriority.setStatus("current")
_Ptpv2ReflectorTable_Object = MibTable
ptpv2ReflectorTable = _Ptpv2ReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ptpv2ReflectorTable.setStatus("current")
_Ptpv2ReflectorEntry_Object = MibTableRow
ptpv2ReflectorEntry = _Ptpv2ReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1)
)
ptpv2ReflectorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMCOMMONPTP", "ptpv2ReflectorIndex"),
)
if mibBuilder.loadTexts:
    ptpv2ReflectorEntry.setStatus("current")


class _Ptpv2ReflectorIndex_Type(Integer32):
    """Custom type ptpv2ReflectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Ptpv2ReflectorIndex_Type.__name__ = "Integer32"
_Ptpv2ReflectorIndex_Object = MibTableColumn
ptpv2ReflectorIndex = _Ptpv2ReflectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 1),
    _Ptpv2ReflectorIndex_Type()
)
ptpv2ReflectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpv2ReflectorIndex.setStatus("current")


class _Ptpv2ReflectorAnnounceIntv_Type(Integer32):
    """Custom type ptpv2ReflectorAnnounceIntv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 0),
    )


_Ptpv2ReflectorAnnounceIntv_Type.__name__ = "Integer32"
_Ptpv2ReflectorAnnounceIntv_Object = MibTableColumn
ptpv2ReflectorAnnounceIntv = _Ptpv2ReflectorAnnounceIntv_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 2),
    _Ptpv2ReflectorAnnounceIntv_Type()
)
ptpv2ReflectorAnnounceIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2ReflectorAnnounceIntv.setStatus("current")


class _Ptpv2ReflectorSyncDelayIntv_Type(Integer32):
    """Custom type ptpv2ReflectorSyncDelayIntv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, -4),
    )


_Ptpv2ReflectorSyncDelayIntv_Type.__name__ = "Integer32"
_Ptpv2ReflectorSyncDelayIntv_Object = MibTableColumn
ptpv2ReflectorSyncDelayIntv = _Ptpv2ReflectorSyncDelayIntv_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 3),
    _Ptpv2ReflectorSyncDelayIntv_Type()
)
ptpv2ReflectorSyncDelayIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2ReflectorSyncDelayIntv.setStatus("current")


class _Ptpv2ReflectorClientTimeout_Type(Integer32):
    """Custom type ptpv2ReflectorClientTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1000),
    )


_Ptpv2ReflectorClientTimeout_Type.__name__ = "Integer32"
_Ptpv2ReflectorClientTimeout_Object = MibTableColumn
ptpv2ReflectorClientTimeout = _Ptpv2ReflectorClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 4),
    _Ptpv2ReflectorClientTimeout_Type()
)
ptpv2ReflectorClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2ReflectorClientTimeout.setStatus("current")


class _Ptpv2ReflectorVlanID_Type(Integer32):
    """Custom type ptpv2ReflectorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Ptpv2ReflectorVlanID_Type.__name__ = "Integer32"
_Ptpv2ReflectorVlanID_Object = MibTableColumn
ptpv2ReflectorVlanID = _Ptpv2ReflectorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 2, 5, 1, 5),
    _Ptpv2ReflectorVlanID_Type()
)
ptpv2ReflectorVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpv2ReflectorVlanID.setStatus("current")
_Ptpv2Conformance_ObjectIdentity = ObjectIdentity
ptpv2Conformance = _Ptpv2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ptpv2Conformance.setStatus("current")
_Ptpv2Compliances_ObjectIdentity = ObjectIdentity
ptpv2Compliances = _Ptpv2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 1)
)
_Ptpv2UocGroups_ObjectIdentity = ObjectIdentity
ptpv2UocGroups = _Ptpv2UocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2)
)

# Managed Objects groups

ptpv2StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 1)
)
ptpv2StatusGroup.setObjects(
      *(("SYMMCOMMONPTP", "ptpv2StatusPortEnable"),
        ("SYMMCOMMONPTP", "ptpv2StatusClockID"),
        ("SYMMCOMMONPTP", "ptpv2StatusProfile"),
        ("SYMMCOMMONPTP", "ptpv2StatusClockClass"),
        ("SYMMCOMMONPTP", "ptpv2StatusClockAccuracy"),
        ("SYMMCOMMONPTP", "ptpv2StatusTimescale"),
        ("SYMMCOMMONPTP", "ptpv2StatusNumClient"),
        ("SYMMCOMMONPTP", "ptpv2StatusClientLoad"))
)
if mibBuilder.loadTexts:
    ptpv2StatusGroup.setStatus("current")

ptpv2ClientDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 2)
)
ptpv2ClientDataGroup.setObjects(
      *(("SYMMCOMMONPTP", "ptpv2ClientDataIndex"),
        ("SYMMCOMMONPTP", "ptpv2ClientData"))
)
if mibBuilder.loadTexts:
    ptpv2ClientDataGroup.setStatus("current")

ptpv2CommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 3)
)
ptpv2CommonGroup.setObjects(
      *(("SYMMCOMMONPTP", "ptpv2Profile"),
        ("SYMMCOMMONPTP", "ptpv2ClockID"),
        ("SYMMCOMMONPTP", "ptpv2Priority1"),
        ("SYMMCOMMONPTP", "ptpv2Priority2"),
        ("SYMMCOMMONPTP", "ptpv2Domain"),
        ("SYMMCOMMONPTP", "ptpv2DSCPState"),
        ("SYMMCOMMONPTP", "ptpv2DSCPValue"),
        ("SYMMCOMMONPTP", "ptpv2State"),
        ("SYMMCOMMONPTP", "ptpv2MaxClient"),
        ("SYMMCOMMONPTP", "ptpv2AnnounceLimit"),
        ("SYMMCOMMONPTP", "ptpv2SyncLimit"),
        ("SYMMCOMMONPTP", "ptpv2DelayLimit"),
        ("SYMMCOMMONPTP", "ptpv2TwoStep"),
        ("SYMMCOMMONPTP", "ptpv2MgmtAddrMode"),
        ("SYMMCOMMONPTP", "ptpv2TTL"),
        ("SYMMCOMMONPTP", "ptpv2AlternateGM"),
        ("SYMMCOMMONPTP", "ptpv2TimeScale"),
        ("SYMMCOMMONPTP", "ptpv2Dither"))
)
if mibBuilder.loadTexts:
    ptpv2CommonGroup.setStatus("current")

ptpv2UnicastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 4)
)
ptpv2UnicastGroup.setObjects(
      *(("SYMMCOMMONPTP", "ptpv2UnicastNeg"),
        ("SYMMCOMMONPTP", "ptpv2UnicastLeaseDurLimit"),
        ("SYMMCOMMONPTP", "ptpv2UnicastInterfaceRateTLV"),
        ("SYMMCOMMONPTP", "ptpv2UnicastLeaseExtension"))
)
if mibBuilder.loadTexts:
    ptpv2UnicastGroup.setStatus("current")

ptpv2MulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 5)
)
ptpv2MulticastGroup.setObjects(
      *(("SYMMCOMMONPTP", "ptpv2MulticastAnnounceInt"),
        ("SYMMCOMMONPTP", "ptpv2MulticastSyncInt"),
        ("SYMMCOMMONPTP", "ptpv2MulticastDelayInt"),
        ("SYMMCOMMONPTP", "ptpv2MulticastAnnoTimeout"),
        ("SYMMCOMMONPTP", "ptpv2MulticastVlanId"),
        ("SYMMCOMMONPTP", "ptpv2MulticastClientTimeout"))
)
if mibBuilder.loadTexts:
    ptpv2MulticastGroup.setStatus("current")

ptpv2G82751Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 2, 6)
)
ptpv2G82751Group.setObjects(
      *(("SYMMCOMMONPTP", "ptpv2G82751MulticastAddr"),
        ("SYMMCOMMONPTP", "ptpv2G82751LocalPriority"))
)
if mibBuilder.loadTexts:
    ptpv2G82751Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ptpv2BasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ptpv2BasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMCOMMONPTP",
    **{"PTPPROFILEVALUE": PTPPROFILEVALUE,
       "PTPTIMESCALETYPE": PTPTIMESCALETYPE,
       "PTPMGMTADDRTYPE": PTPMGMTADDRTYPE,
       "PTPTRANSPORTTYPE": PTPTRANSPORTTYPE,
       "PTPADDRMODETYPE": PTPADDRMODETYPE,
       "PORTSTATEVALUE": PORTSTATEVALUE,
       "G82751McAddrValue": G82751McAddrValue,
       "VLANID": VLANID,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmPTPv2": symmPTPv2,
       "ptpv2Status": ptpv2Status,
       "ptpv2StatusTable": ptpv2StatusTable,
       "ptpv2StatusEntry": ptpv2StatusEntry,
       "ptpv2StatusIndex": ptpv2StatusIndex,
       "ptpv2StatusPortEnable": ptpv2StatusPortEnable,
       "ptpv2StatusClockID": ptpv2StatusClockID,
       "ptpv2StatusProfile": ptpv2StatusProfile,
       "ptpv2StatusClockClass": ptpv2StatusClockClass,
       "ptpv2StatusClockAccuracy": ptpv2StatusClockAccuracy,
       "ptpv2StatusTimescale": ptpv2StatusTimescale,
       "ptpv2StatusNumClient": ptpv2StatusNumClient,
       "ptpv2StatusClientLoad": ptpv2StatusClientLoad,
       "ptpv2ClientDataTable": ptpv2ClientDataTable,
       "ptpv2ClientDataEntry": ptpv2ClientDataEntry,
       "ptpv2ClientDataIndex": ptpv2ClientDataIndex,
       "ptpv2ClientData": ptpv2ClientData,
       "ptpv2Config": ptpv2Config,
       "ptpv2CommonTable": ptpv2CommonTable,
       "ptpv2CommonEntry": ptpv2CommonEntry,
       "ptpv2CommonIndex": ptpv2CommonIndex,
       "ptpv2Profile": ptpv2Profile,
       "ptpv2ClockID": ptpv2ClockID,
       "ptpv2Priority1": ptpv2Priority1,
       "ptpv2Priority2": ptpv2Priority2,
       "ptpv2Domain": ptpv2Domain,
       "ptpv2DSCPState": ptpv2DSCPState,
       "ptpv2DSCPValue": ptpv2DSCPValue,
       "ptpv2State": ptpv2State,
       "ptpv2MaxClient": ptpv2MaxClient,
       "ptpv2AnnounceLimit": ptpv2AnnounceLimit,
       "ptpv2SyncLimit": ptpv2SyncLimit,
       "ptpv2DelayLimit": ptpv2DelayLimit,
       "ptpv2TwoStep": ptpv2TwoStep,
       "ptpv2MgmtAddrMode": ptpv2MgmtAddrMode,
       "ptpv2TTL": ptpv2TTL,
       "ptpv2AlternateGM": ptpv2AlternateGM,
       "ptpv2TimeScale": ptpv2TimeScale,
       "ptpv2Dither": ptpv2Dither,
       "ptpv2ServiceLoadAlarmThreshold": ptpv2ServiceLoadAlarmThreshold,
       "ptpv2UnicastTable": ptpv2UnicastTable,
       "ptpv2UnicastEntry": ptpv2UnicastEntry,
       "ptpv2UnicastIndex": ptpv2UnicastIndex,
       "ptpv2UnicastNeg": ptpv2UnicastNeg,
       "ptpv2UnicastLeaseDurLimit": ptpv2UnicastLeaseDurLimit,
       "ptpv2UnicastInterfaceRateTLV": ptpv2UnicastInterfaceRateTLV,
       "ptpv2UnicastLeaseExtension": ptpv2UnicastLeaseExtension,
       "ptpv2MulticastTable": ptpv2MulticastTable,
       "ptpv2MulticastEntry": ptpv2MulticastEntry,
       "ptpv2MulticastIndex": ptpv2MulticastIndex,
       "ptpv2MulticastAnnounceInt": ptpv2MulticastAnnounceInt,
       "ptpv2MulticastSyncInt": ptpv2MulticastSyncInt,
       "ptpv2MulticastDelayInt": ptpv2MulticastDelayInt,
       "ptpv2MulticastAnnoTimeout": ptpv2MulticastAnnoTimeout,
       "ptpv2MulticastVlanId": ptpv2MulticastVlanId,
       "ptpv2MulticastClientTimeout": ptpv2MulticastClientTimeout,
       "ptpv2G82751Table": ptpv2G82751Table,
       "ptpv2G82751Entry": ptpv2G82751Entry,
       "ptpv2G82751Index": ptpv2G82751Index,
       "ptpv2G82751MulticastAddr": ptpv2G82751MulticastAddr,
       "ptpv2G82751LocalPriority": ptpv2G82751LocalPriority,
       "ptpv2ReflectorTable": ptpv2ReflectorTable,
       "ptpv2ReflectorEntry": ptpv2ReflectorEntry,
       "ptpv2ReflectorIndex": ptpv2ReflectorIndex,
       "ptpv2ReflectorAnnounceIntv": ptpv2ReflectorAnnounceIntv,
       "ptpv2ReflectorSyncDelayIntv": ptpv2ReflectorSyncDelayIntv,
       "ptpv2ReflectorClientTimeout": ptpv2ReflectorClientTimeout,
       "ptpv2ReflectorVlanID": ptpv2ReflectorVlanID,
       "ptpv2Conformance": ptpv2Conformance,
       "ptpv2Compliances": ptpv2Compliances,
       "ptpv2BasicCompliance": ptpv2BasicCompliance,
       "ptpv2UocGroups": ptpv2UocGroups,
       "ptpv2StatusGroup": ptpv2StatusGroup,
       "ptpv2ClientDataGroup": ptpv2ClientDataGroup,
       "ptpv2CommonGroup": ptpv2CommonGroup,
       "ptpv2UnicastGroup": ptpv2UnicastGroup,
       "ptpv2MulticastGroup": ptpv2MulticastGroup,
       "ptpv2G82751Group": ptpv2G82751Group}
)
