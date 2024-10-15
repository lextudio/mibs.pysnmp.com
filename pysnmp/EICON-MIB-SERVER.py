# SNMP MIB module (EICON-MIB-SERVER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-MIB-SERVER
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:47 2024
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OperState(Integer32):
    """Custom type OperState based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("disabled", 2),
          ("other", 1),
          ("ready", 3))
    )





class AdminState(Integer32):
    """Custom type AdminState based on Integer32"""
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
        *(("dump", 3),
          ("invalid", 5),
          ("start", 1),
          ("stop", 2),
          ("test", 4))
    )





class ActionState(Integer32):
    """Custom type ActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("failed", 2),
          ("in-progress", 3))
    )





class EiconCardType(Integer32):
    """Custom type EiconCardType based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("ect-MC-EC", 11),
          ("ect-MC-EC1M", 21),
          ("ect-MC-HSI", 12),
          ("ect-MC-HSI1M", 18),
          ("ect-MC-IMC", 14),
          ("ect-MC-ISDN", 33),
          ("ect-MC-MPNA", 16),
          ("ect-MC-MPNA2M", 30),
          ("ect-MC-SPCC", 5),
          ("ect-MC-SPCC2", 31),
          ("ect-NB-EC", 25),
          ("ect-NB-EC1M", 22),
          ("ect-NB-HSI1M", 19),
          ("ect-NB-IMC", 23),
          ("ect-NB-SPCC", 24),
          ("ect-NONE", 1),
          ("ect-PC-ACC8", 26),
          ("ect-PC-DNA", 3),
          ("ect-PC-DPNA", 6),
          ("ect-PC-DPNA2M", 28),
          ("ect-PC-EC", 7),
          ("ect-PC-EC1M", 20),
          ("ect-PC-ECHSI", 8),
          ("ect-PC-HSI1M", 17),
          ("ect-PC-HSI2", 35),
          ("ect-PC-IMC", 15),
          ("ect-PC-ISDN", 27),
          ("ect-PC-MPNA", 10),
          ("ect-PC-MPNA2M", 29),
          ("ect-PC-NA", 2),
          ("ect-PC-QPNA", 9),
          ("ect-PC-S51", 36),
          ("ect-PC-S52", 37),
          ("ect-PC-SPNA", 4),
          ("ect-PP-EC", 34),
          ("ect-PP-IMC", 32),
          ("ect-XX-DIGI", 13))
    )





class ControlOnOff(Integer32):
    """Custom type ControlOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("start", 2),
          ("stop", 1))
    )





class CardRef(Integer32):
    """Custom type CardRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class PortName(DisplayString):
    """Custom type PortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1)
)
_SrvAdminStateCtr_Type = AdminState
_SrvAdminStateCtr_Object = MibScalar
srvAdminStateCtr = _SrvAdminStateCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 1),
    _SrvAdminStateCtr_Type()
)
srvAdminStateCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvAdminStateCtr.setStatus("mandatory")


class _SrvOsName_Type(Integer32):
    """Custom type srvOsName based on Integer32"""
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
        *(("dos", 2),
          ("mac", 5),
          ("netware", 7),
          ("nt", 8),
          ("os2", 3),
          ("other", 1),
          ("unix", 4),
          ("windows", 6))
    )


_SrvOsName_Type.__name__ = "Integer32"
_SrvOsName_Object = MibScalar
srvOsName = _SrvOsName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 2),
    _SrvOsName_Type()
)
srvOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOsName.setStatus("mandatory")


class _SrvOsVersion_Type(DisplayString):
    """Custom type srvOsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvOsVersion_Type.__name__ = "DisplayString"
_SrvOsVersion_Object = MibScalar
srvOsVersion = _SrvOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 3),
    _SrvOsVersion_Type()
)
srvOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvOsVersion.setStatus("mandatory")


class _SrvNosName_Type(Integer32):
    """Custom type srvNosName based on Integer32"""
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
        *(("genericNetBIOS", 6),
          ("lanManager", 3),
          ("lanServer", 5),
          ("netWare", 2),
          ("other", 1),
          ("vines", 4))
    )


_SrvNosName_Type.__name__ = "Integer32"
_SrvNosName_Object = MibScalar
srvNosName = _SrvNosName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 4),
    _SrvNosName_Type()
)
srvNosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvNosName.setStatus("mandatory")


class _SrvNosVersion_Type(DisplayString):
    """Custom type srvNosVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvNosVersion_Type.__name__ = "DisplayString"
_SrvNosVersion_Object = MibScalar
srvNosVersion = _SrvNosVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 5),
    _SrvNosVersion_Type()
)
srvNosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvNosVersion.setStatus("mandatory")


class _SrvLanShellInfo_Type(DisplayString):
    """Custom type srvLanShellInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvLanShellInfo_Type.__name__ = "DisplayString"
_SrvLanShellInfo_Object = MibScalar
srvLanShellInfo = _SrvLanShellInfo_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 6),
    _SrvLanShellInfo_Type()
)
srvLanShellInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanShellInfo.setStatus("mandatory")


class _SrvBusType_Type(Integer32):
    """Custom type srvBusType based on Integer32"""
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
        *(("eisa", 3),
          ("isa", 2),
          ("mca", 4),
          ("other", 1),
          ("parallelPort", 5))
    )


_SrvBusType_Type.__name__ = "Integer32"
_SrvBusType_Object = MibScalar
srvBusType = _SrvBusType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 7),
    _SrvBusType_Type()
)
srvBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvBusType.setStatus("mandatory")


class _SrvCpuType_Type(DisplayString):
    """Custom type srvCpuType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvCpuType_Type.__name__ = "DisplayString"
_SrvCpuType_Object = MibScalar
srvCpuType = _SrvCpuType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 8),
    _SrvCpuType_Type()
)
srvCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCpuType.setStatus("mandatory")
_SrvCpuSpeed_Type = PositiveInteger
_SrvCpuSpeed_Object = MibScalar
srvCpuSpeed = _SrvCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 9),
    _SrvCpuSpeed_Type()
)
srvCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCpuSpeed.setStatus("mandatory")
_SrvStdMemory_Type = PositiveInteger
_SrvStdMemory_Object = MibScalar
srvStdMemory = _SrvStdMemory_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 10),
    _SrvStdMemory_Type()
)
srvStdMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvStdMemory.setStatus("mandatory")
_SrvExtendMemory_Type = PositiveInteger
_SrvExtendMemory_Object = MibScalar
srvExtendMemory = _SrvExtendMemory_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 11),
    _SrvExtendMemory_Type()
)
srvExtendMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvExtendMemory.setStatus("mandatory")
_SrvExpandedMemory_Type = PositiveInteger
_SrvExpandedMemory_Object = MibScalar
srvExpandedMemory = _SrvExpandedMemory_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 12),
    _SrvExpandedMemory_Type()
)
srvExpandedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvExpandedMemory.setStatus("mandatory")


class _SrvVideoAdaptType_Type(DisplayString):
    """Custom type srvVideoAdaptType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvVideoAdaptType_Type.__name__ = "DisplayString"
_SrvVideoAdaptType_Object = MibScalar
srvVideoAdaptType = _SrvVideoAdaptType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 13),
    _SrvVideoAdaptType_Type()
)
srvVideoAdaptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvVideoAdaptType.setStatus("mandatory")


class _SrvHardDisk_Type(DisplayString):
    """Custom type srvHardDisk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvHardDisk_Type.__name__ = "DisplayString"
_SrvHardDisk_Object = MibScalar
srvHardDisk = _SrvHardDisk_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 14),
    _SrvHardDisk_Type()
)
srvHardDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvHardDisk.setStatus("mandatory")
_SrvHardDiskSize_Type = Integer32
_SrvHardDiskSize_Object = MibScalar
srvHardDiskSize = _SrvHardDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 15),
    _SrvHardDiskSize_Type()
)
srvHardDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvHardDiskSize.setStatus("mandatory")


class _SrvNotePad_Type(DisplayString):
    """Custom type srvNotePad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SrvNotePad_Type.__name__ = "DisplayString"
_SrvNotePad_Object = MibScalar
srvNotePad = _SrvNotePad_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 16),
    _SrvNotePad_Type()
)
srvNotePad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvNotePad.setStatus("mandatory")


class _SrvAgentMajorVersion_Type(Integer32):
    """Custom type srvAgentMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SrvAgentMajorVersion_Type.__name__ = "Integer32"
_SrvAgentMajorVersion_Object = MibScalar
srvAgentMajorVersion = _SrvAgentMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 17),
    _SrvAgentMajorVersion_Type()
)
srvAgentMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvAgentMajorVersion.setStatus("mandatory")


class _SrvAgentMinorVersion_Type(Integer32):
    """Custom type srvAgentMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SrvAgentMinorVersion_Type.__name__ = "Integer32"
_SrvAgentMinorVersion_Object = MibScalar
srvAgentMinorVersion = _SrvAgentMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 18),
    _SrvAgentMinorVersion_Type()
)
srvAgentMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvAgentMinorVersion.setStatus("mandatory")
_SrvAgentMaxOfLostNMPHeartB_Type = Integer32
_SrvAgentMaxOfLostNMPHeartB_Object = MibScalar
srvAgentMaxOfLostNMPHeartB = _SrvAgentMaxOfLostNMPHeartB_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 19),
    _SrvAgentMaxOfLostNMPHeartB_Type()
)
srvAgentMaxOfLostNMPHeartB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvAgentMaxOfLostNMPHeartB.setStatus("mandatory")


class _SrvAgentHeartBeatPeriod_Type(Integer32):
    """Custom type srvAgentHeartBeatPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_SrvAgentHeartBeatPeriod_Type.__name__ = "Integer32"
_SrvAgentHeartBeatPeriod_Object = MibScalar
srvAgentHeartBeatPeriod = _SrvAgentHeartBeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 20),
    _SrvAgentHeartBeatPeriod_Type()
)
srvAgentHeartBeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvAgentHeartBeatPeriod.setStatus("mandatory")


class _SrvAgentPollFrequency_Type(Integer32):
    """Custom type srvAgentPollFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_SrvAgentPollFrequency_Type.__name__ = "Integer32"
_SrvAgentPollFrequency_Object = MibScalar
srvAgentPollFrequency = _SrvAgentPollFrequency_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 21),
    _SrvAgentPollFrequency_Type()
)
srvAgentPollFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvAgentPollFrequency.setStatus("mandatory")
_SrvAgentAlarmsFilterValue_Type = Integer32
_SrvAgentAlarmsFilterValue_Object = MibScalar
srvAgentAlarmsFilterValue = _SrvAgentAlarmsFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 22),
    _SrvAgentAlarmsFilterValue_Type()
)
srvAgentAlarmsFilterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvAgentAlarmsFilterValue.setStatus("mandatory")


class _SrvDomainName_Type(DisplayString):
    """Custom type srvDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SrvDomainName_Type.__name__ = "DisplayString"
_SrvDomainName_Object = MibScalar
srvDomainName = _SrvDomainName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 23),
    _SrvDomainName_Type()
)
srvDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvDomainName.setStatus("mandatory")


class _SrvDomainConfigDir_Type(DisplayString):
    """Custom type srvDomainConfigDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SrvDomainConfigDir_Type.__name__ = "DisplayString"
_SrvDomainConfigDir_Object = MibScalar
srvDomainConfigDir = _SrvDomainConfigDir_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 24),
    _SrvDomainConfigDir_Type()
)
srvDomainConfigDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvDomainConfigDir.setStatus("mandatory")
_SrvNbOfLanCards_Type = CardRef
_SrvNbOfLanCards_Object = MibScalar
srvNbOfLanCards = _SrvNbOfLanCards_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 25),
    _SrvNbOfLanCards_Type()
)
srvNbOfLanCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvNbOfLanCards.setStatus("mandatory")
_SrvLanCardTable_Object = MibTable
srvLanCardTable = _SrvLanCardTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26)
)
if mibBuilder.loadTexts:
    srvLanCardTable.setStatus("mandatory")
_SrvLanCardEntry_Object = MibTableRow
srvLanCardEntry = _SrvLanCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1)
)
srvLanCardEntry.setIndexNames(
    (0, "EICON-MIB-SERVER", "srvLanCardIndex"),
)
if mibBuilder.loadTexts:
    srvLanCardEntry.setStatus("mandatory")
_SrvLanCardIndex_Type = CardRef
_SrvLanCardIndex_Object = MibTableColumn
srvLanCardIndex = _SrvLanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 1),
    _SrvLanCardIndex_Type()
)
srvLanCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardIndex.setStatus("mandatory")
_SrvLanCardCFGMajorVer_Type = Integer32
_SrvLanCardCFGMajorVer_Object = MibTableColumn
srvLanCardCFGMajorVer = _SrvLanCardCFGMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 2),
    _SrvLanCardCFGMajorVer_Type()
)
srvLanCardCFGMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardCFGMajorVer.setStatus("mandatory")
_SrvLanCardCFGMinorVer_Type = Integer32
_SrvLanCardCFGMinorVer_Object = MibTableColumn
srvLanCardCFGMinorVer = _SrvLanCardCFGMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 3),
    _SrvLanCardCFGMinorVer_Type()
)
srvLanCardCFGMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardCFGMinorVer.setStatus("mandatory")


class _SrvLanCardNodeAddr_Type(DisplayString):
    """Custom type srvLanCardNodeAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SrvLanCardNodeAddr_Type.__name__ = "DisplayString"
_SrvLanCardNodeAddr_Object = MibTableColumn
srvLanCardNodeAddr = _SrvLanCardNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 4),
    _SrvLanCardNodeAddr_Type()
)
srvLanCardNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardNodeAddr.setStatus("mandatory")
_SrvLanCardMaxSize_Type = Integer32
_SrvLanCardMaxSize_Object = MibTableColumn
srvLanCardMaxSize = _SrvLanCardMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 5),
    _SrvLanCardMaxSize_Type()
)
srvLanCardMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardMaxSize.setStatus("mandatory")


class _SrvLanCardName_Type(DisplayString):
    """Custom type srvLanCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SrvLanCardName_Type.__name__ = "DisplayString"
_SrvLanCardName_Object = MibTableColumn
srvLanCardName = _SrvLanCardName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 6),
    _SrvLanCardName_Type()
)
srvLanCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardName.setStatus("mandatory")


class _SrvLanCardShortName_Type(DisplayString):
    """Custom type srvLanCardShortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SrvLanCardShortName_Type.__name__ = "DisplayString"
_SrvLanCardShortName_Object = MibTableColumn
srvLanCardShortName = _SrvLanCardShortName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 7),
    _SrvLanCardShortName_Type()
)
srvLanCardShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardShortName.setStatus("mandatory")


class _SrvLanCardFrameType_Type(DisplayString):
    """Custom type srvLanCardFrameType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SrvLanCardFrameType_Type.__name__ = "DisplayString"
_SrvLanCardFrameType_Object = MibTableColumn
srvLanCardFrameType = _SrvLanCardFrameType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 8),
    _SrvLanCardFrameType_Type()
)
srvLanCardFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardFrameType.setStatus("mandatory")
_SrvLanCardDrvMajorVer_Type = Integer32
_SrvLanCardDrvMajorVer_Object = MibTableColumn
srvLanCardDrvMajorVer = _SrvLanCardDrvMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 9),
    _SrvLanCardDrvMajorVer_Type()
)
srvLanCardDrvMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardDrvMajorVer.setStatus("mandatory")
_SrvLanCardDrvMinorVer_Type = Integer32
_SrvLanCardDrvMinorVer_Object = MibTableColumn
srvLanCardDrvMinorVer = _SrvLanCardDrvMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 10),
    _SrvLanCardDrvMinorVer_Type()
)
srvLanCardDrvMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardDrvMinorVer.setStatus("mandatory")
_SrvLanCardMemoryAddr_Type = Integer32
_SrvLanCardMemoryAddr_Object = MibTableColumn
srvLanCardMemoryAddr = _SrvLanCardMemoryAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 11),
    _SrvLanCardMemoryAddr_Type()
)
srvLanCardMemoryAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardMemoryAddr.setStatus("mandatory")
_SrvLanCardInterrupt_Type = Integer32
_SrvLanCardInterrupt_Object = MibTableColumn
srvLanCardInterrupt = _SrvLanCardInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 12),
    _SrvLanCardInterrupt_Type()
)
srvLanCardInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardInterrupt.setStatus("mandatory")
_SrvLanCardDMAUsage_Type = Integer32
_SrvLanCardDMAUsage_Object = MibTableColumn
srvLanCardDMAUsage = _SrvLanCardDMAUsage_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 26, 1, 13),
    _SrvLanCardDMAUsage_Type()
)
srvLanCardDMAUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvLanCardDMAUsage.setStatus("mandatory")
_SrvNbOfSoftPackage_Type = PositiveInteger
_SrvNbOfSoftPackage_Object = MibScalar
srvNbOfSoftPackage = _SrvNbOfSoftPackage_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 27),
    _SrvNbOfSoftPackage_Type()
)
srvNbOfSoftPackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvNbOfSoftPackage.setStatus("mandatory")
_SrvSoftPackageTable_Object = MibTable
srvSoftPackageTable = _SrvSoftPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 28)
)
if mibBuilder.loadTexts:
    srvSoftPackageTable.setStatus("mandatory")
_SrvPackageEntry_Object = MibTableRow
srvPackageEntry = _SrvPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 28, 1)
)
srvPackageEntry.setIndexNames(
    (0, "EICON-MIB-SERVER", "srvProductIndex"),
)
if mibBuilder.loadTexts:
    srvPackageEntry.setStatus("mandatory")
_SrvProductIndex_Type = PositiveInteger
_SrvProductIndex_Object = MibTableColumn
srvProductIndex = _SrvProductIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 28, 1, 1),
    _SrvProductIndex_Type()
)
srvProductIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvProductIndex.setStatus("mandatory")


class _SrvProductName_Type(DisplayString):
    """Custom type srvProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvProductName_Type.__name__ = "DisplayString"
_SrvProductName_Object = MibTableColumn
srvProductName = _SrvProductName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 28, 1, 2),
    _SrvProductName_Type()
)
srvProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvProductName.setStatus("mandatory")


class _SrvProductVersion_Type(DisplayString):
    """Custom type srvProductVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SrvProductVersion_Type.__name__ = "DisplayString"
_SrvProductVersion_Object = MibTableColumn
srvProductVersion = _SrvProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 28, 1, 3),
    _SrvProductVersion_Type()
)
srvProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvProductVersion.setStatus("mandatory")


class _SrvProductDate_Type(DisplayString):
    """Custom type srvProductDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SrvProductDate_Type.__name__ = "DisplayString"
_SrvProductDate_Object = MibTableColumn
srvProductDate = _SrvProductDate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 28, 1, 4),
    _SrvProductDate_Type()
)
srvProductDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvProductDate.setStatus("mandatory")


class _SrvProductConfigured_Type(Integer32):
    """Custom type srvProductConfigured based on Integer32"""
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


_SrvProductConfigured_Type.__name__ = "Integer32"
_SrvProductConfigured_Object = MibTableColumn
srvProductConfigured = _SrvProductConfigured_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 28, 1, 5),
    _SrvProductConfigured_Type()
)
srvProductConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvProductConfigured.setStatus("mandatory")
_SrvCfgNbOfEiconCards_Type = CardRef
_SrvCfgNbOfEiconCards_Object = MibScalar
srvCfgNbOfEiconCards = _SrvCfgNbOfEiconCards_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 29),
    _SrvCfgNbOfEiconCards_Type()
)
srvCfgNbOfEiconCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgNbOfEiconCards.setStatus("mandatory")
_SrvCfgEiconCardTable_Object = MibTable
srvCfgEiconCardTable = _SrvCfgEiconCardTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30)
)
if mibBuilder.loadTexts:
    srvCfgEiconCardTable.setStatus("mandatory")
_SrvCfgEiconCardEntry_Object = MibTableRow
srvCfgEiconCardEntry = _SrvCfgEiconCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1)
)
srvCfgEiconCardEntry.setIndexNames(
    (0, "EICON-MIB-SERVER", "srvCfgECIndex"),
)
if mibBuilder.loadTexts:
    srvCfgEiconCardEntry.setStatus("mandatory")
_SrvCfgECIndex_Type = CardRef
_SrvCfgECIndex_Object = MibTableColumn
srvCfgECIndex = _SrvCfgECIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 1),
    _SrvCfgECIndex_Type()
)
srvCfgECIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECIndex.setStatus("mandatory")
_SrvCfgECMemAddr_Type = Integer32
_SrvCfgECMemAddr_Object = MibTableColumn
srvCfgECMemAddr = _SrvCfgECMemAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 2),
    _SrvCfgECMemAddr_Type()
)
srvCfgECMemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECMemAddr.setStatus("mandatory")
_SrvCfgECIoAddr_Type = Integer32
_SrvCfgECIoAddr_Object = MibTableColumn
srvCfgECIoAddr = _SrvCfgECIoAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 3),
    _SrvCfgECIoAddr_Type()
)
srvCfgECIoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECIoAddr.setStatus("mandatory")
_SrvCfgECIntrLevel_Type = Integer32
_SrvCfgECIntrLevel_Object = MibTableColumn
srvCfgECIntrLevel = _SrvCfgECIntrLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 4),
    _SrvCfgECIntrLevel_Type()
)
srvCfgECIntrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECIntrLevel.setStatus("mandatory")
_SrvCfgECNbOfPorts_Type = PortRef
_SrvCfgECNbOfPorts_Object = MibTableColumn
srvCfgECNbOfPorts = _SrvCfgECNbOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 5),
    _SrvCfgECNbOfPorts_Type()
)
srvCfgECNbOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECNbOfPorts.setStatus("mandatory")


class _SrvCfgECSlotNumber_Type(Integer32):
    """Custom type srvCfgECSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SrvCfgECSlotNumber_Type.__name__ = "Integer32"
_SrvCfgECSlotNumber_Object = MibTableColumn
srvCfgECSlotNumber = _SrvCfgECSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 6),
    _SrvCfgECSlotNumber_Type()
)
srvCfgECSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECSlotNumber.setStatus("mandatory")


class _SrvCfgECOptModule_Type(Integer32):
    """Custom type srvCfgECOptModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mod-DPSM", 1),
          ("mod-HSIM", 2),
          ("mod-None", 3))
    )


_SrvCfgECOptModule_Type.__name__ = "Integer32"
_SrvCfgECOptModule_Object = MibTableColumn
srvCfgECOptModule = _SrvCfgECOptModule_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 7),
    _SrvCfgECOptModule_Type()
)
srvCfgECOptModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECOptModule.setStatus("mandatory")


class _SrvCfgECAutoActivate_Type(Integer32):
    """Custom type srvCfgECAutoActivate based on Integer32"""
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


_SrvCfgECAutoActivate_Type.__name__ = "Integer32"
_SrvCfgECAutoActivate_Object = MibTableColumn
srvCfgECAutoActivate = _SrvCfgECAutoActivate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 30, 1, 8),
    _SrvCfgECAutoActivate_Type()
)
srvCfgECAutoActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgECAutoActivate.setStatus("mandatory")
_SrvCfgNbOfPorts_Type = PortRef
_SrvCfgNbOfPorts_Object = MibScalar
srvCfgNbOfPorts = _SrvCfgNbOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 31),
    _SrvCfgNbOfPorts_Type()
)
srvCfgNbOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgNbOfPorts.setStatus("mandatory")
_SrvCfgPortTable_Object = MibTable
srvCfgPortTable = _SrvCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 32)
)
if mibBuilder.loadTexts:
    srvCfgPortTable.setStatus("mandatory")
_SrvCfgPortEntry_Object = MibTableRow
srvCfgPortEntry = _SrvCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 32, 1)
)
srvCfgPortEntry.setIndexNames(
    (0, "EICON-MIB-SERVER", "srvCfgPortIndex"),
)
if mibBuilder.loadTexts:
    srvCfgPortEntry.setStatus("mandatory")
_SrvCfgPortIndex_Type = PortRef
_SrvCfgPortIndex_Object = MibTableColumn
srvCfgPortIndex = _SrvCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 32, 1, 1),
    _SrvCfgPortIndex_Type()
)
srvCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgPortIndex.setStatus("mandatory")
_SrvCfgPortLanaNo_Type = PortRef
_SrvCfgPortLanaNo_Object = MibTableColumn
srvCfgPortLanaNo = _SrvCfgPortLanaNo_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 32, 1, 2),
    _SrvCfgPortLanaNo_Type()
)
srvCfgPortLanaNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgPortLanaNo.setStatus("mandatory")
_SrvCfgPortName_Type = PortName
_SrvCfgPortName_Object = MibTableColumn
srvCfgPortName = _SrvCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 32, 1, 3),
    _SrvCfgPortName_Type()
)
srvCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvCfgPortName.setStatus("mandatory")


class _SrvDescr_Type(DisplayString):
    """Custom type srvDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SrvDescr_Type.__name__ = "DisplayString"
_SrvDescr_Object = MibScalar
srvDescr = _SrvDescr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 33),
    _SrvDescr_Type()
)
srvDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDescr.setStatus("mandatory")
_SrvObjectID_Type = ObjectIdentifier
_SrvObjectID_Object = MibScalar
srvObjectID = _SrvObjectID_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 34),
    _SrvObjectID_Type()
)
srvObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvObjectID.setStatus("mandatory")
_SrvUpTime_Type = TimeTicks
_SrvUpTime_Object = MibScalar
srvUpTime = _SrvUpTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 35),
    _SrvUpTime_Type()
)
srvUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvUpTime.setStatus("mandatory")


class _SrvContact_Type(DisplayString):
    """Custom type srvContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SrvContact_Type.__name__ = "DisplayString"
_SrvContact_Object = MibScalar
srvContact = _SrvContact_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 36),
    _SrvContact_Type()
)
srvContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvContact.setStatus("mandatory")


class _SrvName_Type(DisplayString):
    """Custom type srvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SrvName_Type.__name__ = "DisplayString"
_SrvName_Object = MibScalar
srvName = _SrvName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 37),
    _SrvName_Type()
)
srvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvName.setStatus("mandatory")


class _SrvLocation_Type(DisplayString):
    """Custom type srvLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SrvLocation_Type.__name__ = "DisplayString"
_SrvLocation_Object = MibScalar
srvLocation = _SrvLocation_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 38),
    _SrvLocation_Type()
)
srvLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvLocation.setStatus("mandatory")


class _SrvServices_Type(Integer32):
    """Custom type srvServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SrvServices_Type.__name__ = "Integer32"
_SrvServices_Object = MibScalar
srvServices = _SrvServices_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 39),
    _SrvServices_Type()
)
srvServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvServices.setStatus("mandatory")
_SrvIfNumber_Type = Integer32
_SrvIfNumber_Object = MibScalar
srvIfNumber = _SrvIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 40),
    _SrvIfNumber_Type()
)
srvIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfNumber.setStatus("mandatory")
_SrvIfTable_Object = MibTable
srvIfTable = _SrvIfTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41)
)
if mibBuilder.loadTexts:
    srvIfTable.setStatus("mandatory")
_SrvIfEntry_Object = MibTableRow
srvIfEntry = _SrvIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1)
)
srvIfEntry.setIndexNames(
    (0, "EICON-MIB-SERVER", "srvIfIndex"),
)
if mibBuilder.loadTexts:
    srvIfEntry.setStatus("mandatory")
_SrvIfIndex_Type = Integer32
_SrvIfIndex_Object = MibTableColumn
srvIfIndex = _SrvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 1),
    _SrvIfIndex_Type()
)
srvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfIndex.setStatus("mandatory")


class _SrvIfDescr_Type(DisplayString):
    """Custom type srvIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SrvIfDescr_Type.__name__ = "DisplayString"
_SrvIfDescr_Object = MibTableColumn
srvIfDescr = _SrvIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 2),
    _SrvIfDescr_Type()
)
srvIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfDescr.setStatus("mandatory")


class _SrvIfType_Type(Integer32):
    """Custom type srvIfType based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("appc", 33),
          ("basicISDN", 20),
          ("ddn-x25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
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
          ("llc", 39),
          ("netview", 38),
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
          ("snafm", 34),
          ("snafr", 40),
          ("snapc", 35),
          ("softwareLoopback", 24),
          ("starLan", 11),
          ("ultra", 29),
          ("xport-iso", 36),
          ("xport-tgx", 37))
    )


_SrvIfType_Type.__name__ = "Integer32"
_SrvIfType_Object = MibTableColumn
srvIfType = _SrvIfType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 3),
    _SrvIfType_Type()
)
srvIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfType.setStatus("mandatory")
_SrvIfMtu_Type = Integer32
_SrvIfMtu_Object = MibTableColumn
srvIfMtu = _SrvIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 4),
    _SrvIfMtu_Type()
)
srvIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfMtu.setStatus("mandatory")
_SrvIfSpeed_Type = Gauge32
_SrvIfSpeed_Object = MibTableColumn
srvIfSpeed = _SrvIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 5),
    _SrvIfSpeed_Type()
)
srvIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfSpeed.setStatus("mandatory")
_SrvIfPhysAddress_Type = PhysAddress
_SrvIfPhysAddress_Object = MibTableColumn
srvIfPhysAddress = _SrvIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 6),
    _SrvIfPhysAddress_Type()
)
srvIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfPhysAddress.setStatus("mandatory")


class _SrvIfAdminStatus_Type(Integer32):
    """Custom type srvIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SrvIfAdminStatus_Type.__name__ = "Integer32"
_SrvIfAdminStatus_Object = MibTableColumn
srvIfAdminStatus = _SrvIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 7),
    _SrvIfAdminStatus_Type()
)
srvIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvIfAdminStatus.setStatus("mandatory")


class _SrvIfOperStatus_Type(Integer32):
    """Custom type srvIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SrvIfOperStatus_Type.__name__ = "Integer32"
_SrvIfOperStatus_Object = MibTableColumn
srvIfOperStatus = _SrvIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 8),
    _SrvIfOperStatus_Type()
)
srvIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfOperStatus.setStatus("mandatory")
_SrvIfLastChange_Type = TimeTicks
_SrvIfLastChange_Object = MibTableColumn
srvIfLastChange = _SrvIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 9),
    _SrvIfLastChange_Type()
)
srvIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfLastChange.setStatus("mandatory")
_SrvIfInOctets_Type = Counter32
_SrvIfInOctets_Object = MibTableColumn
srvIfInOctets = _SrvIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 10),
    _SrvIfInOctets_Type()
)
srvIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfInOctets.setStatus("mandatory")
_SrvIfInUcastPkts_Type = Counter32
_SrvIfInUcastPkts_Object = MibTableColumn
srvIfInUcastPkts = _SrvIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 11),
    _SrvIfInUcastPkts_Type()
)
srvIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfInUcastPkts.setStatus("mandatory")
_SrvIfInNUcastPkts_Type = Counter32
_SrvIfInNUcastPkts_Object = MibTableColumn
srvIfInNUcastPkts = _SrvIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 12),
    _SrvIfInNUcastPkts_Type()
)
srvIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfInNUcastPkts.setStatus("mandatory")
_SrvIfInDiscards_Type = Counter32
_SrvIfInDiscards_Object = MibTableColumn
srvIfInDiscards = _SrvIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 13),
    _SrvIfInDiscards_Type()
)
srvIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfInDiscards.setStatus("mandatory")
_SrvIfInErrors_Type = Counter32
_SrvIfInErrors_Object = MibTableColumn
srvIfInErrors = _SrvIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 14),
    _SrvIfInErrors_Type()
)
srvIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfInErrors.setStatus("mandatory")
_SrvIfInUnknownProtos_Type = Counter32
_SrvIfInUnknownProtos_Object = MibTableColumn
srvIfInUnknownProtos = _SrvIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 15),
    _SrvIfInUnknownProtos_Type()
)
srvIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfInUnknownProtos.setStatus("mandatory")
_SrvIfOutOctets_Type = Counter32
_SrvIfOutOctets_Object = MibTableColumn
srvIfOutOctets = _SrvIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 16),
    _SrvIfOutOctets_Type()
)
srvIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfOutOctets.setStatus("mandatory")
_SrvIfOutUcastPkts_Type = Counter32
_SrvIfOutUcastPkts_Object = MibTableColumn
srvIfOutUcastPkts = _SrvIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 17),
    _SrvIfOutUcastPkts_Type()
)
srvIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfOutUcastPkts.setStatus("mandatory")
_SrvIfOutNUcastPkts_Type = Counter32
_SrvIfOutNUcastPkts_Object = MibTableColumn
srvIfOutNUcastPkts = _SrvIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 18),
    _SrvIfOutNUcastPkts_Type()
)
srvIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfOutNUcastPkts.setStatus("mandatory")
_SrvIfOutDiscards_Type = Counter32
_SrvIfOutDiscards_Object = MibTableColumn
srvIfOutDiscards = _SrvIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 19),
    _SrvIfOutDiscards_Type()
)
srvIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfOutDiscards.setStatus("mandatory")
_SrvIfOutErrors_Type = Counter32
_SrvIfOutErrors_Object = MibTableColumn
srvIfOutErrors = _SrvIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 20),
    _SrvIfOutErrors_Type()
)
srvIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfOutErrors.setStatus("mandatory")
_SrvIfOutQLen_Type = Gauge32
_SrvIfOutQLen_Object = MibTableColumn
srvIfOutQLen = _SrvIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 21),
    _SrvIfOutQLen_Type()
)
srvIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfOutQLen.setStatus("mandatory")
_SrvIfSpecific_Type = Integer32
_SrvIfSpecific_Object = MibTableColumn
srvIfSpecific = _SrvIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 41, 1, 22),
    _SrvIfSpecific_Type()
)
srvIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvIfSpecific.setStatus("mandatory")


class _SrvModulesOperStates_Type(OctetString):
    """Custom type srvModulesOperStates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SrvModulesOperStates_Type.__name__ = "OctetString"
_SrvModulesOperStates_Object = MibScalar
srvModulesOperStates = _SrvModulesOperStates_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 42),
    _SrvModulesOperStates_Type()
)
srvModulesOperStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvModulesOperStates.setStatus("mandatory")


class _SrvInstallDirName_Type(DisplayString):
    """Custom type srvInstallDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SrvInstallDirName_Type.__name__ = "DisplayString"
_SrvInstallDirName_Object = MibScalar
srvInstallDirName = _SrvInstallDirName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 43),
    _SrvInstallDirName_Type()
)
srvInstallDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvInstallDirName.setStatus("mandatory")


class _SrvCurrDirName_Type(DisplayString):
    """Custom type srvCurrDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SrvCurrDirName_Type.__name__ = "DisplayString"
_SrvCurrDirName_Object = MibScalar
srvCurrDirName = _SrvCurrDirName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 44),
    _SrvCurrDirName_Type()
)
srvCurrDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvCurrDirName.setStatus("mandatory")
_SrvDirTable_Object = MibTable
srvDirTable = _SrvDirTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 45)
)
if mibBuilder.loadTexts:
    srvDirTable.setStatus("mandatory")
_SrvDirEntry_Object = MibTableRow
srvDirEntry = _SrvDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 45, 1)
)
srvDirEntry.setIndexNames(
    (0, "EICON-MIB-SERVER", "srvIfIndex"),
)
if mibBuilder.loadTexts:
    srvDirEntry.setStatus("mandatory")
_SrvDirIndex_Type = Integer32
_SrvDirIndex_Object = MibTableColumn
srvDirIndex = _SrvDirIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 45, 1, 1),
    _SrvDirIndex_Type()
)
srvDirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDirIndex.setStatus("mandatory")


class _SrvDirFilename_Type(DisplayString):
    """Custom type srvDirFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SrvDirFilename_Type.__name__ = "DisplayString"
_SrvDirFilename_Object = MibTableColumn
srvDirFilename = _SrvDirFilename_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 45, 1, 2),
    _SrvDirFilename_Type()
)
srvDirFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDirFilename.setStatus("mandatory")
_SrvDirFileAttribute_Type = Integer32
_SrvDirFileAttribute_Object = MibTableColumn
srvDirFileAttribute = _SrvDirFileAttribute_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 45, 1, 3),
    _SrvDirFileAttribute_Type()
)
srvDirFileAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDirFileAttribute.setStatus("mandatory")
_SrvDirFileAccessTime_Type = Integer32
_SrvDirFileAccessTime_Object = MibTableColumn
srvDirFileAccessTime = _SrvDirFileAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 45, 1, 4),
    _SrvDirFileAccessTime_Type()
)
srvDirFileAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDirFileAccessTime.setStatus("mandatory")
_SrvDirFileSize_Type = Integer32
_SrvDirFileSize_Object = MibTableColumn
srvDirFileSize = _SrvDirFileSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 1, 45, 1, 5),
    _SrvDirFileSize_Type()
)
srvDirFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvDirFileSize.setStatus("mandatory")
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)

# Managed Objects groups


# Notification objects

srvTrapHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 0, 11)
)
srvTrapHeartbeat.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    srvTrapHeartbeat.setStatus(
        ""
    )

srvTrapInternal = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 0, 12)
)
srvTrapInternal.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    srvTrapInternal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-MIB-SERVER",
    **{"OperState": OperState,
       "AdminState": AdminState,
       "ActionState": ActionState,
       "EiconCardType": EiconCardType,
       "ControlOnOff": ControlOnOff,
       "CardRef": CardRef,
       "PortRef": PortRef,
       "PortName": PortName,
       "PositiveInteger": PositiveInteger,
       "eicon": eicon,
       "srvTrapHeartbeat": srvTrapHeartbeat,
       "srvTrapInternal": srvTrapInternal,
       "management": management,
       "mibv2": mibv2,
       "server": server,
       "srvAdminStateCtr": srvAdminStateCtr,
       "srvOsName": srvOsName,
       "srvOsVersion": srvOsVersion,
       "srvNosName": srvNosName,
       "srvNosVersion": srvNosVersion,
       "srvLanShellInfo": srvLanShellInfo,
       "srvBusType": srvBusType,
       "srvCpuType": srvCpuType,
       "srvCpuSpeed": srvCpuSpeed,
       "srvStdMemory": srvStdMemory,
       "srvExtendMemory": srvExtendMemory,
       "srvExpandedMemory": srvExpandedMemory,
       "srvVideoAdaptType": srvVideoAdaptType,
       "srvHardDisk": srvHardDisk,
       "srvHardDiskSize": srvHardDiskSize,
       "srvNotePad": srvNotePad,
       "srvAgentMajorVersion": srvAgentMajorVersion,
       "srvAgentMinorVersion": srvAgentMinorVersion,
       "srvAgentMaxOfLostNMPHeartB": srvAgentMaxOfLostNMPHeartB,
       "srvAgentHeartBeatPeriod": srvAgentHeartBeatPeriod,
       "srvAgentPollFrequency": srvAgentPollFrequency,
       "srvAgentAlarmsFilterValue": srvAgentAlarmsFilterValue,
       "srvDomainName": srvDomainName,
       "srvDomainConfigDir": srvDomainConfigDir,
       "srvNbOfLanCards": srvNbOfLanCards,
       "srvLanCardTable": srvLanCardTable,
       "srvLanCardEntry": srvLanCardEntry,
       "srvLanCardIndex": srvLanCardIndex,
       "srvLanCardCFGMajorVer": srvLanCardCFGMajorVer,
       "srvLanCardCFGMinorVer": srvLanCardCFGMinorVer,
       "srvLanCardNodeAddr": srvLanCardNodeAddr,
       "srvLanCardMaxSize": srvLanCardMaxSize,
       "srvLanCardName": srvLanCardName,
       "srvLanCardShortName": srvLanCardShortName,
       "srvLanCardFrameType": srvLanCardFrameType,
       "srvLanCardDrvMajorVer": srvLanCardDrvMajorVer,
       "srvLanCardDrvMinorVer": srvLanCardDrvMinorVer,
       "srvLanCardMemoryAddr": srvLanCardMemoryAddr,
       "srvLanCardInterrupt": srvLanCardInterrupt,
       "srvLanCardDMAUsage": srvLanCardDMAUsage,
       "srvNbOfSoftPackage": srvNbOfSoftPackage,
       "srvSoftPackageTable": srvSoftPackageTable,
       "srvPackageEntry": srvPackageEntry,
       "srvProductIndex": srvProductIndex,
       "srvProductName": srvProductName,
       "srvProductVersion": srvProductVersion,
       "srvProductDate": srvProductDate,
       "srvProductConfigured": srvProductConfigured,
       "srvCfgNbOfEiconCards": srvCfgNbOfEiconCards,
       "srvCfgEiconCardTable": srvCfgEiconCardTable,
       "srvCfgEiconCardEntry": srvCfgEiconCardEntry,
       "srvCfgECIndex": srvCfgECIndex,
       "srvCfgECMemAddr": srvCfgECMemAddr,
       "srvCfgECIoAddr": srvCfgECIoAddr,
       "srvCfgECIntrLevel": srvCfgECIntrLevel,
       "srvCfgECNbOfPorts": srvCfgECNbOfPorts,
       "srvCfgECSlotNumber": srvCfgECSlotNumber,
       "srvCfgECOptModule": srvCfgECOptModule,
       "srvCfgECAutoActivate": srvCfgECAutoActivate,
       "srvCfgNbOfPorts": srvCfgNbOfPorts,
       "srvCfgPortTable": srvCfgPortTable,
       "srvCfgPortEntry": srvCfgPortEntry,
       "srvCfgPortIndex": srvCfgPortIndex,
       "srvCfgPortLanaNo": srvCfgPortLanaNo,
       "srvCfgPortName": srvCfgPortName,
       "srvDescr": srvDescr,
       "srvObjectID": srvObjectID,
       "srvUpTime": srvUpTime,
       "srvContact": srvContact,
       "srvName": srvName,
       "srvLocation": srvLocation,
       "srvServices": srvServices,
       "srvIfNumber": srvIfNumber,
       "srvIfTable": srvIfTable,
       "srvIfEntry": srvIfEntry,
       "srvIfIndex": srvIfIndex,
       "srvIfDescr": srvIfDescr,
       "srvIfType": srvIfType,
       "srvIfMtu": srvIfMtu,
       "srvIfSpeed": srvIfSpeed,
       "srvIfPhysAddress": srvIfPhysAddress,
       "srvIfAdminStatus": srvIfAdminStatus,
       "srvIfOperStatus": srvIfOperStatus,
       "srvIfLastChange": srvIfLastChange,
       "srvIfInOctets": srvIfInOctets,
       "srvIfInUcastPkts": srvIfInUcastPkts,
       "srvIfInNUcastPkts": srvIfInNUcastPkts,
       "srvIfInDiscards": srvIfInDiscards,
       "srvIfInErrors": srvIfInErrors,
       "srvIfInUnknownProtos": srvIfInUnknownProtos,
       "srvIfOutOctets": srvIfOutOctets,
       "srvIfOutUcastPkts": srvIfOutUcastPkts,
       "srvIfOutNUcastPkts": srvIfOutNUcastPkts,
       "srvIfOutDiscards": srvIfOutDiscards,
       "srvIfOutErrors": srvIfOutErrors,
       "srvIfOutQLen": srvIfOutQLen,
       "srvIfSpecific": srvIfSpecific,
       "srvModulesOperStates": srvModulesOperStates,
       "srvInstallDirName": srvInstallDirName,
       "srvCurrDirName": srvCurrDirName,
       "srvDirTable": srvDirTable,
       "srvDirEntry": srvDirEntry,
       "srvDirIndex": srvDirIndex,
       "srvDirFilename": srvDirFilename,
       "srvDirFileAttribute": srvDirFileAttribute,
       "srvDirFileAccessTime": srvDirFileAccessTime,
       "srvDirFileSize": srvDirFileSize,
       "module": module}
)
