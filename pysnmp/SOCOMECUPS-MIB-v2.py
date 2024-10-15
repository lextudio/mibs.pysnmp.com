# SNMP MIB module (SOCOMECUPS-MIB-v2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SOCOMECUPS-MIB-v2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:32 2024
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

_SocomecSicon_ObjectIdentity = ObjectIdentity
socomecSicon = _SocomecSicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1)
)
_PduAgent_ObjectIdentity = ObjectIdentity
pduAgent = _PduAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1)
)
_IPDU_ObjectIdentity = ObjectIdentity
iPDU = _IPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20)
)
_IpduObjects_ObjectIdentity = ObjectIdentity
ipduObjects = _IpduObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1)
)
_IpduIdent_ObjectIdentity = ObjectIdentity
ipduIdent = _IpduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 1)
)


class _IpduIdentManufacturer_Type(DisplayString):
    """Custom type ipduIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduIdentManufacturer_Type.__name__ = "DisplayString"
_IpduIdentManufacturer_Object = MibScalar
ipduIdentManufacturer = _IpduIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 1, 1),
    _IpduIdentManufacturer_Type()
)
ipduIdentManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduIdentManufacturer.setStatus("mandatory")


class _IpduIdentModel_Type(DisplayString):
    """Custom type ipduIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduIdentModel_Type.__name__ = "DisplayString"
_IpduIdentModel_Object = MibScalar
ipduIdentModel = _IpduIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 1, 2),
    _IpduIdentModel_Type()
)
ipduIdentModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduIdentModel.setStatus("mandatory")


class _IpduIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type ipduIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IpduIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_IpduIdentAgentSoftwareVersion_Object = MibScalar
ipduIdentAgentSoftwareVersion = _IpduIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 1, 3),
    _IpduIdentAgentSoftwareVersion_Type()
)
ipduIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduIdentAgentSoftwareVersion.setStatus("mandatory")


class _IpduIdentName_Type(DisplayString):
    """Custom type ipduIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduIdentName_Type.__name__ = "DisplayString"
_IpduIdentName_Object = MibScalar
ipduIdentName = _IpduIdentName_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 1, 4),
    _IpduIdentName_Type()
)
ipduIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduIdentName.setStatus("mandatory")
_IpduAgent_ObjectIdentity = ObjectIdentity
ipduAgent = _IpduAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2)
)
_IpduAgentConfig_ObjectIdentity = ObjectIdentity
ipduAgentConfig = _IpduAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1)
)


class _IpduAgentMibVersion_Type(Integer32):
    """Custom type ipduAgentMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_IpduAgentMibVersion_Type.__name__ = "Integer32"
_IpduAgentMibVersion_Object = MibScalar
ipduAgentMibVersion = _IpduAgentMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 1),
    _IpduAgentMibVersion_Type()
)
ipduAgentMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduAgentMibVersion.setStatus("mandatory")
_IpduAgentLog_ObjectIdentity = ObjectIdentity
ipduAgentLog = _IpduAgentLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 4, 1),
    _PduAgentDataLogInterval_Type()
)
pduAgentDataLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduAgentDataLogInterval.setStatus("mandatory")
_IpduAgentControl_ObjectIdentity = ObjectIdentity
ipduAgentControl = _IpduAgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 5)
)


class _IpduAgentControlDefault_Type(Integer32):
    """Custom type ipduAgentControlDefault based on Integer32"""
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


_IpduAgentControlDefault_Type.__name__ = "Integer32"
_IpduAgentControlDefault_Object = MibScalar
ipduAgentControlDefault = _IpduAgentControlDefault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 5, 1),
    _IpduAgentControlDefault_Type()
)
ipduAgentControlDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentControlDefault.setStatus("mandatory")


class _IpduAgentControlRestart_Type(Integer32):
    """Custom type ipduAgentControlRestart based on Integer32"""
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


_IpduAgentControlRestart_Type.__name__ = "Integer32"
_IpduAgentControlRestart_Object = MibScalar
ipduAgentControlRestart = _IpduAgentControlRestart_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 5, 2),
    _IpduAgentControlRestart_Type()
)
ipduAgentControlRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentControlRestart.setStatus("mandatory")
_IpduAgentTrap_ObjectIdentity = ObjectIdentity
ipduAgentTrap = _IpduAgentTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 6)
)
_IpduAgentTrapRetryCount_Type = Integer32
_IpduAgentTrapRetryCount_Object = MibScalar
ipduAgentTrapRetryCount = _IpduAgentTrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 6, 1),
    _IpduAgentTrapRetryCount_Type()
)
ipduAgentTrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTrapRetryCount.setStatus("mandatory")
_IpduAgentTrapRetryTime_Type = Integer32
_IpduAgentTrapRetryTime_Object = MibScalar
ipduAgentTrapRetryTime = _IpduAgentTrapRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 6, 2),
    _IpduAgentTrapRetryTime_Type()
)
ipduAgentTrapRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTrapRetryTime.setStatus("mandatory")
_IpduAgentTrapAckSignature_Type = Integer32
_IpduAgentTrapAckSignature_Object = MibScalar
ipduAgentTrapAckSignature = _IpduAgentTrapAckSignature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 6, 3),
    _IpduAgentTrapAckSignature_Type()
)
ipduAgentTrapAckSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTrapAckSignature.setStatus("mandatory")
_IpduAgentTrapsReceiversTable_Object = MibTable
ipduAgentTrapsReceiversTable = _IpduAgentTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ipduAgentTrapsReceiversTable.setStatus("mandatory")
_IpduAgentTrapsReceiversEntry_Object = MibTableRow
ipduAgentTrapsReceiversEntry = _IpduAgentTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7, 1)
)
ipduAgentTrapsReceiversEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "trapsIndex"),
)
if mibBuilder.loadTexts:
    ipduAgentTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = IpAddress
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7, 1, 3),
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
        *(("iPDU-trap", 2),
          ("none", 1))
    )


_ReceiverNmsType_Type.__name__ = "Integer32"
_ReceiverNmsType_Object = MibTableColumn
receiverNmsType = _ReceiverNmsType_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 7, 1, 6),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_IpduAgentAccessControlTable_Object = MibTable
ipduAgentAccessControlTable = _IpduAgentAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ipduAgentAccessControlTable.setStatus("mandatory")
_IpduAgentAccessControlEntry_Object = MibTableRow
ipduAgentAccessControlEntry = _IpduAgentAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 8, 1)
)
ipduAgentAccessControlEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "accessIndex"),
)
if mibBuilder.loadTexts:
    ipduAgentAccessControlEntry.setStatus("mandatory")


class _AccessIndex_Type(Integer32):
    """Custom type accessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccessIndex_Type.__name__ = "Integer32"
_AccessIndex_Object = MibTableColumn
accessIndex = _AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 8, 1, 1),
    _AccessIndex_Type()
)
accessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessIndex.setStatus("mandatory")
_AccessControlAddr_Type = IpAddress
_AccessControlAddr_Object = MibTableColumn
accessControlAddr = _AccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 1, 8, 1, 3),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("mandatory")
_IpduAgentTime_ObjectIdentity = ObjectIdentity
ipduAgentTime = _IpduAgentTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 2)
)


class _IpduAgentTimeDate_Type(DisplayString):
    """Custom type ipduAgentTimeDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IpduAgentTimeDate_Type.__name__ = "DisplayString"
_IpduAgentTimeDate_Object = MibScalar
ipduAgentTimeDate = _IpduAgentTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 2, 1),
    _IpduAgentTimeDate_Type()
)
ipduAgentTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTimeDate.setStatus("mandatory")


class _IpduAgentTimeTime_Type(DisplayString):
    """Custom type ipduAgentTimeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IpduAgentTimeTime_Type.__name__ = "DisplayString"
_IpduAgentTimeTime_Object = MibScalar
ipduAgentTimeTime = _IpduAgentTimeTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 2, 2),
    _IpduAgentTimeTime_Type()
)
ipduAgentTimeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTimeTime.setStatus("mandatory")


class _IpduAgentTimerFromNtp_Type(Integer32):
    """Custom type ipduAgentTimerFromNtp based on Integer32"""
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


_IpduAgentTimerFromNtp_Type.__name__ = "Integer32"
_IpduAgentTimerFromNtp_Object = MibScalar
ipduAgentTimerFromNtp = _IpduAgentTimerFromNtp_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 2, 3),
    _IpduAgentTimerFromNtp_Type()
)
ipduAgentTimerFromNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTimerFromNtp.setStatus("mandatory")
_IpduAgentNtpIpAddress_Type = IpAddress
_IpduAgentNtpIpAddress_Object = MibScalar
ipduAgentNtpIpAddress = _IpduAgentNtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 2, 4),
    _IpduAgentNtpIpAddress_Type()
)
ipduAgentNtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNtpIpAddress.setStatus("mandatory")


class _IpduAgentNtpTimeZone_Type(Integer32):
    """Custom type ipduAgentNtpTimeZone based on Integer32"""
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


_IpduAgentNtpTimeZone_Type.__name__ = "Integer32"
_IpduAgentNtpTimeZone_Object = MibScalar
ipduAgentNtpTimeZone = _IpduAgentNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 2, 5),
    _IpduAgentNtpTimeZone_Type()
)
ipduAgentNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNtpTimeZone.setStatus("mandatory")


class _IpduAgentDayLightSaving_Type(Integer32):
    """Custom type ipduAgentDayLightSaving based on Integer32"""
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


_IpduAgentDayLightSaving_Type.__name__ = "Integer32"
_IpduAgentDayLightSaving_Object = MibScalar
ipduAgentDayLightSaving = _IpduAgentDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 2, 6),
    _IpduAgentDayLightSaving_Type()
)
ipduAgentDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentDayLightSaving.setStatus("mandatory")
_IpduAgentNetwork_ObjectIdentity = ObjectIdentity
ipduAgentNetwork = _IpduAgentNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3)
)
_IpduAgentNetworkIp_ObjectIdentity = ObjectIdentity
ipduAgentNetworkIp = _IpduAgentNetworkIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 1)
)
_IpduAgentNetworkIpAdress_Type = IpAddress
_IpduAgentNetworkIpAdress_Object = MibScalar
ipduAgentNetworkIpAdress = _IpduAgentNetworkIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 1, 1),
    _IpduAgentNetworkIpAdress_Type()
)
ipduAgentNetworkIpAdress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNetworkIpAdress.setStatus("mandatory")
_IpduAgentNetworkIpGateway_Type = IpAddress
_IpduAgentNetworkIpGateway_Object = MibScalar
ipduAgentNetworkIpGateway = _IpduAgentNetworkIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 1, 2),
    _IpduAgentNetworkIpGateway_Type()
)
ipduAgentNetworkIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNetworkIpGateway.setStatus("mandatory")
_IpduAgentNetworkIpSubnet_Type = IpAddress
_IpduAgentNetworkIpSubnet_Object = MibScalar
ipduAgentNetworkIpSubnet = _IpduAgentNetworkIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 1, 3),
    _IpduAgentNetworkIpSubnet_Type()
)
ipduAgentNetworkIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNetworkIpSubnet.setStatus("mandatory")


class _IpduAgentNetworkDhcpControl_Type(Integer32):
    """Custom type ipduAgentNetworkDhcpControl based on Integer32"""
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


_IpduAgentNetworkDhcpControl_Type.__name__ = "Integer32"
_IpduAgentNetworkDhcpControl_Object = MibScalar
ipduAgentNetworkDhcpControl = _IpduAgentNetworkDhcpControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 2),
    _IpduAgentNetworkDhcpControl_Type()
)
ipduAgentNetworkDhcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNetworkDhcpControl.setStatus("mandatory")


class _IpduAgentNetworkPingControl_Type(Integer32):
    """Custom type ipduAgentNetworkPingControl based on Integer32"""
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


_IpduAgentNetworkPingControl_Type.__name__ = "Integer32"
_IpduAgentNetworkPingControl_Object = MibScalar
ipduAgentNetworkPingControl = _IpduAgentNetworkPingControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 3),
    _IpduAgentNetworkPingControl_Type()
)
ipduAgentNetworkPingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNetworkPingControl.setStatus("mandatory")


class _IpduAgentNetworkTftpControl_Type(Integer32):
    """Custom type ipduAgentNetworkTftpControl based on Integer32"""
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


_IpduAgentNetworkTftpControl_Type.__name__ = "Integer32"
_IpduAgentNetworkTftpControl_Object = MibScalar
ipduAgentNetworkTftpControl = _IpduAgentNetworkTftpControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 4),
    _IpduAgentNetworkTftpControl_Type()
)
ipduAgentNetworkTftpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentNetworkTftpControl.setStatus("mandatory")
_IpduAgentNetworkTelnet_ObjectIdentity = ObjectIdentity
ipduAgentNetworkTelnet = _IpduAgentNetworkTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 5)
)


class _IpduAgentTelnetControl_Type(Integer32):
    """Custom type ipduAgentTelnetControl based on Integer32"""
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


_IpduAgentTelnetControl_Type.__name__ = "Integer32"
_IpduAgentTelnetControl_Object = MibScalar
ipduAgentTelnetControl = _IpduAgentTelnetControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 5, 1),
    _IpduAgentTelnetControl_Type()
)
ipduAgentTelnetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTelnetControl.setStatus("mandatory")
_IpduAgentTelnetPort_Type = Integer32
_IpduAgentTelnetPort_Object = MibScalar
ipduAgentTelnetPort = _IpduAgentTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 5, 2),
    _IpduAgentTelnetPort_Type()
)
ipduAgentTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentTelnetPort.setStatus("mandatory")
_IpduAgentNetworkHttp_ObjectIdentity = ObjectIdentity
ipduAgentNetworkHttp = _IpduAgentNetworkHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 6)
)


class _IpduAgentHttpControl_Type(Integer32):
    """Custom type ipduAgentHttpControl based on Integer32"""
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


_IpduAgentHttpControl_Type.__name__ = "Integer32"
_IpduAgentHttpControl_Object = MibScalar
ipduAgentHttpControl = _IpduAgentHttpControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 6, 1),
    _IpduAgentHttpControl_Type()
)
ipduAgentHttpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentHttpControl.setStatus("mandatory")
_IpduAgentHttpPort_Type = Integer32
_IpduAgentHttpPort_Object = MibScalar
ipduAgentHttpPort = _IpduAgentHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 6, 2),
    _IpduAgentHttpPort_Type()
)
ipduAgentHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentHttpPort.setStatus("mandatory")
_IpduAgentNetworkSnmp_ObjectIdentity = ObjectIdentity
ipduAgentNetworkSnmp = _IpduAgentNetworkSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 7)
)


class _IpduAgentSnmpControl_Type(Integer32):
    """Custom type ipduAgentSnmpControl based on Integer32"""
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


_IpduAgentSnmpControl_Type.__name__ = "Integer32"
_IpduAgentSnmpControl_Object = MibScalar
ipduAgentSnmpControl = _IpduAgentSnmpControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 7, 1),
    _IpduAgentSnmpControl_Type()
)
ipduAgentSnmpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentSnmpControl.setStatus("mandatory")
_IpduAgentSnmpPort_Type = Integer32
_IpduAgentSnmpPort_Object = MibScalar
ipduAgentSnmpPort = _IpduAgentSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 2, 3, 7, 2),
    _IpduAgentSnmpPort_Type()
)
ipduAgentSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduAgentSnmpPort.setStatus("mandatory")
_IpduDevice_ObjectIdentity = ObjectIdentity
ipduDevice = _IpduDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3)
)
_IpduDeviceInlet_ObjectIdentity = ObjectIdentity
ipduDeviceInlet = _IpduDeviceInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1)
)
_IpduDeviceInletNumber_Type = Integer32
_IpduDeviceInletNumber_Object = MibScalar
ipduDeviceInletNumber = _IpduDeviceInletNumber_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 1),
    _IpduDeviceInletNumber_Type()
)
ipduDeviceInletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduDeviceInletNumber.setStatus("mandatory")
_IpduDeviceInletConfigTable_Object = MibTable
ipduDeviceInletConfigTable = _IpduDeviceInletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ipduDeviceInletConfigTable.setStatus("mandatory")
_IpduDeviceInletConfigEntry_Object = MibTableRow
ipduDeviceInletConfigEntry = _IpduDeviceInletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1)
)
ipduDeviceInletConfigEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "inletConfigIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceInletConfigEntry.setStatus("mandatory")


class _InletConfigIndex_Type(Integer32):
    """Custom type inletConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InletConfigIndex_Type.__name__ = "Integer32"
_InletConfigIndex_Object = MibTableColumn
inletConfigIndex = _InletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 2, 1, 12),
    _InletConfigfrequencyLowAction_Type()
)
inletConfigfrequencyLowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletConfigfrequencyLowAction.setStatus("mandatory")
_IpduDeviceInletStatusTable_Object = MibTable
ipduDeviceInletStatusTable = _IpduDeviceInletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ipduDeviceInletStatusTable.setStatus("mandatory")
_IpduDeviceInletStatusEntry_Object = MibTableRow
ipduDeviceInletStatusEntry = _IpduDeviceInletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3, 1)
)
ipduDeviceInletStatusEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "inletStatusIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceInletStatusEntry.setStatus("mandatory")


class _InletStatusIndex_Type(Integer32):
    """Custom type inletStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InletStatusIndex_Type.__name__ = "Integer32"
_InletStatusIndex_Object = MibTableColumn
inletStatusIndex = _InletStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 1, 4),
    _InletWattReset_Type()
)
inletWattReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletWattReset.setStatus("mandatory")
_IpduDeviceOutlet_ObjectIdentity = ObjectIdentity
ipduDeviceOutlet = _IpduDeviceOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2)
)
_IpduDeviceOutletNumber_Type = Integer32
_IpduDeviceOutletNumber_Object = MibScalar
ipduDeviceOutletNumber = _IpduDeviceOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 1),
    _IpduDeviceOutletNumber_Type()
)
ipduDeviceOutletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduDeviceOutletNumber.setStatus("mandatory")
_IpduDeviceOutletConfigTable_Object = MibTable
ipduDeviceOutletConfigTable = _IpduDeviceOutletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ipduDeviceOutletConfigTable.setStatus("mandatory")
_IpduDeviceOutletConfigEntry_Object = MibTableRow
ipduDeviceOutletConfigEntry = _IpduDeviceOutletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1)
)
ipduDeviceOutletConfigEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "inletConfigIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceOutletConfigEntry.setStatus("mandatory")
_OutletConfigIndex_Type = Integer32
_OutletConfigIndex_Object = MibTableColumn
outletConfigIndex = _OutletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1, 3),
    _OutletConfigLocation_Type()
)
outletConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigLocation.setStatus("mandatory")
_OutletConfigOnDelay_Type = Integer32
_OutletConfigOnDelay_Object = MibTableColumn
outletConfigOnDelay = _OutletConfigOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1, 4),
    _OutletConfigOnDelay_Type()
)
outletConfigOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigOnDelay.setStatus("mandatory")
_OutletConfigOffDelay_Type = Integer32
_OutletConfigOffDelay_Object = MibTableColumn
outletConfigOffDelay = _OutletConfigOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 2, 1, 7),
    _OutletConfigCurrentHighAction_Type()
)
outletConfigCurrentHighAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletConfigCurrentHighAction.setStatus("mandatory")
_IpduDeviceOutletStatusTable_Object = MibTable
ipduDeviceOutletStatusTable = _IpduDeviceOutletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ipduDeviceOutletStatusTable.setStatus("mandatory")
_IpduDeviceOutletStatusEntry_Object = MibTableRow
ipduDeviceOutletStatusEntry = _IpduDeviceOutletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1)
)
ipduDeviceOutletStatusEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "outletStatusIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceOutletStatusEntry.setStatus("mandatory")


class _OutletStatusIndex_Type(Integer32):
    """Custom type outletStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OutletStatusIndex_Type.__name__ = "Integer32"
_OutletStatusIndex_Object = MibTableColumn
outletStatusIndex = _OutletStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1, 5),
    _OutletStatusWH_Type()
)
outletStatusWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusWH.setStatus("mandatory")
_OutletStatusStateTime_Type = Integer32
_OutletStatusStateTime_Object = MibTableColumn
outletStatusStateTime = _OutletStatusStateTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1, 6),
    _OutletStatusStateTime_Type()
)
outletStatusStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusStateTime.setStatus("mandatory")
_OutletStatusTimeToGo_Type = Integer32
_OutletStatusTimeToGo_Object = MibTableColumn
outletStatusTimeToGo = _OutletStatusTimeToGo_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 3, 1, 7),
    _OutletStatusTimeToGo_Type()
)
outletStatusTimeToGo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatusTimeToGo.setStatus("mandatory")
_IpduDeviceOutletControlTable_Object = MibTable
ipduDeviceOutletControlTable = _IpduDeviceOutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    ipduDeviceOutletControlTable.setStatus("mandatory")
_IpduDeviceOutletControlEntry_Object = MibTableRow
ipduDeviceOutletControlEntry = _IpduDeviceOutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 4, 1)
)
ipduDeviceOutletControlEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "outletControlIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceOutletControlEntry.setStatus("mandatory")


class _OutletControlIndex_Type(Integer32):
    """Custom type outletControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OutletControlIndex_Type.__name__ = "Integer32"
_OutletControlIndex_Object = MibTableColumn
outletControlIndex = _OutletControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 4, 1, 2),
    _OutletControlControl_Type()
)
outletControlControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlControl.setStatus("mandatory")


class _IpduDeviceOutletControlAll_Type(Integer32):
    """Custom type ipduDeviceOutletControlAll based on Integer32"""
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


_IpduDeviceOutletControlAll_Type.__name__ = "Integer32"
_IpduDeviceOutletControlAll_Object = MibScalar
ipduDeviceOutletControlAll = _IpduDeviceOutletControlAll_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 5),
    _IpduDeviceOutletControlAll_Type()
)
ipduDeviceOutletControlAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduDeviceOutletControlAll.setStatus("mandatory")


class _IpduDeviceOutletWattReset_Type(Integer32):
    """Custom type ipduDeviceOutletWattReset based on Integer32"""
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


_IpduDeviceOutletWattReset_Type.__name__ = "Integer32"
_IpduDeviceOutletWattReset_Object = MibScalar
ipduDeviceOutletWattReset = _IpduDeviceOutletWattReset_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 2, 6),
    _IpduDeviceOutletWattReset_Type()
)
ipduDeviceOutletWattReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduDeviceOutletWattReset.setStatus("mandatory")
_IpduDeviceCcOut_ObjectIdentity = ObjectIdentity
ipduDeviceCcOut = _IpduDeviceCcOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3)
)
_IpduDeviceCcOutNumber_Type = Integer32
_IpduDeviceCcOutNumber_Object = MibScalar
ipduDeviceCcOutNumber = _IpduDeviceCcOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 1),
    _IpduDeviceCcOutNumber_Type()
)
ipduDeviceCcOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduDeviceCcOutNumber.setStatus("mandatory")
_IpduDeviceCcOutConfigTable_Object = MibTable
ipduDeviceCcOutConfigTable = _IpduDeviceCcOutConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ipduDeviceCcOutConfigTable.setStatus("mandatory")
_IpduDeviceCcOutConfigEntry_Object = MibTableRow
ipduDeviceCcOutConfigEntry = _IpduDeviceCcOutConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 2, 1)
)
ipduDeviceCcOutConfigEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "ccOutConfigIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceCcOutConfigEntry.setStatus("mandatory")


class _CcOutConfigIndex_Type(Integer32):
    """Custom type ccOutConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcOutConfigIndex_Type.__name__ = "Integer32"
_CcOutConfigIndex_Object = MibTableColumn
ccOutConfigIndex = _CcOutConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 2, 1, 3),
    _CcOutConfigEventAction_Type()
)
ccOutConfigEventAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutConfigEventAction.setStatus("mandatory")
_CcOutConfigCloseDelay_Type = Integer32
_CcOutConfigCloseDelay_Object = MibTableColumn
ccOutConfigCloseDelay = _CcOutConfigCloseDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 2, 1, 4),
    _CcOutConfigCloseDelay_Type()
)
ccOutConfigCloseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutConfigCloseDelay.setStatus("mandatory")
_CcOutConfigOpenDelay_Type = Integer32
_CcOutConfigOpenDelay_Object = MibTableColumn
ccOutConfigOpenDelay = _CcOutConfigOpenDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 2, 1, 5),
    _CcOutConfigOpenDelay_Type()
)
ccOutConfigOpenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutConfigOpenDelay.setStatus("mandatory")
_IpduDeviceCcOutStatusTable_Object = MibTable
ipduDeviceCcOutStatusTable = _IpduDeviceCcOutStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    ipduDeviceCcOutStatusTable.setStatus("mandatory")
_IpduDeviceCcOutStatusEntry_Object = MibTableRow
ipduDeviceCcOutStatusEntry = _IpduDeviceCcOutStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 3, 1)
)
ipduDeviceCcOutStatusEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "ccOutStatusIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceCcOutStatusEntry.setStatus("mandatory")


class _CcOutStatusIndex_Type(Integer32):
    """Custom type ccOutStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcOutStatusIndex_Type.__name__ = "Integer32"
_CcOutStatusIndex_Object = MibTableColumn
ccOutStatusIndex = _CcOutStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 3, 1, 2),
    _CcOutStatusStatus_Type()
)
ccOutStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccOutStatusStatus.setStatus("mandatory")
_CcOutStatusTimeOnState_Type = Integer32
_CcOutStatusTimeOnState_Object = MibTableColumn
ccOutStatusTimeOnState = _CcOutStatusTimeOnState_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 3, 1, 3),
    _CcOutStatusTimeOnState_Type()
)
ccOutStatusTimeOnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccOutStatusTimeOnState.setStatus("mandatory")
_IpduDeviceCcOutControlTable_Object = MibTable
ipduDeviceCcOutControlTable = _IpduDeviceCcOutControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    ipduDeviceCcOutControlTable.setStatus("mandatory")
_IpduDeviceCcOutControlEntry_Object = MibTableRow
ipduDeviceCcOutControlEntry = _IpduDeviceCcOutControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 4, 1)
)
ipduDeviceCcOutControlEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "ccOutControlIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceCcOutControlEntry.setStatus("mandatory")


class _CcOutControlIndex_Type(Integer32):
    """Custom type ccOutControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcOutControlIndex_Type.__name__ = "Integer32"
_CcOutControlIndex_Object = MibTableColumn
ccOutControlIndex = _CcOutControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 3, 3, 4, 1, 2),
    _CcOutControlControl_Type()
)
ccOutControlControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccOutControlControl.setStatus("mandatory")
_IpduSlave_ObjectIdentity = ObjectIdentity
ipduSlave = _IpduSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4)
)
_IpduSlaveState_ObjectIdentity = ObjectIdentity
ipduSlaveState = _IpduSlaveState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 1)
)
_IpduSlaveStateTable_Object = MibTable
ipduSlaveStateTable = _IpduSlaveStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ipduSlaveStateTable.setStatus("mandatory")
_IpduSlaveStateEntry_Object = MibTableRow
ipduSlaveStateEntry = _IpduSlaveStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 1, 1, 1)
)
ipduSlaveStateEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveStateIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveStateEntry.setStatus("mandatory")


class _SlaveStateIndex_Type(Integer32):
    """Custom type slaveStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveStateIndex_Type.__name__ = "Integer32"
_SlaveStateIndex_Object = MibTableColumn
slaveStateIndex = _SlaveStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 1, 1, 1, 2),
    _SlaveStateControl01_Type()
)
slaveStateControl01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveStateControl01.setStatus("mandatory")
_IpduSlaveInlet_ObjectIdentity = ObjectIdentity
ipduSlaveInlet = _IpduSlaveInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2)
)
_IpduSlaveInletStatus_ObjectIdentity = ObjectIdentity
ipduSlaveInletStatus = _IpduSlaveInletStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1)
)
_IpduDeviceSlaveInletStatusTable_Object = MibTable
ipduDeviceSlaveInletStatusTable = _IpduDeviceSlaveInletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipduDeviceSlaveInletStatusTable.setStatus("mandatory")
_IpduDeviceSlaveInletStatusEntry_Object = MibTableRow
ipduDeviceSlaveInletStatusEntry = _IpduDeviceSlaveInletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1)
)
ipduDeviceSlaveInletStatusEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "inletStatusIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceSlaveInletStatusEntry.setStatus("mandatory")


class _InletSlaveStatusIndex_Type(Integer32):
    """Custom type inletSlaveStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InletSlaveStatusIndex_Type.__name__ = "Integer32"
_InletSlaveStatusIndex_Object = MibTableColumn
inletSlaveStatusIndex = _InletSlaveStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 1, 1, 1, 11),
    _InletSlaveStatusWH2_Type()
)
inletSlaveStatusWH2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSlaveStatusWH2.setStatus("mandatory")
_IpduSlaveInletConfig_ObjectIdentity = ObjectIdentity
ipduSlaveInletConfig = _IpduSlaveInletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2)
)
_IpduDeviceslaveInletConfigTable_Object = MibTable
ipduDeviceslaveInletConfigTable = _IpduDeviceslaveInletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipduDeviceslaveInletConfigTable.setStatus("mandatory")
_IpduDeviceslaveInletConfigEntry_Object = MibTableRow
ipduDeviceslaveInletConfigEntry = _IpduDeviceslaveInletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2, 1, 1)
)
ipduDeviceslaveInletConfigEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveInletConfigIndex"),
)
if mibBuilder.loadTexts:
    ipduDeviceslaveInletConfigEntry.setStatus("mandatory")


class _SlaveInletConfigIndex_Type(Integer32):
    """Custom type slaveInletConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveInletConfigIndex_Type.__name__ = "Integer32"
_SlaveInletConfigIndex_Object = MibTableColumn
slaveInletConfigIndex = _SlaveInletConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 2, 2, 1, 1, 5),
    _SlaveInlet2ConfigVoltageLow_Type()
)
slaveInlet2ConfigVoltageLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveInlet2ConfigVoltageLow.setStatus("mandatory")
_IpduSlaveOutlet_ObjectIdentity = ObjectIdentity
ipduSlaveOutlet = _IpduSlaveOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3)
)
_IpduSlaveOutletConfig_ObjectIdentity = ObjectIdentity
ipduSlaveOutletConfig = _IpduSlaveOutletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1)
)
_IpduSlaveDeviceOutletNameTable_Object = MibTable
ipduSlaveDeviceOutletNameTable = _IpduSlaveDeviceOutletNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletNameTable.setStatus("mandatory")
_IpduSlaveDeviceOutletNameEntry_Object = MibTableRow
ipduSlaveDeviceOutletNameEntry = _IpduSlaveDeviceOutletNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1)
)
ipduSlaveDeviceOutletNameEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletNameIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletNameEntry.setStatus("mandatory")


class _SlaveOutletNameIndex_Type(Integer32):
    """Custom type slaveOutletNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletNameIndex_Type.__name__ = "Integer32"
_SlaveOutletNameIndex_Object = MibTableColumn
slaveOutletNameIndex = _SlaveOutletNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 1, 1, 13),
    _SlaveOutletName12_Type()
)
slaveOutletName12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletName12.setStatus("mandatory")
_IpduSlaveDeviceOutletLocationTable_Object = MibTable
ipduSlaveDeviceOutletLocationTable = _IpduSlaveDeviceOutletLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletLocationTable.setStatus("mandatory")
_IpduSlaveDeviceOutletLocationEntry_Object = MibTableRow
ipduSlaveDeviceOutletLocationEntry = _IpduSlaveDeviceOutletLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1)
)
ipduSlaveDeviceOutletLocationEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletLocationIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletLocationEntry.setStatus("mandatory")


class _SlaveOutletLocationIndex_Type(Integer32):
    """Custom type slaveOutletLocationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletLocationIndex_Type.__name__ = "Integer32"
_SlaveOutletLocationIndex_Object = MibTableColumn
slaveOutletLocationIndex = _SlaveOutletLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 2, 1, 13),
    _SlaveOutletLocation12_Type()
)
slaveOutletLocation12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletLocation12.setStatus("mandatory")
_IpduSlaveDeviceOutletOnTimeTable_Object = MibTable
ipduSlaveDeviceOutletOnTimeTable = _IpduSlaveDeviceOutletOnTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletOnTimeTable.setStatus("mandatory")
_IpduSlaveDeviceOutletOnTimeEntry_Object = MibTableRow
ipduSlaveDeviceOutletOnTimeEntry = _IpduSlaveDeviceOutletOnTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1)
)
ipduSlaveDeviceOutletOnTimeEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletOnTimeIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletOnTimeEntry.setStatus("mandatory")


class _SlaveOutletOnTimeIndex_Type(Integer32):
    """Custom type slaveOutletOnTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletOnTimeIndex_Type.__name__ = "Integer32"
_SlaveOutletOnTimeIndex_Object = MibTableColumn
slaveOutletOnTimeIndex = _SlaveOutletOnTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 1),
    _SlaveOutletOnTimeIndex_Type()
)
slaveOutletOnTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletOnTimeIndex.setStatus("mandatory")
_SlaveOutletOnTime01_Type = Integer32
_SlaveOutletOnTime01_Object = MibTableColumn
slaveOutletOnTime01 = _SlaveOutletOnTime01_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 2),
    _SlaveOutletOnTime01_Type()
)
slaveOutletOnTime01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime01.setStatus("mandatory")
_SlaveOutletOnTime02_Type = Integer32
_SlaveOutletOnTime02_Object = MibTableColumn
slaveOutletOnTime02 = _SlaveOutletOnTime02_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 3),
    _SlaveOutletOnTime02_Type()
)
slaveOutletOnTime02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime02.setStatus("mandatory")
_SlaveOutletOnTime03_Type = Integer32
_SlaveOutletOnTime03_Object = MibTableColumn
slaveOutletOnTime03 = _SlaveOutletOnTime03_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 4),
    _SlaveOutletOnTime03_Type()
)
slaveOutletOnTime03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime03.setStatus("mandatory")
_SlaveOutletOnTime04_Type = Integer32
_SlaveOutletOnTime04_Object = MibTableColumn
slaveOutletOnTime04 = _SlaveOutletOnTime04_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 5),
    _SlaveOutletOnTime04_Type()
)
slaveOutletOnTime04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime04.setStatus("mandatory")
_SlaveOutletOnTime05_Type = Integer32
_SlaveOutletOnTime05_Object = MibTableColumn
slaveOutletOnTime05 = _SlaveOutletOnTime05_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 6),
    _SlaveOutletOnTime05_Type()
)
slaveOutletOnTime05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime05.setStatus("mandatory")
_SlaveOutletOnTime06_Type = Integer32
_SlaveOutletOnTime06_Object = MibTableColumn
slaveOutletOnTime06 = _SlaveOutletOnTime06_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 7),
    _SlaveOutletOnTime06_Type()
)
slaveOutletOnTime06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime06.setStatus("mandatory")
_SlaveOutletOnTime07_Type = Integer32
_SlaveOutletOnTime07_Object = MibTableColumn
slaveOutletOnTime07 = _SlaveOutletOnTime07_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 8),
    _SlaveOutletOnTime07_Type()
)
slaveOutletOnTime07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime07.setStatus("mandatory")
_SlaveOutletOnTime08_Type = Integer32
_SlaveOutletOnTime08_Object = MibTableColumn
slaveOutletOnTime08 = _SlaveOutletOnTime08_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 9),
    _SlaveOutletOnTime08_Type()
)
slaveOutletOnTime08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime08.setStatus("mandatory")
_SlaveOutletOnTime09_Type = Integer32
_SlaveOutletOnTime09_Object = MibTableColumn
slaveOutletOnTime09 = _SlaveOutletOnTime09_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 10),
    _SlaveOutletOnTime09_Type()
)
slaveOutletOnTime09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime09.setStatus("mandatory")
_SlaveOutletOnTime10_Type = Integer32
_SlaveOutletOnTime10_Object = MibTableColumn
slaveOutletOnTime10 = _SlaveOutletOnTime10_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 11),
    _SlaveOutletOnTime10_Type()
)
slaveOutletOnTime10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime10.setStatus("mandatory")
_SlaveOutletOnTime11_Type = Integer32
_SlaveOutletOnTime11_Object = MibTableColumn
slaveOutletOnTime11 = _SlaveOutletOnTime11_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 12),
    _SlaveOutletOnTime11_Type()
)
slaveOutletOnTime11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime11.setStatus("mandatory")
_SlaveOutletOnTime12_Type = Integer32
_SlaveOutletOnTime12_Object = MibTableColumn
slaveOutletOnTime12 = _SlaveOutletOnTime12_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 3, 1, 13),
    _SlaveOutletOnTime12_Type()
)
slaveOutletOnTime12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOnTime12.setStatus("mandatory")
_IpduSlaveDeviceOutletOffTimeTable_Object = MibTable
ipduSlaveDeviceOutletOffTimeTable = _IpduSlaveDeviceOutletOffTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletOffTimeTable.setStatus("mandatory")
_IpduSlaveDeviceOutletOffTimeEntry_Object = MibTableRow
ipduSlaveDeviceOutletOffTimeEntry = _IpduSlaveDeviceOutletOffTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1)
)
ipduSlaveDeviceOutletOffTimeEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletOffTimeIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletOffTimeEntry.setStatus("mandatory")


class _SlaveOutletOffTimeIndex_Type(Integer32):
    """Custom type slaveOutletOffTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletOffTimeIndex_Type.__name__ = "Integer32"
_SlaveOutletOffTimeIndex_Object = MibTableColumn
slaveOutletOffTimeIndex = _SlaveOutletOffTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 1),
    _SlaveOutletOffTimeIndex_Type()
)
slaveOutletOffTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletOffTimeIndex.setStatus("mandatory")
_SlaveOutletOffTime01_Type = Integer32
_SlaveOutletOffTime01_Object = MibTableColumn
slaveOutletOffTime01 = _SlaveOutletOffTime01_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 2),
    _SlaveOutletOffTime01_Type()
)
slaveOutletOffTime01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime01.setStatus("mandatory")
_SlaveOutletOffTime02_Type = Integer32
_SlaveOutletOffTime02_Object = MibTableColumn
slaveOutletOffTime02 = _SlaveOutletOffTime02_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 3),
    _SlaveOutletOffTime02_Type()
)
slaveOutletOffTime02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime02.setStatus("mandatory")
_SlaveOutletOffTime03_Type = Integer32
_SlaveOutletOffTime03_Object = MibTableColumn
slaveOutletOffTime03 = _SlaveOutletOffTime03_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 4),
    _SlaveOutletOffTime03_Type()
)
slaveOutletOffTime03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime03.setStatus("mandatory")
_SlaveOutletOffTime04_Type = Integer32
_SlaveOutletOffTime04_Object = MibTableColumn
slaveOutletOffTime04 = _SlaveOutletOffTime04_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 5),
    _SlaveOutletOffTime04_Type()
)
slaveOutletOffTime04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime04.setStatus("mandatory")
_SlaveOutletOffTime05_Type = Integer32
_SlaveOutletOffTime05_Object = MibTableColumn
slaveOutletOffTime05 = _SlaveOutletOffTime05_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 6),
    _SlaveOutletOffTime05_Type()
)
slaveOutletOffTime05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime05.setStatus("mandatory")
_SlaveOutletOffTime06_Type = Integer32
_SlaveOutletOffTime06_Object = MibTableColumn
slaveOutletOffTime06 = _SlaveOutletOffTime06_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 7),
    _SlaveOutletOffTime06_Type()
)
slaveOutletOffTime06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime06.setStatus("mandatory")
_SlaveOutletOffTime07_Type = Integer32
_SlaveOutletOffTime07_Object = MibTableColumn
slaveOutletOffTime07 = _SlaveOutletOffTime07_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 8),
    _SlaveOutletOffTime07_Type()
)
slaveOutletOffTime07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime07.setStatus("mandatory")
_SlaveOutletOffTime08_Type = Integer32
_SlaveOutletOffTime08_Object = MibTableColumn
slaveOutletOffTime08 = _SlaveOutletOffTime08_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 9),
    _SlaveOutletOffTime08_Type()
)
slaveOutletOffTime08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime08.setStatus("mandatory")
_SlaveOutletOffTime09_Type = Integer32
_SlaveOutletOffTime09_Object = MibTableColumn
slaveOutletOffTime09 = _SlaveOutletOffTime09_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 10),
    _SlaveOutletOffTime09_Type()
)
slaveOutletOffTime09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime09.setStatus("mandatory")
_SlaveOutletOffTime10_Type = Integer32
_SlaveOutletOffTime10_Object = MibTableColumn
slaveOutletOffTime10 = _SlaveOutletOffTime10_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 11),
    _SlaveOutletOffTime10_Type()
)
slaveOutletOffTime10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime10.setStatus("mandatory")
_SlaveOutletOffTime11_Type = Integer32
_SlaveOutletOffTime11_Object = MibTableColumn
slaveOutletOffTime11 = _SlaveOutletOffTime11_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 12),
    _SlaveOutletOffTime11_Type()
)
slaveOutletOffTime11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime11.setStatus("mandatory")
_SlaveOutletOffTime12_Type = Integer32
_SlaveOutletOffTime12_Object = MibTableColumn
slaveOutletOffTime12 = _SlaveOutletOffTime12_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 4, 1, 13),
    _SlaveOutletOffTime12_Type()
)
slaveOutletOffTime12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletOffTime12.setStatus("mandatory")
_IpduSlaveDeviceOutletCurrThTable_Object = MibTable
ipduSlaveDeviceOutletCurrThTable = _IpduSlaveDeviceOutletCurrThTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletCurrThTable.setStatus("mandatory")
_IpduSlaveDeviceOutletCurrThEntry_Object = MibTableRow
ipduSlaveDeviceOutletCurrThEntry = _IpduSlaveDeviceOutletCurrThEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1)
)
ipduSlaveDeviceOutletCurrThEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletCurrThIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletCurrThEntry.setStatus("mandatory")


class _SlaveOutletCurrThIndex_Type(Integer32):
    """Custom type slaveOutletCurrThIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletCurrThIndex_Type.__name__ = "Integer32"
_SlaveOutletCurrThIndex_Object = MibTableColumn
slaveOutletCurrThIndex = _SlaveOutletCurrThIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 1),
    _SlaveOutletCurrThIndex_Type()
)
slaveOutletCurrThIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrThIndex.setStatus("mandatory")
_SlaveOutletCurrTh01_Type = Integer32
_SlaveOutletCurrTh01_Object = MibTableColumn
slaveOutletCurrTh01 = _SlaveOutletCurrTh01_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 2),
    _SlaveOutletCurrTh01_Type()
)
slaveOutletCurrTh01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh01.setStatus("mandatory")
_SlaveOutletCurrTh02_Type = Integer32
_SlaveOutletCurrTh02_Object = MibTableColumn
slaveOutletCurrTh02 = _SlaveOutletCurrTh02_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 3),
    _SlaveOutletCurrTh02_Type()
)
slaveOutletCurrTh02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh02.setStatus("mandatory")
_SlaveOutletCurrTh03_Type = Integer32
_SlaveOutletCurrTh03_Object = MibTableColumn
slaveOutletCurrTh03 = _SlaveOutletCurrTh03_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 4),
    _SlaveOutletCurrTh03_Type()
)
slaveOutletCurrTh03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh03.setStatus("mandatory")
_SlaveOutletCurrTh04_Type = Integer32
_SlaveOutletCurrTh04_Object = MibTableColumn
slaveOutletCurrTh04 = _SlaveOutletCurrTh04_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 5),
    _SlaveOutletCurrTh04_Type()
)
slaveOutletCurrTh04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh04.setStatus("mandatory")
_SlaveOutletCurrTh05_Type = Integer32
_SlaveOutletCurrTh05_Object = MibTableColumn
slaveOutletCurrTh05 = _SlaveOutletCurrTh05_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 6),
    _SlaveOutletCurrTh05_Type()
)
slaveOutletCurrTh05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh05.setStatus("mandatory")
_SlaveOutletCurrTh06_Type = Integer32
_SlaveOutletCurrTh06_Object = MibTableColumn
slaveOutletCurrTh06 = _SlaveOutletCurrTh06_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 7),
    _SlaveOutletCurrTh06_Type()
)
slaveOutletCurrTh06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh06.setStatus("mandatory")
_SlaveOutletCurrTh07_Type = Integer32
_SlaveOutletCurrTh07_Object = MibTableColumn
slaveOutletCurrTh07 = _SlaveOutletCurrTh07_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 8),
    _SlaveOutletCurrTh07_Type()
)
slaveOutletCurrTh07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh07.setStatus("mandatory")
_SlaveOutletCurrTh08_Type = Integer32
_SlaveOutletCurrTh08_Object = MibTableColumn
slaveOutletCurrTh08 = _SlaveOutletCurrTh08_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 9),
    _SlaveOutletCurrTh08_Type()
)
slaveOutletCurrTh08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh08.setStatus("mandatory")
_SlaveOutletCurrTh09_Type = Integer32
_SlaveOutletCurrTh09_Object = MibTableColumn
slaveOutletCurrTh09 = _SlaveOutletCurrTh09_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 10),
    _SlaveOutletCurrTh09_Type()
)
slaveOutletCurrTh09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh09.setStatus("mandatory")
_SlaveOutletCurrTh10_Type = Integer32
_SlaveOutletCurrTh10_Object = MibTableColumn
slaveOutletCurrTh10 = _SlaveOutletCurrTh10_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 11),
    _SlaveOutletCurrTh10_Type()
)
slaveOutletCurrTh10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh10.setStatus("mandatory")
_SlaveOutletCurrTh11_Type = Integer32
_SlaveOutletCurrTh11_Object = MibTableColumn
slaveOutletCurrTh11 = _SlaveOutletCurrTh11_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 12),
    _SlaveOutletCurrTh11_Type()
)
slaveOutletCurrTh11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh11.setStatus("mandatory")
_SlaveOutletCurrTh12_Type = Integer32
_SlaveOutletCurrTh12_Object = MibTableColumn
slaveOutletCurrTh12 = _SlaveOutletCurrTh12_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 1, 5, 1, 13),
    _SlaveOutletCurrTh12_Type()
)
slaveOutletCurrTh12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletCurrTh12.setStatus("mandatory")
_IpduSlaveOutletStatus_ObjectIdentity = ObjectIdentity
ipduSlaveOutletStatus = _IpduSlaveOutletStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2)
)
_IpduSlaveDeviceOutletCurrentTable_Object = MibTable
ipduSlaveDeviceOutletCurrentTable = _IpduSlaveDeviceOutletCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletCurrentTable.setStatus("mandatory")
_IpduSlaveDeviceOutletCurrentEntry_Object = MibTableRow
ipduSlaveDeviceOutletCurrentEntry = _IpduSlaveDeviceOutletCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1)
)
ipduSlaveDeviceOutletCurrentEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletCurrentIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletCurrentEntry.setStatus("mandatory")


class _SlaveOutletCurrentIndex_Type(Integer32):
    """Custom type slaveOutletCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletCurrentIndex_Type.__name__ = "Integer32"
_SlaveOutletCurrentIndex_Object = MibTableColumn
slaveOutletCurrentIndex = _SlaveOutletCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 1),
    _SlaveOutletCurrentIndex_Type()
)
slaveOutletCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrentIndex.setStatus("mandatory")
_SlaveOutletCurrent01_Type = Integer32
_SlaveOutletCurrent01_Object = MibTableColumn
slaveOutletCurrent01 = _SlaveOutletCurrent01_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 2),
    _SlaveOutletCurrent01_Type()
)
slaveOutletCurrent01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent01.setStatus("mandatory")
_SlaveOutletCurrent02_Type = Integer32
_SlaveOutletCurrent02_Object = MibTableColumn
slaveOutletCurrent02 = _SlaveOutletCurrent02_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 3),
    _SlaveOutletCurrent02_Type()
)
slaveOutletCurrent02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent02.setStatus("mandatory")
_SlaveOutletCurrent03_Type = Integer32
_SlaveOutletCurrent03_Object = MibTableColumn
slaveOutletCurrent03 = _SlaveOutletCurrent03_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 4),
    _SlaveOutletCurrent03_Type()
)
slaveOutletCurrent03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent03.setStatus("mandatory")
_SlaveOutletCurrent04_Type = Integer32
_SlaveOutletCurrent04_Object = MibTableColumn
slaveOutletCurrent04 = _SlaveOutletCurrent04_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 5),
    _SlaveOutletCurrent04_Type()
)
slaveOutletCurrent04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent04.setStatus("mandatory")
_SlaveOutletCurrent05_Type = Integer32
_SlaveOutletCurrent05_Object = MibTableColumn
slaveOutletCurrent05 = _SlaveOutletCurrent05_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 6),
    _SlaveOutletCurrent05_Type()
)
slaveOutletCurrent05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent05.setStatus("mandatory")
_SlaveOutletCurrent06_Type = Integer32
_SlaveOutletCurrent06_Object = MibTableColumn
slaveOutletCurrent06 = _SlaveOutletCurrent06_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 7),
    _SlaveOutletCurrent06_Type()
)
slaveOutletCurrent06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent06.setStatus("mandatory")
_SlaveOutletCurrent07_Type = Integer32
_SlaveOutletCurrent07_Object = MibTableColumn
slaveOutletCurrent07 = _SlaveOutletCurrent07_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 8),
    _SlaveOutletCurrent07_Type()
)
slaveOutletCurrent07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent07.setStatus("mandatory")
_SlaveOutletCurrent08_Type = Integer32
_SlaveOutletCurrent08_Object = MibTableColumn
slaveOutletCurrent08 = _SlaveOutletCurrent08_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 9),
    _SlaveOutletCurrent08_Type()
)
slaveOutletCurrent08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent08.setStatus("mandatory")
_SlaveOutletCurrent09_Type = Integer32
_SlaveOutletCurrent09_Object = MibTableColumn
slaveOutletCurrent09 = _SlaveOutletCurrent09_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 10),
    _SlaveOutletCurrent09_Type()
)
slaveOutletCurrent09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent09.setStatus("mandatory")
_SlaveOutletCurrent10_Type = Integer32
_SlaveOutletCurrent10_Object = MibTableColumn
slaveOutletCurrent10 = _SlaveOutletCurrent10_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 11),
    _SlaveOutletCurrent10_Type()
)
slaveOutletCurrent10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent10.setStatus("mandatory")
_SlaveOutletCurrent11_Type = Integer32
_SlaveOutletCurrent11_Object = MibTableColumn
slaveOutletCurrent11 = _SlaveOutletCurrent11_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 12),
    _SlaveOutletCurrent11_Type()
)
slaveOutletCurrent11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent11.setStatus("mandatory")
_SlaveOutletCurrent12_Type = Integer32
_SlaveOutletCurrent12_Object = MibTableColumn
slaveOutletCurrent12 = _SlaveOutletCurrent12_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 1, 1, 13),
    _SlaveOutletCurrent12_Type()
)
slaveOutletCurrent12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletCurrent12.setStatus("mandatory")
_IpduSlaveDeviceOutletWattTable_Object = MibTable
ipduSlaveDeviceOutletWattTable = _IpduSlaveDeviceOutletWattTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletWattTable.setStatus("mandatory")
_IpduSlaveDeviceOutletWattEntry_Object = MibTableRow
ipduSlaveDeviceOutletWattEntry = _IpduSlaveDeviceOutletWattEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1)
)
ipduSlaveDeviceOutletWattEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletWattIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletWattEntry.setStatus("mandatory")


class _SlaveOutletWattIndex_Type(Integer32):
    """Custom type slaveOutletWattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletWattIndex_Type.__name__ = "Integer32"
_SlaveOutletWattIndex_Object = MibTableColumn
slaveOutletWattIndex = _SlaveOutletWattIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 1),
    _SlaveOutletWattIndex_Type()
)
slaveOutletWattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWattIndex.setStatus("mandatory")
_SlaveOutletWatt01_Type = Integer32
_SlaveOutletWatt01_Object = MibTableColumn
slaveOutletWatt01 = _SlaveOutletWatt01_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 2),
    _SlaveOutletWatt01_Type()
)
slaveOutletWatt01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt01.setStatus("mandatory")
_SlaveOutletWatt02_Type = Integer32
_SlaveOutletWatt02_Object = MibTableColumn
slaveOutletWatt02 = _SlaveOutletWatt02_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 3),
    _SlaveOutletWatt02_Type()
)
slaveOutletWatt02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt02.setStatus("mandatory")
_SlaveOutletWatt03_Type = Integer32
_SlaveOutletWatt03_Object = MibTableColumn
slaveOutletWatt03 = _SlaveOutletWatt03_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 4),
    _SlaveOutletWatt03_Type()
)
slaveOutletWatt03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt03.setStatus("mandatory")
_SlaveOutletWatt04_Type = Integer32
_SlaveOutletWatt04_Object = MibTableColumn
slaveOutletWatt04 = _SlaveOutletWatt04_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 5),
    _SlaveOutletWatt04_Type()
)
slaveOutletWatt04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt04.setStatus("mandatory")
_SlaveOutletWatt05_Type = Integer32
_SlaveOutletWatt05_Object = MibTableColumn
slaveOutletWatt05 = _SlaveOutletWatt05_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 6),
    _SlaveOutletWatt05_Type()
)
slaveOutletWatt05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt05.setStatus("mandatory")
_SlaveOutletWatt06_Type = Integer32
_SlaveOutletWatt06_Object = MibTableColumn
slaveOutletWatt06 = _SlaveOutletWatt06_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 7),
    _SlaveOutletWatt06_Type()
)
slaveOutletWatt06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt06.setStatus("mandatory")
_SlaveOutletWatt07_Type = Integer32
_SlaveOutletWatt07_Object = MibTableColumn
slaveOutletWatt07 = _SlaveOutletWatt07_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 8),
    _SlaveOutletWatt07_Type()
)
slaveOutletWatt07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt07.setStatus("mandatory")
_SlaveOutletWatt08_Type = Integer32
_SlaveOutletWatt08_Object = MibTableColumn
slaveOutletWatt08 = _SlaveOutletWatt08_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 9),
    _SlaveOutletWatt08_Type()
)
slaveOutletWatt08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt08.setStatus("mandatory")
_SlaveOutletWatt09_Type = Integer32
_SlaveOutletWatt09_Object = MibTableColumn
slaveOutletWatt09 = _SlaveOutletWatt09_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 10),
    _SlaveOutletWatt09_Type()
)
slaveOutletWatt09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt09.setStatus("mandatory")
_SlaveOutletWatt10_Type = Integer32
_SlaveOutletWatt10_Object = MibTableColumn
slaveOutletWatt10 = _SlaveOutletWatt10_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 11),
    _SlaveOutletWatt10_Type()
)
slaveOutletWatt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt10.setStatus("mandatory")
_SlaveOutletWatt11_Type = Integer32
_SlaveOutletWatt11_Object = MibTableColumn
slaveOutletWatt11 = _SlaveOutletWatt11_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 12),
    _SlaveOutletWatt11_Type()
)
slaveOutletWatt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt11.setStatus("mandatory")
_SlaveOutletWatt12_Type = Integer32
_SlaveOutletWatt12_Object = MibTableColumn
slaveOutletWatt12 = _SlaveOutletWatt12_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 2, 1, 13),
    _SlaveOutletWatt12_Type()
)
slaveOutletWatt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletWatt12.setStatus("mandatory")
_IpduSlaveDeviceOutletKwattTable_Object = MibTable
ipduSlaveDeviceOutletKwattTable = _IpduSlaveDeviceOutletKwattTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletKwattTable.setStatus("mandatory")
_IpduSlaveDeviceOutletKwattEntry_Object = MibTableRow
ipduSlaveDeviceOutletKwattEntry = _IpduSlaveDeviceOutletKwattEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1)
)
ipduSlaveDeviceOutletKwattEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletKwattIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletKwattEntry.setStatus("mandatory")


class _SlaveOutletKwattIndex_Type(Integer32):
    """Custom type slaveOutletKwattIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletKwattIndex_Type.__name__ = "Integer32"
_SlaveOutletKwattIndex_Object = MibTableColumn
slaveOutletKwattIndex = _SlaveOutletKwattIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 1),
    _SlaveOutletKwattIndex_Type()
)
slaveOutletKwattIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwattIndex.setStatus("mandatory")
_SlaveOutletKwatt01_Type = Integer32
_SlaveOutletKwatt01_Object = MibTableColumn
slaveOutletKwatt01 = _SlaveOutletKwatt01_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 2),
    _SlaveOutletKwatt01_Type()
)
slaveOutletKwatt01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt01.setStatus("mandatory")
_SlaveOutletKwatt02_Type = Integer32
_SlaveOutletKwatt02_Object = MibTableColumn
slaveOutletKwatt02 = _SlaveOutletKwatt02_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 3),
    _SlaveOutletKwatt02_Type()
)
slaveOutletKwatt02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt02.setStatus("mandatory")
_SlaveOutletKwatt03_Type = Integer32
_SlaveOutletKwatt03_Object = MibTableColumn
slaveOutletKwatt03 = _SlaveOutletKwatt03_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 4),
    _SlaveOutletKwatt03_Type()
)
slaveOutletKwatt03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt03.setStatus("mandatory")
_SlaveOutletKwatt04_Type = Integer32
_SlaveOutletKwatt04_Object = MibTableColumn
slaveOutletKwatt04 = _SlaveOutletKwatt04_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 5),
    _SlaveOutletKwatt04_Type()
)
slaveOutletKwatt04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt04.setStatus("mandatory")
_SlaveOutletKwatt05_Type = Integer32
_SlaveOutletKwatt05_Object = MibTableColumn
slaveOutletKwatt05 = _SlaveOutletKwatt05_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 6),
    _SlaveOutletKwatt05_Type()
)
slaveOutletKwatt05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt05.setStatus("mandatory")
_SlaveOutletKwatt06_Type = Integer32
_SlaveOutletKwatt06_Object = MibTableColumn
slaveOutletKwatt06 = _SlaveOutletKwatt06_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 7),
    _SlaveOutletKwatt06_Type()
)
slaveOutletKwatt06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt06.setStatus("mandatory")
_SlaveOutletKwatt07_Type = Integer32
_SlaveOutletKwatt07_Object = MibTableColumn
slaveOutletKwatt07 = _SlaveOutletKwatt07_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 8),
    _SlaveOutletKwatt07_Type()
)
slaveOutletKwatt07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt07.setStatus("mandatory")
_SlaveOutletKwatt08_Type = Integer32
_SlaveOutletKwatt08_Object = MibTableColumn
slaveOutletKwatt08 = _SlaveOutletKwatt08_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 9),
    _SlaveOutletKwatt08_Type()
)
slaveOutletKwatt08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt08.setStatus("mandatory")
_SlaveOutletKwatt09_Type = Integer32
_SlaveOutletKwatt09_Object = MibTableColumn
slaveOutletKwatt09 = _SlaveOutletKwatt09_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 10),
    _SlaveOutletKwatt09_Type()
)
slaveOutletKwatt09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt09.setStatus("mandatory")
_SlaveOutletKwatt10_Type = Integer32
_SlaveOutletKwatt10_Object = MibTableColumn
slaveOutletKwatt10 = _SlaveOutletKwatt10_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 11),
    _SlaveOutletKwatt10_Type()
)
slaveOutletKwatt10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt10.setStatus("mandatory")
_SlaveOutletKwatt11_Type = Integer32
_SlaveOutletKwatt11_Object = MibTableColumn
slaveOutletKwatt11 = _SlaveOutletKwatt11_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 12),
    _SlaveOutletKwatt11_Type()
)
slaveOutletKwatt11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt11.setStatus("mandatory")
_SlaveOutletKwatt12_Type = Integer32
_SlaveOutletKwatt12_Object = MibTableColumn
slaveOutletKwatt12 = _SlaveOutletKwatt12_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 2, 3, 1, 13),
    _SlaveOutletKwatt12_Type()
)
slaveOutletKwatt12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveOutletKwatt12.setStatus("mandatory")
_IpduSlaveOutletAction_ObjectIdentity = ObjectIdentity
ipduSlaveOutletAction = _IpduSlaveOutletAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3)
)
_IpduSlaveDeviceOutletActionTable_Object = MibTable
ipduSlaveDeviceOutletActionTable = _IpduSlaveDeviceOutletActionTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletActionTable.setStatus("mandatory")
_IpduSlaveDeviceOutletActionEntry_Object = MibTableRow
ipduSlaveDeviceOutletActionEntry = _IpduSlaveDeviceOutletActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1)
)
ipduSlaveDeviceOutletActionEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB-v2", "slaveOutletActionIndex"),
)
if mibBuilder.loadTexts:
    ipduSlaveDeviceOutletActionEntry.setStatus("mandatory")


class _SlaveOutletActionIndex_Type(Integer32):
    """Custom type slaveOutletActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlaveOutletActionIndex_Type.__name__ = "Integer32"
_SlaveOutletActionIndex_Object = MibTableColumn
slaveOutletActionIndex = _SlaveOutletActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 4, 3, 3, 1, 1, 13),
    _SlaveOutletAction12_Type()
)
slaveOutletAction12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveOutletAction12.setStatus("mandatory")
_IpduEnv_ObjectIdentity = ObjectIdentity
ipduEnv = _IpduEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5)
)
_IpduEnvEmd_ObjectIdentity = ObjectIdentity
ipduEnvEmd = _IpduEnvEmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1)
)
_IpduEnvEmdStatus_ObjectIdentity = ObjectIdentity
ipduEnvEmdStatus = _IpduEnvEmdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 1)
)


class _IpduEnvEmdStatusEmdType_Type(Integer32):
    """Custom type ipduEnvEmdStatusEmdType based on Integer32"""
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


_IpduEnvEmdStatusEmdType_Type.__name__ = "Integer32"
_IpduEnvEmdStatusEmdType_Object = MibScalar
ipduEnvEmdStatusEmdType = _IpduEnvEmdStatusEmdType_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 1, 1),
    _IpduEnvEmdStatusEmdType_Type()
)
ipduEnvEmdStatusEmdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduEnvEmdStatusEmdType.setStatus("mandatory")


class _IpduEnvEmdStatusTemperature_Type(Integer32):
    """Custom type ipduEnvEmdStatusTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_IpduEnvEmdStatusTemperature_Type.__name__ = "Integer32"
_IpduEnvEmdStatusTemperature_Object = MibScalar
ipduEnvEmdStatusTemperature = _IpduEnvEmdStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 1, 2),
    _IpduEnvEmdStatusTemperature_Type()
)
ipduEnvEmdStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduEnvEmdStatusTemperature.setStatus("mandatory")


class _IpduEnvEmdStatusHumidity_Type(Integer32):
    """Custom type ipduEnvEmdStatusHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_IpduEnvEmdStatusHumidity_Type.__name__ = "Integer32"
_IpduEnvEmdStatusHumidity_Object = MibScalar
ipduEnvEmdStatusHumidity = _IpduEnvEmdStatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 1, 3),
    _IpduEnvEmdStatusHumidity_Type()
)
ipduEnvEmdStatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduEnvEmdStatusHumidity.setStatus("mandatory")


class _IpduEnvEmdStatusAlarm1_Type(Integer32):
    """Custom type ipduEnvEmdStatusAlarm1 based on Integer32"""
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


_IpduEnvEmdStatusAlarm1_Type.__name__ = "Integer32"
_IpduEnvEmdStatusAlarm1_Object = MibScalar
ipduEnvEmdStatusAlarm1 = _IpduEnvEmdStatusAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 1, 4),
    _IpduEnvEmdStatusAlarm1_Type()
)
ipduEnvEmdStatusAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduEnvEmdStatusAlarm1.setStatus("mandatory")


class _IpduEnvEmdStatusAlarm2_Type(Integer32):
    """Custom type ipduEnvEmdStatusAlarm2 based on Integer32"""
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


_IpduEnvEmdStatusAlarm2_Type.__name__ = "Integer32"
_IpduEnvEmdStatusAlarm2_Object = MibScalar
ipduEnvEmdStatusAlarm2 = _IpduEnvEmdStatusAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 1, 5),
    _IpduEnvEmdStatusAlarm2_Type()
)
ipduEnvEmdStatusAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipduEnvEmdStatusAlarm2.setStatus("mandatory")
_IpduEnvEmdConfig_ObjectIdentity = ObjectIdentity
ipduEnvEmdConfig = _IpduEnvEmdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2)
)


class _IpduEnvEmdConfigEmdPresence_Type(Integer32):
    """Custom type ipduEnvEmdConfigEmdPresence based on Integer32"""
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


_IpduEnvEmdConfigEmdPresence_Type.__name__ = "Integer32"
_IpduEnvEmdConfigEmdPresence_Object = MibScalar
ipduEnvEmdConfigEmdPresence = _IpduEnvEmdConfigEmdPresence_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 1),
    _IpduEnvEmdConfigEmdPresence_Type()
)
ipduEnvEmdConfigEmdPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigEmdPresence.setStatus("mandatory")


class _IpduEnvEmdConfigEmdName_Type(DisplayString):
    """Custom type ipduEnvEmdConfigEmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduEnvEmdConfigEmdName_Type.__name__ = "DisplayString"
_IpduEnvEmdConfigEmdName_Object = MibScalar
ipduEnvEmdConfigEmdName = _IpduEnvEmdConfigEmdName_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 2),
    _IpduEnvEmdConfigEmdName_Type()
)
ipduEnvEmdConfigEmdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigEmdName.setStatus("mandatory")
_IpduEnvEmdConfigTemp_ObjectIdentity = ObjectIdentity
ipduEnvEmdConfigTemp = _IpduEnvEmdConfigTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 3)
)


class _IpduEnvEmdConfigTempName_Type(DisplayString):
    """Custom type ipduEnvEmdConfigTempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduEnvEmdConfigTempName_Type.__name__ = "DisplayString"
_IpduEnvEmdConfigTempName_Object = MibScalar
ipduEnvEmdConfigTempName = _IpduEnvEmdConfigTempName_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 3, 1),
    _IpduEnvEmdConfigTempName_Type()
)
ipduEnvEmdConfigTempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigTempName.setStatus("mandatory")


class _IpduEnvEmdConfigTempHighSetPoint_Type(Integer32):
    """Custom type ipduEnvEmdConfigTempHighSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65),
    )


_IpduEnvEmdConfigTempHighSetPoint_Type.__name__ = "Integer32"
_IpduEnvEmdConfigTempHighSetPoint_Object = MibScalar
ipduEnvEmdConfigTempHighSetPoint = _IpduEnvEmdConfigTempHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 3, 2),
    _IpduEnvEmdConfigTempHighSetPoint_Type()
)
ipduEnvEmdConfigTempHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigTempHighSetPoint.setStatus("mandatory")


class _IpduEnvEmdConfigTempHighStatus_Type(Integer32):
    """Custom type ipduEnvEmdConfigTempHighStatus based on Integer32"""
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


_IpduEnvEmdConfigTempHighStatus_Type.__name__ = "Integer32"
_IpduEnvEmdConfigTempHighStatus_Object = MibScalar
ipduEnvEmdConfigTempHighStatus = _IpduEnvEmdConfigTempHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 3, 3),
    _IpduEnvEmdConfigTempHighStatus_Type()
)
ipduEnvEmdConfigTempHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigTempHighStatus.setStatus("mandatory")


class _IpduEnvEmdConfigTempLowSetPoint_Type(Integer32):
    """Custom type ipduEnvEmdConfigTempLowSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65),
    )


_IpduEnvEmdConfigTempLowSetPoint_Type.__name__ = "Integer32"
_IpduEnvEmdConfigTempLowSetPoint_Object = MibScalar
ipduEnvEmdConfigTempLowSetPoint = _IpduEnvEmdConfigTempLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 3, 4),
    _IpduEnvEmdConfigTempLowSetPoint_Type()
)
ipduEnvEmdConfigTempLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigTempLowSetPoint.setStatus("mandatory")


class _IpduEnvEmdConfigTempLowStatus_Type(Integer32):
    """Custom type ipduEnvEmdConfigTempLowStatus based on Integer32"""
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


_IpduEnvEmdConfigTempLowStatus_Type.__name__ = "Integer32"
_IpduEnvEmdConfigTempLowStatus_Object = MibScalar
ipduEnvEmdConfigTempLowStatus = _IpduEnvEmdConfigTempLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 3, 5),
    _IpduEnvEmdConfigTempLowStatus_Type()
)
ipduEnvEmdConfigTempLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigTempLowStatus.setStatus("mandatory")


class _IpduEnvEmdConfigTempOffset_Type(Integer32):
    """Custom type ipduEnvEmdConfigTempOffset based on Integer32"""
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


_IpduEnvEmdConfigTempOffset_Type.__name__ = "Integer32"
_IpduEnvEmdConfigTempOffset_Object = MibScalar
ipduEnvEmdConfigTempOffset = _IpduEnvEmdConfigTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 3, 6),
    _IpduEnvEmdConfigTempOffset_Type()
)
ipduEnvEmdConfigTempOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigTempOffset.setStatus("mandatory")
_IpduEnvEmdConfigHumi_ObjectIdentity = ObjectIdentity
ipduEnvEmdConfigHumi = _IpduEnvEmdConfigHumi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 4)
)


class _IpduEnvEmdConfigHumiName_Type(DisplayString):
    """Custom type ipduEnvEmdConfigHumiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduEnvEmdConfigHumiName_Type.__name__ = "DisplayString"
_IpduEnvEmdConfigHumiName_Object = MibScalar
ipduEnvEmdConfigHumiName = _IpduEnvEmdConfigHumiName_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 4, 1),
    _IpduEnvEmdConfigHumiName_Type()
)
ipduEnvEmdConfigHumiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigHumiName.setStatus("mandatory")


class _IpduEnvEmdConfigHumiHighSetPoint_Type(Integer32):
    """Custom type ipduEnvEmdConfigHumiHighSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 95),
    )


_IpduEnvEmdConfigHumiHighSetPoint_Type.__name__ = "Integer32"
_IpduEnvEmdConfigHumiHighSetPoint_Object = MibScalar
ipduEnvEmdConfigHumiHighSetPoint = _IpduEnvEmdConfigHumiHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 4, 2),
    _IpduEnvEmdConfigHumiHighSetPoint_Type()
)
ipduEnvEmdConfigHumiHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigHumiHighSetPoint.setStatus("mandatory")


class _IpduEnvEmdConfigHumiHighStatus_Type(Integer32):
    """Custom type ipduEnvEmdConfigHumiHighStatus based on Integer32"""
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


_IpduEnvEmdConfigHumiHighStatus_Type.__name__ = "Integer32"
_IpduEnvEmdConfigHumiHighStatus_Object = MibScalar
ipduEnvEmdConfigHumiHighStatus = _IpduEnvEmdConfigHumiHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 4, 3),
    _IpduEnvEmdConfigHumiHighStatus_Type()
)
ipduEnvEmdConfigHumiHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigHumiHighStatus.setStatus("mandatory")


class _IpduEnvEmdConfigHumiLowSetPoint_Type(Integer32):
    """Custom type ipduEnvEmdConfigHumiLowSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 95),
    )


_IpduEnvEmdConfigHumiLowSetPoint_Type.__name__ = "Integer32"
_IpduEnvEmdConfigHumiLowSetPoint_Object = MibScalar
ipduEnvEmdConfigHumiLowSetPoint = _IpduEnvEmdConfigHumiLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 4, 4),
    _IpduEnvEmdConfigHumiLowSetPoint_Type()
)
ipduEnvEmdConfigHumiLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigHumiLowSetPoint.setStatus("mandatory")


class _IpduEnvEmdConfigHumiLowStatus_Type(Integer32):
    """Custom type ipduEnvEmdConfigHumiLowStatus based on Integer32"""
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


_IpduEnvEmdConfigHumiLowStatus_Type.__name__ = "Integer32"
_IpduEnvEmdConfigHumiLowStatus_Object = MibScalar
ipduEnvEmdConfigHumiLowStatus = _IpduEnvEmdConfigHumiLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 4, 5),
    _IpduEnvEmdConfigHumiLowStatus_Type()
)
ipduEnvEmdConfigHumiLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigHumiLowStatus.setStatus("mandatory")


class _IpduEnvEmdConfigHumiOffset_Type(Integer32):
    """Custom type ipduEnvEmdConfigHumiOffset based on Integer32"""
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


_IpduEnvEmdConfigHumiOffset_Type.__name__ = "Integer32"
_IpduEnvEmdConfigHumiOffset_Object = MibScalar
ipduEnvEmdConfigHumiOffset = _IpduEnvEmdConfigHumiOffset_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 4, 6),
    _IpduEnvEmdConfigHumiOffset_Type()
)
ipduEnvEmdConfigHumiOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigHumiOffset.setStatus("mandatory")
_IpduEnvEmdConfigAlarm1_ObjectIdentity = ObjectIdentity
ipduEnvEmdConfigAlarm1 = _IpduEnvEmdConfigAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 5)
)


class _IpduEnvEmdConfigAlarm1Name_Type(DisplayString):
    """Custom type ipduEnvEmdConfigAlarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduEnvEmdConfigAlarm1Name_Type.__name__ = "DisplayString"
_IpduEnvEmdConfigAlarm1Name_Object = MibScalar
ipduEnvEmdConfigAlarm1Name = _IpduEnvEmdConfigAlarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 5, 1),
    _IpduEnvEmdConfigAlarm1Name_Type()
)
ipduEnvEmdConfigAlarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigAlarm1Name.setStatus("mandatory")


class _IpduEnvEmdConfigAlarm1Type_Type(Integer32):
    """Custom type ipduEnvEmdConfigAlarm1Type based on Integer32"""
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


_IpduEnvEmdConfigAlarm1Type_Type.__name__ = "Integer32"
_IpduEnvEmdConfigAlarm1Type_Object = MibScalar
ipduEnvEmdConfigAlarm1Type = _IpduEnvEmdConfigAlarm1Type_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 5, 2),
    _IpduEnvEmdConfigAlarm1Type_Type()
)
ipduEnvEmdConfigAlarm1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigAlarm1Type.setStatus("mandatory")
_IpduEnvEmdConfigAlarm2_ObjectIdentity = ObjectIdentity
ipduEnvEmdConfigAlarm2 = _IpduEnvEmdConfigAlarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 6)
)


class _IpduEnvEmdConfigAlarm2Name_Type(DisplayString):
    """Custom type ipduEnvEmdConfigAlarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpduEnvEmdConfigAlarm2Name_Type.__name__ = "DisplayString"
_IpduEnvEmdConfigAlarm2Name_Object = MibScalar
ipduEnvEmdConfigAlarm2Name = _IpduEnvEmdConfigAlarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 6, 1),
    _IpduEnvEmdConfigAlarm2Name_Type()
)
ipduEnvEmdConfigAlarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigAlarm2Name.setStatus("mandatory")


class _IpduEnvEmdConfigAlarm2Type_Type(Integer32):
    """Custom type ipduEnvEmdConfigAlarm2Type based on Integer32"""
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


_IpduEnvEmdConfigAlarm2Type_Type.__name__ = "Integer32"
_IpduEnvEmdConfigAlarm2Type_Object = MibScalar
ipduEnvEmdConfigAlarm2Type = _IpduEnvEmdConfigAlarm2Type_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 1, 5, 1, 2, 6, 2),
    _IpduEnvEmdConfigAlarm2Type_Type()
)
ipduEnvEmdConfigAlarm2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipduEnvEmdConfigAlarm2Type.setStatus("mandatory")
_IpduTraps_ObjectIdentity = ObjectIdentity
ipduTraps = _IpduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2)
)

# Managed Objects groups


# Notification objects

ipduInletVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 1)
)
ipduInletVoltageTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletVoltageTooHigh.setStatus(
        ""
    )

ipduInletVoltageNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 2)
)
ipduInletVoltageNotTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletVoltageNotTooHigh.setStatus(
        ""
    )

ipduInletVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 3)
)
ipduInletVoltageTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletVoltageTooLow.setStatus(
        ""
    )

ipduInletVoltageNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 4)
)
ipduInletVoltageNotTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletVoltageNotTooLow.setStatus(
        ""
    )

ipduInletCurrentTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 5)
)
ipduInletCurrentTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusCurrent"),
        ("SOCOMECUPS-MIB-v2", "inletConfigCurrentHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletCurrentTooHigh.setStatus(
        ""
    )

ipduInletCurrentNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 6)
)
ipduInletCurrentNotTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusCurrent"),
        ("SOCOMECUPS-MIB-v2", "inletConfigCurrentHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletCurrentNotTooHigh.setStatus(
        ""
    )

ipduInletFrequencyTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 7)
)
ipduInletFrequencyTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletFrequencyTooHigh.setStatus(
        ""
    )

ipduInletFrequencyNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 8)
)
ipduInletFrequencyNotTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletFrequencyNotTooHigh.setStatus(
        ""
    )

ipduInletFrequencyTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 9)
)
ipduInletFrequencyTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletFrequencyTooLow.setStatus(
        ""
    )

ipduInletFrequencyNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 10)
)
ipduInletFrequencyNotTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInletFrequencyNotTooLow.setStatus(
        ""
    )

ipduInlet2VoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 11)
)
ipduInlet2VoltageTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2VoltageTooHigh.setStatus(
        ""
    )

ipduInlet2VoltageNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 12)
)
ipduInlet2VoltageNotTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2VoltageNotTooHigh.setStatus(
        ""
    )

ipduInlet2VoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 13)
)
ipduInlet2VoltageTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2VoltageTooLow.setStatus(
        ""
    )

ipduInlet2VoltageNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 14)
)
ipduInlet2VoltageNotTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusVoltage"),
        ("SOCOMECUPS-MIB-v2", "inletConfigVoltageLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2VoltageNotTooLow.setStatus(
        ""
    )

ipduInlet2CurrentTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 15)
)
ipduInlet2CurrentTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusCurrent"),
        ("SOCOMECUPS-MIB-v2", "inletConfigCurrentHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2CurrentTooHigh.setStatus(
        ""
    )

ipduInlet2CurrentNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 16)
)
ipduInlet2CurrentNotTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusCurrent"),
        ("SOCOMECUPS-MIB-v2", "inletConfigCurrentHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2CurrentNotTooHigh.setStatus(
        ""
    )

ipduInlet2FrequencyTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 17)
)
ipduInlet2FrequencyTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2FrequencyTooHigh.setStatus(
        ""
    )

ipduInlet2FrequencyNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 18)
)
ipduInlet2FrequencyNotTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyHigh"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2FrequencyNotTooHigh.setStatus(
        ""
    )

ipduInlet2FrequencyTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 19)
)
ipduInlet2FrequencyTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2FrequencyTooLow.setStatus(
        ""
    )

ipduInlet2FrequencyNotTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 20)
)
ipduInlet2FrequencyNotTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "inletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "inletStatusFrequency"),
        ("SOCOMECUPS-MIB-v2", "inletConfigFrequencyLow"),
        ("SOCOMECUPS-MIB-v2", "inletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduInlet2FrequencyNotTooLow.setStatus(
        ""
    )

ipduOutletCurrentTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 21)
)
ipduOutletCurrentTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "outletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "outletStatusCurrent"),
        ("SOCOMECUPS-MIB-v2", "outletConfigCurrentHigh"),
        ("SOCOMECUPS-MIB-v2", "outletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduOutletCurrentTooHigh.setStatus(
        ""
    )

ipduOutletCurrentNotTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 22)
)
ipduOutletCurrentNotTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "outletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "outletStatusCurrent"),
        ("SOCOMECUPS-MIB-v2", "outletConfigCurrentHigh"),
        ("SOCOMECUPS-MIB-v2", "outletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduOutletCurrentNotTooHigh.setStatus(
        ""
    )

ipduOutletStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 23)
)
ipduOutletStateChanged.setObjects(
      *(("SOCOMECUPS-MIB-v2", "outletConfigIndex"),
        ("SOCOMECUPS-MIB-v2", "outletStatusStatus"),
        ("SOCOMECUPS-MIB-v2", "outletConfigDesc"))
)
if mibBuilder.loadTexts:
    ipduOutletStateChanged.setStatus(
        ""
    )

ipduEmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 24)
)
ipduEmdTemperatureNotHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusTemperature"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempHighSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipduEmdTemperatureNotHigh.setStatus(
        ""
    )

ipduEmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 25)
)
ipduEmdTemperatureTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusTemperature"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempHighSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipduEmdTemperatureTooHigh.setStatus(
        ""
    )

ipduEmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 26)
)
ipduEmdTemperatureNotLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusTemperature"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempLowSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipduEmdTemperatureNotLow.setStatus(
        ""
    )

ipduEmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 27)
)
ipduEmdTemperatureTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusTemperature"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempLowSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigTempName"))
)
if mibBuilder.loadTexts:
    ipduEmdTemperatureTooLow.setStatus(
        ""
    )

ipduEmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 28)
)
ipduEmdHumidityNotHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusHumidity"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiHighSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipduEmdHumidityNotHigh.setStatus(
        ""
    )

ipduEmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 29)
)
ipduEmdHumidityTooHigh.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusHumidity"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiHighSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipduEmdHumidityTooHigh.setStatus(
        ""
    )

ipduEmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 30)
)
ipduEmdHumidityNotLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusHumidity"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiLowSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipduEmdHumidityNotLow.setStatus(
        ""
    )

ipduEmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 31)
)
ipduEmdHumidityTooLow.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdStatusHumidity"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiLowSetPoint"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigHumiName"))
)
if mibBuilder.loadTexts:
    ipduEmdHumidityTooLow.setStatus(
        ""
    )

ipduEmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 32)
)
ipduEmdAlarm1Normal.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm1Type"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    ipduEmdAlarm1Normal.setStatus(
        ""
    )

ipduEmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 33)
)
ipduEmdAlarm1Active.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm1Type"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    ipduEmdAlarm1Active.setStatus(
        ""
    )

ipduEmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 34)
)
ipduEmdAlarm2Normal.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm2Type"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    ipduEmdAlarm2Normal.setStatus(
        ""
    )

ipduEmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 35)
)
ipduEmdAlarm2Active.setObjects(
      *(("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm2Type"),
        ("SOCOMECUPS-MIB-v2", "ipduEnvEmdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    ipduEmdAlarm2Active.setStatus(
        ""
    )

ipduSlave01Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 36)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet01OverHigh.setStatus(
        ""
    )

ipduSlave01Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 37)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet01NotOverHigh.setStatus(
        ""
    )

ipduSlave01Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 38)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet02OverHigh.setStatus(
        ""
    )

ipduSlave01Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 39)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet02NotOverHigh.setStatus(
        ""
    )

ipduSlave01Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 40)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet01UnderLow.setStatus(
        ""
    )

ipduSlave01Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 41)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet01NotUnderLow.setStatus(
        ""
    )

ipduSlave01Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 42)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet02UnderLow.setStatus(
        ""
    )

ipduSlave01Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 43)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet02NotUnderLow.setStatus(
        ""
    )

ipduSlave01Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 44)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet01CurrentOverTh.setStatus(
        ""
    )

ipduSlave01Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 45)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave01Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 46)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet02CurrentOverTh.setStatus(
        ""
    )

ipduSlave01Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 47)
)
if mibBuilder.loadTexts:
    ipduSlave01Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave01EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 48)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdTemperatureNotHigh.setStatus(
        ""
    )

ipduSlave01EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 49)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdTemperatureTooHigh.setStatus(
        ""
    )

ipduSlave01EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 50)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdTemperatureNotLow.setStatus(
        ""
    )

ipduSlave01EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 51)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdTemperatureTooLow.setStatus(
        ""
    )

ipduSlave01EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 52)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdHumidityNotHigh.setStatus(
        ""
    )

ipduSlave01EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 53)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdHumidityTooHigh.setStatus(
        ""
    )

ipduSlave01EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 54)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdHumidityNotLow.setStatus(
        ""
    )

ipduSlave01EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 55)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdHumidityTooLow.setStatus(
        ""
    )

ipduSlave01EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 56)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdAlarm1Normal.setStatus(
        ""
    )

ipduSlave01EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 57)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdAlarm1Active.setStatus(
        ""
    )

ipduSlave01EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 58)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdAlarm2Normal.setStatus(
        ""
    )

ipduSlave01EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 59)
)
if mibBuilder.loadTexts:
    ipduSlave01EmdAlarm2Active.setStatus(
        ""
    )

ipduSlave01OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 60)
)
if mibBuilder.loadTexts:
    ipduSlave01OutletCurrentOverTh.setStatus(
        ""
    )

ipduSlave02Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 61)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet01OverHigh.setStatus(
        ""
    )

ipduSlave02Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 62)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet01NotOverHigh.setStatus(
        ""
    )

ipduSlave02Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 63)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet02OverHigh.setStatus(
        ""
    )

ipduSlave02Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 64)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet02NotOverHigh.setStatus(
        ""
    )

ipduSlave02Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 65)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet01UnderLow.setStatus(
        ""
    )

ipduSlave02Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 66)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet01NotUnderLow.setStatus(
        ""
    )

ipduSlave02Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 67)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet02UnderLow.setStatus(
        ""
    )

ipduSlave02Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 68)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet02NotUnderLow.setStatus(
        ""
    )

ipduSlave02Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 69)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet01CurrentOverTh.setStatus(
        ""
    )

ipduSlave02Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 70)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave02Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 71)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet02CurrentOverTh.setStatus(
        ""
    )

ipduSlave02Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 72)
)
if mibBuilder.loadTexts:
    ipduSlave02Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave02EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 73)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdTemperatureNotHigh.setStatus(
        ""
    )

ipduSlave02EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 74)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdTemperatureTooHigh.setStatus(
        ""
    )

ipduSlave02EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 75)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdTemperatureNotLow.setStatus(
        ""
    )

ipduSlave02EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 76)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdTemperatureTooLow.setStatus(
        ""
    )

ipduSlave02EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 77)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdHumidityNotHigh.setStatus(
        ""
    )

ipduSlave02EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 78)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdHumidityTooHigh.setStatus(
        ""
    )

ipduSlave02EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 79)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdHumidityNotLow.setStatus(
        ""
    )

ipduSlave02EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 80)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdHumidityTooLow.setStatus(
        ""
    )

ipduSlave02EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 81)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdAlarm1Normal.setStatus(
        ""
    )

ipduSlave02EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 82)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdAlarm1Active.setStatus(
        ""
    )

ipduSlave02EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 83)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdAlarm2Normal.setStatus(
        ""
    )

ipduSlave02EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 84)
)
if mibBuilder.loadTexts:
    ipduSlave02EmdAlarm2Active.setStatus(
        ""
    )

ipduSlave02OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 85)
)
if mibBuilder.loadTexts:
    ipduSlave02OutletCurrentOverTh.setStatus(
        ""
    )

ipduSlave03Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 86)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet01OverHigh.setStatus(
        ""
    )

ipduSlave03Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 87)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet01NotOverHigh.setStatus(
        ""
    )

ipduSlave03Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 88)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet02OverHigh.setStatus(
        ""
    )

ipduSlave03Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 89)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet02NotOverHigh.setStatus(
        ""
    )

ipduSlave03Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 90)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet01UnderLow.setStatus(
        ""
    )

ipduSlave03Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 91)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet01NotUnderLow.setStatus(
        ""
    )

ipduSlave03Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 92)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet02UnderLow.setStatus(
        ""
    )

ipduSlave03Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 93)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet02NotUnderLow.setStatus(
        ""
    )

ipduSlave03Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 94)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet01CurrentOverTh.setStatus(
        ""
    )

ipduSlave03Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 95)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave03Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 96)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet02CurrentOverTh.setStatus(
        ""
    )

ipduSlave03Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 97)
)
if mibBuilder.loadTexts:
    ipduSlave03Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave03EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 98)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdTemperatureNotHigh.setStatus(
        ""
    )

ipduSlave03EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 99)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdTemperatureTooHigh.setStatus(
        ""
    )

ipduSlave03EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 100)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdTemperatureNotLow.setStatus(
        ""
    )

ipduSlave03EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 101)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdTemperatureTooLow.setStatus(
        ""
    )

ipduSlave03EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 102)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdHumidityNotHigh.setStatus(
        ""
    )

ipduSlave03EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 103)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdHumidityTooHigh.setStatus(
        ""
    )

ipduSlave03EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 104)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdHumidityNotLow.setStatus(
        ""
    )

ipduSlave03EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 105)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdHumidityTooLow.setStatus(
        ""
    )

ipduSlave03EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 106)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdAlarm1Normal.setStatus(
        ""
    )

ipduSlave03EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 107)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdAlarm1Active.setStatus(
        ""
    )

ipduSlave03EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 108)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdAlarm2Normal.setStatus(
        ""
    )

ipduSlave03EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 109)
)
if mibBuilder.loadTexts:
    ipduSlave03EmdAlarm2Active.setStatus(
        ""
    )

ipduSlave03OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 110)
)
if mibBuilder.loadTexts:
    ipduSlave03OutletCurrentOverTh.setStatus(
        ""
    )

ipduSlave04Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 111)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet01OverHigh.setStatus(
        ""
    )

ipduSlave04Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 112)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet01NotOverHigh.setStatus(
        ""
    )

ipduSlave04Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 113)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet02OverHigh.setStatus(
        ""
    )

ipduSlave04Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 114)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet02NotOverHigh.setStatus(
        ""
    )

ipduSlave04Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 115)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet01UnderLow.setStatus(
        ""
    )

ipduSlave04Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 116)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet01NotUnderLow.setStatus(
        ""
    )

ipduSlave04Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 117)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet02UnderLow.setStatus(
        ""
    )

ipduSlave04Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 118)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet02NotUnderLow.setStatus(
        ""
    )

ipduSlave04Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 119)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet01CurrentOverTh.setStatus(
        ""
    )

ipduSlave04Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 120)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave04Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 121)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet02CurrentOverTh.setStatus(
        ""
    )

ipduSlave04Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 122)
)
if mibBuilder.loadTexts:
    ipduSlave04Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave04EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 123)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdTemperatureNotHigh.setStatus(
        ""
    )

ipduSlave04EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 124)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdTemperatureTooHigh.setStatus(
        ""
    )

ipduSlave04EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 125)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdTemperatureNotLow.setStatus(
        ""
    )

ipduSlave04EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 126)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdTemperatureTooLow.setStatus(
        ""
    )

ipduSlave04EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 127)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdHumidityNotHigh.setStatus(
        ""
    )

ipduSlave04EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 128)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdHumidityTooHigh.setStatus(
        ""
    )

ipduSlave04EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 129)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdHumidityNotLow.setStatus(
        ""
    )

ipduSlave04EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 130)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdHumidityTooLow.setStatus(
        ""
    )

ipduSlave04EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 131)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdAlarm1Normal.setStatus(
        ""
    )

ipduSlave04EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 132)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdAlarm1Active.setStatus(
        ""
    )

ipduSlave04EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 133)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdAlarm2Normal.setStatus(
        ""
    )

ipduSlave04EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 134)
)
if mibBuilder.loadTexts:
    ipduSlave04EmdAlarm2Active.setStatus(
        ""
    )

ipduSlave04OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 135)
)
if mibBuilder.loadTexts:
    ipduSlave04OutletCurrentOverTh.setStatus(
        ""
    )

ipduSlave05Inlet01OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 136)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet01OverHigh.setStatus(
        ""
    )

ipduSlave05Inlet01NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 137)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet01NotOverHigh.setStatus(
        ""
    )

ipduSlave05Inlet02OverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 138)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet02OverHigh.setStatus(
        ""
    )

ipduSlave05Inlet02NotOverHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 139)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet02NotOverHigh.setStatus(
        ""
    )

ipduSlave05Inlet01UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 140)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet01UnderLow.setStatus(
        ""
    )

ipduSlave05Inlet01NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 141)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet01NotUnderLow.setStatus(
        ""
    )

ipduSlave05Inlet02UnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 142)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet02UnderLow.setStatus(
        ""
    )

ipduSlave05Inlet02NotUnderLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 143)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet02NotUnderLow.setStatus(
        ""
    )

ipduSlave05Inlet01CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 144)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet01CurrentOverTh.setStatus(
        ""
    )

ipduSlave05Inlet01NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 145)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet01NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave05Inlet02CurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 146)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet02CurrentOverTh.setStatus(
        ""
    )

ipduSlave05Inlet02NotCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 147)
)
if mibBuilder.loadTexts:
    ipduSlave05Inlet02NotCurrentOverTh.setStatus(
        ""
    )

ipduSlave05EmdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 148)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdTemperatureNotHigh.setStatus(
        ""
    )

ipduSlave05EmdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 149)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdTemperatureTooHigh.setStatus(
        ""
    )

ipduSlave05EmdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 150)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdTemperatureNotLow.setStatus(
        ""
    )

ipduSlave05EmdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 151)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdTemperatureTooLow.setStatus(
        ""
    )

ipduSlave05EmdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 152)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdHumidityNotHigh.setStatus(
        ""
    )

ipduSlave05EmdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 153)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdHumidityTooHigh.setStatus(
        ""
    )

ipduSlave05EmdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 154)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdHumidityNotLow.setStatus(
        ""
    )

ipduSlave05EmdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 155)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdHumidityTooLow.setStatus(
        ""
    )

ipduSlave05EmdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 156)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdAlarm1Normal.setStatus(
        ""
    )

ipduSlave05EmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 157)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdAlarm1Active.setStatus(
        ""
    )

ipduSlave05EmdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 158)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdAlarm2Normal.setStatus(
        ""
    )

ipduSlave05EmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 159)
)
if mibBuilder.loadTexts:
    ipduSlave05EmdAlarm2Active.setStatus(
        ""
    )

ipduSlave05OutletCurrentOverTh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 20, 2, 0, 160)
)
if mibBuilder.loadTexts:
    ipduSlave05OutletCurrentOverTh.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SOCOMECUPS-MIB-v2",
    **{"socomecSicon": socomecSicon,
       "product": product,
       "pduAgent": pduAgent,
       "iPDU": iPDU,
       "ipduObjects": ipduObjects,
       "ipduIdent": ipduIdent,
       "ipduIdentManufacturer": ipduIdentManufacturer,
       "ipduIdentModel": ipduIdentModel,
       "ipduIdentAgentSoftwareVersion": ipduIdentAgentSoftwareVersion,
       "ipduIdentName": ipduIdentName,
       "ipduAgent": ipduAgent,
       "ipduAgentConfig": ipduAgentConfig,
       "ipduAgentMibVersion": ipduAgentMibVersion,
       "ipduAgentLog": ipduAgentLog,
       "pduAgentDataLogInterval": pduAgentDataLogInterval,
       "ipduAgentControl": ipduAgentControl,
       "ipduAgentControlDefault": ipduAgentControlDefault,
       "ipduAgentControlRestart": ipduAgentControlRestart,
       "ipduAgentTrap": ipduAgentTrap,
       "ipduAgentTrapRetryCount": ipduAgentTrapRetryCount,
       "ipduAgentTrapRetryTime": ipduAgentTrapRetryTime,
       "ipduAgentTrapAckSignature": ipduAgentTrapAckSignature,
       "ipduAgentTrapsReceiversTable": ipduAgentTrapsReceiversTable,
       "ipduAgentTrapsReceiversEntry": ipduAgentTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "receiverNmsType": receiverNmsType,
       "receiverSeverityLevel": receiverSeverityLevel,
       "receiverDescription": receiverDescription,
       "ipduAgentAccessControlTable": ipduAgentAccessControlTable,
       "ipduAgentAccessControlEntry": ipduAgentAccessControlEntry,
       "accessIndex": accessIndex,
       "accessControlAddr": accessControlAddr,
       "accessControlMode": accessControlMode,
       "ipduAgentTime": ipduAgentTime,
       "ipduAgentTimeDate": ipduAgentTimeDate,
       "ipduAgentTimeTime": ipduAgentTimeTime,
       "ipduAgentTimerFromNtp": ipduAgentTimerFromNtp,
       "ipduAgentNtpIpAddress": ipduAgentNtpIpAddress,
       "ipduAgentNtpTimeZone": ipduAgentNtpTimeZone,
       "ipduAgentDayLightSaving": ipduAgentDayLightSaving,
       "ipduAgentNetwork": ipduAgentNetwork,
       "ipduAgentNetworkIp": ipduAgentNetworkIp,
       "ipduAgentNetworkIpAdress": ipduAgentNetworkIpAdress,
       "ipduAgentNetworkIpGateway": ipduAgentNetworkIpGateway,
       "ipduAgentNetworkIpSubnet": ipduAgentNetworkIpSubnet,
       "ipduAgentNetworkDhcpControl": ipduAgentNetworkDhcpControl,
       "ipduAgentNetworkPingControl": ipduAgentNetworkPingControl,
       "ipduAgentNetworkTftpControl": ipduAgentNetworkTftpControl,
       "ipduAgentNetworkTelnet": ipduAgentNetworkTelnet,
       "ipduAgentTelnetControl": ipduAgentTelnetControl,
       "ipduAgentTelnetPort": ipduAgentTelnetPort,
       "ipduAgentNetworkHttp": ipduAgentNetworkHttp,
       "ipduAgentHttpControl": ipduAgentHttpControl,
       "ipduAgentHttpPort": ipduAgentHttpPort,
       "ipduAgentNetworkSnmp": ipduAgentNetworkSnmp,
       "ipduAgentSnmpControl": ipduAgentSnmpControl,
       "ipduAgentSnmpPort": ipduAgentSnmpPort,
       "ipduDevice": ipduDevice,
       "ipduDeviceInlet": ipduDeviceInlet,
       "ipduDeviceInletNumber": ipduDeviceInletNumber,
       "ipduDeviceInletConfigTable": ipduDeviceInletConfigTable,
       "ipduDeviceInletConfigEntry": ipduDeviceInletConfigEntry,
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
       "ipduDeviceInletStatusTable": ipduDeviceInletStatusTable,
       "ipduDeviceInletStatusEntry": ipduDeviceInletStatusEntry,
       "inletStatusIndex": inletStatusIndex,
       "inletStatusVoltage": inletStatusVoltage,
       "inletStatusCurrent": inletStatusCurrent,
       "inletStatusFrequency": inletStatusFrequency,
       "inletStatusKwatt": inletStatusKwatt,
       "inletStatusWH": inletStatusWH,
       "inletWattReset": inletWattReset,
       "ipduDeviceOutlet": ipduDeviceOutlet,
       "ipduDeviceOutletNumber": ipduDeviceOutletNumber,
       "ipduDeviceOutletConfigTable": ipduDeviceOutletConfigTable,
       "ipduDeviceOutletConfigEntry": ipduDeviceOutletConfigEntry,
       "outletConfigIndex": outletConfigIndex,
       "outletConfigDesc": outletConfigDesc,
       "outletConfigLocation": outletConfigLocation,
       "outletConfigOnDelay": outletConfigOnDelay,
       "outletConfigOffDelay": outletConfigOffDelay,
       "outletConfigCurrentHigh": outletConfigCurrentHigh,
       "outletConfigCurrentHighAction": outletConfigCurrentHighAction,
       "ipduDeviceOutletStatusTable": ipduDeviceOutletStatusTable,
       "ipduDeviceOutletStatusEntry": ipduDeviceOutletStatusEntry,
       "outletStatusIndex": outletStatusIndex,
       "outletStatusStatus": outletStatusStatus,
       "outletStatusCurrent": outletStatusCurrent,
       "outletStatusKwatt": outletStatusKwatt,
       "outletStatusWH": outletStatusWH,
       "outletStatusStateTime": outletStatusStateTime,
       "outletStatusTimeToGo": outletStatusTimeToGo,
       "ipduDeviceOutletControlTable": ipduDeviceOutletControlTable,
       "ipduDeviceOutletControlEntry": ipduDeviceOutletControlEntry,
       "outletControlIndex": outletControlIndex,
       "outletControlControl": outletControlControl,
       "ipduDeviceOutletControlAll": ipduDeviceOutletControlAll,
       "ipduDeviceOutletWattReset": ipduDeviceOutletWattReset,
       "ipduDeviceCcOut": ipduDeviceCcOut,
       "ipduDeviceCcOutNumber": ipduDeviceCcOutNumber,
       "ipduDeviceCcOutConfigTable": ipduDeviceCcOutConfigTable,
       "ipduDeviceCcOutConfigEntry": ipduDeviceCcOutConfigEntry,
       "ccOutConfigIndex": ccOutConfigIndex,
       "ccOutConfigDesc": ccOutConfigDesc,
       "ccOutConfigEventAction": ccOutConfigEventAction,
       "ccOutConfigCloseDelay": ccOutConfigCloseDelay,
       "ccOutConfigOpenDelay": ccOutConfigOpenDelay,
       "ipduDeviceCcOutStatusTable": ipduDeviceCcOutStatusTable,
       "ipduDeviceCcOutStatusEntry": ipduDeviceCcOutStatusEntry,
       "ccOutStatusIndex": ccOutStatusIndex,
       "ccOutStatusStatus": ccOutStatusStatus,
       "ccOutStatusTimeOnState": ccOutStatusTimeOnState,
       "ipduDeviceCcOutControlTable": ipduDeviceCcOutControlTable,
       "ipduDeviceCcOutControlEntry": ipduDeviceCcOutControlEntry,
       "ccOutControlIndex": ccOutControlIndex,
       "ccOutControlControl": ccOutControlControl,
       "ipduSlave": ipduSlave,
       "ipduSlaveState": ipduSlaveState,
       "ipduSlaveStateTable": ipduSlaveStateTable,
       "ipduSlaveStateEntry": ipduSlaveStateEntry,
       "slaveStateIndex": slaveStateIndex,
       "slaveStateControl01": slaveStateControl01,
       "ipduSlaveInlet": ipduSlaveInlet,
       "ipduSlaveInletStatus": ipduSlaveInletStatus,
       "ipduDeviceSlaveInletStatusTable": ipduDeviceSlaveInletStatusTable,
       "ipduDeviceSlaveInletStatusEntry": ipduDeviceSlaveInletStatusEntry,
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
       "ipduSlaveInletConfig": ipduSlaveInletConfig,
       "ipduDeviceslaveInletConfigTable": ipduDeviceslaveInletConfigTable,
       "ipduDeviceslaveInletConfigEntry": ipduDeviceslaveInletConfigEntry,
       "slaveInletConfigIndex": slaveInletConfigIndex,
       "slaveInletConfigVoltageHigh": slaveInletConfigVoltageHigh,
       "slaveInletConfigVoltageLow": slaveInletConfigVoltageLow,
       "slaveInlet2ConfigVoltageHigh": slaveInlet2ConfigVoltageHigh,
       "slaveInlet2ConfigVoltageLow": slaveInlet2ConfigVoltageLow,
       "ipduSlaveOutlet": ipduSlaveOutlet,
       "ipduSlaveOutletConfig": ipduSlaveOutletConfig,
       "ipduSlaveDeviceOutletNameTable": ipduSlaveDeviceOutletNameTable,
       "ipduSlaveDeviceOutletNameEntry": ipduSlaveDeviceOutletNameEntry,
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
       "ipduSlaveDeviceOutletLocationTable": ipduSlaveDeviceOutletLocationTable,
       "ipduSlaveDeviceOutletLocationEntry": ipduSlaveDeviceOutletLocationEntry,
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
       "ipduSlaveDeviceOutletOnTimeTable": ipduSlaveDeviceOutletOnTimeTable,
       "ipduSlaveDeviceOutletOnTimeEntry": ipduSlaveDeviceOutletOnTimeEntry,
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
       "ipduSlaveDeviceOutletOffTimeTable": ipduSlaveDeviceOutletOffTimeTable,
       "ipduSlaveDeviceOutletOffTimeEntry": ipduSlaveDeviceOutletOffTimeEntry,
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
       "ipduSlaveDeviceOutletCurrThTable": ipduSlaveDeviceOutletCurrThTable,
       "ipduSlaveDeviceOutletCurrThEntry": ipduSlaveDeviceOutletCurrThEntry,
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
       "ipduSlaveOutletStatus": ipduSlaveOutletStatus,
       "ipduSlaveDeviceOutletCurrentTable": ipduSlaveDeviceOutletCurrentTable,
       "ipduSlaveDeviceOutletCurrentEntry": ipduSlaveDeviceOutletCurrentEntry,
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
       "ipduSlaveDeviceOutletWattTable": ipduSlaveDeviceOutletWattTable,
       "ipduSlaveDeviceOutletWattEntry": ipduSlaveDeviceOutletWattEntry,
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
       "ipduSlaveDeviceOutletKwattTable": ipduSlaveDeviceOutletKwattTable,
       "ipduSlaveDeviceOutletKwattEntry": ipduSlaveDeviceOutletKwattEntry,
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
       "ipduSlaveOutletAction": ipduSlaveOutletAction,
       "ipduSlaveDeviceOutletActionTable": ipduSlaveDeviceOutletActionTable,
       "ipduSlaveDeviceOutletActionEntry": ipduSlaveDeviceOutletActionEntry,
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
       "ipduEnv": ipduEnv,
       "ipduEnvEmd": ipduEnvEmd,
       "ipduEnvEmdStatus": ipduEnvEmdStatus,
       "ipduEnvEmdStatusEmdType": ipduEnvEmdStatusEmdType,
       "ipduEnvEmdStatusTemperature": ipduEnvEmdStatusTemperature,
       "ipduEnvEmdStatusHumidity": ipduEnvEmdStatusHumidity,
       "ipduEnvEmdStatusAlarm1": ipduEnvEmdStatusAlarm1,
       "ipduEnvEmdStatusAlarm2": ipduEnvEmdStatusAlarm2,
       "ipduEnvEmdConfig": ipduEnvEmdConfig,
       "ipduEnvEmdConfigEmdPresence": ipduEnvEmdConfigEmdPresence,
       "ipduEnvEmdConfigEmdName": ipduEnvEmdConfigEmdName,
       "ipduEnvEmdConfigTemp": ipduEnvEmdConfigTemp,
       "ipduEnvEmdConfigTempName": ipduEnvEmdConfigTempName,
       "ipduEnvEmdConfigTempHighSetPoint": ipduEnvEmdConfigTempHighSetPoint,
       "ipduEnvEmdConfigTempHighStatus": ipduEnvEmdConfigTempHighStatus,
       "ipduEnvEmdConfigTempLowSetPoint": ipduEnvEmdConfigTempLowSetPoint,
       "ipduEnvEmdConfigTempLowStatus": ipduEnvEmdConfigTempLowStatus,
       "ipduEnvEmdConfigTempOffset": ipduEnvEmdConfigTempOffset,
       "ipduEnvEmdConfigHumi": ipduEnvEmdConfigHumi,
       "ipduEnvEmdConfigHumiName": ipduEnvEmdConfigHumiName,
       "ipduEnvEmdConfigHumiHighSetPoint": ipduEnvEmdConfigHumiHighSetPoint,
       "ipduEnvEmdConfigHumiHighStatus": ipduEnvEmdConfigHumiHighStatus,
       "ipduEnvEmdConfigHumiLowSetPoint": ipduEnvEmdConfigHumiLowSetPoint,
       "ipduEnvEmdConfigHumiLowStatus": ipduEnvEmdConfigHumiLowStatus,
       "ipduEnvEmdConfigHumiOffset": ipduEnvEmdConfigHumiOffset,
       "ipduEnvEmdConfigAlarm1": ipduEnvEmdConfigAlarm1,
       "ipduEnvEmdConfigAlarm1Name": ipduEnvEmdConfigAlarm1Name,
       "ipduEnvEmdConfigAlarm1Type": ipduEnvEmdConfigAlarm1Type,
       "ipduEnvEmdConfigAlarm2": ipduEnvEmdConfigAlarm2,
       "ipduEnvEmdConfigAlarm2Name": ipduEnvEmdConfigAlarm2Name,
       "ipduEnvEmdConfigAlarm2Type": ipduEnvEmdConfigAlarm2Type,
       "ipduTraps": ipduTraps,
       "ipduInletVoltageTooHigh": ipduInletVoltageTooHigh,
       "ipduInletVoltageNotTooHigh": ipduInletVoltageNotTooHigh,
       "ipduInletVoltageTooLow": ipduInletVoltageTooLow,
       "ipduInletVoltageNotTooLow": ipduInletVoltageNotTooLow,
       "ipduInletCurrentTooHigh": ipduInletCurrentTooHigh,
       "ipduInletCurrentNotTooHigh": ipduInletCurrentNotTooHigh,
       "ipduInletFrequencyTooHigh": ipduInletFrequencyTooHigh,
       "ipduInletFrequencyNotTooHigh": ipduInletFrequencyNotTooHigh,
       "ipduInletFrequencyTooLow": ipduInletFrequencyTooLow,
       "ipduInletFrequencyNotTooLow": ipduInletFrequencyNotTooLow,
       "ipduInlet2VoltageTooHigh": ipduInlet2VoltageTooHigh,
       "ipduInlet2VoltageNotTooHigh": ipduInlet2VoltageNotTooHigh,
       "ipduInlet2VoltageTooLow": ipduInlet2VoltageTooLow,
       "ipduInlet2VoltageNotTooLow": ipduInlet2VoltageNotTooLow,
       "ipduInlet2CurrentTooHigh": ipduInlet2CurrentTooHigh,
       "ipduInlet2CurrentNotTooHigh": ipduInlet2CurrentNotTooHigh,
       "ipduInlet2FrequencyTooHigh": ipduInlet2FrequencyTooHigh,
       "ipduInlet2FrequencyNotTooHigh": ipduInlet2FrequencyNotTooHigh,
       "ipduInlet2FrequencyTooLow": ipduInlet2FrequencyTooLow,
       "ipduInlet2FrequencyNotTooLow": ipduInlet2FrequencyNotTooLow,
       "ipduOutletCurrentTooHigh": ipduOutletCurrentTooHigh,
       "ipduOutletCurrentNotTooHigh": ipduOutletCurrentNotTooHigh,
       "ipduOutletStateChanged": ipduOutletStateChanged,
       "ipduEmdTemperatureNotHigh": ipduEmdTemperatureNotHigh,
       "ipduEmdTemperatureTooHigh": ipduEmdTemperatureTooHigh,
       "ipduEmdTemperatureNotLow": ipduEmdTemperatureNotLow,
       "ipduEmdTemperatureTooLow": ipduEmdTemperatureTooLow,
       "ipduEmdHumidityNotHigh": ipduEmdHumidityNotHigh,
       "ipduEmdHumidityTooHigh": ipduEmdHumidityTooHigh,
       "ipduEmdHumidityNotLow": ipduEmdHumidityNotLow,
       "ipduEmdHumidityTooLow": ipduEmdHumidityTooLow,
       "ipduEmdAlarm1Normal": ipduEmdAlarm1Normal,
       "ipduEmdAlarm1Active": ipduEmdAlarm1Active,
       "ipduEmdAlarm2Normal": ipduEmdAlarm2Normal,
       "ipduEmdAlarm2Active": ipduEmdAlarm2Active,
       "ipduSlave01Inlet01OverHigh": ipduSlave01Inlet01OverHigh,
       "ipduSlave01Inlet01NotOverHigh": ipduSlave01Inlet01NotOverHigh,
       "ipduSlave01Inlet02OverHigh": ipduSlave01Inlet02OverHigh,
       "ipduSlave01Inlet02NotOverHigh": ipduSlave01Inlet02NotOverHigh,
       "ipduSlave01Inlet01UnderLow": ipduSlave01Inlet01UnderLow,
       "ipduSlave01Inlet01NotUnderLow": ipduSlave01Inlet01NotUnderLow,
       "ipduSlave01Inlet02UnderLow": ipduSlave01Inlet02UnderLow,
       "ipduSlave01Inlet02NotUnderLow": ipduSlave01Inlet02NotUnderLow,
       "ipduSlave01Inlet01CurrentOverTh": ipduSlave01Inlet01CurrentOverTh,
       "ipduSlave01Inlet01NotCurrentOverTh": ipduSlave01Inlet01NotCurrentOverTh,
       "ipduSlave01Inlet02CurrentOverTh": ipduSlave01Inlet02CurrentOverTh,
       "ipduSlave01Inlet02NotCurrentOverTh": ipduSlave01Inlet02NotCurrentOverTh,
       "ipduSlave01EmdTemperatureNotHigh": ipduSlave01EmdTemperatureNotHigh,
       "ipduSlave01EmdTemperatureTooHigh": ipduSlave01EmdTemperatureTooHigh,
       "ipduSlave01EmdTemperatureNotLow": ipduSlave01EmdTemperatureNotLow,
       "ipduSlave01EmdTemperatureTooLow": ipduSlave01EmdTemperatureTooLow,
       "ipduSlave01EmdHumidityNotHigh": ipduSlave01EmdHumidityNotHigh,
       "ipduSlave01EmdHumidityTooHigh": ipduSlave01EmdHumidityTooHigh,
       "ipduSlave01EmdHumidityNotLow": ipduSlave01EmdHumidityNotLow,
       "ipduSlave01EmdHumidityTooLow": ipduSlave01EmdHumidityTooLow,
       "ipduSlave01EmdAlarm1Normal": ipduSlave01EmdAlarm1Normal,
       "ipduSlave01EmdAlarm1Active": ipduSlave01EmdAlarm1Active,
       "ipduSlave01EmdAlarm2Normal": ipduSlave01EmdAlarm2Normal,
       "ipduSlave01EmdAlarm2Active": ipduSlave01EmdAlarm2Active,
       "ipduSlave01OutletCurrentOverTh": ipduSlave01OutletCurrentOverTh,
       "ipduSlave02Inlet01OverHigh": ipduSlave02Inlet01OverHigh,
       "ipduSlave02Inlet01NotOverHigh": ipduSlave02Inlet01NotOverHigh,
       "ipduSlave02Inlet02OverHigh": ipduSlave02Inlet02OverHigh,
       "ipduSlave02Inlet02NotOverHigh": ipduSlave02Inlet02NotOverHigh,
       "ipduSlave02Inlet01UnderLow": ipduSlave02Inlet01UnderLow,
       "ipduSlave02Inlet01NotUnderLow": ipduSlave02Inlet01NotUnderLow,
       "ipduSlave02Inlet02UnderLow": ipduSlave02Inlet02UnderLow,
       "ipduSlave02Inlet02NotUnderLow": ipduSlave02Inlet02NotUnderLow,
       "ipduSlave02Inlet01CurrentOverTh": ipduSlave02Inlet01CurrentOverTh,
       "ipduSlave02Inlet01NotCurrentOverTh": ipduSlave02Inlet01NotCurrentOverTh,
       "ipduSlave02Inlet02CurrentOverTh": ipduSlave02Inlet02CurrentOverTh,
       "ipduSlave02Inlet02NotCurrentOverTh": ipduSlave02Inlet02NotCurrentOverTh,
       "ipduSlave02EmdTemperatureNotHigh": ipduSlave02EmdTemperatureNotHigh,
       "ipduSlave02EmdTemperatureTooHigh": ipduSlave02EmdTemperatureTooHigh,
       "ipduSlave02EmdTemperatureNotLow": ipduSlave02EmdTemperatureNotLow,
       "ipduSlave02EmdTemperatureTooLow": ipduSlave02EmdTemperatureTooLow,
       "ipduSlave02EmdHumidityNotHigh": ipduSlave02EmdHumidityNotHigh,
       "ipduSlave02EmdHumidityTooHigh": ipduSlave02EmdHumidityTooHigh,
       "ipduSlave02EmdHumidityNotLow": ipduSlave02EmdHumidityNotLow,
       "ipduSlave02EmdHumidityTooLow": ipduSlave02EmdHumidityTooLow,
       "ipduSlave02EmdAlarm1Normal": ipduSlave02EmdAlarm1Normal,
       "ipduSlave02EmdAlarm1Active": ipduSlave02EmdAlarm1Active,
       "ipduSlave02EmdAlarm2Normal": ipduSlave02EmdAlarm2Normal,
       "ipduSlave02EmdAlarm2Active": ipduSlave02EmdAlarm2Active,
       "ipduSlave02OutletCurrentOverTh": ipduSlave02OutletCurrentOverTh,
       "ipduSlave03Inlet01OverHigh": ipduSlave03Inlet01OverHigh,
       "ipduSlave03Inlet01NotOverHigh": ipduSlave03Inlet01NotOverHigh,
       "ipduSlave03Inlet02OverHigh": ipduSlave03Inlet02OverHigh,
       "ipduSlave03Inlet02NotOverHigh": ipduSlave03Inlet02NotOverHigh,
       "ipduSlave03Inlet01UnderLow": ipduSlave03Inlet01UnderLow,
       "ipduSlave03Inlet01NotUnderLow": ipduSlave03Inlet01NotUnderLow,
       "ipduSlave03Inlet02UnderLow": ipduSlave03Inlet02UnderLow,
       "ipduSlave03Inlet02NotUnderLow": ipduSlave03Inlet02NotUnderLow,
       "ipduSlave03Inlet01CurrentOverTh": ipduSlave03Inlet01CurrentOverTh,
       "ipduSlave03Inlet01NotCurrentOverTh": ipduSlave03Inlet01NotCurrentOverTh,
       "ipduSlave03Inlet02CurrentOverTh": ipduSlave03Inlet02CurrentOverTh,
       "ipduSlave03Inlet02NotCurrentOverTh": ipduSlave03Inlet02NotCurrentOverTh,
       "ipduSlave03EmdTemperatureNotHigh": ipduSlave03EmdTemperatureNotHigh,
       "ipduSlave03EmdTemperatureTooHigh": ipduSlave03EmdTemperatureTooHigh,
       "ipduSlave03EmdTemperatureNotLow": ipduSlave03EmdTemperatureNotLow,
       "ipduSlave03EmdTemperatureTooLow": ipduSlave03EmdTemperatureTooLow,
       "ipduSlave03EmdHumidityNotHigh": ipduSlave03EmdHumidityNotHigh,
       "ipduSlave03EmdHumidityTooHigh": ipduSlave03EmdHumidityTooHigh,
       "ipduSlave03EmdHumidityNotLow": ipduSlave03EmdHumidityNotLow,
       "ipduSlave03EmdHumidityTooLow": ipduSlave03EmdHumidityTooLow,
       "ipduSlave03EmdAlarm1Normal": ipduSlave03EmdAlarm1Normal,
       "ipduSlave03EmdAlarm1Active": ipduSlave03EmdAlarm1Active,
       "ipduSlave03EmdAlarm2Normal": ipduSlave03EmdAlarm2Normal,
       "ipduSlave03EmdAlarm2Active": ipduSlave03EmdAlarm2Active,
       "ipduSlave03OutletCurrentOverTh": ipduSlave03OutletCurrentOverTh,
       "ipduSlave04Inlet01OverHigh": ipduSlave04Inlet01OverHigh,
       "ipduSlave04Inlet01NotOverHigh": ipduSlave04Inlet01NotOverHigh,
       "ipduSlave04Inlet02OverHigh": ipduSlave04Inlet02OverHigh,
       "ipduSlave04Inlet02NotOverHigh": ipduSlave04Inlet02NotOverHigh,
       "ipduSlave04Inlet01UnderLow": ipduSlave04Inlet01UnderLow,
       "ipduSlave04Inlet01NotUnderLow": ipduSlave04Inlet01NotUnderLow,
       "ipduSlave04Inlet02UnderLow": ipduSlave04Inlet02UnderLow,
       "ipduSlave04Inlet02NotUnderLow": ipduSlave04Inlet02NotUnderLow,
       "ipduSlave04Inlet01CurrentOverTh": ipduSlave04Inlet01CurrentOverTh,
       "ipduSlave04Inlet01NotCurrentOverTh": ipduSlave04Inlet01NotCurrentOverTh,
       "ipduSlave04Inlet02CurrentOverTh": ipduSlave04Inlet02CurrentOverTh,
       "ipduSlave04Inlet02NotCurrentOverTh": ipduSlave04Inlet02NotCurrentOverTh,
       "ipduSlave04EmdTemperatureNotHigh": ipduSlave04EmdTemperatureNotHigh,
       "ipduSlave04EmdTemperatureTooHigh": ipduSlave04EmdTemperatureTooHigh,
       "ipduSlave04EmdTemperatureNotLow": ipduSlave04EmdTemperatureNotLow,
       "ipduSlave04EmdTemperatureTooLow": ipduSlave04EmdTemperatureTooLow,
       "ipduSlave04EmdHumidityNotHigh": ipduSlave04EmdHumidityNotHigh,
       "ipduSlave04EmdHumidityTooHigh": ipduSlave04EmdHumidityTooHigh,
       "ipduSlave04EmdHumidityNotLow": ipduSlave04EmdHumidityNotLow,
       "ipduSlave04EmdHumidityTooLow": ipduSlave04EmdHumidityTooLow,
       "ipduSlave04EmdAlarm1Normal": ipduSlave04EmdAlarm1Normal,
       "ipduSlave04EmdAlarm1Active": ipduSlave04EmdAlarm1Active,
       "ipduSlave04EmdAlarm2Normal": ipduSlave04EmdAlarm2Normal,
       "ipduSlave04EmdAlarm2Active": ipduSlave04EmdAlarm2Active,
       "ipduSlave04OutletCurrentOverTh": ipduSlave04OutletCurrentOverTh,
       "ipduSlave05Inlet01OverHigh": ipduSlave05Inlet01OverHigh,
       "ipduSlave05Inlet01NotOverHigh": ipduSlave05Inlet01NotOverHigh,
       "ipduSlave05Inlet02OverHigh": ipduSlave05Inlet02OverHigh,
       "ipduSlave05Inlet02NotOverHigh": ipduSlave05Inlet02NotOverHigh,
       "ipduSlave05Inlet01UnderLow": ipduSlave05Inlet01UnderLow,
       "ipduSlave05Inlet01NotUnderLow": ipduSlave05Inlet01NotUnderLow,
       "ipduSlave05Inlet02UnderLow": ipduSlave05Inlet02UnderLow,
       "ipduSlave05Inlet02NotUnderLow": ipduSlave05Inlet02NotUnderLow,
       "ipduSlave05Inlet01CurrentOverTh": ipduSlave05Inlet01CurrentOverTh,
       "ipduSlave05Inlet01NotCurrentOverTh": ipduSlave05Inlet01NotCurrentOverTh,
       "ipduSlave05Inlet02CurrentOverTh": ipduSlave05Inlet02CurrentOverTh,
       "ipduSlave05Inlet02NotCurrentOverTh": ipduSlave05Inlet02NotCurrentOverTh,
       "ipduSlave05EmdTemperatureNotHigh": ipduSlave05EmdTemperatureNotHigh,
       "ipduSlave05EmdTemperatureTooHigh": ipduSlave05EmdTemperatureTooHigh,
       "ipduSlave05EmdTemperatureNotLow": ipduSlave05EmdTemperatureNotLow,
       "ipduSlave05EmdTemperatureTooLow": ipduSlave05EmdTemperatureTooLow,
       "ipduSlave05EmdHumidityNotHigh": ipduSlave05EmdHumidityNotHigh,
       "ipduSlave05EmdHumidityTooHigh": ipduSlave05EmdHumidityTooHigh,
       "ipduSlave05EmdHumidityNotLow": ipduSlave05EmdHumidityNotLow,
       "ipduSlave05EmdHumidityTooLow": ipduSlave05EmdHumidityTooLow,
       "ipduSlave05EmdAlarm1Normal": ipduSlave05EmdAlarm1Normal,
       "ipduSlave05EmdAlarm1Active": ipduSlave05EmdAlarm1Active,
       "ipduSlave05EmdAlarm2Normal": ipduSlave05EmdAlarm2Normal,
       "ipduSlave05EmdAlarm2Active": ipduSlave05EmdAlarm2Active,
       "ipduSlave05OutletCurrentOverTh": ipduSlave05OutletCurrentOverTh}
)
