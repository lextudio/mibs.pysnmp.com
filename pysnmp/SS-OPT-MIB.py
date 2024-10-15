# SNMP MIB module (SS-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SS-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:40 2024
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
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500GCTLSSTable_Object = MibTable
cdx6500GCTLSSTable = _Cdx6500GCTLSSTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14)
)
if mibBuilder.loadTexts:
    cdx6500GCTLSSTable.setStatus("mandatory")
_Cdx6500SSCfgEntry_Object = MibTableRow
cdx6500SSCfgEntry = _Cdx6500SSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1)
)
cdx6500SSCfgEntry.setIndexNames(
    (0, "SS-OPT-MIB", "cdx6500SSEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500SSCfgEntry.setStatus("mandatory")


class _Cdx6500SSEntryNumber_Type(Integer32):
    """Custom type cdx6500SSEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Cdx6500SSEntryNumber_Type.__name__ = "Integer32"
_Cdx6500SSEntryNumber_Object = MibTableColumn
cdx6500SSEntryNumber = _Cdx6500SSEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 1),
    _Cdx6500SSEntryNumber_Type()
)
cdx6500SSEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSEntryNumber.setStatus("mandatory")


class _Cdx6500SSDestinationName_Type(DisplayString):
    """Custom type cdx6500SSDestinationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500SSDestinationName_Type.__name__ = "DisplayString"
_Cdx6500SSDestinationName_Object = MibTableColumn
cdx6500SSDestinationName = _Cdx6500SSDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 2),
    _Cdx6500SSDestinationName_Type()
)
cdx6500SSDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSDestinationName.setStatus("mandatory")


class _Cdx6500SSCfgMonitoredPort_Type(DisplayString):
    """Custom type cdx6500SSCfgMonitoredPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500SSCfgMonitoredPort_Type.__name__ = "DisplayString"
_Cdx6500SSCfgMonitoredPort_Object = MibTableColumn
cdx6500SSCfgMonitoredPort = _Cdx6500SSCfgMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 3),
    _Cdx6500SSCfgMonitoredPort_Type()
)
cdx6500SSCfgMonitoredPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSCfgMonitoredPort.setStatus("mandatory")


class _Cdx6500SSCfgRestoralPort_Type(DisplayString):
    """Custom type cdx6500SSCfgRestoralPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500SSCfgRestoralPort_Type.__name__ = "DisplayString"
_Cdx6500SSCfgRestoralPort_Object = MibTableColumn
cdx6500SSCfgRestoralPort = _Cdx6500SSCfgRestoralPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 4),
    _Cdx6500SSCfgRestoralPort_Type()
)
cdx6500SSCfgRestoralPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSCfgRestoralPort.setStatus("mandatory")


class _Cdx6500SSDialSequence_Type(DisplayString):
    """Custom type cdx6500SSDialSequence based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cdx6500SSDialSequence_Type.__name__ = "DisplayString"
_Cdx6500SSDialSequence_Object = MibTableColumn
cdx6500SSDialSequence = _Cdx6500SSDialSequence_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 5),
    _Cdx6500SSDialSequence_Type()
)
cdx6500SSDialSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSDialSequence.setStatus("mandatory")


class _Cdx6500SSActivationMode_Type(Integer32):
    """Custom type cdx6500SSActivationMode based on Integer32"""
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
        *(("call", 1),
          ("either", 2),
          ("fail", 0),
          ("newvalFail", 50))
    )


_Cdx6500SSActivationMode_Type.__name__ = "Integer32"
_Cdx6500SSActivationMode_Object = MibTableColumn
cdx6500SSActivationMode = _Cdx6500SSActivationMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 6),
    _Cdx6500SSActivationMode_Type()
)
cdx6500SSActivationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSActivationMode.setStatus("mandatory")


class _Cdx6500SSDeactivationMode_Type(Integer32):
    """Custom type cdx6500SSDeactivationMode based on Integer32"""
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
        *(("busyOut", 1),
          ("imm", 2),
          ("newvalNone", 50),
          ("none", 0))
    )


_Cdx6500SSDeactivationMode_Type.__name__ = "Integer32"
_Cdx6500SSDeactivationMode_Object = MibTableColumn
cdx6500SSDeactivationMode = _Cdx6500SSDeactivationMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 7),
    _Cdx6500SSDeactivationMode_Type()
)
cdx6500SSDeactivationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSDeactivationMode.setStatus("mandatory")
_Cdx6500SSLinkHoldTime_Type = Integer32
_Cdx6500SSLinkHoldTime_Object = MibTableColumn
cdx6500SSLinkHoldTime = _Cdx6500SSLinkHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 8),
    _Cdx6500SSLinkHoldTime_Type()
)
cdx6500SSLinkHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSLinkHoldTime.setStatus("mandatory")


class _Cdx6500SSOutBoundPass_Type(DisplayString):
    """Custom type cdx6500SSOutBoundPass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Cdx6500SSOutBoundPass_Type.__name__ = "DisplayString"
_Cdx6500SSOutBoundPass_Object = MibTableColumn
cdx6500SSOutBoundPass = _Cdx6500SSOutBoundPass_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 9),
    _Cdx6500SSOutBoundPass_Type()
)
cdx6500SSOutBoundPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSOutBoundPass.setStatus("mandatory")
_Cdx6500SSRedialTime_Type = Integer32
_Cdx6500SSRedialTime_Object = MibTableColumn
cdx6500SSRedialTime = _Cdx6500SSRedialTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 10),
    _Cdx6500SSRedialTime_Type()
)
cdx6500SSRedialTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSRedialTime.setStatus("mandatory")
_Cdx6500SSRedialCounter_Type = Integer32
_Cdx6500SSRedialCounter_Object = MibTableColumn
cdx6500SSRedialCounter = _Cdx6500SSRedialCounter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 11),
    _Cdx6500SSRedialCounter_Type()
)
cdx6500SSRedialCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSRedialCounter.setStatus("mandatory")


class _Cdx6500SSSecurityMode_Type(Integer32):
    """Custom type cdx6500SSSecurityMode based on Integer32"""
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
        *(("both", 3),
          ("callingId", 2),
          ("newvalNone", 50),
          ("none", 0),
          ("password", 1))
    )


_Cdx6500SSSecurityMode_Type.__name__ = "Integer32"
_Cdx6500SSSecurityMode_Object = MibTableColumn
cdx6500SSSecurityMode = _Cdx6500SSSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 12),
    _Cdx6500SSSecurityMode_Type()
)
cdx6500SSSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSSecurityMode.setStatus("mandatory")
_Cdx6500SSSetupTime_Type = Integer32
_Cdx6500SSSetupTime_Object = MibTableColumn
cdx6500SSSetupTime = _Cdx6500SSSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 13),
    _Cdx6500SSSetupTime_Type()
)
cdx6500SSSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSSetupTime.setStatus("mandatory")


class _Cdx6500SSCfgMonitoredPort2_Type(DisplayString):
    """Custom type cdx6500SSCfgMonitoredPort2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500SSCfgMonitoredPort2_Type.__name__ = "DisplayString"
_Cdx6500SSCfgMonitoredPort2_Object = MibTableColumn
cdx6500SSCfgMonitoredPort2 = _Cdx6500SSCfgMonitoredPort2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 14),
    _Cdx6500SSCfgMonitoredPort2_Type()
)
cdx6500SSCfgMonitoredPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSCfgMonitoredPort2.setStatus("mandatory")


class _Cdx6500SSCfgMonitoredPort3_Type(DisplayString):
    """Custom type cdx6500SSCfgMonitoredPort3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500SSCfgMonitoredPort3_Type.__name__ = "DisplayString"
_Cdx6500SSCfgMonitoredPort3_Object = MibTableColumn
cdx6500SSCfgMonitoredPort3 = _Cdx6500SSCfgMonitoredPort3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 15),
    _Cdx6500SSCfgMonitoredPort3_Type()
)
cdx6500SSCfgMonitoredPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSCfgMonitoredPort3.setStatus("mandatory")


class _Cdx6500SSCfgMonitoredPort4_Type(DisplayString):
    """Custom type cdx6500SSCfgMonitoredPort4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500SSCfgMonitoredPort4_Type.__name__ = "DisplayString"
_Cdx6500SSCfgMonitoredPort4_Object = MibTableColumn
cdx6500SSCfgMonitoredPort4 = _Cdx6500SSCfgMonitoredPort4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 16),
    _Cdx6500SSCfgMonitoredPort4_Type()
)
cdx6500SSCfgMonitoredPort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSCfgMonitoredPort4.setStatus("mandatory")


class _Cdx6500SSDialSequence2_Type(DisplayString):
    """Custom type cdx6500SSDialSequence2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cdx6500SSDialSequence2_Type.__name__ = "DisplayString"
_Cdx6500SSDialSequence2_Object = MibTableColumn
cdx6500SSDialSequence2 = _Cdx6500SSDialSequence2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 17),
    _Cdx6500SSDialSequence2_Type()
)
cdx6500SSDialSequence2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSDialSequence2.setStatus("mandatory")


class _Cdx6500SSDialSequence3_Type(DisplayString):
    """Custom type cdx6500SSDialSequence3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cdx6500SSDialSequence3_Type.__name__ = "DisplayString"
_Cdx6500SSDialSequence3_Object = MibTableColumn
cdx6500SSDialSequence3 = _Cdx6500SSDialSequence3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 18),
    _Cdx6500SSDialSequence3_Type()
)
cdx6500SSDialSequence3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSDialSequence3.setStatus("mandatory")


class _Cdx6500SSDialSequence4_Type(DisplayString):
    """Custom type cdx6500SSDialSequence4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cdx6500SSDialSequence4_Type.__name__ = "DisplayString"
_Cdx6500SSDialSequence4_Object = MibTableColumn
cdx6500SSDialSequence4 = _Cdx6500SSDialSequence4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 14, 1, 19),
    _Cdx6500SSDialSequence4_Type()
)
cdx6500SSDialSequence4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSDialSequence4.setStatus("mandatory")
_Cdx6500CallIDTable_Object = MibTable
cdx6500CallIDTable = _Cdx6500CallIDTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 18)
)
if mibBuilder.loadTexts:
    cdx6500CallIDTable.setStatus("mandatory")
_Cdx6500CallIDEntry_Object = MibTableRow
cdx6500CallIDEntry = _Cdx6500CallIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 18, 1)
)
cdx6500CallIDEntry.setIndexNames(
    (0, "SS-OPT-MIB", "cdx6500CallIDEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500CallIDEntry.setStatus("mandatory")


class _Cdx6500CallIDEntryNumber_Type(Integer32):
    """Custom type cdx6500CallIDEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Cdx6500CallIDEntryNumber_Type.__name__ = "Integer32"
_Cdx6500CallIDEntryNumber_Object = MibTableColumn
cdx6500CallIDEntryNumber = _Cdx6500CallIDEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 18, 1, 1),
    _Cdx6500CallIDEntryNumber_Type()
)
cdx6500CallIDEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CallIDEntryNumber.setStatus("mandatory")


class _Cdx6500CallIDString_Type(DisplayString):
    """Custom type cdx6500CallIDString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cdx6500CallIDString_Type.__name__ = "DisplayString"
_Cdx6500CallIDString_Object = MibTableColumn
cdx6500CallIDString = _Cdx6500CallIDString_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 18, 1, 2),
    _Cdx6500CallIDString_Type()
)
cdx6500CallIDString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CallIDString.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500OSTSSTable_Object = MibTable
cdx6500OSTSSTable = _Cdx6500OSTSSTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    cdx6500OSTSSTable.setStatus("mandatory")
_Cdx6500SSStatEntry_Object = MibTableRow
cdx6500SSStatEntry = _Cdx6500SSStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1)
)
cdx6500SSStatEntry.setIndexNames(
    (0, "SS-OPT-MIB", "cdx6500SSStatRestoralPort"),
)
if mibBuilder.loadTexts:
    cdx6500SSStatEntry.setStatus("mandatory")
_Cdx6500SSStatRestoralPort_Type = Integer32
_Cdx6500SSStatRestoralPort_Object = MibTableColumn
cdx6500SSStatRestoralPort = _Cdx6500SSStatRestoralPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 1),
    _Cdx6500SSStatRestoralPort_Type()
)
cdx6500SSStatRestoralPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSStatRestoralPort.setStatus("mandatory")
_Cdx6500SSPortType_Type = DisplayString
_Cdx6500SSPortType_Object = MibTableColumn
cdx6500SSPortType = _Cdx6500SSPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 2),
    _Cdx6500SSPortType_Type()
)
cdx6500SSPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSPortType.setStatus("mandatory")
_Cdx6500SSConnType_Type = DisplayString
_Cdx6500SSConnType_Object = MibTableColumn
cdx6500SSConnType = _Cdx6500SSConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 3),
    _Cdx6500SSConnType_Type()
)
cdx6500SSConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSConnType.setStatus("mandatory")


class _Cdx6500SSStatus_Type(Integer32):
    """Custom type cdx6500SSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              50)
        )
    )
    namedValues = NamedValues(
        *(("activating", 2),
          ("deactivating", 5),
          ("down", 0),
          ("idle", 4),
          ("newvalDown", 50),
          ("redial", 3),
          ("up", 1))
    )


_Cdx6500SSStatus_Type.__name__ = "Integer32"
_Cdx6500SSStatus_Object = MibTableColumn
cdx6500SSStatus = _Cdx6500SSStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 4),
    _Cdx6500SSStatus_Type()
)
cdx6500SSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSStatus.setStatus("mandatory")


class _Cdx6500SSReason_Type(Integer32):
    """Custom type cdx6500SSReason based on Integer32"""
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
        *(("call", 1),
          ("ctp", 4),
          ("fail", 2),
          ("newvalNone", 50),
          ("none", 0),
          ("remote", 3))
    )


_Cdx6500SSReason_Type.__name__ = "Integer32"
_Cdx6500SSReason_Object = MibTableColumn
cdx6500SSReason = _Cdx6500SSReason_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 5),
    _Cdx6500SSReason_Type()
)
cdx6500SSReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSReason.setStatus("mandatory")
_Cdx6500SSRedial_Type = Integer32
_Cdx6500SSRedial_Object = MibTableColumn
cdx6500SSRedial = _Cdx6500SSRedial_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 6),
    _Cdx6500SSRedial_Type()
)
cdx6500SSRedial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSRedial.setStatus("mandatory")
_Cdx6500SSLastActivated_Type = DisplayString
_Cdx6500SSLastActivated_Object = MibTableColumn
cdx6500SSLastActivated = _Cdx6500SSLastActivated_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 7),
    _Cdx6500SSLastActivated_Type()
)
cdx6500SSLastActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSLastActivated.setStatus("mandatory")
_Cdx6500SSLastPhoneDialed_Type = DisplayString
_Cdx6500SSLastPhoneDialed_Object = MibTableColumn
cdx6500SSLastPhoneDialed = _Cdx6500SSLastPhoneDialed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 3, 1, 8),
    _Cdx6500SSLastPhoneDialed_Type()
)
cdx6500SSLastPhoneDialed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSLastPhoneDialed.setStatus("mandatory")
_Cdx6500OSTSSMonTable_Object = MibTable
cdx6500OSTSSMonTable = _Cdx6500OSTSSMonTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    cdx6500OSTSSMonTable.setStatus("mandatory")
_Cdx6500SSMonStatEntry_Object = MibTableRow
cdx6500SSMonStatEntry = _Cdx6500SSMonStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 4, 1)
)
cdx6500SSMonStatEntry.setIndexNames(
    (0, "SS-OPT-MIB", "cdx6500SSStatRestMonPort"),
    (0, "SS-OPT-MIB", "cdx6500SSStatMonitoredPort"),
)
if mibBuilder.loadTexts:
    cdx6500SSMonStatEntry.setStatus("mandatory")
_Cdx6500SSStatRestMonPort_Type = Integer32
_Cdx6500SSStatRestMonPort_Object = MibTableColumn
cdx6500SSStatRestMonPort = _Cdx6500SSStatRestMonPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 4, 1, 1),
    _Cdx6500SSStatRestMonPort_Type()
)
cdx6500SSStatRestMonPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSStatRestMonPort.setStatus("mandatory")
_Cdx6500SSStatMonitoredPort_Type = Integer32
_Cdx6500SSStatMonitoredPort_Object = MibTableColumn
cdx6500SSStatMonitoredPort = _Cdx6500SSStatMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 4, 1, 2),
    _Cdx6500SSStatMonitoredPort_Type()
)
cdx6500SSStatMonitoredPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSStatMonitoredPort.setStatus("mandatory")


class _Cdx6500SSMonPortState_Type(Integer32):
    """Custom type cdx6500SSMonPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              50)
        )
    )
    namedValues = NamedValues(
        *(("activating", 2),
          ("deactivating", 5),
          ("down", 0),
          ("idle", 4),
          ("newvalDown", 50),
          ("redial", 3),
          ("up", 1))
    )


_Cdx6500SSMonPortState_Type.__name__ = "Integer32"
_Cdx6500SSMonPortState_Object = MibTableColumn
cdx6500SSMonPortState = _Cdx6500SSMonPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 4, 1, 3),
    _Cdx6500SSMonPortState_Type()
)
cdx6500SSMonPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSMonPortState.setStatus("mandatory")


class _Cdx6500SSRestPhoneNum_Type(DisplayString):
    """Custom type cdx6500SSRestPhoneNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cdx6500SSRestPhoneNum_Type.__name__ = "DisplayString"
_Cdx6500SSRestPhoneNum_Object = MibTableColumn
cdx6500SSRestPhoneNum = _Cdx6500SSRestPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 4, 1, 4),
    _Cdx6500SSRestPhoneNum_Type()
)
cdx6500SSRestPhoneNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SSRestPhoneNum.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SS-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500GCTLSSTable": cdx6500GCTLSSTable,
       "cdx6500SSCfgEntry": cdx6500SSCfgEntry,
       "cdx6500SSEntryNumber": cdx6500SSEntryNumber,
       "cdx6500SSDestinationName": cdx6500SSDestinationName,
       "cdx6500SSCfgMonitoredPort": cdx6500SSCfgMonitoredPort,
       "cdx6500SSCfgRestoralPort": cdx6500SSCfgRestoralPort,
       "cdx6500SSDialSequence": cdx6500SSDialSequence,
       "cdx6500SSActivationMode": cdx6500SSActivationMode,
       "cdx6500SSDeactivationMode": cdx6500SSDeactivationMode,
       "cdx6500SSLinkHoldTime": cdx6500SSLinkHoldTime,
       "cdx6500SSOutBoundPass": cdx6500SSOutBoundPass,
       "cdx6500SSRedialTime": cdx6500SSRedialTime,
       "cdx6500SSRedialCounter": cdx6500SSRedialCounter,
       "cdx6500SSSecurityMode": cdx6500SSSecurityMode,
       "cdx6500SSSetupTime": cdx6500SSSetupTime,
       "cdx6500SSCfgMonitoredPort2": cdx6500SSCfgMonitoredPort2,
       "cdx6500SSCfgMonitoredPort3": cdx6500SSCfgMonitoredPort3,
       "cdx6500SSCfgMonitoredPort4": cdx6500SSCfgMonitoredPort4,
       "cdx6500SSDialSequence2": cdx6500SSDialSequence2,
       "cdx6500SSDialSequence3": cdx6500SSDialSequence3,
       "cdx6500SSDialSequence4": cdx6500SSDialSequence4,
       "cdx6500CallIDTable": cdx6500CallIDTable,
       "cdx6500CallIDEntry": cdx6500CallIDEntry,
       "cdx6500CallIDEntryNumber": cdx6500CallIDEntryNumber,
       "cdx6500CallIDString": cdx6500CallIDString,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500OSTSSTable": cdx6500OSTSSTable,
       "cdx6500SSStatEntry": cdx6500SSStatEntry,
       "cdx6500SSStatRestoralPort": cdx6500SSStatRestoralPort,
       "cdx6500SSPortType": cdx6500SSPortType,
       "cdx6500SSConnType": cdx6500SSConnType,
       "cdx6500SSStatus": cdx6500SSStatus,
       "cdx6500SSReason": cdx6500SSReason,
       "cdx6500SSRedial": cdx6500SSRedial,
       "cdx6500SSLastActivated": cdx6500SSLastActivated,
       "cdx6500SSLastPhoneDialed": cdx6500SSLastPhoneDialed,
       "cdx6500OSTSSMonTable": cdx6500OSTSSMonTable,
       "cdx6500SSMonStatEntry": cdx6500SSMonStatEntry,
       "cdx6500SSStatRestMonPort": cdx6500SSStatRestMonPort,
       "cdx6500SSStatMonitoredPort": cdx6500SSStatMonitoredPort,
       "cdx6500SSMonPortState": cdx6500SSMonPortState,
       "cdx6500SSRestPhoneNum": cdx6500SSRestPhoneNum}
)
