# SNMP MIB module (ACLEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACLEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:31 2024
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

(aclExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "aclExt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apAclExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApAclExtEnable_Type(Integer32):
    """Custom type apAclExtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApAclExtEnable_Type.__name__ = "Integer32"
_ApAclExtEnable_Object = MibScalar
apAclExtEnable = _ApAclExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 2),
    _ApAclExtEnable_Type()
)
apAclExtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAclExtEnable.setStatus("current")


class _ApAclExtLogEnable_Type(Integer32):
    """Custom type apAclExtLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApAclExtLogEnable_Type.__name__ = "Integer32"
_ApAclExtLogEnable_Object = MibScalar
apAclExtLogEnable = _ApAclExtLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 3),
    _ApAclExtLogEnable_Type()
)
apAclExtLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAclExtLogEnable.setStatus("obsolete")
_ApMainAclTable_Object = MibTable
apMainAclTable = _ApMainAclTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 4)
)
if mibBuilder.loadTexts:
    apMainAclTable.setStatus("current")
_ApMainAclEntry_Object = MibTableRow
apMainAclEntry = _ApMainAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1)
)
apMainAclEntry.setIndexNames(
    (0, "ACLEXT-MIB", "apMainAclIndex"),
)
if mibBuilder.loadTexts:
    apMainAclEntry.setStatus("current")


class _ApMainAclIndex_Type(Integer32):
    """Custom type apMainAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ApMainAclIndex_Type.__name__ = "Integer32"
_ApMainAclIndex_Object = MibTableColumn
apMainAclIndex = _ApMainAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1, 1),
    _ApMainAclIndex_Type()
)
apMainAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apMainAclIndex.setStatus("current")
_ApMainAclStatus_Type = RowStatus
_ApMainAclStatus_Object = MibTableColumn
apMainAclStatus = _ApMainAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1, 2),
    _ApMainAclStatus_Type()
)
apMainAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apMainAclStatus.setStatus("current")


class _ApMainAclCountZero_Type(Integer32):
    """Custom type apMainAclCountZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_ApMainAclCountZero_Type.__name__ = "Integer32"
_ApMainAclCountZero_Object = MibTableColumn
apMainAclCountZero = _ApMainAclCountZero_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 4, 1, 3),
    _ApMainAclCountZero_Type()
)
apMainAclCountZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apMainAclCountZero.setStatus("current")
_ApAclTable_Object = MibTable
apAclTable = _ApAclTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5)
)
if mibBuilder.loadTexts:
    apAclTable.setStatus("current")
_ApAclEntry_Object = MibTableRow
apAclEntry = _ApAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1)
)
apAclEntry.setIndexNames(
    (0, "ACLEXT-MIB", "apMainAclIndex"),
    (0, "ACLEXT-MIB", "apAclSubIndex"),
)
if mibBuilder.loadTexts:
    apAclEntry.setStatus("current")


class _ApAclIndex_Type(Integer32):
    """Custom type apAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ApAclIndex_Type.__name__ = "Integer32"
_ApAclIndex_Object = MibTableColumn
apAclIndex = _ApAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 1),
    _ApAclIndex_Type()
)
apAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclIndex.setStatus("current")


class _ApAclSubIndex_Type(Integer32):
    """Custom type apAclSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ApAclSubIndex_Type.__name__ = "Integer32"
_ApAclSubIndex_Object = MibTableColumn
apAclSubIndex = _ApAclSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 2),
    _ApAclSubIndex_Type()
)
apAclSubIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSubIndex.setStatus("current")


class _ApAclAction_Type(Integer32):
    """Custom type apAclAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 3),
          ("deny", 2),
          ("permit", 1))
    )


_ApAclAction_Type.__name__ = "Integer32"
_ApAclAction_Object = MibTableColumn
apAclAction = _ApAclAction_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 3),
    _ApAclAction_Type()
)
apAclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclAction.setStatus("current")


class _ApAclProtocol_Type(Integer32):
    """Custom type apAclProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              9,
              17,
              89)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("igp", 9),
          ("ospf", 89),
          ("tcp", 6),
          ("udp", 17))
    )


_ApAclProtocol_Type.__name__ = "Integer32"
_ApAclProtocol_Object = MibTableColumn
apAclProtocol = _ApAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 4),
    _ApAclProtocol_Type()
)
apAclProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclProtocol.setStatus("current")
_ApAclSourceIpAddr_Type = IpAddress
_ApAclSourceIpAddr_Object = MibTableColumn
apAclSourceIpAddr = _ApAclSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 5),
    _ApAclSourceIpAddr_Type()
)
apAclSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSourceIpAddr.setStatus("current")
_ApAclSourceMask_Type = IpAddress
_ApAclSourceMask_Object = MibTableColumn
apAclSourceMask = _ApAclSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 6),
    _ApAclSourceMask_Type()
)
apAclSourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSourceMask.setStatus("current")
_ApAclSourceGroup_Type = DisplayString
_ApAclSourceGroup_Object = MibTableColumn
apAclSourceGroup = _ApAclSourceGroup_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 7),
    _ApAclSourceGroup_Type()
)
apAclSourceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSourceGroup.setStatus("current")
_ApAclDestIpAddr_Type = IpAddress
_ApAclDestIpAddr_Object = MibTableColumn
apAclDestIpAddr = _ApAclDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 8),
    _ApAclDestIpAddr_Type()
)
apAclDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestIpAddr.setStatus("current")
_ApAclDestMask_Type = IpAddress
_ApAclDestMask_Object = MibTableColumn
apAclDestMask = _ApAclDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 9),
    _ApAclDestMask_Type()
)
apAclDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestMask.setStatus("current")
_ApAclDestContent_Type = DisplayString
_ApAclDestContent_Object = MibTableColumn
apAclDestContent = _ApAclDestContent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 10),
    _ApAclDestContent_Type()
)
apAclDestContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestContent.setStatus("current")
_ApAclPrecedence_Type = Integer32
_ApAclPrecedence_Object = MibTableColumn
apAclPrecedence = _ApAclPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 11),
    _ApAclPrecedence_Type()
)
apAclPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclPrecedence.setStatus("current")
_ApAclTOS_Type = Integer32
_ApAclTOS_Object = MibTableColumn
apAclTOS = _ApAclTOS_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 12),
    _ApAclTOS_Type()
)
apAclTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclTOS.setStatus("current")


class _ApAclLog_Type(Integer32):
    """Custom type apAclLog based on Integer32"""
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


_ApAclLog_Type.__name__ = "Integer32"
_ApAclLog_Object = MibTableColumn
apAclLog = _ApAclLog_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 13),
    _ApAclLog_Type()
)
apAclLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclLog.setStatus("current")
_ApAclStartTime_Type = Integer32
_ApAclStartTime_Object = MibTableColumn
apAclStartTime = _ApAclStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 14),
    _ApAclStartTime_Type()
)
apAclStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclStartTime.setStatus("current")
_ApAclStopTime_Type = Integer32
_ApAclStopTime_Object = MibTableColumn
apAclStopTime = _ApAclStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 15),
    _ApAclStopTime_Type()
)
apAclStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclStopTime.setStatus("current")


class _ApAclQOSClass_Type(Integer32):
    """Custom type apAclQOSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ApAclQOSClass_Type.__name__ = "Integer32"
_ApAclQOSClass_Object = MibTableColumn
apAclQOSClass = _ApAclQOSClass_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 16),
    _ApAclQOSClass_Type()
)
apAclQOSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclQOSClass.setStatus("current")


class _ApAclSourcePortOperator_Type(Integer32):
    """Custom type apAclSourcePortOperator based on Integer32"""
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
        *(("eq", 3),
          ("gt", 2),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_ApAclSourcePortOperator_Type.__name__ = "Integer32"
_ApAclSourcePortOperator_Object = MibTableColumn
apAclSourcePortOperator = _ApAclSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 17),
    _ApAclSourcePortOperator_Type()
)
apAclSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSourcePortOperator.setStatus("current")


class _ApAclSourcePortStart_Type(Integer32):
    """Custom type apAclSourcePortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApAclSourcePortStart_Type.__name__ = "Integer32"
_ApAclSourcePortStart_Object = MibTableColumn
apAclSourcePortStart = _ApAclSourcePortStart_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 18),
    _ApAclSourcePortStart_Type()
)
apAclSourcePortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSourcePortStart.setStatus("current")


class _ApAclSourcePortEnd_Type(Integer32):
    """Custom type apAclSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApAclSourcePortEnd_Type.__name__ = "Integer32"
_ApAclSourcePortEnd_Object = MibTableColumn
apAclSourcePortEnd = _ApAclSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 19),
    _ApAclSourcePortEnd_Type()
)
apAclSourcePortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSourcePortEnd.setStatus("current")


class _ApAclDestPortOperator_Type(Integer32):
    """Custom type apAclDestPortOperator based on Integer32"""
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
        *(("eq", 3),
          ("gt", 2),
          ("lt", 1),
          ("neq", 4),
          ("range", 5))
    )


_ApAclDestPortOperator_Type.__name__ = "Integer32"
_ApAclDestPortOperator_Object = MibTableColumn
apAclDestPortOperator = _ApAclDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 20),
    _ApAclDestPortOperator_Type()
)
apAclDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestPortOperator.setStatus("current")


class _ApAclDestPortEnum_Type(Integer32):
    """Custom type apAclDestPortEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              20,
              21,
              23,
              25,
              53,
              70,
              80,
              110,
              119,
              123,
              179,
              389,
              443)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 179),
          ("domain", 53),
          ("ftp", 21),
          ("ftp-data", 20),
          ("gopher", 70),
          ("http", 80),
          ("https", 443),
          ("ldap", 389),
          ("nntp", 119),
          ("none", 0),
          ("ntp", 123),
          ("pop", 110),
          ("smtp", 25),
          ("telnet", 23))
    )


_ApAclDestPortEnum_Type.__name__ = "Integer32"
_ApAclDestPortEnum_Object = MibTableColumn
apAclDestPortEnum = _ApAclDestPortEnum_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 21),
    _ApAclDestPortEnum_Type()
)
apAclDestPortEnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestPortEnum.setStatus("current")


class _ApAclDestPortStart_Type(Integer32):
    """Custom type apAclDestPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApAclDestPortStart_Type.__name__ = "Integer32"
_ApAclDestPortStart_Object = MibTableColumn
apAclDestPortStart = _ApAclDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 22),
    _ApAclDestPortStart_Type()
)
apAclDestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestPortStart.setStatus("current")


class _ApAclDestPortEnd_Type(Integer32):
    """Custom type apAclDestPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApAclDestPortEnd_Type.__name__ = "Integer32"
_ApAclDestPortEnd_Object = MibTableColumn
apAclDestPortEnd = _ApAclDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 23),
    _ApAclDestPortEnd_Type()
)
apAclDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestPortEnd.setStatus("current")


class _ApAclEnable_Type(Integer32):
    """Custom type apAclEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApAclEnable_Type.__name__ = "Integer32"
_ApAclEnable_Object = MibTableColumn
apAclEnable = _ApAclEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 24),
    _ApAclEnable_Type()
)
apAclEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclEnable.setStatus("current")


class _ApAclProtocolNumber_Type(Integer32):
    """Custom type apAclProtocolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApAclProtocolNumber_Type.__name__ = "Integer32"
_ApAclProtocolNumber_Object = MibTableColumn
apAclProtocolNumber = _ApAclProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 25),
    _ApAclProtocolNumber_Type()
)
apAclProtocolNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclProtocolNumber.setStatus("current")
_ApAclStatus_Type = RowStatus
_ApAclStatus_Object = MibTableColumn
apAclStatus = _ApAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 26),
    _ApAclStatus_Type()
)
apAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclStatus.setStatus("current")


class _ApAclPreferredService_Type(DisplayString):
    """Custom type apAclPreferredService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApAclPreferredService_Type.__name__ = "DisplayString"
_ApAclPreferredService_Object = MibTableColumn
apAclPreferredService = _ApAclPreferredService_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 27),
    _ApAclPreferredService_Type()
)
apAclPreferredService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclPreferredService.setStatus("current")


class _ApAclSourceNQLName_Type(DisplayString):
    """Custom type apAclSourceNQLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApAclSourceNQLName_Type.__name__ = "DisplayString"
_ApAclSourceNQLName_Object = MibTableColumn
apAclSourceNQLName = _ApAclSourceNQLName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 28),
    _ApAclSourceNQLName_Type()
)
apAclSourceNQLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclSourceNQLName.setStatus("current")


class _ApAclDestNQLName_Type(DisplayString):
    """Custom type apAclDestNQLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApAclDestNQLName_Type.__name__ = "DisplayString"
_ApAclDestNQLName_Object = MibTableColumn
apAclDestNQLName = _ApAclDestNQLName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 29),
    _ApAclDestNQLName_Type()
)
apAclDestNQLName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclDestNQLName.setStatus("current")
_ApAclCountContentHits_Type = Integer32
_ApAclCountContentHits_Object = MibTableColumn
apAclCountContentHits = _ApAclCountContentHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 30),
    _ApAclCountContentHits_Type()
)
apAclCountContentHits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclCountContentHits.setStatus("current")
_ApAclCountRouterHits_Type = Integer32
_ApAclCountRouterHits_Object = MibTableColumn
apAclCountRouterHits = _ApAclCountRouterHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 31),
    _ApAclCountRouterHits_Type()
)
apAclCountRouterHits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclCountRouterHits.setStatus("current")
_ApAclCountDNSHits_Type = Integer32
_ApAclCountDNSHits_Object = MibTableColumn
apAclCountDNSHits = _ApAclCountDNSHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 23, 5, 1, 32),
    _ApAclCountDNSHits_Type()
)
apAclCountDNSHits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apAclCountDNSHits.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACLEXT-MIB",
    **{"apAclExtMib": apAclExtMib,
       "apAclExtEnable": apAclExtEnable,
       "apAclExtLogEnable": apAclExtLogEnable,
       "apMainAclTable": apMainAclTable,
       "apMainAclEntry": apMainAclEntry,
       "apMainAclIndex": apMainAclIndex,
       "apMainAclStatus": apMainAclStatus,
       "apMainAclCountZero": apMainAclCountZero,
       "apAclTable": apAclTable,
       "apAclEntry": apAclEntry,
       "apAclIndex": apAclIndex,
       "apAclSubIndex": apAclSubIndex,
       "apAclAction": apAclAction,
       "apAclProtocol": apAclProtocol,
       "apAclSourceIpAddr": apAclSourceIpAddr,
       "apAclSourceMask": apAclSourceMask,
       "apAclSourceGroup": apAclSourceGroup,
       "apAclDestIpAddr": apAclDestIpAddr,
       "apAclDestMask": apAclDestMask,
       "apAclDestContent": apAclDestContent,
       "apAclPrecedence": apAclPrecedence,
       "apAclTOS": apAclTOS,
       "apAclLog": apAclLog,
       "apAclStartTime": apAclStartTime,
       "apAclStopTime": apAclStopTime,
       "apAclQOSClass": apAclQOSClass,
       "apAclSourcePortOperator": apAclSourcePortOperator,
       "apAclSourcePortStart": apAclSourcePortStart,
       "apAclSourcePortEnd": apAclSourcePortEnd,
       "apAclDestPortOperator": apAclDestPortOperator,
       "apAclDestPortEnum": apAclDestPortEnum,
       "apAclDestPortStart": apAclDestPortStart,
       "apAclDestPortEnd": apAclDestPortEnd,
       "apAclEnable": apAclEnable,
       "apAclProtocolNumber": apAclProtocolNumber,
       "apAclStatus": apAclStatus,
       "apAclPreferredService": apAclPreferredService,
       "apAclSourceNQLName": apAclSourceNQLName,
       "apAclDestNQLName": apAclDestNQLName,
       "apAclCountContentHits": apAclCountContentHits,
       "apAclCountRouterHits": apAclCountRouterHits,
       "apAclCountDNSHits": apAclCountDNSHits}
)
