# SNMP MIB module (NOKIA-UNITTYPES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-UNITTYPES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:44 2024
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

(ntcCommonModules,
 ntcHWUnitTypeMibs) = mibBuilder.importSymbols(
    "NOKIA-COMMON-MIB-OID-REGISTRATION-MIB",
    "ntcCommonModules",
    "ntcHWUnitTypeMibs")

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


# MODULE-IDENTITY

ntcHWUnitTypeModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 3)
)
ntcHWUnitTypeModule.setRevisions(
        ("1998-09-24 00:00",
         "1998-10-04 00:00",
         "1998-11-25 00:00",
         "1998-12-03 00:00",
         "1999-10-18 00:00",
         "1901-03-14 00:00",
         "1902-02-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcHWUnitNone_ObjectIdentity = ObjectIdentity
ntcHWUnitNone = _NtcHWUnitNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 1)
)
_NtcHWUnitAny_ObjectIdentity = ObjectIdentity
ntcHWUnitAny = _NtcHWUnitAny_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 2)
)
_NtcHWUnitIanNcaStm1Electrical_ObjectIdentity = ObjectIdentity
ntcHWUnitIanNcaStm1Electrical = _NtcHWUnitIanNcaStm1Electrical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 3)
)
_NtcHWUnitNcaStm1SingleModeOptical_ObjectIdentity = ObjectIdentity
ntcHWUnitNcaStm1SingleModeOptical = _NtcHWUnitNcaStm1SingleModeOptical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 4)
)
_NtcHWUnitNcaStm1MultiModeOptical_ObjectIdentity = ObjectIdentity
ntcHWUnitNcaStm1MultiModeOptical = _NtcHWUnitNcaStm1MultiModeOptical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 5)
)
_NtcHWUnitIanASU_ObjectIdentity = ObjectIdentity
ntcHWUnitIanASU = _NtcHWUnitIanASU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 6)
)
_NtcHWUnitIan4PortV35_ObjectIdentity = ObjectIdentity
ntcHWUnitIan4PortV35 = _NtcHWUnitIan4PortV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 7)
)
_NtcHWUnitIan4PortE1_ObjectIdentity = ObjectIdentity
ntcHWUnitIan4PortE1 = _NtcHWUnitIan4PortE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 8)
)
_NtcHWUnitIan4PortMsdsl_ObjectIdentity = ObjectIdentity
ntcHWUnitIan4PortMsdsl = _NtcHWUnitIan4PortMsdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 9)
)
_NtcHWUnitIanIpFwrdingUnit_ObjectIdentity = ObjectIdentity
ntcHWUnitIanIpFwrdingUnit = _NtcHWUnitIanIpFwrdingUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 10)
)
_NtcHWUnitBbanAlbaStm1E_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanAlbaStm1E = _NtcHWUnitBbanAlbaStm1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 11)
)
_NtcHWUnitBbanAlbaStm1Om_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanAlbaStm1Om = _NtcHWUnitBbanAlbaStm1Om_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 12)
)
_NtcHWUnitBbanAlbaStm1Os_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanAlbaStm1Os = _NtcHWUnitBbanAlbaStm1Os_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 13)
)
_NtcHWUnitBbanAlbaE3_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanAlbaE3 = _NtcHWUnitBbanAlbaE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 14)
)
_NtcHWUnitBbanSliuAdslMiDmt_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanSliuAdslMiDmt = _NtcHWUnitBbanSliuAdslMiDmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 15)
)
_NtcHWUnitBbanSliuAdslAdDmt_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanSliuAdslAdDmt = _NtcHWUnitBbanSliuAdslAdDmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 16)
)
_NtcHWUnitBbanSliuE1I75_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanSliuE1I75 = _NtcHWUnitBbanSliuE1I75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 17)
)
_NtcHWUnitBbanSliuE1I120_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanSliuE1I120 = _NtcHWUnitBbanSliuE1I120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 18)
)
_NtcHWUnitBbanBackplane8_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanBackplane8 = _NtcHWUnitBbanBackplane8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 19)
)
_NtcHWUnitBbanBackplane17_ObjectIdentity = ObjectIdentity
ntcHWUnitBbanBackplane17 = _NtcHWUnitBbanBackplane17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 20)
)
_NtcHWSlot_ObjectIdentity = ObjectIdentity
ntcHWSlot = _NtcHWSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 21)
)
_NtcHWBackplane_ObjectIdentity = ObjectIdentity
ntcHWBackplane = _NtcHWBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 22)
)
_NtcHWUnitIprgSeqCrp_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgSeqCrp = _NtcHWUnitIprgSeqCrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 23)
)
_NtcHWUnitIprgSeqGplc1_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgSeqGplc1 = _NtcHWUnitIprgSeqGplc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 24)
)
_NtcHWUnitIprgSeqGplc2_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgSeqGplc2 = _NtcHWUnitIprgSeqGplc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 25)
)
_NtcHWUnitIprgSeqWslc_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgSeqWslc = _NtcHWUnitIprgSeqWslc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 26)
)
_NtcHWUnitIprgEth1_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgEth1 = _NtcHWUnitIprgEth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 27)
)
_NtcHWUnitIprgEth2_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgEth2 = _NtcHWUnitIprgEth2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 28)
)
_NtcHWUnitIprgEth4_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgEth4 = _NtcHWUnitIprgEth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 29)
)
_NtcHWUnitIprgAtm_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgAtm = _NtcHWUnitIprgAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 30)
)
_NtcHWUnitIprgX211_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgX211 = _NtcHWUnitIprgX211_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 31)
)
_NtcHWUnitIprgV351_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgV351 = _NtcHWUnitIprgV351_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 32)
)
_NtcHWUnitIprgX212_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgX212 = _NtcHWUnitIprgX212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 33)
)
_NtcHWUnitIprgV352_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgV352 = _NtcHWUnitIprgV352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 34)
)
_NtcHWUnitIprgHssi_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgHssi = _NtcHWUnitIprgHssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 35)
)
_NtcHWUnitIprgE1_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgE1 = _NtcHWUnitIprgE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 36)
)
_NtcHWUnitIprgT1_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgT1 = _NtcHWUnitIprgT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 37)
)
_NtcHWUnitIprgFddi_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgFddi = _NtcHWUnitIprgFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 38)
)
_NtcHWUnitIprgTok_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgTok = _NtcHWUnitIprgTok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 39)
)
_NtcHWUnitIprgIsdn_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgIsdn = _NtcHWUnitIprgIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 40)
)
_NtcHWUnitIprgBackplaneIP110_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneIP110 = _NtcHWUnitIprgBackplaneIP110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 41)
)
_NtcHWUnitIprgBackplaneIP330_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneIP330 = _NtcHWUnitIprgBackplaneIP330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 42)
)
_NtcHWUnitIprgBackplaneIP440_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneIP440 = _NtcHWUnitIprgBackplaneIP440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 43)
)
_NtcHWUnitIprgBackplaneIP530_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneIP530 = _NtcHWUnitIprgBackplaneIP530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 44)
)
_NtcHWUnitIprgBackplaneIP650_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneIP650 = _NtcHWUnitIprgBackplaneIP650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 45)
)
_NtcHWUnitIprgBackplaneIP730_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneIP730 = _NtcHWUnitIprgBackplaneIP730_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 46)
)
_NtcHWUnitIprgBackplaneSeq9_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneSeq9 = _NtcHWUnitIprgBackplaneSeq9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 47)
)
_NtcHWUnitIprgBackplaneSeq18_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgBackplaneSeq18 = _NtcHWUnitIprgBackplaneSeq18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 48)
)
_NtcHWUnitIprgChassisIP110_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisIP110 = _NtcHWUnitIprgChassisIP110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 49)
)
_NtcHWUnitIprgChassisIP330_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisIP330 = _NtcHWUnitIprgChassisIP330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 50)
)
_NtcHWUnitIprgChassisIP440_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisIP440 = _NtcHWUnitIprgChassisIP440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 51)
)
_NtcHWUnitIprgChassisIP530_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisIP530 = _NtcHWUnitIprgChassisIP530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 52)
)
_NtcHWUnitIprgChassisIP650_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisIP650 = _NtcHWUnitIprgChassisIP650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 53)
)
_NtcHWUnitIprgChassisIP730_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisIP730 = _NtcHWUnitIprgChassisIP730_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 54)
)
_NtcHWUnitIprgChassisSeq9_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisSeq9 = _NtcHWUnitIprgChassisSeq9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 55)
)
_NtcHWUnitIprgChassisSeq18_ObjectIdentity = ObjectIdentity
ntcHWUnitIprgChassisSeq18 = _NtcHWUnitIprgChassisSeq18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 56)
)
_NtcHWUnitIpsoGigEth1_ObjectIdentity = ObjectIdentity
ntcHWUnitIpsoGigEth1 = _NtcHWUnitIpsoGigEth1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 57)
)
_NtcHWUnitIpsoSs7_ObjectIdentity = ObjectIdentity
ntcHWUnitIpsoSs7 = _NtcHWUnitIpsoSs7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 58)
)
_NtcHWUnitIpsoCryptoAccelerator_ObjectIdentity = ObjectIdentity
ntcHWUnitIpsoCryptoAccelerator = _NtcHWUnitIpsoCryptoAccelerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 59)
)
_NtcHWUnitIpsoHardDisk_ObjectIdentity = ObjectIdentity
ntcHWUnitIpsoHardDisk = _NtcHWUnitIpsoHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3, 60)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-UNITTYPES-MIB",
    **{"ntcHWUnitTypeModule": ntcHWUnitTypeModule,
       "ntcHWUnitNone": ntcHWUnitNone,
       "ntcHWUnitAny": ntcHWUnitAny,
       "ntcHWUnitIanNcaStm1Electrical": ntcHWUnitIanNcaStm1Electrical,
       "ntcHWUnitNcaStm1SingleModeOptical": ntcHWUnitNcaStm1SingleModeOptical,
       "ntcHWUnitNcaStm1MultiModeOptical": ntcHWUnitNcaStm1MultiModeOptical,
       "ntcHWUnitIanASU": ntcHWUnitIanASU,
       "ntcHWUnitIan4PortV35": ntcHWUnitIan4PortV35,
       "ntcHWUnitIan4PortE1": ntcHWUnitIan4PortE1,
       "ntcHWUnitIan4PortMsdsl": ntcHWUnitIan4PortMsdsl,
       "ntcHWUnitIanIpFwrdingUnit": ntcHWUnitIanIpFwrdingUnit,
       "ntcHWUnitBbanAlbaStm1E": ntcHWUnitBbanAlbaStm1E,
       "ntcHWUnitBbanAlbaStm1Om": ntcHWUnitBbanAlbaStm1Om,
       "ntcHWUnitBbanAlbaStm1Os": ntcHWUnitBbanAlbaStm1Os,
       "ntcHWUnitBbanAlbaE3": ntcHWUnitBbanAlbaE3,
       "ntcHWUnitBbanSliuAdslMiDmt": ntcHWUnitBbanSliuAdslMiDmt,
       "ntcHWUnitBbanSliuAdslAdDmt": ntcHWUnitBbanSliuAdslAdDmt,
       "ntcHWUnitBbanSliuE1I75": ntcHWUnitBbanSliuE1I75,
       "ntcHWUnitBbanSliuE1I120": ntcHWUnitBbanSliuE1I120,
       "ntcHWUnitBbanBackplane8": ntcHWUnitBbanBackplane8,
       "ntcHWUnitBbanBackplane17": ntcHWUnitBbanBackplane17,
       "ntcHWSlot": ntcHWSlot,
       "ntcHWBackplane": ntcHWBackplane,
       "ntcHWUnitIprgSeqCrp": ntcHWUnitIprgSeqCrp,
       "ntcHWUnitIprgSeqGplc1": ntcHWUnitIprgSeqGplc1,
       "ntcHWUnitIprgSeqGplc2": ntcHWUnitIprgSeqGplc2,
       "ntcHWUnitIprgSeqWslc": ntcHWUnitIprgSeqWslc,
       "ntcHWUnitIprgEth1": ntcHWUnitIprgEth1,
       "ntcHWUnitIprgEth2": ntcHWUnitIprgEth2,
       "ntcHWUnitIprgEth4": ntcHWUnitIprgEth4,
       "ntcHWUnitIprgAtm": ntcHWUnitIprgAtm,
       "ntcHWUnitIprgX211": ntcHWUnitIprgX211,
       "ntcHWUnitIprgV351": ntcHWUnitIprgV351,
       "ntcHWUnitIprgX212": ntcHWUnitIprgX212,
       "ntcHWUnitIprgV352": ntcHWUnitIprgV352,
       "ntcHWUnitIprgHssi": ntcHWUnitIprgHssi,
       "ntcHWUnitIprgE1": ntcHWUnitIprgE1,
       "ntcHWUnitIprgT1": ntcHWUnitIprgT1,
       "ntcHWUnitIprgFddi": ntcHWUnitIprgFddi,
       "ntcHWUnitIprgTok": ntcHWUnitIprgTok,
       "ntcHWUnitIprgIsdn": ntcHWUnitIprgIsdn,
       "ntcHWUnitIprgBackplaneIP110": ntcHWUnitIprgBackplaneIP110,
       "ntcHWUnitIprgBackplaneIP330": ntcHWUnitIprgBackplaneIP330,
       "ntcHWUnitIprgBackplaneIP440": ntcHWUnitIprgBackplaneIP440,
       "ntcHWUnitIprgBackplaneIP530": ntcHWUnitIprgBackplaneIP530,
       "ntcHWUnitIprgBackplaneIP650": ntcHWUnitIprgBackplaneIP650,
       "ntcHWUnitIprgBackplaneIP730": ntcHWUnitIprgBackplaneIP730,
       "ntcHWUnitIprgBackplaneSeq9": ntcHWUnitIprgBackplaneSeq9,
       "ntcHWUnitIprgBackplaneSeq18": ntcHWUnitIprgBackplaneSeq18,
       "ntcHWUnitIprgChassisIP110": ntcHWUnitIprgChassisIP110,
       "ntcHWUnitIprgChassisIP330": ntcHWUnitIprgChassisIP330,
       "ntcHWUnitIprgChassisIP440": ntcHWUnitIprgChassisIP440,
       "ntcHWUnitIprgChassisIP530": ntcHWUnitIprgChassisIP530,
       "ntcHWUnitIprgChassisIP650": ntcHWUnitIprgChassisIP650,
       "ntcHWUnitIprgChassisIP730": ntcHWUnitIprgChassisIP730,
       "ntcHWUnitIprgChassisSeq9": ntcHWUnitIprgChassisSeq9,
       "ntcHWUnitIprgChassisSeq18": ntcHWUnitIprgChassisSeq18,
       "ntcHWUnitIpsoGigEth1": ntcHWUnitIpsoGigEth1,
       "ntcHWUnitIpsoSs7": ntcHWUnitIpsoSs7,
       "ntcHWUnitIpsoCryptoAccelerator": ntcHWUnitIpsoCryptoAccelerator,
       "ntcHWUnitIpsoHardDisk": ntcHWUnitIpsoHardDisk}
)
