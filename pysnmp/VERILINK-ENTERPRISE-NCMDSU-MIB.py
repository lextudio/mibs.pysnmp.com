# SNMP MIB module (VERILINK-ENTERPRISE-NCMDSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMDSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:13 2024
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

(ncm_dbu,
 ncm_dds,
 ncm_dsu) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-dbu",
    "ncm-dds",
    "ncm-dsu")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmdsuCommonTable_Object = MibTable
ncmdsuCommonTable = _NcmdsuCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2000)
)
if mibBuilder.loadTexts:
    ncmdsuCommonTable.setStatus("mandatory")
_NcmdsuCommonEntry_Object = MibTableRow
ncmdsuCommonEntry = _NcmdsuCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2000, 1)
)
ncmdsuCommonEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdsuNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdsuIndex"),
)
if mibBuilder.loadTexts:
    ncmdsuCommonEntry.setStatus("mandatory")
_NcmdsuNIDIndex_Type = Integer32
_NcmdsuNIDIndex_Object = MibTableColumn
ncmdsuNIDIndex = _NcmdsuNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2000, 1, 1),
    _NcmdsuNIDIndex_Type()
)
ncmdsuNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuNIDIndex.setStatus("mandatory")
_NcmdsuIndex_Type = Integer32
_NcmdsuIndex_Object = MibTableColumn
ncmdsuIndex = _NcmdsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2000, 1, 2),
    _NcmdsuIndex_Type()
)
ncmdsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuIndex.setStatus("mandatory")


class _NcmdsuPortType_Type(Integer32):
    """Custom type ncmdsuPortType based on Integer32"""
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
        *(("eia530", 4),
          ("none", 1),
          ("rS-232", 5),
          ("rs-449", 3),
          ("unknown", 7),
          ("v35", 2),
          ("wrong-DIM", 6))
    )


_NcmdsuPortType_Type.__name__ = "Integer32"
_NcmdsuPortType_Object = MibTableColumn
ncmdsuPortType = _NcmdsuPortType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2000, 1, 3),
    _NcmdsuPortType_Type()
)
ncmdsuPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortType.setStatus("mandatory")


class _NcmdsuPortLoopback_Type(Integer32):
    """Custom type ncmdsuPortLoopback based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("dds-latching-loop-down", 13),
          ("dds-latching-loop-up", 12),
          ("dds-nonlatching-loop-down", 15),
          ("dds-nonlatching-loop-up", 14),
          ("ft1-loop-down", 17),
          ("ft1-loop-up", 16),
          ("inband-loop", 2),
          ("local-loop", 3),
          ("local-loop-down", 9),
          ("local-loop-up", 8),
          ("none", 1),
          ("sending-loop-down", 5),
          ("sending-loop-up", 4),
          ("v54-loop-down", 11),
          ("v54-loop-up", 10),
          ("verilink-loop-down", 7),
          ("verilink-loop-up", 6))
    )


_NcmdsuPortLoopback_Type.__name__ = "Integer32"
_NcmdsuPortLoopback_Object = MibTableColumn
ncmdsuPortLoopback = _NcmdsuPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2000, 1, 4),
    _NcmdsuPortLoopback_Type()
)
ncmdsuPortLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuPortLoopback.setStatus("mandatory")


class _NcmdsuPortTest_Type(Integer32):
    """Custom type ncmdsuPortTest based on Integer32"""
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
        *(("no-test", 1),
          ("run-ber-test", 3),
          ("start-test", 2),
          ("stop-ber-test", 4),
          ("test-2047", 6),
          ("test-511", 5))
    )


_NcmdsuPortTest_Type.__name__ = "Integer32"
_NcmdsuPortTest_Object = MibTableColumn
ncmdsuPortTest = _NcmdsuPortTest_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2000, 1, 5),
    _NcmdsuPortTest_Type()
)
ncmdsuPortTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuPortTest.setStatus("mandatory")
_NcmdsuConfigTable_Object = MibTable
ncmdsuConfigTable = _NcmdsuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001)
)
if mibBuilder.loadTexts:
    ncmdsuConfigTable.setStatus("mandatory")
_NcmdsuConfigEntry_Object = MibTableRow
ncmdsuConfigEntry = _NcmdsuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1)
)
ncmdsuConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdsuNIDConfigIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdsuLineIndex"),
)
if mibBuilder.loadTexts:
    ncmdsuConfigEntry.setStatus("mandatory")


class _NcmdsuNIDConfigIndex_Type(Integer32):
    """Custom type ncmdsuNIDConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmdsuNIDConfigIndex_Type.__name__ = "Integer32"
_NcmdsuNIDConfigIndex_Object = MibTableColumn
ncmdsuNIDConfigIndex = _NcmdsuNIDConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 1),
    _NcmdsuNIDConfigIndex_Type()
)
ncmdsuNIDConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuNIDConfigIndex.setStatus("mandatory")
_NcmdsuLineIndex_Type = Integer32
_NcmdsuLineIndex_Object = MibTableColumn
ncmdsuLineIndex = _NcmdsuLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 2),
    _NcmdsuLineIndex_Type()
)
ncmdsuLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuLineIndex.setStatus("mandatory")


class _Ncmdsubus_Type(Integer32):
    """Custom type ncmdsubus based on Integer32"""
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
        *(("busA", 2),
          ("busB", 3),
          ("busC", 4),
          ("disabled", 1))
    )


_Ncmdsubus_Type.__name__ = "Integer32"
_Ncmdsubus_Object = MibTableColumn
ncmdsubus = _Ncmdsubus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 3),
    _Ncmdsubus_Type()
)
ncmdsubus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsubus.setStatus("mandatory")


class _NcmdsuPortChannel_Type(DisplayString):
    """Custom type ncmdsuPortChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmdsuPortChannel_Type.__name__ = "DisplayString"
_NcmdsuPortChannel_Object = MibTableColumn
ncmdsuPortChannel = _NcmdsuPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 4),
    _NcmdsuPortChannel_Type()
)
ncmdsuPortChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuPortChannel.setStatus("mandatory")
_NcmdsuPortConfiguration_Type = Integer32
_NcmdsuPortConfiguration_Object = MibTableColumn
ncmdsuPortConfiguration = _NcmdsuPortConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 5),
    _NcmdsuPortConfiguration_Type()
)
ncmdsuPortConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuPortConfiguration.setStatus("mandatory")
_Ncmcsushelf_Type = Integer32
_Ncmcsushelf_Object = MibTableColumn
ncmcsushelf = _Ncmcsushelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 6),
    _Ncmcsushelf_Type()
)
ncmcsushelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsushelf.setStatus("mandatory")
_Ncmcsuslot_Type = Integer32
_Ncmcsuslot_Object = MibTableColumn
ncmcsuslot = _Ncmcsuslot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 7),
    _Ncmcsuslot_Type()
)
ncmcsuslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuslot.setStatus("mandatory")


class _NcmdsuAlarmEnable_Type(Integer32):
    """Custom type ncmdsuAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nO", 1),
          ("yES", 2))
    )


_NcmdsuAlarmEnable_Type.__name__ = "Integer32"
_NcmdsuAlarmEnable_Object = MibTableColumn
ncmdsuAlarmEnable = _NcmdsuAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 8),
    _NcmdsuAlarmEnable_Type()
)
ncmdsuAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuAlarmEnable.setStatus("mandatory")
_NcmdsuLosLead_Type = Integer32
_NcmdsuLosLead_Object = MibTableColumn
ncmdsuLosLead = _NcmdsuLosLead_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 9),
    _NcmdsuLosLead_Type()
)
ncmdsuLosLead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuLosLead.setStatus("mandatory")


class _NcmdsuTimingSource_Type(Integer32):
    """Custom type ncmdsuTimingSource based on Integer32"""
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
        *(("cSU", 4),
          ("none", 1),
          ("port1", 2),
          ("port2", 3))
    )


_NcmdsuTimingSource_Type.__name__ = "Integer32"
_NcmdsuTimingSource_Object = MibTableColumn
ncmdsuTimingSource = _NcmdsuTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 10),
    _NcmdsuTimingSource_Type()
)
ncmdsuTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuTimingSource.setStatus("mandatory")


class _NcmdsuDTESpeed_Type(Integer32):
    """Custom type ncmdsuDTESpeed based on Integer32"""
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
        *(("mode-19-2", 5),
          ("mode-2-4", 8),
          ("mode-38-4", 4),
          ("mode-4-8", 7),
          ("mode-56k", 3),
          ("mode-64k", 2),
          ("mode-9-6", 6),
          ("none", 1))
    )


_NcmdsuDTESpeed_Type.__name__ = "Integer32"
_NcmdsuDTESpeed_Object = MibTableColumn
ncmdsuDTESpeed = _NcmdsuDTESpeed_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2001, 1, 11),
    _NcmdsuDTESpeed_Type()
)
ncmdsuDTESpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsuDTESpeed.setStatus("mandatory")
_NcmdsustatTable_Object = MibTable
ncmdsustatTable = _NcmdsustatTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003)
)
if mibBuilder.loadTexts:
    ncmdsustatTable.setStatus("mandatory")
_NcmdsustatEntry_Object = MibTableRow
ncmdsustatEntry = _NcmdsustatEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1)
)
ncmdsustatEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdsuNIDstatIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdsustatIndex"),
)
if mibBuilder.loadTexts:
    ncmdsustatEntry.setStatus("mandatory")
_NcmdsuNIDstatIndex_Type = Integer32
_NcmdsuNIDstatIndex_Object = MibTableColumn
ncmdsuNIDstatIndex = _NcmdsuNIDstatIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 1),
    _NcmdsuNIDstatIndex_Type()
)
ncmdsuNIDstatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuNIDstatIndex.setStatus("mandatory")
_NcmdsustatIndex_Type = Integer32
_NcmdsustatIndex_Object = MibTableColumn
ncmdsustatIndex = _NcmdsustatIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 2),
    _NcmdsustatIndex_Type()
)
ncmdsustatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsustatIndex.setStatus("mandatory")


class _NcmdsuPortLowbattery_Type(Integer32):
    """Custom type ncmdsuPortLowbattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low-battery", 2),
          ("not-low-battery", 1))
    )


_NcmdsuPortLowbattery_Type.__name__ = "Integer32"
_NcmdsuPortLowbattery_Object = MibTableColumn
ncmdsuPortLowbattery = _NcmdsuPortLowbattery_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 3),
    _NcmdsuPortLowbattery_Type()
)
ncmdsuPortLowbattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortLowbattery.setStatus("mandatory")


class _NcmdsuPortLOSstatus_Type(Integer32):
    """Custom type ncmdsuPortLOSstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("los-status", 2),
          ("not-Los-status", 1))
    )


_NcmdsuPortLOSstatus_Type.__name__ = "Integer32"
_NcmdsuPortLOSstatus_Object = MibTableColumn
ncmdsuPortLOSstatus = _NcmdsuPortLOSstatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 4),
    _NcmdsuPortLOSstatus_Type()
)
ncmdsuPortLOSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortLOSstatus.setStatus("mandatory")
_NcmdsuPortblockerrorcounter_Type = Gauge32
_NcmdsuPortblockerrorcounter_Object = MibTableColumn
ncmdsuPortblockerrorcounter = _NcmdsuPortblockerrorcounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 5),
    _NcmdsuPortblockerrorcounter_Type()
)
ncmdsuPortblockerrorcounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortblockerrorcounter.setStatus("mandatory")
_NcmdsuPortTestSeconds_Type = Gauge32
_NcmdsuPortTestSeconds_Object = MibTableColumn
ncmdsuPortTestSeconds = _NcmdsuPortTestSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 6),
    _NcmdsuPortTestSeconds_Type()
)
ncmdsuPortTestSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortTestSeconds.setStatus("mandatory")
_NcmdsuPortrateper8000_Type = Integer32
_NcmdsuPortrateper8000_Object = MibTableColumn
ncmdsuPortrateper8000 = _NcmdsuPortrateper8000_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 7),
    _NcmdsuPortrateper8000_Type()
)
ncmdsuPortrateper8000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortrateper8000.setStatus("mandatory")
_NcmdsuPortLeadStatus1_Type = Integer32
_NcmdsuPortLeadStatus1_Object = MibTableColumn
ncmdsuPortLeadStatus1 = _NcmdsuPortLeadStatus1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 8),
    _NcmdsuPortLeadStatus1_Type()
)
ncmdsuPortLeadStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortLeadStatus1.setStatus("mandatory")
_NcmdsuPortLeadStatus2_Type = Integer32
_NcmdsuPortLeadStatus2_Object = MibTableColumn
ncmdsuPortLeadStatus2 = _NcmdsuPortLeadStatus2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 9),
    _NcmdsuPortLeadStatus2_Type()
)
ncmdsuPortLeadStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortLeadStatus2.setStatus("mandatory")


class _NcmdbuPrimaryLineStatus_Type(Integer32):
    """Custom type ncmdbuPrimaryLineStatus based on Integer32"""
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
        *(("aLLONE", 8),
          ("aSC", 2),
          ("bER", 7),
          ("cD", 4),
          ("lOF", 3),
          ("lOS", 9),
          ("oK", 1),
          ("uSER", 5),
          ("yEL", 6))
    )


_NcmdbuPrimaryLineStatus_Type.__name__ = "Integer32"
_NcmdbuPrimaryLineStatus_Object = MibTableColumn
ncmdbuPrimaryLineStatus = _NcmdbuPrimaryLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 10),
    _NcmdbuPrimaryLineStatus_Type()
)
ncmdbuPrimaryLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuPrimaryLineStatus.setStatus("mandatory")


class _NcmdbuLineStatus_Type(Integer32):
    """Custom type ncmdbuLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aCTIVE", 2),
          ("eRROR", 3),
          ("sTANDBY", 1))
    )


_NcmdbuLineStatus_Type.__name__ = "Integer32"
_NcmdbuLineStatus_Object = MibTableColumn
ncmdbuLineStatus = _NcmdbuLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 11),
    _NcmdbuLineStatus_Type()
)
ncmdbuLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuLineStatus.setStatus("mandatory")


class _NcmdbuSwitchBy_Type(Integer32):
    """Custom type ncmdbuSwitchBy based on Integer32"""
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
        *(("aLLONE", 8),
          ("aSC", 2),
          ("bER", 7),
          ("cD", 4),
          ("lOF", 3),
          ("lOS", 9),
          ("nONE", 1),
          ("uSER", 5),
          ("yEL", 6))
    )


_NcmdbuSwitchBy_Type.__name__ = "Integer32"
_NcmdbuSwitchBy_Object = MibTableColumn
ncmdbuSwitchBy = _NcmdbuSwitchBy_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 12),
    _NcmdbuSwitchBy_Type()
)
ncmdbuSwitchBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuSwitchBy.setStatus("mandatory")
_NcmdbuReceivedCode_Type = Integer32
_NcmdbuReceivedCode_Object = MibTableColumn
ncmdbuReceivedCode = _NcmdbuReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 13),
    _NcmdbuReceivedCode_Type()
)
ncmdbuReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuReceivedCode.setStatus("mandatory")
_NcmdsuPortTestResults_Type = Integer32
_NcmdsuPortTestResults_Object = MibTableColumn
ncmdsuPortTestResults = _NcmdsuPortTestResults_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 14),
    _NcmdsuPortTestResults_Type()
)
ncmdsuPortTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortTestResults.setStatus("mandatory")
_NcmdsuPortDiagStatus_Type = Integer32
_NcmdsuPortDiagStatus_Object = MibTableColumn
ncmdsuPortDiagStatus = _NcmdsuPortDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3022, 2003, 1, 15),
    _NcmdsuPortDiagStatus_Type()
)
ncmdsuPortDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdsuPortDiagStatus.setStatus("mandatory")
_NcmdbuMainConfigTable_Object = MibTable
ncmdbuMainConfigTable = _NcmdbuMainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000)
)
if mibBuilder.loadTexts:
    ncmdbuMainConfigTable.setStatus("mandatory")
_NcmdbuMainConfigEntry_Object = MibTableRow
ncmdbuMainConfigEntry = _NcmdbuMainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1)
)
ncmdbuMainConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdbuNIDMainConfigIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdbuMainLineIndex"),
)
if mibBuilder.loadTexts:
    ncmdbuMainConfigEntry.setStatus("mandatory")


class _NcmdbuNIDMainConfigIndex_Type(Integer32):
    """Custom type ncmdbuNIDMainConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmdbuNIDMainConfigIndex_Type.__name__ = "Integer32"
_NcmdbuNIDMainConfigIndex_Object = MibTableColumn
ncmdbuNIDMainConfigIndex = _NcmdbuNIDMainConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 1),
    _NcmdbuNIDMainConfigIndex_Type()
)
ncmdbuNIDMainConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuNIDMainConfigIndex.setStatus("mandatory")
_NcmdbuMainLineIndex_Type = Integer32
_NcmdbuMainLineIndex_Object = MibTableColumn
ncmdbuMainLineIndex = _NcmdbuMainLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 2),
    _NcmdbuMainLineIndex_Type()
)
ncmdbuMainLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuMainLineIndex.setStatus("mandatory")


class _Ncmdbudsubus_Type(Integer32):
    """Custom type ncmdbudsubus based on Integer32"""
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
        *(("busA", 2),
          ("busB", 3),
          ("busC", 4),
          ("disabled", 1))
    )


_Ncmdbudsubus_Type.__name__ = "Integer32"
_Ncmdbudsubus_Object = MibTableColumn
ncmdbudsubus = _Ncmdbudsubus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 3),
    _Ncmdbudsubus_Type()
)
ncmdbudsubus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbudsubus.setStatus("mandatory")


class _NcmdbuPortChannel_Type(DisplayString):
    """Custom type ncmdbuPortChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmdbuPortChannel_Type.__name__ = "DisplayString"
_NcmdbuPortChannel_Object = MibTableColumn
ncmdbuPortChannel = _NcmdbuPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 4),
    _NcmdbuPortChannel_Type()
)
ncmdbuPortChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuPortChannel.setStatus("mandatory")
_NcmdbuPortConfiguration_Type = Integer32
_NcmdbuPortConfiguration_Object = MibTableColumn
ncmdbuPortConfiguration = _NcmdbuPortConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 5),
    _NcmdbuPortConfiguration_Type()
)
ncmdbuPortConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuPortConfiguration.setStatus("mandatory")
_Ncmdbucsushelf_Type = Integer32
_Ncmdbucsushelf_Object = MibTableColumn
ncmdbucsushelf = _Ncmdbucsushelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 6),
    _Ncmdbucsushelf_Type()
)
ncmdbucsushelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbucsushelf.setStatus("mandatory")
_Ncmdbucsuslot_Type = Integer32
_Ncmdbucsuslot_Object = MibTableColumn
ncmdbucsuslot = _Ncmdbucsuslot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 7),
    _Ncmdbucsuslot_Type()
)
ncmdbucsuslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbucsuslot.setStatus("mandatory")
_NcmdbuLosLead_Type = Integer32
_NcmdbuLosLead_Object = MibTableColumn
ncmdbuLosLead = _NcmdbuLosLead_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4000, 1, 8),
    _NcmdbuLosLead_Type()
)
ncmdbuLosLead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuLosLead.setStatus("mandatory")
_NcmdbuConfigTable_Object = MibTable
ncmdbuConfigTable = _NcmdbuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001)
)
if mibBuilder.loadTexts:
    ncmdbuConfigTable.setStatus("mandatory")
_NcmdbuConfigEntry_Object = MibTableRow
ncmdbuConfigEntry = _NcmdbuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1)
)
ncmdbuConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdbuNIDConfigIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmdbuLineIndex"),
)
if mibBuilder.loadTexts:
    ncmdbuConfigEntry.setStatus("mandatory")
_NcmdbuNIDConfigIndex_Type = Integer32
_NcmdbuNIDConfigIndex_Object = MibTableColumn
ncmdbuNIDConfigIndex = _NcmdbuNIDConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 1),
    _NcmdbuNIDConfigIndex_Type()
)
ncmdbuNIDConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuNIDConfigIndex.setStatus("mandatory")
_NcmdbuLineIndex_Type = Integer32
_NcmdbuLineIndex_Object = MibTableColumn
ncmdbuLineIndex = _NcmdbuLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 2),
    _NcmdbuLineIndex_Type()
)
ncmdbuLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmdbuLineIndex.setStatus("mandatory")
_NcmdbuAllOnesSwitchOverTime_Type = Integer32
_NcmdbuAllOnesSwitchOverTime_Object = MibTableColumn
ncmdbuAllOnesSwitchOverTime = _NcmdbuAllOnesSwitchOverTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 3),
    _NcmdbuAllOnesSwitchOverTime_Type()
)
ncmdbuAllOnesSwitchOverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuAllOnesSwitchOverTime.setStatus("mandatory")


class _NcmdbuSwitchOnBERThresholdExceeded_Type(Integer32):
    """Custom type ncmdbuSwitchOnBERThresholdExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nO", 1),
          ("yES", 2))
    )


_NcmdbuSwitchOnBERThresholdExceeded_Type.__name__ = "Integer32"
_NcmdbuSwitchOnBERThresholdExceeded_Object = MibTableColumn
ncmdbuSwitchOnBERThresholdExceeded = _NcmdbuSwitchOnBERThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 4),
    _NcmdbuSwitchOnBERThresholdExceeded_Type()
)
ncmdbuSwitchOnBERThresholdExceeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuSwitchOnBERThresholdExceeded.setStatus("mandatory")


class _NcmdbuDialBackupMode_Type(Integer32):
    """Custom type ncmdbuDialBackupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic-automatic", 2),
          ("automatic-manual", 3),
          ("manual-manual", 1))
    )


_NcmdbuDialBackupMode_Type.__name__ = "Integer32"
_NcmdbuDialBackupMode_Object = MibTableColumn
ncmdbuDialBackupMode = _NcmdbuDialBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 5),
    _NcmdbuDialBackupMode_Type()
)
ncmdbuDialBackupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuDialBackupMode.setStatus("mandatory")


class _NcmdbuBackupConnection_Type(Integer32):
    """Custom type ncmdbuBackupConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 3),
          ("deactivate", 2),
          ("none", 1))
    )


_NcmdbuBackupConnection_Type.__name__ = "Integer32"
_NcmdbuBackupConnection_Object = MibTableColumn
ncmdbuBackupConnection = _NcmdbuBackupConnection_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 6),
    _NcmdbuBackupConnection_Type()
)
ncmdbuBackupConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuBackupConnection.setStatus("mandatory")


class _Ncmdbumode_Type(Integer32):
    """Custom type ncmdbumode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode-56k", 1),
          ("mode-56kncmdds", 3),
          ("mode-64k", 2))
    )


_Ncmdbumode_Type.__name__ = "Integer32"
_Ncmdbumode_Object = MibTableColumn
ncmdbumode = _Ncmdbumode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 7),
    _Ncmdbumode_Type()
)
ncmdbumode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbumode.setStatus("mandatory")


class _NcmdbuLoopType_Type(Integer32):
    """Custom type ncmdbuLoopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("fT1", 1)
    )


_NcmdbuLoopType_Type.__name__ = "Integer32"
_NcmdbuLoopType_Object = MibTableColumn
ncmdbuLoopType = _NcmdbuLoopType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3023, 4001, 1, 8),
    _NcmdbuLoopType_Type()
)
ncmdbuLoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdbuLoopType.setStatus("mandatory")
_NcmddsMainConfigTable_Object = MibTable
ncmddsMainConfigTable = _NcmddsMainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000)
)
if mibBuilder.loadTexts:
    ncmddsMainConfigTable.setStatus("mandatory")
_NcmddsMainConfigEntry_Object = MibTableRow
ncmddsMainConfigEntry = _NcmddsMainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1)
)
ncmddsMainConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmddsNIDMainConfigIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmddsMainLineIndex"),
)
if mibBuilder.loadTexts:
    ncmddsMainConfigEntry.setStatus("mandatory")


class _NcmddsNIDMainConfigIndex_Type(Integer32):
    """Custom type ncmddsNIDMainConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmddsNIDMainConfigIndex_Type.__name__ = "Integer32"
_NcmddsNIDMainConfigIndex_Object = MibTableColumn
ncmddsNIDMainConfigIndex = _NcmddsNIDMainConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 1),
    _NcmddsNIDMainConfigIndex_Type()
)
ncmddsNIDMainConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmddsNIDMainConfigIndex.setStatus("mandatory")
_NcmddsMainLineIndex_Type = Integer32
_NcmddsMainLineIndex_Object = MibTableColumn
ncmddsMainLineIndex = _NcmddsMainLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 2),
    _NcmddsMainLineIndex_Type()
)
ncmddsMainLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmddsMainLineIndex.setStatus("mandatory")


class _Ncmddsdsubus_Type(Integer32):
    """Custom type ncmddsdsubus based on Integer32"""
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
        *(("busA", 2),
          ("busB", 3),
          ("busC", 4),
          ("disabled", 1))
    )


_Ncmddsdsubus_Type.__name__ = "Integer32"
_Ncmddsdsubus_Object = MibTableColumn
ncmddsdsubus = _Ncmddsdsubus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 3),
    _Ncmddsdsubus_Type()
)
ncmddsdsubus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsdsubus.setStatus("mandatory")


class _NcmddsPortChannel_Type(DisplayString):
    """Custom type ncmddsPortChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmddsPortChannel_Type.__name__ = "DisplayString"
_NcmddsPortChannel_Object = MibTableColumn
ncmddsPortChannel = _NcmddsPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 4),
    _NcmddsPortChannel_Type()
)
ncmddsPortChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortChannel.setStatus("mandatory")
_NcmddsPortConfiguration_Type = Integer32
_NcmddsPortConfiguration_Object = MibTableColumn
ncmddsPortConfiguration = _NcmddsPortConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 5),
    _NcmddsPortConfiguration_Type()
)
ncmddsPortConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortConfiguration.setStatus("mandatory")
_Ncmddscsushelf_Type = Integer32
_Ncmddscsushelf_Object = MibTableColumn
ncmddscsushelf = _Ncmddscsushelf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 6),
    _Ncmddscsushelf_Type()
)
ncmddscsushelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddscsushelf.setStatus("mandatory")
_Ncmddscsuslot_Type = Integer32
_Ncmddscsuslot_Object = MibTableColumn
ncmddscsuslot = _Ncmddscsuslot_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 7),
    _Ncmddscsuslot_Type()
)
ncmddscsuslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddscsuslot.setStatus("mandatory")
_NcmddsLosLead_Type = Integer32
_NcmddsLosLead_Object = MibTableColumn
ncmddsLosLead = _NcmddsLosLead_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5000, 1, 8),
    _NcmddsLosLead_Type()
)
ncmddsLosLead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsLosLead.setStatus("mandatory")
_NcmddsConfigTable_Object = MibTable
ncmddsConfigTable = _NcmddsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001)
)
if mibBuilder.loadTexts:
    ncmddsConfigTable.setStatus("mandatory")
_NcmddsConfigEntry_Object = MibTableRow
ncmddsConfigEntry = _NcmddsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1)
)
ncmddsConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmddsNIDConfigIndex"),
    (0, "VERILINK-ENTERPRISE-NCMDSU-MIB", "ncmddsConfigLineIndex"),
)
if mibBuilder.loadTexts:
    ncmddsConfigEntry.setStatus("mandatory")
_NcmddsNIDConfigIndex_Type = Integer32
_NcmddsNIDConfigIndex_Object = MibTableColumn
ncmddsNIDConfigIndex = _NcmddsNIDConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 1),
    _NcmddsNIDConfigIndex_Type()
)
ncmddsNIDConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmddsNIDConfigIndex.setStatus("mandatory")
_NcmddsConfigLineIndex_Type = Integer32
_NcmddsConfigLineIndex_Object = MibTableColumn
ncmddsConfigLineIndex = _NcmddsConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 2),
    _NcmddsConfigLineIndex_Type()
)
ncmddsConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmddsConfigLineIndex.setStatus("mandatory")


class _NcmddsPortLoopEnable_Type(Integer32):
    """Custom type ncmddsPortLoopEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmddsPortLoopEnable_Type.__name__ = "Integer32"
_NcmddsPortLoopEnable_Object = MibTableColumn
ncmddsPortLoopEnable = _NcmddsPortLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 3),
    _NcmddsPortLoopEnable_Type()
)
ncmddsPortLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortLoopEnable.setStatus("mandatory")


class _NcmddsPortReceiveLoopCode_Type(Integer32):
    """Custom type ncmddsPortReceiveLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel", 2),
          ("dSU", 1))
    )


_NcmddsPortReceiveLoopCode_Type.__name__ = "Integer32"
_NcmddsPortReceiveLoopCode_Object = MibTableColumn
ncmddsPortReceiveLoopCode = _NcmddsPortReceiveLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 4),
    _NcmddsPortReceiveLoopCode_Type()
)
ncmddsPortReceiveLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortReceiveLoopCode.setStatus("mandatory")


class _NcmddsPortRemoteLoopCode_Type(Integer32):
    """Custom type ncmddsPortRemoteLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fTI", 2),
          ("v54", 1),
          ("verilink", 3))
    )


_NcmddsPortRemoteLoopCode_Type.__name__ = "Integer32"
_NcmddsPortRemoteLoopCode_Object = MibTableColumn
ncmddsPortRemoteLoopCode = _NcmddsPortRemoteLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 5),
    _NcmddsPortRemoteLoopCode_Type()
)
ncmddsPortRemoteLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortRemoteLoopCode.setStatus("mandatory")


class _NcmddsPortAlarmEnable_Type(Integer32):
    """Custom type ncmddsPortAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NcmddsPortAlarmEnable_Type.__name__ = "Integer32"
_NcmddsPortAlarmEnable_Object = MibTableColumn
ncmddsPortAlarmEnable = _NcmddsPortAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 6),
    _NcmddsPortAlarmEnable_Type()
)
ncmddsPortAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortAlarmEnable.setStatus("mandatory")
_NcmddsPortAlarmClearDelayTime_Type = Integer32
_NcmddsPortAlarmClearDelayTime_Object = MibTableColumn
ncmddsPortAlarmClearDelayTime = _NcmddsPortAlarmClearDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 7),
    _NcmddsPortAlarmClearDelayTime_Type()
)
ncmddsPortAlarmClearDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortAlarmClearDelayTime.setStatus("mandatory")
_NcmddsPortAbnormalStationCodeThreshold_Type = Integer32
_NcmddsPortAbnormalStationCodeThreshold_Object = MibTableColumn
ncmddsPortAbnormalStationCodeThreshold = _NcmddsPortAbnormalStationCodeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 8),
    _NcmddsPortAbnormalStationCodeThreshold_Type()
)
ncmddsPortAbnormalStationCodeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortAbnormalStationCodeThreshold.setStatus("mandatory")
_NcmddsPortControlModeIdleThreshold_Type = Integer32
_NcmddsPortControlModeIdleThreshold_Object = MibTableColumn
ncmddsPortControlModeIdleThreshold = _NcmddsPortControlModeIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 9),
    _NcmddsPortControlModeIdleThreshold_Type()
)
ncmddsPortControlModeIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortControlModeIdleThreshold.setStatus("mandatory")
_NcmddsPortMuxOutofSyncThreshold_Type = Integer32
_NcmddsPortMuxOutofSyncThreshold_Object = MibTableColumn
ncmddsPortMuxOutofSyncThreshold = _NcmddsPortMuxOutofSyncThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 10),
    _NcmddsPortMuxOutofSyncThreshold_Type()
)
ncmddsPortMuxOutofSyncThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortMuxOutofSyncThreshold.setStatus("mandatory")
_NcmddsPortUnAssignedMuxChannelThreshold_Type = Integer32
_NcmddsPortUnAssignedMuxChannelThreshold_Object = MibTableColumn
ncmddsPortUnAssignedMuxChannelThreshold = _NcmddsPortUnAssignedMuxChannelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 11),
    _NcmddsPortUnAssignedMuxChannelThreshold_Type()
)
ncmddsPortUnAssignedMuxChannelThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortUnAssignedMuxChannelThreshold.setStatus("mandatory")
_NcmddsPortGroup1Codes_Type = Integer32
_NcmddsPortGroup1Codes_Object = MibTableColumn
ncmddsPortGroup1Codes = _NcmddsPortGroup1Codes_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 12),
    _NcmddsPortGroup1Codes_Type()
)
ncmddsPortGroup1Codes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsPortGroup1Codes.setStatus("mandatory")
_NcmddsPort56KStatus_Type = Integer32
_NcmddsPort56KStatus_Object = MibTableColumn
ncmddsPort56KStatus = _NcmddsPort56KStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 13),
    _NcmddsPort56KStatus_Type()
)
ncmddsPort56KStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmddsPort56KStatus.setStatus("mandatory")


class _NcmddsPortReceived56KCode_Type(Integer32):
    """Custom type ncmddsPortReceived56KCode based on Integer32"""
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
        *(("asc", 9),
          ("bl", 6),
          ("cmi", 11),
          ("fev", 8),
          ("lbe", 7),
          ("ma", 4),
          ("oos", 10),
          ("rc", 5),
          ("ta", 3),
          ("tc", 12),
          ("tip", 2),
          ("umc", 1))
    )


_NcmddsPortReceived56KCode_Type.__name__ = "Integer32"
_NcmddsPortReceived56KCode_Object = MibTableColumn
ncmddsPortReceived56KCode = _NcmddsPortReceived56KCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 14),
    _NcmddsPortReceived56KCode_Type()
)
ncmddsPortReceived56KCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmddsPortReceived56KCode.setStatus("mandatory")


class _Ncmddsmode_Type(Integer32):
    """Custom type ncmddsmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode-56k", 1),
          ("mode-56kncmdds", 3),
          ("mode-64k", 2))
    )


_Ncmddsmode_Type.__name__ = "Integer32"
_Ncmddsmode_Object = MibTableColumn
ncmddsmode = _Ncmddsmode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 15),
    _Ncmddsmode_Type()
)
ncmddsmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsmode.setStatus("mandatory")


class _NcmddsLatchingLoopbackType_Type(Integer32):
    """Custom type ncmddsLatchingLoopbackType based on Integer32"""
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
        *(("chan-loop-dn", 4),
          ("chan-loop-up", 1),
          ("dsu-loop-up", 2),
          ("none", 5),
          ("ocu-loop-up", 3))
    )


_NcmddsLatchingLoopbackType_Type.__name__ = "Integer32"
_NcmddsLatchingLoopbackType_Object = MibTableColumn
ncmddsLatchingLoopbackType = _NcmddsLatchingLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 16),
    _NcmddsLatchingLoopbackType_Type()
)
ncmddsLatchingLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsLatchingLoopbackType.setStatus("mandatory")
_NcmddsLatchingLoopbackDevNo_Type = Integer32
_NcmddsLatchingLoopbackDevNo_Object = MibTableColumn
ncmddsLatchingLoopbackDevNo = _NcmddsLatchingLoopbackDevNo_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3024, 5001, 1, 17),
    _NcmddsLatchingLoopbackDevNo_Type()
)
ncmddsLatchingLoopbackDevNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmddsLatchingLoopbackDevNo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMDSU-MIB",
    **{"ncmdsuCommonTable": ncmdsuCommonTable,
       "ncmdsuCommonEntry": ncmdsuCommonEntry,
       "ncmdsuNIDIndex": ncmdsuNIDIndex,
       "ncmdsuIndex": ncmdsuIndex,
       "ncmdsuPortType": ncmdsuPortType,
       "ncmdsuPortLoopback": ncmdsuPortLoopback,
       "ncmdsuPortTest": ncmdsuPortTest,
       "ncmdsuConfigTable": ncmdsuConfigTable,
       "ncmdsuConfigEntry": ncmdsuConfigEntry,
       "ncmdsuNIDConfigIndex": ncmdsuNIDConfigIndex,
       "ncmdsuLineIndex": ncmdsuLineIndex,
       "ncmdsubus": ncmdsubus,
       "ncmdsuPortChannel": ncmdsuPortChannel,
       "ncmdsuPortConfiguration": ncmdsuPortConfiguration,
       "ncmcsushelf": ncmcsushelf,
       "ncmcsuslot": ncmcsuslot,
       "ncmdsuAlarmEnable": ncmdsuAlarmEnable,
       "ncmdsuLosLead": ncmdsuLosLead,
       "ncmdsuTimingSource": ncmdsuTimingSource,
       "ncmdsuDTESpeed": ncmdsuDTESpeed,
       "ncmdsustatTable": ncmdsustatTable,
       "ncmdsustatEntry": ncmdsustatEntry,
       "ncmdsuNIDstatIndex": ncmdsuNIDstatIndex,
       "ncmdsustatIndex": ncmdsustatIndex,
       "ncmdsuPortLowbattery": ncmdsuPortLowbattery,
       "ncmdsuPortLOSstatus": ncmdsuPortLOSstatus,
       "ncmdsuPortblockerrorcounter": ncmdsuPortblockerrorcounter,
       "ncmdsuPortTestSeconds": ncmdsuPortTestSeconds,
       "ncmdsuPortrateper8000": ncmdsuPortrateper8000,
       "ncmdsuPortLeadStatus1": ncmdsuPortLeadStatus1,
       "ncmdsuPortLeadStatus2": ncmdsuPortLeadStatus2,
       "ncmdbuPrimaryLineStatus": ncmdbuPrimaryLineStatus,
       "ncmdbuLineStatus": ncmdbuLineStatus,
       "ncmdbuSwitchBy": ncmdbuSwitchBy,
       "ncmdbuReceivedCode": ncmdbuReceivedCode,
       "ncmdsuPortTestResults": ncmdsuPortTestResults,
       "ncmdsuPortDiagStatus": ncmdsuPortDiagStatus,
       "ncmdbuMainConfigTable": ncmdbuMainConfigTable,
       "ncmdbuMainConfigEntry": ncmdbuMainConfigEntry,
       "ncmdbuNIDMainConfigIndex": ncmdbuNIDMainConfigIndex,
       "ncmdbuMainLineIndex": ncmdbuMainLineIndex,
       "ncmdbudsubus": ncmdbudsubus,
       "ncmdbuPortChannel": ncmdbuPortChannel,
       "ncmdbuPortConfiguration": ncmdbuPortConfiguration,
       "ncmdbucsushelf": ncmdbucsushelf,
       "ncmdbucsuslot": ncmdbucsuslot,
       "ncmdbuLosLead": ncmdbuLosLead,
       "ncmdbuConfigTable": ncmdbuConfigTable,
       "ncmdbuConfigEntry": ncmdbuConfigEntry,
       "ncmdbuNIDConfigIndex": ncmdbuNIDConfigIndex,
       "ncmdbuLineIndex": ncmdbuLineIndex,
       "ncmdbuAllOnesSwitchOverTime": ncmdbuAllOnesSwitchOverTime,
       "ncmdbuSwitchOnBERThresholdExceeded": ncmdbuSwitchOnBERThresholdExceeded,
       "ncmdbuDialBackupMode": ncmdbuDialBackupMode,
       "ncmdbuBackupConnection": ncmdbuBackupConnection,
       "ncmdbumode": ncmdbumode,
       "ncmdbuLoopType": ncmdbuLoopType,
       "ncmddsMainConfigTable": ncmddsMainConfigTable,
       "ncmddsMainConfigEntry": ncmddsMainConfigEntry,
       "ncmddsNIDMainConfigIndex": ncmddsNIDMainConfigIndex,
       "ncmddsMainLineIndex": ncmddsMainLineIndex,
       "ncmddsdsubus": ncmddsdsubus,
       "ncmddsPortChannel": ncmddsPortChannel,
       "ncmddsPortConfiguration": ncmddsPortConfiguration,
       "ncmddscsushelf": ncmddscsushelf,
       "ncmddscsuslot": ncmddscsuslot,
       "ncmddsLosLead": ncmddsLosLead,
       "ncmddsConfigTable": ncmddsConfigTable,
       "ncmddsConfigEntry": ncmddsConfigEntry,
       "ncmddsNIDConfigIndex": ncmddsNIDConfigIndex,
       "ncmddsConfigLineIndex": ncmddsConfigLineIndex,
       "ncmddsPortLoopEnable": ncmddsPortLoopEnable,
       "ncmddsPortReceiveLoopCode": ncmddsPortReceiveLoopCode,
       "ncmddsPortRemoteLoopCode": ncmddsPortRemoteLoopCode,
       "ncmddsPortAlarmEnable": ncmddsPortAlarmEnable,
       "ncmddsPortAlarmClearDelayTime": ncmddsPortAlarmClearDelayTime,
       "ncmddsPortAbnormalStationCodeThreshold": ncmddsPortAbnormalStationCodeThreshold,
       "ncmddsPortControlModeIdleThreshold": ncmddsPortControlModeIdleThreshold,
       "ncmddsPortMuxOutofSyncThreshold": ncmddsPortMuxOutofSyncThreshold,
       "ncmddsPortUnAssignedMuxChannelThreshold": ncmddsPortUnAssignedMuxChannelThreshold,
       "ncmddsPortGroup1Codes": ncmddsPortGroup1Codes,
       "ncmddsPort56KStatus": ncmddsPort56KStatus,
       "ncmddsPortReceived56KCode": ncmddsPortReceived56KCode,
       "ncmddsmode": ncmddsmode,
       "ncmddsLatchingLoopbackType": ncmddsLatchingLoopbackType,
       "ncmddsLatchingLoopbackDevNo": ncmddsLatchingLoopbackDevNo}
)
