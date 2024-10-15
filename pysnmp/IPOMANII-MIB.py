# SNMP MIB module (IPOMANII-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPOMANII-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:03 2024
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
 NotificationType,
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
    "NotificationType",
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

_Ingrasys_ObjectIdentity = ObjectIdentity
ingrasys = _Ingrasys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1)
)
_PduAgent_ObjectIdentity = ObjectIdentity
pduAgent = _PduAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4)
)
_IPoManII_ObjectIdentity = ObjectIdentity
iPoManII = _IPoManII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2)
)
_IpmObjects_ObjectIdentity = ObjectIdentity
ipmObjects = _IpmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1)
)
_IpmIdent_ObjectIdentity = ObjectIdentity
ipmIdent = _IpmIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 1)
)


class _IpmIdentManufacturer_Type(DisplayString):
    """Custom type ipmIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmIdentManufacturer_Type.__name__ = "DisplayString"
_IpmIdentManufacturer_Object = MibScalar
ipmIdentManufacturer = _IpmIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 1, 1),
    _IpmIdentManufacturer_Type()
)
ipmIdentManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmIdentManufacturer.setStatus("mandatory")


class _IpmIdentModel_Type(DisplayString):
    """Custom type ipmIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmIdentModel_Type.__name__ = "DisplayString"
_IpmIdentModel_Object = MibScalar
ipmIdentModel = _IpmIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 1, 2),
    _IpmIdentModel_Type()
)
ipmIdentModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmIdentModel.setStatus("mandatory")


class _IpmIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type ipmIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IpmIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_IpmIdentAgentSoftwareVersion_Object = MibScalar
ipmIdentAgentSoftwareVersion = _IpmIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 1, 3),
    _IpmIdentAgentSoftwareVersion_Type()
)
ipmIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmIdentAgentSoftwareVersion.setStatus("mandatory")


class _IpmIdentName_Type(DisplayString):
    """Custom type ipmIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmIdentName_Type.__name__ = "DisplayString"
_IpmIdentName_Object = MibScalar
ipmIdentName = _IpmIdentName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 1, 4),
    _IpmIdentName_Type()
)
ipmIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmIdentName.setStatus("mandatory")
_IpmAgent_ObjectIdentity = ObjectIdentity
ipmAgent = _IpmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2)
)
_IpmAgentConfig_ObjectIdentity = ObjectIdentity
ipmAgentConfig = _IpmAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1)
)


class _IpmAgentMibVersion_Type(Integer32):
    """Custom type ipmAgentMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_IpmAgentMibVersion_Type.__name__ = "Integer32"
_IpmAgentMibVersion_Object = MibScalar
ipmAgentMibVersion = _IpmAgentMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 1),
    _IpmAgentMibVersion_Type()
)
ipmAgentMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmAgentMibVersion.setStatus("mandatory")
_IpmAgentLog_ObjectIdentity = ObjectIdentity
ipmAgentLog = _IpmAgentLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 4)
)


class _PduAgentDataLogInterval_Type(Integer32):
    """Custom type pduAgentDataLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 28800),
    )


_PduAgentDataLogInterval_Type.__name__ = "Integer32"
_PduAgentDataLogInterval_Object = MibScalar
pduAgentDataLogInterval = _PduAgentDataLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 4, 1),
    _PduAgentDataLogInterval_Type()
)
pduAgentDataLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduAgentDataLogInterval.setStatus("mandatory")
_IpmAgentControl_ObjectIdentity = ObjectIdentity
ipmAgentControl = _IpmAgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 5)
)


class _IpmAgentControlDefault_Type(Integer32):
    """Custom type ipmAgentControlDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("reset", 1))
    )


_IpmAgentControlDefault_Type.__name__ = "Integer32"
_IpmAgentControlDefault_Object = MibScalar
ipmAgentControlDefault = _IpmAgentControlDefault_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 5, 1),
    _IpmAgentControlDefault_Type()
)
ipmAgentControlDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentControlDefault.setStatus("mandatory")


class _IpmAgentControlRestart_Type(Integer32):
    """Custom type ipmAgentControlRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("restart", 1))
    )


_IpmAgentControlRestart_Type.__name__ = "Integer32"
_IpmAgentControlRestart_Object = MibScalar
ipmAgentControlRestart = _IpmAgentControlRestart_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 5, 2),
    _IpmAgentControlRestart_Type()
)
ipmAgentControlRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentControlRestart.setStatus("mandatory")
_IpmAgentTrap_ObjectIdentity = ObjectIdentity
ipmAgentTrap = _IpmAgentTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 6)
)
_IpmAgentTrapRetryCount_Type = Integer32
_IpmAgentTrapRetryCount_Object = MibScalar
ipmAgentTrapRetryCount = _IpmAgentTrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 6, 1),
    _IpmAgentTrapRetryCount_Type()
)
ipmAgentTrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTrapRetryCount.setStatus("mandatory")
_IpmAgentTrapRetryTime_Type = Integer32
_IpmAgentTrapRetryTime_Object = MibScalar
ipmAgentTrapRetryTime = _IpmAgentTrapRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 6, 2),
    _IpmAgentTrapRetryTime_Type()
)
ipmAgentTrapRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTrapRetryTime.setStatus("mandatory")
_IpmAgentTrapAckSignature_Type = Integer32
_IpmAgentTrapAckSignature_Object = MibScalar
ipmAgentTrapAckSignature = _IpmAgentTrapAckSignature_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 6, 3),
    _IpmAgentTrapAckSignature_Type()
)
ipmAgentTrapAckSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTrapAckSignature.setStatus("mandatory")
_IpmAgentTrapsReceiversTable_Object = MibTable
ipmAgentTrapsReceiversTable = _IpmAgentTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ipmAgentTrapsReceiversTable.setStatus("mandatory")
_IpmAgentTrapsReceiversEntry_Object = MibTableRow
ipmAgentTrapsReceiversEntry = _IpmAgentTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7, 1)
)
ipmAgentTrapsReceiversEntry.setIndexNames(
    (0, "IPOMANII-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    ipmAgentTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = IpAddress
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverCommunityString_Type(DisplayString):
    """Custom type receiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ReceiverCommunityString_Type.__name__ = "DisplayString"
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("mandatory")


class _ReceiverNmsType_Type(Integer32):
    """Custom type receiverNmsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPoManII-trap", 2),
          ("none", 1))
    )


_ReceiverNmsType_Type.__name__ = "Integer32"
_ReceiverNmsType_Object = MibTableColumn
receiverNmsType = _ReceiverNmsType_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7, 1, 4),
    _ReceiverNmsType_Type()
)
receiverNmsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverNmsType.setStatus("mandatory")


class _ReceiverSeverityLevel_Type(Integer32):
    """Custom type receiverSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("severe", 3),
          ("warning", 2))
    )


_ReceiverSeverityLevel_Type.__name__ = "Integer32"
_ReceiverSeverityLevel_Object = MibTableColumn
receiverSeverityLevel = _ReceiverSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7, 1, 5),
    _ReceiverSeverityLevel_Type()
)
receiverSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverSeverityLevel.setStatus("mandatory")


class _ReceiverDescription_Type(DisplayString):
    """Custom type receiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReceiverDescription_Type.__name__ = "DisplayString"
_ReceiverDescription_Object = MibTableColumn
receiverDescription = _ReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 7, 1, 6),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_IpmAgentAccessControlTable_Object = MibTable
ipmAgentAccessControlTable = _IpmAgentAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ipmAgentAccessControlTable.setStatus("mandatory")
_IpmAgentAccessControlEntry_Object = MibTableRow
ipmAgentAccessControlEntry = _IpmAgentAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 8, 1)
)
ipmAgentAccessControlEntry.setIndexNames(
    (0, "IPOMANII-MIB", "accessIndex"),
)
if mibBuilder.loadTexts:
    ipmAgentAccessControlEntry.setStatus("mandatory")


class _AccessIndex_Type(Integer32):
    """Custom type accessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccessIndex_Type.__name__ = "Integer32"
_AccessIndex_Object = MibTableColumn
accessIndex = _AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 8, 1, 1),
    _AccessIndex_Type()
)
accessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessIndex.setStatus("mandatory")
_AccessControlAddr_Type = IpAddress
_AccessControlAddr_Object = MibTableColumn
accessControlAddr = _AccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 8, 1, 2),
    _AccessControlAddr_Type()
)
accessControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlAddr.setStatus("mandatory")


class _AccessControlMode_Type(Integer32):
    """Custom type accessControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denied", 2),
          ("permitted", 1))
    )


_AccessControlMode_Type.__name__ = "Integer32"
_AccessControlMode_Object = MibTableColumn
accessControlMode = _AccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 1, 8, 1, 3),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("mandatory")
_IpmAgentTime_ObjectIdentity = ObjectIdentity
ipmAgentTime = _IpmAgentTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 2)
)


class _IpmAgentTimeDate_Type(DisplayString):
    """Custom type ipmAgentTimeDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IpmAgentTimeDate_Type.__name__ = "DisplayString"
_IpmAgentTimeDate_Object = MibScalar
ipmAgentTimeDate = _IpmAgentTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 2, 1),
    _IpmAgentTimeDate_Type()
)
ipmAgentTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTimeDate.setStatus("mandatory")


class _IpmAgentTimeTime_Type(DisplayString):
    """Custom type ipmAgentTimeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IpmAgentTimeTime_Type.__name__ = "DisplayString"
_IpmAgentTimeTime_Object = MibScalar
ipmAgentTimeTime = _IpmAgentTimeTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 2, 2),
    _IpmAgentTimeTime_Type()
)
ipmAgentTimeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTimeTime.setStatus("mandatory")


class _IpmAgentTimerFromNtp_Type(Integer32):
    """Custom type ipmAgentTimerFromNtp based on Integer32"""
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


_IpmAgentTimerFromNtp_Type.__name__ = "Integer32"
_IpmAgentTimerFromNtp_Object = MibScalar
ipmAgentTimerFromNtp = _IpmAgentTimerFromNtp_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 2, 3),
    _IpmAgentTimerFromNtp_Type()
)
ipmAgentTimerFromNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTimerFromNtp.setStatus("mandatory")
_IpmAgentNtpIpAddress_Type = IpAddress
_IpmAgentNtpIpAddress_Object = MibScalar
ipmAgentNtpIpAddress = _IpmAgentNtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 2, 4),
    _IpmAgentNtpIpAddress_Type()
)
ipmAgentNtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNtpIpAddress.setStatus("mandatory")


class _IpmAgentNtpTimeZone_Type(Integer32):
    """Custom type ipmAgentNtpTimeZone based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("gMT-0000", 14),
          ("gMT-0100", 13),
          ("gMT-0200", 12),
          ("gMT-0300", 11),
          ("gMT-0330", 10),
          ("gMT-0400", 9),
          ("gMT-0500", 8),
          ("gMT-0600", 7),
          ("gMT-0700", 6),
          ("gMT-0800", 5),
          ("gMT-0900", 4),
          ("gMT-1000", 3),
          ("gMT-1100", 2),
          ("gMT-1200", 1),
          ("gMT0100", 15),
          ("gMT0200", 16),
          ("gMT0300", 17),
          ("gMT0330", 18),
          ("gMT0400", 19),
          ("gMT0500", 20),
          ("gMT0530", 21),
          ("gMT0600", 22),
          ("gMT0700", 23),
          ("gMT0800", 24),
          ("gMT0900", 25),
          ("gMT1000", 26),
          ("gMT1100", 27),
          ("gMT1200", 28))
    )


_IpmAgentNtpTimeZone_Type.__name__ = "Integer32"
_IpmAgentNtpTimeZone_Object = MibScalar
ipmAgentNtpTimeZone = _IpmAgentNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 2, 5),
    _IpmAgentNtpTimeZone_Type()
)
ipmAgentNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNtpTimeZone.setStatus("mandatory")


class _IpmAgentDayLightSaving_Type(Integer32):
    """Custom type ipmAgentDayLightSaving based on Integer32"""
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


_IpmAgentDayLightSaving_Type.__name__ = "Integer32"
_IpmAgentDayLightSaving_Object = MibScalar
ipmAgentDayLightSaving = _IpmAgentDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 2, 6),
    _IpmAgentDayLightSaving_Type()
)
ipmAgentDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentDayLightSaving.setStatus("mandatory")
_IpmAgentNetwork_ObjectIdentity = ObjectIdentity
ipmAgentNetwork = _IpmAgentNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3)
)
_IpmAgentNetworkIp_ObjectIdentity = ObjectIdentity
ipmAgentNetworkIp = _IpmAgentNetworkIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 1)
)
_IpmAgentNetworkIpAdress_Type = IpAddress
_IpmAgentNetworkIpAdress_Object = MibScalar
ipmAgentNetworkIpAdress = _IpmAgentNetworkIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 1, 1),
    _IpmAgentNetworkIpAdress_Type()
)
ipmAgentNetworkIpAdress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNetworkIpAdress.setStatus("mandatory")
_IpmAgentNetworkIpGateway_Type = IpAddress
_IpmAgentNetworkIpGateway_Object = MibScalar
ipmAgentNetworkIpGateway = _IpmAgentNetworkIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 1, 2),
    _IpmAgentNetworkIpGateway_Type()
)
ipmAgentNetworkIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNetworkIpGateway.setStatus("mandatory")
_IpmAgentNetworkIpSubnet_Type = IpAddress
_IpmAgentNetworkIpSubnet_Object = MibScalar
ipmAgentNetworkIpSubnet = _IpmAgentNetworkIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 1, 3),
    _IpmAgentNetworkIpSubnet_Type()
)
ipmAgentNetworkIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNetworkIpSubnet.setStatus("mandatory")


class _IpmAgentNetworkDhcpControl_Type(Integer32):
    """Custom type ipmAgentNetworkDhcpControl based on Integer32"""
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


_IpmAgentNetworkDhcpControl_Type.__name__ = "Integer32"
_IpmAgentNetworkDhcpControl_Object = MibScalar
ipmAgentNetworkDhcpControl = _IpmAgentNetworkDhcpControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 2),
    _IpmAgentNetworkDhcpControl_Type()
)
ipmAgentNetworkDhcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNetworkDhcpControl.setStatus("mandatory")


class _IpmAgentNetworkPingControl_Type(Integer32):
    """Custom type ipmAgentNetworkPingControl based on Integer32"""
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


_IpmAgentNetworkPingControl_Type.__name__ = "Integer32"
_IpmAgentNetworkPingControl_Object = MibScalar
ipmAgentNetworkPingControl = _IpmAgentNetworkPingControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 3),
    _IpmAgentNetworkPingControl_Type()
)
ipmAgentNetworkPingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNetworkPingControl.setStatus("mandatory")


class _IpmAgentNetworkTftpControl_Type(Integer32):
    """Custom type ipmAgentNetworkTftpControl based on Integer32"""
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


_IpmAgentNetworkTftpControl_Type.__name__ = "Integer32"
_IpmAgentNetworkTftpControl_Object = MibScalar
ipmAgentNetworkTftpControl = _IpmAgentNetworkTftpControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 4),
    _IpmAgentNetworkTftpControl_Type()
)
ipmAgentNetworkTftpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentNetworkTftpControl.setStatus("mandatory")
_IpmAgentNetworkTelnet_ObjectIdentity = ObjectIdentity
ipmAgentNetworkTelnet = _IpmAgentNetworkTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 5)
)


class _IpmAgentTelnetControl_Type(Integer32):
    """Custom type ipmAgentTelnetControl based on Integer32"""
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


_IpmAgentTelnetControl_Type.__name__ = "Integer32"
_IpmAgentTelnetControl_Object = MibScalar
ipmAgentTelnetControl = _IpmAgentTelnetControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 5, 1),
    _IpmAgentTelnetControl_Type()
)
ipmAgentTelnetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTelnetControl.setStatus("mandatory")
_IpmAgentTelnetPort_Type = Integer32
_IpmAgentTelnetPort_Object = MibScalar
ipmAgentTelnetPort = _IpmAgentTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 5, 2),
    _IpmAgentTelnetPort_Type()
)
ipmAgentTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentTelnetPort.setStatus("mandatory")
_IpmAgentNetworkHttp_ObjectIdentity = ObjectIdentity
ipmAgentNetworkHttp = _IpmAgentNetworkHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 6)
)


class _IpmAgentHttpControl_Type(Integer32):
    """Custom type ipmAgentHttpControl based on Integer32"""
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


_IpmAgentHttpControl_Type.__name__ = "Integer32"
_IpmAgentHttpControl_Object = MibScalar
ipmAgentHttpControl = _IpmAgentHttpControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 6, 1),
    _IpmAgentHttpControl_Type()
)
ipmAgentHttpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentHttpControl.setStatus("mandatory")
_IpmAgentHttpPort_Type = Integer32
_IpmAgentHttpPort_Object = MibScalar
ipmAgentHttpPort = _IpmAgentHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 6, 2),
    _IpmAgentHttpPort_Type()
)
ipmAgentHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentHttpPort.setStatus("mandatory")
_IpmAgentNetworkSnmp_ObjectIdentity = ObjectIdentity
ipmAgentNetworkSnmp = _IpmAgentNetworkSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 7)
)


class _IpmAgentSnmpControl_Type(Integer32):
    """Custom type ipmAgentSnmpControl based on Integer32"""
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


_IpmAgentSnmpControl_Type.__name__ = "Integer32"
_IpmAgentSnmpControl_Object = MibScalar
ipmAgentSnmpControl = _IpmAgentSnmpControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 7, 1),
    _IpmAgentSnmpControl_Type()
)
ipmAgentSnmpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentSnmpControl.setStatus("mandatory")
_IpmAgentSnmpPort_Type = Integer32
_IpmAgentSnmpPort_Object = MibScalar
ipmAgentSnmpPort = _IpmAgentSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 2, 3, 7, 2),
    _IpmAgentSnmpPort_Type()
)
ipmAgentSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmAgentSnmpPort.setStatus("mandatory")
_IpmDevice_ObjectIdentity = ObjectIdentity
ipmDevice = _IpmDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3)
)
_IpmDeviceInlet_ObjectIdentity = ObjectIdentity
ipmDeviceInlet = _IpmDeviceInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1)
)
_IpmDeviceInletNumber_Type = Integer32
_IpmDeviceInletNumber_Object = MibScalar
ipmDeviceInletNumber = _IpmDeviceInletNumber_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 1),
    _IpmDeviceInletNumber_Type()
)
ipmDeviceInletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmDeviceInletNumber.setStatus("mandatory")
_IpmDeviceInletConfigTable_Object = MibTable
ipmDeviceInletConfigTable = _IpmDeviceInletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ipmDeviceInletConfigTable.setStatus("mandatory")
_IpmDeviceInletConfigEntry_Object = MibTableRow
ipmDeviceInletConfigEntry = _IpmDeviceInletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1)
)
ipmDeviceInletConfigEntry.setIndexNames(
    (0, "IPOMANII-MIB", "inletConfigIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceInletConfigEntry.setStatus("mandatory")


class _InletConfigIndex_Type(Integer32):
    """Custom type inletConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InletConfigIndex_Type.__name__ = "Integer32"
_InletConfigIndex_Object = MibTableColumn
inletConfigIndex = _InletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 1),
    _InletConfigIndex_Type()
)
inletConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletConfigIndex.setStatus("mandatory")


class _InletConfigDesc_Type(DisplayString):
    """Custom type inletConfigDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InletConfigDesc_Type.__name__ = "DisplayString"
_InletConfigDesc_Object = MibTableColumn
inletConfigDesc = _InletConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 2),
    _InletConfigDesc_Type()
)
inletConfigDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigDesc.setStatus("mandatory")


class _InletConfigVoltageHigh_Type(Integer32):
    """Custom type inletConfigVoltageHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletConfigVoltageHigh_Type.__name__ = "Integer32"
_InletConfigVoltageHigh_Object = MibTableColumn
inletConfigVoltageHigh = _InletConfigVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 3),
    _InletConfigVoltageHigh_Type()
)
inletConfigVoltageHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigVoltageHigh.setStatus("mandatory")


class _InletConfigVoltageHighAction_Type(Integer32):
    """Custom type inletConfigVoltageHighAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("outletsOff", 1))
    )


_InletConfigVoltageHighAction_Type.__name__ = "Integer32"
_InletConfigVoltageHighAction_Object = MibTableColumn
inletConfigVoltageHighAction = _InletConfigVoltageHighAction_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 4),
    _InletConfigVoltageHighAction_Type()
)
inletConfigVoltageHighAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigVoltageHighAction.setStatus("mandatory")


class _InletConfigVoltageLow_Type(Integer32):
    """Custom type inletConfigVoltageLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletConfigVoltageLow_Type.__name__ = "Integer32"
_InletConfigVoltageLow_Object = MibTableColumn
inletConfigVoltageLow = _InletConfigVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 5),
    _InletConfigVoltageLow_Type()
)
inletConfigVoltageLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigVoltageLow.setStatus("mandatory")


class _InletConfigVoltageLowAction_Type(Integer32):
    """Custom type inletConfigVoltageLowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("outletsOff", 1))
    )


_InletConfigVoltageLowAction_Type.__name__ = "Integer32"
_InletConfigVoltageLowAction_Object = MibTableColumn
inletConfigVoltageLowAction = _InletConfigVoltageLowAction_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 6),
    _InletConfigVoltageLowAction_Type()
)
inletConfigVoltageLowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigVoltageLowAction.setStatus("mandatory")


class _InletConfigCurrentHigh_Type(Integer32):
    """Custom type inletConfigCurrentHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_InletConfigCurrentHigh_Type.__name__ = "Integer32"
_InletConfigCurrentHigh_Object = MibTableColumn
inletConfigCurrentHigh = _InletConfigCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 7),
    _InletConfigCurrentHigh_Type()
)
inletConfigCurrentHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigCurrentHigh.setStatus("mandatory")


class _InletConfigCurrentHighAction_Type(Integer32):
    """Custom type inletConfigCurrentHighAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("outletsOff", 1))
    )


_InletConfigCurrentHighAction_Type.__name__ = "Integer32"
_InletConfigCurrentHighAction_Object = MibTableColumn
inletConfigCurrentHighAction = _InletConfigCurrentHighAction_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 8),
    _InletConfigCurrentHighAction_Type()
)
inletConfigCurrentHighAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigCurrentHighAction.setStatus("mandatory")


class _InletConfigFrequencyHigh_Type(Integer32):
    """Custom type inletConfigFrequencyHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletConfigFrequencyHigh_Type.__name__ = "Integer32"
_InletConfigFrequencyHigh_Object = MibTableColumn
inletConfigFrequencyHigh = _InletConfigFrequencyHigh_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 9),
    _InletConfigFrequencyHigh_Type()
)
inletConfigFrequencyHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigFrequencyHigh.setStatus("mandatory")


class _InletConfigfrequencyHighAction_Type(Integer32):
    """Custom type inletConfigfrequencyHighAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("outletsOff", 1))
    )


_InletConfigfrequencyHighAction_Type.__name__ = "Integer32"
_InletConfigfrequencyHighAction_Object = MibTableColumn
inletConfigfrequencyHighAction = _InletConfigfrequencyHighAction_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 10),
    _InletConfigfrequencyHighAction_Type()
)
inletConfigfrequencyHighAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigfrequencyHighAction.setStatus("mandatory")


class _InletConfigFrequencyLow_Type(Integer32):
    """Custom type inletConfigFrequencyLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletConfigFrequencyLow_Type.__name__ = "Integer32"
_InletConfigFrequencyLow_Object = MibTableColumn
inletConfigFrequencyLow = _InletConfigFrequencyLow_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 11),
    _InletConfigFrequencyLow_Type()
)
inletConfigFrequencyLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigFrequencyLow.setStatus("mandatory")


class _InletConfigfrequencyLowAction_Type(Integer32):
    """Custom type inletConfigfrequencyLowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("outletsOff", 1))
    )


_InletConfigfrequencyLowAction_Type.__name__ = "Integer32"
_InletConfigfrequencyLowAction_Object = MibTableColumn
inletConfigfrequencyLowAction = _InletConfigfrequencyLowAction_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 2, 1, 12),
    _InletConfigfrequencyLowAction_Type()
)
inletConfigfrequencyLowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigfrequencyLowAction.setStatus("mandatory")
_IpmDeviceInletStatusTable_Object = MibTable
ipmDeviceInletStatusTable = _IpmDeviceInletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ipmDeviceInletStatusTable.setStatus("mandatory")
_IpmDeviceInletStatusEntry_Object = MibTableRow
ipmDeviceInletStatusEntry = _IpmDeviceInletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3, 1)
)
ipmDeviceInletStatusEntry.setIndexNames(
    (0, "IPOMANII-MIB", "inletStatusIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceInletStatusEntry.setStatus("mandatory")


class _InletStatusIndex_Type(Integer32):
    """Custom type inletStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InletStatusIndex_Type.__name__ = "Integer32"
_InletStatusIndex_Object = MibTableColumn
inletStatusIndex = _InletStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3, 1, 1),
    _InletStatusIndex_Type()
)
inletStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusIndex.setStatus("mandatory")


class _InletStatusVoltage_Type(Integer32):
    """Custom type inletStatusVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletStatusVoltage_Type.__name__ = "Integer32"
_InletStatusVoltage_Object = MibTableColumn
inletStatusVoltage = _InletStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3, 1, 2),
    _InletStatusVoltage_Type()
)
inletStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusVoltage.setStatus("mandatory")


class _InletStatusCurrent_Type(Integer32):
    """Custom type inletStatusCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_InletStatusCurrent_Type.__name__ = "Integer32"
_InletStatusCurrent_Object = MibTableColumn
inletStatusCurrent = _InletStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3, 1, 3),
    _InletStatusCurrent_Type()
)
inletStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusCurrent.setStatus("mandatory")


class _InletStatusFrequency_Type(Integer32):
    """Custom type inletStatusFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletStatusFrequency_Type.__name__ = "Integer32"
_InletStatusFrequency_Object = MibTableColumn
inletStatusFrequency = _InletStatusFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3, 1, 4),
    _InletStatusFrequency_Type()
)
inletStatusFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusFrequency.setStatus("mandatory")


class _InletStatusKwatt_Type(Integer32):
    """Custom type inletStatusKwatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_InletStatusKwatt_Type.__name__ = "Integer32"
_InletStatusKwatt_Object = MibTableColumn
inletStatusKwatt = _InletStatusKwatt_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3, 1, 5),
    _InletStatusKwatt_Type()
)
inletStatusKwatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusKwatt.setStatus("mandatory")


class _InletStatusWH_Type(Integer32):
    """Custom type inletStatusWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletStatusWH_Type.__name__ = "Integer32"
_InletStatusWH_Object = MibTableColumn
inletStatusWH = _InletStatusWH_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 3, 1, 6),
    _InletStatusWH_Type()
)
inletStatusWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusWH.setStatus("mandatory")


class _InletWattReset_Type(Integer32):
    """Custom type inletWattReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inlet1", 2),
          ("inlet2", 3),
          ("none", 1))
    )


_InletWattReset_Type.__name__ = "Integer32"
_InletWattReset_Object = MibScalar
inletWattReset = _InletWattReset_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 1, 4),
    _InletWattReset_Type()
)
inletWattReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletWattReset.setStatus("mandatory")
_IpmDeviceOutlet_ObjectIdentity = ObjectIdentity
ipmDeviceOutlet = _IpmDeviceOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2)
)
_IpmDeviceOutletNumber_Type = Integer32
_IpmDeviceOutletNumber_Object = MibScalar
ipmDeviceOutletNumber = _IpmDeviceOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 1),
    _IpmDeviceOutletNumber_Type()
)
ipmDeviceOutletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmDeviceOutletNumber.setStatus("mandatory")
_IpmDeviceOutletConfigTable_Object = MibTable
ipmDeviceOutletConfigTable = _IpmDeviceOutletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ipmDeviceOutletConfigTable.setStatus("mandatory")
_IpmDeviceOutletConfigEntry_Object = MibTableRow
ipmDeviceOutletConfigEntry = _IpmDeviceOutletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1)
)
ipmDeviceOutletConfigEntry.setIndexNames(
    (0, "IPOMANII-MIB", "inletConfigIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceOutletConfigEntry.setStatus("mandatory")
_OutletConfigIndex_Type = Integer32
_OutletConfigIndex_Object = MibTableColumn
outletConfigIndex = _OutletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1, 1),
    _OutletConfigIndex_Type()
)
outletConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletConfigIndex.setStatus("mandatory")


class _OutletConfigDesc_Type(DisplayString):
    """Custom type outletConfigDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_OutletConfigDesc_Type.__name__ = "DisplayString"
_OutletConfigDesc_Object = MibTableColumn
outletConfigDesc = _OutletConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1, 2),
    _OutletConfigDesc_Type()
)
outletConfigDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigDesc.setStatus("mandatory")


class _OutletConfigLocation_Type(DisplayString):
    """Custom type outletConfigLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_OutletConfigLocation_Type.__name__ = "DisplayString"
_OutletConfigLocation_Object = MibTableColumn
outletConfigLocation = _OutletConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1, 3),
    _OutletConfigLocation_Type()
)
outletConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigLocation.setStatus("mandatory")
_OutletConfigOnDelay_Type = Integer32
_OutletConfigOnDelay_Object = MibTableColumn
outletConfigOnDelay = _OutletConfigOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1, 4),
    _OutletConfigOnDelay_Type()
)
outletConfigOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigOnDelay.setStatus("mandatory")
_OutletConfigOffDelay_Type = Integer32
_OutletConfigOffDelay_Object = MibTableColumn
outletConfigOffDelay = _OutletConfigOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1, 5),
    _OutletConfigOffDelay_Type()
)
outletConfigOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigOffDelay.setStatus("mandatory")


class _OutletConfigCurrentHigh_Type(Integer32):
    """Custom type outletConfigCurrentHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_OutletConfigCurrentHigh_Type.__name__ = "Integer32"
_OutletConfigCurrentHigh_Object = MibTableColumn
outletConfigCurrentHigh = _OutletConfigCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1, 6),
    _OutletConfigCurrentHigh_Type()
)
outletConfigCurrentHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigCurrentHigh.setStatus("mandatory")


class _OutletConfigCurrentHighAction_Type(Integer32):
    """Custom type outletConfigCurrentHighAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("outletOff", 1))
    )


_OutletConfigCurrentHighAction_Type.__name__ = "Integer32"
_OutletConfigCurrentHighAction_Object = MibTableColumn
outletConfigCurrentHighAction = _OutletConfigCurrentHighAction_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 2, 1, 7),
    _OutletConfigCurrentHighAction_Type()
)
outletConfigCurrentHighAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigCurrentHighAction.setStatus("mandatory")
_IpmDeviceOutletStatusTable_Object = MibTable
ipmDeviceOutletStatusTable = _IpmDeviceOutletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ipmDeviceOutletStatusTable.setStatus("mandatory")
_IpmDeviceOutletStatusEntry_Object = MibTableRow
ipmDeviceOutletStatusEntry = _IpmDeviceOutletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1)
)
ipmDeviceOutletStatusEntry.setIndexNames(
    (0, "IPOMANII-MIB", "outletStatusIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceOutletStatusEntry.setStatus("mandatory")


class _OutletStatusIndex_Type(Integer32):
    """Custom type outletStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OutletStatusIndex_Type.__name__ = "Integer32"
_OutletStatusIndex_Object = MibTableColumn
outletStatusIndex = _OutletStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1, 1),
    _OutletStatusIndex_Type()
)
outletStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusIndex.setStatus("mandatory")


class _OutletStatusStatus_Type(Integer32):
    """Custom type outletStatusStatus based on Integer32"""
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
        *(("outletCycling", 6),
          ("outletOff", 2),
          ("outletOffToOn", 4),
          ("outletOn", 3),
          ("outletOnToOff", 5),
          ("unknow", 1))
    )


_OutletStatusStatus_Type.__name__ = "Integer32"
_OutletStatusStatus_Object = MibTableColumn
outletStatusStatus = _OutletStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1, 2),
    _OutletStatusStatus_Type()
)
outletStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusStatus.setStatus("mandatory")


class _OutletStatusCurrent_Type(Integer32):
    """Custom type outletStatusCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_OutletStatusCurrent_Type.__name__ = "Integer32"
_OutletStatusCurrent_Object = MibTableColumn
outletStatusCurrent = _OutletStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1, 3),
    _OutletStatusCurrent_Type()
)
outletStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusCurrent.setStatus("mandatory")


class _OutletStatusKwatt_Type(Integer32):
    """Custom type outletStatusKwatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_OutletStatusKwatt_Type.__name__ = "Integer32"
_OutletStatusKwatt_Object = MibTableColumn
outletStatusKwatt = _OutletStatusKwatt_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1, 4),
    _OutletStatusKwatt_Type()
)
outletStatusKwatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusKwatt.setStatus("mandatory")


class _OutletStatusWH_Type(Integer32):
    """Custom type outletStatusWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_OutletStatusWH_Type.__name__ = "Integer32"
_OutletStatusWH_Object = MibTableColumn
outletStatusWH = _OutletStatusWH_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1, 5),
    _OutletStatusWH_Type()
)
outletStatusWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusWH.setStatus("mandatory")
_OutletStatusStateTime_Type = Integer32
_OutletStatusStateTime_Object = MibTableColumn
outletStatusStateTime = _OutletStatusStateTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1, 6),
    _OutletStatusStateTime_Type()
)
outletStatusStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusStateTime.setStatus("mandatory")
_OutletStatusTimeToGo_Type = Integer32
_OutletStatusTimeToGo_Object = MibTableColumn
outletStatusTimeToGo = _OutletStatusTimeToGo_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 3, 1, 7),
    _OutletStatusTimeToGo_Type()
)
outletStatusTimeToGo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusTimeToGo.setStatus("mandatory")
_IpmDeviceOutletControlTable_Object = MibTable
ipmDeviceOutletControlTable = _IpmDeviceOutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    ipmDeviceOutletControlTable.setStatus("mandatory")
_IpmDeviceOutletControlEntry_Object = MibTableRow
ipmDeviceOutletControlEntry = _IpmDeviceOutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 4, 1)
)
ipmDeviceOutletControlEntry.setIndexNames(
    (0, "IPOMANII-MIB", "outletControlIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceOutletControlEntry.setStatus("mandatory")


class _OutletControlIndex_Type(Integer32):
    """Custom type outletControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OutletControlIndex_Type.__name__ = "Integer32"
_OutletControlIndex_Object = MibTableColumn
outletControlIndex = _OutletControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 4, 1, 1),
    _OutletControlIndex_Type()
)
outletControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletControlIndex.setStatus("mandatory")


class _OutletControlControl_Type(Integer32):
    """Custom type outletControlControl based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_OutletControlControl_Type.__name__ = "Integer32"
_OutletControlControl_Object = MibTableColumn
outletControlControl = _OutletControlControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 4, 1, 2),
    _OutletControlControl_Type()
)
outletControlControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlControl.setStatus("mandatory")


class _IpmDeviceOutletControlAll_Type(Integer32):
    """Custom type ipmDeviceOutletControlAll based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimers", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimers", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimers", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_IpmDeviceOutletControlAll_Type.__name__ = "Integer32"
_IpmDeviceOutletControlAll_Object = MibScalar
ipmDeviceOutletControlAll = _IpmDeviceOutletControlAll_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 5),
    _IpmDeviceOutletControlAll_Type()
)
ipmDeviceOutletControlAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmDeviceOutletControlAll.setStatus("mandatory")


class _IpmDeviceOutletWattReset_Type(Integer32):
    """Custom type ipmDeviceOutletWattReset based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("outleta", 2),
          ("outletb", 3),
          ("outletc", 4),
          ("outletd", 5),
          ("outlete", 6),
          ("outletf", 7),
          ("outletg", 8),
          ("outleth", 9),
          ("outleti", 10),
          ("outletj", 11),
          ("outletk", 12),
          ("outletl", 13))
    )


_IpmDeviceOutletWattReset_Type.__name__ = "Integer32"
_IpmDeviceOutletWattReset_Object = MibScalar
ipmDeviceOutletWattReset = _IpmDeviceOutletWattReset_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 2, 6),
    _IpmDeviceOutletWattReset_Type()
)
ipmDeviceOutletWattReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmDeviceOutletWattReset.setStatus("mandatory")
_IpmDeviceCcOut_ObjectIdentity = ObjectIdentity
ipmDeviceCcOut = _IpmDeviceCcOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3)
)
_IpmDeviceCcOutNumber_Type = Integer32
_IpmDeviceCcOutNumber_Object = MibScalar
ipmDeviceCcOutNumber = _IpmDeviceCcOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 1),
    _IpmDeviceCcOutNumber_Type()
)
ipmDeviceCcOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmDeviceCcOutNumber.setStatus("mandatory")
_IpmDeviceCcOutConfigTable_Object = MibTable
ipmDeviceCcOutConfigTable = _IpmDeviceCcOutConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ipmDeviceCcOutConfigTable.setStatus("mandatory")
_IpmDeviceCcOutConfigEntry_Object = MibTableRow
ipmDeviceCcOutConfigEntry = _IpmDeviceCcOutConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 2, 1)
)
ipmDeviceCcOutConfigEntry.setIndexNames(
    (0, "IPOMANII-MIB", "ccOutConfigIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceCcOutConfigEntry.setStatus("mandatory")


class _CcOutConfigIndex_Type(Integer32):
    """Custom type ccOutConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcOutConfigIndex_Type.__name__ = "Integer32"
_CcOutConfigIndex_Object = MibTableColumn
ccOutConfigIndex = _CcOutConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 2, 1, 1),
    _CcOutConfigIndex_Type()
)
ccOutConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccOutConfigIndex.setStatus("mandatory")


class _CcOutConfigDesc_Type(DisplayString):
    """Custom type ccOutConfigDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CcOutConfigDesc_Type.__name__ = "DisplayString"
_CcOutConfigDesc_Object = MibTableColumn
ccOutConfigDesc = _CcOutConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 2, 1, 2),
    _CcOutConfigDesc_Type()
)
ccOutConfigDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutConfigDesc.setStatus("mandatory")


class _CcOutConfigEventAction_Type(Integer32):
    """Custom type ccOutConfigEventAction based on Integer32"""
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


_CcOutConfigEventAction_Type.__name__ = "Integer32"
_CcOutConfigEventAction_Object = MibTableColumn
ccOutConfigEventAction = _CcOutConfigEventAction_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 2, 1, 3),
    _CcOutConfigEventAction_Type()
)
ccOutConfigEventAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutConfigEventAction.setStatus("mandatory")
_CcOutConfigCloseDelay_Type = Integer32
_CcOutConfigCloseDelay_Object = MibTableColumn
ccOutConfigCloseDelay = _CcOutConfigCloseDelay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 2, 1, 4),
    _CcOutConfigCloseDelay_Type()
)
ccOutConfigCloseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutConfigCloseDelay.setStatus("mandatory")
_CcOutConfigOpenDelay_Type = Integer32
_CcOutConfigOpenDelay_Object = MibTableColumn
ccOutConfigOpenDelay = _CcOutConfigOpenDelay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 2, 1, 5),
    _CcOutConfigOpenDelay_Type()
)
ccOutConfigOpenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutConfigOpenDelay.setStatus("mandatory")
_IpmDeviceCcOutStatusTable_Object = MibTable
ipmDeviceCcOutStatusTable = _IpmDeviceCcOutStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    ipmDeviceCcOutStatusTable.setStatus("mandatory")
_IpmDeviceCcOutStatusEntry_Object = MibTableRow
ipmDeviceCcOutStatusEntry = _IpmDeviceCcOutStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 3, 1)
)
ipmDeviceCcOutStatusEntry.setIndexNames(
    (0, "IPOMANII-MIB", "ccOutStatusIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceCcOutStatusEntry.setStatus("mandatory")


class _CcOutStatusIndex_Type(Integer32):
    """Custom type ccOutStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcOutStatusIndex_Type.__name__ = "Integer32"
_CcOutStatusIndex_Object = MibTableColumn
ccOutStatusIndex = _CcOutStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 3, 1, 1),
    _CcOutStatusIndex_Type()
)
ccOutStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccOutStatusIndex.setStatus("mandatory")


class _CcOutStatusStatus_Type(Integer32):
    """Custom type ccOutStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2))
    )


_CcOutStatusStatus_Type.__name__ = "Integer32"
_CcOutStatusStatus_Object = MibTableColumn
ccOutStatusStatus = _CcOutStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 3, 1, 2),
    _CcOutStatusStatus_Type()
)
ccOutStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccOutStatusStatus.setStatus("mandatory")
_CcOutStatusTimeOnState_Type = Integer32
_CcOutStatusTimeOnState_Object = MibTableColumn
ccOutStatusTimeOnState = _CcOutStatusTimeOnState_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 3, 1, 3),
    _CcOutStatusTimeOnState_Type()
)
ccOutStatusTimeOnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccOutStatusTimeOnState.setStatus("mandatory")
_IpmDeviceCcOutControlTable_Object = MibTable
ipmDeviceCcOutControlTable = _IpmDeviceCcOutControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    ipmDeviceCcOutControlTable.setStatus("mandatory")
_IpmDeviceCcOutControlEntry_Object = MibTableRow
ipmDeviceCcOutControlEntry = _IpmDeviceCcOutControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 4, 1)
)
ipmDeviceCcOutControlEntry.setIndexNames(
    (0, "IPOMANII-MIB", "ccOutControlIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceCcOutControlEntry.setStatus("mandatory")


class _CcOutControlIndex_Type(Integer32):
    """Custom type ccOutControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcOutControlIndex_Type.__name__ = "Integer32"
_CcOutControlIndex_Object = MibTableColumn
ccOutControlIndex = _CcOutControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 4, 1, 1),
    _CcOutControlIndex_Type()
)
ccOutControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccOutControlIndex.setStatus("mandatory")


class _CcOutControlControl_Type(Integer32):
    """Custom type ccOutControlControl based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("closeByCloseTimer", 6),
          ("closeImmediately", 3),
          ("closeThenOpenByActionTimers", 9),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("openByOpenTimer", 7),
          ("openImmediately", 4),
          ("openThenCloseByActionTimers", 10))
    )


_CcOutControlControl_Type.__name__ = "Integer32"
_CcOutControlControl_Object = MibTableColumn
ccOutControlControl = _CcOutControlControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 3, 3, 4, 1, 2),
    _CcOutControlControl_Type()
)
ccOutControlControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutControlControl.setStatus("mandatory")
_IpmSlave_ObjectIdentity = ObjectIdentity
ipmSlave = _IpmSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4)
)
_IpmSlaveState_ObjectIdentity = ObjectIdentity
ipmSlaveState = _IpmSlaveState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 1)
)
_IpmSlaveStateTable_Object = MibTable
ipmSlaveStateTable = _IpmSlaveStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ipmSlaveStateTable.setStatus("mandatory")
_IpmSlaveStateEntry_Object = MibTableRow
ipmSlaveStateEntry = _IpmSlaveStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 1, 1, 1)
)
ipmSlaveStateEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveStateIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveStateEntry.setStatus("mandatory")


class _SlaveStateIndex_Type(Integer32):
    """Custom type slaveStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveStateIndex_Type.__name__ = "Integer32"
_SlaveStateIndex_Object = MibTableColumn
slaveStateIndex = _SlaveStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 1, 1, 1, 1),
    _SlaveStateIndex_Type()
)
slaveStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveStateIndex.setStatus("mandatory")


class _SlaveStateControl01_Type(Integer32):
    """Custom type slaveStateControl01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )


_SlaveStateControl01_Type.__name__ = "Integer32"
_SlaveStateControl01_Object = MibTableColumn
slaveStateControl01 = _SlaveStateControl01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 1, 1, 1, 2),
    _SlaveStateControl01_Type()
)
slaveStateControl01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveStateControl01.setStatus("mandatory")
_IpmSlaveInlet_ObjectIdentity = ObjectIdentity
ipmSlaveInlet = _IpmSlaveInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2)
)
_IpmSlaveInletStatus_ObjectIdentity = ObjectIdentity
ipmSlaveInletStatus = _IpmSlaveInletStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1)
)
_IpmDeviceSlaveInletStatusTable_Object = MibTable
ipmDeviceSlaveInletStatusTable = _IpmDeviceSlaveInletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipmDeviceSlaveInletStatusTable.setStatus("mandatory")
_IpmDeviceSlaveInletStatusEntry_Object = MibTableRow
ipmDeviceSlaveInletStatusEntry = _IpmDeviceSlaveInletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1)
)
ipmDeviceSlaveInletStatusEntry.setIndexNames(
    (0, "IPOMANII-MIB", "inletStatusIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceSlaveInletStatusEntry.setStatus("mandatory")


class _InletSlaveStatusIndex_Type(Integer32):
    """Custom type inletSlaveStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InletSlaveStatusIndex_Type.__name__ = "Integer32"
_InletSlaveStatusIndex_Object = MibTableColumn
inletSlaveStatusIndex = _InletSlaveStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 1),
    _InletSlaveStatusIndex_Type()
)
inletSlaveStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusIndex.setStatus("mandatory")


class _InletSlaveStatusVoltage_Type(Integer32):
    """Custom type inletSlaveStatusVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletSlaveStatusVoltage_Type.__name__ = "Integer32"
_InletSlaveStatusVoltage_Object = MibTableColumn
inletSlaveStatusVoltage = _InletSlaveStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 2),
    _InletSlaveStatusVoltage_Type()
)
inletSlaveStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusVoltage.setStatus("mandatory")


class _InletSlaveStatusCurrent_Type(Integer32):
    """Custom type inletSlaveStatusCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_InletSlaveStatusCurrent_Type.__name__ = "Integer32"
_InletSlaveStatusCurrent_Object = MibTableColumn
inletSlaveStatusCurrent = _InletSlaveStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 3),
    _InletSlaveStatusCurrent_Type()
)
inletSlaveStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusCurrent.setStatus("mandatory")


class _InletSlaveStatusFrequency_Type(Integer32):
    """Custom type inletSlaveStatusFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletSlaveStatusFrequency_Type.__name__ = "Integer32"
_InletSlaveStatusFrequency_Object = MibTableColumn
inletSlaveStatusFrequency = _InletSlaveStatusFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 4),
    _InletSlaveStatusFrequency_Type()
)
inletSlaveStatusFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusFrequency.setStatus("mandatory")


class _InletSlaveStatusKwatt_Type(Integer32):
    """Custom type inletSlaveStatusKwatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_InletSlaveStatusKwatt_Type.__name__ = "Integer32"
_InletSlaveStatusKwatt_Object = MibTableColumn
inletSlaveStatusKwatt = _InletSlaveStatusKwatt_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 5),
    _InletSlaveStatusKwatt_Type()
)
inletSlaveStatusKwatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusKwatt.setStatus("mandatory")


class _InletSlaveStatusWH_Type(Integer32):
    """Custom type inletSlaveStatusWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletSlaveStatusWH_Type.__name__ = "Integer32"
_InletSlaveStatusWH_Object = MibTableColumn
inletSlaveStatusWH = _InletSlaveStatusWH_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 6),
    _InletSlaveStatusWH_Type()
)
inletSlaveStatusWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusWH.setStatus("mandatory")


class _InletSlaveStatusVoltage2_Type(Integer32):
    """Custom type inletSlaveStatusVoltage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletSlaveStatusVoltage2_Type.__name__ = "Integer32"
_InletSlaveStatusVoltage2_Object = MibTableColumn
inletSlaveStatusVoltage2 = _InletSlaveStatusVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 7),
    _InletSlaveStatusVoltage2_Type()
)
inletSlaveStatusVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusVoltage2.setStatus("mandatory")


class _InletSlaveStatusCurrent2_Type(Integer32):
    """Custom type inletSlaveStatusCurrent2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_InletSlaveStatusCurrent2_Type.__name__ = "Integer32"
_InletSlaveStatusCurrent2_Object = MibTableColumn
inletSlaveStatusCurrent2 = _InletSlaveStatusCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 8),
    _InletSlaveStatusCurrent2_Type()
)
inletSlaveStatusCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusCurrent2.setStatus("mandatory")


class _InletSlaveStatusFrequency2_Type(Integer32):
    """Custom type inletSlaveStatusFrequency2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletSlaveStatusFrequency2_Type.__name__ = "Integer32"
_InletSlaveStatusFrequency2_Object = MibTableColumn
inletSlaveStatusFrequency2 = _InletSlaveStatusFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 9),
    _InletSlaveStatusFrequency2_Type()
)
inletSlaveStatusFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusFrequency2.setStatus("mandatory")


class _InletSlaveStatusKwatt2_Type(Integer32):
    """Custom type inletSlaveStatusKwatt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_InletSlaveStatusKwatt2_Type.__name__ = "Integer32"
_InletSlaveStatusKwatt2_Object = MibTableColumn
inletSlaveStatusKwatt2 = _InletSlaveStatusKwatt2_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 10),
    _InletSlaveStatusKwatt2_Type()
)
inletSlaveStatusKwatt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusKwatt2.setStatus("mandatory")


class _InletSlaveStatusWH2_Type(Integer32):
    """Custom type inletSlaveStatusWH2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_InletSlaveStatusWH2_Type.__name__ = "Integer32"
_InletSlaveStatusWH2_Object = MibTableColumn
inletSlaveStatusWH2 = _InletSlaveStatusWH2_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 1, 1, 1, 11),
    _InletSlaveStatusWH2_Type()
)
inletSlaveStatusWH2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusWH2.setStatus("mandatory")
_IpmSlaveInletConfig_ObjectIdentity = ObjectIdentity
ipmSlaveInletConfig = _IpmSlaveInletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2)
)
_IpmDeviceslaveInletConfigTable_Object = MibTable
ipmDeviceslaveInletConfigTable = _IpmDeviceslaveInletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipmDeviceslaveInletConfigTable.setStatus("mandatory")
_IpmDeviceslaveInletConfigEntry_Object = MibTableRow
ipmDeviceslaveInletConfigEntry = _IpmDeviceslaveInletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2, 1, 1)
)
ipmDeviceslaveInletConfigEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveInletConfigIndex"),
)
if mibBuilder.loadTexts:
    ipmDeviceslaveInletConfigEntry.setStatus("mandatory")


class _SlaveInletConfigIndex_Type(Integer32):
    """Custom type slaveInletConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveInletConfigIndex_Type.__name__ = "Integer32"
_SlaveInletConfigIndex_Object = MibTableColumn
slaveInletConfigIndex = _SlaveInletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2, 1, 1, 1),
    _SlaveInletConfigIndex_Type()
)
slaveInletConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveInletConfigIndex.setStatus("mandatory")


class _SlaveInletConfigVoltageHigh_Type(Integer32):
    """Custom type slaveInletConfigVoltageHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_SlaveInletConfigVoltageHigh_Type.__name__ = "Integer32"
_SlaveInletConfigVoltageHigh_Object = MibTableColumn
slaveInletConfigVoltageHigh = _SlaveInletConfigVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2, 1, 1, 2),
    _SlaveInletConfigVoltageHigh_Type()
)
slaveInletConfigVoltageHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveInletConfigVoltageHigh.setStatus("mandatory")


class _SlaveInletConfigVoltageLow_Type(Integer32):
    """Custom type slaveInletConfigVoltageLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_SlaveInletConfigVoltageLow_Type.__name__ = "Integer32"
_SlaveInletConfigVoltageLow_Object = MibTableColumn
slaveInletConfigVoltageLow = _SlaveInletConfigVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2, 1, 1, 3),
    _SlaveInletConfigVoltageLow_Type()
)
slaveInletConfigVoltageLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveInletConfigVoltageLow.setStatus("mandatory")


class _SlaveInlet2ConfigVoltageHigh_Type(Integer32):
    """Custom type slaveInlet2ConfigVoltageHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_SlaveInlet2ConfigVoltageHigh_Type.__name__ = "Integer32"
_SlaveInlet2ConfigVoltageHigh_Object = MibTableColumn
slaveInlet2ConfigVoltageHigh = _SlaveInlet2ConfigVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2, 1, 1, 4),
    _SlaveInlet2ConfigVoltageHigh_Type()
)
slaveInlet2ConfigVoltageHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveInlet2ConfigVoltageHigh.setStatus("mandatory")


class _SlaveInlet2ConfigVoltageLow_Type(Integer32):
    """Custom type slaveInlet2ConfigVoltageLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_SlaveInlet2ConfigVoltageLow_Type.__name__ = "Integer32"
_SlaveInlet2ConfigVoltageLow_Object = MibTableColumn
slaveInlet2ConfigVoltageLow = _SlaveInlet2ConfigVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 2, 2, 1, 1, 5),
    _SlaveInlet2ConfigVoltageLow_Type()
)
slaveInlet2ConfigVoltageLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveInlet2ConfigVoltageLow.setStatus("mandatory")
_IpmSlaveOutlet_ObjectIdentity = ObjectIdentity
ipmSlaveOutlet = _IpmSlaveOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3)
)
_IpmSlaveOutletConfig_ObjectIdentity = ObjectIdentity
ipmSlaveOutletConfig = _IpmSlaveOutletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1)
)
_IpmSlaveDeviceOutletNameTable_Object = MibTable
ipmSlaveDeviceOutletNameTable = _IpmSlaveDeviceOutletNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletNameTable.setStatus("mandatory")
_IpmSlaveDeviceOutletNameEntry_Object = MibTableRow
ipmSlaveDeviceOutletNameEntry = _IpmSlaveDeviceOutletNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1)
)
ipmSlaveDeviceOutletNameEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletNameIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletNameEntry.setStatus("mandatory")


class _SlaveOutletNameIndex_Type(Integer32):
    """Custom type slaveOutletNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletNameIndex_Type.__name__ = "Integer32"
_SlaveOutletNameIndex_Object = MibTableColumn
slaveOutletNameIndex = _SlaveOutletNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 1),
    _SlaveOutletNameIndex_Type()
)
slaveOutletNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletNameIndex.setStatus("mandatory")


class _SlaveOutletName01_Type(DisplayString):
    """Custom type slaveOutletName01 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName01_Type.__name__ = "DisplayString"
_SlaveOutletName01_Object = MibTableColumn
slaveOutletName01 = _SlaveOutletName01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 2),
    _SlaveOutletName01_Type()
)
slaveOutletName01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName01.setStatus("mandatory")


class _SlaveOutletName02_Type(DisplayString):
    """Custom type slaveOutletName02 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName02_Type.__name__ = "DisplayString"
_SlaveOutletName02_Object = MibTableColumn
slaveOutletName02 = _SlaveOutletName02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 3),
    _SlaveOutletName02_Type()
)
slaveOutletName02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName02.setStatus("mandatory")


class _SlaveOutletName03_Type(DisplayString):
    """Custom type slaveOutletName03 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName03_Type.__name__ = "DisplayString"
_SlaveOutletName03_Object = MibTableColumn
slaveOutletName03 = _SlaveOutletName03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 4),
    _SlaveOutletName03_Type()
)
slaveOutletName03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName03.setStatus("mandatory")


class _SlaveOutletName04_Type(DisplayString):
    """Custom type slaveOutletName04 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName04_Type.__name__ = "DisplayString"
_SlaveOutletName04_Object = MibTableColumn
slaveOutletName04 = _SlaveOutletName04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 5),
    _SlaveOutletName04_Type()
)
slaveOutletName04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName04.setStatus("mandatory")


class _SlaveOutletName05_Type(DisplayString):
    """Custom type slaveOutletName05 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName05_Type.__name__ = "DisplayString"
_SlaveOutletName05_Object = MibTableColumn
slaveOutletName05 = _SlaveOutletName05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 6),
    _SlaveOutletName05_Type()
)
slaveOutletName05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName05.setStatus("mandatory")


class _SlaveOutletName06_Type(DisplayString):
    """Custom type slaveOutletName06 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName06_Type.__name__ = "DisplayString"
_SlaveOutletName06_Object = MibTableColumn
slaveOutletName06 = _SlaveOutletName06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 7),
    _SlaveOutletName06_Type()
)
slaveOutletName06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName06.setStatus("mandatory")


class _SlaveOutletName07_Type(DisplayString):
    """Custom type slaveOutletName07 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName07_Type.__name__ = "DisplayString"
_SlaveOutletName07_Object = MibTableColumn
slaveOutletName07 = _SlaveOutletName07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 8),
    _SlaveOutletName07_Type()
)
slaveOutletName07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName07.setStatus("mandatory")


class _SlaveOutletName08_Type(DisplayString):
    """Custom type slaveOutletName08 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName08_Type.__name__ = "DisplayString"
_SlaveOutletName08_Object = MibTableColumn
slaveOutletName08 = _SlaveOutletName08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 9),
    _SlaveOutletName08_Type()
)
slaveOutletName08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName08.setStatus("mandatory")


class _SlaveOutletName09_Type(DisplayString):
    """Custom type slaveOutletName09 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName09_Type.__name__ = "DisplayString"
_SlaveOutletName09_Object = MibTableColumn
slaveOutletName09 = _SlaveOutletName09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 10),
    _SlaveOutletName09_Type()
)
slaveOutletName09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName09.setStatus("mandatory")


class _SlaveOutletName10_Type(DisplayString):
    """Custom type slaveOutletName10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName10_Type.__name__ = "DisplayString"
_SlaveOutletName10_Object = MibTableColumn
slaveOutletName10 = _SlaveOutletName10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 11),
    _SlaveOutletName10_Type()
)
slaveOutletName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName10.setStatus("mandatory")


class _SlaveOutletName11_Type(DisplayString):
    """Custom type slaveOutletName11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName11_Type.__name__ = "DisplayString"
_SlaveOutletName11_Object = MibTableColumn
slaveOutletName11 = _SlaveOutletName11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 12),
    _SlaveOutletName11_Type()
)
slaveOutletName11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName11.setStatus("mandatory")


class _SlaveOutletName12_Type(DisplayString):
    """Custom type slaveOutletName12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletName12_Type.__name__ = "DisplayString"
_SlaveOutletName12_Object = MibTableColumn
slaveOutletName12 = _SlaveOutletName12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 1, 1, 13),
    _SlaveOutletName12_Type()
)
slaveOutletName12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName12.setStatus("mandatory")
_IpmSlaveDeviceOutletLocationTable_Object = MibTable
ipmSlaveDeviceOutletLocationTable = _IpmSlaveDeviceOutletLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletLocationTable.setStatus("mandatory")
_IpmSlaveDeviceOutletLocationEntry_Object = MibTableRow
ipmSlaveDeviceOutletLocationEntry = _IpmSlaveDeviceOutletLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1)
)
ipmSlaveDeviceOutletLocationEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletLocationIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletLocationEntry.setStatus("mandatory")


class _SlaveOutletLocationIndex_Type(Integer32):
    """Custom type slaveOutletLocationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletLocationIndex_Type.__name__ = "Integer32"
_SlaveOutletLocationIndex_Object = MibTableColumn
slaveOutletLocationIndex = _SlaveOutletLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 1),
    _SlaveOutletLocationIndex_Type()
)
slaveOutletLocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletLocationIndex.setStatus("mandatory")


class _SlaveOutletLocation01_Type(DisplayString):
    """Custom type slaveOutletLocation01 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation01_Type.__name__ = "DisplayString"
_SlaveOutletLocation01_Object = MibTableColumn
slaveOutletLocation01 = _SlaveOutletLocation01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 2),
    _SlaveOutletLocation01_Type()
)
slaveOutletLocation01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation01.setStatus("mandatory")


class _SlaveOutletLocation02_Type(DisplayString):
    """Custom type slaveOutletLocation02 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation02_Type.__name__ = "DisplayString"
_SlaveOutletLocation02_Object = MibTableColumn
slaveOutletLocation02 = _SlaveOutletLocation02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 3),
    _SlaveOutletLocation02_Type()
)
slaveOutletLocation02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation02.setStatus("mandatory")


class _SlaveOutletLocation03_Type(DisplayString):
    """Custom type slaveOutletLocation03 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation03_Type.__name__ = "DisplayString"
_SlaveOutletLocation03_Object = MibTableColumn
slaveOutletLocation03 = _SlaveOutletLocation03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 4),
    _SlaveOutletLocation03_Type()
)
slaveOutletLocation03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation03.setStatus("mandatory")


class _SlaveOutletLocation04_Type(DisplayString):
    """Custom type slaveOutletLocation04 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation04_Type.__name__ = "DisplayString"
_SlaveOutletLocation04_Object = MibTableColumn
slaveOutletLocation04 = _SlaveOutletLocation04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 5),
    _SlaveOutletLocation04_Type()
)
slaveOutletLocation04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation04.setStatus("mandatory")


class _SlaveOutletLocation05_Type(DisplayString):
    """Custom type slaveOutletLocation05 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation05_Type.__name__ = "DisplayString"
_SlaveOutletLocation05_Object = MibTableColumn
slaveOutletLocation05 = _SlaveOutletLocation05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 6),
    _SlaveOutletLocation05_Type()
)
slaveOutletLocation05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation05.setStatus("mandatory")


class _SlaveOutletLocation06_Type(DisplayString):
    """Custom type slaveOutletLocation06 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation06_Type.__name__ = "DisplayString"
_SlaveOutletLocation06_Object = MibTableColumn
slaveOutletLocation06 = _SlaveOutletLocation06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 7),
    _SlaveOutletLocation06_Type()
)
slaveOutletLocation06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation06.setStatus("mandatory")


class _SlaveOutletLocation07_Type(DisplayString):
    """Custom type slaveOutletLocation07 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation07_Type.__name__ = "DisplayString"
_SlaveOutletLocation07_Object = MibTableColumn
slaveOutletLocation07 = _SlaveOutletLocation07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 8),
    _SlaveOutletLocation07_Type()
)
slaveOutletLocation07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation07.setStatus("mandatory")


class _SlaveOutletLocation08_Type(DisplayString):
    """Custom type slaveOutletLocation08 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation08_Type.__name__ = "DisplayString"
_SlaveOutletLocation08_Object = MibTableColumn
slaveOutletLocation08 = _SlaveOutletLocation08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 9),
    _SlaveOutletLocation08_Type()
)
slaveOutletLocation08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation08.setStatus("mandatory")


class _SlaveOutletLocation09_Type(DisplayString):
    """Custom type slaveOutletLocation09 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation09_Type.__name__ = "DisplayString"
_SlaveOutletLocation09_Object = MibTableColumn
slaveOutletLocation09 = _SlaveOutletLocation09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 10),
    _SlaveOutletLocation09_Type()
)
slaveOutletLocation09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation09.setStatus("mandatory")


class _SlaveOutletLocation10_Type(DisplayString):
    """Custom type slaveOutletLocation10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation10_Type.__name__ = "DisplayString"
_SlaveOutletLocation10_Object = MibTableColumn
slaveOutletLocation10 = _SlaveOutletLocation10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 11),
    _SlaveOutletLocation10_Type()
)
slaveOutletLocation10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation10.setStatus("mandatory")


class _SlaveOutletLocation11_Type(DisplayString):
    """Custom type slaveOutletLocation11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation11_Type.__name__ = "DisplayString"
_SlaveOutletLocation11_Object = MibTableColumn
slaveOutletLocation11 = _SlaveOutletLocation11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 12),
    _SlaveOutletLocation11_Type()
)
slaveOutletLocation11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation11.setStatus("mandatory")


class _SlaveOutletLocation12_Type(DisplayString):
    """Custom type slaveOutletLocation12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlaveOutletLocation12_Type.__name__ = "DisplayString"
_SlaveOutletLocation12_Object = MibTableColumn
slaveOutletLocation12 = _SlaveOutletLocation12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 2, 1, 13),
    _SlaveOutletLocation12_Type()
)
slaveOutletLocation12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation12.setStatus("mandatory")
_IpmSlaveDeviceOutletOnTimeTable_Object = MibTable
ipmSlaveDeviceOutletOnTimeTable = _IpmSlaveDeviceOutletOnTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletOnTimeTable.setStatus("mandatory")
_IpmSlaveDeviceOutletOnTimeEntry_Object = MibTableRow
ipmSlaveDeviceOutletOnTimeEntry = _IpmSlaveDeviceOutletOnTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1)
)
ipmSlaveDeviceOutletOnTimeEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletOnTimeIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletOnTimeEntry.setStatus("mandatory")


class _SlaveOutletOnTimeIndex_Type(Integer32):
    """Custom type slaveOutletOnTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletOnTimeIndex_Type.__name__ = "Integer32"
_SlaveOutletOnTimeIndex_Object = MibTableColumn
slaveOutletOnTimeIndex = _SlaveOutletOnTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 1),
    _SlaveOutletOnTimeIndex_Type()
)
slaveOutletOnTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletOnTimeIndex.setStatus("mandatory")
_SlaveOutletOnTime01_Type = Integer32
_SlaveOutletOnTime01_Object = MibTableColumn
slaveOutletOnTime01 = _SlaveOutletOnTime01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 2),
    _SlaveOutletOnTime01_Type()
)
slaveOutletOnTime01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime01.setStatus("mandatory")
_SlaveOutletOnTime02_Type = Integer32
_SlaveOutletOnTime02_Object = MibTableColumn
slaveOutletOnTime02 = _SlaveOutletOnTime02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 3),
    _SlaveOutletOnTime02_Type()
)
slaveOutletOnTime02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime02.setStatus("mandatory")
_SlaveOutletOnTime03_Type = Integer32
_SlaveOutletOnTime03_Object = MibTableColumn
slaveOutletOnTime03 = _SlaveOutletOnTime03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 4),
    _SlaveOutletOnTime03_Type()
)
slaveOutletOnTime03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime03.setStatus("mandatory")
_SlaveOutletOnTime04_Type = Integer32
_SlaveOutletOnTime04_Object = MibTableColumn
slaveOutletOnTime04 = _SlaveOutletOnTime04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 5),
    _SlaveOutletOnTime04_Type()
)
slaveOutletOnTime04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime04.setStatus("mandatory")
_SlaveOutletOnTime05_Type = Integer32
_SlaveOutletOnTime05_Object = MibTableColumn
slaveOutletOnTime05 = _SlaveOutletOnTime05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 6),
    _SlaveOutletOnTime05_Type()
)
slaveOutletOnTime05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime05.setStatus("mandatory")
_SlaveOutletOnTime06_Type = Integer32
_SlaveOutletOnTime06_Object = MibTableColumn
slaveOutletOnTime06 = _SlaveOutletOnTime06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 7),
    _SlaveOutletOnTime06_Type()
)
slaveOutletOnTime06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime06.setStatus("mandatory")
_SlaveOutletOnTime07_Type = Integer32
_SlaveOutletOnTime07_Object = MibTableColumn
slaveOutletOnTime07 = _SlaveOutletOnTime07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 8),
    _SlaveOutletOnTime07_Type()
)
slaveOutletOnTime07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime07.setStatus("mandatory")
_SlaveOutletOnTime08_Type = Integer32
_SlaveOutletOnTime08_Object = MibTableColumn
slaveOutletOnTime08 = _SlaveOutletOnTime08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 9),
    _SlaveOutletOnTime08_Type()
)
slaveOutletOnTime08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime08.setStatus("mandatory")
_SlaveOutletOnTime09_Type = Integer32
_SlaveOutletOnTime09_Object = MibTableColumn
slaveOutletOnTime09 = _SlaveOutletOnTime09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 10),
    _SlaveOutletOnTime09_Type()
)
slaveOutletOnTime09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime09.setStatus("mandatory")
_SlaveOutletOnTime10_Type = Integer32
_SlaveOutletOnTime10_Object = MibTableColumn
slaveOutletOnTime10 = _SlaveOutletOnTime10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 11),
    _SlaveOutletOnTime10_Type()
)
slaveOutletOnTime10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime10.setStatus("mandatory")
_SlaveOutletOnTime11_Type = Integer32
_SlaveOutletOnTime11_Object = MibTableColumn
slaveOutletOnTime11 = _SlaveOutletOnTime11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 12),
    _SlaveOutletOnTime11_Type()
)
slaveOutletOnTime11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime11.setStatus("mandatory")
_SlaveOutletOnTime12_Type = Integer32
_SlaveOutletOnTime12_Object = MibTableColumn
slaveOutletOnTime12 = _SlaveOutletOnTime12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 3, 1, 13),
    _SlaveOutletOnTime12_Type()
)
slaveOutletOnTime12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime12.setStatus("mandatory")
_IpmSlaveDeviceOutletOffTimeTable_Object = MibTable
ipmSlaveDeviceOutletOffTimeTable = _IpmSlaveDeviceOutletOffTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletOffTimeTable.setStatus("mandatory")
_IpmSlaveDeviceOutletOffTimeEntry_Object = MibTableRow
ipmSlaveDeviceOutletOffTimeEntry = _IpmSlaveDeviceOutletOffTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1)
)
ipmSlaveDeviceOutletOffTimeEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletOffTimeIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletOffTimeEntry.setStatus("mandatory")


class _SlaveOutletOffTimeIndex_Type(Integer32):
    """Custom type slaveOutletOffTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletOffTimeIndex_Type.__name__ = "Integer32"
_SlaveOutletOffTimeIndex_Object = MibTableColumn
slaveOutletOffTimeIndex = _SlaveOutletOffTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 1),
    _SlaveOutletOffTimeIndex_Type()
)
slaveOutletOffTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletOffTimeIndex.setStatus("mandatory")
_SlaveOutletOffTime01_Type = Integer32
_SlaveOutletOffTime01_Object = MibTableColumn
slaveOutletOffTime01 = _SlaveOutletOffTime01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 2),
    _SlaveOutletOffTime01_Type()
)
slaveOutletOffTime01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime01.setStatus("mandatory")
_SlaveOutletOffTime02_Type = Integer32
_SlaveOutletOffTime02_Object = MibTableColumn
slaveOutletOffTime02 = _SlaveOutletOffTime02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 3),
    _SlaveOutletOffTime02_Type()
)
slaveOutletOffTime02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime02.setStatus("mandatory")
_SlaveOutletOffTime03_Type = Integer32
_SlaveOutletOffTime03_Object = MibTableColumn
slaveOutletOffTime03 = _SlaveOutletOffTime03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 4),
    _SlaveOutletOffTime03_Type()
)
slaveOutletOffTime03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime03.setStatus("mandatory")
_SlaveOutletOffTime04_Type = Integer32
_SlaveOutletOffTime04_Object = MibTableColumn
slaveOutletOffTime04 = _SlaveOutletOffTime04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 5),
    _SlaveOutletOffTime04_Type()
)
slaveOutletOffTime04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime04.setStatus("mandatory")
_SlaveOutletOffTime05_Type = Integer32
_SlaveOutletOffTime05_Object = MibTableColumn
slaveOutletOffTime05 = _SlaveOutletOffTime05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 6),
    _SlaveOutletOffTime05_Type()
)
slaveOutletOffTime05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime05.setStatus("mandatory")
_SlaveOutletOffTime06_Type = Integer32
_SlaveOutletOffTime06_Object = MibTableColumn
slaveOutletOffTime06 = _SlaveOutletOffTime06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 7),
    _SlaveOutletOffTime06_Type()
)
slaveOutletOffTime06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime06.setStatus("mandatory")
_SlaveOutletOffTime07_Type = Integer32
_SlaveOutletOffTime07_Object = MibTableColumn
slaveOutletOffTime07 = _SlaveOutletOffTime07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 8),
    _SlaveOutletOffTime07_Type()
)
slaveOutletOffTime07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime07.setStatus("mandatory")
_SlaveOutletOffTime08_Type = Integer32
_SlaveOutletOffTime08_Object = MibTableColumn
slaveOutletOffTime08 = _SlaveOutletOffTime08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 9),
    _SlaveOutletOffTime08_Type()
)
slaveOutletOffTime08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime08.setStatus("mandatory")
_SlaveOutletOffTime09_Type = Integer32
_SlaveOutletOffTime09_Object = MibTableColumn
slaveOutletOffTime09 = _SlaveOutletOffTime09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 10),
    _SlaveOutletOffTime09_Type()
)
slaveOutletOffTime09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime09.setStatus("mandatory")
_SlaveOutletOffTime10_Type = Integer32
_SlaveOutletOffTime10_Object = MibTableColumn
slaveOutletOffTime10 = _SlaveOutletOffTime10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 11),
    _SlaveOutletOffTime10_Type()
)
slaveOutletOffTime10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime10.setStatus("mandatory")
_SlaveOutletOffTime11_Type = Integer32
_SlaveOutletOffTime11_Object = MibTableColumn
slaveOutletOffTime11 = _SlaveOutletOffTime11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 12),
    _SlaveOutletOffTime11_Type()
)
slaveOutletOffTime11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime11.setStatus("mandatory")
_SlaveOutletOffTime12_Type = Integer32
_SlaveOutletOffTime12_Object = MibTableColumn
slaveOutletOffTime12 = _SlaveOutletOffTime12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 4, 1, 13),
    _SlaveOutletOffTime12_Type()
)
slaveOutletOffTime12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime12.setStatus("mandatory")
_IpmSlaveDeviceOutletCurrThTable_Object = MibTable
ipmSlaveDeviceOutletCurrThTable = _IpmSlaveDeviceOutletCurrThTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletCurrThTable.setStatus("mandatory")
_IpmSlaveDeviceOutletCurrThEntry_Object = MibTableRow
ipmSlaveDeviceOutletCurrThEntry = _IpmSlaveDeviceOutletCurrThEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1)
)
ipmSlaveDeviceOutletCurrThEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletCurrThIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletCurrThEntry.setStatus("mandatory")


class _SlaveOutletCurrThIndex_Type(Integer32):
    """Custom type slaveOutletCurrThIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletCurrThIndex_Type.__name__ = "Integer32"
_SlaveOutletCurrThIndex_Object = MibTableColumn
slaveOutletCurrThIndex = _SlaveOutletCurrThIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 1),
    _SlaveOutletCurrThIndex_Type()
)
slaveOutletCurrThIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrThIndex.setStatus("mandatory")
_SlaveOutletCurrTh01_Type = Integer32
_SlaveOutletCurrTh01_Object = MibTableColumn
slaveOutletCurrTh01 = _SlaveOutletCurrTh01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 2),
    _SlaveOutletCurrTh01_Type()
)
slaveOutletCurrTh01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh01.setStatus("mandatory")
_SlaveOutletCurrTh02_Type = Integer32
_SlaveOutletCurrTh02_Object = MibTableColumn
slaveOutletCurrTh02 = _SlaveOutletCurrTh02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 3),
    _SlaveOutletCurrTh02_Type()
)
slaveOutletCurrTh02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh02.setStatus("mandatory")
_SlaveOutletCurrTh03_Type = Integer32
_SlaveOutletCurrTh03_Object = MibTableColumn
slaveOutletCurrTh03 = _SlaveOutletCurrTh03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 4),
    _SlaveOutletCurrTh03_Type()
)
slaveOutletCurrTh03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh03.setStatus("mandatory")
_SlaveOutletCurrTh04_Type = Integer32
_SlaveOutletCurrTh04_Object = MibTableColumn
slaveOutletCurrTh04 = _SlaveOutletCurrTh04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 5),
    _SlaveOutletCurrTh04_Type()
)
slaveOutletCurrTh04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh04.setStatus("mandatory")
_SlaveOutletCurrTh05_Type = Integer32
_SlaveOutletCurrTh05_Object = MibTableColumn
slaveOutletCurrTh05 = _SlaveOutletCurrTh05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 6),
    _SlaveOutletCurrTh05_Type()
)
slaveOutletCurrTh05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh05.setStatus("mandatory")
_SlaveOutletCurrTh06_Type = Integer32
_SlaveOutletCurrTh06_Object = MibTableColumn
slaveOutletCurrTh06 = _SlaveOutletCurrTh06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 7),
    _SlaveOutletCurrTh06_Type()
)
slaveOutletCurrTh06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh06.setStatus("mandatory")
_SlaveOutletCurrTh07_Type = Integer32
_SlaveOutletCurrTh07_Object = MibTableColumn
slaveOutletCurrTh07 = _SlaveOutletCurrTh07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 8),
    _SlaveOutletCurrTh07_Type()
)
slaveOutletCurrTh07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh07.setStatus("mandatory")
_SlaveOutletCurrTh08_Type = Integer32
_SlaveOutletCurrTh08_Object = MibTableColumn
slaveOutletCurrTh08 = _SlaveOutletCurrTh08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 9),
    _SlaveOutletCurrTh08_Type()
)
slaveOutletCurrTh08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh08.setStatus("mandatory")
_SlaveOutletCurrTh09_Type = Integer32
_SlaveOutletCurrTh09_Object = MibTableColumn
slaveOutletCurrTh09 = _SlaveOutletCurrTh09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 10),
    _SlaveOutletCurrTh09_Type()
)
slaveOutletCurrTh09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh09.setStatus("mandatory")
_SlaveOutletCurrTh10_Type = Integer32
_SlaveOutletCurrTh10_Object = MibTableColumn
slaveOutletCurrTh10 = _SlaveOutletCurrTh10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 11),
    _SlaveOutletCurrTh10_Type()
)
slaveOutletCurrTh10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh10.setStatus("mandatory")
_SlaveOutletCurrTh11_Type = Integer32
_SlaveOutletCurrTh11_Object = MibTableColumn
slaveOutletCurrTh11 = _SlaveOutletCurrTh11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 12),
    _SlaveOutletCurrTh11_Type()
)
slaveOutletCurrTh11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh11.setStatus("mandatory")
_SlaveOutletCurrTh12_Type = Integer32
_SlaveOutletCurrTh12_Object = MibTableColumn
slaveOutletCurrTh12 = _SlaveOutletCurrTh12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 1, 5, 1, 13),
    _SlaveOutletCurrTh12_Type()
)
slaveOutletCurrTh12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh12.setStatus("mandatory")
_IpmSlaveOutletStatus_ObjectIdentity = ObjectIdentity
ipmSlaveOutletStatus = _IpmSlaveOutletStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2)
)
_IpmSlaveDeviceOutletCurrentTable_Object = MibTable
ipmSlaveDeviceOutletCurrentTable = _IpmSlaveDeviceOutletCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletCurrentTable.setStatus("mandatory")
_IpmSlaveDeviceOutletCurrentEntry_Object = MibTableRow
ipmSlaveDeviceOutletCurrentEntry = _IpmSlaveDeviceOutletCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1)
)
ipmSlaveDeviceOutletCurrentEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletCurrentIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletCurrentEntry.setStatus("mandatory")


class _SlaveOutletCurrentIndex_Type(Integer32):
    """Custom type slaveOutletCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletCurrentIndex_Type.__name__ = "Integer32"
_SlaveOutletCurrentIndex_Object = MibTableColumn
slaveOutletCurrentIndex = _SlaveOutletCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 1),
    _SlaveOutletCurrentIndex_Type()
)
slaveOutletCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrentIndex.setStatus("mandatory")
_SlaveOutletCurrent01_Type = Integer32
_SlaveOutletCurrent01_Object = MibTableColumn
slaveOutletCurrent01 = _SlaveOutletCurrent01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 2),
    _SlaveOutletCurrent01_Type()
)
slaveOutletCurrent01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent01.setStatus("mandatory")
_SlaveOutletCurrent02_Type = Integer32
_SlaveOutletCurrent02_Object = MibTableColumn
slaveOutletCurrent02 = _SlaveOutletCurrent02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 3),
    _SlaveOutletCurrent02_Type()
)
slaveOutletCurrent02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent02.setStatus("mandatory")
_SlaveOutletCurrent03_Type = Integer32
_SlaveOutletCurrent03_Object = MibTableColumn
slaveOutletCurrent03 = _SlaveOutletCurrent03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 4),
    _SlaveOutletCurrent03_Type()
)
slaveOutletCurrent03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent03.setStatus("mandatory")
_SlaveOutletCurrent04_Type = Integer32
_SlaveOutletCurrent04_Object = MibTableColumn
slaveOutletCurrent04 = _SlaveOutletCurrent04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 5),
    _SlaveOutletCurrent04_Type()
)
slaveOutletCurrent04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent04.setStatus("mandatory")
_SlaveOutletCurrent05_Type = Integer32
_SlaveOutletCurrent05_Object = MibTableColumn
slaveOutletCurrent05 = _SlaveOutletCurrent05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 6),
    _SlaveOutletCurrent05_Type()
)
slaveOutletCurrent05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent05.setStatus("mandatory")
_SlaveOutletCurrent06_Type = Integer32
_SlaveOutletCurrent06_Object = MibTableColumn
slaveOutletCurrent06 = _SlaveOutletCurrent06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 7),
    _SlaveOutletCurrent06_Type()
)
slaveOutletCurrent06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent06.setStatus("mandatory")
_SlaveOutletCurrent07_Type = Integer32
_SlaveOutletCurrent07_Object = MibTableColumn
slaveOutletCurrent07 = _SlaveOutletCurrent07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 8),
    _SlaveOutletCurrent07_Type()
)
slaveOutletCurrent07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent07.setStatus("mandatory")
_SlaveOutletCurrent08_Type = Integer32
_SlaveOutletCurrent08_Object = MibTableColumn
slaveOutletCurrent08 = _SlaveOutletCurrent08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 9),
    _SlaveOutletCurrent08_Type()
)
slaveOutletCurrent08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent08.setStatus("mandatory")
_SlaveOutletCurrent09_Type = Integer32
_SlaveOutletCurrent09_Object = MibTableColumn
slaveOutletCurrent09 = _SlaveOutletCurrent09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 10),
    _SlaveOutletCurrent09_Type()
)
slaveOutletCurrent09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent09.setStatus("mandatory")
_SlaveOutletCurrent10_Type = Integer32
_SlaveOutletCurrent10_Object = MibTableColumn
slaveOutletCurrent10 = _SlaveOutletCurrent10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 11),
    _SlaveOutletCurrent10_Type()
)
slaveOutletCurrent10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent10.setStatus("mandatory")
_SlaveOutletCurrent11_Type = Integer32
_SlaveOutletCurrent11_Object = MibTableColumn
slaveOutletCurrent11 = _SlaveOutletCurrent11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 12),
    _SlaveOutletCurrent11_Type()
)
slaveOutletCurrent11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent11.setStatus("mandatory")
_SlaveOutletCurrent12_Type = Integer32
_SlaveOutletCurrent12_Object = MibTableColumn
slaveOutletCurrent12 = _SlaveOutletCurrent12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 1, 1, 13),
    _SlaveOutletCurrent12_Type()
)
slaveOutletCurrent12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent12.setStatus("mandatory")
_IpmSlaveDeviceOutletWattTable_Object = MibTable
ipmSlaveDeviceOutletWattTable = _IpmSlaveDeviceOutletWattTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletWattTable.setStatus("mandatory")
_IpmSlaveDeviceOutletWattEntry_Object = MibTableRow
ipmSlaveDeviceOutletWattEntry = _IpmSlaveDeviceOutletWattEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1)
)
ipmSlaveDeviceOutletWattEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletWattIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletWattEntry.setStatus("mandatory")


class _SlaveOutletWattIndex_Type(Integer32):
    """Custom type slaveOutletWattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletWattIndex_Type.__name__ = "Integer32"
_SlaveOutletWattIndex_Object = MibTableColumn
slaveOutletWattIndex = _SlaveOutletWattIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 1),
    _SlaveOutletWattIndex_Type()
)
slaveOutletWattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWattIndex.setStatus("mandatory")
_SlaveOutletWatt01_Type = Integer32
_SlaveOutletWatt01_Object = MibTableColumn
slaveOutletWatt01 = _SlaveOutletWatt01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 2),
    _SlaveOutletWatt01_Type()
)
slaveOutletWatt01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt01.setStatus("mandatory")
_SlaveOutletWatt02_Type = Integer32
_SlaveOutletWatt02_Object = MibTableColumn
slaveOutletWatt02 = _SlaveOutletWatt02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 3),
    _SlaveOutletWatt02_Type()
)
slaveOutletWatt02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt02.setStatus("mandatory")
_SlaveOutletWatt03_Type = Integer32
_SlaveOutletWatt03_Object = MibTableColumn
slaveOutletWatt03 = _SlaveOutletWatt03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 4),
    _SlaveOutletWatt03_Type()
)
slaveOutletWatt03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt03.setStatus("mandatory")
_SlaveOutletWatt04_Type = Integer32
_SlaveOutletWatt04_Object = MibTableColumn
slaveOutletWatt04 = _SlaveOutletWatt04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 5),
    _SlaveOutletWatt04_Type()
)
slaveOutletWatt04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt04.setStatus("mandatory")
_SlaveOutletWatt05_Type = Integer32
_SlaveOutletWatt05_Object = MibTableColumn
slaveOutletWatt05 = _SlaveOutletWatt05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 6),
    _SlaveOutletWatt05_Type()
)
slaveOutletWatt05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt05.setStatus("mandatory")
_SlaveOutletWatt06_Type = Integer32
_SlaveOutletWatt06_Object = MibTableColumn
slaveOutletWatt06 = _SlaveOutletWatt06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 7),
    _SlaveOutletWatt06_Type()
)
slaveOutletWatt06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt06.setStatus("mandatory")
_SlaveOutletWatt07_Type = Integer32
_SlaveOutletWatt07_Object = MibTableColumn
slaveOutletWatt07 = _SlaveOutletWatt07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 8),
    _SlaveOutletWatt07_Type()
)
slaveOutletWatt07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt07.setStatus("mandatory")
_SlaveOutletWatt08_Type = Integer32
_SlaveOutletWatt08_Object = MibTableColumn
slaveOutletWatt08 = _SlaveOutletWatt08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 9),
    _SlaveOutletWatt08_Type()
)
slaveOutletWatt08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt08.setStatus("mandatory")
_SlaveOutletWatt09_Type = Integer32
_SlaveOutletWatt09_Object = MibTableColumn
slaveOutletWatt09 = _SlaveOutletWatt09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 10),
    _SlaveOutletWatt09_Type()
)
slaveOutletWatt09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt09.setStatus("mandatory")
_SlaveOutletWatt10_Type = Integer32
_SlaveOutletWatt10_Object = MibTableColumn
slaveOutletWatt10 = _SlaveOutletWatt10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 11),
    _SlaveOutletWatt10_Type()
)
slaveOutletWatt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt10.setStatus("mandatory")
_SlaveOutletWatt11_Type = Integer32
_SlaveOutletWatt11_Object = MibTableColumn
slaveOutletWatt11 = _SlaveOutletWatt11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 12),
    _SlaveOutletWatt11_Type()
)
slaveOutletWatt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt11.setStatus("mandatory")
_SlaveOutletWatt12_Type = Integer32
_SlaveOutletWatt12_Object = MibTableColumn
slaveOutletWatt12 = _SlaveOutletWatt12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 2, 1, 13),
    _SlaveOutletWatt12_Type()
)
slaveOutletWatt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt12.setStatus("mandatory")
_IpmSlaveDeviceOutletKwattTable_Object = MibTable
ipmSlaveDeviceOutletKwattTable = _IpmSlaveDeviceOutletKwattTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletKwattTable.setStatus("mandatory")
_IpmSlaveDeviceOutletKwattEntry_Object = MibTableRow
ipmSlaveDeviceOutletKwattEntry = _IpmSlaveDeviceOutletKwattEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1)
)
ipmSlaveDeviceOutletKwattEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletKwattIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletKwattEntry.setStatus("mandatory")


class _SlaveOutletKwattIndex_Type(Integer32):
    """Custom type slaveOutletKwattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletKwattIndex_Type.__name__ = "Integer32"
_SlaveOutletKwattIndex_Object = MibTableColumn
slaveOutletKwattIndex = _SlaveOutletKwattIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 1),
    _SlaveOutletKwattIndex_Type()
)
slaveOutletKwattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwattIndex.setStatus("mandatory")
_SlaveOutletKwatt01_Type = Integer32
_SlaveOutletKwatt01_Object = MibTableColumn
slaveOutletKwatt01 = _SlaveOutletKwatt01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 2),
    _SlaveOutletKwatt01_Type()
)
slaveOutletKwatt01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt01.setStatus("mandatory")
_SlaveOutletKwatt02_Type = Integer32
_SlaveOutletKwatt02_Object = MibTableColumn
slaveOutletKwatt02 = _SlaveOutletKwatt02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 3),
    _SlaveOutletKwatt02_Type()
)
slaveOutletKwatt02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt02.setStatus("mandatory")
_SlaveOutletKwatt03_Type = Integer32
_SlaveOutletKwatt03_Object = MibTableColumn
slaveOutletKwatt03 = _SlaveOutletKwatt03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 4),
    _SlaveOutletKwatt03_Type()
)
slaveOutletKwatt03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt03.setStatus("mandatory")
_SlaveOutletKwatt04_Type = Integer32
_SlaveOutletKwatt04_Object = MibTableColumn
slaveOutletKwatt04 = _SlaveOutletKwatt04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 5),
    _SlaveOutletKwatt04_Type()
)
slaveOutletKwatt04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt04.setStatus("mandatory")
_SlaveOutletKwatt05_Type = Integer32
_SlaveOutletKwatt05_Object = MibTableColumn
slaveOutletKwatt05 = _SlaveOutletKwatt05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 6),
    _SlaveOutletKwatt05_Type()
)
slaveOutletKwatt05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt05.setStatus("mandatory")
_SlaveOutletKwatt06_Type = Integer32
_SlaveOutletKwatt06_Object = MibTableColumn
slaveOutletKwatt06 = _SlaveOutletKwatt06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 7),
    _SlaveOutletKwatt06_Type()
)
slaveOutletKwatt06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt06.setStatus("mandatory")
_SlaveOutletKwatt07_Type = Integer32
_SlaveOutletKwatt07_Object = MibTableColumn
slaveOutletKwatt07 = _SlaveOutletKwatt07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 8),
    _SlaveOutletKwatt07_Type()
)
slaveOutletKwatt07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt07.setStatus("mandatory")
_SlaveOutletKwatt08_Type = Integer32
_SlaveOutletKwatt08_Object = MibTableColumn
slaveOutletKwatt08 = _SlaveOutletKwatt08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 9),
    _SlaveOutletKwatt08_Type()
)
slaveOutletKwatt08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt08.setStatus("mandatory")
_SlaveOutletKwatt09_Type = Integer32
_SlaveOutletKwatt09_Object = MibTableColumn
slaveOutletKwatt09 = _SlaveOutletKwatt09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 10),
    _SlaveOutletKwatt09_Type()
)
slaveOutletKwatt09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt09.setStatus("mandatory")
_SlaveOutletKwatt10_Type = Integer32
_SlaveOutletKwatt10_Object = MibTableColumn
slaveOutletKwatt10 = _SlaveOutletKwatt10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 11),
    _SlaveOutletKwatt10_Type()
)
slaveOutletKwatt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt10.setStatus("mandatory")
_SlaveOutletKwatt11_Type = Integer32
_SlaveOutletKwatt11_Object = MibTableColumn
slaveOutletKwatt11 = _SlaveOutletKwatt11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 12),
    _SlaveOutletKwatt11_Type()
)
slaveOutletKwatt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt11.setStatus("mandatory")
_SlaveOutletKwatt12_Type = Integer32
_SlaveOutletKwatt12_Object = MibTableColumn
slaveOutletKwatt12 = _SlaveOutletKwatt12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 2, 3, 1, 13),
    _SlaveOutletKwatt12_Type()
)
slaveOutletKwatt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt12.setStatus("mandatory")
_IpmSlaveOutletAction_ObjectIdentity = ObjectIdentity
ipmSlaveOutletAction = _IpmSlaveOutletAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3)
)
_IpmSlaveDeviceOutletActionTable_Object = MibTable
ipmSlaveDeviceOutletActionTable = _IpmSlaveDeviceOutletActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletActionTable.setStatus("mandatory")
_IpmSlaveDeviceOutletActionEntry_Object = MibTableRow
ipmSlaveDeviceOutletActionEntry = _IpmSlaveDeviceOutletActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1)
)
ipmSlaveDeviceOutletActionEntry.setIndexNames(
    (0, "IPOMANII-MIB", "slaveOutletActionIndex"),
)
if mibBuilder.loadTexts:
    ipmSlaveDeviceOutletActionEntry.setStatus("mandatory")


class _SlaveOutletActionIndex_Type(Integer32):
    """Custom type slaveOutletActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletActionIndex_Type.__name__ = "Integer32"
_SlaveOutletActionIndex_Object = MibTableColumn
slaveOutletActionIndex = _SlaveOutletActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 1),
    _SlaveOutletActionIndex_Type()
)
slaveOutletActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletActionIndex.setStatus("mandatory")


class _SlaveOutletAction01_Type(Integer32):
    """Custom type slaveOutletAction01 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction01_Type.__name__ = "Integer32"
_SlaveOutletAction01_Object = MibTableColumn
slaveOutletAction01 = _SlaveOutletAction01_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 2),
    _SlaveOutletAction01_Type()
)
slaveOutletAction01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction01.setStatus("mandatory")


class _SlaveOutletAction02_Type(Integer32):
    """Custom type slaveOutletAction02 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction02_Type.__name__ = "Integer32"
_SlaveOutletAction02_Object = MibTableColumn
slaveOutletAction02 = _SlaveOutletAction02_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 3),
    _SlaveOutletAction02_Type()
)
slaveOutletAction02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction02.setStatus("mandatory")


class _SlaveOutletAction03_Type(Integer32):
    """Custom type slaveOutletAction03 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction03_Type.__name__ = "Integer32"
_SlaveOutletAction03_Object = MibTableColumn
slaveOutletAction03 = _SlaveOutletAction03_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 4),
    _SlaveOutletAction03_Type()
)
slaveOutletAction03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction03.setStatus("mandatory")


class _SlaveOutletAction04_Type(Integer32):
    """Custom type slaveOutletAction04 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction04_Type.__name__ = "Integer32"
_SlaveOutletAction04_Object = MibTableColumn
slaveOutletAction04 = _SlaveOutletAction04_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 5),
    _SlaveOutletAction04_Type()
)
slaveOutletAction04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction04.setStatus("mandatory")


class _SlaveOutletAction05_Type(Integer32):
    """Custom type slaveOutletAction05 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction05_Type.__name__ = "Integer32"
_SlaveOutletAction05_Object = MibTableColumn
slaveOutletAction05 = _SlaveOutletAction05_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 6),
    _SlaveOutletAction05_Type()
)
slaveOutletAction05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction05.setStatus("mandatory")


class _SlaveOutletAction06_Type(Integer32):
    """Custom type slaveOutletAction06 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction06_Type.__name__ = "Integer32"
_SlaveOutletAction06_Object = MibTableColumn
slaveOutletAction06 = _SlaveOutletAction06_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 7),
    _SlaveOutletAction06_Type()
)
slaveOutletAction06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction06.setStatus("mandatory")


class _SlaveOutletAction07_Type(Integer32):
    """Custom type slaveOutletAction07 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction07_Type.__name__ = "Integer32"
_SlaveOutletAction07_Object = MibTableColumn
slaveOutletAction07 = _SlaveOutletAction07_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 8),
    _SlaveOutletAction07_Type()
)
slaveOutletAction07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction07.setStatus("mandatory")


class _SlaveOutletAction08_Type(Integer32):
    """Custom type slaveOutletAction08 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction08_Type.__name__ = "Integer32"
_SlaveOutletAction08_Object = MibTableColumn
slaveOutletAction08 = _SlaveOutletAction08_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 9),
    _SlaveOutletAction08_Type()
)
slaveOutletAction08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction08.setStatus("mandatory")


class _SlaveOutletAction09_Type(Integer32):
    """Custom type slaveOutletAction09 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction09_Type.__name__ = "Integer32"
_SlaveOutletAction09_Object = MibTableColumn
slaveOutletAction09 = _SlaveOutletAction09_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 10),
    _SlaveOutletAction09_Type()
)
slaveOutletAction09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction09.setStatus("mandatory")


class _SlaveOutletAction10_Type(Integer32):
    """Custom type slaveOutletAction10 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction10_Type.__name__ = "Integer32"
_SlaveOutletAction10_Object = MibTableColumn
slaveOutletAction10 = _SlaveOutletAction10_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 11),
    _SlaveOutletAction10_Type()
)
slaveOutletAction10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction10.setStatus("mandatory")


class _SlaveOutletAction11_Type(Integer32):
    """Custom type slaveOutletAction11 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction11_Type.__name__ = "Integer32"
_SlaveOutletAction11_Object = MibTableColumn
slaveOutletAction11 = _SlaveOutletAction11_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 12),
    _SlaveOutletAction11_Type()
)
slaveOutletAction11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction11.setStatus("mandatory")


class _SlaveOutletAction12_Type(Integer32):
    """Custom type slaveOutletAction12 based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelAction", 2),
          ("cycleByActionTimer", 8),
          ("cycleImmediately", 5),
          ("none", 1),
          ("offByActionTimer", 7),
          ("offImmediately", 4),
          ("offThenOnByActionTimers", 10),
          ("onByActionTimer", 6),
          ("onImmediately", 3),
          ("onThenOffByActionTimers", 9))
    )


_SlaveOutletAction12_Type.__name__ = "Integer32"
_SlaveOutletAction12_Object = MibTableColumn
slaveOutletAction12 = _SlaveOutletAction12_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 4, 3, 3, 1, 1, 13),
    _SlaveOutletAction12_Type()
)
slaveOutletAction12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction12.setStatus("mandatory")
_IpmEnv_ObjectIdentity = ObjectIdentity
ipmEnv = _IpmEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5)
)
_IpmEnvEmd_ObjectIdentity = ObjectIdentity
ipmEnvEmd = _IpmEnvEmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1)
)
_IpmEnvEmdStatus_ObjectIdentity = ObjectIdentity
ipmEnvEmdStatus = _IpmEnvEmdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 1)
)


class _IpmEnvEmdStatusEmdType_Type(Integer32):
    """Custom type ipmEnvEmdStatusEmdType based on Integer32"""
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
        *(("disabled", 2),
          ("eMD-HT", 3),
          ("eMD-T", 4),
          ("unknown", 1))
    )


_IpmEnvEmdStatusEmdType_Type.__name__ = "Integer32"
_IpmEnvEmdStatusEmdType_Object = MibScalar
ipmEnvEmdStatusEmdType = _IpmEnvEmdStatusEmdType_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 1, 1),
    _IpmEnvEmdStatusEmdType_Type()
)
ipmEnvEmdStatusEmdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmEnvEmdStatusEmdType.setStatus("mandatory")


class _IpmEnvEmdStatusTemperature_Type(Integer32):
    """Custom type ipmEnvEmdStatusTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_IpmEnvEmdStatusTemperature_Type.__name__ = "Integer32"
_IpmEnvEmdStatusTemperature_Object = MibScalar
ipmEnvEmdStatusTemperature = _IpmEnvEmdStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 1, 2),
    _IpmEnvEmdStatusTemperature_Type()
)
ipmEnvEmdStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmEnvEmdStatusTemperature.setStatus("mandatory")


class _IpmEnvEmdStatusHumidity_Type(Integer32):
    """Custom type ipmEnvEmdStatusHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_IpmEnvEmdStatusHumidity_Type.__name__ = "Integer32"
_IpmEnvEmdStatusHumidity_Object = MibScalar
ipmEnvEmdStatusHumidity = _IpmEnvEmdStatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 1, 3),
    _IpmEnvEmdStatusHumidity_Type()
)
ipmEnvEmdStatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmEnvEmdStatusHumidity.setStatus("mandatory")


class _IpmEnvEmdStatusAlarm1_Type(Integer32):
    """Custom type ipmEnvEmdStatusAlarm1 based on Integer32"""
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
        *(("alarm", 3),
          ("disabled", 2),
          ("normal", 4),
          ("unknown", 1))
    )


_IpmEnvEmdStatusAlarm1_Type.__name__ = "Integer32"
_IpmEnvEmdStatusAlarm1_Object = MibScalar
ipmEnvEmdStatusAlarm1 = _IpmEnvEmdStatusAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 1, 4),
    _IpmEnvEmdStatusAlarm1_Type()
)
ipmEnvEmdStatusAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmEnvEmdStatusAlarm1.setStatus("mandatory")


class _IpmEnvEmdStatusAlarm2_Type(Integer32):
    """Custom type ipmEnvEmdStatusAlarm2 based on Integer32"""
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
        *(("alarm", 3),
          ("disabled", 2),
          ("normal", 4),
          ("unknown", 1))
    )


_IpmEnvEmdStatusAlarm2_Type.__name__ = "Integer32"
_IpmEnvEmdStatusAlarm2_Object = MibScalar
ipmEnvEmdStatusAlarm2 = _IpmEnvEmdStatusAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 1, 5),
    _IpmEnvEmdStatusAlarm2_Type()
)
ipmEnvEmdStatusAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmEnvEmdStatusAlarm2.setStatus("mandatory")
_IpmEnvEmdConfig_ObjectIdentity = ObjectIdentity
ipmEnvEmdConfig = _IpmEnvEmdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2)
)


class _IpmEnvEmdConfigEmdPresence_Type(Integer32):
    """Custom type ipmEnvEmdConfigEmdPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 2),
          ("disabled", 1))
    )


_IpmEnvEmdConfigEmdPresence_Type.__name__ = "Integer32"
_IpmEnvEmdConfigEmdPresence_Object = MibScalar
ipmEnvEmdConfigEmdPresence = _IpmEnvEmdConfigEmdPresence_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 1),
    _IpmEnvEmdConfigEmdPresence_Type()
)
ipmEnvEmdConfigEmdPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigEmdPresence.setStatus("mandatory")


class _IpmEnvEmdConfigEmdName_Type(DisplayString):
    """Custom type ipmEnvEmdConfigEmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmEnvEmdConfigEmdName_Type.__name__ = "DisplayString"
_IpmEnvEmdConfigEmdName_Object = MibScalar
ipmEnvEmdConfigEmdName = _IpmEnvEmdConfigEmdName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 2),
    _IpmEnvEmdConfigEmdName_Type()
)
ipmEnvEmdConfigEmdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigEmdName.setStatus("mandatory")
_IpmEnvEmdConfigTemp_ObjectIdentity = ObjectIdentity
ipmEnvEmdConfigTemp = _IpmEnvEmdConfigTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 3)
)


class _IpmEnvEmdConfigTempName_Type(DisplayString):
    """Custom type ipmEnvEmdConfigTempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmEnvEmdConfigTempName_Type.__name__ = "DisplayString"
_IpmEnvEmdConfigTempName_Object = MibScalar
ipmEnvEmdConfigTempName = _IpmEnvEmdConfigTempName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 3, 1),
    _IpmEnvEmdConfigTempName_Type()
)
ipmEnvEmdConfigTempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigTempName.setStatus("mandatory")


class _IpmEnvEmdConfigTempHighSetPoint_Type(Integer32):
    """Custom type ipmEnvEmdConfigTempHighSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65),
    )


_IpmEnvEmdConfigTempHighSetPoint_Type.__name__ = "Integer32"
_IpmEnvEmdConfigTempHighSetPoint_Object = MibScalar
ipmEnvEmdConfigTempHighSetPoint = _IpmEnvEmdConfigTempHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 3, 2),
    _IpmEnvEmdConfigTempHighSetPoint_Type()
)
ipmEnvEmdConfigTempHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigTempHighSetPoint.setStatus("mandatory")


class _IpmEnvEmdConfigTempHighStatus_Type(Integer32):
    """Custom type ipmEnvEmdConfigTempHighStatus based on Integer32"""
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


_IpmEnvEmdConfigTempHighStatus_Type.__name__ = "Integer32"
_IpmEnvEmdConfigTempHighStatus_Object = MibScalar
ipmEnvEmdConfigTempHighStatus = _IpmEnvEmdConfigTempHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 3, 3),
    _IpmEnvEmdConfigTempHighStatus_Type()
)
ipmEnvEmdConfigTempHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigTempHighStatus.setStatus("mandatory")


class _IpmEnvEmdConfigTempLowSetPoint_Type(Integer32):
    """Custom type ipmEnvEmdConfigTempLowSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65),
    )


_IpmEnvEmdConfigTempLowSetPoint_Type.__name__ = "Integer32"
_IpmEnvEmdConfigTempLowSetPoint_Object = MibScalar
ipmEnvEmdConfigTempLowSetPoint = _IpmEnvEmdConfigTempLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 3, 4),
    _IpmEnvEmdConfigTempLowSetPoint_Type()
)
ipmEnvEmdConfigTempLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigTempLowSetPoint.setStatus("mandatory")


class _IpmEnvEmdConfigTempLowStatus_Type(Integer32):
    """Custom type ipmEnvEmdConfigTempLowStatus based on Integer32"""
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


_IpmEnvEmdConfigTempLowStatus_Type.__name__ = "Integer32"
_IpmEnvEmdConfigTempLowStatus_Object = MibScalar
ipmEnvEmdConfigTempLowStatus = _IpmEnvEmdConfigTempLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 3, 5),
    _IpmEnvEmdConfigTempLowStatus_Type()
)
ipmEnvEmdConfigTempLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigTempLowStatus.setStatus("mandatory")


class _IpmEnvEmdConfigTempOffset_Type(Integer32):
    """Custom type ipmEnvEmdConfigTempOffset based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("t-0p5", 8),
          ("t-1p0", 9),
          ("t-1p5", 10),
          ("t-2p0", 11),
          ("t-2p5", 12),
          ("t-3p0", 13),
          ("t0p0", 1),
          ("t0p5", 2),
          ("t1p0", 3),
          ("t1p5", 4),
          ("t2p0", 5),
          ("t2p5", 6),
          ("t3p0", 7))
    )


_IpmEnvEmdConfigTempOffset_Type.__name__ = "Integer32"
_IpmEnvEmdConfigTempOffset_Object = MibScalar
ipmEnvEmdConfigTempOffset = _IpmEnvEmdConfigTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 3, 6),
    _IpmEnvEmdConfigTempOffset_Type()
)
ipmEnvEmdConfigTempOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigTempOffset.setStatus("mandatory")
_IpmEnvEmdConfigHumi_ObjectIdentity = ObjectIdentity
ipmEnvEmdConfigHumi = _IpmEnvEmdConfigHumi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 4)
)


class _IpmEnvEmdConfigHumiName_Type(DisplayString):
    """Custom type ipmEnvEmdConfigHumiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmEnvEmdConfigHumiName_Type.__name__ = "DisplayString"
_IpmEnvEmdConfigHumiName_Object = MibScalar
ipmEnvEmdConfigHumiName = _IpmEnvEmdConfigHumiName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 4, 1),
    _IpmEnvEmdConfigHumiName_Type()
)
ipmEnvEmdConfigHumiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigHumiName.setStatus("mandatory")


class _IpmEnvEmdConfigHumiHighSetPoint_Type(Integer32):
    """Custom type ipmEnvEmdConfigHumiHighSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 95),
    )


_IpmEnvEmdConfigHumiHighSetPoint_Type.__name__ = "Integer32"
_IpmEnvEmdConfigHumiHighSetPoint_Object = MibScalar
ipmEnvEmdConfigHumiHighSetPoint = _IpmEnvEmdConfigHumiHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 4, 2),
    _IpmEnvEmdConfigHumiHighSetPoint_Type()
)
ipmEnvEmdConfigHumiHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigHumiHighSetPoint.setStatus("mandatory")


class _IpmEnvEmdConfigHumiHighStatus_Type(Integer32):
    """Custom type ipmEnvEmdConfigHumiHighStatus based on Integer32"""
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


_IpmEnvEmdConfigHumiHighStatus_Type.__name__ = "Integer32"
_IpmEnvEmdConfigHumiHighStatus_Object = MibScalar
ipmEnvEmdConfigHumiHighStatus = _IpmEnvEmdConfigHumiHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 4, 3),
    _IpmEnvEmdConfigHumiHighStatus_Type()
)
ipmEnvEmdConfigHumiHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigHumiHighStatus.setStatus("mandatory")


class _IpmEnvEmdConfigHumiLowSetPoint_Type(Integer32):
    """Custom type ipmEnvEmdConfigHumiLowSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 95),
    )


_IpmEnvEmdConfigHumiLowSetPoint_Type.__name__ = "Integer32"
_IpmEnvEmdConfigHumiLowSetPoint_Object = MibScalar
ipmEnvEmdConfigHumiLowSetPoint = _IpmEnvEmdConfigHumiLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 4, 4),
    _IpmEnvEmdConfigHumiLowSetPoint_Type()
)
ipmEnvEmdConfigHumiLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigHumiLowSetPoint.setStatus("mandatory")


class _IpmEnvEmdConfigHumiLowStatus_Type(Integer32):
    """Custom type ipmEnvEmdConfigHumiLowStatus based on Integer32"""
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


_IpmEnvEmdConfigHumiLowStatus_Type.__name__ = "Integer32"
_IpmEnvEmdConfigHumiLowStatus_Object = MibScalar
ipmEnvEmdConfigHumiLowStatus = _IpmEnvEmdConfigHumiLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 4, 5),
    _IpmEnvEmdConfigHumiLowStatus_Type()
)
ipmEnvEmdConfigHumiLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigHumiLowStatus.setStatus("mandatory")


class _IpmEnvEmdConfigHumiOffset_Type(Integer32):
    """Custom type ipmEnvEmdConfigHumiOffset based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("h-1p0", 8),
          ("h-2p0", 9),
          ("h-3p0", 10),
          ("h-4p0", 11),
          ("h-5p0", 12),
          ("h-6p0", 13),
          ("h0p0", 1),
          ("h1p0", 2),
          ("h2p0", 3),
          ("h3p0", 4),
          ("h4p0", 5),
          ("h5p0", 6),
          ("h6p0", 7))
    )


_IpmEnvEmdConfigHumiOffset_Type.__name__ = "Integer32"
_IpmEnvEmdConfigHumiOffset_Object = MibScalar
ipmEnvEmdConfigHumiOffset = _IpmEnvEmdConfigHumiOffset_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 4, 6),
    _IpmEnvEmdConfigHumiOffset_Type()
)
ipmEnvEmdConfigHumiOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigHumiOffset.setStatus("mandatory")
_IpmEnvEmdConfigAlarm1_ObjectIdentity = ObjectIdentity
ipmEnvEmdConfigAlarm1 = _IpmEnvEmdConfigAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 5)
)


class _IpmEnvEmdConfigAlarm1Name_Type(DisplayString):
    """Custom type ipmEnvEmdConfigAlarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmEnvEmdConfigAlarm1Name_Type.__name__ = "DisplayString"
_IpmEnvEmdConfigAlarm1Name_Object = MibScalar
ipmEnvEmdConfigAlarm1Name = _IpmEnvEmdConfigAlarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 5, 1),
    _IpmEnvEmdConfigAlarm1Name_Type()
)
ipmEnvEmdConfigAlarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigAlarm1Name.setStatus("mandatory")


class _IpmEnvEmdConfigAlarm1Type_Type(Integer32):
    """Custom type ipmEnvEmdConfigAlarm1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("normalClose", 3),
          ("normalOpen", 2))
    )


_IpmEnvEmdConfigAlarm1Type_Type.__name__ = "Integer32"
_IpmEnvEmdConfigAlarm1Type_Object = MibScalar
ipmEnvEmdConfigAlarm1Type = _IpmEnvEmdConfigAlarm1Type_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 5, 2),
    _IpmEnvEmdConfigAlarm1Type_Type()
)
ipmEnvEmdConfigAlarm1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigAlarm1Type.setStatus("mandatory")
_IpmEnvEmdConfigAlarm2_ObjectIdentity = ObjectIdentity
ipmEnvEmdConfigAlarm2 = _IpmEnvEmdConfigAlarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 6)
)


class _IpmEnvEmdConfigAlarm2Name_Type(DisplayString):
    """Custom type ipmEnvEmdConfigAlarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpmEnvEmdConfigAlarm2Name_Type.__name__ = "DisplayString"
_IpmEnvEmdConfigAlarm2Name_Object = MibScalar
ipmEnvEmdConfigAlarm2Name = _IpmEnvEmdConfigAlarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 6, 1),
    _IpmEnvEmdConfigAlarm2Name_Type()
)
ipmEnvEmdConfigAlarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigAlarm2Name.setStatus("mandatory")


class _IpmEnvEmdConfigAlarm2Type_Type(Integer32):
    """Custom type ipmEnvEmdConfigAlarm2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("normalClose", 3),
          ("normalOpen", 2))
    )


_IpmEnvEmdConfigAlarm2Type_Type.__name__ = "Integer32"
_IpmEnvEmdConfigAlarm2Type_Object = MibScalar
ipmEnvEmdConfigAlarm2Type = _IpmEnvEmdConfigAlarm2Type_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 1, 5, 1, 2, 6, 2),
    _IpmEnvEmdConfigAlarm2Type_Type()
)
ipmEnvEmdConfigAlarm2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmEnvEmdConfigAlarm2Type.setStatus("mandatory")
_IpmTraps_ObjectIdentity = ObjectIdentity
ipmTraps = _IpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2)
)

# Managed Objects groups


# Notification objects

ipmInletVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 1)
)
ipmInletVoltageTooHigh.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusVoltage"),
        ("IPOMANII-MIB", "inletConfigVoltageHigh"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletVoltageTooHigh.setStatus(
        ""
    )

ipmInletVoltageNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 2)
)
ipmInletVoltageNotTooHigh.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusVoltage"),
        ("IPOMANII-MIB", "inletConfigVoltageHigh"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletVoltageNotTooHigh.setStatus(
        ""
    )

ipmInletVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 3)
)
ipmInletVoltageTooLow.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusVoltage"),
        ("IPOMANII-MIB", "inletConfigVoltageLow"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletVoltageTooLow.setStatus(
        ""
    )

ipmInletVoltageNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 4)
)
ipmInletVoltageNotTooLow.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusVoltage"),
        ("IPOMANII-MIB", "inletConfigVoltageLow"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletVoltageNotTooLow.setStatus(
        ""
    )

ipmInletCurrentTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 5)
)
ipmInletCurrentTooHigh.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusCurrent"),
        ("IPOMANII-MIB", "inletConfigCurrentHigh"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletCurrentTooHigh.setStatus(
        ""
    )

ipmInletCurrentNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 6)
)
ipmInletCurrentNotTooHigh.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusCurrent"),
        ("IPOMANII-MIB", "inletConfigCurrentHigh"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletCurrentNotTooHigh.setStatus(
        ""
    )

ipmInletFrequencyTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 7)
)
ipmInletFrequencyTooHigh.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusFrequency"),
        ("IPOMANII-MIB", "inletConfigFrequencyHigh"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletFrequencyTooHigh.setStatus(
        ""
    )

ipmInletFrequencyNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 8)
)
ipmInletFrequencyNotTooHigh.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusFrequency"),
        ("IPOMANII-MIB", "inletConfigFrequencyHigh"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletFrequencyNotTooHigh.setStatus(
        ""
    )

ipmInletFrequencyTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 9)
)
ipmInletFrequencyTooLow.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusFrequency"),
        ("IPOMANII-MIB", "inletConfigFrequencyLow"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletFrequencyTooLow.setStatus(
        ""
    )

ipmInletFrequencyNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 10)
)
ipmInletFrequencyNotTooLow.setObjects(
      *(("IPOMANII-MIB", "inletConfigIndex"),
        ("IPOMANII-MIB", "inletStatusFrequency"),
        ("IPOMANII-MIB", "inletConfigFrequencyLow"),
        ("IPOMANII-MIB", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmInletFrequencyNotTooLow.setStatus(
        ""
    )

ipmOutletCurrentTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 11)
)
ipmOutletCurrentTooHigh.setObjects(
      *(("IPOMANII-MIB", "outletConfigIndex"),
        ("IPOMANII-MIB", "outletStatusCurrent"),
        ("IPOMANII-MIB", "outletConfigCurrentHigh"),
        ("IPOMANII-MIB", "outletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmOutletCurrentTooHigh.setStatus(
        ""
    )

ipmOutletCurrentNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 12)
)
ipmOutletCurrentNotTooHigh.setObjects(
      *(("IPOMANII-MIB", "outletConfigIndex"),
        ("IPOMANII-MIB", "outletStatusCurrent"),
        ("IPOMANII-MIB", "outletConfigCurrentHigh"),
        ("IPOMANII-MIB", "outletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmOutletCurrentNotTooHigh.setStatus(
        ""
    )

ipmOutletStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 13)
)
ipmOutletStateChanged.setObjects(
      *(("IPOMANII-MIB", "outletConfigIndex"),
        ("IPOMANII-MIB", "outletStatusStatus"),
        ("IPOMANII-MIB", "outletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipmOutletStateChanged.setStatus(
        ""
    )

ipmEmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 14)
)
ipmEmdTemperatureNotHigh.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusTemperature"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempHighSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipmEmdTemperatureNotHigh.setStatus(
        ""
    )

ipmEmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 15)
)
ipmEmdTemperatureTooHigh.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusTemperature"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempHighSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipmEmdTemperatureTooHigh.setStatus(
        ""
    )

ipmEmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 16)
)
ipmEmdTemperatureNotLow.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusTemperature"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempLowSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipmEmdTemperatureNotLow.setStatus(
        ""
    )

ipmEmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 17)
)
ipmEmdTemperatureTooLow.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusTemperature"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempLowSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipmEmdTemperatureTooLow.setStatus(
        ""
    )

ipmEmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 18)
)
ipmEmdHumidityNotHigh.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusHumidity"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiHighSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipmEmdHumidityNotHigh.setStatus(
        ""
    )

ipmEmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 19)
)
ipmEmdHumidityTooHigh.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusHumidity"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiHighSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipmEmdHumidityTooHigh.setStatus(
        ""
    )

ipmEmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 20)
)
ipmEmdHumidityNotLow.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusHumidity"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiLowSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipmEmdHumidityNotLow.setStatus(
        ""
    )

ipmEmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 21)
)
ipmEmdHumidityTooLow.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdStatusHumidity"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiLowSetPoint"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipmEmdHumidityTooLow.setStatus(
        ""
    )

ipmEmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 22)
)
ipmEmdAlarm1Normal.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdConfigAlarm1Type"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    ipmEmdAlarm1Normal.setStatus(
        ""
    )

ipmEmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 23)
)
ipmEmdAlarm1Active.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdConfigAlarm1Type"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    ipmEmdAlarm1Active.setStatus(
        ""
    )

ipmEmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 24)
)
ipmEmdAlarm2Normal.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdConfigAlarm2Type"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    ipmEmdAlarm2Normal.setStatus(
        ""
    )

ipmEmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 25)
)
ipmEmdAlarm2Active.setObjects(
      *(("IPOMANII-MIB", "ipmEnvEmdConfigAlarm2Type"),
        ("IPOMANII-MIB", "ipmEnvEmdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    ipmEmdAlarm2Active.setStatus(
        ""
    )

ipmSlave01Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 26)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet01OverHigh.setStatus(
        ""
    )

ipmSlave01Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 27)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet01NotOverHigh.setStatus(
        ""
    )

ipmSlave01Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 28)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet02OverHigh.setStatus(
        ""
    )

ipmSlave01Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 29)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet02NotOverHigh.setStatus(
        ""
    )

ipmSlave01Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 30)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet01UnderLow.setStatus(
        ""
    )

ipmSlave01Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 31)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet01NotUnderLow.setStatus(
        ""
    )

ipmSlave01Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 32)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet02UnderLow.setStatus(
        ""
    )

ipmSlave01Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 33)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet02NotUnderLow.setStatus(
        ""
    )

ipmSlave01Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 34)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet01CurrentOverTh.setStatus(
        ""
    )

ipmSlave01Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 35)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave01Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 36)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet02CurrentOverTh.setStatus(
        ""
    )

ipmSlave01Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 37)
)
if mibBuilder.loadTexts:
    ipmSlave01Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave01EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 38)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdTemperatureNotHigh.setStatus(
        ""
    )

ipmSlave01EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 39)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdTemperatureTooHigh.setStatus(
        ""
    )

ipmSlave01EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 40)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdTemperatureNotLow.setStatus(
        ""
    )

ipmSlave01EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 41)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdTemperatureTooLow.setStatus(
        ""
    )

ipmSlave01EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 42)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdHumidityNotHigh.setStatus(
        ""
    )

ipmSlave01EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 43)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdHumidityTooHigh.setStatus(
        ""
    )

ipmSlave01EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 44)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdHumidityNotLow.setStatus(
        ""
    )

ipmSlave01EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 45)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdHumidityTooLow.setStatus(
        ""
    )

ipmSlave01EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 46)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdAlarm1Normal.setStatus(
        ""
    )

ipmSlave01EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 47)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdAlarm1Active.setStatus(
        ""
    )

ipmSlave01EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 48)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdAlarm2Normal.setStatus(
        ""
    )

ipmSlave01EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 49)
)
if mibBuilder.loadTexts:
    ipmSlave01EmdAlarm2Active.setStatus(
        ""
    )

ipmSlave01OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 50)
)
if mibBuilder.loadTexts:
    ipmSlave01OutletCurrentOverTh.setStatus(
        ""
    )

ipmSlave02Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 51)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet01OverHigh.setStatus(
        ""
    )

ipmSlave02Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 52)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet01NotOverHigh.setStatus(
        ""
    )

ipmSlave02Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 53)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet02OverHigh.setStatus(
        ""
    )

ipmSlave02Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 54)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet02NotOverHigh.setStatus(
        ""
    )

ipmSlave02Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 55)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet01UnderLow.setStatus(
        ""
    )

ipmSlave02Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 56)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet01NotUnderLow.setStatus(
        ""
    )

ipmSlave02Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 57)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet02UnderLow.setStatus(
        ""
    )

ipmSlave02Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 58)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet02NotUnderLow.setStatus(
        ""
    )

ipmSlave02Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 59)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet01CurrentOverTh.setStatus(
        ""
    )

ipmSlave02Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 60)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave02Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 61)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet02CurrentOverTh.setStatus(
        ""
    )

ipmSlave02Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 62)
)
if mibBuilder.loadTexts:
    ipmSlave02Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave02EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 63)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdTemperatureNotHigh.setStatus(
        ""
    )

ipmSlave02EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 64)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdTemperatureTooHigh.setStatus(
        ""
    )

ipmSlave02EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 65)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdTemperatureNotLow.setStatus(
        ""
    )

ipmSlave02EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 66)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdTemperatureTooLow.setStatus(
        ""
    )

ipmSlave02EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 67)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdHumidityNotHigh.setStatus(
        ""
    )

ipmSlave02EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 68)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdHumidityTooHigh.setStatus(
        ""
    )

ipmSlave02EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 69)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdHumidityNotLow.setStatus(
        ""
    )

ipmSlave02EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 70)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdHumidityTooLow.setStatus(
        ""
    )

ipmSlave02EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 71)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdAlarm1Normal.setStatus(
        ""
    )

ipmSlave02EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 72)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdAlarm1Active.setStatus(
        ""
    )

ipmSlave02EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 73)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdAlarm2Normal.setStatus(
        ""
    )

ipmSlave02EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 74)
)
if mibBuilder.loadTexts:
    ipmSlave02EmdAlarm2Active.setStatus(
        ""
    )

ipmSlave02OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 75)
)
if mibBuilder.loadTexts:
    ipmSlave02OutletCurrentOverTh.setStatus(
        ""
    )

ipmSlave03Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 76)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet01OverHigh.setStatus(
        ""
    )

ipmSlave03Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 77)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet01NotOverHigh.setStatus(
        ""
    )

ipmSlave03Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 78)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet02OverHigh.setStatus(
        ""
    )

ipmSlave03Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 79)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet02NotOverHigh.setStatus(
        ""
    )

ipmSlave03Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 80)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet01UnderLow.setStatus(
        ""
    )

ipmSlave03Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 81)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet01NotUnderLow.setStatus(
        ""
    )

ipmSlave03Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 82)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet02UnderLow.setStatus(
        ""
    )

ipmSlave03Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 83)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet02NotUnderLow.setStatus(
        ""
    )

ipmSlave03Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 84)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet01CurrentOverTh.setStatus(
        ""
    )

ipmSlave03Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 85)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave03Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 86)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet02CurrentOverTh.setStatus(
        ""
    )

ipmSlave03Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 87)
)
if mibBuilder.loadTexts:
    ipmSlave03Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave03EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 88)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdTemperatureNotHigh.setStatus(
        ""
    )

ipmSlave03EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 89)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdTemperatureTooHigh.setStatus(
        ""
    )

ipmSlave03EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 90)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdTemperatureNotLow.setStatus(
        ""
    )

ipmSlave03EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 91)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdTemperatureTooLow.setStatus(
        ""
    )

ipmSlave03EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 92)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdHumidityNotHigh.setStatus(
        ""
    )

ipmSlave03EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 93)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdHumidityTooHigh.setStatus(
        ""
    )

ipmSlave03EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 94)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdHumidityNotLow.setStatus(
        ""
    )

ipmSlave03EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 95)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdHumidityTooLow.setStatus(
        ""
    )

ipmSlave03EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 96)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdAlarm1Normal.setStatus(
        ""
    )

ipmSlave03EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 97)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdAlarm1Active.setStatus(
        ""
    )

ipmSlave03EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 98)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdAlarm2Normal.setStatus(
        ""
    )

ipmSlave03EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 99)
)
if mibBuilder.loadTexts:
    ipmSlave03EmdAlarm2Active.setStatus(
        ""
    )

ipmSlave03OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 100)
)
if mibBuilder.loadTexts:
    ipmSlave03OutletCurrentOverTh.setStatus(
        ""
    )

ipmSlave04Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 101)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet01OverHigh.setStatus(
        ""
    )

ipmSlave04Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 102)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet01NotOverHigh.setStatus(
        ""
    )

ipmSlave04Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 103)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet02OverHigh.setStatus(
        ""
    )

ipmSlave04Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 104)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet02NotOverHigh.setStatus(
        ""
    )

ipmSlave04Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 105)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet01UnderLow.setStatus(
        ""
    )

ipmSlave04Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 106)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet01NotUnderLow.setStatus(
        ""
    )

ipmSlave04Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 107)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet02UnderLow.setStatus(
        ""
    )

ipmSlave04Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 108)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet02NotUnderLow.setStatus(
        ""
    )

ipmSlave04Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 109)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet01CurrentOverTh.setStatus(
        ""
    )

ipmSlave04Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 110)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave04Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 111)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet02CurrentOverTh.setStatus(
        ""
    )

ipmSlave04Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 112)
)
if mibBuilder.loadTexts:
    ipmSlave04Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave04EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 113)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdTemperatureNotHigh.setStatus(
        ""
    )

ipmSlave04EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 114)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdTemperatureTooHigh.setStatus(
        ""
    )

ipmSlave04EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 115)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdTemperatureNotLow.setStatus(
        ""
    )

ipmSlave04EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 116)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdTemperatureTooLow.setStatus(
        ""
    )

ipmSlave04EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 117)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdHumidityNotHigh.setStatus(
        ""
    )

ipmSlave04EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 118)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdHumidityTooHigh.setStatus(
        ""
    )

ipmSlave04EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 119)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdHumidityNotLow.setStatus(
        ""
    )

ipmSlave04EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 120)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdHumidityTooLow.setStatus(
        ""
    )

ipmSlave04EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 121)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdAlarm1Normal.setStatus(
        ""
    )

ipmSlave04EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 122)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdAlarm1Active.setStatus(
        ""
    )

ipmSlave04EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 123)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdAlarm2Normal.setStatus(
        ""
    )

ipmSlave04EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 124)
)
if mibBuilder.loadTexts:
    ipmSlave04EmdAlarm2Active.setStatus(
        ""
    )

ipmSlave04OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 125)
)
if mibBuilder.loadTexts:
    ipmSlave04OutletCurrentOverTh.setStatus(
        ""
    )

ipmSlave05Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 126)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet01OverHigh.setStatus(
        ""
    )

ipmSlave05Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 127)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet01NotOverHigh.setStatus(
        ""
    )

ipmSlave05Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 128)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet02OverHigh.setStatus(
        ""
    )

ipmSlave05Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 129)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet02NotOverHigh.setStatus(
        ""
    )

ipmSlave05Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 130)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet01UnderLow.setStatus(
        ""
    )

ipmSlave05Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 131)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet01NotUnderLow.setStatus(
        ""
    )

ipmSlave05Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 132)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet02UnderLow.setStatus(
        ""
    )

ipmSlave05Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 133)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet02NotUnderLow.setStatus(
        ""
    )

ipmSlave05Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 134)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet01CurrentOverTh.setStatus(
        ""
    )

ipmSlave05Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 135)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave05Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 136)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet02CurrentOverTh.setStatus(
        ""
    )

ipmSlave05Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 137)
)
if mibBuilder.loadTexts:
    ipmSlave05Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipmSlave05EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 138)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdTemperatureNotHigh.setStatus(
        ""
    )

ipmSlave05EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 139)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdTemperatureTooHigh.setStatus(
        ""
    )

ipmSlave05EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 140)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdTemperatureNotLow.setStatus(
        ""
    )

ipmSlave05EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 141)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdTemperatureTooLow.setStatus(
        ""
    )

ipmSlave05EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 142)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdHumidityNotHigh.setStatus(
        ""
    )

ipmSlave05EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 143)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdHumidityTooHigh.setStatus(
        ""
    )

ipmSlave05EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 144)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdHumidityNotLow.setStatus(
        ""
    )

ipmSlave05EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 145)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdHumidityTooLow.setStatus(
        ""
    )

ipmSlave05EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 146)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdAlarm1Normal.setStatus(
        ""
    )

ipmSlave05EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 147)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdAlarm1Active.setStatus(
        ""
    )

ipmSlave05EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 148)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdAlarm2Normal.setStatus(
        ""
    )

ipmSlave05EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 149)
)
if mibBuilder.loadTexts:
    ipmSlave05EmdAlarm2Active.setStatus(
        ""
    )

ipmSlave05OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 4, 2, 2, 0, 150)
)
if mibBuilder.loadTexts:
    ipmSlave05OutletCurrentOverTh.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPOMANII-MIB",
    **{"ingrasys": ingrasys,
       "product": product,
       "pduAgent": pduAgent,
       "iPoManII": iPoManII,
       "ipmObjects": ipmObjects,
       "ipmIdent": ipmIdent,
       "ipmIdentManufacturer": ipmIdentManufacturer,
       "ipmIdentModel": ipmIdentModel,
       "ipmIdentAgentSoftwareVersion": ipmIdentAgentSoftwareVersion,
       "ipmIdentName": ipmIdentName,
       "ipmAgent": ipmAgent,
       "ipmAgentConfig": ipmAgentConfig,
       "ipmAgentMibVersion": ipmAgentMibVersion,
       "ipmAgentLog": ipmAgentLog,
       "pduAgentDataLogInterval": pduAgentDataLogInterval,
       "ipmAgentControl": ipmAgentControl,
       "ipmAgentControlDefault": ipmAgentControlDefault,
       "ipmAgentControlRestart": ipmAgentControlRestart,
       "ipmAgentTrap": ipmAgentTrap,
       "ipmAgentTrapRetryCount": ipmAgentTrapRetryCount,
       "ipmAgentTrapRetryTime": ipmAgentTrapRetryTime,
       "ipmAgentTrapAckSignature": ipmAgentTrapAckSignature,
       "ipmAgentTrapsReceiversTable": ipmAgentTrapsReceiversTable,
       "ipmAgentTrapsReceiversEntry": ipmAgentTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "receiverNmsType": receiverNmsType,
       "receiverSeverityLevel": receiverSeverityLevel,
       "receiverDescription": receiverDescription,
       "ipmAgentAccessControlTable": ipmAgentAccessControlTable,
       "ipmAgentAccessControlEntry": ipmAgentAccessControlEntry,
       "accessIndex": accessIndex,
       "accessControlAddr": accessControlAddr,
       "accessControlMode": accessControlMode,
       "ipmAgentTime": ipmAgentTime,
       "ipmAgentTimeDate": ipmAgentTimeDate,
       "ipmAgentTimeTime": ipmAgentTimeTime,
       "ipmAgentTimerFromNtp": ipmAgentTimerFromNtp,
       "ipmAgentNtpIpAddress": ipmAgentNtpIpAddress,
       "ipmAgentNtpTimeZone": ipmAgentNtpTimeZone,
       "ipmAgentDayLightSaving": ipmAgentDayLightSaving,
       "ipmAgentNetwork": ipmAgentNetwork,
       "ipmAgentNetworkIp": ipmAgentNetworkIp,
       "ipmAgentNetworkIpAdress": ipmAgentNetworkIpAdress,
       "ipmAgentNetworkIpGateway": ipmAgentNetworkIpGateway,
       "ipmAgentNetworkIpSubnet": ipmAgentNetworkIpSubnet,
       "ipmAgentNetworkDhcpControl": ipmAgentNetworkDhcpControl,
       "ipmAgentNetworkPingControl": ipmAgentNetworkPingControl,
       "ipmAgentNetworkTftpControl": ipmAgentNetworkTftpControl,
       "ipmAgentNetworkTelnet": ipmAgentNetworkTelnet,
       "ipmAgentTelnetControl": ipmAgentTelnetControl,
       "ipmAgentTelnetPort": ipmAgentTelnetPort,
       "ipmAgentNetworkHttp": ipmAgentNetworkHttp,
       "ipmAgentHttpControl": ipmAgentHttpControl,
       "ipmAgentHttpPort": ipmAgentHttpPort,
       "ipmAgentNetworkSnmp": ipmAgentNetworkSnmp,
       "ipmAgentSnmpControl": ipmAgentSnmpControl,
       "ipmAgentSnmpPort": ipmAgentSnmpPort,
       "ipmDevice": ipmDevice,
       "ipmDeviceInlet": ipmDeviceInlet,
       "ipmDeviceInletNumber": ipmDeviceInletNumber,
       "ipmDeviceInletConfigTable": ipmDeviceInletConfigTable,
       "ipmDeviceInletConfigEntry": ipmDeviceInletConfigEntry,
       "inletConfigIndex": inletConfigIndex,
       "inletConfigDesc": inletConfigDesc,
       "inletConfigVoltageHigh": inletConfigVoltageHigh,
       "inletConfigVoltageHighAction": inletConfigVoltageHighAction,
       "inletConfigVoltageLow": inletConfigVoltageLow,
       "inletConfigVoltageLowAction": inletConfigVoltageLowAction,
       "inletConfigCurrentHigh": inletConfigCurrentHigh,
       "inletConfigCurrentHighAction": inletConfigCurrentHighAction,
       "inletConfigFrequencyHigh": inletConfigFrequencyHigh,
       "inletConfigfrequencyHighAction": inletConfigfrequencyHighAction,
       "inletConfigFrequencyLow": inletConfigFrequencyLow,
       "inletConfigfrequencyLowAction": inletConfigfrequencyLowAction,
       "ipmDeviceInletStatusTable": ipmDeviceInletStatusTable,
       "ipmDeviceInletStatusEntry": ipmDeviceInletStatusEntry,
       "inletStatusIndex": inletStatusIndex,
       "inletStatusVoltage": inletStatusVoltage,
       "inletStatusCurrent": inletStatusCurrent,
       "inletStatusFrequency": inletStatusFrequency,
       "inletStatusKwatt": inletStatusKwatt,
       "inletStatusWH": inletStatusWH,
       "inletWattReset": inletWattReset,
       "ipmDeviceOutlet": ipmDeviceOutlet,
       "ipmDeviceOutletNumber": ipmDeviceOutletNumber,
       "ipmDeviceOutletConfigTable": ipmDeviceOutletConfigTable,
       "ipmDeviceOutletConfigEntry": ipmDeviceOutletConfigEntry,
       "outletConfigIndex": outletConfigIndex,
       "outletConfigDesc": outletConfigDesc,
       "outletConfigLocation": outletConfigLocation,
       "outletConfigOnDelay": outletConfigOnDelay,
       "outletConfigOffDelay": outletConfigOffDelay,
       "outletConfigCurrentHigh": outletConfigCurrentHigh,
       "outletConfigCurrentHighAction": outletConfigCurrentHighAction,
       "ipmDeviceOutletStatusTable": ipmDeviceOutletStatusTable,
       "ipmDeviceOutletStatusEntry": ipmDeviceOutletStatusEntry,
       "outletStatusIndex": outletStatusIndex,
       "outletStatusStatus": outletStatusStatus,
       "outletStatusCurrent": outletStatusCurrent,
       "outletStatusKwatt": outletStatusKwatt,
       "outletStatusWH": outletStatusWH,
       "outletStatusStateTime": outletStatusStateTime,
       "outletStatusTimeToGo": outletStatusTimeToGo,
       "ipmDeviceOutletControlTable": ipmDeviceOutletControlTable,
       "ipmDeviceOutletControlEntry": ipmDeviceOutletControlEntry,
       "outletControlIndex": outletControlIndex,
       "outletControlControl": outletControlControl,
       "ipmDeviceOutletControlAll": ipmDeviceOutletControlAll,
       "ipmDeviceOutletWattReset": ipmDeviceOutletWattReset,
       "ipmDeviceCcOut": ipmDeviceCcOut,
       "ipmDeviceCcOutNumber": ipmDeviceCcOutNumber,
       "ipmDeviceCcOutConfigTable": ipmDeviceCcOutConfigTable,
       "ipmDeviceCcOutConfigEntry": ipmDeviceCcOutConfigEntry,
       "ccOutConfigIndex": ccOutConfigIndex,
       "ccOutConfigDesc": ccOutConfigDesc,
       "ccOutConfigEventAction": ccOutConfigEventAction,
       "ccOutConfigCloseDelay": ccOutConfigCloseDelay,
       "ccOutConfigOpenDelay": ccOutConfigOpenDelay,
       "ipmDeviceCcOutStatusTable": ipmDeviceCcOutStatusTable,
       "ipmDeviceCcOutStatusEntry": ipmDeviceCcOutStatusEntry,
       "ccOutStatusIndex": ccOutStatusIndex,
       "ccOutStatusStatus": ccOutStatusStatus,
       "ccOutStatusTimeOnState": ccOutStatusTimeOnState,
       "ipmDeviceCcOutControlTable": ipmDeviceCcOutControlTable,
       "ipmDeviceCcOutControlEntry": ipmDeviceCcOutControlEntry,
       "ccOutControlIndex": ccOutControlIndex,
       "ccOutControlControl": ccOutControlControl,
       "ipmSlave": ipmSlave,
       "ipmSlaveState": ipmSlaveState,
       "ipmSlaveStateTable": ipmSlaveStateTable,
       "ipmSlaveStateEntry": ipmSlaveStateEntry,
       "slaveStateIndex": slaveStateIndex,
       "slaveStateControl01": slaveStateControl01,
       "ipmSlaveInlet": ipmSlaveInlet,
       "ipmSlaveInletStatus": ipmSlaveInletStatus,
       "ipmDeviceSlaveInletStatusTable": ipmDeviceSlaveInletStatusTable,
       "ipmDeviceSlaveInletStatusEntry": ipmDeviceSlaveInletStatusEntry,
       "inletSlaveStatusIndex": inletSlaveStatusIndex,
       "inletSlaveStatusVoltage": inletSlaveStatusVoltage,
       "inletSlaveStatusCurrent": inletSlaveStatusCurrent,
       "inletSlaveStatusFrequency": inletSlaveStatusFrequency,
       "inletSlaveStatusKwatt": inletSlaveStatusKwatt,
       "inletSlaveStatusWH": inletSlaveStatusWH,
       "inletSlaveStatusVoltage2": inletSlaveStatusVoltage2,
       "inletSlaveStatusCurrent2": inletSlaveStatusCurrent2,
       "inletSlaveStatusFrequency2": inletSlaveStatusFrequency2,
       "inletSlaveStatusKwatt2": inletSlaveStatusKwatt2,
       "inletSlaveStatusWH2": inletSlaveStatusWH2,
       "ipmSlaveInletConfig": ipmSlaveInletConfig,
       "ipmDeviceslaveInletConfigTable": ipmDeviceslaveInletConfigTable,
       "ipmDeviceslaveInletConfigEntry": ipmDeviceslaveInletConfigEntry,
       "slaveInletConfigIndex": slaveInletConfigIndex,
       "slaveInletConfigVoltageHigh": slaveInletConfigVoltageHigh,
       "slaveInletConfigVoltageLow": slaveInletConfigVoltageLow,
       "slaveInlet2ConfigVoltageHigh": slaveInlet2ConfigVoltageHigh,
       "slaveInlet2ConfigVoltageLow": slaveInlet2ConfigVoltageLow,
       "ipmSlaveOutlet": ipmSlaveOutlet,
       "ipmSlaveOutletConfig": ipmSlaveOutletConfig,
       "ipmSlaveDeviceOutletNameTable": ipmSlaveDeviceOutletNameTable,
       "ipmSlaveDeviceOutletNameEntry": ipmSlaveDeviceOutletNameEntry,
       "slaveOutletNameIndex": slaveOutletNameIndex,
       "slaveOutletName01": slaveOutletName01,
       "slaveOutletName02": slaveOutletName02,
       "slaveOutletName03": slaveOutletName03,
       "slaveOutletName04": slaveOutletName04,
       "slaveOutletName05": slaveOutletName05,
       "slaveOutletName06": slaveOutletName06,
       "slaveOutletName07": slaveOutletName07,
       "slaveOutletName08": slaveOutletName08,
       "slaveOutletName09": slaveOutletName09,
       "slaveOutletName10": slaveOutletName10,
       "slaveOutletName11": slaveOutletName11,
       "slaveOutletName12": slaveOutletName12,
       "ipmSlaveDeviceOutletLocationTable": ipmSlaveDeviceOutletLocationTable,
       "ipmSlaveDeviceOutletLocationEntry": ipmSlaveDeviceOutletLocationEntry,
       "slaveOutletLocationIndex": slaveOutletLocationIndex,
       "slaveOutletLocation01": slaveOutletLocation01,
       "slaveOutletLocation02": slaveOutletLocation02,
       "slaveOutletLocation03": slaveOutletLocation03,
       "slaveOutletLocation04": slaveOutletLocation04,
       "slaveOutletLocation05": slaveOutletLocation05,
       "slaveOutletLocation06": slaveOutletLocation06,
       "slaveOutletLocation07": slaveOutletLocation07,
       "slaveOutletLocation08": slaveOutletLocation08,
       "slaveOutletLocation09": slaveOutletLocation09,
       "slaveOutletLocation10": slaveOutletLocation10,
       "slaveOutletLocation11": slaveOutletLocation11,
       "slaveOutletLocation12": slaveOutletLocation12,
       "ipmSlaveDeviceOutletOnTimeTable": ipmSlaveDeviceOutletOnTimeTable,
       "ipmSlaveDeviceOutletOnTimeEntry": ipmSlaveDeviceOutletOnTimeEntry,
       "slaveOutletOnTimeIndex": slaveOutletOnTimeIndex,
       "slaveOutletOnTime01": slaveOutletOnTime01,
       "slaveOutletOnTime02": slaveOutletOnTime02,
       "slaveOutletOnTime03": slaveOutletOnTime03,
       "slaveOutletOnTime04": slaveOutletOnTime04,
       "slaveOutletOnTime05": slaveOutletOnTime05,
       "slaveOutletOnTime06": slaveOutletOnTime06,
       "slaveOutletOnTime07": slaveOutletOnTime07,
       "slaveOutletOnTime08": slaveOutletOnTime08,
       "slaveOutletOnTime09": slaveOutletOnTime09,
       "slaveOutletOnTime10": slaveOutletOnTime10,
       "slaveOutletOnTime11": slaveOutletOnTime11,
       "slaveOutletOnTime12": slaveOutletOnTime12,
       "ipmSlaveDeviceOutletOffTimeTable": ipmSlaveDeviceOutletOffTimeTable,
       "ipmSlaveDeviceOutletOffTimeEntry": ipmSlaveDeviceOutletOffTimeEntry,
       "slaveOutletOffTimeIndex": slaveOutletOffTimeIndex,
       "slaveOutletOffTime01": slaveOutletOffTime01,
       "slaveOutletOffTime02": slaveOutletOffTime02,
       "slaveOutletOffTime03": slaveOutletOffTime03,
       "slaveOutletOffTime04": slaveOutletOffTime04,
       "slaveOutletOffTime05": slaveOutletOffTime05,
       "slaveOutletOffTime06": slaveOutletOffTime06,
       "slaveOutletOffTime07": slaveOutletOffTime07,
       "slaveOutletOffTime08": slaveOutletOffTime08,
       "slaveOutletOffTime09": slaveOutletOffTime09,
       "slaveOutletOffTime10": slaveOutletOffTime10,
       "slaveOutletOffTime11": slaveOutletOffTime11,
       "slaveOutletOffTime12": slaveOutletOffTime12,
       "ipmSlaveDeviceOutletCurrThTable": ipmSlaveDeviceOutletCurrThTable,
       "ipmSlaveDeviceOutletCurrThEntry": ipmSlaveDeviceOutletCurrThEntry,
       "slaveOutletCurrThIndex": slaveOutletCurrThIndex,
       "slaveOutletCurrTh01": slaveOutletCurrTh01,
       "slaveOutletCurrTh02": slaveOutletCurrTh02,
       "slaveOutletCurrTh03": slaveOutletCurrTh03,
       "slaveOutletCurrTh04": slaveOutletCurrTh04,
       "slaveOutletCurrTh05": slaveOutletCurrTh05,
       "slaveOutletCurrTh06": slaveOutletCurrTh06,
       "slaveOutletCurrTh07": slaveOutletCurrTh07,
       "slaveOutletCurrTh08": slaveOutletCurrTh08,
       "slaveOutletCurrTh09": slaveOutletCurrTh09,
       "slaveOutletCurrTh10": slaveOutletCurrTh10,
       "slaveOutletCurrTh11": slaveOutletCurrTh11,
       "slaveOutletCurrTh12": slaveOutletCurrTh12,
       "ipmSlaveOutletStatus": ipmSlaveOutletStatus,
       "ipmSlaveDeviceOutletCurrentTable": ipmSlaveDeviceOutletCurrentTable,
       "ipmSlaveDeviceOutletCurrentEntry": ipmSlaveDeviceOutletCurrentEntry,
       "slaveOutletCurrentIndex": slaveOutletCurrentIndex,
       "slaveOutletCurrent01": slaveOutletCurrent01,
       "slaveOutletCurrent02": slaveOutletCurrent02,
       "slaveOutletCurrent03": slaveOutletCurrent03,
       "slaveOutletCurrent04": slaveOutletCurrent04,
       "slaveOutletCurrent05": slaveOutletCurrent05,
       "slaveOutletCurrent06": slaveOutletCurrent06,
       "slaveOutletCurrent07": slaveOutletCurrent07,
       "slaveOutletCurrent08": slaveOutletCurrent08,
       "slaveOutletCurrent09": slaveOutletCurrent09,
       "slaveOutletCurrent10": slaveOutletCurrent10,
       "slaveOutletCurrent11": slaveOutletCurrent11,
       "slaveOutletCurrent12": slaveOutletCurrent12,
       "ipmSlaveDeviceOutletWattTable": ipmSlaveDeviceOutletWattTable,
       "ipmSlaveDeviceOutletWattEntry": ipmSlaveDeviceOutletWattEntry,
       "slaveOutletWattIndex": slaveOutletWattIndex,
       "slaveOutletWatt01": slaveOutletWatt01,
       "slaveOutletWatt02": slaveOutletWatt02,
       "slaveOutletWatt03": slaveOutletWatt03,
       "slaveOutletWatt04": slaveOutletWatt04,
       "slaveOutletWatt05": slaveOutletWatt05,
       "slaveOutletWatt06": slaveOutletWatt06,
       "slaveOutletWatt07": slaveOutletWatt07,
       "slaveOutletWatt08": slaveOutletWatt08,
       "slaveOutletWatt09": slaveOutletWatt09,
       "slaveOutletWatt10": slaveOutletWatt10,
       "slaveOutletWatt11": slaveOutletWatt11,
       "slaveOutletWatt12": slaveOutletWatt12,
       "ipmSlaveDeviceOutletKwattTable": ipmSlaveDeviceOutletKwattTable,
       "ipmSlaveDeviceOutletKwattEntry": ipmSlaveDeviceOutletKwattEntry,
       "slaveOutletKwattIndex": slaveOutletKwattIndex,
       "slaveOutletKwatt01": slaveOutletKwatt01,
       "slaveOutletKwatt02": slaveOutletKwatt02,
       "slaveOutletKwatt03": slaveOutletKwatt03,
       "slaveOutletKwatt04": slaveOutletKwatt04,
       "slaveOutletKwatt05": slaveOutletKwatt05,
       "slaveOutletKwatt06": slaveOutletKwatt06,
       "slaveOutletKwatt07": slaveOutletKwatt07,
       "slaveOutletKwatt08": slaveOutletKwatt08,
       "slaveOutletKwatt09": slaveOutletKwatt09,
       "slaveOutletKwatt10": slaveOutletKwatt10,
       "slaveOutletKwatt11": slaveOutletKwatt11,
       "slaveOutletKwatt12": slaveOutletKwatt12,
       "ipmSlaveOutletAction": ipmSlaveOutletAction,
       "ipmSlaveDeviceOutletActionTable": ipmSlaveDeviceOutletActionTable,
       "ipmSlaveDeviceOutletActionEntry": ipmSlaveDeviceOutletActionEntry,
       "slaveOutletActionIndex": slaveOutletActionIndex,
       "slaveOutletAction01": slaveOutletAction01,
       "slaveOutletAction02": slaveOutletAction02,
       "slaveOutletAction03": slaveOutletAction03,
       "slaveOutletAction04": slaveOutletAction04,
       "slaveOutletAction05": slaveOutletAction05,
       "slaveOutletAction06": slaveOutletAction06,
       "slaveOutletAction07": slaveOutletAction07,
       "slaveOutletAction08": slaveOutletAction08,
       "slaveOutletAction09": slaveOutletAction09,
       "slaveOutletAction10": slaveOutletAction10,
       "slaveOutletAction11": slaveOutletAction11,
       "slaveOutletAction12": slaveOutletAction12,
       "ipmEnv": ipmEnv,
       "ipmEnvEmd": ipmEnvEmd,
       "ipmEnvEmdStatus": ipmEnvEmdStatus,
       "ipmEnvEmdStatusEmdType": ipmEnvEmdStatusEmdType,
       "ipmEnvEmdStatusTemperature": ipmEnvEmdStatusTemperature,
       "ipmEnvEmdStatusHumidity": ipmEnvEmdStatusHumidity,
       "ipmEnvEmdStatusAlarm1": ipmEnvEmdStatusAlarm1,
       "ipmEnvEmdStatusAlarm2": ipmEnvEmdStatusAlarm2,
       "ipmEnvEmdConfig": ipmEnvEmdConfig,
       "ipmEnvEmdConfigEmdPresence": ipmEnvEmdConfigEmdPresence,
       "ipmEnvEmdConfigEmdName": ipmEnvEmdConfigEmdName,
       "ipmEnvEmdConfigTemp": ipmEnvEmdConfigTemp,
       "ipmEnvEmdConfigTempName": ipmEnvEmdConfigTempName,
       "ipmEnvEmdConfigTempHighSetPoint": ipmEnvEmdConfigTempHighSetPoint,
       "ipmEnvEmdConfigTempHighStatus": ipmEnvEmdConfigTempHighStatus,
       "ipmEnvEmdConfigTempLowSetPoint": ipmEnvEmdConfigTempLowSetPoint,
       "ipmEnvEmdConfigTempLowStatus": ipmEnvEmdConfigTempLowStatus,
       "ipmEnvEmdConfigTempOffset": ipmEnvEmdConfigTempOffset,
       "ipmEnvEmdConfigHumi": ipmEnvEmdConfigHumi,
       "ipmEnvEmdConfigHumiName": ipmEnvEmdConfigHumiName,
       "ipmEnvEmdConfigHumiHighSetPoint": ipmEnvEmdConfigHumiHighSetPoint,
       "ipmEnvEmdConfigHumiHighStatus": ipmEnvEmdConfigHumiHighStatus,
       "ipmEnvEmdConfigHumiLowSetPoint": ipmEnvEmdConfigHumiLowSetPoint,
       "ipmEnvEmdConfigHumiLowStatus": ipmEnvEmdConfigHumiLowStatus,
       "ipmEnvEmdConfigHumiOffset": ipmEnvEmdConfigHumiOffset,
       "ipmEnvEmdConfigAlarm1": ipmEnvEmdConfigAlarm1,
       "ipmEnvEmdConfigAlarm1Name": ipmEnvEmdConfigAlarm1Name,
       "ipmEnvEmdConfigAlarm1Type": ipmEnvEmdConfigAlarm1Type,
       "ipmEnvEmdConfigAlarm2": ipmEnvEmdConfigAlarm2,
       "ipmEnvEmdConfigAlarm2Name": ipmEnvEmdConfigAlarm2Name,
       "ipmEnvEmdConfigAlarm2Type": ipmEnvEmdConfigAlarm2Type,
       "ipmTraps": ipmTraps,
       "ipmInletVoltageTooHigh": ipmInletVoltageTooHigh,
       "ipmInletVoltageNotTooHigh": ipmInletVoltageNotTooHigh,
       "ipmInletVoltageTooLow": ipmInletVoltageTooLow,
       "ipmInletVoltageNotTooLow": ipmInletVoltageNotTooLow,
       "ipmInletCurrentTooHigh": ipmInletCurrentTooHigh,
       "ipmInletCurrentNotTooHigh": ipmInletCurrentNotTooHigh,
       "ipmInletFrequencyTooHigh": ipmInletFrequencyTooHigh,
       "ipmInletFrequencyNotTooHigh": ipmInletFrequencyNotTooHigh,
       "ipmInletFrequencyTooLow": ipmInletFrequencyTooLow,
       "ipmInletFrequencyNotTooLow": ipmInletFrequencyNotTooLow,
       "ipmOutletCurrentTooHigh": ipmOutletCurrentTooHigh,
       "ipmOutletCurrentNotTooHigh": ipmOutletCurrentNotTooHigh,
       "ipmOutletStateChanged": ipmOutletStateChanged,
       "ipmEmdTemperatureNotHigh": ipmEmdTemperatureNotHigh,
       "ipmEmdTemperatureTooHigh": ipmEmdTemperatureTooHigh,
       "ipmEmdTemperatureNotLow": ipmEmdTemperatureNotLow,
       "ipmEmdTemperatureTooLow": ipmEmdTemperatureTooLow,
       "ipmEmdHumidityNotHigh": ipmEmdHumidityNotHigh,
       "ipmEmdHumidityTooHigh": ipmEmdHumidityTooHigh,
       "ipmEmdHumidityNotLow": ipmEmdHumidityNotLow,
       "ipmEmdHumidityTooLow": ipmEmdHumidityTooLow,
       "ipmEmdAlarm1Normal": ipmEmdAlarm1Normal,
       "ipmEmdAlarm1Active": ipmEmdAlarm1Active,
       "ipmEmdAlarm2Normal": ipmEmdAlarm2Normal,
       "ipmEmdAlarm2Active": ipmEmdAlarm2Active,
       "ipmSlave01Inlet01OverHigh": ipmSlave01Inlet01OverHigh,
       "ipmSlave01Inlet01NotOverHigh": ipmSlave01Inlet01NotOverHigh,
       "ipmSlave01Inlet02OverHigh": ipmSlave01Inlet02OverHigh,
       "ipmSlave01Inlet02NotOverHigh": ipmSlave01Inlet02NotOverHigh,
       "ipmSlave01Inlet01UnderLow": ipmSlave01Inlet01UnderLow,
       "ipmSlave01Inlet01NotUnderLow": ipmSlave01Inlet01NotUnderLow,
       "ipmSlave01Inlet02UnderLow": ipmSlave01Inlet02UnderLow,
       "ipmSlave01Inlet02NotUnderLow": ipmSlave01Inlet02NotUnderLow,
       "ipmSlave01Inlet01CurrentOverTh": ipmSlave01Inlet01CurrentOverTh,
       "ipmSlave01Inlet01NotCurrentOverTh": ipmSlave01Inlet01NotCurrentOverTh,
       "ipmSlave01Inlet02CurrentOverTh": ipmSlave01Inlet02CurrentOverTh,
       "ipmSlave01Inlet02NotCurrentOverTh": ipmSlave01Inlet02NotCurrentOverTh,
       "ipmSlave01EmdTemperatureNotHigh": ipmSlave01EmdTemperatureNotHigh,
       "ipmSlave01EmdTemperatureTooHigh": ipmSlave01EmdTemperatureTooHigh,
       "ipmSlave01EmdTemperatureNotLow": ipmSlave01EmdTemperatureNotLow,
       "ipmSlave01EmdTemperatureTooLow": ipmSlave01EmdTemperatureTooLow,
       "ipmSlave01EmdHumidityNotHigh": ipmSlave01EmdHumidityNotHigh,
       "ipmSlave01EmdHumidityTooHigh": ipmSlave01EmdHumidityTooHigh,
       "ipmSlave01EmdHumidityNotLow": ipmSlave01EmdHumidityNotLow,
       "ipmSlave01EmdHumidityTooLow": ipmSlave01EmdHumidityTooLow,
       "ipmSlave01EmdAlarm1Normal": ipmSlave01EmdAlarm1Normal,
       "ipmSlave01EmdAlarm1Active": ipmSlave01EmdAlarm1Active,
       "ipmSlave01EmdAlarm2Normal": ipmSlave01EmdAlarm2Normal,
       "ipmSlave01EmdAlarm2Active": ipmSlave01EmdAlarm2Active,
       "ipmSlave01OutletCurrentOverTh": ipmSlave01OutletCurrentOverTh,
       "ipmSlave02Inlet01OverHigh": ipmSlave02Inlet01OverHigh,
       "ipmSlave02Inlet01NotOverHigh": ipmSlave02Inlet01NotOverHigh,
       "ipmSlave02Inlet02OverHigh": ipmSlave02Inlet02OverHigh,
       "ipmSlave02Inlet02NotOverHigh": ipmSlave02Inlet02NotOverHigh,
       "ipmSlave02Inlet01UnderLow": ipmSlave02Inlet01UnderLow,
       "ipmSlave02Inlet01NotUnderLow": ipmSlave02Inlet01NotUnderLow,
       "ipmSlave02Inlet02UnderLow": ipmSlave02Inlet02UnderLow,
       "ipmSlave02Inlet02NotUnderLow": ipmSlave02Inlet02NotUnderLow,
       "ipmSlave02Inlet01CurrentOverTh": ipmSlave02Inlet01CurrentOverTh,
       "ipmSlave02Inlet01NotCurrentOverTh": ipmSlave02Inlet01NotCurrentOverTh,
       "ipmSlave02Inlet02CurrentOverTh": ipmSlave02Inlet02CurrentOverTh,
       "ipmSlave02Inlet02NotCurrentOverTh": ipmSlave02Inlet02NotCurrentOverTh,
       "ipmSlave02EmdTemperatureNotHigh": ipmSlave02EmdTemperatureNotHigh,
       "ipmSlave02EmdTemperatureTooHigh": ipmSlave02EmdTemperatureTooHigh,
       "ipmSlave02EmdTemperatureNotLow": ipmSlave02EmdTemperatureNotLow,
       "ipmSlave02EmdTemperatureTooLow": ipmSlave02EmdTemperatureTooLow,
       "ipmSlave02EmdHumidityNotHigh": ipmSlave02EmdHumidityNotHigh,
       "ipmSlave02EmdHumidityTooHigh": ipmSlave02EmdHumidityTooHigh,
       "ipmSlave02EmdHumidityNotLow": ipmSlave02EmdHumidityNotLow,
       "ipmSlave02EmdHumidityTooLow": ipmSlave02EmdHumidityTooLow,
       "ipmSlave02EmdAlarm1Normal": ipmSlave02EmdAlarm1Normal,
       "ipmSlave02EmdAlarm1Active": ipmSlave02EmdAlarm1Active,
       "ipmSlave02EmdAlarm2Normal": ipmSlave02EmdAlarm2Normal,
       "ipmSlave02EmdAlarm2Active": ipmSlave02EmdAlarm2Active,
       "ipmSlave02OutletCurrentOverTh": ipmSlave02OutletCurrentOverTh,
       "ipmSlave03Inlet01OverHigh": ipmSlave03Inlet01OverHigh,
       "ipmSlave03Inlet01NotOverHigh": ipmSlave03Inlet01NotOverHigh,
       "ipmSlave03Inlet02OverHigh": ipmSlave03Inlet02OverHigh,
       "ipmSlave03Inlet02NotOverHigh": ipmSlave03Inlet02NotOverHigh,
       "ipmSlave03Inlet01UnderLow": ipmSlave03Inlet01UnderLow,
       "ipmSlave03Inlet01NotUnderLow": ipmSlave03Inlet01NotUnderLow,
       "ipmSlave03Inlet02UnderLow": ipmSlave03Inlet02UnderLow,
       "ipmSlave03Inlet02NotUnderLow": ipmSlave03Inlet02NotUnderLow,
       "ipmSlave03Inlet01CurrentOverTh": ipmSlave03Inlet01CurrentOverTh,
       "ipmSlave03Inlet01NotCurrentOverTh": ipmSlave03Inlet01NotCurrentOverTh,
       "ipmSlave03Inlet02CurrentOverTh": ipmSlave03Inlet02CurrentOverTh,
       "ipmSlave03Inlet02NotCurrentOverTh": ipmSlave03Inlet02NotCurrentOverTh,
       "ipmSlave03EmdTemperatureNotHigh": ipmSlave03EmdTemperatureNotHigh,
       "ipmSlave03EmdTemperatureTooHigh": ipmSlave03EmdTemperatureTooHigh,
       "ipmSlave03EmdTemperatureNotLow": ipmSlave03EmdTemperatureNotLow,
       "ipmSlave03EmdTemperatureTooLow": ipmSlave03EmdTemperatureTooLow,
       "ipmSlave03EmdHumidityNotHigh": ipmSlave03EmdHumidityNotHigh,
       "ipmSlave03EmdHumidityTooHigh": ipmSlave03EmdHumidityTooHigh,
       "ipmSlave03EmdHumidityNotLow": ipmSlave03EmdHumidityNotLow,
       "ipmSlave03EmdHumidityTooLow": ipmSlave03EmdHumidityTooLow,
       "ipmSlave03EmdAlarm1Normal": ipmSlave03EmdAlarm1Normal,
       "ipmSlave03EmdAlarm1Active": ipmSlave03EmdAlarm1Active,
       "ipmSlave03EmdAlarm2Normal": ipmSlave03EmdAlarm2Normal,
       "ipmSlave03EmdAlarm2Active": ipmSlave03EmdAlarm2Active,
       "ipmSlave03OutletCurrentOverTh": ipmSlave03OutletCurrentOverTh,
       "ipmSlave04Inlet01OverHigh": ipmSlave04Inlet01OverHigh,
       "ipmSlave04Inlet01NotOverHigh": ipmSlave04Inlet01NotOverHigh,
       "ipmSlave04Inlet02OverHigh": ipmSlave04Inlet02OverHigh,
       "ipmSlave04Inlet02NotOverHigh": ipmSlave04Inlet02NotOverHigh,
       "ipmSlave04Inlet01UnderLow": ipmSlave04Inlet01UnderLow,
       "ipmSlave04Inlet01NotUnderLow": ipmSlave04Inlet01NotUnderLow,
       "ipmSlave04Inlet02UnderLow": ipmSlave04Inlet02UnderLow,
       "ipmSlave04Inlet02NotUnderLow": ipmSlave04Inlet02NotUnderLow,
       "ipmSlave04Inlet01CurrentOverTh": ipmSlave04Inlet01CurrentOverTh,
       "ipmSlave04Inlet01NotCurrentOverTh": ipmSlave04Inlet01NotCurrentOverTh,
       "ipmSlave04Inlet02CurrentOverTh": ipmSlave04Inlet02CurrentOverTh,
       "ipmSlave04Inlet02NotCurrentOverTh": ipmSlave04Inlet02NotCurrentOverTh,
       "ipmSlave04EmdTemperatureNotHigh": ipmSlave04EmdTemperatureNotHigh,
       "ipmSlave04EmdTemperatureTooHigh": ipmSlave04EmdTemperatureTooHigh,
       "ipmSlave04EmdTemperatureNotLow": ipmSlave04EmdTemperatureNotLow,
       "ipmSlave04EmdTemperatureTooLow": ipmSlave04EmdTemperatureTooLow,
       "ipmSlave04EmdHumidityNotHigh": ipmSlave04EmdHumidityNotHigh,
       "ipmSlave04EmdHumidityTooHigh": ipmSlave04EmdHumidityTooHigh,
       "ipmSlave04EmdHumidityNotLow": ipmSlave04EmdHumidityNotLow,
       "ipmSlave04EmdHumidityTooLow": ipmSlave04EmdHumidityTooLow,
       "ipmSlave04EmdAlarm1Normal": ipmSlave04EmdAlarm1Normal,
       "ipmSlave04EmdAlarm1Active": ipmSlave04EmdAlarm1Active,
       "ipmSlave04EmdAlarm2Normal": ipmSlave04EmdAlarm2Normal,
       "ipmSlave04EmdAlarm2Active": ipmSlave04EmdAlarm2Active,
       "ipmSlave04OutletCurrentOverTh": ipmSlave04OutletCurrentOverTh,
       "ipmSlave05Inlet01OverHigh": ipmSlave05Inlet01OverHigh,
       "ipmSlave05Inlet01NotOverHigh": ipmSlave05Inlet01NotOverHigh,
       "ipmSlave05Inlet02OverHigh": ipmSlave05Inlet02OverHigh,
       "ipmSlave05Inlet02NotOverHigh": ipmSlave05Inlet02NotOverHigh,
       "ipmSlave05Inlet01UnderLow": ipmSlave05Inlet01UnderLow,
       "ipmSlave05Inlet01NotUnderLow": ipmSlave05Inlet01NotUnderLow,
       "ipmSlave05Inlet02UnderLow": ipmSlave05Inlet02UnderLow,
       "ipmSlave05Inlet02NotUnderLow": ipmSlave05Inlet02NotUnderLow,
       "ipmSlave05Inlet01CurrentOverTh": ipmSlave05Inlet01CurrentOverTh,
       "ipmSlave05Inlet01NotCurrentOverTh": ipmSlave05Inlet01NotCurrentOverTh,
       "ipmSlave05Inlet02CurrentOverTh": ipmSlave05Inlet02CurrentOverTh,
       "ipmSlave05Inlet02NotCurrentOverTh": ipmSlave05Inlet02NotCurrentOverTh,
       "ipmSlave05EmdTemperatureNotHigh": ipmSlave05EmdTemperatureNotHigh,
       "ipmSlave05EmdTemperatureTooHigh": ipmSlave05EmdTemperatureTooHigh,
       "ipmSlave05EmdTemperatureNotLow": ipmSlave05EmdTemperatureNotLow,
       "ipmSlave05EmdTemperatureTooLow": ipmSlave05EmdTemperatureTooLow,
       "ipmSlave05EmdHumidityNotHigh": ipmSlave05EmdHumidityNotHigh,
       "ipmSlave05EmdHumidityTooHigh": ipmSlave05EmdHumidityTooHigh,
       "ipmSlave05EmdHumidityNotLow": ipmSlave05EmdHumidityNotLow,
       "ipmSlave05EmdHumidityTooLow": ipmSlave05EmdHumidityTooLow,
       "ipmSlave05EmdAlarm1Normal": ipmSlave05EmdAlarm1Normal,
       "ipmSlave05EmdAlarm1Active": ipmSlave05EmdAlarm1Active,
       "ipmSlave05EmdAlarm2Normal": ipmSlave05EmdAlarm2Normal,
       "ipmSlave05EmdAlarm2Active": ipmSlave05EmdAlarm2Active,
       "ipmSlave05OutletCurrentOverTh": ipmSlave05OutletCurrentOverTh}
)
