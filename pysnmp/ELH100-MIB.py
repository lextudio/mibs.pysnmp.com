# SNMP MIB module (ELH100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELH100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:53 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_CabletronOEM_ObjectIdentity = ObjectIdentity
cabletronOEM = _CabletronOEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259)
)
_CabletronRepeaters_ObjectIdentity = ObjectIdentity
cabletronRepeaters = _CabletronRepeaters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10)
)
_CabletronELH100_ObjectIdentity = ObjectIdentity
cabletronELH100 = _CabletronELH100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3)
)
_CabletronELH100Common_ObjectIdentity = ObjectIdentity
cabletronELH100Common = _CabletronELH100Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1)
)
_Elh100System_ObjectIdentity = ObjectIdentity
elh100System = _Elh100System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1)
)
_Elh100MajorVer_Type = Integer32
_Elh100MajorVer_Object = MibScalar
elh100MajorVer = _Elh100MajorVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1, 1),
    _Elh100MajorVer_Type()
)
elh100MajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elh100MajorVer.setStatus("mandatory")
_Elh100MinorVer_Type = Integer32
_Elh100MinorVer_Object = MibScalar
elh100MinorVer = _Elh100MinorVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1, 2),
    _Elh100MinorVer_Type()
)
elh100MinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elh100MinorVer.setStatus("mandatory")
_Elh100HardwareVer_Type = Integer32
_Elh100HardwareVer_Object = MibScalar
elh100HardwareVer = _Elh100HardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1, 3),
    _Elh100HardwareVer_Type()
)
elh100HardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elh100HardwareVer.setStatus("mandatory")
_Elh100CommunityMgt_ObjectIdentity = ObjectIdentity
elh100CommunityMgt = _Elh100CommunityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2)
)
_Elh100CommunityTable_Object = MibTable
elh100CommunityTable = _Elh100CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    elh100CommunityTable.setStatus("mandatory")
_Elh100CommunityEntry_Object = MibTableRow
elh100CommunityEntry = _Elh100CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1)
)
elh100CommunityEntry.setIndexNames(
    (0, "ELH100-MIB", "elh100CommunityIndex"),
)
if mibBuilder.loadTexts:
    elh100CommunityEntry.setStatus("mandatory")
_Elh100CommunityIndex_Type = Integer32
_Elh100CommunityIndex_Object = MibTableColumn
elh100CommunityIndex = _Elh100CommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 1),
    _Elh100CommunityIndex_Type()
)
elh100CommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elh100CommunityIndex.setStatus("mandatory")


class _Elh100CommunityRowCreation_Type(Integer32):
    """Custom type elh100CommunityRowCreation based on Integer32"""
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


_Elh100CommunityRowCreation_Type.__name__ = "Integer32"
_Elh100CommunityRowCreation_Object = MibTableColumn
elh100CommunityRowCreation = _Elh100CommunityRowCreation_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 2),
    _Elh100CommunityRowCreation_Type()
)
elh100CommunityRowCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100CommunityRowCreation.setStatus("mandatory")


class _Elh100CommunityString_Type(DisplayString):
    """Custom type elh100CommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Elh100CommunityString_Type.__name__ = "DisplayString"
_Elh100CommunityString_Object = MibTableColumn
elh100CommunityString = _Elh100CommunityString_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 3),
    _Elh100CommunityString_Type()
)
elh100CommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100CommunityString.setStatus("mandatory")


class _Elh100CommunityStatus_Type(Integer32):
    """Custom type elh100CommunityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )


_Elh100CommunityStatus_Type.__name__ = "Integer32"
_Elh100CommunityStatus_Object = MibTableColumn
elh100CommunityStatus = _Elh100CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 4),
    _Elh100CommunityStatus_Type()
)
elh100CommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100CommunityStatus.setStatus("mandatory")
_Elh100TrapManagerMgt_ObjectIdentity = ObjectIdentity
elh100TrapManagerMgt = _Elh100TrapManagerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3)
)
_Elh100TrapManagerTable_Object = MibTable
elh100TrapManagerTable = _Elh100TrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    elh100TrapManagerTable.setStatus("mandatory")
_Elh100TrapMgtEntry_Object = MibTableRow
elh100TrapMgtEntry = _Elh100TrapMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1)
)
elh100TrapMgtEntry.setIndexNames(
    (0, "ELH100-MIB", "elh100TrapMgtIndex"),
)
if mibBuilder.loadTexts:
    elh100TrapMgtEntry.setStatus("mandatory")
_Elh100TrapMgtIndex_Type = Integer32
_Elh100TrapMgtIndex_Object = MibTableColumn
elh100TrapMgtIndex = _Elh100TrapMgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 1),
    _Elh100TrapMgtIndex_Type()
)
elh100TrapMgtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elh100TrapMgtIndex.setStatus("mandatory")


class _Elh100TrapMgtRowCreation_Type(Integer32):
    """Custom type elh100TrapMgtRowCreation based on Integer32"""
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


_Elh100TrapMgtRowCreation_Type.__name__ = "Integer32"
_Elh100TrapMgtRowCreation_Object = MibTableColumn
elh100TrapMgtRowCreation = _Elh100TrapMgtRowCreation_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 2),
    _Elh100TrapMgtRowCreation_Type()
)
elh100TrapMgtRowCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100TrapMgtRowCreation.setStatus("mandatory")


class _Elh100TrapMgtCommunityString_Type(DisplayString):
    """Custom type elh100TrapMgtCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Elh100TrapMgtCommunityString_Type.__name__ = "DisplayString"
_Elh100TrapMgtCommunityString_Object = MibTableColumn
elh100TrapMgtCommunityString = _Elh100TrapMgtCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 3),
    _Elh100TrapMgtCommunityString_Type()
)
elh100TrapMgtCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100TrapMgtCommunityString.setStatus("mandatory")
_Elh100TrapMgtIpAddress_Type = IpAddress
_Elh100TrapMgtIpAddress_Object = MibTableColumn
elh100TrapMgtIpAddress = _Elh100TrapMgtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 4),
    _Elh100TrapMgtIpAddress_Type()
)
elh100TrapMgtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100TrapMgtIpAddress.setStatus("mandatory")
_Elh100DownloadMgt_ObjectIdentity = ObjectIdentity
elh100DownloadMgt = _Elh100DownloadMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4)
)
_Elh100DownloadServerIP_Type = IpAddress
_Elh100DownloadServerIP_Object = MibScalar
elh100DownloadServerIP = _Elh100DownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 1),
    _Elh100DownloadServerIP_Type()
)
elh100DownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100DownloadServerIP.setStatus("mandatory")
_Elh100DownloadFilename_Type = OctetString
_Elh100DownloadFilename_Object = MibScalar
elh100DownloadFilename = _Elh100DownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 2),
    _Elh100DownloadFilename_Type()
)
elh100DownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100DownloadFilename.setStatus("mandatory")


class _Elh100DownloadMode_Type(Integer32):
    """Custom type elh100DownloadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("temporary", 2))
    )


_Elh100DownloadMode_Type.__name__ = "Integer32"
_Elh100DownloadMode_Object = MibScalar
elh100DownloadMode = _Elh100DownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 3),
    _Elh100DownloadMode_Type()
)
elh100DownloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100DownloadMode.setStatus("mandatory")


class _Elh100DownloadAction_Type(Integer32):
    """Custom type elh100DownloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRun", 2),
          ("run", 1))
    )


_Elh100DownloadAction_Type.__name__ = "Integer32"
_Elh100DownloadAction_Object = MibScalar
elh100DownloadAction = _Elh100DownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 4),
    _Elh100DownloadAction_Type()
)
elh100DownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100DownloadAction.setStatus("mandatory")
_Elh100Restart_Type = Integer32
_Elh100Restart_Object = MibScalar
elh100Restart = _Elh100Restart_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 5),
    _Elh100Restart_Type()
)
elh100Restart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elh100Restart.setStatus("mandatory")
_CabletronELH100BasicCapability_ObjectIdentity = ObjectIdentity
cabletronELH100BasicCapability = _CabletronELH100BasicCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2)
)
_CabletronELH100StackInfo_ObjectIdentity = ObjectIdentity
cabletronELH100StackInfo = _CabletronELH100StackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1)
)
_StackInusedIP_Type = IpAddress
_StackInusedIP_Object = MibScalar
stackInusedIP = _StackInusedIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 1),
    _StackInusedIP_Type()
)
stackInusedIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedIP.setStatus("mandatory")
_StackInusedNetMask_Type = IpAddress
_StackInusedNetMask_Object = MibScalar
stackInusedNetMask = _StackInusedNetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 2),
    _StackInusedNetMask_Type()
)
stackInusedNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedNetMask.setStatus("mandatory")
_StackInusedGateway_Type = IpAddress
_StackInusedGateway_Object = MibScalar
stackInusedGateway = _StackInusedGateway_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 3),
    _StackInusedGateway_Type()
)
stackInusedGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInusedGateway.setStatus("mandatory")
_StackBootpIP_Type = IpAddress
_StackBootpIP_Object = MibScalar
stackBootpIP = _StackBootpIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 4),
    _StackBootpIP_Type()
)
stackBootpIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackBootpIP.setStatus("mandatory")
_StackTemporalIP_Type = IpAddress
_StackTemporalIP_Object = MibScalar
stackTemporalIP = _StackTemporalIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 5),
    _StackTemporalIP_Type()
)
stackTemporalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalIP.setStatus("mandatory")
_StackTemporalNetMask_Type = IpAddress
_StackTemporalNetMask_Object = MibScalar
stackTemporalNetMask = _StackTemporalNetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 6),
    _StackTemporalNetMask_Type()
)
stackTemporalNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalNetMask.setStatus("mandatory")
_StackTemporalGateway_Type = IpAddress
_StackTemporalGateway_Object = MibScalar
stackTemporalGateway = _StackTemporalGateway_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 7),
    _StackTemporalGateway_Type()
)
stackTemporalGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackTemporalGateway.setStatus("mandatory")


class _StackBootpEnable_Type(Integer32):
    """Custom type stackBootpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-bootp", 1),
          ("enable-bootp", 2))
    )


_StackBootpEnable_Type.__name__ = "Integer32"
_StackBootpEnable_Object = MibScalar
stackBootpEnable = _StackBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 8),
    _StackBootpEnable_Type()
)
stackBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackBootpEnable.setStatus("mandatory")


class _IpInformationReset_Type(Integer32):
    """Custom type ipInformationReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_IpInformationReset_Type.__name__ = "Integer32"
_IpInformationReset_Object = MibScalar
ipInformationReset = _IpInformationReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 9),
    _IpInformationReset_Type()
)
ipInformationReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInformationReset.setStatus("mandatory")


class _StackHealthMonitor_Type(OctetString):
    """Custom type stackHealthMonitor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_StackHealthMonitor_Type.__name__ = "OctetString"
_StackHealthMonitor_Object = MibScalar
stackHealthMonitor = _StackHealthMonitor_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 10),
    _StackHealthMonitor_Type()
)
stackHealthMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackHealthMonitor.setStatus("mandatory")
_CabletronELH100AgentInfo_ObjectIdentity = ObjectIdentity
cabletronELH100AgentInfo = _CabletronELH100AgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2)
)
_NicAttachSegment_Type = Integer32
_NicAttachSegment_Object = MibScalar
nicAttachSegment = _NicAttachSegment_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 1),
    _NicAttachSegment_Type()
)
nicAttachSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicAttachSegment.setStatus("mandatory")
_SerialNumberTable_Object = MibTable
serialNumberTable = _SerialNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    serialNumberTable.setStatus("mandatory")
_SerialNumberEntry_Object = MibTableRow
serialNumberEntry = _SerialNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1)
)
serialNumberEntry.setIndexNames(
    (0, "ELH100-MIB", "sNIndex"),
)
if mibBuilder.loadTexts:
    serialNumberEntry.setStatus("mandatory")


class _SNIndex_Type(Integer32):
    """Custom type sNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SNIndex_Type.__name__ = "Integer32"
_SNIndex_Object = MibTableColumn
sNIndex = _SNIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1, 1),
    _SNIndex_Type()
)
sNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNIndex.setStatus("mandatory")


class _SerialNumber_Type(OctetString):
    """Custom type serialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SerialNumber_Type.__name__ = "OctetString"
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_SNCurrentUnitID_Type = Integer32
_SNCurrentUnitID_Object = MibTableColumn
sNCurrentUnitID = _SNCurrentUnitID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1, 3),
    _SNCurrentUnitID_Type()
)
sNCurrentUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNCurrentUnitID.setStatus("mandatory")


class _TelnetMaxSessions_Type(Integer32):
    """Custom type telnetMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TelnetMaxSessions_Type.__name__ = "Integer32"
_TelnetMaxSessions_Object = MibScalar
telnetMaxSessions = _TelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 3),
    _TelnetMaxSessions_Type()
)
telnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetMaxSessions.setStatus("mandatory")


class _TelnetAutoLogoutEnable_Type(Integer32):
    """Custom type telnetAutoLogoutEnable based on Integer32"""
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


_TelnetAutoLogoutEnable_Type.__name__ = "Integer32"
_TelnetAutoLogoutEnable_Object = MibScalar
telnetAutoLogoutEnable = _TelnetAutoLogoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 4),
    _TelnetAutoLogoutEnable_Type()
)
telnetAutoLogoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetAutoLogoutEnable.setStatus("mandatory")


class _TelnetAutoLogoutTimeout_Type(Integer32):
    """Custom type telnetAutoLogoutTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TelnetAutoLogoutTimeout_Type.__name__ = "Integer32"
_TelnetAutoLogoutTimeout_Object = MibScalar
telnetAutoLogoutTimeout = _TelnetAutoLogoutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 5),
    _TelnetAutoLogoutTimeout_Type()
)
telnetAutoLogoutTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetAutoLogoutTimeout.setStatus("mandatory")


class _VT100RefreshInterval_Type(Integer32):
    """Custom type vT100RefreshInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              30,
              60,
              120,
              180,
              300)
        )
    )
    namedValues = NamedValues(
        *(("seconds120", 120),
          ("seconds180", 180),
          ("seconds30", 30),
          ("seconds300", 300),
          ("seconds5", 5),
          ("seconds60", 60))
    )


_VT100RefreshInterval_Type.__name__ = "Integer32"
_VT100RefreshInterval_Object = MibScalar
vT100RefreshInterval = _VT100RefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 6),
    _VT100RefreshInterval_Type()
)
vT100RefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vT100RefreshInterval.setStatus("mandatory")
_CabletronELH100gGroupInfo_ObjectIdentity = ObjectIdentity
cabletronELH100gGroupInfo = _CabletronELH100gGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3)
)
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("mandatory")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1)
)
groupEntry.setIndexNames(
    (0, "ELH100-MIB", "groupID"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("mandatory")


class _GroupID_Type(Integer32):
    """Custom type groupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_GroupID_Type.__name__ = "Integer32"
_GroupID_Object = MibTableColumn
groupID = _GroupID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 1),
    _GroupID_Type()
)
groupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupID.setStatus("mandatory")


class _GroupType_Type(Integer32):
    """Custom type groupType based on Integer32"""
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
        *(("elh100-12tx", 3),
          ("elh100-24tx", 4),
          ("notPresent", 1),
          ("unknown", 2))
    )


_GroupType_Type.__name__ = "Integer32"
_GroupType_Object = MibTableColumn
groupType = _GroupType_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 2),
    _GroupType_Type()
)
groupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupType.setStatus("mandatory")


class _GroupCounterReset_Type(Integer32):
    """Custom type groupCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_GroupCounterReset_Type.__name__ = "Integer32"
_GroupCounterReset_Object = MibTableColumn
groupCounterReset = _GroupCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 3),
    _GroupCounterReset_Type()
)
groupCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupCounterReset.setStatus("mandatory")


class _MgmtModuleStatus_Type(Integer32):
    """Custom type mgmtModuleStatus based on Integer32"""
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
          ("notPresent", 1),
          ("standby", 3))
    )


_MgmtModuleStatus_Type.__name__ = "Integer32"
_MgmtModuleStatus_Object = MibTableColumn
mgmtModuleStatus = _MgmtModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 4),
    _MgmtModuleStatus_Type()
)
mgmtModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtModuleStatus.setStatus("mandatory")


class _MgmtModuleDatabaseVersion_Type(OctetString):
    """Custom type mgmtModuleDatabaseVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_MgmtModuleDatabaseVersion_Type.__name__ = "OctetString"
_MgmtModuleDatabaseVersion_Object = MibTableColumn
mgmtModuleDatabaseVersion = _MgmtModuleDatabaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 5),
    _MgmtModuleDatabaseVersion_Type()
)
mgmtModuleDatabaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtModuleDatabaseVersion.setStatus("mandatory")


class _SwitchModuleType_Type(Integer32):
    """Custom type switchModuleType based on Integer32"""
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
        *(("internalSwitch10-100", 3),
          ("mediaFX-SC", 5),
          ("mediaFX-ST", 6),
          ("mediaTX-10-100", 4),
          ("notPresent", 1),
          ("switchMediaFX-SC", 8),
          ("switchMediaFX-ST", 9),
          ("switchMediaTX-10-100", 7),
          ("unknown", 2))
    )


_SwitchModuleType_Type.__name__ = "Integer32"
_SwitchModuleType_Object = MibTableColumn
switchModuleType = _SwitchModuleType_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 6),
    _SwitchModuleType_Type()
)
switchModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchModuleType.setStatus("mandatory")


class _SwitchModuleActive_Type(Integer32):
    """Custom type switchModuleActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2),
          ("notApplicable", 3))
    )


_SwitchModuleActive_Type.__name__ = "Integer32"
_SwitchModuleActive_Object = MibTableColumn
switchModuleActive = _SwitchModuleActive_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 7),
    _SwitchModuleActive_Type()
)
switchModuleActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchModuleActive.setStatus("mandatory")
_BackplaneTable_Object = MibTable
backplaneTable = _BackplaneTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    backplaneTable.setStatus("mandatory")
_BackplaneEntry_Object = MibTableRow
backplaneEntry = _BackplaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1)
)
backplaneEntry.setIndexNames(
    (0, "ELH100-MIB", "backplaneGroupID"),
    (0, "ELH100-MIB", "backplaneSegmentID"),
)
if mibBuilder.loadTexts:
    backplaneEntry.setStatus("mandatory")


class _BackplaneGroupID_Type(Integer32):
    """Custom type backplaneGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_BackplaneGroupID_Type.__name__ = "Integer32"
_BackplaneGroupID_Object = MibTableColumn
backplaneGroupID = _BackplaneGroupID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1, 1),
    _BackplaneGroupID_Type()
)
backplaneGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneGroupID.setStatus("mandatory")


class _BackplaneSegmentID_Type(Integer32):
    """Custom type backplaneSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredMbps", 100),
          ("tenMbps", 10))
    )


_BackplaneSegmentID_Type.__name__ = "Integer32"
_BackplaneSegmentID_Object = MibTableColumn
backplaneSegmentID = _BackplaneSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1, 2),
    _BackplaneSegmentID_Type()
)
backplaneSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSegmentID.setStatus("mandatory")


class _BackplaneIsolated_Type(Integer32):
    """Custom type backplaneIsolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("isolated", 1))
    )


_BackplaneIsolated_Type.__name__ = "Integer32"
_BackplaneIsolated_Object = MibTableColumn
backplaneIsolated = _BackplaneIsolated_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1, 3),
    _BackplaneIsolated_Type()
)
backplaneIsolated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backplaneIsolated.setStatus("mandatory")
_CabletronELH100PortInfo_ObjectIdentity = ObjectIdentity
cabletronELH100PortInfo = _CabletronELH100PortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1)
)
portEntry.setIndexNames(
    (0, "ELH100-MIB", "portGroupID"),
    (0, "ELH100-MIB", "portID"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")


class _PortGroupID_Type(Integer32):
    """Custom type portGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PortGroupID_Type.__name__ = "Integer32"
_PortGroupID_Object = MibTableColumn
portGroupID = _PortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 1),
    _PortGroupID_Type()
)
portGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGroupID.setStatus("mandatory")
_PortID_Type = Integer32
_PortID_Object = MibTableColumn
portID = _PortID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 2),
    _PortID_Type()
)
portID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portID.setStatus("mandatory")


class _PortLinkSpeed_Type(Integer32):
    """Custom type portLinkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("noLink", 1),
          ("oneHundredMbps", 100),
          ("tenMbps", 10))
    )


_PortLinkSpeed_Type.__name__ = "Integer32"
_PortLinkSpeed_Object = MibTableColumn
portLinkSpeed = _PortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 3),
    _PortLinkSpeed_Type()
)
portLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkSpeed.setStatus("mandatory")


class _PortSpeedConfig_Type(Integer32):
    """Custom type portSpeedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("oneHundredMbps", 100),
          ("tenMbps", 10))
    )


_PortSpeedConfig_Type.__name__ = "Integer32"
_PortSpeedConfig_Object = MibTableColumn
portSpeedConfig = _PortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 4),
    _PortSpeedConfig_Type()
)
portSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedConfig.setStatus("mandatory")
_CabletronELH100PerfMonCapability_ObjectIdentity = ObjectIdentity
cabletronELH100PerfMonCapability = _CabletronELH100PerfMonCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3)
)
_CabletronELH100PerfMonAgentInfo_ObjectIdentity = ObjectIdentity
cabletronELH100PerfMonAgentInfo = _CabletronELH100PerfMonAgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1)
)
_PerfMonAgentCRCErrors_Type = Counter32
_PerfMonAgentCRCErrors_Object = MibScalar
perfMonAgentCRCErrors = _PerfMonAgentCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 1),
    _PerfMonAgentCRCErrors_Type()
)
perfMonAgentCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfMonAgentCRCErrors.setStatus("mandatory")
_PerfMonAgentAlignmentErrors_Type = Counter32
_PerfMonAgentAlignmentErrors_Object = MibScalar
perfMonAgentAlignmentErrors = _PerfMonAgentAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 2),
    _PerfMonAgentAlignmentErrors_Type()
)
perfMonAgentAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfMonAgentAlignmentErrors.setStatus("mandatory")
_PerfMonAgentCollisions_Type = Counter32
_PerfMonAgentCollisions_Object = MibScalar
perfMonAgentCollisions = _PerfMonAgentCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 3),
    _PerfMonAgentCollisions_Type()
)
perfMonAgentCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfMonAgentCollisions.setStatus("mandatory")
_PerfMonAgentTotalPortIsolates_Type = Counter32
_PerfMonAgentTotalPortIsolates_Object = MibScalar
perfMonAgentTotalPortIsolates = _PerfMonAgentTotalPortIsolates_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 4),
    _PerfMonAgentTotalPortIsolates_Type()
)
perfMonAgentTotalPortIsolates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfMonAgentTotalPortIsolates.setStatus("mandatory")
_PerfMonAgentSymbolErrors_Type = Counter32
_PerfMonAgentSymbolErrors_Object = MibScalar
perfMonAgentSymbolErrors = _PerfMonAgentSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 5),
    _PerfMonAgentSymbolErrors_Type()
)
perfMonAgentSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfMonAgentSymbolErrors.setStatus("mandatory")
_CabletronELH100SwitchCapability_ObjectIdentity = ObjectIdentity
cabletronELH100SwitchCapability = _CabletronELH100SwitchCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4)
)
_CabletronELH100SwitchInfo_ObjectIdentity = ObjectIdentity
cabletronELH100SwitchInfo = _CabletronELH100SwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1)
)
_SwitchPortTable_Object = MibTable
switchPortTable = _SwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    switchPortTable.setStatus("mandatory")
_SwitchPortEntry_Object = MibTableRow
switchPortEntry = _SwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1)
)
switchPortEntry.setIndexNames(
    (0, "ELH100-MIB", "switchPortGroupID"),
    (0, "ELH100-MIB", "switchPortID"),
)
if mibBuilder.loadTexts:
    switchPortEntry.setStatus("mandatory")
_SwitchPortGroupID_Type = Integer32
_SwitchPortGroupID_Object = MibTableColumn
switchPortGroupID = _SwitchPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 1),
    _SwitchPortGroupID_Type()
)
switchPortGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortGroupID.setStatus("mandatory")


class _SwitchPortID_Type(Integer32):
    """Custom type switchPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwitchPortID_Type.__name__ = "Integer32"
_SwitchPortID_Object = MibTableColumn
switchPortID = _SwitchPortID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 2),
    _SwitchPortID_Type()
)
switchPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortID.setStatus("mandatory")


class _SwitchPortAdminStatus_Type(Integer32):
    """Custom type switchPortAdminStatus based on Integer32"""
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
          ("notApplicable", 3))
    )


_SwitchPortAdminStatus_Type.__name__ = "Integer32"
_SwitchPortAdminStatus_Object = MibTableColumn
switchPortAdminStatus = _SwitchPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 3),
    _SwitchPortAdminStatus_Type()
)
switchPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPortAdminStatus.setStatus("mandatory")


class _SwitchPortSpeed_Type(Integer32):
    """Custom type switchPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("noLink", 1),
          ("oneHundredMbps", 100),
          ("tenMbps", 10))
    )


_SwitchPortSpeed_Type.__name__ = "Integer32"
_SwitchPortSpeed_Object = MibTableColumn
switchPortSpeed = _SwitchPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 4),
    _SwitchPortSpeed_Type()
)
switchPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortSpeed.setStatus("mandatory")


class _SwitchPortDuplex_Type(Integer32):
    """Custom type switchPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1),
          ("notApplicable", 3))
    )


_SwitchPortDuplex_Type.__name__ = "Integer32"
_SwitchPortDuplex_Object = MibTableColumn
switchPortDuplex = _SwitchPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 5),
    _SwitchPortDuplex_Type()
)
switchPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortDuplex.setStatus("mandatory")


class _SwitchPortLink_Type(Integer32):
    """Custom type switchPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("noLink", 2))
    )


_SwitchPortLink_Type.__name__ = "Integer32"
_SwitchPortLink_Object = MibTableColumn
switchPortLink = _SwitchPortLink_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 6),
    _SwitchPortLink_Type()
)
switchPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortLink.setStatus("mandatory")
_CabletronELH100SwitchStatsInfo_ObjectIdentity = ObjectIdentity
cabletronELH100SwitchStatsInfo = _CabletronELH100SwitchStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2)
)
_SwitchPortStatsTable_Object = MibTable
switchPortStatsTable = _SwitchPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    switchPortStatsTable.setStatus("mandatory")
_SwitchPortStatsEntry_Object = MibTableRow
switchPortStatsEntry = _SwitchPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1)
)
switchPortStatsEntry.setIndexNames(
    (0, "ELH100-MIB", "switchPortStatsGroupID"),
    (0, "ELH100-MIB", "switchPortStatsID"),
)
if mibBuilder.loadTexts:
    switchPortStatsEntry.setStatus("mandatory")
_SwitchPortStatsGroupID_Type = Integer32
_SwitchPortStatsGroupID_Object = MibTableColumn
switchPortStatsGroupID = _SwitchPortStatsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 1),
    _SwitchPortStatsGroupID_Type()
)
switchPortStatsGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortStatsGroupID.setStatus("mandatory")


class _SwitchPortStatsID_Type(Integer32):
    """Custom type switchPortStatsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwitchPortStatsID_Type.__name__ = "Integer32"
_SwitchPortStatsID_Object = MibTableColumn
switchPortStatsID = _SwitchPortStatsID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 2),
    _SwitchPortStatsID_Type()
)
switchPortStatsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortStatsID.setStatus("mandatory")
_SwitchPortReadableFrames_Type = Counter32
_SwitchPortReadableFrames_Object = MibTableColumn
switchPortReadableFrames = _SwitchPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 3),
    _SwitchPortReadableFrames_Type()
)
switchPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortReadableFrames.setStatus("mandatory")
_SwitchPortReadableOctets_Type = Counter32
_SwitchPortReadableOctets_Object = MibTableColumn
switchPortReadableOctets = _SwitchPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 4),
    _SwitchPortReadableOctets_Type()
)
switchPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortReadableOctets.setStatus("mandatory")
_SwitchPortFCSErrors_Type = Counter32
_SwitchPortFCSErrors_Object = MibTableColumn
switchPortFCSErrors = _SwitchPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 5),
    _SwitchPortFCSErrors_Type()
)
switchPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortFCSErrors.setStatus("mandatory")
_SwitchPortAlignmentErrors_Type = Counter32
_SwitchPortAlignmentErrors_Object = MibTableColumn
switchPortAlignmentErrors = _SwitchPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 6),
    _SwitchPortAlignmentErrors_Type()
)
switchPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortAlignmentErrors.setStatus("mandatory")
_SwitchPortFramesTooLong_Type = Counter32
_SwitchPortFramesTooLong_Object = MibTableColumn
switchPortFramesTooLong = _SwitchPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 7),
    _SwitchPortFramesTooLong_Type()
)
switchPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortFramesTooLong.setStatus("mandatory")
_SwitchPortShortEvents_Type = Counter32
_SwitchPortShortEvents_Object = MibTableColumn
switchPortShortEvents = _SwitchPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 8),
    _SwitchPortShortEvents_Type()
)
switchPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortShortEvents.setStatus("mandatory")
_SwitchPortRunts_Type = Counter32
_SwitchPortRunts_Object = MibTableColumn
switchPortRunts = _SwitchPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 9),
    _SwitchPortRunts_Type()
)
switchPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortRunts.setStatus("mandatory")
_SwitchPortCollisions_Type = Counter32
_SwitchPortCollisions_Object = MibTableColumn
switchPortCollisions = _SwitchPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 10),
    _SwitchPortCollisions_Type()
)
switchPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortCollisions.setStatus("mandatory")
_SwitchPortLateEvents_Type = Counter32
_SwitchPortLateEvents_Object = MibTableColumn
switchPortLateEvents = _SwitchPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 11),
    _SwitchPortLateEvents_Type()
)
switchPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortLateEvents.setStatus("mandatory")
_SwitchPortVeryLongEvents_Type = Counter32
_SwitchPortVeryLongEvents_Object = MibTableColumn
switchPortVeryLongEvents = _SwitchPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 12),
    _SwitchPortVeryLongEvents_Type()
)
switchPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortVeryLongEvents.setStatus("mandatory")
_SwitchPortDataRateMismatches_Type = Counter32
_SwitchPortDataRateMismatches_Object = MibTableColumn
switchPortDataRateMismatches = _SwitchPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 13),
    _SwitchPortDataRateMismatches_Type()
)
switchPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortDataRateMismatches.setStatus("mandatory")
_SwitchPortAutoPartitions_Type = Counter32
_SwitchPortAutoPartitions_Object = MibTableColumn
switchPortAutoPartitions = _SwitchPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 14),
    _SwitchPortAutoPartitions_Type()
)
switchPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortAutoPartitions.setStatus("mandatory")
_SwitchPortBroadcastPackets_Type = Counter32
_SwitchPortBroadcastPackets_Object = MibTableColumn
switchPortBroadcastPackets = _SwitchPortBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 15),
    _SwitchPortBroadcastPackets_Type()
)
switchPortBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortBroadcastPackets.setStatus("mandatory")
_SwitchPortMulticastPackets_Type = Counter32
_SwitchPortMulticastPackets_Object = MibTableColumn
switchPortMulticastPackets = _SwitchPortMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 16),
    _SwitchPortMulticastPackets_Type()
)
switchPortMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortMulticastPackets.setStatus("mandatory")
_SwitchPortIsolates_Type = Counter32
_SwitchPortIsolates_Object = MibTableColumn
switchPortIsolates = _SwitchPortIsolates_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 17),
    _SwitchPortIsolates_Type()
)
switchPortIsolates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortIsolates.setStatus("mandatory")
_CabletronELH100BackupCapability_ObjectIdentity = ObjectIdentity
cabletronELH100BackupCapability = _CabletronELH100BackupCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5)
)
_CabletronELH100BackupInfo_ObjectIdentity = ObjectIdentity
cabletronELH100BackupInfo = _CabletronELH100BackupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1)
)
_BackupPortTable_Object = MibTable
backupPortTable = _BackupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    backupPortTable.setStatus("mandatory")
_BackupPortEntry_Object = MibTableRow
backupPortEntry = _BackupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1)
)
backupPortEntry.setIndexNames(
    (0, "ELH100-MIB", "backupIndex"),
)
if mibBuilder.loadTexts:
    backupPortEntry.setStatus("mandatory")


class _BackupIndex_Type(Integer32):
    """Custom type backupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_BackupIndex_Type.__name__ = "Integer32"
_BackupIndex_Object = MibTableColumn
backupIndex = _BackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 1),
    _BackupIndex_Type()
)
backupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupIndex.setStatus("mandatory")
_BackupPriPortGroup_Type = Integer32
_BackupPriPortGroup_Object = MibTableColumn
backupPriPortGroup = _BackupPriPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 2),
    _BackupPriPortGroup_Type()
)
backupPriPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupPriPortGroup.setStatus("mandatory")
_BackupPriPortPort_Type = Integer32
_BackupPriPortPort_Object = MibTableColumn
backupPriPortPort = _BackupPriPortPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 3),
    _BackupPriPortPort_Type()
)
backupPriPortPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupPriPortPort.setStatus("mandatory")
_BackupSecPortGroup_Type = Integer32
_BackupSecPortGroup_Object = MibTableColumn
backupSecPortGroup = _BackupSecPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 4),
    _BackupSecPortGroup_Type()
)
backupSecPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSecPortGroup.setStatus("mandatory")
_BackupSecPortPort_Type = Integer32
_BackupSecPortPort_Object = MibTableColumn
backupSecPortPort = _BackupSecPortPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 5),
    _BackupSecPortPort_Type()
)
backupSecPortPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSecPortPort.setStatus("mandatory")


class _BackupPortAction_Type(Integer32):
    """Custom type backupPortAction based on Integer32"""
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
        *(("active", 2),
          ("backup", 4),
          ("delete", 6),
          ("inactive", 1),
          ("invalid", 5),
          ("standby", 3))
    )


_BackupPortAction_Type.__name__ = "Integer32"
_BackupPortAction_Object = MibTableColumn
backupPortAction = _BackupPortAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 6),
    _BackupPortAction_Type()
)
backupPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupPortAction.setStatus("mandatory")
_CabletronELH100SecurityCapability_ObjectIdentity = ObjectIdentity
cabletronELH100SecurityCapability = _CabletronELH100SecurityCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6)
)
_CabletronELH100SecurityInfo_ObjectIdentity = ObjectIdentity
cabletronELH100SecurityInfo = _CabletronELH100SecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1)
)
_SecurityTable_Object = MibTable
securityTable = _SecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    securityTable.setStatus("mandatory")
_SecurityEntry_Object = MibTableRow
securityEntry = _SecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1)
)
securityEntry.setIndexNames(
    (0, "ELH100-MIB", "securityGroupID"),
    (0, "ELH100-MIB", "securityPortID"),
)
if mibBuilder.loadTexts:
    securityEntry.setStatus("mandatory")
_SecurityGroupID_Type = Integer32
_SecurityGroupID_Object = MibTableColumn
securityGroupID = _SecurityGroupID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 1),
    _SecurityGroupID_Type()
)
securityGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityGroupID.setStatus("mandatory")
_SecurityPortID_Type = Integer32
_SecurityPortID_Object = MibTableColumn
securityPortID = _SecurityPortID_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 2),
    _SecurityPortID_Type()
)
securityPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityPortID.setStatus("mandatory")
_SecurityAddr_Type = PhysAddress
_SecurityAddr_Object = MibTableColumn
securityAddr = _SecurityAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 3),
    _SecurityAddr_Type()
)
securityAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityAddr.setStatus("mandatory")


class _SecurityAutoLearnAction_Type(Integer32):
    """Custom type securityAutoLearnAction based on Integer32"""
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
          ("inactive", 1),
          ("learned", 3))
    )


_SecurityAutoLearnAction_Type.__name__ = "Integer32"
_SecurityAutoLearnAction_Object = MibTableColumn
securityAutoLearnAction = _SecurityAutoLearnAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 4),
    _SecurityAutoLearnAction_Type()
)
securityAutoLearnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityAutoLearnAction.setStatus("mandatory")


class _SecurityEnable_Type(Integer32):
    """Custom type securityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("warningAndDisable", 2))
    )


_SecurityEnable_Type.__name__ = "Integer32"
_SecurityEnable_Object = MibTableColumn
securityEnable = _SecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 5),
    _SecurityEnable_Type()
)
securityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELH100-MIB",
    **{"cabletron": cabletron,
       "cabletronOEM": cabletronOEM,
       "cabletronRepeaters": cabletronRepeaters,
       "cabletronELH100": cabletronELH100,
       "cabletronELH100Common": cabletronELH100Common,
       "elh100System": elh100System,
       "elh100MajorVer": elh100MajorVer,
       "elh100MinorVer": elh100MinorVer,
       "elh100HardwareVer": elh100HardwareVer,
       "elh100CommunityMgt": elh100CommunityMgt,
       "elh100CommunityTable": elh100CommunityTable,
       "elh100CommunityEntry": elh100CommunityEntry,
       "elh100CommunityIndex": elh100CommunityIndex,
       "elh100CommunityRowCreation": elh100CommunityRowCreation,
       "elh100CommunityString": elh100CommunityString,
       "elh100CommunityStatus": elh100CommunityStatus,
       "elh100TrapManagerMgt": elh100TrapManagerMgt,
       "elh100TrapManagerTable": elh100TrapManagerTable,
       "elh100TrapMgtEntry": elh100TrapMgtEntry,
       "elh100TrapMgtIndex": elh100TrapMgtIndex,
       "elh100TrapMgtRowCreation": elh100TrapMgtRowCreation,
       "elh100TrapMgtCommunityString": elh100TrapMgtCommunityString,
       "elh100TrapMgtIpAddress": elh100TrapMgtIpAddress,
       "elh100DownloadMgt": elh100DownloadMgt,
       "elh100DownloadServerIP": elh100DownloadServerIP,
       "elh100DownloadFilename": elh100DownloadFilename,
       "elh100DownloadMode": elh100DownloadMode,
       "elh100DownloadAction": elh100DownloadAction,
       "elh100Restart": elh100Restart,
       "cabletronELH100BasicCapability": cabletronELH100BasicCapability,
       "cabletronELH100StackInfo": cabletronELH100StackInfo,
       "stackInusedIP": stackInusedIP,
       "stackInusedNetMask": stackInusedNetMask,
       "stackInusedGateway": stackInusedGateway,
       "stackBootpIP": stackBootpIP,
       "stackTemporalIP": stackTemporalIP,
       "stackTemporalNetMask": stackTemporalNetMask,
       "stackTemporalGateway": stackTemporalGateway,
       "stackBootpEnable": stackBootpEnable,
       "ipInformationReset": ipInformationReset,
       "stackHealthMonitor": stackHealthMonitor,
       "cabletronELH100AgentInfo": cabletronELH100AgentInfo,
       "nicAttachSegment": nicAttachSegment,
       "serialNumberTable": serialNumberTable,
       "serialNumberEntry": serialNumberEntry,
       "sNIndex": sNIndex,
       "serialNumber": serialNumber,
       "sNCurrentUnitID": sNCurrentUnitID,
       "telnetMaxSessions": telnetMaxSessions,
       "telnetAutoLogoutEnable": telnetAutoLogoutEnable,
       "telnetAutoLogoutTimeout": telnetAutoLogoutTimeout,
       "vT100RefreshInterval": vT100RefreshInterval,
       "cabletronELH100gGroupInfo": cabletronELH100gGroupInfo,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupID": groupID,
       "groupType": groupType,
       "groupCounterReset": groupCounterReset,
       "mgmtModuleStatus": mgmtModuleStatus,
       "mgmtModuleDatabaseVersion": mgmtModuleDatabaseVersion,
       "switchModuleType": switchModuleType,
       "switchModuleActive": switchModuleActive,
       "backplaneTable": backplaneTable,
       "backplaneEntry": backplaneEntry,
       "backplaneGroupID": backplaneGroupID,
       "backplaneSegmentID": backplaneSegmentID,
       "backplaneIsolated": backplaneIsolated,
       "cabletronELH100PortInfo": cabletronELH100PortInfo,
       "portTable": portTable,
       "portEntry": portEntry,
       "portGroupID": portGroupID,
       "portID": portID,
       "portLinkSpeed": portLinkSpeed,
       "portSpeedConfig": portSpeedConfig,
       "cabletronELH100PerfMonCapability": cabletronELH100PerfMonCapability,
       "cabletronELH100PerfMonAgentInfo": cabletronELH100PerfMonAgentInfo,
       "perfMonAgentCRCErrors": perfMonAgentCRCErrors,
       "perfMonAgentAlignmentErrors": perfMonAgentAlignmentErrors,
       "perfMonAgentCollisions": perfMonAgentCollisions,
       "perfMonAgentTotalPortIsolates": perfMonAgentTotalPortIsolates,
       "perfMonAgentSymbolErrors": perfMonAgentSymbolErrors,
       "cabletronELH100SwitchCapability": cabletronELH100SwitchCapability,
       "cabletronELH100SwitchInfo": cabletronELH100SwitchInfo,
       "switchPortTable": switchPortTable,
       "switchPortEntry": switchPortEntry,
       "switchPortGroupID": switchPortGroupID,
       "switchPortID": switchPortID,
       "switchPortAdminStatus": switchPortAdminStatus,
       "switchPortSpeed": switchPortSpeed,
       "switchPortDuplex": switchPortDuplex,
       "switchPortLink": switchPortLink,
       "cabletronELH100SwitchStatsInfo": cabletronELH100SwitchStatsInfo,
       "switchPortStatsTable": switchPortStatsTable,
       "switchPortStatsEntry": switchPortStatsEntry,
       "switchPortStatsGroupID": switchPortStatsGroupID,
       "switchPortStatsID": switchPortStatsID,
       "switchPortReadableFrames": switchPortReadableFrames,
       "switchPortReadableOctets": switchPortReadableOctets,
       "switchPortFCSErrors": switchPortFCSErrors,
       "switchPortAlignmentErrors": switchPortAlignmentErrors,
       "switchPortFramesTooLong": switchPortFramesTooLong,
       "switchPortShortEvents": switchPortShortEvents,
       "switchPortRunts": switchPortRunts,
       "switchPortCollisions": switchPortCollisions,
       "switchPortLateEvents": switchPortLateEvents,
       "switchPortVeryLongEvents": switchPortVeryLongEvents,
       "switchPortDataRateMismatches": switchPortDataRateMismatches,
       "switchPortAutoPartitions": switchPortAutoPartitions,
       "switchPortBroadcastPackets": switchPortBroadcastPackets,
       "switchPortMulticastPackets": switchPortMulticastPackets,
       "switchPortIsolates": switchPortIsolates,
       "cabletronELH100BackupCapability": cabletronELH100BackupCapability,
       "cabletronELH100BackupInfo": cabletronELH100BackupInfo,
       "backupPortTable": backupPortTable,
       "backupPortEntry": backupPortEntry,
       "backupIndex": backupIndex,
       "backupPriPortGroup": backupPriPortGroup,
       "backupPriPortPort": backupPriPortPort,
       "backupSecPortGroup": backupSecPortGroup,
       "backupSecPortPort": backupSecPortPort,
       "backupPortAction": backupPortAction,
       "cabletronELH100SecurityCapability": cabletronELH100SecurityCapability,
       "cabletronELH100SecurityInfo": cabletronELH100SecurityInfo,
       "securityTable": securityTable,
       "securityEntry": securityEntry,
       "securityGroupID": securityGroupID,
       "securityPortID": securityPortID,
       "securityAddr": securityAddr,
       "securityAutoLearnAction": securityAutoLearnAction,
       "securityEnable": securityEnable}
)
