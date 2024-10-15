# SNMP MIB module (CDX-6500-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CDX-6500-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:55 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500NodeMgmt_ObjectIdentity = ObjectIdentity
cdx6500NodeMgmt = _Cdx6500NodeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1)
)
_Cdx6500NMSNMPGroup_ObjectIdentity = ObjectIdentity
cdx6500NMSNMPGroup = _Cdx6500NMSNMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1)
)


class _Cdx6500SNMPPrimUDPChan_Type(DisplayString):
    """Custom type cdx6500SNMPPrimUDPChan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500SNMPPrimUDPChan_Type.__name__ = "DisplayString"
_Cdx6500SNMPPrimUDPChan_Object = MibScalar
cdx6500SNMPPrimUDPChan = _Cdx6500SNMPPrimUDPChan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 1),
    _Cdx6500SNMPPrimUDPChan_Type()
)
cdx6500SNMPPrimUDPChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPPrimUDPChan.setStatus("mandatory")


class _Cdx6500SNMPSecUDPChan_Type(DisplayString):
    """Custom type cdx6500SNMPSecUDPChan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500SNMPSecUDPChan_Type.__name__ = "DisplayString"
_Cdx6500SNMPSecUDPChan_Object = MibScalar
cdx6500SNMPSecUDPChan = _Cdx6500SNMPSecUDPChan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 2),
    _Cdx6500SNMPSecUDPChan_Type()
)
cdx6500SNMPSecUDPChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPSecUDPChan.setStatus("mandatory")


class _Cdx6500SNMPAgentTimer_Type(Integer32):
    """Custom type cdx6500SNMPAgentTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500SNMPAgentTimer_Type.__name__ = "Integer32"
_Cdx6500SNMPAgentTimer_Object = MibScalar
cdx6500SNMPAgentTimer = _Cdx6500SNMPAgentTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 3),
    _Cdx6500SNMPAgentTimer_Type()
)
cdx6500SNMPAgentTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPAgentTimer.setStatus("mandatory")


class _Cdx6500SNMPTrapEnable_Type(Integer32):
    """Custom type cdx6500SNMPTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("newvalDisable", 50))
    )


_Cdx6500SNMPTrapEnable_Type.__name__ = "Integer32"
_Cdx6500SNMPTrapEnable_Object = MibScalar
cdx6500SNMPTrapEnable = _Cdx6500SNMPTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 4),
    _Cdx6500SNMPTrapEnable_Type()
)
cdx6500SNMPTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPTrapEnable.setStatus("mandatory")


class _Cdx6500SNMPBootAgent_Type(Integer32):
    """Custom type cdx6500SNMPBootAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_Cdx6500SNMPBootAgent_Type.__name__ = "Integer32"
_Cdx6500SNMPBootAgent_Object = MibScalar
cdx6500SNMPBootAgent = _Cdx6500SNMPBootAgent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 5),
    _Cdx6500SNMPBootAgent_Type()
)
cdx6500SNMPBootAgent.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500SNMPBootAgent.setStatus("mandatory")


class _Cdx6500SNMPResetStats_Type(Integer32):
    """Custom type cdx6500SNMPResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cdx6500SNMPResetStats_Type.__name__ = "Integer32"
_Cdx6500SNMPResetStats_Object = MibScalar
cdx6500SNMPResetStats = _Cdx6500SNMPResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 6),
    _Cdx6500SNMPResetStats_Type()
)
cdx6500SNMPResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500SNMPResetStats.setStatus("mandatory")


class _Cdx6500SNMPLastTrap_Type(DisplayString):
    """Custom type cdx6500SNMPLastTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Cdx6500SNMPLastTrap_Type.__name__ = "DisplayString"
_Cdx6500SNMPLastTrap_Object = MibScalar
cdx6500SNMPLastTrap = _Cdx6500SNMPLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 7),
    _Cdx6500SNMPLastTrap_Type()
)
cdx6500SNMPLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SNMPLastTrap.setStatus("mandatory")


class _Cdx6500SNMPGenTrapsType_Type(Integer32):
    """Custom type cdx6500SNMPGenTrapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enterpriseSpecific", 2),
          ("rfc", 1))
    )


_Cdx6500SNMPGenTrapsType_Type.__name__ = "Integer32"
_Cdx6500SNMPGenTrapsType_Object = MibScalar
cdx6500SNMPGenTrapsType = _Cdx6500SNMPGenTrapsType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 8),
    _Cdx6500SNMPGenTrapsType_Type()
)
cdx6500SNMPGenTrapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPGenTrapsType.setStatus("mandatory")
_Cdx6500SNMPTrapThrottleTable_Object = MibTable
cdx6500SNMPTrapThrottleTable = _Cdx6500SNMPTrapThrottleTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cdx6500SNMPTrapThrottleTable.setStatus("mandatory")
_Cdx6500SNMPTrapThrottleEntry_Object = MibTableRow
cdx6500SNMPTrapThrottleEntry = _Cdx6500SNMPTrapThrottleEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 9, 1)
)
cdx6500SNMPTrapThrottleEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500SNMPTrapNumber"),
)
if mibBuilder.loadTexts:
    cdx6500SNMPTrapThrottleEntry.setStatus("mandatory")


class _Cdx6500SNMPTrapNumber_Type(Integer32):
    """Custom type cdx6500SNMPTrapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2147483647),
    )


_Cdx6500SNMPTrapNumber_Type.__name__ = "Integer32"
_Cdx6500SNMPTrapNumber_Object = MibTableColumn
cdx6500SNMPTrapNumber = _Cdx6500SNMPTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 9, 1, 1),
    _Cdx6500SNMPTrapNumber_Type()
)
cdx6500SNMPTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SNMPTrapNumber.setStatus("mandatory")


class _Cdx6500SNMPMaxNumOfTraps_Type(Integer32):
    """Custom type cdx6500SNMPMaxNumOfTraps based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500SNMPMaxNumOfTraps_Type.__name__ = "Integer32"
_Cdx6500SNMPMaxNumOfTraps_Object = MibTableColumn
cdx6500SNMPMaxNumOfTraps = _Cdx6500SNMPMaxNumOfTraps_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 9, 1, 2),
    _Cdx6500SNMPMaxNumOfTraps_Type()
)
cdx6500SNMPMaxNumOfTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPMaxNumOfTraps.setStatus("mandatory")


class _Cdx6500SNMPThrottlingPeriod_Type(Integer32):
    """Custom type cdx6500SNMPThrottlingPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500SNMPThrottlingPeriod_Type.__name__ = "Integer32"
_Cdx6500SNMPThrottlingPeriod_Object = MibTableColumn
cdx6500SNMPThrottlingPeriod = _Cdx6500SNMPThrottlingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 9, 1, 3),
    _Cdx6500SNMPThrottlingPeriod_Type()
)
cdx6500SNMPThrottlingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPThrottlingPeriod.setStatus("mandatory")


class _Cdx6500SNMPNewTrapLevel_Type(Integer32):
    """Custom type cdx6500SNMPNewTrapLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 5),
          ("medium", 3),
          ("unchanged", 1))
    )


_Cdx6500SNMPNewTrapLevel_Type.__name__ = "Integer32"
_Cdx6500SNMPNewTrapLevel_Object = MibTableColumn
cdx6500SNMPNewTrapLevel = _Cdx6500SNMPNewTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 9, 1, 4),
    _Cdx6500SNMPNewTrapLevel_Type()
)
cdx6500SNMPNewTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPNewTrapLevel.setStatus("mandatory")


class _Cdx6500SNMPEntryStatus_Type(Integer32):
    """Custom type cdx6500SNMPEntryStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deleted", 2))
    )


_Cdx6500SNMPEntryStatus_Type.__name__ = "Integer32"
_Cdx6500SNMPEntryStatus_Object = MibTableColumn
cdx6500SNMPEntryStatus = _Cdx6500SNMPEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 9, 1, 5),
    _Cdx6500SNMPEntryStatus_Type()
)
cdx6500SNMPEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPEntryStatus.setStatus("mandatory")


class _Cdx6500SNMPSetControl_Type(Integer32):
    """Custom type cdx6500SNMPSetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Cdx6500SNMPSetControl_Type.__name__ = "Integer32"
_Cdx6500SNMPSetControl_Object = MibScalar
cdx6500SNMPSetControl = _Cdx6500SNMPSetControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 10),
    _Cdx6500SNMPSetControl_Type()
)
cdx6500SNMPSetControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SNMPSetControl.setStatus("mandatory")
_Cdx6500SNMPIpAddress_Type = DisplayString
_Cdx6500SNMPIpAddress_Object = MibScalar
cdx6500SNMPIpAddress = _Cdx6500SNMPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1, 11),
    _Cdx6500SNMPIpAddress_Type()
)
cdx6500SNMPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500SNMPIpAddress.setStatus("mandatory")
_Cdx6500NMNodeParametersGroup_ObjectIdentity = ObjectIdentity
cdx6500NMNodeParametersGroup = _Cdx6500NMNodeParametersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2)
)
_Cdx6500NMNPconfig_ObjectIdentity = ObjectIdentity
cdx6500NMNPconfig = _Cdx6500NMNPconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1)
)


class _Cdx6500NMNPCnodeName_Type(DisplayString):
    """Custom type cdx6500NMNPCnodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500NMNPCnodeName_Type.__name__ = "DisplayString"
_Cdx6500NMNPCnodeName_Object = MibScalar
cdx6500NMNPCnodeName = _Cdx6500NMNPCnodeName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 1),
    _Cdx6500NMNPCnodeName_Type()
)
cdx6500NMNPCnodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCnodeName.setStatus("mandatory")


class _Cdx6500NMNPCnodeNum_Type(Integer32):
    """Custom type cdx6500NMNPCnodeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500NMNPCnodeNum_Type.__name__ = "Integer32"
_Cdx6500NMNPCnodeNum_Object = MibScalar
cdx6500NMNPCnodeNum = _Cdx6500NMNPCnodeNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 2),
    _Cdx6500NMNPCnodeNum_Type()
)
cdx6500NMNPCnodeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCnodeNum.setStatus("mandatory")


class _Cdx6500NMNPCnodeAddress_Type(DisplayString):
    """Custom type cdx6500NMNPCnodeAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_Cdx6500NMNPCnodeAddress_Type.__name__ = "DisplayString"
_Cdx6500NMNPCnodeAddress_Object = MibScalar
cdx6500NMNPCnodeAddress = _Cdx6500NMNPCnodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 3),
    _Cdx6500NMNPCnodeAddress_Type()
)
cdx6500NMNPCnodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCnodeAddress.setStatus("mandatory")


class _Cdx6500NMNPCchassis_Type(Integer32):
    """Custom type cdx6500NMNPCchassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              50)
        )
    )
    namedValues = NamedValues(
        *(("chassis6520", 5),
          ("chassis6560", 6),
          ("modulus18", 2),
          ("modulus19", 4),
          ("modulus8", 1),
          ("modulus9", 3),
          ("newvalStandalone", 50),
          ("standalone", 0))
    )


_Cdx6500NMNPCchassis_Type.__name__ = "Integer32"
_Cdx6500NMNPCchassis_Object = MibScalar
cdx6500NMNPCchassis = _Cdx6500NMNPCchassis_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 4),
    _Cdx6500NMNPCchassis_Type()
)
cdx6500NMNPCchassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCchassis.setStatus("mandatory")


class _Cdx6500NMNPCdate_Type(DisplayString):
    """Custom type cdx6500NMNPCdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Cdx6500NMNPCdate_Type.__name__ = "DisplayString"
_Cdx6500NMNPCdate_Object = MibScalar
cdx6500NMNPCdate = _Cdx6500NMNPCdate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 5),
    _Cdx6500NMNPCdate_Type()
)
cdx6500NMNPCdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCdate.setStatus("mandatory")


class _Cdx6500NMNPCtime_Type(DisplayString):
    """Custom type cdx6500NMNPCtime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500NMNPCtime_Type.__name__ = "DisplayString"
_Cdx6500NMNPCtime_Object = MibScalar
cdx6500NMNPCtime = _Cdx6500NMNPCtime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 6),
    _Cdx6500NMNPCtime_Type()
)
cdx6500NMNPCtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCtime.setStatus("mandatory")


class _Cdx6500NMNPCportUtil_Type(Integer32):
    """Custom type cdx6500NMNPCportUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 99),
    )


_Cdx6500NMNPCportUtil_Type.__name__ = "Integer32"
_Cdx6500NMNPCportUtil_Object = MibScalar
cdx6500NMNPCportUtil = _Cdx6500NMNPCportUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 7),
    _Cdx6500NMNPCportUtil_Type()
)
cdx6500NMNPCportUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCportUtil.setStatus("mandatory")


class _Cdx6500NMNPCbuffUtil_Type(Integer32):
    """Custom type cdx6500NMNPCbuffUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 99),
    )


_Cdx6500NMNPCbuffUtil_Type.__name__ = "Integer32"
_Cdx6500NMNPCbuffUtil_Object = MibScalar
cdx6500NMNPCbuffUtil = _Cdx6500NMNPCbuffUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 8),
    _Cdx6500NMNPCbuffUtil_Type()
)
cdx6500NMNPCbuffUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCbuffUtil.setStatus("mandatory")


class _Cdx6500NMNPCcpuUtil_Type(Integer32):
    """Custom type cdx6500NMNPCcpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 99),
    )


_Cdx6500NMNPCcpuUtil_Type.__name__ = "Integer32"
_Cdx6500NMNPCcpuUtil_Object = MibScalar
cdx6500NMNPCcpuUtil = _Cdx6500NMNPCcpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 9),
    _Cdx6500NMNPCcpuUtil_Type()
)
cdx6500NMNPCcpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCcpuUtil.setStatus("mandatory")


class _Cdx6500NMNPCportErr_Type(Integer32):
    """Custom type cdx6500NMNPCportErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500NMNPCportErr_Type.__name__ = "Integer32"
_Cdx6500NMNPCportErr_Object = MibScalar
cdx6500NMNPCportErr = _Cdx6500NMNPCportErr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 10),
    _Cdx6500NMNPCportErr_Type()
)
cdx6500NMNPCportErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCportErr.setStatus("mandatory")


class _Cdx6500NMNPCalarmTmr_Type(Integer32):
    """Custom type cdx6500NMNPCalarmTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 255),
    )


_Cdx6500NMNPCalarmTmr_Type.__name__ = "Integer32"
_Cdx6500NMNPCalarmTmr_Object = MibScalar
cdx6500NMNPCalarmTmr = _Cdx6500NMNPCalarmTmr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 11),
    _Cdx6500NMNPCalarmTmr_Type()
)
cdx6500NMNPCalarmTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCalarmTmr.setStatus("mandatory")


class _Cdx6500NMNPCmaxRoutHops_Type(Integer32):
    """Custom type cdx6500NMNPCmaxRoutHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Cdx6500NMNPCmaxRoutHops_Type.__name__ = "Integer32"
_Cdx6500NMNPCmaxRoutHops_Object = MibScalar
cdx6500NMNPCmaxRoutHops = _Cdx6500NMNPCmaxRoutHops_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 12),
    _Cdx6500NMNPCmaxRoutHops_Type()
)
cdx6500NMNPCmaxRoutHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCmaxRoutHops.setStatus("mandatory")


class _Cdx6500NMNPCctpSubAddr_Type(DisplayString):
    """Custom type cdx6500NMNPCctpSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500NMNPCctpSubAddr_Type.__name__ = "DisplayString"
_Cdx6500NMNPCctpSubAddr_Object = MibScalar
cdx6500NMNPCctpSubAddr = _Cdx6500NMNPCctpSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 13),
    _Cdx6500NMNPCctpSubAddr_Type()
)
cdx6500NMNPCctpSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCctpSubAddr.setStatus("mandatory")


class _Cdx6500NMNPCctpIdleTime_Type(Integer32):
    """Custom type cdx6500NMNPCctpIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500NMNPCctpIdleTime_Type.__name__ = "Integer32"
_Cdx6500NMNPCctpIdleTime_Object = MibScalar
cdx6500NMNPCctpIdleTime = _Cdx6500NMNPCctpIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 14),
    _Cdx6500NMNPCctpIdleTime_Type()
)
cdx6500NMNPCctpIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCctpIdleTime.setStatus("mandatory")


class _Cdx6500NMNPCalmDist_Type(Integer32):
    """Custom type cdx6500NMNPCalmDist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500NMNPCalmDist_Type.__name__ = "Integer32"
_Cdx6500NMNPCalmDist_Object = MibScalar
cdx6500NMNPCalmDist = _Cdx6500NMNPCalmDist_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 15),
    _Cdx6500NMNPCalmDist_Type()
)
cdx6500NMNPCalmDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCalmDist.setStatus("deprecated")


class _Cdx6500NMNPCalmMmem_Type(DisplayString):
    """Custom type cdx6500NMNPCalmMmem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500NMNPCalmMmem_Type.__name__ = "DisplayString"
_Cdx6500NMNPCalmMmem_Object = MibScalar
cdx6500NMNPCalmMmem = _Cdx6500NMNPCalmMmem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 16),
    _Cdx6500NMNPCalmMmem_Type()
)
cdx6500NMNPCalmMmem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCalmMmem.setStatus("mandatory")


class _Cdx6500NMNPCalmSelect_Type(Integer32):
    """Custom type cdx6500NMNPCalmSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500NMNPCalmSelect_Type.__name__ = "Integer32"
_Cdx6500NMNPCalmSelect_Object = MibScalar
cdx6500NMNPCalmSelect = _Cdx6500NMNPCalmSelect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 17),
    _Cdx6500NMNPCalmSelect_Type()
)
cdx6500NMNPCalmSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCalmSelect.setStatus("deprecated")


class _Cdx6500NMNPCbroadPortSubad_Type(DisplayString):
    """Custom type cdx6500NMNPCbroadPortSubad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500NMNPCbroadPortSubad_Type.__name__ = "DisplayString"
_Cdx6500NMNPCbroadPortSubad_Object = MibScalar
cdx6500NMNPCbroadPortSubad = _Cdx6500NMNPCbroadPortSubad_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 18),
    _Cdx6500NMNPCbroadPortSubad_Type()
)
cdx6500NMNPCbroadPortSubad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCbroadPortSubad.setStatus("mandatory")


class _Cdx6500NMNPCnoBroadNets_Type(Integer32):
    """Custom type cdx6500NMNPCnoBroadNets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500NMNPCnoBroadNets_Type.__name__ = "Integer32"
_Cdx6500NMNPCnoBroadNets_Object = MibScalar
cdx6500NMNPCnoBroadNets = _Cdx6500NMNPCnoBroadNets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 19),
    _Cdx6500NMNPCnoBroadNets_Type()
)
cdx6500NMNPCnoBroadNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCnoBroadNets.setStatus("mandatory")


class _Cdx6500NMNPCnoBroadInCh_Type(Integer32):
    """Custom type cdx6500NMNPCnoBroadInCh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Cdx6500NMNPCnoBroadInCh_Type.__name__ = "Integer32"
_Cdx6500NMNPCnoBroadInCh_Object = MibScalar
cdx6500NMNPCnoBroadInCh = _Cdx6500NMNPCnoBroadInCh_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 20),
    _Cdx6500NMNPCnoBroadInCh_Type()
)
cdx6500NMNPCnoBroadInCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCnoBroadInCh.setStatus("mandatory")


class _Cdx6500NMNPCbillMnem_Type(DisplayString):
    """Custom type cdx6500NMNPCbillMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500NMNPCbillMnem_Type.__name__ = "DisplayString"
_Cdx6500NMNPCbillMnem_Object = MibScalar
cdx6500NMNPCbillMnem = _Cdx6500NMNPCbillMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 21),
    _Cdx6500NMNPCbillMnem_Type()
)
cdx6500NMNPCbillMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCbillMnem.setStatus("mandatory")


class _Cdx6500NMNPCbillThresh_Type(Integer32):
    """Custom type cdx6500NMNPCbillThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Cdx6500NMNPCbillThresh_Type.__name__ = "Integer32"
_Cdx6500NMNPCbillThresh_Object = MibScalar
cdx6500NMNPCbillThresh = _Cdx6500NMNPCbillThresh_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 22),
    _Cdx6500NMNPCbillThresh_Type()
)
cdx6500NMNPCbillThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCbillThresh.setStatus("mandatory")


class _Cdx6500NMNPCmaxBill_Type(Integer32):
    """Custom type cdx6500NMNPCmaxBill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Cdx6500NMNPCmaxBill_Type.__name__ = "Integer32"
_Cdx6500NMNPCmaxBill_Object = MibScalar
cdx6500NMNPCmaxBill = _Cdx6500NMNPCmaxBill_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 23),
    _Cdx6500NMNPCmaxBill_Type()
)
cdx6500NMNPCmaxBill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCmaxBill.setStatus("mandatory")


class _Cdx6500NMNPCbillTimer_Type(Integer32):
    """Custom type cdx6500NMNPCbillTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500NMNPCbillTimer_Type.__name__ = "Integer32"
_Cdx6500NMNPCbillTimer_Object = MibScalar
cdx6500NMNPCbillTimer = _Cdx6500NMNPCbillTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 24),
    _Cdx6500NMNPCbillTimer_Type()
)
cdx6500NMNPCbillTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCbillTimer.setStatus("mandatory")


class _Cdx6500NMNPCpvcBill_Type(Integer32):
    """Custom type cdx6500NMNPCpvcBill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500NMNPCpvcBill_Type.__name__ = "Integer32"
_Cdx6500NMNPCpvcBill_Object = MibScalar
cdx6500NMNPCpvcBill = _Cdx6500NMNPCpvcBill_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 25),
    _Cdx6500NMNPCpvcBill_Type()
)
cdx6500NMNPCpvcBill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCpvcBill.setStatus("mandatory")


class _Cdx6500NMNPCmaxCalls_Type(Integer32):
    """Custom type cdx6500NMNPCmaxCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Cdx6500NMNPCmaxCalls_Type.__name__ = "Integer32"
_Cdx6500NMNPCmaxCalls_Object = MibScalar
cdx6500NMNPCmaxCalls = _Cdx6500NMNPCmaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 26),
    _Cdx6500NMNPCmaxCalls_Type()
)
cdx6500NMNPCmaxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCmaxCalls.setStatus("mandatory")
_Cdx6500NMNPCpadBulletin_Type = DisplayString
_Cdx6500NMNPCpadBulletin_Object = MibScalar
cdx6500NMNPCpadBulletin = _Cdx6500NMNPCpadBulletin_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 27),
    _Cdx6500NMNPCpadBulletin_Type()
)
cdx6500NMNPCpadBulletin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCpadBulletin.setStatus("mandatory")


class _Cdx6500NMNPCpadBanner_Type(DisplayString):
    """Custom type cdx6500NMNPCpadBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cdx6500NMNPCpadBanner_Type.__name__ = "DisplayString"
_Cdx6500NMNPCpadBanner_Object = MibScalar
cdx6500NMNPCpadBanner = _Cdx6500NMNPCpadBanner_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 28),
    _Cdx6500NMNPCpadBanner_Type()
)
cdx6500NMNPCpadBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCpadBanner.setStatus("mandatory")


class _Cdx6500NMNPCdcpFac_Type(Integer32):
    """Custom type cdx6500NMNPCdcpFac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(201, 254),
    )


_Cdx6500NMNPCdcpFac_Type.__name__ = "Integer32"
_Cdx6500NMNPCdcpFac_Object = MibScalar
cdx6500NMNPCdcpFac = _Cdx6500NMNPCdcpFac_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 29),
    _Cdx6500NMNPCdcpFac_Type()
)
cdx6500NMNPCdcpFac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCdcpFac.setStatus("mandatory")


class _Cdx6500NMNPCtrafficPri_Type(Integer32):
    """Custom type cdx6500NMNPCtrafficPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("exp", 3),
          ("high", 2),
          ("low", 0),
          ("med", 1),
          ("newvalLow", 50))
    )


_Cdx6500NMNPCtrafficPri_Type.__name__ = "Integer32"
_Cdx6500NMNPCtrafficPri_Object = MibScalar
cdx6500NMNPCtrafficPri = _Cdx6500NMNPCtrafficPri_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 30),
    _Cdx6500NMNPCtrafficPri_Type()
)
cdx6500NMNPCtrafficPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCtrafficPri.setStatus("mandatory")


class _Cdx6500NMNPCtrafficStep_Type(Integer32):
    """Custom type cdx6500NMNPCtrafficStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500NMNPCtrafficStep_Type.__name__ = "Integer32"
_Cdx6500NMNPCtrafficStep_Object = MibScalar
cdx6500NMNPCtrafficStep = _Cdx6500NMNPCtrafficStep_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 31),
    _Cdx6500NMNPCtrafficStep_Type()
)
cdx6500NMNPCtrafficStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCtrafficStep.setStatus("mandatory")


class _Cdx6500NMNPCpropProtId_Type(Integer32):
    """Custom type cdx6500NMNPCpropProtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 255),
    )


_Cdx6500NMNPCpropProtId_Type.__name__ = "Integer32"
_Cdx6500NMNPCpropProtId_Object = MibScalar
cdx6500NMNPCpropProtId = _Cdx6500NMNPCpropProtId_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 32),
    _Cdx6500NMNPCpropProtId_Type()
)
cdx6500NMNPCpropProtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCpropProtId.setStatus("mandatory")


class _Cdx6500NMNPClanSubAddr_Type(DisplayString):
    """Custom type cdx6500NMNPClanSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500NMNPClanSubAddr_Type.__name__ = "DisplayString"
_Cdx6500NMNPClanSubAddr_Object = MibScalar
cdx6500NMNPClanSubAddr = _Cdx6500NMNPClanSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 33),
    _Cdx6500NMNPClanSubAddr_Type()
)
cdx6500NMNPClanSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPClanSubAddr.setStatus("mandatory")


class _Cdx6500NMNPCMaxFrameSize_Type(Integer32):
    """Custom type cdx6500NMNPCMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500NMNPCMaxFrameSize_Type.__name__ = "Integer32"
_Cdx6500NMNPCMaxFrameSize_Object = MibScalar
cdx6500NMNPCMaxFrameSize = _Cdx6500NMNPCMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 34),
    _Cdx6500NMNPCMaxFrameSize_Type()
)
cdx6500NMNPCMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCMaxFrameSize.setStatus("mandatory")


class _Cdx6500NMNPCCodexGroupFacility_Type(Integer32):
    """Custom type cdx6500NMNPCCodexGroupFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(202, 254),
    )


_Cdx6500NMNPCCodexGroupFacility_Type.__name__ = "Integer32"
_Cdx6500NMNPCCodexGroupFacility_Object = MibScalar
cdx6500NMNPCCodexGroupFacility = _Cdx6500NMNPCCodexGroupFacility_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 35),
    _Cdx6500NMNPCCodexGroupFacility_Type()
)
cdx6500NMNPCCodexGroupFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCCodexGroupFacility.setStatus("mandatory")


class _Cdx6500NMNPCalmDistrib_Type(DisplayString):
    """Custom type cdx6500NMNPCalmDistrib based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 8),
    )


_Cdx6500NMNPCalmDistrib_Type.__name__ = "DisplayString"
_Cdx6500NMNPCalmDistrib_Object = MibScalar
cdx6500NMNPCalmDistrib = _Cdx6500NMNPCalmDistrib_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 36),
    _Cdx6500NMNPCalmDistrib_Type()
)
cdx6500NMNPCalmDistrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCalmDistrib.setStatus("mandatory")


class _Cdx6500NMNPCalmSelection_Type(DisplayString):
    """Custom type cdx6500NMNPCalmSelection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 27),
    )


_Cdx6500NMNPCalmSelection_Type.__name__ = "DisplayString"
_Cdx6500NMNPCalmSelection_Object = MibScalar
cdx6500NMNPCalmSelection = _Cdx6500NMNPCalmSelection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 37),
    _Cdx6500NMNPCalmSelection_Type()
)
cdx6500NMNPCalmSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCalmSelection.setStatus("mandatory")


class _Cdx6500NMNPChopFacility_Type(Integer32):
    """Custom type cdx6500NMNPChopFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 254),
    )


_Cdx6500NMNPChopFacility_Type.__name__ = "Integer32"
_Cdx6500NMNPChopFacility_Object = MibScalar
cdx6500NMNPChopFacility = _Cdx6500NMNPChopFacility_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 38),
    _Cdx6500NMNPChopFacility_Type()
)
cdx6500NMNPChopFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPChopFacility.setStatus("mandatory")


class _Cdx6500NMNPCnumNccpDevices_Type(Integer32):
    """Custom type cdx6500NMNPCnumNccpDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Cdx6500NMNPCnumNccpDevices_Type.__name__ = "Integer32"
_Cdx6500NMNPCnumNccpDevices_Object = MibScalar
cdx6500NMNPCnumNccpDevices = _Cdx6500NMNPCnumNccpDevices_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 39),
    _Cdx6500NMNPCnumNccpDevices_Type()
)
cdx6500NMNPCnumNccpDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCnumNccpDevices.setStatus("mandatory")


class _Cdx6500NMNPCmaxCallid_Type(Integer32):
    """Custom type cdx6500NMNPCmaxCallid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Cdx6500NMNPCmaxCallid_Type.__name__ = "Integer32"
_Cdx6500NMNPCmaxCallid_Object = MibScalar
cdx6500NMNPCmaxCallid = _Cdx6500NMNPCmaxCallid_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 1, 40),
    _Cdx6500NMNPCmaxCallid_Type()
)
cdx6500NMNPCmaxCallid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPCmaxCallid.setStatus("mandatory")
_Cdx6500NMNPinvent_ObjectIdentity = ObjectIdentity
cdx6500NMNPinvent = _Cdx6500NMNPinvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2)
)
_Cdx6500NMNPIproductType_Type = DisplayString
_Cdx6500NMNPIproductType_Object = MibScalar
cdx6500NMNPIproductType = _Cdx6500NMNPIproductType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 1),
    _Cdx6500NMNPIproductType_Type()
)
cdx6500NMNPIproductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIproductType.setStatus("mandatory")


class _Cdx6500NMNPIsoftwareSrc_Type(Integer32):
    """Custom type cdx6500NMNPIsoftwareSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("newvalProm", 50),
          ("prom", 0),
          ("promLoadingRAM", 2))
    )


_Cdx6500NMNPIsoftwareSrc_Type.__name__ = "Integer32"
_Cdx6500NMNPIsoftwareSrc_Object = MibScalar
cdx6500NMNPIsoftwareSrc = _Cdx6500NMNPIsoftwareSrc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 2),
    _Cdx6500NMNPIsoftwareSrc_Type()
)
cdx6500NMNPIsoftwareSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIsoftwareSrc.setStatus("mandatory")
_Cdx6500NMNPIserialNum_Type = Integer32
_Cdx6500NMNPIserialNum_Object = MibScalar
cdx6500NMNPIserialNum = _Cdx6500NMNPIserialNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 3),
    _Cdx6500NMNPIserialNum_Type()
)
cdx6500NMNPIserialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIserialNum.setStatus("mandatory")
_Cdx6500NMNPIpromRevision_Type = DisplayString
_Cdx6500NMNPIpromRevision_Object = MibScalar
cdx6500NMNPIpromRevision = _Cdx6500NMNPIpromRevision_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 4),
    _Cdx6500NMNPIpromRevision_Type()
)
cdx6500NMNPIpromRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIpromRevision.setStatus("mandatory")
_Cdx6500NMNPIdlCodeRevision_Type = DisplayString
_Cdx6500NMNPIdlCodeRevision_Object = MibScalar
cdx6500NMNPIdlCodeRevision = _Cdx6500NMNPIdlCodeRevision_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 5),
    _Cdx6500NMNPIdlCodeRevision_Type()
)
cdx6500NMNPIdlCodeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIdlCodeRevision.setStatus("optional")
_Cdx6500NMNPIdlCodeSource_Type = DisplayString
_Cdx6500NMNPIdlCodeSource_Object = MibScalar
cdx6500NMNPIdlCodeSource = _Cdx6500NMNPIdlCodeSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 6),
    _Cdx6500NMNPIdlCodeSource_Type()
)
cdx6500NMNPIdlCodeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIdlCodeSource.setStatus("optional")
_Cdx6500NMNPIdlCodeSize_Type = Integer32
_Cdx6500NMNPIdlCodeSize_Object = MibScalar
cdx6500NMNPIdlCodeSize = _Cdx6500NMNPIdlCodeSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 7),
    _Cdx6500NMNPIdlCodeSize_Type()
)
cdx6500NMNPIdlCodeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIdlCodeSize.setStatus("optional")


class _Cdx6500NMNPIflashStatus_Type(Integer32):
    """Custom type cdx6500NMNPIflashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0),
          ("newvalEnabled", 50))
    )


_Cdx6500NMNPIflashStatus_Type.__name__ = "Integer32"
_Cdx6500NMNPIflashStatus_Object = MibScalar
cdx6500NMNPIflashStatus = _Cdx6500NMNPIflashStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 8),
    _Cdx6500NMNPIflashStatus_Type()
)
cdx6500NMNPIflashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIflashStatus.setStatus("optional")
_Cdx6500NMNPIflashIdCur_Type = DisplayString
_Cdx6500NMNPIflashIdCur_Object = MibScalar
cdx6500NMNPIflashIdCur = _Cdx6500NMNPIflashIdCur_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 9),
    _Cdx6500NMNPIflashIdCur_Type()
)
cdx6500NMNPIflashIdCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIflashIdCur.setStatus("mandatory")
_Cdx6500NMNPIflashIdAlt_Type = DisplayString
_Cdx6500NMNPIflashIdAlt_Object = MibScalar
cdx6500NMNPIflashIdAlt = _Cdx6500NMNPIflashIdAlt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 10),
    _Cdx6500NMNPIflashIdAlt_Type()
)
cdx6500NMNPIflashIdAlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIflashIdAlt.setStatus("optional")
_Cdx6500NMNPIflashSizeCur_Type = Integer32
_Cdx6500NMNPIflashSizeCur_Object = MibScalar
cdx6500NMNPIflashSizeCur = _Cdx6500NMNPIflashSizeCur_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 11),
    _Cdx6500NMNPIflashSizeCur_Type()
)
cdx6500NMNPIflashSizeCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIflashSizeCur.setStatus("mandatory")
_Cdx6500NMNPIflashSizeAlt_Type = Integer32
_Cdx6500NMNPIflashSizeAlt_Object = MibScalar
cdx6500NMNPIflashSizeAlt = _Cdx6500NMNPIflashSizeAlt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 12),
    _Cdx6500NMNPIflashSizeAlt_Type()
)
cdx6500NMNPIflashSizeAlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIflashSizeAlt.setStatus("optional")
_Cdx6500NMNPIinventTable_Object = MibTable
cdx6500NMNPIinventTable = _Cdx6500NMNPIinventTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13)
)
if mibBuilder.loadTexts:
    cdx6500NMNPIinventTable.setStatus("mandatory")
_Cdx6500NMNPIinventEntry_Object = MibTableRow
cdx6500NMNPIinventEntry = _Cdx6500NMNPIinventEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1)
)
cdx6500NMNPIinventEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500NMNPIinventBoard"),
)
if mibBuilder.loadTexts:
    cdx6500NMNPIinventEntry.setStatus("mandatory")
_Cdx6500NMNPIinventBoard_Type = Integer32
_Cdx6500NMNPIinventBoard_Object = MibTableColumn
cdx6500NMNPIinventBoard = _Cdx6500NMNPIinventBoard_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 1),
    _Cdx6500NMNPIinventBoard_Type()
)
cdx6500NMNPIinventBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventBoard.setStatus("mandatory")
_Cdx6500NMNPIinventType_Type = DisplayString
_Cdx6500NMNPIinventType_Object = MibTableColumn
cdx6500NMNPIinventType = _Cdx6500NMNPIinventType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 2),
    _Cdx6500NMNPIinventType_Type()
)
cdx6500NMNPIinventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventType.setStatus("mandatory")
_Cdx6500NMNPIinventPorts_Type = Integer32
_Cdx6500NMNPIinventPorts_Object = MibTableColumn
cdx6500NMNPIinventPorts = _Cdx6500NMNPIinventPorts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 3),
    _Cdx6500NMNPIinventPorts_Type()
)
cdx6500NMNPIinventPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventPorts.setStatus("mandatory")
_Cdx6500NMNPIinventStatus_Type = DisplayString
_Cdx6500NMNPIinventStatus_Object = MibTableColumn
cdx6500NMNPIinventStatus = _Cdx6500NMNPIinventStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 4),
    _Cdx6500NMNPIinventStatus_Type()
)
cdx6500NMNPIinventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventStatus.setStatus("mandatory")
_Cdx6500NMNPIinventSerial_Type = DisplayString
_Cdx6500NMNPIinventSerial_Object = MibTableColumn
cdx6500NMNPIinventSerial = _Cdx6500NMNPIinventSerial_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 5),
    _Cdx6500NMNPIinventSerial_Type()
)
cdx6500NMNPIinventSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventSerial.setStatus("mandatory")
_Cdx6500NMNPIinventAssy_Type = DisplayString
_Cdx6500NMNPIinventAssy_Object = MibTableColumn
cdx6500NMNPIinventAssy = _Cdx6500NMNPIinventAssy_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 6),
    _Cdx6500NMNPIinventAssy_Type()
)
cdx6500NMNPIinventAssy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventAssy.setStatus("mandatory")
_Cdx6500NMNPIinventRev_Type = DisplayString
_Cdx6500NMNPIinventRev_Object = MibTableColumn
cdx6500NMNPIinventRev = _Cdx6500NMNPIinventRev_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 7),
    _Cdx6500NMNPIinventRev_Type()
)
cdx6500NMNPIinventRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventRev.setStatus("mandatory")
_Cdx6500NMNPIinventDIM1_Type = DisplayString
_Cdx6500NMNPIinventDIM1_Object = MibTableColumn
cdx6500NMNPIinventDIM1 = _Cdx6500NMNPIinventDIM1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 8),
    _Cdx6500NMNPIinventDIM1_Type()
)
cdx6500NMNPIinventDIM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventDIM1.setStatus("mandatory")
_Cdx6500NMNPIinventDIM2_Type = DisplayString
_Cdx6500NMNPIinventDIM2_Object = MibTableColumn
cdx6500NMNPIinventDIM2 = _Cdx6500NMNPIinventDIM2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 13, 1, 9),
    _Cdx6500NMNPIinventDIM2_Type()
)
cdx6500NMNPIinventDIM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventDIM2.setStatus("mandatory")
_Cdx6500NMNPIinventPortConfigTable_Object = MibTable
cdx6500NMNPIinventPortConfigTable = _Cdx6500NMNPIinventPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 14)
)
if mibBuilder.loadTexts:
    cdx6500NMNPIinventPortConfigTable.setStatus("mandatory")
_Cdx6500NMNPIinventPortConfigEntry_Object = MibTableRow
cdx6500NMNPIinventPortConfigEntry = _Cdx6500NMNPIinventPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 14, 1)
)
cdx6500NMNPIinventPortConfigEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500NMNPIinventPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500NMNPIinventPortConfigEntry.setStatus("mandatory")
_Cdx6500NMNPIinventPortNum_Type = Integer32
_Cdx6500NMNPIinventPortNum_Object = MibTableColumn
cdx6500NMNPIinventPortNum = _Cdx6500NMNPIinventPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 14, 1, 1),
    _Cdx6500NMNPIinventPortNum_Type()
)
cdx6500NMNPIinventPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventPortNum.setStatus("mandatory")
_Cdx6500NMNPIinventPortConfig_Type = DisplayString
_Cdx6500NMNPIinventPortConfig_Object = MibTableColumn
cdx6500NMNPIinventPortConfig = _Cdx6500NMNPIinventPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 2, 14, 1, 2),
    _Cdx6500NMNPIinventPortConfig_Type()
)
cdx6500NMNPIinventPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPIinventPortConfig.setStatus("mandatory")
_Cdx6500NMNPstats_ObjectIdentity = ObjectIdentity
cdx6500NMNPstats = _Cdx6500NMNPstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3)
)
_Cdx6500NMNPSevLastOccPower_Type = DisplayString
_Cdx6500NMNPSevLastOccPower_Object = MibScalar
cdx6500NMNPSevLastOccPower = _Cdx6500NMNPSevLastOccPower_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 1),
    _Cdx6500NMNPSevLastOccPower_Type()
)
cdx6500NMNPSevLastOccPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSevLastOccPower.setStatus("mandatory")
_Cdx6500NMNPSevLastOccReset_Type = DisplayString
_Cdx6500NMNPSevLastOccReset_Object = MibScalar
cdx6500NMNPSevLastOccReset = _Cdx6500NMNPSevLastOccReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 2),
    _Cdx6500NMNPSevLastOccReset_Type()
)
cdx6500NMNPSevLastOccReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSevLastOccReset.setStatus("mandatory")
_Cdx6500NMNPSevLastOccReboot_Type = DisplayString
_Cdx6500NMNPSevLastOccReboot_Object = MibScalar
cdx6500NMNPSevLastOccReboot = _Cdx6500NMNPSevLastOccReboot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 3),
    _Cdx6500NMNPSevLastOccReboot_Type()
)
cdx6500NMNPSevLastOccReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSevLastOccReboot.setStatus("mandatory")
_Cdx6500NMNPSevLastOccWDTimer_Type = DisplayString
_Cdx6500NMNPSevLastOccWDTimer_Object = MibScalar
cdx6500NMNPSevLastOccWDTimer = _Cdx6500NMNPSevLastOccWDTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 4),
    _Cdx6500NMNPSevLastOccWDTimer_Type()
)
cdx6500NMNPSevLastOccWDTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSevLastOccWDTimer.setStatus("mandatory")
_Cdx6500NMNPSevLastOccConfig_Type = DisplayString
_Cdx6500NMNPSevLastOccConfig_Object = MibScalar
cdx6500NMNPSevLastOccConfig = _Cdx6500NMNPSevLastOccConfig_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 5),
    _Cdx6500NMNPSevLastOccConfig_Type()
)
cdx6500NMNPSevLastOccConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSevLastOccConfig.setStatus("mandatory")


class _Cdx6500NMNPSstatusFan_Type(Integer32):
    """Custom type cdx6500NMNPSstatusFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("impaired", 2),
          ("newvalNotMonitored", 50),
          ("notMonitored", 0),
          ("operational", 1))
    )


_Cdx6500NMNPSstatusFan_Type.__name__ = "Integer32"
_Cdx6500NMNPSstatusFan_Object = MibScalar
cdx6500NMNPSstatusFan = _Cdx6500NMNPSstatusFan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 6),
    _Cdx6500NMNPSstatusFan_Type()
)
cdx6500NMNPSstatusFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatusFan.setStatus("mandatory")


class _Cdx6500NMNPSstatusPwrSy_Type(Integer32):
    """Custom type cdx6500NMNPSstatusPwrSy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("impaired", 2),
          ("newvalNotMonitored", 50),
          ("notAvailable", 100),
          ("notMonitored", 0),
          ("operational", 1))
    )


_Cdx6500NMNPSstatusPwrSy_Type.__name__ = "Integer32"
_Cdx6500NMNPSstatusPwrSy_Object = MibScalar
cdx6500NMNPSstatusPwrSy = _Cdx6500NMNPSstatusPwrSy_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 7),
    _Cdx6500NMNPSstatusPwrSy_Type()
)
cdx6500NMNPSstatusPwrSy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatusPwrSy.setStatus("deprecated")
_Cdx6500NMNPScmemSizeComp_Type = Integer32
_Cdx6500NMNPScmemSizeComp_Object = MibScalar
cdx6500NMNPScmemSizeComp = _Cdx6500NMNPScmemSizeComp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 8),
    _Cdx6500NMNPScmemSizeComp_Type()
)
cdx6500NMNPScmemSizeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScmemSizeComp.setStatus("mandatory")
_Cdx6500NMNPScmemUseComp_Type = Integer32
_Cdx6500NMNPScmemUseComp_Object = MibScalar
cdx6500NMNPScmemUseComp = _Cdx6500NMNPScmemUseComp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 9),
    _Cdx6500NMNPScmemUseComp_Type()
)
cdx6500NMNPScmemUseComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScmemUseComp.setStatus("mandatory")
_Cdx6500NMNPScmemSizeUncomp_Type = Integer32
_Cdx6500NMNPScmemSizeUncomp_Object = MibScalar
cdx6500NMNPScmemSizeUncomp = _Cdx6500NMNPScmemSizeUncomp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 10),
    _Cdx6500NMNPScmemSizeUncomp_Type()
)
cdx6500NMNPScmemSizeUncomp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScmemSizeUncomp.setStatus("mandatory")
_Cdx6500NMNPScmemUseUnComp_Type = Integer32
_Cdx6500NMNPScmemUseUnComp_Object = MibScalar
cdx6500NMNPScmemUseUnComp = _Cdx6500NMNPScmemUseUnComp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 11),
    _Cdx6500NMNPScmemUseUnComp_Type()
)
cdx6500NMNPScmemUseUnComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScmemUseUnComp.setStatus("mandatory")
_Cdx6500NMNPScallsInPlaceCur_Type = Integer32
_Cdx6500NMNPScallsInPlaceCur_Object = MibScalar
cdx6500NMNPScallsInPlaceCur = _Cdx6500NMNPScallsInPlaceCur_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 12),
    _Cdx6500NMNPScallsInPlaceCur_Type()
)
cdx6500NMNPScallsInPlaceCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScallsInPlaceCur.setStatus("mandatory")
_Cdx6500NMNPScallsInPlaceMax_Type = Gauge32
_Cdx6500NMNPScallsInPlaceMax_Object = MibScalar
cdx6500NMNPScallsInPlaceMax = _Cdx6500NMNPScallsInPlaceMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 13),
    _Cdx6500NMNPScallsInPlaceMax_Type()
)
cdx6500NMNPScallsInPlaceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScallsInPlaceMax.setStatus("mandatory")
_Cdx6500NMNPScallsPerSecCur_Type = Integer32
_Cdx6500NMNPScallsPerSecCur_Object = MibScalar
cdx6500NMNPScallsPerSecCur = _Cdx6500NMNPScallsPerSecCur_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 14),
    _Cdx6500NMNPScallsPerSecCur_Type()
)
cdx6500NMNPScallsPerSecCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScallsPerSecCur.setStatus("mandatory")
_Cdx6500NMNPScallsPerSecMax_Type = Gauge32
_Cdx6500NMNPScallsPerSecMax_Object = MibScalar
cdx6500NMNPScallsPerSecMax = _Cdx6500NMNPScallsPerSecMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 15),
    _Cdx6500NMNPScallsPerSecMax_Type()
)
cdx6500NMNPScallsPerSecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScallsPerSecMax.setStatus("mandatory")
_Cdx6500NMNPSpvcConnectCur_Type = Integer32
_Cdx6500NMNPSpvcConnectCur_Object = MibScalar
cdx6500NMNPSpvcConnectCur = _Cdx6500NMNPSpvcConnectCur_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 16),
    _Cdx6500NMNPSpvcConnectCur_Type()
)
cdx6500NMNPSpvcConnectCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSpvcConnectCur.setStatus("mandatory")
_Cdx6500NMNPSPVCConnectMax_Type = Gauge32
_Cdx6500NMNPSPVCConnectMax_Object = MibScalar
cdx6500NMNPSPVCConnectMax = _Cdx6500NMNPSPVCConnectMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 17),
    _Cdx6500NMNPSPVCConnectMax_Type()
)
cdx6500NMNPSPVCConnectMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSPVCConnectMax.setStatus("mandatory")
_Cdx6500NMNPSbuffDataAvail_Type = Integer32
_Cdx6500NMNPSbuffDataAvail_Object = MibScalar
cdx6500NMNPSbuffDataAvail = _Cdx6500NMNPSbuffDataAvail_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 18),
    _Cdx6500NMNPSbuffDataAvail_Type()
)
cdx6500NMNPSbuffDataAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffDataAvail.setStatus("optional")
_Cdx6500NMNPSbuffDataUse_Type = Integer32
_Cdx6500NMNPSbuffDataUse_Object = MibScalar
cdx6500NMNPSbuffDataUse = _Cdx6500NMNPSbuffDataUse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 19),
    _Cdx6500NMNPSbuffDataUse_Type()
)
cdx6500NMNPSbuffDataUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffDataUse.setStatus("optional")
_Cdx6500NMNPSbuffDataGauge_Type = Gauge32
_Cdx6500NMNPSbuffDataGauge_Object = MibScalar
cdx6500NMNPSbuffDataGauge = _Cdx6500NMNPSbuffDataGauge_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 20),
    _Cdx6500NMNPSbuffDataGauge_Type()
)
cdx6500NMNPSbuffDataGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffDataGauge.setStatus("optional")
_Cdx6500NMNPSbuffPacketAvail_Type = Integer32
_Cdx6500NMNPSbuffPacketAvail_Object = MibScalar
cdx6500NMNPSbuffPacketAvail = _Cdx6500NMNPSbuffPacketAvail_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 21),
    _Cdx6500NMNPSbuffPacketAvail_Type()
)
cdx6500NMNPSbuffPacketAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffPacketAvail.setStatus("optional")
_Cdx6500NMNPSbuffPacketUse_Type = Integer32
_Cdx6500NMNPSbuffPacketUse_Object = MibScalar
cdx6500NMNPSbuffPacketUse = _Cdx6500NMNPSbuffPacketUse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 22),
    _Cdx6500NMNPSbuffPacketUse_Type()
)
cdx6500NMNPSbuffPacketUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffPacketUse.setStatus("optional")
_Cdx6500NMNPSbuffPacketExhaust_Type = Gauge32
_Cdx6500NMNPSbuffPacketExhaust_Object = MibScalar
cdx6500NMNPSbuffPacketExhaust = _Cdx6500NMNPSbuffPacketExhaust_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 23),
    _Cdx6500NMNPSbuffPacketExhaust_Type()
)
cdx6500NMNPSbuffPacketExhaust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffPacketExhaust.setStatus("optional")
_Cdx6500NMNPSbuffMgtAvail_Type = Integer32
_Cdx6500NMNPSbuffMgtAvail_Object = MibScalar
cdx6500NMNPSbuffMgtAvail = _Cdx6500NMNPSbuffMgtAvail_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 24),
    _Cdx6500NMNPSbuffMgtAvail_Type()
)
cdx6500NMNPSbuffMgtAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffMgtAvail.setStatus("optional")
_Cdx6500NMNPSbuffMgtUse_Type = Integer32
_Cdx6500NMNPSbuffMgtUse_Object = MibScalar
cdx6500NMNPSbuffMgtUse = _Cdx6500NMNPSbuffMgtUse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 25),
    _Cdx6500NMNPSbuffMgtUse_Type()
)
cdx6500NMNPSbuffMgtUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffMgtUse.setStatus("optional")
_Cdx6500NMNPSbuffMgtExhaust_Type = Gauge32
_Cdx6500NMNPSbuffMgtExhaust_Object = MibScalar
cdx6500NMNPSbuffMgtExhaust = _Cdx6500NMNPSbuffMgtExhaust_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 26),
    _Cdx6500NMNPSbuffMgtExhaust_Type()
)
cdx6500NMNPSbuffMgtExhaust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffMgtExhaust.setStatus("optional")
_Cdx6500NMNPSrateCurChar_Type = Integer32
_Cdx6500NMNPSrateCurChar_Object = MibScalar
cdx6500NMNPSrateCurChar = _Cdx6500NMNPSrateCurChar_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 27),
    _Cdx6500NMNPSrateCurChar_Type()
)
cdx6500NMNPSrateCurChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSrateCurChar.setStatus("mandatory")
_Cdx6500NMNPSrateCurPkt_Type = Integer32
_Cdx6500NMNPSrateCurPkt_Object = MibScalar
cdx6500NMNPSrateCurPkt = _Cdx6500NMNPSrateCurPkt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 28),
    _Cdx6500NMNPSrateCurPkt_Type()
)
cdx6500NMNPSrateCurPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSrateCurPkt.setStatus("mandatory")
_Cdx6500NMNPSrateMaxChar_Type = Gauge32
_Cdx6500NMNPSrateMaxChar_Object = MibScalar
cdx6500NMNPSrateMaxChar = _Cdx6500NMNPSrateMaxChar_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 29),
    _Cdx6500NMNPSrateMaxChar_Type()
)
cdx6500NMNPSrateMaxChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSrateMaxChar.setStatus("mandatory")
_Cdx6500NMNPSrateMaxPkt_Type = Gauge32
_Cdx6500NMNPSrateMaxPkt_Object = MibScalar
cdx6500NMNPSrateMaxPkt = _Cdx6500NMNPSrateMaxPkt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 30),
    _Cdx6500NMNPSrateMaxPkt_Type()
)
cdx6500NMNPSrateMaxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSrateMaxPkt.setStatus("mandatory")
_Cdx6500NMNPSmemEprom_Type = Integer32
_Cdx6500NMNPSmemEprom_Object = MibScalar
cdx6500NMNPSmemEprom = _Cdx6500NMNPSmemEprom_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 31),
    _Cdx6500NMNPSmemEprom_Type()
)
cdx6500NMNPSmemEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSmemEprom.setStatus("optional")
_Cdx6500NMNPSmemDram_Type = Integer32
_Cdx6500NMNPSmemDram_Object = MibScalar
cdx6500NMNPSmemDram = _Cdx6500NMNPSmemDram_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 32),
    _Cdx6500NMNPSmemDram_Type()
)
cdx6500NMNPSmemDram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSmemDram.setStatus("optional")
_Cdx6500NMNPSmemFlashCur_Type = Integer32
_Cdx6500NMNPSmemFlashCur_Object = MibScalar
cdx6500NMNPSmemFlashCur = _Cdx6500NMNPSmemFlashCur_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 33),
    _Cdx6500NMNPSmemFlashCur_Type()
)
cdx6500NMNPSmemFlashCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSmemFlashCur.setStatus("optional")
_Cdx6500NMNPSmemFlashAlt_Type = Integer32
_Cdx6500NMNPSmemFlashAlt_Object = MibScalar
cdx6500NMNPSmemFlashAlt = _Cdx6500NMNPSmemFlashAlt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 34),
    _Cdx6500NMNPSmemFlashAlt_Type()
)
cdx6500NMNPSmemFlashAlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSmemFlashAlt.setStatus("optional")
_Cdx6500NMNPScpuUtil_Type = Integer32
_Cdx6500NMNPScpuUtil_Object = MibScalar
cdx6500NMNPScpuUtil = _Cdx6500NMNPScpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 35),
    _Cdx6500NMNPScpuUtil_Type()
)
cdx6500NMNPScpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScpuUtil.setStatus("optional")
_Cdx6500NMNPSDisplayNumImage_Type = DisplayString
_Cdx6500NMNPSDisplayNumImage_Object = MibScalar
cdx6500NMNPSDisplayNumImage = _Cdx6500NMNPSDisplayNumImage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 36),
    _Cdx6500NMNPSDisplayNumImage_Type()
)
cdx6500NMNPSDisplayNumImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSDisplayNumImage.setStatus("optional")


class _Cdx6500NMNPSDisplayLEDstatus_Type(Integer32):
    """Custom type cdx6500NMNPSDisplayLEDstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 2),
          ("newvalOff", 50),
          ("notSupported", 100),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500NMNPSDisplayLEDstatus_Type.__name__ = "Integer32"
_Cdx6500NMNPSDisplayLEDstatus_Object = MibScalar
cdx6500NMNPSDisplayLEDstatus = _Cdx6500NMNPSDisplayLEDstatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 37),
    _Cdx6500NMNPSDisplayLEDstatus_Type()
)
cdx6500NMNPSDisplayLEDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSDisplayLEDstatus.setStatus("optional")


class _Cdx6500NMNPSDisplayLEDdiag_Type(Integer32):
    """Custom type cdx6500NMNPSDisplayLEDdiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 2),
          ("newvalOff", 50),
          ("notSupported", 100),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500NMNPSDisplayLEDdiag_Type.__name__ = "Integer32"
_Cdx6500NMNPSDisplayLEDdiag_Object = MibScalar
cdx6500NMNPSDisplayLEDdiag = _Cdx6500NMNPSDisplayLEDdiag_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 38),
    _Cdx6500NMNPSDisplayLEDdiag_Type()
)
cdx6500NMNPSDisplayLEDdiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSDisplayLEDdiag.setStatus("optional")


class _Cdx6500NMNPSdefaultNode_Type(Integer32):
    """Custom type cdx6500NMNPSdefaultNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("noDefault", 2))
    )


_Cdx6500NMNPSdefaultNode_Type.__name__ = "Integer32"
_Cdx6500NMNPSdefaultNode_Object = MibScalar
cdx6500NMNPSdefaultNode = _Cdx6500NMNPSdefaultNode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 39),
    _Cdx6500NMNPSdefaultNode_Type()
)
cdx6500NMNPSdefaultNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500NMNPSdefaultNode.setStatus("mandatory")
_Cdx6500NMNPSresetStatTable_Object = MibTable
cdx6500NMNPSresetStatTable = _Cdx6500NMNPSresetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 40)
)
if mibBuilder.loadTexts:
    cdx6500NMNPSresetStatTable.setStatus("mandatory")
_Cdx6500NMNPSresetStatEntry_Object = MibTableRow
cdx6500NMNPSresetStatEntry = _Cdx6500NMNPSresetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 40, 1)
)
cdx6500NMNPSresetStatEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500NMNPSresetStatPort"),
)
if mibBuilder.loadTexts:
    cdx6500NMNPSresetStatEntry.setStatus("mandatory")


class _Cdx6500NMNPSresetStatPort_Type(Integer32):
    """Custom type cdx6500NMNPSresetStatPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500NMNPSresetStatPort_Type.__name__ = "Integer32"
_Cdx6500NMNPSresetStatPort_Object = MibTableColumn
cdx6500NMNPSresetStatPort = _Cdx6500NMNPSresetStatPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 40, 1, 1),
    _Cdx6500NMNPSresetStatPort_Type()
)
cdx6500NMNPSresetStatPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500NMNPSresetStatPort.setStatus("mandatory")


class _Cdx6500NMNPSresetStatStatus_Type(Integer32):
    """Custom type cdx6500NMNPSresetStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cdx6500NMNPSresetStatStatus_Type.__name__ = "Integer32"
_Cdx6500NMNPSresetStatStatus_Object = MibTableColumn
cdx6500NMNPSresetStatStatus = _Cdx6500NMNPSresetStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 40, 1, 2),
    _Cdx6500NMNPSresetStatStatus_Type()
)
cdx6500NMNPSresetStatStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSresetStatStatus.setStatus("mandatory")


class _Cdx6500NMNPSresetStatAll_Type(Integer32):
    """Custom type cdx6500NMNPSresetStatAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cdx6500NMNPSresetStatAll_Type.__name__ = "Integer32"
_Cdx6500NMNPSresetStatAll_Object = MibScalar
cdx6500NMNPSresetStatAll = _Cdx6500NMNPSresetStatAll_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 41),
    _Cdx6500NMNPSresetStatAll_Type()
)
cdx6500NMNPSresetStatAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSresetStatAll.setStatus("mandatory")


class _Cdx6500NMNPSstatusPowerSy_Type(DisplayString):
    """Custom type cdx6500NMNPSstatusPowerSy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500NMNPSstatusPowerSy_Type.__name__ = "DisplayString"
_Cdx6500NMNPSstatusPowerSy_Object = MibScalar
cdx6500NMNPSstatusPowerSy = _Cdx6500NMNPSstatusPowerSy_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 42),
    _Cdx6500NMNPSstatusPowerSy_Type()
)
cdx6500NMNPSstatusPowerSy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatusPowerSy.setStatus("mandatory")
_Cdx6500NMNPSstatsTable_Object = MibTable
cdx6500NMNPSstatsTable = _Cdx6500NMNPSstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43)
)
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsTable.setStatus("optional")
_Cdx6500NMNPSstatsEntry_Object = MibTableRow
cdx6500NMNPSstatsEntry = _Cdx6500NMNPSstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1)
)
cdx6500NMNPSstatsEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500NMNPSstatsBoard"),
)
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsEntry.setStatus("optional")
_Cdx6500NMNPSstatsBoard_Type = Integer32
_Cdx6500NMNPSstatsBoard_Object = MibTableColumn
cdx6500NMNPSstatsBoard = _Cdx6500NMNPSstatsBoard_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 1),
    _Cdx6500NMNPSstatsBoard_Type()
)
cdx6500NMNPSstatsBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsBoard.setStatus("optional")
_Cdx6500NMNPSstatsbuffDataAvail_Type = Integer32
_Cdx6500NMNPSstatsbuffDataAvail_Object = MibTableColumn
cdx6500NMNPSstatsbuffDataAvail = _Cdx6500NMNPSstatsbuffDataAvail_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 2),
    _Cdx6500NMNPSstatsbuffDataAvail_Type()
)
cdx6500NMNPSstatsbuffDataAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsbuffDataAvail.setStatus("optional")
_Cdx6500NMNPSstatsbuffDataUse_Type = Integer32
_Cdx6500NMNPSstatsbuffDataUse_Object = MibTableColumn
cdx6500NMNPSstatsbuffDataUse = _Cdx6500NMNPSstatsbuffDataUse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 3),
    _Cdx6500NMNPSstatsbuffDataUse_Type()
)
cdx6500NMNPSstatsbuffDataUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsbuffDataUse.setStatus("optional")
_Cdx6500NMNPSstatsbuffDataGauge_Type = Gauge32
_Cdx6500NMNPSstatsbuffDataGauge_Object = MibTableColumn
cdx6500NMNPSstatsbuffDataGauge = _Cdx6500NMNPSstatsbuffDataGauge_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 4),
    _Cdx6500NMNPSstatsbuffDataGauge_Type()
)
cdx6500NMNPSstatsbuffDataGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsbuffDataGauge.setStatus("optional")
_Cdx6500NMNPSstatsmemEprom_Type = Integer32
_Cdx6500NMNPSstatsmemEprom_Object = MibTableColumn
cdx6500NMNPSstatsmemEprom = _Cdx6500NMNPSstatsmemEprom_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 5),
    _Cdx6500NMNPSstatsmemEprom_Type()
)
cdx6500NMNPSstatsmemEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsmemEprom.setStatus("optional")
_Cdx6500NMNPSstatsmemDram_Type = Integer32
_Cdx6500NMNPSstatsmemDram_Object = MibTableColumn
cdx6500NMNPSstatsmemDram = _Cdx6500NMNPSstatsmemDram_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 6),
    _Cdx6500NMNPSstatsmemDram_Type()
)
cdx6500NMNPSstatsmemDram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsmemDram.setStatus("optional")
_Cdx6500NMNPSstatsmemFlash_Type = Integer32
_Cdx6500NMNPSstatsmemFlash_Object = MibTableColumn
cdx6500NMNPSstatsmemFlash = _Cdx6500NMNPSstatsmemFlash_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 7),
    _Cdx6500NMNPSstatsmemFlash_Type()
)
cdx6500NMNPSstatsmemFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsmemFlash.setStatus("optional")
_Cdx6500NMNPSstatscpuUtil_Type = Integer32
_Cdx6500NMNPSstatscpuUtil_Object = MibTableColumn
cdx6500NMNPSstatscpuUtil = _Cdx6500NMNPSstatscpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 8),
    _Cdx6500NMNPSstatscpuUtil_Type()
)
cdx6500NMNPSstatscpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatscpuUtil.setStatus("optional")
_Cdx6500NMNPSstatsMaxcpuUtil_Type = Integer32
_Cdx6500NMNPSstatsMaxcpuUtil_Object = MibTableColumn
cdx6500NMNPSstatsMaxcpuUtil = _Cdx6500NMNPSstatsMaxcpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 9),
    _Cdx6500NMNPSstatsMaxcpuUtil_Type()
)
cdx6500NMNPSstatsMaxcpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsMaxcpuUtil.setStatus("optional")
_Cdx6500NMNPSstatsMaxcpuUtilTime_Type = DisplayString
_Cdx6500NMNPSstatsMaxcpuUtilTime_Object = MibTableColumn
cdx6500NMNPSstatsMaxcpuUtilTime = _Cdx6500NMNPSstatsMaxcpuUtilTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 43, 1, 10),
    _Cdx6500NMNPSstatsMaxcpuUtilTime_Type()
)
cdx6500NMNPSstatsMaxcpuUtilTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSstatsMaxcpuUtilTime.setStatus("optional")
_Cdx6500NMNPScallsInPlaceMaxTime_Type = DisplayString
_Cdx6500NMNPScallsInPlaceMaxTime_Object = MibScalar
cdx6500NMNPScallsInPlaceMaxTime = _Cdx6500NMNPScallsInPlaceMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 44),
    _Cdx6500NMNPScallsInPlaceMaxTime_Type()
)
cdx6500NMNPScallsInPlaceMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScallsInPlaceMaxTime.setStatus("mandatory")
_Cdx6500NMNPSPVCConnectMaxTime_Type = DisplayString
_Cdx6500NMNPSPVCConnectMaxTime_Object = MibScalar
cdx6500NMNPSPVCConnectMaxTime = _Cdx6500NMNPSPVCConnectMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 45),
    _Cdx6500NMNPSPVCConnectMaxTime_Type()
)
cdx6500NMNPSPVCConnectMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSPVCConnectMaxTime.setStatus("mandatory")
_Cdx6500NMNPScallsPerSecMaxTime_Type = DisplayString
_Cdx6500NMNPScallsPerSecMaxTime_Object = MibScalar
cdx6500NMNPScallsPerSecMaxTime = _Cdx6500NMNPScallsPerSecMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 46),
    _Cdx6500NMNPScallsPerSecMaxTime_Type()
)
cdx6500NMNPScallsPerSecMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPScallsPerSecMaxTime.setStatus("mandatory")
_Cdx6500NMNPSbuffDataGaugeTime_Type = DisplayString
_Cdx6500NMNPSbuffDataGaugeTime_Object = MibScalar
cdx6500NMNPSbuffDataGaugeTime = _Cdx6500NMNPSbuffDataGaugeTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 47),
    _Cdx6500NMNPSbuffDataGaugeTime_Type()
)
cdx6500NMNPSbuffDataGaugeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffDataGaugeTime.setStatus("optional")
_Cdx6500NMNPSbuffPacketGauge_Type = Gauge32
_Cdx6500NMNPSbuffPacketGauge_Object = MibScalar
cdx6500NMNPSbuffPacketGauge = _Cdx6500NMNPSbuffPacketGauge_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 48),
    _Cdx6500NMNPSbuffPacketGauge_Type()
)
cdx6500NMNPSbuffPacketGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffPacketGauge.setStatus("optional")
_Cdx6500NMNPSbuffPacketGaugeTime_Type = DisplayString
_Cdx6500NMNPSbuffPacketGaugeTime_Object = MibScalar
cdx6500NMNPSbuffPacketGaugeTime = _Cdx6500NMNPSbuffPacketGaugeTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 49),
    _Cdx6500NMNPSbuffPacketGaugeTime_Type()
)
cdx6500NMNPSbuffPacketGaugeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffPacketGaugeTime.setStatus("optional")
_Cdx6500NMNPSbuffMgtGauge_Type = Gauge32
_Cdx6500NMNPSbuffMgtGauge_Object = MibScalar
cdx6500NMNPSbuffMgtGauge = _Cdx6500NMNPSbuffMgtGauge_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 50),
    _Cdx6500NMNPSbuffMgtGauge_Type()
)
cdx6500NMNPSbuffMgtGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffMgtGauge.setStatus("optional")
_Cdx6500NMNPSbuffMgtGaugeTime_Type = DisplayString
_Cdx6500NMNPSbuffMgtGaugeTime_Object = MibScalar
cdx6500NMNPSbuffMgtGaugeTime = _Cdx6500NMNPSbuffMgtGaugeTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 51),
    _Cdx6500NMNPSbuffMgtGaugeTime_Type()
)
cdx6500NMNPSbuffMgtGaugeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSbuffMgtGaugeTime.setStatus("optional")
_Cdx6500NMNPSrateMaxCharTime_Type = DisplayString
_Cdx6500NMNPSrateMaxCharTime_Object = MibScalar
cdx6500NMNPSrateMaxCharTime = _Cdx6500NMNPSrateMaxCharTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 52),
    _Cdx6500NMNPSrateMaxCharTime_Type()
)
cdx6500NMNPSrateMaxCharTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSrateMaxCharTime.setStatus("mandatory")
_Cdx6500NMNPSrateMaxPktTime_Type = DisplayString
_Cdx6500NMNPSrateMaxPktTime_Object = MibScalar
cdx6500NMNPSrateMaxPktTime = _Cdx6500NMNPSrateMaxPktTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 53),
    _Cdx6500NMNPSrateMaxPktTime_Type()
)
cdx6500NMNPSrateMaxPktTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSrateMaxPktTime.setStatus("mandatory")
_Cdx6500NMNPSMaxcpuUtil_Type = Integer32
_Cdx6500NMNPSMaxcpuUtil_Object = MibScalar
cdx6500NMNPSMaxcpuUtil = _Cdx6500NMNPSMaxcpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 54),
    _Cdx6500NMNPSMaxcpuUtil_Type()
)
cdx6500NMNPSMaxcpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSMaxcpuUtil.setStatus("optional")
_Cdx6500NMNPSMaxcpuUtilTime_Type = DisplayString
_Cdx6500NMNPSMaxcpuUtilTime_Object = MibScalar
cdx6500NMNPSMaxcpuUtilTime = _Cdx6500NMNPSMaxcpuUtilTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2, 3, 55),
    _Cdx6500NMNPSMaxcpuUtilTime_Type()
)
cdx6500NMNPSMaxcpuUtilTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMNPSMaxcpuUtilTime.setStatus("optional")
_Cdx6500NMDiagnosticsGroup_ObjectIdentity = ObjectIdentity
cdx6500NMDiagnosticsGroup = _Cdx6500NMDiagnosticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3)
)
_Cdx6500NMReportTable_Object = MibTable
cdx6500NMReportTable = _Cdx6500NMReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdx6500NMReportTable.setStatus("mandatory")
_Cdx6500NMReportEntry_Object = MibTableRow
cdx6500NMReportEntry = _Cdx6500NMReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 1, 1)
)
cdx6500NMReportEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500reptIndex"),
)
if mibBuilder.loadTexts:
    cdx6500NMReportEntry.setStatus("mandatory")


class _Cdx6500reptIndex_Type(Integer32):
    """Custom type cdx6500reptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Cdx6500reptIndex_Type.__name__ = "Integer32"
_Cdx6500reptIndex_Object = MibTableColumn
cdx6500reptIndex = _Cdx6500reptIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 1, 1, 1),
    _Cdx6500reptIndex_Type()
)
cdx6500reptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500reptIndex.setStatus("mandatory")


class _Cdx6500reptEvent_Type(DisplayString):
    """Custom type cdx6500reptEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 152),
    )


_Cdx6500reptEvent_Type.__name__ = "DisplayString"
_Cdx6500reptEvent_Object = MibTableColumn
cdx6500reptEvent = _Cdx6500reptEvent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 1, 1, 2),
    _Cdx6500reptEvent_Type()
)
cdx6500reptEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500reptEvent.setStatus("mandatory")


class _Cdx6500NMreptClearLog_Type(Integer32):
    """Custom type cdx6500NMreptClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearLog", 1),
          ("noClearLog", 2))
    )


_Cdx6500NMreptClearLog_Type.__name__ = "Integer32"
_Cdx6500NMreptClearLog_Object = MibScalar
cdx6500NMreptClearLog = _Cdx6500NMreptClearLog_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 2),
    _Cdx6500NMreptClearLog_Type()
)
cdx6500NMreptClearLog.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMreptClearLog.setStatus("mandatory")
_Cdx6500NMV54Loopback_ObjectIdentity = ObjectIdentity
cdx6500NMV54Loopback = _Cdx6500NMV54Loopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3)
)


class _Cdx6500NMV54LocalLoop_Type(Integer32):
    """Custom type cdx6500NMV54LocalLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 2),
          ("startTest", 1))
    )


_Cdx6500NMV54LocalLoop_Type.__name__ = "Integer32"
_Cdx6500NMV54LocalLoop_Object = MibScalar
cdx6500NMV54LocalLoop = _Cdx6500NMV54LocalLoop_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 1),
    _Cdx6500NMV54LocalLoop_Type()
)
cdx6500NMV54LocalLoop.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMV54LocalLoop.setStatus("obsolete")


class _Cdx6500NMV54Loop2_Type(Integer32):
    """Custom type cdx6500NMV54Loop2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 2),
          ("startTest", 1))
    )


_Cdx6500NMV54Loop2_Type.__name__ = "Integer32"
_Cdx6500NMV54Loop2_Object = MibScalar
cdx6500NMV54Loop2 = _Cdx6500NMV54Loop2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 2),
    _Cdx6500NMV54Loop2_Type()
)
cdx6500NMV54Loop2.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMV54Loop2.setStatus("obsolete")


class _Cdx6500NMV54Loop3_Type(Integer32):
    """Custom type cdx6500NMV54Loop3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 2),
          ("startTest", 1))
    )


_Cdx6500NMV54Loop3_Type.__name__ = "Integer32"
_Cdx6500NMV54Loop3_Object = MibScalar
cdx6500NMV54Loop3 = _Cdx6500NMV54Loop3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 3),
    _Cdx6500NMV54Loop3_Type()
)
cdx6500NMV54Loop3.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMV54Loop3.setStatus("obsolete")


class _Cdx6500NMV54turnLoopbackOff_Type(Integer32):
    """Custom type cdx6500NMV54turnLoopbackOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loopbackOff", 1)
    )


_Cdx6500NMV54turnLoopbackOff_Type.__name__ = "Integer32"
_Cdx6500NMV54turnLoopbackOff_Object = MibScalar
cdx6500NMV54turnLoopbackOff = _Cdx6500NMV54turnLoopbackOff_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 4),
    _Cdx6500NMV54turnLoopbackOff_Type()
)
cdx6500NMV54turnLoopbackOff.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMV54turnLoopbackOff.setStatus("obsolete")


class _Cdx6500NMV54LoopbackDuration_Type(Integer32):
    """Custom type cdx6500NMV54LoopbackDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500NMV54LoopbackDuration_Type.__name__ = "Integer32"
_Cdx6500NMV54LoopbackDuration_Object = MibScalar
cdx6500NMV54LoopbackDuration = _Cdx6500NMV54LoopbackDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 5),
    _Cdx6500NMV54LoopbackDuration_Type()
)
cdx6500NMV54LoopbackDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackDuration.setStatus("mandatory")


class _Cdx6500NMV54TestType_Type(Integer32):
    """Custom type cdx6500NMV54TestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v54LocalLoop", 1),
          ("v54Loop2", 2),
          ("v54Loop3", 3))
    )


_Cdx6500NMV54TestType_Type.__name__ = "Integer32"
_Cdx6500NMV54TestType_Object = MibScalar
cdx6500NMV54TestType = _Cdx6500NMV54TestType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 6),
    _Cdx6500NMV54TestType_Type()
)
cdx6500NMV54TestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54TestType.setStatus("obsolete")


class _Cdx6500NMV54LoopbackStatus_Type(Integer32):
    """Custom type cdx6500NMV54LoopbackStatus based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("v54AbortCpuNotRunning", 10),
          ("v54AbortEiaDisc", 9),
          ("v54AbortIsRunning", 7),
          ("v54AbortNotSupported", 11),
          ("v54AbortPortDisabled", 6),
          ("v54AbortPortNull", 8),
          ("v54AbortWrongParams", 12),
          ("v54AbortWrongPort", 13),
          ("v54Clearing", 4),
          ("v54NotRun", 14),
          ("v54Running", 2),
          ("v54Starting", 1),
          ("v54Stopped", 5),
          ("v54Stopping", 3))
    )


_Cdx6500NMV54LoopbackStatus_Type.__name__ = "Integer32"
_Cdx6500NMV54LoopbackStatus_Object = MibScalar
cdx6500NMV54LoopbackStatus = _Cdx6500NMV54LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 7),
    _Cdx6500NMV54LoopbackStatus_Type()
)
cdx6500NMV54LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackStatus.setStatus("mandatory")
_Cdx6500NMV54MessagesSent_Type = Integer32
_Cdx6500NMV54MessagesSent_Object = MibScalar
cdx6500NMV54MessagesSent = _Cdx6500NMV54MessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 9),
    _Cdx6500NMV54MessagesSent_Type()
)
cdx6500NMV54MessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54MessagesSent.setStatus("obsolete")
_Cdx6500NMV54GoodMsgsReceived_Type = Integer32
_Cdx6500NMV54GoodMsgsReceived_Object = MibScalar
cdx6500NMV54GoodMsgsReceived = _Cdx6500NMV54GoodMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 10),
    _Cdx6500NMV54GoodMsgsReceived_Type()
)
cdx6500NMV54GoodMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54GoodMsgsReceived.setStatus("obsolete")
_Cdx6500NMV54BadMsgsReceived_Type = Integer32
_Cdx6500NMV54BadMsgsReceived_Object = MibScalar
cdx6500NMV54BadMsgsReceived = _Cdx6500NMV54BadMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 11),
    _Cdx6500NMV54BadMsgsReceived_Type()
)
cdx6500NMV54BadMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54BadMsgsReceived.setStatus("obsolete")


class _Cdx6500NMV54LastPortTested_Type(Integer32):
    """Custom type cdx6500NMV54LastPortTested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500NMV54LastPortTested_Type.__name__ = "Integer32"
_Cdx6500NMV54LastPortTested_Object = MibScalar
cdx6500NMV54LastPortTested = _Cdx6500NMV54LastPortTested_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 12),
    _Cdx6500NMV54LastPortTested_Type()
)
cdx6500NMV54LastPortTested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54LastPortTested.setStatus("obsolete")


class _Cdx6500NMV54CurrentTestPort_Type(Integer32):
    """Custom type cdx6500NMV54CurrentTestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500NMV54CurrentTestPort_Type.__name__ = "Integer32"
_Cdx6500NMV54CurrentTestPort_Object = MibScalar
cdx6500NMV54CurrentTestPort = _Cdx6500NMV54CurrentTestPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 13),
    _Cdx6500NMV54CurrentTestPort_Type()
)
cdx6500NMV54CurrentTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500NMV54CurrentTestPort.setStatus("obsolete")


class _Cdx6500NMV54LoopbackTest_Type(Integer32):
    """Custom type cdx6500NMV54LoopbackTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTesting", 2),
          ("testing", 1))
    )


_Cdx6500NMV54LoopbackTest_Type.__name__ = "Integer32"
_Cdx6500NMV54LoopbackTest_Object = MibScalar
cdx6500NMV54LoopbackTest = _Cdx6500NMV54LoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 14),
    _Cdx6500NMV54LoopbackTest_Type()
)
cdx6500NMV54LoopbackTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackTest.setStatus("mandatory")


class _Cdx6500NMV54LoopbackTestType_Type(Integer32):
    """Custom type cdx6500NMV54LoopbackTestType based on Integer32"""
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
        *(("dsuInternal", 4),
          ("dsuInternalExternal", 5),
          ("v54LocalLoop", 1),
          ("v54Loop2", 2),
          ("v54Loop3", 3))
    )


_Cdx6500NMV54LoopbackTestType_Type.__name__ = "Integer32"
_Cdx6500NMV54LoopbackTestType_Object = MibScalar
cdx6500NMV54LoopbackTestType = _Cdx6500NMV54LoopbackTestType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 15),
    _Cdx6500NMV54LoopbackTestType_Type()
)
cdx6500NMV54LoopbackTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackTestType.setStatus("mandatory")


class _Cdx6500NMV54LoopbackLastPortTested_Type(Integer32):
    """Custom type cdx6500NMV54LoopbackLastPortTested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_Cdx6500NMV54LoopbackLastPortTested_Type.__name__ = "Integer32"
_Cdx6500NMV54LoopbackLastPortTested_Object = MibScalar
cdx6500NMV54LoopbackLastPortTested = _Cdx6500NMV54LoopbackLastPortTested_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 16),
    _Cdx6500NMV54LoopbackLastPortTested_Type()
)
cdx6500NMV54LoopbackLastPortTested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackLastPortTested.setStatus("mandatory")


class _Cdx6500NMV54LoopbackCurrentTestPort_Type(Integer32):
    """Custom type cdx6500NMV54LoopbackCurrentTestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_Cdx6500NMV54LoopbackCurrentTestPort_Type.__name__ = "Integer32"
_Cdx6500NMV54LoopbackCurrentTestPort_Object = MibScalar
cdx6500NMV54LoopbackCurrentTestPort = _Cdx6500NMV54LoopbackCurrentTestPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 17),
    _Cdx6500NMV54LoopbackCurrentTestPort_Type()
)
cdx6500NMV54LoopbackCurrentTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackCurrentTestPort.setStatus("mandatory")
_Cdx6500NMV54LoopbackMessagesSent_Type = Counter32
_Cdx6500NMV54LoopbackMessagesSent_Object = MibScalar
cdx6500NMV54LoopbackMessagesSent = _Cdx6500NMV54LoopbackMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 18),
    _Cdx6500NMV54LoopbackMessagesSent_Type()
)
cdx6500NMV54LoopbackMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackMessagesSent.setStatus("mandatory")
_Cdx6500NMV54LoopbackGoodMsgsReceived_Type = Counter32
_Cdx6500NMV54LoopbackGoodMsgsReceived_Object = MibScalar
cdx6500NMV54LoopbackGoodMsgsReceived = _Cdx6500NMV54LoopbackGoodMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 19),
    _Cdx6500NMV54LoopbackGoodMsgsReceived_Type()
)
cdx6500NMV54LoopbackGoodMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackGoodMsgsReceived.setStatus("mandatory")
_Cdx6500NMV54LoopbackBadMsgsReceived_Type = Counter32
_Cdx6500NMV54LoopbackBadMsgsReceived_Object = MibScalar
cdx6500NMV54LoopbackBadMsgsReceived = _Cdx6500NMV54LoopbackBadMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3, 3, 20),
    _Cdx6500NMV54LoopbackBadMsgsReceived_Type()
)
cdx6500NMV54LoopbackBadMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NMV54LoopbackBadMsgsReceived.setStatus("mandatory")
_Cdx6500NMControlsGroup_ObjectIdentity = ObjectIdentity
cdx6500NMControlsGroup = _Cdx6500NMControlsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 4)
)


class _Cdx6500NMCBootNode_Type(Integer32):
    """Custom type cdx6500NMCBootNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("bootCold", 0),
          ("bootWarm", 1),
          ("newvalBootCold", 50))
    )


_Cdx6500NMCBootNode_Type.__name__ = "Integer32"
_Cdx6500NMCBootNode_Object = MibScalar
cdx6500NMCBootNode = _Cdx6500NMCBootNode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 4, 1),
    _Cdx6500NMCBootNode_Type()
)
cdx6500NMCBootNode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMCBootNode.setStatus("mandatory")


class _Cdx6500NMCBootTableNodeRec_Type(Integer32):
    """Custom type cdx6500NMCBootTableNodeRec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bootrec", 1)
    )


_Cdx6500NMCBootTableNodeRec_Type.__name__ = "Integer32"
_Cdx6500NMCBootTableNodeRec_Object = MibScalar
cdx6500NMCBootTableNodeRec = _Cdx6500NMCBootTableNodeRec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 4, 2),
    _Cdx6500NMCBootTableNodeRec_Type()
)
cdx6500NMCBootTableNodeRec.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500NMCBootTableNodeRec.setStatus("mandatory")
_Cdx6500NMDLSVGroup_ObjectIdentity = ObjectIdentity
cdx6500NMDLSVGroup = _Cdx6500NMDLSVGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5)
)


class _Cdx6500DLSVDLstate_Type(Integer32):
    """Custom type cdx6500DLSVDLstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16,
              32,
              50,
              64)
        )
    )
    namedValues = NamedValues(
        *(("dlBoot", 64),
          ("dlCall", 2),
          ("dlDone", 32),
          ("dlGss", 8),
          ("dlIdle", 50),
          ("dlLgs", 16),
          ("dlLoad", 4),
          ("dlReq", 3),
          ("dlStart", 1))
    )


_Cdx6500DLSVDLstate_Type.__name__ = "Integer32"
_Cdx6500DLSVDLstate_Object = MibScalar
cdx6500DLSVDLstate = _Cdx6500DLSVDLstate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 1),
    _Cdx6500DLSVDLstate_Type()
)
cdx6500DLSVDLstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVDLstate.setStatus("mandatory")
_Cdx6500DLSVPercentComplete_Type = Integer32
_Cdx6500DLSVPercentComplete_Object = MibScalar
cdx6500DLSVPercentComplete = _Cdx6500DLSVPercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 2),
    _Cdx6500DLSVPercentComplete_Type()
)
cdx6500DLSVPercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVPercentComplete.setStatus("mandatory")
_Cdx6500DLSVTimestamp_Type = DisplayString
_Cdx6500DLSVTimestamp_Object = MibScalar
cdx6500DLSVTimestamp = _Cdx6500DLSVTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 3),
    _Cdx6500DLSVTimestamp_Type()
)
cdx6500DLSVTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVTimestamp.setStatus("mandatory")
_Cdx6500DLSVLastServer_Type = DisplayString
_Cdx6500DLSVLastServer_Object = MibScalar
cdx6500DLSVLastServer = _Cdx6500DLSVLastServer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 4),
    _Cdx6500DLSVLastServer_Type()
)
cdx6500DLSVLastServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVLastServer.setStatus("mandatory")


class _Cdx6500DLSVTransferType_Type(Integer32):
    """Custom type cdx6500DLSVTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flashToflash", 3),
          ("idle", 1),
          ("ramToram", 2))
    )


_Cdx6500DLSVTransferType_Type.__name__ = "Integer32"
_Cdx6500DLSVTransferType_Object = MibScalar
cdx6500DLSVTransferType = _Cdx6500DLSVTransferType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 5),
    _Cdx6500DLSVTransferType_Type()
)
cdx6500DLSVTransferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVTransferType.setStatus("mandatory")
_Cdx6500DLSVInitiateTransfer_Type = Integer32
_Cdx6500DLSVInitiateTransfer_Object = MibScalar
cdx6500DLSVInitiateTransfer = _Cdx6500DLSVInitiateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 6),
    _Cdx6500DLSVInitiateTransfer_Type()
)
cdx6500DLSVInitiateTransfer.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500DLSVInitiateTransfer.setStatus("mandatory")


class _Cdx6500DLSVAgntSegmentSize_Type(Integer32):
    """Custom type cdx6500DLSVAgntSegmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalSegmentSizeDisable", 50),
          ("segmentSize1024", 10),
          ("segmentSize128", 7),
          ("segmentSize16", 4),
          ("segmentSize256", 8),
          ("segmentSize32", 5),
          ("segmentSize512", 9),
          ("segmentSize64", 6),
          ("segmentSizeDisable", 0))
    )


_Cdx6500DLSVAgntSegmentSize_Type.__name__ = "Integer32"
_Cdx6500DLSVAgntSegmentSize_Object = MibScalar
cdx6500DLSVAgntSegmentSize = _Cdx6500DLSVAgntSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 7),
    _Cdx6500DLSVAgntSegmentSize_Type()
)
cdx6500DLSVAgntSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVAgntSegmentSize.setStatus("mandatory")


class _Cdx6500DLSVAgntnmServAddress_Type(DisplayString):
    """Custom type cdx6500DLSVAgntnmServAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500DLSVAgntnmServAddress_Type.__name__ = "DisplayString"
_Cdx6500DLSVAgntnmServAddress_Object = MibScalar
cdx6500DLSVAgntnmServAddress = _Cdx6500DLSVAgntnmServAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 8),
    _Cdx6500DLSVAgntnmServAddress_Type()
)
cdx6500DLSVAgntnmServAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVAgntnmServAddress.setStatus("mandatory")
_Cdx6500DLSVagntloaderSubaddress_Type = Integer32
_Cdx6500DLSVagntloaderSubaddress_Object = MibScalar
cdx6500DLSVagntloaderSubaddress = _Cdx6500DLSVagntloaderSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 9),
    _Cdx6500DLSVagntloaderSubaddress_Type()
)
cdx6500DLSVagntloaderSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVagntloaderSubaddress.setStatus("mandatory")
_Cdx6500DLSVagntdlServSubaddress_Type = Integer32
_Cdx6500DLSVagntdlServSubaddress_Object = MibScalar
cdx6500DLSVagntdlServSubaddress = _Cdx6500DLSVagntdlServSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5, 10),
    _Cdx6500DLSVagntdlServSubaddress_Type()
)
cdx6500DLSVagntdlServSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DLSVagntdlServSubaddress.setStatus("mandatory")
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500CreatePortAndStationTable_Object = MibTable
cdx6500CreatePortAndStationTable = _Cdx6500CreatePortAndStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    cdx6500CreatePortAndStationTable.setStatus("mandatory")
_Cdx6500CreatePortAndStationEntry_Object = MibTableRow
cdx6500CreatePortAndStationEntry = _Cdx6500CreatePortAndStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 9, 1)
)
cdx6500CreatePortAndStationEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500PortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500CreatePortAndStationEntry.setStatus("mandatory")


class _Cdx6500PortNumber_Type(Integer32):
    """Custom type cdx6500PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PortNumber_Type.__name__ = "Integer32"
_Cdx6500PortNumber_Object = MibTableColumn
cdx6500PortNumber = _Cdx6500PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 9, 1, 1),
    _Cdx6500PortNumber_Type()
)
cdx6500PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PortNumber.setStatus("mandatory")


class _Cdx6500CreatePortType_Type(Integer32):
    """Custom type cdx6500CreatePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              9,
              15,
              17,
              18,
              28,
              29,
              33)
        )
    )
    namedValues = NamedValues(
        *(("eth", 29),
          ("fra", 33),
          ("fri", 17),
          ("mx25", 9),
          ("pad", 2),
          ("sdlc", 15),
          ("tr", 28),
          ("x25", 3),
          ("xdlc", 18))
    )


_Cdx6500CreatePortType_Type.__name__ = "Integer32"
_Cdx6500CreatePortType_Object = MibTableColumn
cdx6500CreatePortType = _Cdx6500CreatePortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 9, 1, 2),
    _Cdx6500CreatePortType_Type()
)
cdx6500CreatePortType.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500CreatePortType.setStatus("mandatory")
_Cdx6500CreateStation_Type = Integer32
_Cdx6500CreateStation_Object = MibTableColumn
cdx6500CreateStation = _Cdx6500CreateStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 9, 1, 3),
    _Cdx6500CreateStation_Type()
)
cdx6500CreateStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500CreateStation.setStatus("mandatory")
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500GCTRouteSelectionTable_Object = MibTable
cdx6500GCTRouteSelectionTable = _Cdx6500GCTRouteSelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cdx6500GCTRouteSelectionTable.setStatus("mandatory")
_Cdx6500GCTRouteSelectionEntry_Object = MibTableRow
cdx6500GCTRouteSelectionEntry = _Cdx6500GCTRouteSelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1)
)
cdx6500GCTRouteSelectionEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500RoutSVCEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500GCTRouteSelectionEntry.setStatus("mandatory")


class _Cdx6500RoutSVCEntryNumber_Type(Integer32):
    """Custom type cdx6500RoutSVCEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdx6500RoutSVCEntryNumber_Type.__name__ = "Integer32"
_Cdx6500RoutSVCEntryNumber_Object = MibTableColumn
cdx6500RoutSVCEntryNumber = _Cdx6500RoutSVCEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 1),
    _Cdx6500RoutSVCEntryNumber_Type()
)
cdx6500RoutSVCEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RoutSVCEntryNumber.setStatus("mandatory")
_Cdx6500RoutSVCAddress_Type = Integer32
_Cdx6500RoutSVCAddress_Object = MibTableColumn
cdx6500RoutSVCAddress = _Cdx6500RoutSVCAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 2),
    _Cdx6500RoutSVCAddress_Type()
)
cdx6500RoutSVCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500RoutSVCAddress.setStatus("deprecated")
_Cdx6500RoutSVCDestination1_Type = DisplayString
_Cdx6500RoutSVCDestination1_Object = MibTableColumn
cdx6500RoutSVCDestination1 = _Cdx6500RoutSVCDestination1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 3),
    _Cdx6500RoutSVCDestination1_Type()
)
cdx6500RoutSVCDestination1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination1.setStatus("mandatory")


class _Cdx6500RoutSVCPriority1_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority1_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority1_Object = MibTableColumn
cdx6500RoutSVCPriority1 = _Cdx6500RoutSVCPriority1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 4),
    _Cdx6500RoutSVCPriority1_Type()
)
cdx6500RoutSVCPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority1.setStatus("mandatory")
_Cdx6500RoutSVCDestination2_Type = DisplayString
_Cdx6500RoutSVCDestination2_Object = MibTableColumn
cdx6500RoutSVCDestination2 = _Cdx6500RoutSVCDestination2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 5),
    _Cdx6500RoutSVCDestination2_Type()
)
cdx6500RoutSVCDestination2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination2.setStatus("mandatory")


class _Cdx6500RoutSVCPriority2_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority2_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority2_Object = MibTableColumn
cdx6500RoutSVCPriority2 = _Cdx6500RoutSVCPriority2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 6),
    _Cdx6500RoutSVCPriority2_Type()
)
cdx6500RoutSVCPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority2.setStatus("mandatory")
_Cdx6500RoutSVCDestination3_Type = DisplayString
_Cdx6500RoutSVCDestination3_Object = MibTableColumn
cdx6500RoutSVCDestination3 = _Cdx6500RoutSVCDestination3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 7),
    _Cdx6500RoutSVCDestination3_Type()
)
cdx6500RoutSVCDestination3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination3.setStatus("mandatory")


class _Cdx6500RoutSVCPriority3_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority3_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority3_Object = MibTableColumn
cdx6500RoutSVCPriority3 = _Cdx6500RoutSVCPriority3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 8),
    _Cdx6500RoutSVCPriority3_Type()
)
cdx6500RoutSVCPriority3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority3.setStatus("mandatory")
_Cdx6500RoutSVCDestination4_Type = DisplayString
_Cdx6500RoutSVCDestination4_Object = MibTableColumn
cdx6500RoutSVCDestination4 = _Cdx6500RoutSVCDestination4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 9),
    _Cdx6500RoutSVCDestination4_Type()
)
cdx6500RoutSVCDestination4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination4.setStatus("mandatory")


class _Cdx6500RoutSVCPriority4_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority4_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority4_Object = MibTableColumn
cdx6500RoutSVCPriority4 = _Cdx6500RoutSVCPriority4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 10),
    _Cdx6500RoutSVCPriority4_Type()
)
cdx6500RoutSVCPriority4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority4.setStatus("mandatory")
_Cdx6500RoutSVCDestination5_Type = DisplayString
_Cdx6500RoutSVCDestination5_Object = MibTableColumn
cdx6500RoutSVCDestination5 = _Cdx6500RoutSVCDestination5_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 11),
    _Cdx6500RoutSVCDestination5_Type()
)
cdx6500RoutSVCDestination5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination5.setStatus("mandatory")


class _Cdx6500RoutSVCPriority5_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority5_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority5_Object = MibTableColumn
cdx6500RoutSVCPriority5 = _Cdx6500RoutSVCPriority5_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 12),
    _Cdx6500RoutSVCPriority5_Type()
)
cdx6500RoutSVCPriority5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority5.setStatus("mandatory")
_Cdx6500RoutSVCDestination6_Type = DisplayString
_Cdx6500RoutSVCDestination6_Object = MibTableColumn
cdx6500RoutSVCDestination6 = _Cdx6500RoutSVCDestination6_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 13),
    _Cdx6500RoutSVCDestination6_Type()
)
cdx6500RoutSVCDestination6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination6.setStatus("mandatory")


class _Cdx6500RoutSVCPriority6_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority6_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority6_Object = MibTableColumn
cdx6500RoutSVCPriority6 = _Cdx6500RoutSVCPriority6_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 14),
    _Cdx6500RoutSVCPriority6_Type()
)
cdx6500RoutSVCPriority6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority6.setStatus("mandatory")
_Cdx6500RoutSVCDestination7_Type = DisplayString
_Cdx6500RoutSVCDestination7_Object = MibTableColumn
cdx6500RoutSVCDestination7 = _Cdx6500RoutSVCDestination7_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 15),
    _Cdx6500RoutSVCDestination7_Type()
)
cdx6500RoutSVCDestination7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination7.setStatus("mandatory")


class _Cdx6500RoutSVCPriority7_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority7_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority7_Object = MibTableColumn
cdx6500RoutSVCPriority7 = _Cdx6500RoutSVCPriority7_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 16),
    _Cdx6500RoutSVCPriority7_Type()
)
cdx6500RoutSVCPriority7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority7.setStatus("mandatory")
_Cdx6500RoutSVCDestination8_Type = DisplayString
_Cdx6500RoutSVCDestination8_Object = MibTableColumn
cdx6500RoutSVCDestination8 = _Cdx6500RoutSVCDestination8_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 17),
    _Cdx6500RoutSVCDestination8_Type()
)
cdx6500RoutSVCDestination8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCDestination8.setStatus("mandatory")


class _Cdx6500RoutSVCPriority8_Type(Integer32):
    """Custom type cdx6500RoutSVCPriority8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500RoutSVCPriority8_Type.__name__ = "Integer32"
_Cdx6500RoutSVCPriority8_Object = MibTableColumn
cdx6500RoutSVCPriority8 = _Cdx6500RoutSVCPriority8_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 18),
    _Cdx6500RoutSVCPriority8_Type()
)
cdx6500RoutSVCPriority8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCPriority8.setStatus("mandatory")
_Cdx6500RoutSVCAddress1_Type = DisplayString
_Cdx6500RoutSVCAddress1_Object = MibTableColumn
cdx6500RoutSVCAddress1 = _Cdx6500RoutSVCAddress1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 1, 1, 19),
    _Cdx6500RoutSVCAddress1_Type()
)
cdx6500RoutSVCAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500RoutSVCAddress1.setStatus("mandatory")
_Cdx6500GCTPVCSetupTable_Object = MibTable
cdx6500GCTPVCSetupTable = _Cdx6500GCTPVCSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cdx6500GCTPVCSetupTable.setStatus("mandatory")
_Cdx6500GCTPVCSetupEntry_Object = MibTableRow
cdx6500GCTPVCSetupEntry = _Cdx6500GCTPVCSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 5, 1)
)
cdx6500GCTPVCSetupEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500PVCSetupEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500GCTPVCSetupEntry.setStatus("mandatory")


class _Cdx6500PVCSetupEntryNumber_Type(Integer32):
    """Custom type cdx6500PVCSetupEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PVCSetupEntryNumber_Type.__name__ = "Integer32"
_Cdx6500PVCSetupEntryNumber_Object = MibTableColumn
cdx6500PVCSetupEntryNumber = _Cdx6500PVCSetupEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 5, 1, 1),
    _Cdx6500PVCSetupEntryNumber_Type()
)
cdx6500PVCSetupEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PVCSetupEntryNumber.setStatus("mandatory")
_Cdx6500PVCSetupSource_Type = DisplayString
_Cdx6500PVCSetupSource_Object = MibTableColumn
cdx6500PVCSetupSource = _Cdx6500PVCSetupSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 5, 1, 2),
    _Cdx6500PVCSetupSource_Type()
)
cdx6500PVCSetupSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PVCSetupSource.setStatus("mandatory")
_Cdx6500PVCSetupDestination_Type = DisplayString
_Cdx6500PVCSetupDestination_Object = MibTableColumn
cdx6500PVCSetupDestination = _Cdx6500PVCSetupDestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 5, 1, 3),
    _Cdx6500PVCSetupDestination_Type()
)
cdx6500PVCSetupDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PVCSetupDestination.setStatus("mandatory")
_Cdx6500CfgMnemonicTable_Object = MibTable
cdx6500CfgMnemonicTable = _Cdx6500CfgMnemonicTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cdx6500CfgMnemonicTable.setStatus("mandatory")
_Cdx6500CfgMnemonicEntry_Object = MibTableRow
cdx6500CfgMnemonicEntry = _Cdx6500CfgMnemonicEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 6, 1)
)
cdx6500CfgMnemonicEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500mnemEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500CfgMnemonicEntry.setStatus("mandatory")


class _Cdx6500mnemEntryNum_Type(Integer32):
    """Custom type cdx6500mnemEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500mnemEntryNum_Type.__name__ = "Integer32"
_Cdx6500mnemEntryNum_Object = MibTableColumn
cdx6500mnemEntryNum = _Cdx6500mnemEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 6, 1, 1),
    _Cdx6500mnemEntryNum_Type()
)
cdx6500mnemEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mnemEntryNum.setStatus("mandatory")


class _Cdx6500mnemName_Type(DisplayString):
    """Custom type cdx6500mnemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500mnemName_Type.__name__ = "DisplayString"
_Cdx6500mnemName_Object = MibTableColumn
cdx6500mnemName = _Cdx6500mnemName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 6, 1, 2),
    _Cdx6500mnemName_Type()
)
cdx6500mnemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mnemName.setStatus("mandatory")


class _Cdx6500mnemx28Cmd_Type(DisplayString):
    """Custom type cdx6500mnemx28Cmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cdx6500mnemx28Cmd_Type.__name__ = "DisplayString"
_Cdx6500mnemx28Cmd_Object = MibTableColumn
cdx6500mnemx28Cmd = _Cdx6500mnemx28Cmd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 6, 1, 3),
    _Cdx6500mnemx28Cmd_Type()
)
cdx6500mnemx28Cmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500mnemx28Cmd.setStatus("mandatory")
_Cdx6500GCTNUIPasswordTable_Object = MibTable
cdx6500GCTNUIPasswordTable = _Cdx6500GCTNUIPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    cdx6500GCTNUIPasswordTable.setStatus("mandatory")
_Cdx6500GCTNUIPasswordEntry_Object = MibTableRow
cdx6500GCTNUIPasswordEntry = _Cdx6500GCTNUIPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 7, 1)
)
cdx6500GCTNUIPasswordEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500NUITEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500GCTNUIPasswordEntry.setStatus("mandatory")


class _Cdx6500NUITEntryNumber_Type(Integer32):
    """Custom type cdx6500NUITEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_Cdx6500NUITEntryNumber_Type.__name__ = "Integer32"
_Cdx6500NUITEntryNumber_Object = MibTableColumn
cdx6500NUITEntryNumber = _Cdx6500NUITEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 7, 1, 1),
    _Cdx6500NUITEntryNumber_Type()
)
cdx6500NUITEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NUITEntryNumber.setStatus("mandatory")


class _Cdx6500NUITAcctName_Type(DisplayString):
    """Custom type cdx6500NUITAcctName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500NUITAcctName_Type.__name__ = "DisplayString"
_Cdx6500NUITAcctName_Object = MibTableColumn
cdx6500NUITAcctName = _Cdx6500NUITAcctName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 7, 1, 2),
    _Cdx6500NUITAcctName_Type()
)
cdx6500NUITAcctName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NUITAcctName.setStatus("mandatory")


class _Cdx6500NUITPasswd_Type(DisplayString):
    """Custom type cdx6500NUITPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500NUITPasswd_Type.__name__ = "DisplayString"
_Cdx6500NUITPasswd_Object = MibTableColumn
cdx6500NUITPasswd = _Cdx6500NUITPasswd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 7, 1, 3),
    _Cdx6500NUITPasswd_Type()
)
cdx6500NUITPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NUITPasswd.setStatus("mandatory")


class _Cdx6500NUITPADPromptNum_Type(Integer32):
    """Custom type cdx6500NUITPADPromptNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500NUITPADPromptNum_Type.__name__ = "Integer32"
_Cdx6500NUITPADPromptNum_Object = MibTableColumn
cdx6500NUITPADPromptNum = _Cdx6500NUITPADPromptNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 7, 1, 4),
    _Cdx6500NUITPADPromptNum_Type()
)
cdx6500NUITPADPromptNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NUITPADPromptNum.setStatus("mandatory")
_Cdx6500GCTSoftwareKeyTable_Object = MibTable
cdx6500GCTSoftwareKeyTable = _Cdx6500GCTSoftwareKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    cdx6500GCTSoftwareKeyTable.setStatus("mandatory")
_Cdx6500GCTSoftwareKeyEntry_Object = MibTableRow
cdx6500GCTSoftwareKeyEntry = _Cdx6500GCTSoftwareKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 12, 1)
)
cdx6500GCTSoftwareKeyEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500CSISSoftKeyEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500GCTSoftwareKeyEntry.setStatus("mandatory")


class _Cdx6500CSISSoftKeyEntryNumber_Type(Integer32):
    """Custom type cdx6500CSISSoftKeyEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Cdx6500CSISSoftKeyEntryNumber_Type.__name__ = "Integer32"
_Cdx6500CSISSoftKeyEntryNumber_Object = MibTableColumn
cdx6500CSISSoftKeyEntryNumber = _Cdx6500CSISSoftKeyEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 12, 1, 1),
    _Cdx6500CSISSoftKeyEntryNumber_Type()
)
cdx6500CSISSoftKeyEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISSoftKeyEntryNumber.setStatus("mandatory")


class _Cdx6500CSISSoftKeyValue_Type(DisplayString):
    """Custom type cdx6500CSISSoftKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500CSISSoftKeyValue_Type.__name__ = "DisplayString"
_Cdx6500CSISSoftKeyValue_Object = MibTableColumn
cdx6500CSISSoftKeyValue = _Cdx6500CSISSoftKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 12, 1, 2),
    _Cdx6500CSISSoftKeyValue_Type()
)
cdx6500CSISSoftKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISSoftKeyValue.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTallPortsTable_Object = MibTable
cdx6500PPSTallPortsTable = _Cdx6500PPSTallPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cdx6500PPSTallPortsTable.setStatus("mandatory")
_Cdx6500PPSTallPortsEntry_Object = MibTableRow
cdx6500PPSTallPortsEntry = _Cdx6500PPSTallPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1)
)
cdx6500PPSTallPortsEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500allportsPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTallPortsEntry.setStatus("mandatory")


class _Cdx6500allportsPortNum_Type(Integer32):
    """Custom type cdx6500allportsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500allportsPortNum_Type.__name__ = "Integer32"
_Cdx6500allportsPortNum_Object = MibTableColumn
cdx6500allportsPortNum = _Cdx6500allportsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 1),
    _Cdx6500allportsPortNum_Type()
)
cdx6500allportsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPortNum.setStatus("mandatory")


class _Cdx6500allportsPortType_Type(Integer32):
    """Custom type cdx6500allportsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              9,
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              48,
              50,
              51,
              52,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("alc", 31),
          ("atm", 56),
          ("atpad", 35),
          ("bri", 40),
          ("bsc2780", 11),
          ("bsc3270", 12),
          ("bstd", 19),
          ("e1", 45),
          ("eth", 29),
          ("fra", 33),
          ("fri", 17),
          ("gsc", 51),
          ("hub", 39),
          ("ibm2260", 23),
          ("mux", 4),
          ("mx25", 9),
          ("n270", 26),
          ("ncrbsc", 16),
          ("null", 1),
          ("pad", 2),
          ("pos", 14),
          ("ppp", 42),
          ("ptype3201", 50),
          ("rs366", 20),
          ("sdlc", 15),
          ("sl", 32),
          ("slip", 37),
          ("spp", 52),
          ("t1", 44),
          ("t1e1", 54),
          ("t3e3", 55),
          ("t3pos", 34),
          ("tbop", 25),
          ("tcop", 27),
          ("tdlc", 48),
          ("tnpp", 36),
          ("tr", 28),
          ("vap", 24),
          ("vip", 13),
          ("voice", 43),
          ("x25", 3),
          ("x32pcm", 41),
          ("xdlc", 18))
    )


_Cdx6500allportsPortType_Type.__name__ = "Integer32"
_Cdx6500allportsPortType_Object = MibTableColumn
cdx6500allportsPortType = _Cdx6500allportsPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 2),
    _Cdx6500allportsPortType_Type()
)
cdx6500allportsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPortType.setStatus("mandatory")


class _Cdx6500allportsPortStatus_Type(Integer32):
    """Custom type cdx6500allportsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500allportsPortStatus_Type.__name__ = "Integer32"
_Cdx6500allportsPortStatus_Object = MibTableColumn
cdx6500allportsPortStatus = _Cdx6500allportsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 3),
    _Cdx6500allportsPortStatus_Type()
)
cdx6500allportsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPortStatus.setStatus("mandatory")


class _Cdx6500allportsPortState_Type(DisplayString):
    """Custom type cdx6500allportsPortState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_Cdx6500allportsPortState_Type.__name__ = "DisplayString"
_Cdx6500allportsPortState_Object = MibTableColumn
cdx6500allportsPortState = _Cdx6500allportsPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 4),
    _Cdx6500allportsPortState_Type()
)
cdx6500allportsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPortState.setStatus("mandatory")
_Cdx6500allportsPortSpeed_Type = Integer32
_Cdx6500allportsPortSpeed_Object = MibTableColumn
cdx6500allportsPortSpeed = _Cdx6500allportsPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 5),
    _Cdx6500allportsPortSpeed_Type()
)
cdx6500allportsPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPortSpeed.setStatus("mandatory")
_Cdx6500allportsUtilizationIn_Type = Integer32
_Cdx6500allportsUtilizationIn_Object = MibTableColumn
cdx6500allportsUtilizationIn = _Cdx6500allportsUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 6),
    _Cdx6500allportsUtilizationIn_Type()
)
cdx6500allportsUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsUtilizationIn.setStatus("mandatory")
_Cdx6500allportsUtilizationOut_Type = Integer32
_Cdx6500allportsUtilizationOut_Object = MibTableColumn
cdx6500allportsUtilizationOut = _Cdx6500allportsUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 7),
    _Cdx6500allportsUtilizationOut_Type()
)
cdx6500allportsUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsUtilizationOut.setStatus("mandatory")
_Cdx6500allportsCharInTot_Type = Counter32
_Cdx6500allportsCharInTot_Object = MibTableColumn
cdx6500allportsCharInTot = _Cdx6500allportsCharInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 8),
    _Cdx6500allportsCharInTot_Type()
)
cdx6500allportsCharInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsCharInTot.setStatus("mandatory")
_Cdx6500allportsCharOutTot_Type = Counter32
_Cdx6500allportsCharOutTot_Object = MibTableColumn
cdx6500allportsCharOutTot = _Cdx6500allportsCharOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 9),
    _Cdx6500allportsCharOutTot_Type()
)
cdx6500allportsCharOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsCharOutTot.setStatus("mandatory")
_Cdx6500allportsPktInTot_Type = Counter32
_Cdx6500allportsPktInTot_Object = MibTableColumn
cdx6500allportsPktInTot = _Cdx6500allportsPktInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 10),
    _Cdx6500allportsPktInTot_Type()
)
cdx6500allportsPktInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPktInTot.setStatus("mandatory")
_Cdx6500allportsPktOutTot_Type = Counter32
_Cdx6500allportsPktOutTot_Object = MibTableColumn
cdx6500allportsPktOutTot = _Cdx6500allportsPktOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 11),
    _Cdx6500allportsPktOutTot_Type()
)
cdx6500allportsPktOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPktOutTot.setStatus("mandatory")
_Cdx6500allportsFrameInTot_Type = Counter32
_Cdx6500allportsFrameInTot_Object = MibTableColumn
cdx6500allportsFrameInTot = _Cdx6500allportsFrameInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 12),
    _Cdx6500allportsFrameInTot_Type()
)
cdx6500allportsFrameInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsFrameInTot.setStatus("mandatory")
_Cdx6500allportsFrameOutTot_Type = Counter32
_Cdx6500allportsFrameOutTot_Object = MibTableColumn
cdx6500allportsFrameOutTot = _Cdx6500allportsFrameOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 13),
    _Cdx6500allportsFrameOutTot_Type()
)
cdx6500allportsFrameOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsFrameOutTot.setStatus("mandatory")
_Cdx6500allportsPktsQueued_Type = Integer32
_Cdx6500allportsPktsQueued_Object = MibTableColumn
cdx6500allportsPktsQueued = _Cdx6500allportsPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 14),
    _Cdx6500allportsPktsQueued_Type()
)
cdx6500allportsPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPktsQueued.setStatus("mandatory")
_Cdx6500allportsCharsInPerSec_Type = Integer32
_Cdx6500allportsCharsInPerSec_Object = MibTableColumn
cdx6500allportsCharsInPerSec = _Cdx6500allportsCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 15),
    _Cdx6500allportsCharsInPerSec_Type()
)
cdx6500allportsCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsCharsInPerSec.setStatus("mandatory")
_Cdx6500allportsCharsOutPerSec_Type = Integer32
_Cdx6500allportsCharsOutPerSec_Object = MibTableColumn
cdx6500allportsCharsOutPerSec = _Cdx6500allportsCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 16),
    _Cdx6500allportsCharsOutPerSec_Type()
)
cdx6500allportsCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsCharsOutPerSec.setStatus("mandatory")
_Cdx6500allportsPktsInPerSec_Type = Integer32
_Cdx6500allportsPktsInPerSec_Object = MibTableColumn
cdx6500allportsPktsInPerSec = _Cdx6500allportsPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 17),
    _Cdx6500allportsPktsInPerSec_Type()
)
cdx6500allportsPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPktsInPerSec.setStatus("mandatory")
_Cdx6500allportsPktsOutPerSec_Type = Integer32
_Cdx6500allportsPktsOutPerSec_Object = MibTableColumn
cdx6500allportsPktsOutPerSec = _Cdx6500allportsPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 18),
    _Cdx6500allportsPktsOutPerSec_Type()
)
cdx6500allportsPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsPktsOutPerSec.setStatus("mandatory")
_Cdx6500allportsFramesInPerSec_Type = Integer32
_Cdx6500allportsFramesInPerSec_Object = MibTableColumn
cdx6500allportsFramesInPerSec = _Cdx6500allportsFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 19),
    _Cdx6500allportsFramesInPerSec_Type()
)
cdx6500allportsFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsFramesInPerSec.setStatus("mandatory")
_Cdx6500allportsFramesOutPerSec_Type = Integer32
_Cdx6500allportsFramesOutPerSec_Object = MibTableColumn
cdx6500allportsFramesOutPerSec = _Cdx6500allportsFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 20),
    _Cdx6500allportsFramesOutPerSec_Type()
)
cdx6500allportsFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsFramesOutPerSec.setStatus("mandatory")
_Cdx6500allportsOverrunErrors_Type = Counter16
_Cdx6500allportsOverrunErrors_Object = MibTableColumn
cdx6500allportsOverrunErrors = _Cdx6500allportsOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 21),
    _Cdx6500allportsOverrunErrors_Type()
)
cdx6500allportsOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsOverrunErrors.setStatus("mandatory")
_Cdx6500allportsUnderrunErrors_Type = Counter16
_Cdx6500allportsUnderrunErrors_Object = MibTableColumn
cdx6500allportsUnderrunErrors = _Cdx6500allportsUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 22),
    _Cdx6500allportsUnderrunErrors_Type()
)
cdx6500allportsUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsUnderrunErrors.setStatus("mandatory")
_Cdx6500allportsCRCErrors_Type = Counter16
_Cdx6500allportsCRCErrors_Object = MibTableColumn
cdx6500allportsCRCErrors = _Cdx6500allportsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 23),
    _Cdx6500allportsCRCErrors_Type()
)
cdx6500allportsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsCRCErrors.setStatus("mandatory")
_Cdx6500allportsParityErrors_Type = Counter16
_Cdx6500allportsParityErrors_Object = MibTableColumn
cdx6500allportsParityErrors = _Cdx6500allportsParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 24),
    _Cdx6500allportsParityErrors_Type()
)
cdx6500allportsParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsParityErrors.setStatus("mandatory")
_Cdx6500allportsFramingErrors_Type = Counter16
_Cdx6500allportsFramingErrors_Object = MibTableColumn
cdx6500allportsFramingErrors = _Cdx6500allportsFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 25),
    _Cdx6500allportsFramingErrors_Type()
)
cdx6500allportsFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allportsFramingErrors.setStatus("mandatory")


class _Cdx6500allportsBootPort_Type(Integer32):
    """Custom type cdx6500allportsBootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bootPort", 1)
    )


_Cdx6500allportsBootPort_Type.__name__ = "Integer32"
_Cdx6500allportsBootPort_Object = MibTableColumn
cdx6500allportsBootPort = _Cdx6500allportsBootPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 26),
    _Cdx6500allportsBootPort_Type()
)
cdx6500allportsBootPort.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500allportsBootPort.setStatus("mandatory")


class _Cdx6500allportsPortControlStatus_Type(Integer32):
    """Custom type cdx6500allportsPortControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busyout", 3),
          ("disable", 2),
          ("enable", 1))
    )


_Cdx6500allportsPortControlStatus_Type.__name__ = "Integer32"
_Cdx6500allportsPortControlStatus_Object = MibTableColumn
cdx6500allportsPortControlStatus = _Cdx6500allportsPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 18, 1, 27),
    _Cdx6500allportsPortControlStatus_Type()
)
cdx6500allportsPortControlStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500allportsPortControlStatus.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTallStationsTable_Object = MibTable
cdx6500SPSTallStationsTable = _Cdx6500SPSTallStationsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cdx6500SPSTallStationsTable.setStatus("mandatory")
_Cdx6500SPSTallStationsEntry_Object = MibTableRow
cdx6500SPSTallStationsEntry = _Cdx6500SPSTallStationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1)
)
cdx6500SPSTallStationsEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500allstationsPortNum"),
    (0, "CDX-6500-COMMON-MIB", "cdx6500allstationsStnNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTallStationsEntry.setStatus("mandatory")


class _Cdx6500allstationsPortNum_Type(Integer32):
    """Custom type cdx6500allstationsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500allstationsPortNum_Type.__name__ = "Integer32"
_Cdx6500allstationsPortNum_Object = MibTableColumn
cdx6500allstationsPortNum = _Cdx6500allstationsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 1),
    _Cdx6500allstationsPortNum_Type()
)
cdx6500allstationsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsPortNum.setStatus("mandatory")
_Cdx6500allstationsStnNum_Type = Integer32
_Cdx6500allstationsStnNum_Object = MibTableColumn
cdx6500allstationsStnNum = _Cdx6500allstationsStnNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 2),
    _Cdx6500allstationsStnNum_Type()
)
cdx6500allstationsStnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsStnNum.setStatus("mandatory")


class _Cdx6500allstationsStnType_Type(DisplayString):
    """Custom type cdx6500allstationsStnType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Cdx6500allstationsStnType_Type.__name__ = "DisplayString"
_Cdx6500allstationsStnType_Object = MibTableColumn
cdx6500allstationsStnType = _Cdx6500allstationsStnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 3),
    _Cdx6500allstationsStnType_Type()
)
cdx6500allstationsStnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsStnType.setStatus("mandatory")


class _Cdx6500allstationsStnStatus_Type(Integer32):
    """Custom type cdx6500allstationsStnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500allstationsStnStatus_Type.__name__ = "Integer32"
_Cdx6500allstationsStnStatus_Object = MibTableColumn
cdx6500allstationsStnStatus = _Cdx6500allstationsStnStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 4),
    _Cdx6500allstationsStnStatus_Type()
)
cdx6500allstationsStnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsStnStatus.setStatus("mandatory")


class _Cdx6500allstationsStnState_Type(DisplayString):
    """Custom type cdx6500allstationsStnState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500allstationsStnState_Type.__name__ = "DisplayString"
_Cdx6500allstationsStnState_Object = MibTableColumn
cdx6500allstationsStnState = _Cdx6500allstationsStnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 5),
    _Cdx6500allstationsStnState_Type()
)
cdx6500allstationsStnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsStnState.setStatus("mandatory")


class _Cdx6500allstationsUtilizationIn_Type(Integer32):
    """Custom type cdx6500allstationsUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500allstationsUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500allstationsUtilizationIn_Object = MibTableColumn
cdx6500allstationsUtilizationIn = _Cdx6500allstationsUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 6),
    _Cdx6500allstationsUtilizationIn_Type()
)
cdx6500allstationsUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsUtilizationIn.setStatus("mandatory")


class _Cdx6500allstationsUtilizationOut_Type(Integer32):
    """Custom type cdx6500allstationsUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500allstationsUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500allstationsUtilizationOut_Object = MibTableColumn
cdx6500allstationsUtilizationOut = _Cdx6500allstationsUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 7),
    _Cdx6500allstationsUtilizationOut_Type()
)
cdx6500allstationsUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsUtilizationOut.setStatus("mandatory")
_Cdx6500allstationsCharInTot_Type = Counter32
_Cdx6500allstationsCharInTot_Object = MibTableColumn
cdx6500allstationsCharInTot = _Cdx6500allstationsCharInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 8),
    _Cdx6500allstationsCharInTot_Type()
)
cdx6500allstationsCharInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsCharInTot.setStatus("mandatory")
_Cdx6500allstationsCharOutTot_Type = Counter32
_Cdx6500allstationsCharOutTot_Object = MibTableColumn
cdx6500allstationsCharOutTot = _Cdx6500allstationsCharOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 9),
    _Cdx6500allstationsCharOutTot_Type()
)
cdx6500allstationsCharOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsCharOutTot.setStatus("mandatory")
_Cdx6500allstationsPktInTot_Type = Counter32
_Cdx6500allstationsPktInTot_Object = MibTableColumn
cdx6500allstationsPktInTot = _Cdx6500allstationsPktInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 10),
    _Cdx6500allstationsPktInTot_Type()
)
cdx6500allstationsPktInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsPktInTot.setStatus("mandatory")
_Cdx6500allstationsPktOutTot_Type = Counter32
_Cdx6500allstationsPktOutTot_Object = MibTableColumn
cdx6500allstationsPktOutTot = _Cdx6500allstationsPktOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 11),
    _Cdx6500allstationsPktOutTot_Type()
)
cdx6500allstationsPktOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsPktOutTot.setStatus("mandatory")
_Cdx6500allstationsFrameInTot_Type = Counter32
_Cdx6500allstationsFrameInTot_Object = MibTableColumn
cdx6500allstationsFrameInTot = _Cdx6500allstationsFrameInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 12),
    _Cdx6500allstationsFrameInTot_Type()
)
cdx6500allstationsFrameInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsFrameInTot.setStatus("mandatory")
_Cdx6500allstationsFrameOutTot_Type = Counter32
_Cdx6500allstationsFrameOutTot_Object = MibTableColumn
cdx6500allstationsFrameOutTot = _Cdx6500allstationsFrameOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 13),
    _Cdx6500allstationsFrameOutTot_Type()
)
cdx6500allstationsFrameOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsFrameOutTot.setStatus("mandatory")
_Cdx6500allstationsPktsQueued_Type = Integer32
_Cdx6500allstationsPktsQueued_Object = MibTableColumn
cdx6500allstationsPktsQueued = _Cdx6500allstationsPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 14),
    _Cdx6500allstationsPktsQueued_Type()
)
cdx6500allstationsPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsPktsQueued.setStatus("mandatory")
_Cdx6500allstationsCharsInPerSec_Type = Integer32
_Cdx6500allstationsCharsInPerSec_Object = MibTableColumn
cdx6500allstationsCharsInPerSec = _Cdx6500allstationsCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 15),
    _Cdx6500allstationsCharsInPerSec_Type()
)
cdx6500allstationsCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsCharsInPerSec.setStatus("mandatory")
_Cdx6500allstationsCharsOutPerSec_Type = Integer32
_Cdx6500allstationsCharsOutPerSec_Object = MibTableColumn
cdx6500allstationsCharsOutPerSec = _Cdx6500allstationsCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 16),
    _Cdx6500allstationsCharsOutPerSec_Type()
)
cdx6500allstationsCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsCharsOutPerSec.setStatus("mandatory")
_Cdx6500allstationsPktsInPerSec_Type = Integer32
_Cdx6500allstationsPktsInPerSec_Object = MibTableColumn
cdx6500allstationsPktsInPerSec = _Cdx6500allstationsPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 17),
    _Cdx6500allstationsPktsInPerSec_Type()
)
cdx6500allstationsPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsPktsInPerSec.setStatus("mandatory")
_Cdx6500allstationsPktsOutPerSec_Type = Integer32
_Cdx6500allstationsPktsOutPerSec_Object = MibTableColumn
cdx6500allstationsPktsOutPerSec = _Cdx6500allstationsPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 18),
    _Cdx6500allstationsPktsOutPerSec_Type()
)
cdx6500allstationsPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsPktsOutPerSec.setStatus("mandatory")
_Cdx6500allstationsFramesInPerSec_Type = Integer32
_Cdx6500allstationsFramesInPerSec_Object = MibTableColumn
cdx6500allstationsFramesInPerSec = _Cdx6500allstationsFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 19),
    _Cdx6500allstationsFramesInPerSec_Type()
)
cdx6500allstationsFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsFramesInPerSec.setStatus("mandatory")
_Cdx6500allstationsFramesOutPerSec_Type = Integer32
_Cdx6500allstationsFramesOutPerSec_Object = MibTableColumn
cdx6500allstationsFramesOutPerSec = _Cdx6500allstationsFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 20),
    _Cdx6500allstationsFramesOutPerSec_Type()
)
cdx6500allstationsFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500allstationsFramesOutPerSec.setStatus("mandatory")


class _Cdx6500allstationsBootStation_Type(Integer32):
    """Custom type cdx6500allstationsBootStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootStn", 1),
          ("noBootStn", 2))
    )


_Cdx6500allstationsBootStation_Type.__name__ = "Integer32"
_Cdx6500allstationsBootStation_Object = MibTableColumn
cdx6500allstationsBootStation = _Cdx6500allstationsBootStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 21),
    _Cdx6500allstationsBootStation_Type()
)
cdx6500allstationsBootStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500allstationsBootStation.setStatus("mandatory")


class _Cdx6500allstationsDisableStation_Type(Integer32):
    """Custom type cdx6500allstationsDisableStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableStn", 1),
          ("noDisableStn", 2))
    )


_Cdx6500allstationsDisableStation_Type.__name__ = "Integer32"
_Cdx6500allstationsDisableStation_Object = MibTableColumn
cdx6500allstationsDisableStation = _Cdx6500allstationsDisableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 22),
    _Cdx6500allstationsDisableStation_Type()
)
cdx6500allstationsDisableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500allstationsDisableStation.setStatus("mandatory")


class _Cdx6500allstationsEnableStation_Type(Integer32):
    """Custom type cdx6500allstationsEnableStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableStn", 1),
          ("noEnableStn", 2))
    )


_Cdx6500allstationsEnableStation_Type.__name__ = "Integer32"
_Cdx6500allstationsEnableStation_Object = MibTableColumn
cdx6500allstationsEnableStation = _Cdx6500allstationsEnableStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 23),
    _Cdx6500allstationsEnableStation_Type()
)
cdx6500allstationsEnableStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500allstationsEnableStation.setStatus("mandatory")


class _Cdx6500allstationsBusyOutStation_Type(Integer32):
    """Custom type cdx6500allstationsBusyOutStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busyoutStn", 1),
          ("noBusyoutStn", 2))
    )


_Cdx6500allstationsBusyOutStation_Type.__name__ = "Integer32"
_Cdx6500allstationsBusyOutStation_Object = MibTableColumn
cdx6500allstationsBusyOutStation = _Cdx6500allstationsBusyOutStation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 8, 1, 24),
    _Cdx6500allstationsBusyOutStation_Type()
)
cdx6500allstationsBusyOutStation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500allstationsBusyOutStation.setStatus("mandatory")
_Cdx6500PSTLANConnectionGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTLANConnectionGroup = _Cdx6500PSTLANConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500OSTCSISOptionStatTable_Object = MibTable
cdx6500OSTCSISOptionStatTable = _Cdx6500OSTCSISOptionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    cdx6500OSTCSISOptionStatTable.setStatus("mandatory")
_Cdx6500OSTCSISOptionStatEntry_Object = MibTableRow
cdx6500OSTCSISOptionStatEntry = _Cdx6500OSTCSISOptionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 5, 1)
)
cdx6500OSTCSISOptionStatEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500CSISOptionNumber"),
)
if mibBuilder.loadTexts:
    cdx6500OSTCSISOptionStatEntry.setStatus("mandatory")


class _Cdx6500CSISOptionNumber_Type(Integer32):
    """Custom type cdx6500CSISOptionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_Cdx6500CSISOptionNumber_Type.__name__ = "Integer32"
_Cdx6500CSISOptionNumber_Object = MibTableColumn
cdx6500CSISOptionNumber = _Cdx6500CSISOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 5, 1, 1),
    _Cdx6500CSISOptionNumber_Type()
)
cdx6500CSISOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISOptionNumber.setStatus("mandatory")


class _Cdx6500CSISMaxAllowed_Type(Integer32):
    """Custom type cdx6500CSISMaxAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500CSISMaxAllowed_Type.__name__ = "Integer32"
_Cdx6500CSISMaxAllowed_Object = MibTableColumn
cdx6500CSISMaxAllowed = _Cdx6500CSISMaxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 5, 1, 2),
    _Cdx6500CSISMaxAllowed_Type()
)
cdx6500CSISMaxAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISMaxAllowed.setStatus("mandatory")


class _Cdx6500CSISNumUsed_Type(Integer32):
    """Custom type cdx6500CSISNumUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_Cdx6500CSISNumUsed_Type.__name__ = "Integer32"
_Cdx6500CSISNumUsed_Object = MibTableColumn
cdx6500CSISNumUsed = _Cdx6500CSISNumUsed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 5, 1, 3),
    _Cdx6500CSISNumUsed_Type()
)
cdx6500CSISNumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISNumUsed.setStatus("mandatory")


class _Cdx6500CSISOptionAuth_Type(Integer32):
    """Custom type cdx6500CSISOptionAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("unauthorized", 1))
    )


_Cdx6500CSISOptionAuth_Type.__name__ = "Integer32"
_Cdx6500CSISOptionAuth_Object = MibTableColumn
cdx6500CSISOptionAuth = _Cdx6500CSISOptionAuth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 5, 1, 4),
    _Cdx6500CSISOptionAuth_Type()
)
cdx6500CSISOptionAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISOptionAuth.setStatus("mandatory")
_Cdx6500OSTCSISPortUsageTable_Object = MibTable
cdx6500OSTCSISPortUsageTable = _Cdx6500OSTCSISPortUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    cdx6500OSTCSISPortUsageTable.setStatus("mandatory")
_Cdx6500OSTCSISPortUsageEntry_Object = MibTableRow
cdx6500OSTCSISPortUsageEntry = _Cdx6500OSTCSISPortUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 6, 1)
)
cdx6500OSTCSISPortUsageEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500CSISPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500OSTCSISPortUsageEntry.setStatus("mandatory")


class _Cdx6500CSISPortNumber_Type(Integer32):
    """Custom type cdx6500CSISPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500CSISPortNumber_Type.__name__ = "Integer32"
_Cdx6500CSISPortNumber_Object = MibTableColumn
cdx6500CSISPortNumber = _Cdx6500CSISPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 6, 1, 1),
    _Cdx6500CSISPortNumber_Type()
)
cdx6500CSISPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISPortNumber.setStatus("mandatory")


class _Cdx6500CSISPortAuth_Type(Integer32):
    """Custom type cdx6500CSISPortAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("unauthorized", 1))
    )


_Cdx6500CSISPortAuth_Type.__name__ = "Integer32"
_Cdx6500CSISPortAuth_Object = MibTableColumn
cdx6500CSISPortAuth = _Cdx6500CSISPortAuth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 6, 1, 2),
    _Cdx6500CSISPortAuth_Type()
)
cdx6500CSISPortAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CSISPortAuth.setStatus("mandatory")
_Cdx6500StatTFTPGroup_ObjectIdentity = ObjectIdentity
cdx6500StatTFTPGroup = _Cdx6500StatTFTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3)
)
_Cdx6500StatNetworkSvcsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatNetworkSvcsGroup = _Cdx6500StatNetworkSvcsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4)
)
_Cdx6500StatSVCTable_Object = MibTable
cdx6500StatSVCTable = _Cdx6500StatSVCTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cdx6500StatSVCTable.setStatus("mandatory")
_Cdx6500StatSVCEntry_Object = MibTableRow
cdx6500StatSVCEntry = _Cdx6500StatSVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1)
)
cdx6500StatSVCEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "cdx6500StatSVCIndex"),
)
if mibBuilder.loadTexts:
    cdx6500StatSVCEntry.setStatus("mandatory")


class _Cdx6500StatSVCIndex_Type(Integer32):
    """Custom type cdx6500StatSVCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500StatSVCIndex_Type.__name__ = "Integer32"
_Cdx6500StatSVCIndex_Object = MibTableColumn
cdx6500StatSVCIndex = _Cdx6500StatSVCIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 1),
    _Cdx6500StatSVCIndex_Type()
)
cdx6500StatSVCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCIndex.setStatus("mandatory")


class _Cdx6500StatSVCCallingChannel_Type(DisplayString):
    """Custom type cdx6500StatSVCCallingChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Cdx6500StatSVCCallingChannel_Type.__name__ = "DisplayString"
_Cdx6500StatSVCCallingChannel_Object = MibTableColumn
cdx6500StatSVCCallingChannel = _Cdx6500StatSVCCallingChannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 2),
    _Cdx6500StatSVCCallingChannel_Type()
)
cdx6500StatSVCCallingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCCallingChannel.setStatus("mandatory")


class _Cdx6500StatSVCCalledChannel_Type(DisplayString):
    """Custom type cdx6500StatSVCCalledChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_Cdx6500StatSVCCalledChannel_Type.__name__ = "DisplayString"
_Cdx6500StatSVCCalledChannel_Object = MibTableColumn
cdx6500StatSVCCalledChannel = _Cdx6500StatSVCCalledChannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 3),
    _Cdx6500StatSVCCalledChannel_Type()
)
cdx6500StatSVCCalledChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCCalledChannel.setStatus("mandatory")


class _Cdx6500StatSVCReverseCharge_Type(Integer32):
    """Custom type cdx6500StatSVCReverseCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("newvalRefuse", 50),
          ("refuse", 0))
    )


_Cdx6500StatSVCReverseCharge_Type.__name__ = "Integer32"
_Cdx6500StatSVCReverseCharge_Object = MibTableColumn
cdx6500StatSVCReverseCharge = _Cdx6500StatSVCReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 4),
    _Cdx6500StatSVCReverseCharge_Type()
)
cdx6500StatSVCReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCReverseCharge.setStatus("mandatory")


class _Cdx6500StatSVCFastSelect_Type(Integer32):
    """Custom type cdx6500StatSVCFastSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("fastSelect", 1),
          ("newvalNoFastSelect", 50),
          ("noFastSelect", 0))
    )


_Cdx6500StatSVCFastSelect_Type.__name__ = "Integer32"
_Cdx6500StatSVCFastSelect_Object = MibTableColumn
cdx6500StatSVCFastSelect = _Cdx6500StatSVCFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 5),
    _Cdx6500StatSVCFastSelect_Type()
)
cdx6500StatSVCFastSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCFastSelect.setStatus("mandatory")


class _Cdx6500StatSVCNetUserIdentification_Type(Integer32):
    """Custom type cdx6500StatSVCNetUserIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalNotRequested", 50),
          ("notRequested", 0),
          ("requested", 1))
    )


_Cdx6500StatSVCNetUserIdentification_Type.__name__ = "Integer32"
_Cdx6500StatSVCNetUserIdentification_Object = MibTableColumn
cdx6500StatSVCNetUserIdentification = _Cdx6500StatSVCNetUserIdentification_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 6),
    _Cdx6500StatSVCNetUserIdentification_Type()
)
cdx6500StatSVCNetUserIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCNetUserIdentification.setStatus("mandatory")


class _Cdx6500StatSVCClosedUserGroup_Type(Integer32):
    """Custom type cdx6500StatSVCClosedUserGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalNotRequested", 50),
          ("notRequested", 0),
          ("requested", 1))
    )


_Cdx6500StatSVCClosedUserGroup_Type.__name__ = "Integer32"
_Cdx6500StatSVCClosedUserGroup_Object = MibTableColumn
cdx6500StatSVCClosedUserGroup = _Cdx6500StatSVCClosedUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 7),
    _Cdx6500StatSVCClosedUserGroup_Type()
)
cdx6500StatSVCClosedUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCClosedUserGroup.setStatus("mandatory")


class _Cdx6500StatSVCConnectionUPTime_Type(DisplayString):
    """Custom type cdx6500StatSVCConnectionUPTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_Cdx6500StatSVCConnectionUPTime_Type.__name__ = "DisplayString"
_Cdx6500StatSVCConnectionUPTime_Object = MibTableColumn
cdx6500StatSVCConnectionUPTime = _Cdx6500StatSVCConnectionUPTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 1, 1, 8),
    _Cdx6500StatSVCConnectionUPTime_Type()
)
cdx6500StatSVCConnectionUPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatSVCConnectionUPTime.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContTFTP_ObjectIdentity = ObjectIdentity
cdx6500ContTFTP = _Cdx6500ContTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2)
)
_Cdx6500statControls_ObjectIdentity = ObjectIdentity
cdx6500statControls = _Cdx6500statControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 4)
)


class _Cdx6500statResetAllStats_Type(Integer32):
    """Custom type cdx6500statResetAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cdx6500statResetAllStats_Type.__name__ = "Integer32"
_Cdx6500statResetAllStats_Object = MibScalar
cdx6500statResetAllStats = _Cdx6500statResetAllStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 4, 1),
    _Cdx6500statResetAllStats_Type()
)
cdx6500statResetAllStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500statResetAllStats.setStatus("mandatory")
_Cdx6500ContFlash_ObjectIdentity = ObjectIdentity
cdx6500ContFlash = _Cdx6500ContFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 21)
)


class _Cdx6500ContFlashCopyImage_Type(Integer32):
    """Custom type cdx6500ContFlashCopyImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("alternateTocurrent", 2),
          ("currentToalternate", 1),
          ("noOperation", 100))
    )


_Cdx6500ContFlashCopyImage_Type.__name__ = "Integer32"
_Cdx6500ContFlashCopyImage_Object = MibScalar
cdx6500ContFlashCopyImage = _Cdx6500ContFlashCopyImage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 21, 1),
    _Cdx6500ContFlashCopyImage_Type()
)
cdx6500ContFlashCopyImage.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContFlashCopyImage.setStatus("mandatory")


class _Cdx6500ContFlashCopyCmem_Type(Integer32):
    """Custom type cdx6500ContFlashCopyCmem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("alternateTocurrent", 2),
          ("currentToalternate", 1),
          ("noOperation", 100))
    )


_Cdx6500ContFlashCopyCmem_Type.__name__ = "Integer32"
_Cdx6500ContFlashCopyCmem_Object = MibScalar
cdx6500ContFlashCopyCmem = _Cdx6500ContFlashCopyCmem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 21, 2),
    _Cdx6500ContFlashCopyCmem_Type()
)
cdx6500ContFlashCopyCmem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContFlashCopyCmem.setStatus("mandatory")


class _Cdx6500ContFlashActiveImage_Type(Integer32):
    """Custom type cdx6500ContFlashActiveImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 100),
          ("setalternateImage", 2),
          ("setcurrentImage", 1))
    )


_Cdx6500ContFlashActiveImage_Type.__name__ = "Integer32"
_Cdx6500ContFlashActiveImage_Object = MibScalar
cdx6500ContFlashActiveImage = _Cdx6500ContFlashActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 21, 3),
    _Cdx6500ContFlashActiveImage_Type()
)
cdx6500ContFlashActiveImage.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContFlashActiveImage.setStatus("mandatory")


class _Cdx6500ContFlashActiveCmem_Type(Integer32):
    """Custom type cdx6500ContFlashActiveCmem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 100),
          ("setalternateCmem", 2),
          ("setcurrentCmem", 1))
    )


_Cdx6500ContFlashActiveCmem_Type.__name__ = "Integer32"
_Cdx6500ContFlashActiveCmem_Object = MibScalar
cdx6500ContFlashActiveCmem = _Cdx6500ContFlashActiveCmem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 21, 4),
    _Cdx6500ContFlashActiveCmem_Type()
)
cdx6500ContFlashActiveCmem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContFlashActiveCmem.setStatus("mandatory")


class _Cdx6500ContFlashDeleteImage_Type(Integer32):
    """Custom type cdx6500ContFlashDeleteImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100)
        )
    )
    namedValues = NamedValues(
        *(("deleteImage", 1),
          ("noOperation", 100))
    )


_Cdx6500ContFlashDeleteImage_Type.__name__ = "Integer32"
_Cdx6500ContFlashDeleteImage_Object = MibScalar
cdx6500ContFlashDeleteImage = _Cdx6500ContFlashDeleteImage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 21, 5),
    _Cdx6500ContFlashDeleteImage_Type()
)
cdx6500ContFlashDeleteImage.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContFlashDeleteImage.setStatus("mandatory")
_Cdx6500ContT3E3Table_ObjectIdentity = ObjectIdentity
cdx6500ContT3E3Table = _Cdx6500ContT3E3Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 23)
)
_Cdx6500T3E3ContEntry_Object = MibTableRow
cdx6500T3E3ContEntry = _Cdx6500T3E3ContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 23, 1)
)
cdx6500T3E3ContEntry.setIndexNames(
    (0, "CDX-6500-COMMON-MIB", "t3e3ContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T3E3ContEntry.setStatus("mandatory")


class _T3e3ContPortNumber_Type(Integer32):
    """Custom type t3e3ContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_T3e3ContPortNumber_Type.__name__ = "Integer32"
_T3e3ContPortNumber_Object = MibTableColumn
t3e3ContPortNumber = _T3e3ContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 23, 1, 1),
    _T3e3ContPortNumber_Type()
)
t3e3ContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t3e3ContPortNumber.setStatus("mandatory")


class _T3e3ContPortControl_Type(Integer32):
    """Custom type t3e3ContPortControl based on Integer32"""
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
        *(("boot", 1),
          ("disable", 3),
          ("enable", 2),
          ("resetstats", 4))
    )


_T3e3ContPortControl_Type.__name__ = "Integer32"
_T3e3ContPortControl_Object = MibTableColumn
t3e3ContPortControl = _T3e3ContPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 23, 1, 2),
    _T3e3ContPortControl_Type()
)
t3e3ContPortControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    t3e3ContPortControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CDX-6500-COMMON-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500NodeMgmt": cdx6500NodeMgmt,
       "cdx6500NMSNMPGroup": cdx6500NMSNMPGroup,
       "cdx6500SNMPPrimUDPChan": cdx6500SNMPPrimUDPChan,
       "cdx6500SNMPSecUDPChan": cdx6500SNMPSecUDPChan,
       "cdx6500SNMPAgentTimer": cdx6500SNMPAgentTimer,
       "cdx6500SNMPTrapEnable": cdx6500SNMPTrapEnable,
       "cdx6500SNMPBootAgent": cdx6500SNMPBootAgent,
       "cdx6500SNMPResetStats": cdx6500SNMPResetStats,
       "cdx6500SNMPLastTrap": cdx6500SNMPLastTrap,
       "cdx6500SNMPGenTrapsType": cdx6500SNMPGenTrapsType,
       "cdx6500SNMPTrapThrottleTable": cdx6500SNMPTrapThrottleTable,
       "cdx6500SNMPTrapThrottleEntry": cdx6500SNMPTrapThrottleEntry,
       "cdx6500SNMPTrapNumber": cdx6500SNMPTrapNumber,
       "cdx6500SNMPMaxNumOfTraps": cdx6500SNMPMaxNumOfTraps,
       "cdx6500SNMPThrottlingPeriod": cdx6500SNMPThrottlingPeriod,
       "cdx6500SNMPNewTrapLevel": cdx6500SNMPNewTrapLevel,
       "cdx6500SNMPEntryStatus": cdx6500SNMPEntryStatus,
       "cdx6500SNMPSetControl": cdx6500SNMPSetControl,
       "cdx6500SNMPIpAddress": cdx6500SNMPIpAddress,
       "cdx6500NMNodeParametersGroup": cdx6500NMNodeParametersGroup,
       "cdx6500NMNPconfig": cdx6500NMNPconfig,
       "cdx6500NMNPCnodeName": cdx6500NMNPCnodeName,
       "cdx6500NMNPCnodeNum": cdx6500NMNPCnodeNum,
       "cdx6500NMNPCnodeAddress": cdx6500NMNPCnodeAddress,
       "cdx6500NMNPCchassis": cdx6500NMNPCchassis,
       "cdx6500NMNPCdate": cdx6500NMNPCdate,
       "cdx6500NMNPCtime": cdx6500NMNPCtime,
       "cdx6500NMNPCportUtil": cdx6500NMNPCportUtil,
       "cdx6500NMNPCbuffUtil": cdx6500NMNPCbuffUtil,
       "cdx6500NMNPCcpuUtil": cdx6500NMNPCcpuUtil,
       "cdx6500NMNPCportErr": cdx6500NMNPCportErr,
       "cdx6500NMNPCalarmTmr": cdx6500NMNPCalarmTmr,
       "cdx6500NMNPCmaxRoutHops": cdx6500NMNPCmaxRoutHops,
       "cdx6500NMNPCctpSubAddr": cdx6500NMNPCctpSubAddr,
       "cdx6500NMNPCctpIdleTime": cdx6500NMNPCctpIdleTime,
       "cdx6500NMNPCalmDist": cdx6500NMNPCalmDist,
       "cdx6500NMNPCalmMmem": cdx6500NMNPCalmMmem,
       "cdx6500NMNPCalmSelect": cdx6500NMNPCalmSelect,
       "cdx6500NMNPCbroadPortSubad": cdx6500NMNPCbroadPortSubad,
       "cdx6500NMNPCnoBroadNets": cdx6500NMNPCnoBroadNets,
       "cdx6500NMNPCnoBroadInCh": cdx6500NMNPCnoBroadInCh,
       "cdx6500NMNPCbillMnem": cdx6500NMNPCbillMnem,
       "cdx6500NMNPCbillThresh": cdx6500NMNPCbillThresh,
       "cdx6500NMNPCmaxBill": cdx6500NMNPCmaxBill,
       "cdx6500NMNPCbillTimer": cdx6500NMNPCbillTimer,
       "cdx6500NMNPCpvcBill": cdx6500NMNPCpvcBill,
       "cdx6500NMNPCmaxCalls": cdx6500NMNPCmaxCalls,
       "cdx6500NMNPCpadBulletin": cdx6500NMNPCpadBulletin,
       "cdx6500NMNPCpadBanner": cdx6500NMNPCpadBanner,
       "cdx6500NMNPCdcpFac": cdx6500NMNPCdcpFac,
       "cdx6500NMNPCtrafficPri": cdx6500NMNPCtrafficPri,
       "cdx6500NMNPCtrafficStep": cdx6500NMNPCtrafficStep,
       "cdx6500NMNPCpropProtId": cdx6500NMNPCpropProtId,
       "cdx6500NMNPClanSubAddr": cdx6500NMNPClanSubAddr,
       "cdx6500NMNPCMaxFrameSize": cdx6500NMNPCMaxFrameSize,
       "cdx6500NMNPCCodexGroupFacility": cdx6500NMNPCCodexGroupFacility,
       "cdx6500NMNPCalmDistrib": cdx6500NMNPCalmDistrib,
       "cdx6500NMNPCalmSelection": cdx6500NMNPCalmSelection,
       "cdx6500NMNPChopFacility": cdx6500NMNPChopFacility,
       "cdx6500NMNPCnumNccpDevices": cdx6500NMNPCnumNccpDevices,
       "cdx6500NMNPCmaxCallid": cdx6500NMNPCmaxCallid,
       "cdx6500NMNPinvent": cdx6500NMNPinvent,
       "cdx6500NMNPIproductType": cdx6500NMNPIproductType,
       "cdx6500NMNPIsoftwareSrc": cdx6500NMNPIsoftwareSrc,
       "cdx6500NMNPIserialNum": cdx6500NMNPIserialNum,
       "cdx6500NMNPIpromRevision": cdx6500NMNPIpromRevision,
       "cdx6500NMNPIdlCodeRevision": cdx6500NMNPIdlCodeRevision,
       "cdx6500NMNPIdlCodeSource": cdx6500NMNPIdlCodeSource,
       "cdx6500NMNPIdlCodeSize": cdx6500NMNPIdlCodeSize,
       "cdx6500NMNPIflashStatus": cdx6500NMNPIflashStatus,
       "cdx6500NMNPIflashIdCur": cdx6500NMNPIflashIdCur,
       "cdx6500NMNPIflashIdAlt": cdx6500NMNPIflashIdAlt,
       "cdx6500NMNPIflashSizeCur": cdx6500NMNPIflashSizeCur,
       "cdx6500NMNPIflashSizeAlt": cdx6500NMNPIflashSizeAlt,
       "cdx6500NMNPIinventTable": cdx6500NMNPIinventTable,
       "cdx6500NMNPIinventEntry": cdx6500NMNPIinventEntry,
       "cdx6500NMNPIinventBoard": cdx6500NMNPIinventBoard,
       "cdx6500NMNPIinventType": cdx6500NMNPIinventType,
       "cdx6500NMNPIinventPorts": cdx6500NMNPIinventPorts,
       "cdx6500NMNPIinventStatus": cdx6500NMNPIinventStatus,
       "cdx6500NMNPIinventSerial": cdx6500NMNPIinventSerial,
       "cdx6500NMNPIinventAssy": cdx6500NMNPIinventAssy,
       "cdx6500NMNPIinventRev": cdx6500NMNPIinventRev,
       "cdx6500NMNPIinventDIM1": cdx6500NMNPIinventDIM1,
       "cdx6500NMNPIinventDIM2": cdx6500NMNPIinventDIM2,
       "cdx6500NMNPIinventPortConfigTable": cdx6500NMNPIinventPortConfigTable,
       "cdx6500NMNPIinventPortConfigEntry": cdx6500NMNPIinventPortConfigEntry,
       "cdx6500NMNPIinventPortNum": cdx6500NMNPIinventPortNum,
       "cdx6500NMNPIinventPortConfig": cdx6500NMNPIinventPortConfig,
       "cdx6500NMNPstats": cdx6500NMNPstats,
       "cdx6500NMNPSevLastOccPower": cdx6500NMNPSevLastOccPower,
       "cdx6500NMNPSevLastOccReset": cdx6500NMNPSevLastOccReset,
       "cdx6500NMNPSevLastOccReboot": cdx6500NMNPSevLastOccReboot,
       "cdx6500NMNPSevLastOccWDTimer": cdx6500NMNPSevLastOccWDTimer,
       "cdx6500NMNPSevLastOccConfig": cdx6500NMNPSevLastOccConfig,
       "cdx6500NMNPSstatusFan": cdx6500NMNPSstatusFan,
       "cdx6500NMNPSstatusPwrSy": cdx6500NMNPSstatusPwrSy,
       "cdx6500NMNPScmemSizeComp": cdx6500NMNPScmemSizeComp,
       "cdx6500NMNPScmemUseComp": cdx6500NMNPScmemUseComp,
       "cdx6500NMNPScmemSizeUncomp": cdx6500NMNPScmemSizeUncomp,
       "cdx6500NMNPScmemUseUnComp": cdx6500NMNPScmemUseUnComp,
       "cdx6500NMNPScallsInPlaceCur": cdx6500NMNPScallsInPlaceCur,
       "cdx6500NMNPScallsInPlaceMax": cdx6500NMNPScallsInPlaceMax,
       "cdx6500NMNPScallsPerSecCur": cdx6500NMNPScallsPerSecCur,
       "cdx6500NMNPScallsPerSecMax": cdx6500NMNPScallsPerSecMax,
       "cdx6500NMNPSpvcConnectCur": cdx6500NMNPSpvcConnectCur,
       "cdx6500NMNPSPVCConnectMax": cdx6500NMNPSPVCConnectMax,
       "cdx6500NMNPSbuffDataAvail": cdx6500NMNPSbuffDataAvail,
       "cdx6500NMNPSbuffDataUse": cdx6500NMNPSbuffDataUse,
       "cdx6500NMNPSbuffDataGauge": cdx6500NMNPSbuffDataGauge,
       "cdx6500NMNPSbuffPacketAvail": cdx6500NMNPSbuffPacketAvail,
       "cdx6500NMNPSbuffPacketUse": cdx6500NMNPSbuffPacketUse,
       "cdx6500NMNPSbuffPacketExhaust": cdx6500NMNPSbuffPacketExhaust,
       "cdx6500NMNPSbuffMgtAvail": cdx6500NMNPSbuffMgtAvail,
       "cdx6500NMNPSbuffMgtUse": cdx6500NMNPSbuffMgtUse,
       "cdx6500NMNPSbuffMgtExhaust": cdx6500NMNPSbuffMgtExhaust,
       "cdx6500NMNPSrateCurChar": cdx6500NMNPSrateCurChar,
       "cdx6500NMNPSrateCurPkt": cdx6500NMNPSrateCurPkt,
       "cdx6500NMNPSrateMaxChar": cdx6500NMNPSrateMaxChar,
       "cdx6500NMNPSrateMaxPkt": cdx6500NMNPSrateMaxPkt,
       "cdx6500NMNPSmemEprom": cdx6500NMNPSmemEprom,
       "cdx6500NMNPSmemDram": cdx6500NMNPSmemDram,
       "cdx6500NMNPSmemFlashCur": cdx6500NMNPSmemFlashCur,
       "cdx6500NMNPSmemFlashAlt": cdx6500NMNPSmemFlashAlt,
       "cdx6500NMNPScpuUtil": cdx6500NMNPScpuUtil,
       "cdx6500NMNPSDisplayNumImage": cdx6500NMNPSDisplayNumImage,
       "cdx6500NMNPSDisplayLEDstatus": cdx6500NMNPSDisplayLEDstatus,
       "cdx6500NMNPSDisplayLEDdiag": cdx6500NMNPSDisplayLEDdiag,
       "cdx6500NMNPSdefaultNode": cdx6500NMNPSdefaultNode,
       "cdx6500NMNPSresetStatTable": cdx6500NMNPSresetStatTable,
       "cdx6500NMNPSresetStatEntry": cdx6500NMNPSresetStatEntry,
       "cdx6500NMNPSresetStatPort": cdx6500NMNPSresetStatPort,
       "cdx6500NMNPSresetStatStatus": cdx6500NMNPSresetStatStatus,
       "cdx6500NMNPSresetStatAll": cdx6500NMNPSresetStatAll,
       "cdx6500NMNPSstatusPowerSy": cdx6500NMNPSstatusPowerSy,
       "cdx6500NMNPSstatsTable": cdx6500NMNPSstatsTable,
       "cdx6500NMNPSstatsEntry": cdx6500NMNPSstatsEntry,
       "cdx6500NMNPSstatsBoard": cdx6500NMNPSstatsBoard,
       "cdx6500NMNPSstatsbuffDataAvail": cdx6500NMNPSstatsbuffDataAvail,
       "cdx6500NMNPSstatsbuffDataUse": cdx6500NMNPSstatsbuffDataUse,
       "cdx6500NMNPSstatsbuffDataGauge": cdx6500NMNPSstatsbuffDataGauge,
       "cdx6500NMNPSstatsmemEprom": cdx6500NMNPSstatsmemEprom,
       "cdx6500NMNPSstatsmemDram": cdx6500NMNPSstatsmemDram,
       "cdx6500NMNPSstatsmemFlash": cdx6500NMNPSstatsmemFlash,
       "cdx6500NMNPSstatscpuUtil": cdx6500NMNPSstatscpuUtil,
       "cdx6500NMNPSstatsMaxcpuUtil": cdx6500NMNPSstatsMaxcpuUtil,
       "cdx6500NMNPSstatsMaxcpuUtilTime": cdx6500NMNPSstatsMaxcpuUtilTime,
       "cdx6500NMNPScallsInPlaceMaxTime": cdx6500NMNPScallsInPlaceMaxTime,
       "cdx6500NMNPSPVCConnectMaxTime": cdx6500NMNPSPVCConnectMaxTime,
       "cdx6500NMNPScallsPerSecMaxTime": cdx6500NMNPScallsPerSecMaxTime,
       "cdx6500NMNPSbuffDataGaugeTime": cdx6500NMNPSbuffDataGaugeTime,
       "cdx6500NMNPSbuffPacketGauge": cdx6500NMNPSbuffPacketGauge,
       "cdx6500NMNPSbuffPacketGaugeTime": cdx6500NMNPSbuffPacketGaugeTime,
       "cdx6500NMNPSbuffMgtGauge": cdx6500NMNPSbuffMgtGauge,
       "cdx6500NMNPSbuffMgtGaugeTime": cdx6500NMNPSbuffMgtGaugeTime,
       "cdx6500NMNPSrateMaxCharTime": cdx6500NMNPSrateMaxCharTime,
       "cdx6500NMNPSrateMaxPktTime": cdx6500NMNPSrateMaxPktTime,
       "cdx6500NMNPSMaxcpuUtil": cdx6500NMNPSMaxcpuUtil,
       "cdx6500NMNPSMaxcpuUtilTime": cdx6500NMNPSMaxcpuUtilTime,
       "cdx6500NMDiagnosticsGroup": cdx6500NMDiagnosticsGroup,
       "cdx6500NMReportTable": cdx6500NMReportTable,
       "cdx6500NMReportEntry": cdx6500NMReportEntry,
       "cdx6500reptIndex": cdx6500reptIndex,
       "cdx6500reptEvent": cdx6500reptEvent,
       "cdx6500NMreptClearLog": cdx6500NMreptClearLog,
       "cdx6500NMV54Loopback": cdx6500NMV54Loopback,
       "cdx6500NMV54LocalLoop": cdx6500NMV54LocalLoop,
       "cdx6500NMV54Loop2": cdx6500NMV54Loop2,
       "cdx6500NMV54Loop3": cdx6500NMV54Loop3,
       "cdx6500NMV54turnLoopbackOff": cdx6500NMV54turnLoopbackOff,
       "cdx6500NMV54LoopbackDuration": cdx6500NMV54LoopbackDuration,
       "cdx6500NMV54TestType": cdx6500NMV54TestType,
       "cdx6500NMV54LoopbackStatus": cdx6500NMV54LoopbackStatus,
       "cdx6500NMV54MessagesSent": cdx6500NMV54MessagesSent,
       "cdx6500NMV54GoodMsgsReceived": cdx6500NMV54GoodMsgsReceived,
       "cdx6500NMV54BadMsgsReceived": cdx6500NMV54BadMsgsReceived,
       "cdx6500NMV54LastPortTested": cdx6500NMV54LastPortTested,
       "cdx6500NMV54CurrentTestPort": cdx6500NMV54CurrentTestPort,
       "cdx6500NMV54LoopbackTest": cdx6500NMV54LoopbackTest,
       "cdx6500NMV54LoopbackTestType": cdx6500NMV54LoopbackTestType,
       "cdx6500NMV54LoopbackLastPortTested": cdx6500NMV54LoopbackLastPortTested,
       "cdx6500NMV54LoopbackCurrentTestPort": cdx6500NMV54LoopbackCurrentTestPort,
       "cdx6500NMV54LoopbackMessagesSent": cdx6500NMV54LoopbackMessagesSent,
       "cdx6500NMV54LoopbackGoodMsgsReceived": cdx6500NMV54LoopbackGoodMsgsReceived,
       "cdx6500NMV54LoopbackBadMsgsReceived": cdx6500NMV54LoopbackBadMsgsReceived,
       "cdx6500NMControlsGroup": cdx6500NMControlsGroup,
       "cdx6500NMCBootNode": cdx6500NMCBootNode,
       "cdx6500NMCBootTableNodeRec": cdx6500NMCBootTableNodeRec,
       "cdx6500NMDLSVGroup": cdx6500NMDLSVGroup,
       "cdx6500DLSVDLstate": cdx6500DLSVDLstate,
       "cdx6500DLSVPercentComplete": cdx6500DLSVPercentComplete,
       "cdx6500DLSVTimestamp": cdx6500DLSVTimestamp,
       "cdx6500DLSVLastServer": cdx6500DLSVLastServer,
       "cdx6500DLSVTransferType": cdx6500DLSVTransferType,
       "cdx6500DLSVInitiateTransfer": cdx6500DLSVInitiateTransfer,
       "cdx6500DLSVAgntSegmentSize": cdx6500DLSVAgntSegmentSize,
       "cdx6500DLSVAgntnmServAddress": cdx6500DLSVAgntnmServAddress,
       "cdx6500DLSVagntloaderSubaddress": cdx6500DLSVagntloaderSubaddress,
       "cdx6500DLSVagntdlServSubaddress": cdx6500DLSVagntdlServSubaddress,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500CreatePortAndStationTable": cdx6500CreatePortAndStationTable,
       "cdx6500CreatePortAndStationEntry": cdx6500CreatePortAndStationEntry,
       "cdx6500PortNumber": cdx6500PortNumber,
       "cdx6500CreatePortType": cdx6500CreatePortType,
       "cdx6500CreateStation": cdx6500CreateStation,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500GCTRouteSelectionTable": cdx6500GCTRouteSelectionTable,
       "cdx6500GCTRouteSelectionEntry": cdx6500GCTRouteSelectionEntry,
       "cdx6500RoutSVCEntryNumber": cdx6500RoutSVCEntryNumber,
       "cdx6500RoutSVCAddress": cdx6500RoutSVCAddress,
       "cdx6500RoutSVCDestination1": cdx6500RoutSVCDestination1,
       "cdx6500RoutSVCPriority1": cdx6500RoutSVCPriority1,
       "cdx6500RoutSVCDestination2": cdx6500RoutSVCDestination2,
       "cdx6500RoutSVCPriority2": cdx6500RoutSVCPriority2,
       "cdx6500RoutSVCDestination3": cdx6500RoutSVCDestination3,
       "cdx6500RoutSVCPriority3": cdx6500RoutSVCPriority3,
       "cdx6500RoutSVCDestination4": cdx6500RoutSVCDestination4,
       "cdx6500RoutSVCPriority4": cdx6500RoutSVCPriority4,
       "cdx6500RoutSVCDestination5": cdx6500RoutSVCDestination5,
       "cdx6500RoutSVCPriority5": cdx6500RoutSVCPriority5,
       "cdx6500RoutSVCDestination6": cdx6500RoutSVCDestination6,
       "cdx6500RoutSVCPriority6": cdx6500RoutSVCPriority6,
       "cdx6500RoutSVCDestination7": cdx6500RoutSVCDestination7,
       "cdx6500RoutSVCPriority7": cdx6500RoutSVCPriority7,
       "cdx6500RoutSVCDestination8": cdx6500RoutSVCDestination8,
       "cdx6500RoutSVCPriority8": cdx6500RoutSVCPriority8,
       "cdx6500RoutSVCAddress1": cdx6500RoutSVCAddress1,
       "cdx6500GCTPVCSetupTable": cdx6500GCTPVCSetupTable,
       "cdx6500GCTPVCSetupEntry": cdx6500GCTPVCSetupEntry,
       "cdx6500PVCSetupEntryNumber": cdx6500PVCSetupEntryNumber,
       "cdx6500PVCSetupSource": cdx6500PVCSetupSource,
       "cdx6500PVCSetupDestination": cdx6500PVCSetupDestination,
       "cdx6500CfgMnemonicTable": cdx6500CfgMnemonicTable,
       "cdx6500CfgMnemonicEntry": cdx6500CfgMnemonicEntry,
       "cdx6500mnemEntryNum": cdx6500mnemEntryNum,
       "cdx6500mnemName": cdx6500mnemName,
       "cdx6500mnemx28Cmd": cdx6500mnemx28Cmd,
       "cdx6500GCTNUIPasswordTable": cdx6500GCTNUIPasswordTable,
       "cdx6500GCTNUIPasswordEntry": cdx6500GCTNUIPasswordEntry,
       "cdx6500NUITEntryNumber": cdx6500NUITEntryNumber,
       "cdx6500NUITAcctName": cdx6500NUITAcctName,
       "cdx6500NUITPasswd": cdx6500NUITPasswd,
       "cdx6500NUITPADPromptNum": cdx6500NUITPADPromptNum,
       "cdx6500GCTSoftwareKeyTable": cdx6500GCTSoftwareKeyTable,
       "cdx6500GCTSoftwareKeyEntry": cdx6500GCTSoftwareKeyEntry,
       "cdx6500CSISSoftKeyEntryNumber": cdx6500CSISSoftKeyEntryNumber,
       "cdx6500CSISSoftKeyValue": cdx6500CSISSoftKeyValue,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTallPortsTable": cdx6500PPSTallPortsTable,
       "cdx6500PPSTallPortsEntry": cdx6500PPSTallPortsEntry,
       "cdx6500allportsPortNum": cdx6500allportsPortNum,
       "cdx6500allportsPortType": cdx6500allportsPortType,
       "cdx6500allportsPortStatus": cdx6500allportsPortStatus,
       "cdx6500allportsPortState": cdx6500allportsPortState,
       "cdx6500allportsPortSpeed": cdx6500allportsPortSpeed,
       "cdx6500allportsUtilizationIn": cdx6500allportsUtilizationIn,
       "cdx6500allportsUtilizationOut": cdx6500allportsUtilizationOut,
       "cdx6500allportsCharInTot": cdx6500allportsCharInTot,
       "cdx6500allportsCharOutTot": cdx6500allportsCharOutTot,
       "cdx6500allportsPktInTot": cdx6500allportsPktInTot,
       "cdx6500allportsPktOutTot": cdx6500allportsPktOutTot,
       "cdx6500allportsFrameInTot": cdx6500allportsFrameInTot,
       "cdx6500allportsFrameOutTot": cdx6500allportsFrameOutTot,
       "cdx6500allportsPktsQueued": cdx6500allportsPktsQueued,
       "cdx6500allportsCharsInPerSec": cdx6500allportsCharsInPerSec,
       "cdx6500allportsCharsOutPerSec": cdx6500allportsCharsOutPerSec,
       "cdx6500allportsPktsInPerSec": cdx6500allportsPktsInPerSec,
       "cdx6500allportsPktsOutPerSec": cdx6500allportsPktsOutPerSec,
       "cdx6500allportsFramesInPerSec": cdx6500allportsFramesInPerSec,
       "cdx6500allportsFramesOutPerSec": cdx6500allportsFramesOutPerSec,
       "cdx6500allportsOverrunErrors": cdx6500allportsOverrunErrors,
       "cdx6500allportsUnderrunErrors": cdx6500allportsUnderrunErrors,
       "cdx6500allportsCRCErrors": cdx6500allportsCRCErrors,
       "cdx6500allportsParityErrors": cdx6500allportsParityErrors,
       "cdx6500allportsFramingErrors": cdx6500allportsFramingErrors,
       "cdx6500allportsBootPort": cdx6500allportsBootPort,
       "cdx6500allportsPortControlStatus": cdx6500allportsPortControlStatus,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTallStationsTable": cdx6500SPSTallStationsTable,
       "cdx6500SPSTallStationsEntry": cdx6500SPSTallStationsEntry,
       "cdx6500allstationsPortNum": cdx6500allstationsPortNum,
       "cdx6500allstationsStnNum": cdx6500allstationsStnNum,
       "cdx6500allstationsStnType": cdx6500allstationsStnType,
       "cdx6500allstationsStnStatus": cdx6500allstationsStnStatus,
       "cdx6500allstationsStnState": cdx6500allstationsStnState,
       "cdx6500allstationsUtilizationIn": cdx6500allstationsUtilizationIn,
       "cdx6500allstationsUtilizationOut": cdx6500allstationsUtilizationOut,
       "cdx6500allstationsCharInTot": cdx6500allstationsCharInTot,
       "cdx6500allstationsCharOutTot": cdx6500allstationsCharOutTot,
       "cdx6500allstationsPktInTot": cdx6500allstationsPktInTot,
       "cdx6500allstationsPktOutTot": cdx6500allstationsPktOutTot,
       "cdx6500allstationsFrameInTot": cdx6500allstationsFrameInTot,
       "cdx6500allstationsFrameOutTot": cdx6500allstationsFrameOutTot,
       "cdx6500allstationsPktsQueued": cdx6500allstationsPktsQueued,
       "cdx6500allstationsCharsInPerSec": cdx6500allstationsCharsInPerSec,
       "cdx6500allstationsCharsOutPerSec": cdx6500allstationsCharsOutPerSec,
       "cdx6500allstationsPktsInPerSec": cdx6500allstationsPktsInPerSec,
       "cdx6500allstationsPktsOutPerSec": cdx6500allstationsPktsOutPerSec,
       "cdx6500allstationsFramesInPerSec": cdx6500allstationsFramesInPerSec,
       "cdx6500allstationsFramesOutPerSec": cdx6500allstationsFramesOutPerSec,
       "cdx6500allstationsBootStation": cdx6500allstationsBootStation,
       "cdx6500allstationsDisableStation": cdx6500allstationsDisableStation,
       "cdx6500allstationsEnableStation": cdx6500allstationsEnableStation,
       "cdx6500allstationsBusyOutStation": cdx6500allstationsBusyOutStation,
       "cdx6500PSTLANConnectionGroup": cdx6500PSTLANConnectionGroup,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500OSTCSISOptionStatTable": cdx6500OSTCSISOptionStatTable,
       "cdx6500OSTCSISOptionStatEntry": cdx6500OSTCSISOptionStatEntry,
       "cdx6500CSISOptionNumber": cdx6500CSISOptionNumber,
       "cdx6500CSISMaxAllowed": cdx6500CSISMaxAllowed,
       "cdx6500CSISNumUsed": cdx6500CSISNumUsed,
       "cdx6500CSISOptionAuth": cdx6500CSISOptionAuth,
       "cdx6500OSTCSISPortUsageTable": cdx6500OSTCSISPortUsageTable,
       "cdx6500OSTCSISPortUsageEntry": cdx6500OSTCSISPortUsageEntry,
       "cdx6500CSISPortNumber": cdx6500CSISPortNumber,
       "cdx6500CSISPortAuth": cdx6500CSISPortAuth,
       "cdx6500StatTFTPGroup": cdx6500StatTFTPGroup,
       "cdx6500StatNetworkSvcsGroup": cdx6500StatNetworkSvcsGroup,
       "cdx6500StatSVCTable": cdx6500StatSVCTable,
       "cdx6500StatSVCEntry": cdx6500StatSVCEntry,
       "cdx6500StatSVCIndex": cdx6500StatSVCIndex,
       "cdx6500StatSVCCallingChannel": cdx6500StatSVCCallingChannel,
       "cdx6500StatSVCCalledChannel": cdx6500StatSVCCalledChannel,
       "cdx6500StatSVCReverseCharge": cdx6500StatSVCReverseCharge,
       "cdx6500StatSVCFastSelect": cdx6500StatSVCFastSelect,
       "cdx6500StatSVCNetUserIdentification": cdx6500StatSVCNetUserIdentification,
       "cdx6500StatSVCClosedUserGroup": cdx6500StatSVCClosedUserGroup,
       "cdx6500StatSVCConnectionUPTime": cdx6500StatSVCConnectionUPTime,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContTFTP": cdx6500ContTFTP,
       "cdx6500statControls": cdx6500statControls,
       "cdx6500statResetAllStats": cdx6500statResetAllStats,
       "cdx6500ContFlash": cdx6500ContFlash,
       "cdx6500ContFlashCopyImage": cdx6500ContFlashCopyImage,
       "cdx6500ContFlashCopyCmem": cdx6500ContFlashCopyCmem,
       "cdx6500ContFlashActiveImage": cdx6500ContFlashActiveImage,
       "cdx6500ContFlashActiveCmem": cdx6500ContFlashActiveCmem,
       "cdx6500ContFlashDeleteImage": cdx6500ContFlashDeleteImage,
       "cdx6500ContT3E3Table": cdx6500ContT3E3Table,
       "cdx6500T3E3ContEntry": cdx6500T3E3ContEntry,
       "t3e3ContPortNumber": t3e3ContPortNumber,
       "t3e3ContPortControl": t3e3ContPortControl}
)
