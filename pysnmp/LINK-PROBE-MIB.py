# SNMP MIB module (LINK-PROBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LINK-PROBE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:17 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetQuest_ObjectIdentity = ObjectIdentity
netQuest = _NetQuest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568)
)
_Link_probe_ObjectIdentity = ObjectIdentity
link_probe = _Link_probe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8)
)
_ProbeConfig_ObjectIdentity = ObjectIdentity
probeConfig = _ProbeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1)
)
_Chan_config_ObjectIdentity = ObjectIdentity
chan_config = _Chan_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 1)
)


class _Lmi_Operation_Type(Integer32):
    """Custom type lmi_Operation based on Integer32"""
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


_Lmi_Operation_Type.__name__ = "Integer32"
_Lmi_Operation_Object = MibScalar
lmi_Operation = _Lmi_Operation_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 1, 1),
    _Lmi_Operation_Type()
)
lmi_Operation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmi_Operation.setStatus("mandatory")


class _Lmi_DLCI_Type(Integer32):
    """Custom type lmi_DLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc-0", 1),
          ("pvc-1023", 2))
    )


_Lmi_DLCI_Type.__name__ = "Integer32"
_Lmi_DLCI_Object = MibScalar
lmi_DLCI = _Lmi_DLCI_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 1, 2),
    _Lmi_DLCI_Type()
)
lmi_DLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmi_DLCI.setStatus("mandatory")


class _Inband_IP_DLCI_Type(Integer32):
    """Custom type inband_IP_DLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_Inband_IP_DLCI_Type.__name__ = "Integer32"
_Inband_IP_DLCI_Object = MibScalar
inband_IP_DLCI = _Inband_IP_DLCI_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 1, 3),
    _Inband_IP_DLCI_Type()
)
inband_IP_DLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inband_IP_DLCI.setStatus("mandatory")


class _Ip_Encapsu_Type(Integer32):
    """Custom type ip_Encapsu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ietf-ip", 2),
          ("raw-ip", 1),
          ("snap-ip", 3))
    )


_Ip_Encapsu_Type.__name__ = "Integer32"
_Ip_Encapsu_Object = MibScalar
ip_Encapsu = _Ip_Encapsu_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 1, 4),
    _Ip_Encapsu_Type()
)
ip_Encapsu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip_Encapsu.setStatus("mandatory")


class _Interface_Speed_Type(Integer32):
    """Custom type interface_Speed based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("n1024-kbps", 16),
          ("n1088-kbps", 17),
          ("n1152-kbps", 18),
          ("n1216-kbps", 19),
          ("n128-kbps", 2),
          ("n1280-kbps", 20),
          ("n1344-kbps", 21),
          ("n1408-kbps", 22),
          ("n1472-kbps", 23),
          ("n1536-kbps", 24),
          ("n1600-kbps", 25),
          ("n1664-kbps", 26),
          ("n1728-kbps", 27),
          ("n1792-kbps", 28),
          ("n1856-kbps", 29),
          ("n192-kbps", 3),
          ("n1920-kbps", 30),
          ("n1984-kbps", 31),
          ("n2048-kbps", 32),
          ("n256-kbps", 4),
          ("n320-kbps", 5),
          ("n384-kbps", 6),
          ("n448-kbps", 7),
          ("n512-kbps", 8),
          ("n576-kbps", 9),
          ("n64-kbps", 1),
          ("n640-kbps", 10),
          ("n704-kbps", 11),
          ("n768-kbps", 12),
          ("n832-kbps", 13),
          ("n896-kbps", 14),
          ("n960-kbps", 15))
    )


_Interface_Speed_Type.__name__ = "Integer32"
_Interface_Speed_Object = MibScalar
interface_Speed = _Interface_Speed_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 1, 5),
    _Interface_Speed_Type()
)
interface_Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interface_Speed.setStatus("mandatory")


class _Nvram_update_Type(Integer32):
    """Custom type nvram_update based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restoreParam", 2),
          ("write-to-nvram", 1))
    )


_Nvram_update_Type.__name__ = "Integer32"
_Nvram_update_Object = MibScalar
nvram_update = _Nvram_update_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 1, 6),
    _Nvram_update_Type()
)
nvram_update.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nvram_update.setStatus("mandatory")
_Lmi_config_ObjectIdentity = ObjectIdentity
lmi_config = _Lmi_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2)
)


class _Lmi_type_Type(Integer32):
    """Custom type lmi_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annex-a", 1),
          ("annex-d", 2),
          ("lmi-rev1", 3))
    )


_Lmi_type_Type.__name__ = "Integer32"
_Lmi_type_Object = MibScalar
lmi_type = _Lmi_type_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 1),
    _Lmi_type_Type()
)
lmi_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmi_type.setStatus("mandatory")


class _Max_Info_Length_Type(Integer32):
    """Custom type max_Info_Length based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 4000),
    )


_Max_Info_Length_Type.__name__ = "Integer32"
_Max_Info_Length_Object = MibScalar
max_Info_Length = _Max_Info_Length_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 2),
    _Max_Info_Length_Type()
)
max_Info_Length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    max_Info_Length.setStatus("mandatory")


class _N391_Counter_Type(Integer32):
    """Custom type n391_Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_N391_Counter_Type.__name__ = "Integer32"
_N391_Counter_Object = MibScalar
n391_Counter = _N391_Counter_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 3),
    _N391_Counter_Type()
)
n391_Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n391_Counter.setStatus("mandatory")


class _N392_Net_Counter_Type(Integer32):
    """Custom type n392_Net_Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N392_Net_Counter_Type.__name__ = "Integer32"
_N392_Net_Counter_Object = MibScalar
n392_Net_Counter = _N392_Net_Counter_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 4),
    _N392_Net_Counter_Type()
)
n392_Net_Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n392_Net_Counter.setStatus("mandatory")


class _N392_User_Counter_Type(Integer32):
    """Custom type n392_User_Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N392_User_Counter_Type.__name__ = "Integer32"
_N392_User_Counter_Object = MibScalar
n392_User_Counter = _N392_User_Counter_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 5),
    _N392_User_Counter_Type()
)
n392_User_Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n392_User_Counter.setStatus("mandatory")


class _N393_Net_Counter_Type(Integer32):
    """Custom type n393_Net_Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N393_Net_Counter_Type.__name__ = "Integer32"
_N393_Net_Counter_Object = MibScalar
n393_Net_Counter = _N393_Net_Counter_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 6),
    _N393_Net_Counter_Type()
)
n393_Net_Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n393_Net_Counter.setStatus("mandatory")


class _N393_User_Counter_Type(Integer32):
    """Custom type n393_User_Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N393_User_Counter_Type.__name__ = "Integer32"
_N393_User_Counter_Object = MibScalar
n393_User_Counter = _N393_User_Counter_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 7),
    _N393_User_Counter_Type()
)
n393_User_Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n393_User_Counter.setStatus("mandatory")


class _T391_Timer_Type(Integer32):
    """Custom type t391_Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_T391_Timer_Type.__name__ = "Integer32"
_T391_Timer_Object = MibScalar
t391_Timer = _T391_Timer_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 8),
    _T391_Timer_Type()
)
t391_Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t391_Timer.setStatus("mandatory")


class _T392_Timer_Type(Integer32):
    """Custom type t392_Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_T392_Timer_Type.__name__ = "Integer32"
_T392_Timer_Object = MibScalar
t392_Timer = _T392_Timer_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 9),
    _T392_Timer_Type()
)
t392_Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t392_Timer.setStatus("mandatory")


class _LMI_Controller_Type(Integer32):
    """Custom type lMI_Controller based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restoreParam", 2),
          ("update-para", 1))
    )


_LMI_Controller_Type.__name__ = "Integer32"
_LMI_Controller_Object = MibScalar
lMI_Controller = _LMI_Controller_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 2, 10),
    _LMI_Controller_Type()
)
lMI_Controller.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lMI_Controller.setStatus("mandatory")
_Pro_fun_config_ObjectIdentity = ObjectIdentity
pro_fun_config = _Pro_fun_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3)
)


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("mandatory")


class _Probe_Mode_Type(Integer32):
    """Custom type probe_Mode based on Integer32"""
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
        *(("both", 3),
          ("disabled", 4),
          ("generator", 1),
          ("responder", 2))
    )


_Probe_Mode_Type.__name__ = "Integer32"
_Probe_Mode_Object = MibScalar
probe_Mode = _Probe_Mode_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 2),
    _Probe_Mode_Type()
)
probe_Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe_Mode.setStatus("mandatory")


class _Poll_Period_Type(Integer32):
    """Custom type poll_Period based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Poll_Period_Type.__name__ = "Integer32"
_Poll_Period_Object = MibScalar
poll_Period = _Poll_Period_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 3),
    _Poll_Period_Type()
)
poll_Period.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poll_Period.setStatus("mandatory")


class _Sys_current_time_Type(DisplayString):
    """Custom type sys_current_time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Sys_current_time_Type.__name__ = "DisplayString"
_Sys_current_time_Object = MibScalar
sys_current_time = _Sys_current_time_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 4),
    _Sys_current_time_Type()
)
sys_current_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sys_current_time.setStatus("mandatory")


class _Current_intv_start_time_Type(DisplayString):
    """Custom type current_intv_start_time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Current_intv_start_time_Type.__name__ = "DisplayString"
_Current_intv_start_time_Object = MibScalar
current_intv_start_time = _Current_intv_start_time_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 5),
    _Current_intv_start_time_Type()
)
current_intv_start_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_intv_start_time.setStatus("mandatory")


class _Pvc_Count_Type(Integer32):
    """Custom type pvc_Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Pvc_Count_Type.__name__ = "Integer32"
_Pvc_Count_Object = MibScalar
pvc_Count = _Pvc_Count_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 6),
    _Pvc_Count_Type()
)
pvc_Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_Count.setStatus("mandatory")


class _ProbeTokenSize_Type(Integer32):
    """Custom type probeTokenSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19, 4096),
    )


_ProbeTokenSize_Type.__name__ = "Integer32"
_ProbeTokenSize_Object = MibScalar
probeTokenSize = _ProbeTokenSize_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 7),
    _ProbeTokenSize_Type()
)
probeTokenSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeTokenSize.setStatus("mandatory")


class _Pvc_add_Type(Integer32):
    """Custom type pvc_add based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_Pvc_add_Type.__name__ = "Integer32"
_Pvc_add_Object = MibScalar
pvc_add = _Pvc_add_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 8),
    _Pvc_add_Type()
)
pvc_add.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pvc_add.setStatus("mandatory")


class _Pvc_delete_Type(Integer32):
    """Custom type pvc_delete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_Pvc_delete_Type.__name__ = "Integer32"
_Pvc_delete_Object = MibScalar
pvc_delete = _Pvc_delete_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 9),
    _Pvc_delete_Type()
)
pvc_delete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pvc_delete.setStatus("mandatory")
_Pvc_Table_Object = MibTable
pvc_Table = _Pvc_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 10)
)
if mibBuilder.loadTexts:
    pvc_Table.setStatus("mandatory")
_Pvc_Entry_Object = MibTableRow
pvc_Entry = _Pvc_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 10, 1)
)
pvc_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvc-Table-Index"),
)
if mibBuilder.loadTexts:
    pvc_Entry.setStatus("mandatory")


class _Pvc_Table_Index_Type(Integer32):
    """Custom type pvc_Table_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_Pvc_Table_Index_Type.__name__ = "Integer32"
_Pvc_Table_Index_Object = MibScalar
pvc_Table_Index = _Pvc_Table_Index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 10, 1, 1),
    _Pvc_Table_Index_Type()
)
pvc_Table_Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_Table_Index.setStatus("mandatory")


class _Pvc_Operation_Type(Integer32):
    """Custom type pvc_Operation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pvc-in-waiting", 2),
          ("pvc-not-probed", 1),
          ("pvc-probed", 3))
    )


_Pvc_Operation_Type.__name__ = "Integer32"
_Pvc_Operation_Object = MibScalar
pvc_Operation = _Pvc_Operation_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 10, 1, 2),
    _Pvc_Operation_Type()
)
pvc_Operation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvc_Operation.setStatus("mandatory")
_Pvc_Remote_IpAddress_Type = IpAddress
_Pvc_Remote_IpAddress_Object = MibScalar
pvc_Remote_IpAddress = _Pvc_Remote_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 10, 1, 3),
    _Pvc_Remote_IpAddress_Type()
)
pvc_Remote_IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_Remote_IpAddress.setStatus("mandatory")


class _AlternateVersion_Type(DisplayString):
    """Custom type alternateVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AlternateVersion_Type.__name__ = "DisplayString"
_AlternateVersion_Object = MibScalar
alternateVersion = _AlternateVersion_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 11),
    _AlternateVersion_Type()
)
alternateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternateVersion.setStatus("mandatory")


class _BypassStatus_Type(Integer32):
    """Custom type bypassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypass-auto", 3),
          ("bypass-off", 1),
          ("bypass-on", 2))
    )


_BypassStatus_Type.__name__ = "Integer32"
_BypassStatus_Object = MibScalar
bypassStatus = _BypassStatus_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 3, 12),
    _BypassStatus_Type()
)
bypassStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bypassStatus.setStatus("mandatory")
_Trap_config_ObjectIdentity = ObjectIdentity
trap_config = _Trap_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4)
)


class _TrapCtlGlobal_Type(Integer32):
    """Custom type trapCtlGlobal based on Integer32"""
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


_TrapCtlGlobal_Type.__name__ = "Integer32"
_TrapCtlGlobal_Object = MibScalar
trapCtlGlobal = _TrapCtlGlobal_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 1),
    _TrapCtlGlobal_Type()
)
trapCtlGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCtlGlobal.setStatus("mandatory")


class _TrapCtlSpecific_Type(Integer32):
    """Custom type trapCtlSpecific based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapCtlSpecific_Type.__name__ = "Integer32"
_TrapCtlSpecific_Object = MibScalar
trapCtlSpecific = _TrapCtlSpecific_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 2),
    _TrapCtlSpecific_Type()
)
trapCtlSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCtlSpecific.setStatus("mandatory")


class _PvcNotAvailThreshDCE_Type(Integer32):
    """Custom type pvcNotAvailThreshDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcNotAvailThreshDCE_Type.__name__ = "Integer32"
_PvcNotAvailThreshDCE_Object = MibScalar
pvcNotAvailThreshDCE = _PvcNotAvailThreshDCE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 3),
    _PvcNotAvailThreshDCE_Type()
)
pvcNotAvailThreshDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcNotAvailThreshDCE.setStatus("mandatory")


class _PvcNotAvailThreshDTE_Type(Integer32):
    """Custom type pvcNotAvailThreshDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcNotAvailThreshDTE_Type.__name__ = "Integer32"
_PvcNotAvailThreshDTE_Object = MibScalar
pvcNotAvailThreshDTE = _PvcNotAvailThreshDTE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 4),
    _PvcNotAvailThreshDTE_Type()
)
pvcNotAvailThreshDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcNotAvailThreshDTE.setStatus("mandatory")


class _PvcAveRTDThresh_Type(Integer32):
    """Custom type pvcAveRTDThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_PvcAveRTDThresh_Type.__name__ = "Integer32"
_PvcAveRTDThresh_Object = MibScalar
pvcAveRTDThresh = _PvcAveRTDThresh_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 5),
    _PvcAveRTDThresh_Type()
)
pvcAveRTDThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcAveRTDThresh.setStatus("mandatory")


class _FrChanUtilizThreshToDTE_Type(Integer32):
    """Custom type frChanUtilizThreshToDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_FrChanUtilizThreshToDTE_Type.__name__ = "Integer32"
_FrChanUtilizThreshToDTE_Object = MibScalar
frChanUtilizThreshToDTE = _FrChanUtilizThreshToDTE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 6),
    _FrChanUtilizThreshToDTE_Type()
)
frChanUtilizThreshToDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanUtilizThreshToDTE.setStatus("mandatory")


class _FrChanUtilizThreshToDCE_Type(Integer32):
    """Custom type frChanUtilizThreshToDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_FrChanUtilizThreshToDCE_Type.__name__ = "Integer32"
_FrChanUtilizThreshToDCE_Object = MibScalar
frChanUtilizThreshToDCE = _FrChanUtilizThreshToDCE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 7),
    _FrChanUtilizThreshToDCE_Type()
)
frChanUtilizThreshToDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanUtilizThreshToDCE.setStatus("mandatory")


class _PvcBecnThresh_Type(Integer32):
    """Custom type pvcBecnThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PvcBecnThresh_Type.__name__ = "Integer32"
_PvcBecnThresh_Object = MibScalar
pvcBecnThresh = _PvcBecnThresh_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 8),
    _PvcBecnThresh_Type()
)
pvcBecnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcBecnThresh.setStatus("mandatory")


class _PvcFecnThresh_Type(Integer32):
    """Custom type pvcFecnThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PvcFecnThresh_Type.__name__ = "Integer32"
_PvcFecnThresh_Object = MibScalar
pvcFecnThresh = _PvcFecnThresh_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 9),
    _PvcFecnThresh_Type()
)
pvcFecnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcFecnThresh.setStatus("mandatory")


class _PvcUtilToDTEThresh_Type(Integer32):
    """Custom type pvcUtilToDTEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PvcUtilToDTEThresh_Type.__name__ = "Integer32"
_PvcUtilToDTEThresh_Object = MibScalar
pvcUtilToDTEThresh = _PvcUtilToDTEThresh_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 10),
    _PvcUtilToDTEThresh_Type()
)
pvcUtilToDTEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUtilToDTEThresh.setStatus("mandatory")


class _PvcUtilToDCEThresh_Type(Integer32):
    """Custom type pvcUtilToDCEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PvcUtilToDCEThresh_Type.__name__ = "Integer32"
_PvcUtilToDCEThresh_Object = MibScalar
pvcUtilToDCEThresh = _PvcUtilToDCEThresh_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 11),
    _PvcUtilToDCEThresh_Type()
)
pvcUtilToDCEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUtilToDCEThresh.setStatus("mandatory")


class _ChanLoadToDTEThresh_realTime_Type(Integer32):
    """Custom type chanLoadToDTEThresh_realTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ChanLoadToDTEThresh_realTime_Type.__name__ = "Integer32"
_ChanLoadToDTEThresh_realTime_Object = MibScalar
chanLoadToDTEThresh_realTime = _ChanLoadToDTEThresh_realTime_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 12),
    _ChanLoadToDTEThresh_realTime_Type()
)
chanLoadToDTEThresh_realTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanLoadToDTEThresh_realTime.setStatus("mandatory")


class _ChanLoadToDCEThresh_realTime_Type(Integer32):
    """Custom type chanLoadToDCEThresh_realTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ChanLoadToDCEThresh_realTime_Type.__name__ = "Integer32"
_ChanLoadToDCEThresh_realTime_Object = MibScalar
chanLoadToDCEThresh_realTime = _ChanLoadToDCEThresh_realTime_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 13),
    _ChanLoadToDCEThresh_realTime_Type()
)
chanLoadToDCEThresh_realTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanLoadToDCEThresh_realTime.setStatus("mandatory")


class _ChanLoadThreshToDTE_realTimeRange_Type(Integer32):
    """Custom type chanLoadThreshToDTE_realTimeRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChanLoadThreshToDTE_realTimeRange_Type.__name__ = "Integer32"
_ChanLoadThreshToDTE_realTimeRange_Object = MibScalar
chanLoadThreshToDTE_realTimeRange = _ChanLoadThreshToDTE_realTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 14),
    _ChanLoadThreshToDTE_realTimeRange_Type()
)
chanLoadThreshToDTE_realTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanLoadThreshToDTE_realTimeRange.setStatus("mandatory")


class _ChanLoadThreshToDCE_realTimeRange_Type(Integer32):
    """Custom type chanLoadThreshToDCE_realTimeRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChanLoadThreshToDCE_realTimeRange_Type.__name__ = "Integer32"
_ChanLoadThreshToDCE_realTimeRange_Object = MibScalar
chanLoadThreshToDCE_realTimeRange = _ChanLoadThreshToDCE_realTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 15),
    _ChanLoadThreshToDCE_realTimeRange_Type()
)
chanLoadThreshToDCE_realTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanLoadThreshToDCE_realTimeRange.setStatus("mandatory")


class _PvcRTDThresh_realTime_Type(Integer32):
    """Custom type pvcRTDThresh_realTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PvcRTDThresh_realTime_Type.__name__ = "Integer32"
_PvcRTDThresh_realTime_Object = MibScalar
pvcRTDThresh_realTime = _PvcRTDThresh_realTime_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 16),
    _PvcRTDThresh_realTime_Type()
)
pvcRTDThresh_realTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRTDThresh_realTime.setStatus("mandatory")


class _PvcRTDThresh_realTimeRange_Type(Integer32):
    """Custom type pvcRTDThresh_realTimeRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcRTDThresh_realTimeRange_Type.__name__ = "Integer32"
_PvcRTDThresh_realTimeRange_Object = MibScalar
pvcRTDThresh_realTimeRange = _PvcRTDThresh_realTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 17),
    _PvcRTDThresh_realTimeRange_Type()
)
pvcRTDThresh_realTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRTDThresh_realTimeRange.setStatus("mandatory")


class _PvcLoadToDTEThresh_realTime_Type(Integer32):
    """Custom type pvcLoadToDTEThresh_realTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PvcLoadToDTEThresh_realTime_Type.__name__ = "Integer32"
_PvcLoadToDTEThresh_realTime_Object = MibScalar
pvcLoadToDTEThresh_realTime = _PvcLoadToDTEThresh_realTime_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 18),
    _PvcLoadToDTEThresh_realTime_Type()
)
pvcLoadToDTEThresh_realTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcLoadToDTEThresh_realTime.setStatus("mandatory")


class _PvcLoadToDCEThresh_realTime_Type(Integer32):
    """Custom type pvcLoadToDCEThresh_realTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PvcLoadToDCEThresh_realTime_Type.__name__ = "Integer32"
_PvcLoadToDCEThresh_realTime_Object = MibScalar
pvcLoadToDCEThresh_realTime = _PvcLoadToDCEThresh_realTime_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 19),
    _PvcLoadToDCEThresh_realTime_Type()
)
pvcLoadToDCEThresh_realTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcLoadToDCEThresh_realTime.setStatus("mandatory")


class _PvcLoadToDTEThresh_realTimeRange_Type(Integer32):
    """Custom type pvcLoadToDTEThresh_realTimeRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcLoadToDTEThresh_realTimeRange_Type.__name__ = "Integer32"
_PvcLoadToDTEThresh_realTimeRange_Object = MibScalar
pvcLoadToDTEThresh_realTimeRange = _PvcLoadToDTEThresh_realTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 20),
    _PvcLoadToDTEThresh_realTimeRange_Type()
)
pvcLoadToDTEThresh_realTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcLoadToDTEThresh_realTimeRange.setStatus("mandatory")


class _PvcLoadToDCEThresh_realTimeRange_Type(Integer32):
    """Custom type pvcLoadToDCEThresh_realTimeRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcLoadToDCEThresh_realTimeRange_Type.__name__ = "Integer32"
_PvcLoadToDCEThresh_realTimeRange_Object = MibScalar
pvcLoadToDCEThresh_realTimeRange = _PvcLoadToDCEThresh_realTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 4, 21),
    _PvcLoadToDCEThresh_realTimeRange_Type()
)
pvcLoadToDCEThresh_realTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcLoadToDCEThresh_realTimeRange.setStatus("mandatory")
_Pvc_config_ObjectIdentity = ObjectIdentity
pvc_config = _Pvc_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5)
)


class _PvcTC_Type(Integer32):
    """Custom type pvcTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcTC_Type.__name__ = "Integer32"
_PvcTC_Object = MibScalar
pvcTC = _PvcTC_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 1),
    _PvcTC_Type()
)
pvcTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcTC.setStatus("mandatory")
_PvcCirEir_Table_Object = MibTable
pvcCirEir_Table = _PvcCirEir_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 2)
)
if mibBuilder.loadTexts:
    pvcCirEir_Table.setStatus("mandatory")
_PvcCirEir_Entry_Object = MibTableRow
pvcCirEir_Entry = _PvcCirEir_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 2, 1)
)
pvcCirEir_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcCirEir-Table-Index"),
)
if mibBuilder.loadTexts:
    pvcCirEir_Entry.setStatus("mandatory")


class _PvcCirEir_Table_Index_Type(Integer32):
    """Custom type pvcCirEir_Table_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcCirEir_Table_Index_Type.__name__ = "Integer32"
_PvcCirEir_Table_Index_Object = MibScalar
pvcCirEir_Table_Index = _PvcCirEir_Table_Index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 2, 1, 1),
    _PvcCirEir_Table_Index_Type()
)
pvcCirEir_Table_Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCirEir_Table_Index.setStatus("mandatory")


class _PvcCirToDTE_Type(Integer32):
    """Custom type pvcCirToDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048000),
    )


_PvcCirToDTE_Type.__name__ = "Integer32"
_PvcCirToDTE_Object = MibTableColumn
pvcCirToDTE = _PvcCirToDTE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 2, 1, 2),
    _PvcCirToDTE_Type()
)
pvcCirToDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcCirToDTE.setStatus("mandatory")


class _PvcCirToDCE_Type(Integer32):
    """Custom type pvcCirToDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048000),
    )


_PvcCirToDCE_Type.__name__ = "Integer32"
_PvcCirToDCE_Object = MibTableColumn
pvcCirToDCE = _PvcCirToDCE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 2, 1, 3),
    _PvcCirToDCE_Type()
)
pvcCirToDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcCirToDCE.setStatus("mandatory")


class _PvcEirToDTE_Type(Integer32):
    """Custom type pvcEirToDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_PvcEirToDTE_Type.__name__ = "Integer32"
_PvcEirToDTE_Object = MibTableColumn
pvcEirToDTE = _PvcEirToDTE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 2, 1, 4),
    _PvcEirToDTE_Type()
)
pvcEirToDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcEirToDTE.setStatus("mandatory")


class _PvcEirToDCE_Type(Integer32):
    """Custom type pvcEirToDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_PvcEirToDCE_Type.__name__ = "Integer32"
_PvcEirToDCE_Object = MibTableColumn
pvcEirToDCE = _PvcEirToDCE_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 5, 2, 1, 5),
    _PvcEirToDCE_Type()
)
pvcEirToDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcEirToDCE.setStatus("mandatory")
_File_download_config_ObjectIdentity = ObjectIdentity
file_download_config = _File_download_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6)
)
_SourceIpAddress_Type = IpAddress
_SourceIpAddress_Object = MibScalar
sourceIpAddress = _SourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6, 1),
    _SourceIpAddress_Type()
)
sourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceIpAddress.setStatus("mandatory")


class _SourceFileName_Type(DisplayString):
    """Custom type sourceFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SourceFileName_Type.__name__ = "DisplayString"
_SourceFileName_Object = MibScalar
sourceFileName = _SourceFileName_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6, 2),
    _SourceFileName_Type()
)
sourceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceFileName.setStatus("mandatory")


class _SourceFileMode_Type(Integer32):
    """Custom type sourceFileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("netAscii", 1)
    )


_SourceFileMode_Type.__name__ = "Integer32"
_SourceFileMode_Object = MibScalar
sourceFileMode = _SourceFileMode_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6, 3),
    _SourceFileMode_Type()
)
sourceFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceFileMode.setStatus("mandatory")


class _TftpAction_Type(Integer32):
    """Custom type tftpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("getfile", 1)
    )


_TftpAction_Type.__name__ = "Integer32"
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6, 4),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tftpAction.setStatus("mandatory")


class _ChangeVersion_Type(Integer32):
    """Custom type changeVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sameVersion", 1),
          ("switchVersion", 2))
    )


_ChangeVersion_Type.__name__ = "Integer32"
_ChangeVersion_Object = MibScalar
changeVersion = _ChangeVersion_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6, 5),
    _ChangeVersion_Type()
)
changeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    changeVersion.setStatus("mandatory")


class _SoftwareReset_Type(Integer32):
    """Custom type softwareReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_SoftwareReset_Type.__name__ = "Integer32"
_SoftwareReset_Object = MibScalar
softwareReset = _SoftwareReset_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6, 6),
    _SoftwareReset_Type()
)
softwareReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    softwareReset.setStatus("mandatory")


class _TftpState_Type(Integer32):
    """Custom type tftpState based on Integer32"""
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
          ("idle-failed", 3),
          ("idle-ok", 1))
    )


_TftpState_Type.__name__ = "Integer32"
_TftpState_Object = MibScalar
tftpState = _TftpState_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 6, 7),
    _TftpState_Type()
)
tftpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpState.setStatus("mandatory")
_Net_management_config_ObjectIdentity = ObjectIdentity
net_management_config = _Net_management_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 7)
)


class _IpInterface_Type(Integer32):
    """Custom type ipInterface based on Integer32"""
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
        *(("ethernetIpInterface", 2),
          ("isdnIpInterface", 5),
          ("pppIpInterface", 1),
          ("privateInbandIpInterface", 3),
          ("userInbandIpInterface", 4))
    )


_IpInterface_Type.__name__ = "Integer32"
_IpInterface_Object = MibScalar
ipInterface = _IpInterface_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 7, 1),
    _IpInterface_Type()
)
ipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterface.setStatus("mandatory")
_InbandIpAddress_Type = IpAddress
_InbandIpAddress_Object = MibScalar
inbandIpAddress = _InbandIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 7, 2),
    _InbandIpAddress_Type()
)
inbandIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbandIpAddress.setStatus("mandatory")
_OutbandIpAddress_Type = IpAddress
_OutbandIpAddress_Object = MibScalar
outbandIpAddress = _OutbandIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 7, 3),
    _OutbandIpAddress_Type()
)
outbandIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbandIpAddress.setStatus("mandatory")
_RouterIpAddress_Type = IpAddress
_RouterIpAddress_Object = MibScalar
routerIpAddress = _RouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 7, 4),
    _RouterIpAddress_Type()
)
routerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerIpAddress.setStatus("mandatory")
_SubnetmaskIpAddress_Type = IpAddress
_SubnetmaskIpAddress_Object = MibScalar
subnetmaskIpAddress = _SubnetmaskIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 1, 7, 5),
    _SubnetmaskIpAddress_Type()
)
subnetmaskIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetmaskIpAddress.setStatus("mandatory")
_ProbeStat_ObjectIdentity = ObjectIdentity
probeStat = _ProbeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 2)
)
_ChStCurrent_ObjectIdentity = ObjectIdentity
chStCurrent = _ChStCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1)
)
_Dte_frames_ch_curr_Type = Counter32
_Dte_frames_ch_curr_Object = MibScalar
dte_frames_ch_curr = _Dte_frames_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 1),
    _Dte_frames_ch_curr_Type()
)
dte_frames_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_frames_ch_curr.setStatus("mandatory")
_Dce_frames_ch_curr_Type = Counter32
_Dce_frames_ch_curr_Object = MibScalar
dce_frames_ch_curr = _Dce_frames_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 2),
    _Dce_frames_ch_curr_Type()
)
dce_frames_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_frames_ch_curr.setStatus("mandatory")
_Dte_octets_ch_curr_Type = Counter32
_Dte_octets_ch_curr_Object = MibScalar
dte_octets_ch_curr = _Dte_octets_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 3),
    _Dte_octets_ch_curr_Type()
)
dte_octets_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_octets_ch_curr.setStatus("mandatory")
_Dce_octets_ch_curr_Type = Counter32
_Dce_octets_ch_curr_Object = MibScalar
dce_octets_ch_curr = _Dce_octets_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 4),
    _Dce_octets_ch_curr_Type()
)
dce_octets_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_octets_ch_curr.setStatus("mandatory")
_Lmi_enq_tx_ch_curr_Type = Counter32
_Lmi_enq_tx_ch_curr_Object = MibScalar
lmi_enq_tx_ch_curr = _Lmi_enq_tx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 5),
    _Lmi_enq_tx_ch_curr_Type()
)
lmi_enq_tx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_enq_tx_ch_curr.setStatus("mandatory")
_Lmi_resp_tx_ch_curr_Type = Counter32
_Lmi_resp_tx_ch_curr_Object = MibScalar
lmi_resp_tx_ch_curr = _Lmi_resp_tx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 6),
    _Lmi_resp_tx_ch_curr_Type()
)
lmi_resp_tx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_resp_tx_ch_curr.setStatus("mandatory")
_Lmi_enq_rx_ch_curr_Type = Counter32
_Lmi_enq_rx_ch_curr_Object = MibScalar
lmi_enq_rx_ch_curr = _Lmi_enq_rx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 7),
    _Lmi_enq_rx_ch_curr_Type()
)
lmi_enq_rx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_enq_rx_ch_curr.setStatus("mandatory")
_Lmi_resp_rx_ch_curr_Type = Counter32
_Lmi_resp_rx_ch_curr_Object = MibScalar
lmi_resp_rx_ch_curr = _Lmi_resp_rx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 8),
    _Lmi_resp_rx_ch_curr_Type()
)
lmi_resp_rx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_resp_rx_ch_curr.setStatus("mandatory")
_Fecn_frames_ch_curr_Type = Counter32
_Fecn_frames_ch_curr_Object = MibScalar
fecn_frames_ch_curr = _Fecn_frames_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 9),
    _Fecn_frames_ch_curr_Type()
)
fecn_frames_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecn_frames_ch_curr.setStatus("mandatory")
_Becn_frames_ch_curr_Type = Counter32
_Becn_frames_ch_curr_Object = MibScalar
becn_frames_ch_curr = _Becn_frames_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 10),
    _Becn_frames_ch_curr_Type()
)
becn_frames_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    becn_frames_ch_curr.setStatus("mandatory")
_Ip_tx_ch_curr_Type = Counter32
_Ip_tx_ch_curr_Object = MibScalar
ip_tx_ch_curr = _Ip_tx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 11),
    _Ip_tx_ch_curr_Type()
)
ip_tx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_tx_ch_curr.setStatus("mandatory")
_Ip_rx_ch_curr_Type = Counter32
_Ip_rx_ch_curr_Object = MibScalar
ip_rx_ch_curr = _Ip_rx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 12),
    _Ip_rx_ch_curr_Type()
)
ip_rx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_rx_ch_curr.setStatus("mandatory")
_Poll_tx_ch_curr_Type = Counter32
_Poll_tx_ch_curr_Object = MibScalar
poll_tx_ch_curr = _Poll_tx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 13),
    _Poll_tx_ch_curr_Type()
)
poll_tx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_tx_ch_curr.setStatus("mandatory")
_Resp_tx_ch_curr_Type = Counter32
_Resp_tx_ch_curr_Object = MibScalar
resp_tx_ch_curr = _Resp_tx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 14),
    _Resp_tx_ch_curr_Type()
)
resp_tx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_tx_ch_curr.setStatus("mandatory")
_Poll_rx_ch_curr_Type = Counter32
_Poll_rx_ch_curr_Object = MibScalar
poll_rx_ch_curr = _Poll_rx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 15),
    _Poll_rx_ch_curr_Type()
)
poll_rx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_rx_ch_curr.setStatus("mandatory")
_Resp_rx_ch_curr_Type = Counter32
_Resp_rx_ch_curr_Object = MibScalar
resp_rx_ch_curr = _Resp_rx_ch_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 1, 16),
    _Resp_rx_ch_curr_Type()
)
resp_rx_ch_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_rx_ch_curr.setStatus("mandatory")
_ChStInterval_Table_Object = MibTable
chStInterval_Table = _ChStInterval_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2)
)
if mibBuilder.loadTexts:
    chStInterval_Table.setStatus("mandatory")
_ChStInterval_Entry_Object = MibTableRow
chStInterval_Entry = _ChStInterval_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1)
)
chStInterval_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "chStIntv-index"),
)
if mibBuilder.loadTexts:
    chStInterval_Entry.setStatus("mandatory")


class _ChStIntv_index_Type(Integer32):
    """Custom type chStIntv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ChStIntv_index_Type.__name__ = "Integer32"
_ChStIntv_index_Object = MibScalar
chStIntv_index = _ChStIntv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 1),
    _ChStIntv_index_Type()
)
chStIntv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chStIntv_index.setStatus("mandatory")
_Dte_frames_ch_intv_Type = Counter32
_Dte_frames_ch_intv_Object = MibScalar
dte_frames_ch_intv = _Dte_frames_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 2),
    _Dte_frames_ch_intv_Type()
)
dte_frames_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_frames_ch_intv.setStatus("mandatory")
_Dce_frames_ch_intv_Type = Counter32
_Dce_frames_ch_intv_Object = MibScalar
dce_frames_ch_intv = _Dce_frames_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 3),
    _Dce_frames_ch_intv_Type()
)
dce_frames_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_frames_ch_intv.setStatus("mandatory")
_Dte_octets_ch_intv_Type = Counter32
_Dte_octets_ch_intv_Object = MibScalar
dte_octets_ch_intv = _Dte_octets_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 4),
    _Dte_octets_ch_intv_Type()
)
dte_octets_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_octets_ch_intv.setStatus("mandatory")
_Dce_octets_ch_intv_Type = Counter32
_Dce_octets_ch_intv_Object = MibScalar
dce_octets_ch_intv = _Dce_octets_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 5),
    _Dce_octets_ch_intv_Type()
)
dce_octets_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_octets_ch_intv.setStatus("mandatory")
_Lmi_enq_tx_ch_intv_Type = Counter32
_Lmi_enq_tx_ch_intv_Object = MibScalar
lmi_enq_tx_ch_intv = _Lmi_enq_tx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 6),
    _Lmi_enq_tx_ch_intv_Type()
)
lmi_enq_tx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_enq_tx_ch_intv.setStatus("mandatory")
_Lmi_resp_tx_ch_intv_Type = Counter32
_Lmi_resp_tx_ch_intv_Object = MibScalar
lmi_resp_tx_ch_intv = _Lmi_resp_tx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 7),
    _Lmi_resp_tx_ch_intv_Type()
)
lmi_resp_tx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_resp_tx_ch_intv.setStatus("mandatory")
_Lmi_enq_rx_ch_intv_Type = Counter32
_Lmi_enq_rx_ch_intv_Object = MibScalar
lmi_enq_rx_ch_intv = _Lmi_enq_rx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 8),
    _Lmi_enq_rx_ch_intv_Type()
)
lmi_enq_rx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_enq_rx_ch_intv.setStatus("mandatory")
_Lmi_resp_rx_ch_intv_Type = Counter32
_Lmi_resp_rx_ch_intv_Object = MibScalar
lmi_resp_rx_ch_intv = _Lmi_resp_rx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 9),
    _Lmi_resp_rx_ch_intv_Type()
)
lmi_resp_rx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmi_resp_rx_ch_intv.setStatus("mandatory")
_Fecn_frames_ch_intv_Type = Counter32
_Fecn_frames_ch_intv_Object = MibScalar
fecn_frames_ch_intv = _Fecn_frames_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 10),
    _Fecn_frames_ch_intv_Type()
)
fecn_frames_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecn_frames_ch_intv.setStatus("mandatory")
_Becn_frames_ch_intv_Type = Counter32
_Becn_frames_ch_intv_Object = MibScalar
becn_frames_ch_intv = _Becn_frames_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 11),
    _Becn_frames_ch_intv_Type()
)
becn_frames_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    becn_frames_ch_intv.setStatus("mandatory")
_Ip_tx_ch_intv_Type = Counter32
_Ip_tx_ch_intv_Object = MibScalar
ip_tx_ch_intv = _Ip_tx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 12),
    _Ip_tx_ch_intv_Type()
)
ip_tx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_tx_ch_intv.setStatus("mandatory")
_Ip_rx_ch_intv_Type = Counter32
_Ip_rx_ch_intv_Object = MibScalar
ip_rx_ch_intv = _Ip_rx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 13),
    _Ip_rx_ch_intv_Type()
)
ip_rx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_rx_ch_intv.setStatus("mandatory")
_Poll_tx_ch_intv_Type = Counter32
_Poll_tx_ch_intv_Object = MibScalar
poll_tx_ch_intv = _Poll_tx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 14),
    _Poll_tx_ch_intv_Type()
)
poll_tx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_tx_ch_intv.setStatus("mandatory")
_Resp_tx_ch_intv_Type = Counter32
_Resp_tx_ch_intv_Object = MibScalar
resp_tx_ch_intv = _Resp_tx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 15),
    _Resp_tx_ch_intv_Type()
)
resp_tx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_tx_ch_intv.setStatus("mandatory")
_Poll_rx_ch_intv_Type = Counter32
_Poll_rx_ch_intv_Object = MibScalar
poll_rx_ch_intv = _Poll_rx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 16),
    _Poll_rx_ch_intv_Type()
)
poll_rx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_rx_ch_intv.setStatus("mandatory")
_Resp_rx_ch_intv_Type = Counter32
_Resp_rx_ch_intv_Object = MibScalar
resp_rx_ch_intv = _Resp_rx_ch_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 2, 1, 17),
    _Resp_rx_ch_intv_Type()
)
resp_rx_ch_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_rx_ch_intv.setStatus("mandatory")
_PvcStCurrent_Table_Object = MibTable
pvcStCurrent_Table = _PvcStCurrent_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3)
)
if mibBuilder.loadTexts:
    pvcStCurrent_Table.setStatus("mandatory")
_PvcStCurrent_Entry_Object = MibTableRow
pvcStCurrent_Entry = _PvcStCurrent_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1)
)
pvcStCurrent_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvc-number-index-curr"),
)
if mibBuilder.loadTexts:
    pvcStCurrent_Entry.setStatus("mandatory")


class _Pvc_number_index_curr_Type(Integer32):
    """Custom type pvc_number_index_curr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_Pvc_number_index_curr_Type.__name__ = "Integer32"
_Pvc_number_index_curr_Object = MibScalar
pvc_number_index_curr = _Pvc_number_index_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 1),
    _Pvc_number_index_curr_Type()
)
pvc_number_index_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_number_index_curr.setStatus("mandatory")
_Dte_frames_pvc_curr_Type = Counter32
_Dte_frames_pvc_curr_Object = MibScalar
dte_frames_pvc_curr = _Dte_frames_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 2),
    _Dte_frames_pvc_curr_Type()
)
dte_frames_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_frames_pvc_curr.setStatus("mandatory")
_Dce_frames_pvc_curr_Type = Counter32
_Dce_frames_pvc_curr_Object = MibScalar
dce_frames_pvc_curr = _Dce_frames_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 3),
    _Dce_frames_pvc_curr_Type()
)
dce_frames_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_frames_pvc_curr.setStatus("mandatory")
_Dte_octets_pvc_curr_Type = Counter32
_Dte_octets_pvc_curr_Object = MibScalar
dte_octets_pvc_curr = _Dte_octets_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 4),
    _Dte_octets_pvc_curr_Type()
)
dte_octets_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_octets_pvc_curr.setStatus("mandatory")
_Dce_octets_pvc_curr_Type = Counter32
_Dce_octets_pvc_curr_Object = MibScalar
dce_octets_pvc_curr = _Dce_octets_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 5),
    _Dce_octets_pvc_curr_Type()
)
dce_octets_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_octets_pvc_curr.setStatus("mandatory")
_Dte_frames_with_DE_pvc_curr_Type = Counter32
_Dte_frames_with_DE_pvc_curr_Object = MibScalar
dte_frames_with_DE_pvc_curr = _Dte_frames_with_DE_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 6),
    _Dte_frames_with_DE_pvc_curr_Type()
)
dte_frames_with_DE_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_frames_with_DE_pvc_curr.setStatus("mandatory")
_Dce_frames_with_DE_pvc_curr_Type = Counter32
_Dce_frames_with_DE_pvc_curr_Object = MibScalar
dce_frames_with_DE_pvc_curr = _Dce_frames_with_DE_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 7),
    _Dce_frames_with_DE_pvc_curr_Type()
)
dce_frames_with_DE_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_frames_with_DE_pvc_curr.setStatus("mandatory")
_Fecn_frames_pvc_curr_Type = Counter32
_Fecn_frames_pvc_curr_Object = MibScalar
fecn_frames_pvc_curr = _Fecn_frames_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 8),
    _Fecn_frames_pvc_curr_Type()
)
fecn_frames_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecn_frames_pvc_curr.setStatus("mandatory")
_Becn_frames_pvc_curr_Type = Counter32
_Becn_frames_pvc_curr_Object = MibScalar
becn_frames_pvc_curr = _Becn_frames_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 9),
    _Becn_frames_pvc_curr_Type()
)
becn_frames_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    becn_frames_pvc_curr.setStatus("mandatory")
_Poll_tx_pvc_curr_Type = Counter32
_Poll_tx_pvc_curr_Object = MibScalar
poll_tx_pvc_curr = _Poll_tx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 10),
    _Poll_tx_pvc_curr_Type()
)
poll_tx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_tx_pvc_curr.setStatus("mandatory")
_Resp_tx_pvc_curr_Type = Counter32
_Resp_tx_pvc_curr_Object = MibScalar
resp_tx_pvc_curr = _Resp_tx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 11),
    _Resp_tx_pvc_curr_Type()
)
resp_tx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_tx_pvc_curr.setStatus("mandatory")
_Poll_rx_pvc_curr_Type = Counter32
_Poll_rx_pvc_curr_Object = MibScalar
poll_rx_pvc_curr = _Poll_rx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 12),
    _Poll_rx_pvc_curr_Type()
)
poll_rx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_rx_pvc_curr.setStatus("mandatory")
_Resp_rx_pvc_curr_Type = Counter32
_Resp_rx_pvc_curr_Object = MibScalar
resp_rx_pvc_curr = _Resp_rx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 13),
    _Resp_rx_pvc_curr_Type()
)
resp_rx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_rx_pvc_curr.setStatus("mandatory")


class _Pvc_loop_curr_Type(Integer32):
    """Custom type pvc_loop_curr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("no-loopback", 2))
    )


_Pvc_loop_curr_Type.__name__ = "Integer32"
_Pvc_loop_curr_Object = MibScalar
pvc_loop_curr = _Pvc_loop_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 14),
    _Pvc_loop_curr_Type()
)
pvc_loop_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_loop_curr.setStatus("mandatory")
_Ip_poll_tx_pvc_curr_Type = Counter32
_Ip_poll_tx_pvc_curr_Object = MibScalar
ip_poll_tx_pvc_curr = _Ip_poll_tx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 15),
    _Ip_poll_tx_pvc_curr_Type()
)
ip_poll_tx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_poll_tx_pvc_curr.setStatus("mandatory")
_Ip_resp_tx_pvc_curr_Type = Counter32
_Ip_resp_tx_pvc_curr_Object = MibScalar
ip_resp_tx_pvc_curr = _Ip_resp_tx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 16),
    _Ip_resp_tx_pvc_curr_Type()
)
ip_resp_tx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_resp_tx_pvc_curr.setStatus("mandatory")
_Ip_poll_rx_pvc_curr_Type = Counter32
_Ip_poll_rx_pvc_curr_Object = MibScalar
ip_poll_rx_pvc_curr = _Ip_poll_rx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 17),
    _Ip_poll_rx_pvc_curr_Type()
)
ip_poll_rx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_poll_rx_pvc_curr.setStatus("mandatory")
_Ip_resp_rx_pvc_curr_Type = Counter32
_Ip_resp_rx_pvc_curr_Object = MibScalar
ip_resp_rx_pvc_curr = _Ip_resp_rx_pvc_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 18),
    _Ip_resp_rx_pvc_curr_Type()
)
ip_resp_rx_pvc_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_resp_rx_pvc_curr.setStatus("mandatory")
_IpRtrRxLatTxPvcCurr_Type = Counter32
_IpRtrRxLatTxPvcCurr_Object = MibTableColumn
ipRtrRxLatTxPvcCurr = _IpRtrRxLatTxPvcCurr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 19),
    _IpRtrRxLatTxPvcCurr_Type()
)
ipRtrRxLatTxPvcCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrRxLatTxPvcCurr.setStatus("mandatory")
_IpRtrRxLatRxPvcCurr_Type = Counter32
_IpRtrRxLatRxPvcCurr_Object = MibTableColumn
ipRtrRxLatRxPvcCurr = _IpRtrRxLatRxPvcCurr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 20),
    _IpRtrRxLatRxPvcCurr_Type()
)
ipRtrRxLatRxPvcCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrRxLatRxPvcCurr.setStatus("mandatory")
_IpRtrTxLatTxPvcCurr_Type = Counter32
_IpRtrTxLatTxPvcCurr_Object = MibTableColumn
ipRtrTxLatTxPvcCurr = _IpRtrTxLatTxPvcCurr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 21),
    _IpRtrTxLatTxPvcCurr_Type()
)
ipRtrTxLatTxPvcCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrTxLatTxPvcCurr.setStatus("mandatory")
_IpRtrTxLatRxPvcCurr_Type = Counter32
_IpRtrTxLatRxPvcCurr_Object = MibTableColumn
ipRtrTxLatRxPvcCurr = _IpRtrTxLatRxPvcCurr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 3, 1, 22),
    _IpRtrTxLatRxPvcCurr_Type()
)
ipRtrTxLatRxPvcCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrTxLatRxPvcCurr.setStatus("mandatory")
_PvcStInterval_Table_Object = MibTable
pvcStInterval_Table = _PvcStInterval_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4)
)
if mibBuilder.loadTexts:
    pvcStInterval_Table.setStatus("mandatory")
_PvcStInterval_Entry_Object = MibTableRow
pvcStInterval_Entry = _PvcStInterval_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1)
)
pvcStInterval_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvc-number-index-intv"),
    (0, "LINK-PROBE-MIB", "pvcStIntv-index"),
)
if mibBuilder.loadTexts:
    pvcStInterval_Entry.setStatus("mandatory")


class _Pvc_number_index_intv_Type(Integer32):
    """Custom type pvc_number_index_intv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_Pvc_number_index_intv_Type.__name__ = "Integer32"
_Pvc_number_index_intv_Object = MibScalar
pvc_number_index_intv = _Pvc_number_index_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 1),
    _Pvc_number_index_intv_Type()
)
pvc_number_index_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_number_index_intv.setStatus("mandatory")


class _PvcStIntv_index_Type(Integer32):
    """Custom type pvcStIntv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvcStIntv_index_Type.__name__ = "Integer32"
_PvcStIntv_index_Object = MibScalar
pvcStIntv_index = _PvcStIntv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 2),
    _PvcStIntv_index_Type()
)
pvcStIntv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStIntv_index.setStatus("mandatory")
_Dte_frames_pvc_intv_Type = Counter32
_Dte_frames_pvc_intv_Object = MibScalar
dte_frames_pvc_intv = _Dte_frames_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 3),
    _Dte_frames_pvc_intv_Type()
)
dte_frames_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_frames_pvc_intv.setStatus("mandatory")
_Dce_frames_pvc_intv_Type = Counter32
_Dce_frames_pvc_intv_Object = MibScalar
dce_frames_pvc_intv = _Dce_frames_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 4),
    _Dce_frames_pvc_intv_Type()
)
dce_frames_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_frames_pvc_intv.setStatus("mandatory")
_Dte_octets_pvc_intv_Type = Counter32
_Dte_octets_pvc_intv_Object = MibScalar
dte_octets_pvc_intv = _Dte_octets_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 5),
    _Dte_octets_pvc_intv_Type()
)
dte_octets_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_octets_pvc_intv.setStatus("mandatory")
_Dce_octets_pvc_intv_Type = Counter32
_Dce_octets_pvc_intv_Object = MibScalar
dce_octets_pvc_intv = _Dce_octets_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 6),
    _Dce_octets_pvc_intv_Type()
)
dce_octets_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_octets_pvc_intv.setStatus("mandatory")
_Dte_frames_with_DE_pvc_intv_Type = Counter32
_Dte_frames_with_DE_pvc_intv_Object = MibScalar
dte_frames_with_DE_pvc_intv = _Dte_frames_with_DE_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 7),
    _Dte_frames_with_DE_pvc_intv_Type()
)
dte_frames_with_DE_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dte_frames_with_DE_pvc_intv.setStatus("mandatory")
_Dce_frames_with_DE_pvc_intv_Type = Counter32
_Dce_frames_with_DE_pvc_intv_Object = MibScalar
dce_frames_with_DE_pvc_intv = _Dce_frames_with_DE_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 8),
    _Dce_frames_with_DE_pvc_intv_Type()
)
dce_frames_with_DE_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dce_frames_with_DE_pvc_intv.setStatus("mandatory")
_Fecn_frames_pvc_intv_Type = Counter32
_Fecn_frames_pvc_intv_Object = MibScalar
fecn_frames_pvc_intv = _Fecn_frames_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 9),
    _Fecn_frames_pvc_intv_Type()
)
fecn_frames_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fecn_frames_pvc_intv.setStatus("mandatory")
_Becn_frames_pvc_intv_Type = Counter32
_Becn_frames_pvc_intv_Object = MibScalar
becn_frames_pvc_intv = _Becn_frames_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 10),
    _Becn_frames_pvc_intv_Type()
)
becn_frames_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    becn_frames_pvc_intv.setStatus("mandatory")
_Poll_tx_pvc_intv_Type = Counter32
_Poll_tx_pvc_intv_Object = MibScalar
poll_tx_pvc_intv = _Poll_tx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 11),
    _Poll_tx_pvc_intv_Type()
)
poll_tx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_tx_pvc_intv.setStatus("mandatory")
_Resp_tx_pvc_intv_Type = Counter32
_Resp_tx_pvc_intv_Object = MibScalar
resp_tx_pvc_intv = _Resp_tx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 12),
    _Resp_tx_pvc_intv_Type()
)
resp_tx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_tx_pvc_intv.setStatus("mandatory")
_Poll_rx_pvc_intv_Type = Counter32
_Poll_rx_pvc_intv_Object = MibScalar
poll_rx_pvc_intv = _Poll_rx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 13),
    _Poll_rx_pvc_intv_Type()
)
poll_rx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poll_rx_pvc_intv.setStatus("mandatory")
_Resp_rx_pvc_intv_Type = Counter32
_Resp_rx_pvc_intv_Object = MibScalar
resp_rx_pvc_intv = _Resp_rx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 14),
    _Resp_rx_pvc_intv_Type()
)
resp_rx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resp_rx_pvc_intv.setStatus("mandatory")
_Pvc_loop_intv_Type = Integer32
_Pvc_loop_intv_Object = MibScalar
pvc_loop_intv = _Pvc_loop_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 15),
    _Pvc_loop_intv_Type()
)
pvc_loop_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_loop_intv.setStatus("mandatory")
_Ip_poll_tx_pvc_intv_Type = Counter32
_Ip_poll_tx_pvc_intv_Object = MibScalar
ip_poll_tx_pvc_intv = _Ip_poll_tx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 16),
    _Ip_poll_tx_pvc_intv_Type()
)
ip_poll_tx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_poll_tx_pvc_intv.setStatus("mandatory")
_Ip_resp_tx_pvc_intv_Type = Counter32
_Ip_resp_tx_pvc_intv_Object = MibScalar
ip_resp_tx_pvc_intv = _Ip_resp_tx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 17),
    _Ip_resp_tx_pvc_intv_Type()
)
ip_resp_tx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_resp_tx_pvc_intv.setStatus("mandatory")
_Ip_poll_rx_pvc_intv_Type = Counter32
_Ip_poll_rx_pvc_intv_Object = MibScalar
ip_poll_rx_pvc_intv = _Ip_poll_rx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 18),
    _Ip_poll_rx_pvc_intv_Type()
)
ip_poll_rx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_poll_rx_pvc_intv.setStatus("mandatory")
_Ip_resp_rx_pvc_intv_Type = Counter32
_Ip_resp_rx_pvc_intv_Object = MibScalar
ip_resp_rx_pvc_intv = _Ip_resp_rx_pvc_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 19),
    _Ip_resp_rx_pvc_intv_Type()
)
ip_resp_rx_pvc_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip_resp_rx_pvc_intv.setStatus("mandatory")
_IpRtrRxLatTxPvcIntv_Type = Counter32
_IpRtrRxLatTxPvcIntv_Object = MibTableColumn
ipRtrRxLatTxPvcIntv = _IpRtrRxLatTxPvcIntv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 20),
    _IpRtrRxLatTxPvcIntv_Type()
)
ipRtrRxLatTxPvcIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrRxLatTxPvcIntv.setStatus("mandatory")
_IpRtrRxLatRxPvcIntv_Type = Counter32
_IpRtrRxLatRxPvcIntv_Object = MibTableColumn
ipRtrRxLatRxPvcIntv = _IpRtrRxLatRxPvcIntv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 21),
    _IpRtrRxLatRxPvcIntv_Type()
)
ipRtrRxLatRxPvcIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrRxLatRxPvcIntv.setStatus("mandatory")
_IpRtrTxLatTxPvcIntv_Type = Counter32
_IpRtrTxLatTxPvcIntv_Object = MibTableColumn
ipRtrTxLatTxPvcIntv = _IpRtrTxLatTxPvcIntv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 22),
    _IpRtrTxLatTxPvcIntv_Type()
)
ipRtrTxLatTxPvcIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrTxLatTxPvcIntv.setStatus("mandatory")
_IpRtrTxLatRxPvcIntv_Type = Counter32
_IpRtrTxLatRxPvcIntv_Object = MibTableColumn
ipRtrTxLatRxPvcIntv = _IpRtrTxLatRxPvcIntv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 2, 4, 1, 23),
    _IpRtrTxLatRxPvcIntv_Type()
)
ipRtrTxLatRxPvcIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtrTxLatRxPvcIntv.setStatus("mandatory")
_ProbePerform_ObjectIdentity = ObjectIdentity
probePerform = _ProbePerform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 3)
)
_ChanPerfCurr_ObjectIdentity = ObjectIdentity
chanPerfCurr = _ChanPerfCurr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 1)
)


class _Chan_unvail_toDte_curr_Type(DisplayString):
    """Custom type chan_unvail_toDte_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_unvail_toDte_curr_Type.__name__ = "DisplayString"
_Chan_unvail_toDte_curr_Object = MibScalar
chan_unvail_toDte_curr = _Chan_unvail_toDte_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 1, 1),
    _Chan_unvail_toDte_curr_Type()
)
chan_unvail_toDte_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_unvail_toDte_curr.setStatus("mandatory")


class _Chan_unavail_toDce_curr_Type(DisplayString):
    """Custom type chan_unavail_toDce_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_unavail_toDce_curr_Type.__name__ = "DisplayString"
_Chan_unavail_toDce_curr_Object = MibScalar
chan_unavail_toDce_curr = _Chan_unavail_toDce_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 1, 2),
    _Chan_unavail_toDce_curr_Type()
)
chan_unavail_toDce_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_unavail_toDce_curr.setStatus("mandatory")


class _Chan_user_load_tx_curr_Type(DisplayString):
    """Custom type chan_user_load_tx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_user_load_tx_curr_Type.__name__ = "DisplayString"
_Chan_user_load_tx_curr_Object = MibScalar
chan_user_load_tx_curr = _Chan_user_load_tx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 1, 3),
    _Chan_user_load_tx_curr_Type()
)
chan_user_load_tx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_user_load_tx_curr.setStatus("mandatory")


class _Chan_user_load_rx_curr_Type(DisplayString):
    """Custom type chan_user_load_rx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_user_load_rx_curr_Type.__name__ = "DisplayString"
_Chan_user_load_rx_curr_Object = MibScalar
chan_user_load_rx_curr = _Chan_user_load_rx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 1, 4),
    _Chan_user_load_rx_curr_Type()
)
chan_user_load_rx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_user_load_rx_curr.setStatus("mandatory")


class _Chan_total_load_tx_curr_Type(DisplayString):
    """Custom type chan_total_load_tx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_total_load_tx_curr_Type.__name__ = "DisplayString"
_Chan_total_load_tx_curr_Object = MibScalar
chan_total_load_tx_curr = _Chan_total_load_tx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 1, 5),
    _Chan_total_load_tx_curr_Type()
)
chan_total_load_tx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_total_load_tx_curr.setStatus("mandatory")


class _Chan_total_load_rx_curr_Type(DisplayString):
    """Custom type chan_total_load_rx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_total_load_rx_curr_Type.__name__ = "DisplayString"
_Chan_total_load_rx_curr_Object = MibScalar
chan_total_load_rx_curr = _Chan_total_load_rx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 1, 6),
    _Chan_total_load_rx_curr_Type()
)
chan_total_load_rx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_total_load_rx_curr.setStatus("mandatory")
_ChanPerfIntv_Table_Object = MibTable
chanPerfIntv_Table = _ChanPerfIntv_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2)
)
if mibBuilder.loadTexts:
    chanPerfIntv_Table.setStatus("mandatory")
_ChanPerfIntv_Entry_Object = MibTableRow
chanPerfIntv_Entry = _ChanPerfIntv_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1)
)
chanPerfIntv_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "chanPerfIntv-index"),
)
if mibBuilder.loadTexts:
    chanPerfIntv_Entry.setStatus("mandatory")


class _ChanPerfIntv_index_Type(Integer32):
    """Custom type chanPerfIntv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ChanPerfIntv_index_Type.__name__ = "Integer32"
_ChanPerfIntv_index_Object = MibScalar
chanPerfIntv_index = _ChanPerfIntv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 1),
    _ChanPerfIntv_index_Type()
)
chanPerfIntv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanPerfIntv_index.setStatus("mandatory")


class _Chan_unavail_toDte_intv_Type(DisplayString):
    """Custom type chan_unavail_toDte_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_unavail_toDte_intv_Type.__name__ = "DisplayString"
_Chan_unavail_toDte_intv_Object = MibScalar
chan_unavail_toDte_intv = _Chan_unavail_toDte_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 2),
    _Chan_unavail_toDte_intv_Type()
)
chan_unavail_toDte_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_unavail_toDte_intv.setStatus("mandatory")


class _Chan_unavail_toDce_intv_Type(DisplayString):
    """Custom type chan_unavail_toDce_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_unavail_toDce_intv_Type.__name__ = "DisplayString"
_Chan_unavail_toDce_intv_Object = MibScalar
chan_unavail_toDce_intv = _Chan_unavail_toDce_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 3),
    _Chan_unavail_toDce_intv_Type()
)
chan_unavail_toDce_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_unavail_toDce_intv.setStatus("mandatory")


class _Chan_user_load_tx_intv_Type(DisplayString):
    """Custom type chan_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_user_load_tx_intv_Type.__name__ = "DisplayString"
_Chan_user_load_tx_intv_Object = MibScalar
chan_user_load_tx_intv = _Chan_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 4),
    _Chan_user_load_tx_intv_Type()
)
chan_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_user_load_tx_intv.setStatus("mandatory")


class _Chan_user_load_rx_intv_Type(DisplayString):
    """Custom type chan_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_user_load_rx_intv_Type.__name__ = "DisplayString"
_Chan_user_load_rx_intv_Object = MibScalar
chan_user_load_rx_intv = _Chan_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 5),
    _Chan_user_load_rx_intv_Type()
)
chan_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_user_load_rx_intv.setStatus("mandatory")


class _Chan_total_load_tx_intv_Type(DisplayString):
    """Custom type chan_total_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_total_load_tx_intv_Type.__name__ = "DisplayString"
_Chan_total_load_tx_intv_Object = MibScalar
chan_total_load_tx_intv = _Chan_total_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 6),
    _Chan_total_load_tx_intv_Type()
)
chan_total_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_total_load_tx_intv.setStatus("mandatory")


class _Chan_total_load_rx_intv_Type(DisplayString):
    """Custom type chan_total_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_total_load_rx_intv_Type.__name__ = "DisplayString"
_Chan_total_load_rx_intv_Object = MibScalar
chan_total_load_rx_intv = _Chan_total_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 7),
    _Chan_total_load_rx_intv_Type()
)
chan_total_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_total_load_rx_intv.setStatus("mandatory")


class _Chan_min_user_load_tx_intv_Type(DisplayString):
    """Custom type chan_min_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_min_user_load_tx_intv_Type.__name__ = "DisplayString"
_Chan_min_user_load_tx_intv_Object = MibScalar
chan_min_user_load_tx_intv = _Chan_min_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 8),
    _Chan_min_user_load_tx_intv_Type()
)
chan_min_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_user_load_tx_intv.setStatus("mandatory")


class _Chan_min_user_load_tx_time_intv_Type(DisplayString):
    """Custom type chan_min_user_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chan_min_user_load_tx_time_intv_Type.__name__ = "DisplayString"
_Chan_min_user_load_tx_time_intv_Object = MibScalar
chan_min_user_load_tx_time_intv = _Chan_min_user_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 9),
    _Chan_min_user_load_tx_time_intv_Type()
)
chan_min_user_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_user_load_tx_time_intv.setStatus("mandatory")


class _Chan_min_user_load_rx_intv_Type(DisplayString):
    """Custom type chan_min_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_min_user_load_rx_intv_Type.__name__ = "DisplayString"
_Chan_min_user_load_rx_intv_Object = MibScalar
chan_min_user_load_rx_intv = _Chan_min_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 10),
    _Chan_min_user_load_rx_intv_Type()
)
chan_min_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_user_load_rx_intv.setStatus("mandatory")


class _Chan_min_user_load_rx_time_intv_Type(DisplayString):
    """Custom type chan_min_user_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chan_min_user_load_rx_time_intv_Type.__name__ = "DisplayString"
_Chan_min_user_load_rx_time_intv_Object = MibScalar
chan_min_user_load_rx_time_intv = _Chan_min_user_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 11),
    _Chan_min_user_load_rx_time_intv_Type()
)
chan_min_user_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_user_load_rx_time_intv.setStatus("mandatory")


class _Chan_min_total_load_tx_intv_Type(DisplayString):
    """Custom type chan_min_total_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_min_total_load_tx_intv_Type.__name__ = "DisplayString"
_Chan_min_total_load_tx_intv_Object = MibScalar
chan_min_total_load_tx_intv = _Chan_min_total_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 12),
    _Chan_min_total_load_tx_intv_Type()
)
chan_min_total_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_total_load_tx_intv.setStatus("mandatory")


class _Chan_min_total_load_tx_time_intv_Type(DisplayString):
    """Custom type chan_min_total_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chan_min_total_load_tx_time_intv_Type.__name__ = "DisplayString"
_Chan_min_total_load_tx_time_intv_Object = MibScalar
chan_min_total_load_tx_time_intv = _Chan_min_total_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 13),
    _Chan_min_total_load_tx_time_intv_Type()
)
chan_min_total_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_total_load_tx_time_intv.setStatus("mandatory")


class _Chan_min_total_load_rx_intv_Type(DisplayString):
    """Custom type chan_min_total_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_min_total_load_rx_intv_Type.__name__ = "DisplayString"
_Chan_min_total_load_rx_intv_Object = MibScalar
chan_min_total_load_rx_intv = _Chan_min_total_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 14),
    _Chan_min_total_load_rx_intv_Type()
)
chan_min_total_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_total_load_rx_intv.setStatus("mandatory")


class _Chan_min_total_load_rx_time_intv_Type(DisplayString):
    """Custom type chan_min_total_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chan_min_total_load_rx_time_intv_Type.__name__ = "DisplayString"
_Chan_min_total_load_rx_time_intv_Object = MibScalar
chan_min_total_load_rx_time_intv = _Chan_min_total_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 15),
    _Chan_min_total_load_rx_time_intv_Type()
)
chan_min_total_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_min_total_load_rx_time_intv.setStatus("mandatory")


class _Chan_max_user_load_tx_intv_Type(DisplayString):
    """Custom type chan_max_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_max_user_load_tx_intv_Type.__name__ = "DisplayString"
_Chan_max_user_load_tx_intv_Object = MibScalar
chan_max_user_load_tx_intv = _Chan_max_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 16),
    _Chan_max_user_load_tx_intv_Type()
)
chan_max_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_user_load_tx_intv.setStatus("mandatory")


class _Chan_max_user_load_tx_time_intv_Type(DisplayString):
    """Custom type chan_max_user_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chan_max_user_load_tx_time_intv_Type.__name__ = "DisplayString"
_Chan_max_user_load_tx_time_intv_Object = MibScalar
chan_max_user_load_tx_time_intv = _Chan_max_user_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 17),
    _Chan_max_user_load_tx_time_intv_Type()
)
chan_max_user_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_user_load_tx_time_intv.setStatus("mandatory")


class _Chan_max_user_load_rx_intv_Type(DisplayString):
    """Custom type chan_max_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_max_user_load_rx_intv_Type.__name__ = "DisplayString"
_Chan_max_user_load_rx_intv_Object = MibScalar
chan_max_user_load_rx_intv = _Chan_max_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 18),
    _Chan_max_user_load_rx_intv_Type()
)
chan_max_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_user_load_rx_intv.setStatus("mandatory")


class _Chan_max_user_load_rx_time_intv_Type(DisplayString):
    """Custom type chan_max_user_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chan_max_user_load_rx_time_intv_Type.__name__ = "DisplayString"
_Chan_max_user_load_rx_time_intv_Object = MibScalar
chan_max_user_load_rx_time_intv = _Chan_max_user_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 19),
    _Chan_max_user_load_rx_time_intv_Type()
)
chan_max_user_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_user_load_rx_time_intv.setStatus("mandatory")


class _Chan_max_total_load_tx_intv_Type(DisplayString):
    """Custom type chan_max_total_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_max_total_load_tx_intv_Type.__name__ = "DisplayString"
_Chan_max_total_load_tx_intv_Object = MibScalar
chan_max_total_load_tx_intv = _Chan_max_total_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 20),
    _Chan_max_total_load_tx_intv_Type()
)
chan_max_total_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_total_load_tx_intv.setStatus("mandatory")


class _Chan_max_total_load_tx_time_intv_Type(DisplayString):
    """Custom type chan_max_total_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_max_total_load_tx_time_intv_Type.__name__ = "DisplayString"
_Chan_max_total_load_tx_time_intv_Object = MibScalar
chan_max_total_load_tx_time_intv = _Chan_max_total_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 21),
    _Chan_max_total_load_tx_time_intv_Type()
)
chan_max_total_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_total_load_tx_time_intv.setStatus("mandatory")


class _Chan_max_total_load_rx_intv_Type(DisplayString):
    """Custom type chan_max_total_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Chan_max_total_load_rx_intv_Type.__name__ = "DisplayString"
_Chan_max_total_load_rx_intv_Object = MibScalar
chan_max_total_load_rx_intv = _Chan_max_total_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 22),
    _Chan_max_total_load_rx_intv_Type()
)
chan_max_total_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_total_load_rx_intv.setStatus("mandatory")


class _Chan_max_total_load_rx_time_intv_Type(DisplayString):
    """Custom type chan_max_total_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chan_max_total_load_rx_time_intv_Type.__name__ = "DisplayString"
_Chan_max_total_load_rx_time_intv_Object = MibScalar
chan_max_total_load_rx_time_intv = _Chan_max_total_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 2, 1, 23),
    _Chan_max_total_load_rx_time_intv_Type()
)
chan_max_total_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chan_max_total_load_rx_time_intv.setStatus("mandatory")
_PvcPerfCurr_Table_Object = MibTable
pvcPerfCurr_Table = _PvcPerfCurr_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3)
)
if mibBuilder.loadTexts:
    pvcPerfCurr_Table.setStatus("mandatory")
_PvcPerfCurr_Entry_Object = MibTableRow
pvcPerfCurr_Entry = _PvcPerfCurr_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1)
)
pvcPerfCurr_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcPerfCurr-num-index"),
)
if mibBuilder.loadTexts:
    pvcPerfCurr_Entry.setStatus("mandatory")


class _PvcPerfCurr_num_index_Type(Integer32):
    """Custom type pvcPerfCurr_num_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcPerfCurr_num_index_Type.__name__ = "Integer32"
_PvcPerfCurr_num_index_Object = MibScalar
pvcPerfCurr_num_index = _PvcPerfCurr_num_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 1),
    _PvcPerfCurr_num_index_Type()
)
pvcPerfCurr_num_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurr_num_index.setStatus("mandatory")
_Pvc_tx_time_curr_Type = Integer32
_Pvc_tx_time_curr_Object = MibScalar
pvc_tx_time_curr = _Pvc_tx_time_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 2),
    _Pvc_tx_time_curr_Type()
)
pvc_tx_time_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_tx_time_curr.setStatus("mandatory")


class _Pvc_unavail_toDte_Type(DisplayString):
    """Custom type pvc_unavail_toDte based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_unavail_toDte_Type.__name__ = "DisplayString"
_Pvc_unavail_toDte_Object = MibScalar
pvc_unavail_toDte = _Pvc_unavail_toDte_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 3),
    _Pvc_unavail_toDte_Type()
)
pvc_unavail_toDte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_unavail_toDte.setStatus("mandatory")


class _Pvc_unavail_toDce_Type(DisplayString):
    """Custom type pvc_unavail_toDce based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_unavail_toDce_Type.__name__ = "DisplayString"
_Pvc_unavail_toDce_Object = MibScalar
pvc_unavail_toDce = _Pvc_unavail_toDce_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 4),
    _Pvc_unavail_toDce_Type()
)
pvc_unavail_toDce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_unavail_toDce.setStatus("mandatory")


class _Pvc_user_load_tx_curr_Type(DisplayString):
    """Custom type pvc_user_load_tx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_user_load_tx_curr_Type.__name__ = "DisplayString"
_Pvc_user_load_tx_curr_Object = MibScalar
pvc_user_load_tx_curr = _Pvc_user_load_tx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 5),
    _Pvc_user_load_tx_curr_Type()
)
pvc_user_load_tx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_user_load_tx_curr.setStatus("mandatory")


class _Pvc_user_load_rx_curr_Type(DisplayString):
    """Custom type pvc_user_load_rx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_user_load_rx_curr_Type.__name__ = "DisplayString"
_Pvc_user_load_rx_curr_Object = MibScalar
pvc_user_load_rx_curr = _Pvc_user_load_rx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 6),
    _Pvc_user_load_rx_curr_Type()
)
pvc_user_load_rx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_user_load_rx_curr.setStatus("mandatory")


class _Pvc_total_load_tx_curr_Type(DisplayString):
    """Custom type pvc_total_load_tx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_total_load_tx_curr_Type.__name__ = "DisplayString"
_Pvc_total_load_tx_curr_Object = MibScalar
pvc_total_load_tx_curr = _Pvc_total_load_tx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 7),
    _Pvc_total_load_tx_curr_Type()
)
pvc_total_load_tx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_total_load_tx_curr.setStatus("mandatory")


class _Pvc_total_load_rx_curr_Type(DisplayString):
    """Custom type pvc_total_load_rx_curr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_total_load_rx_curr_Type.__name__ = "DisplayString"
_Pvc_total_load_rx_curr_Object = MibScalar
pvc_total_load_rx_curr = _Pvc_total_load_rx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 8),
    _Pvc_total_load_rx_curr_Type()
)
pvc_total_load_rx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_total_load_rx_curr.setStatus("mandatory")
_Pvc_CIR_toNet_exceed_curr_Type = Integer32
_Pvc_CIR_toNet_exceed_curr_Object = MibScalar
pvc_CIR_toNet_exceed_curr = _Pvc_CIR_toNet_exceed_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 9),
    _Pvc_CIR_toNet_exceed_curr_Type()
)
pvc_CIR_toNet_exceed_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_CIR_toNet_exceed_curr.setStatus("mandatory")
_Pvc_EIR_toNet_exceed_curr_Type = Integer32
_Pvc_EIR_toNet_exceed_curr_Object = MibScalar
pvc_EIR_toNet_exceed_curr = _Pvc_EIR_toNet_exceed_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 10),
    _Pvc_EIR_toNet_exceed_curr_Type()
)
pvc_EIR_toNet_exceed_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_EIR_toNet_exceed_curr.setStatus("mandatory")
_Pvc_loss_frame_tx_curr_Type = Integer32
_Pvc_loss_frame_tx_curr_Object = MibScalar
pvc_loss_frame_tx_curr = _Pvc_loss_frame_tx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 11),
    _Pvc_loss_frame_tx_curr_Type()
)
pvc_loss_frame_tx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_loss_frame_tx_curr.setStatus("mandatory")
_Pvc_loss_frame_rx_curr_Type = Integer32
_Pvc_loss_frame_rx_curr_Object = MibScalar
pvc_loss_frame_rx_curr = _Pvc_loss_frame_rx_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 12),
    _Pvc_loss_frame_rx_curr_Type()
)
pvc_loss_frame_rx_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_loss_frame_rx_curr.setStatus("mandatory")
_Pvc_ip_tx_time_curr_Type = Integer32
_Pvc_ip_tx_time_curr_Object = MibScalar
pvc_ip_tx_time_curr = _Pvc_ip_tx_time_curr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 13),
    _Pvc_ip_tx_time_curr_Type()
)
pvc_ip_tx_time_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_ip_tx_time_curr.setStatus("mandatory")
_PvcIpRtrRxLatTxTimeCurr_Type = Integer32
_PvcIpRtrRxLatTxTimeCurr_Object = MibTableColumn
pvcIpRtrRxLatTxTimeCurr = _PvcIpRtrRxLatTxTimeCurr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 14),
    _PvcIpRtrRxLatTxTimeCurr_Type()
)
pvcIpRtrRxLatTxTimeCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIpRtrRxLatTxTimeCurr.setStatus("mandatory")
_PvcIpRtrTxLatTxTimeCurr_Type = Integer32
_PvcIpRtrTxLatTxTimeCurr_Object = MibTableColumn
pvcIpRtrTxLatTxTimeCurr = _PvcIpRtrTxLatTxTimeCurr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 3, 1, 15),
    _PvcIpRtrTxLatTxTimeCurr_Type()
)
pvcIpRtrTxLatTxTimeCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIpRtrTxLatTxTimeCurr.setStatus("mandatory")
_PvcPerfIntv_Table_Object = MibTable
pvcPerfIntv_Table = _PvcPerfIntv_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4)
)
if mibBuilder.loadTexts:
    pvcPerfIntv_Table.setStatus("mandatory")
_PvcPerfIntv_Entry_Object = MibTableRow
pvcPerfIntv_Entry = _PvcPerfIntv_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1)
)
pvcPerfIntv_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcPerfIntv-num-index"),
    (0, "LINK-PROBE-MIB", "pvcPerf-intv-index"),
)
if mibBuilder.loadTexts:
    pvcPerfIntv_Entry.setStatus("mandatory")


class _PvcPerfIntv_num_index_Type(Integer32):
    """Custom type pvcPerfIntv_num_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcPerfIntv_num_index_Type.__name__ = "Integer32"
_PvcPerfIntv_num_index_Object = MibScalar
pvcPerfIntv_num_index = _PvcPerfIntv_num_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 1),
    _PvcPerfIntv_num_index_Type()
)
pvcPerfIntv_num_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntv_num_index.setStatus("mandatory")


class _PvcPerf_intv_index_Type(Integer32):
    """Custom type pvcPerf_intv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvcPerf_intv_index_Type.__name__ = "Integer32"
_PvcPerf_intv_index_Object = MibScalar
pvcPerf_intv_index = _PvcPerf_intv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 2),
    _PvcPerf_intv_index_Type()
)
pvcPerf_intv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerf_intv_index.setStatus("mandatory")
_Pvc_tx_time_intv_Type = Integer32
_Pvc_tx_time_intv_Object = MibScalar
pvc_tx_time_intv = _Pvc_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 3),
    _Pvc_tx_time_intv_Type()
)
pvc_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_tx_time_intv.setStatus("mandatory")


class _Pvc_unavail_toDte_intv_Type(DisplayString):
    """Custom type pvc_unavail_toDte_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_unavail_toDte_intv_Type.__name__ = "DisplayString"
_Pvc_unavail_toDte_intv_Object = MibScalar
pvc_unavail_toDte_intv = _Pvc_unavail_toDte_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 4),
    _Pvc_unavail_toDte_intv_Type()
)
pvc_unavail_toDte_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_unavail_toDte_intv.setStatus("mandatory")


class _Pvc_unavail_toDce_intv_Type(DisplayString):
    """Custom type pvc_unavail_toDce_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_unavail_toDce_intv_Type.__name__ = "DisplayString"
_Pvc_unavail_toDce_intv_Object = MibScalar
pvc_unavail_toDce_intv = _Pvc_unavail_toDce_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 5),
    _Pvc_unavail_toDce_intv_Type()
)
pvc_unavail_toDce_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_unavail_toDce_intv.setStatus("mandatory")


class _Pvc_user_load_tx_intv_Type(DisplayString):
    """Custom type pvc_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_user_load_tx_intv_Type.__name__ = "DisplayString"
_Pvc_user_load_tx_intv_Object = MibScalar
pvc_user_load_tx_intv = _Pvc_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 6),
    _Pvc_user_load_tx_intv_Type()
)
pvc_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_user_load_tx_intv.setStatus("mandatory")


class _Pvc_user_load_rx_intv_Type(DisplayString):
    """Custom type pvc_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_user_load_rx_intv_Type.__name__ = "DisplayString"
_Pvc_user_load_rx_intv_Object = MibScalar
pvc_user_load_rx_intv = _Pvc_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 7),
    _Pvc_user_load_rx_intv_Type()
)
pvc_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_user_load_rx_intv.setStatus("mandatory")


class _Pvc_total_load_tx_intv_Type(DisplayString):
    """Custom type pvc_total_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_total_load_tx_intv_Type.__name__ = "DisplayString"
_Pvc_total_load_tx_intv_Object = MibScalar
pvc_total_load_tx_intv = _Pvc_total_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 8),
    _Pvc_total_load_tx_intv_Type()
)
pvc_total_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_total_load_tx_intv.setStatus("mandatory")


class _Pvc_total_load_rx_intv_Type(DisplayString):
    """Custom type pvc_total_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_total_load_rx_intv_Type.__name__ = "DisplayString"
_Pvc_total_load_rx_intv_Object = MibScalar
pvc_total_load_rx_intv = _Pvc_total_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 9),
    _Pvc_total_load_rx_intv_Type()
)
pvc_total_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_total_load_rx_intv.setStatus("mandatory")
_Pvc_CIR_toNet_exceed_intv_Type = Integer32
_Pvc_CIR_toNet_exceed_intv_Object = MibScalar
pvc_CIR_toNet_exceed_intv = _Pvc_CIR_toNet_exceed_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 10),
    _Pvc_CIR_toNet_exceed_intv_Type()
)
pvc_CIR_toNet_exceed_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_CIR_toNet_exceed_intv.setStatus("mandatory")
_Pvc_EIR_toNet_exceed_intv_Type = Integer32
_Pvc_EIR_toNet_exceed_intv_Object = MibScalar
pvc_EIR_toNet_exceed_intv = _Pvc_EIR_toNet_exceed_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 11),
    _Pvc_EIR_toNet_exceed_intv_Type()
)
pvc_EIR_toNet_exceed_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_EIR_toNet_exceed_intv.setStatus("mandatory")


class _Pvc_loss_frame_tx_intv_Type(Integer32):
    """Custom type pvc_loss_frame_tx_intv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("not-avail", 255)
    )


_Pvc_loss_frame_tx_intv_Type.__name__ = "Integer32"
_Pvc_loss_frame_tx_intv_Object = MibScalar
pvc_loss_frame_tx_intv = _Pvc_loss_frame_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 12),
    _Pvc_loss_frame_tx_intv_Type()
)
pvc_loss_frame_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_loss_frame_tx_intv.setStatus("mandatory")


class _Pvc_loss_frame_rx_intv_Type(Integer32):
    """Custom type pvc_loss_frame_rx_intv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("not-avail", 255)
    )


_Pvc_loss_frame_rx_intv_Type.__name__ = "Integer32"
_Pvc_loss_frame_rx_intv_Object = MibScalar
pvc_loss_frame_rx_intv = _Pvc_loss_frame_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 13),
    _Pvc_loss_frame_rx_intv_Type()
)
pvc_loss_frame_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_loss_frame_rx_intv.setStatus("mandatory")
_Pvc_ip_tx_time_intv_Type = Integer32
_Pvc_ip_tx_time_intv_Object = MibScalar
pvc_ip_tx_time_intv = _Pvc_ip_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 14),
    _Pvc_ip_tx_time_intv_Type()
)
pvc_ip_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_ip_tx_time_intv.setStatus("mandatory")
_PvcIpRtrRxLatTxTimeIntv_Type = Integer32
_PvcIpRtrRxLatTxTimeIntv_Object = MibTableColumn
pvcIpRtrRxLatTxTimeIntv = _PvcIpRtrRxLatTxTimeIntv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 15),
    _PvcIpRtrRxLatTxTimeIntv_Type()
)
pvcIpRtrRxLatTxTimeIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIpRtrRxLatTxTimeIntv.setStatus("mandatory")
_PvcIpRtrTxLatTxTimeIntv_Type = Integer32
_PvcIpRtrTxLatTxTimeIntv_Object = MibTableColumn
pvcIpRtrTxLatTxTimeIntv = _PvcIpRtrTxLatTxTimeIntv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 16),
    _PvcIpRtrTxLatTxTimeIntv_Type()
)
pvcIpRtrTxLatTxTimeIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIpRtrTxLatTxTimeIntv.setStatus("mandatory")
_Pvc_min_tx_time_intv_Type = Integer32
_Pvc_min_tx_time_intv_Object = MibScalar
pvc_min_tx_time_intv = _Pvc_min_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 17),
    _Pvc_min_tx_time_intv_Type()
)
pvc_min_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_tx_time_intv.setStatus("mandatory")


class _Pvc_min_tx_time_time_intv_Type(DisplayString):
    """Custom type pvc_min_tx_time_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_min_tx_time_time_intv_Type.__name__ = "DisplayString"
_Pvc_min_tx_time_time_intv_Object = MibScalar
pvc_min_tx_time_time_intv = _Pvc_min_tx_time_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 18),
    _Pvc_min_tx_time_time_intv_Type()
)
pvc_min_tx_time_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_tx_time_time_intv.setStatus("mandatory")


class _Pvc_min_user_load_tx_intv_Type(DisplayString):
    """Custom type pvc_min_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_min_user_load_tx_intv_Type.__name__ = "DisplayString"
_Pvc_min_user_load_tx_intv_Object = MibScalar
pvc_min_user_load_tx_intv = _Pvc_min_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 19),
    _Pvc_min_user_load_tx_intv_Type()
)
pvc_min_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_user_load_tx_intv.setStatus("mandatory")


class _Pvc_min_user_load_tx_time_intv_Type(DisplayString):
    """Custom type pvc_min_user_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_min_user_load_tx_time_intv_Type.__name__ = "DisplayString"
_Pvc_min_user_load_tx_time_intv_Object = MibScalar
pvc_min_user_load_tx_time_intv = _Pvc_min_user_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 20),
    _Pvc_min_user_load_tx_time_intv_Type()
)
pvc_min_user_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_user_load_tx_time_intv.setStatus("mandatory")


class _Pvc_min_user_load_rx_intv_Type(DisplayString):
    """Custom type pvc_min_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_min_user_load_rx_intv_Type.__name__ = "DisplayString"
_Pvc_min_user_load_rx_intv_Object = MibScalar
pvc_min_user_load_rx_intv = _Pvc_min_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 21),
    _Pvc_min_user_load_rx_intv_Type()
)
pvc_min_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_user_load_rx_intv.setStatus("mandatory")


class _Pvc_min_user_load_rx_time_intv_Type(DisplayString):
    """Custom type pvc_min_user_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_min_user_load_rx_time_intv_Type.__name__ = "DisplayString"
_Pvc_min_user_load_rx_time_intv_Object = MibScalar
pvc_min_user_load_rx_time_intv = _Pvc_min_user_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 22),
    _Pvc_min_user_load_rx_time_intv_Type()
)
pvc_min_user_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_user_load_rx_time_intv.setStatus("mandatory")


class _Pvc_min_total_load_tx_intv_Type(DisplayString):
    """Custom type pvc_min_total_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_min_total_load_tx_intv_Type.__name__ = "DisplayString"
_Pvc_min_total_load_tx_intv_Object = MibScalar
pvc_min_total_load_tx_intv = _Pvc_min_total_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 23),
    _Pvc_min_total_load_tx_intv_Type()
)
pvc_min_total_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_total_load_tx_intv.setStatus("mandatory")


class _Pvc_min_total_load_tx_time_intv_Type(DisplayString):
    """Custom type pvc_min_total_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_min_total_load_tx_time_intv_Type.__name__ = "DisplayString"
_Pvc_min_total_load_tx_time_intv_Object = MibScalar
pvc_min_total_load_tx_time_intv = _Pvc_min_total_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 24),
    _Pvc_min_total_load_tx_time_intv_Type()
)
pvc_min_total_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_total_load_tx_time_intv.setStatus("mandatory")


class _Pvc_min_total_load_rx_intv_Type(DisplayString):
    """Custom type pvc_min_total_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_min_total_load_rx_intv_Type.__name__ = "DisplayString"
_Pvc_min_total_load_rx_intv_Object = MibScalar
pvc_min_total_load_rx_intv = _Pvc_min_total_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 25),
    _Pvc_min_total_load_rx_intv_Type()
)
pvc_min_total_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_total_load_rx_intv.setStatus("mandatory")


class _Pvc_min_total_load_rx_time_intv_Type(DisplayString):
    """Custom type pvc_min_total_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_min_total_load_rx_time_intv_Type.__name__ = "DisplayString"
_Pvc_min_total_load_rx_time_intv_Object = MibScalar
pvc_min_total_load_rx_time_intv = _Pvc_min_total_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 26),
    _Pvc_min_total_load_rx_time_intv_Type()
)
pvc_min_total_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_total_load_rx_time_intv.setStatus("mandatory")
_Pvc_min_ip_tx_time_intv_Type = Integer32
_Pvc_min_ip_tx_time_intv_Object = MibScalar
pvc_min_ip_tx_time_intv = _Pvc_min_ip_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 27),
    _Pvc_min_ip_tx_time_intv_Type()
)
pvc_min_ip_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_ip_tx_time_intv.setStatus("mandatory")


class _Pvc_min_ip_tx_time_time_intv_Type(DisplayString):
    """Custom type pvc_min_ip_tx_time_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_min_ip_tx_time_time_intv_Type.__name__ = "DisplayString"
_Pvc_min_ip_tx_time_time_intv_Object = MibScalar
pvc_min_ip_tx_time_time_intv = _Pvc_min_ip_tx_time_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 28),
    _Pvc_min_ip_tx_time_time_intv_Type()
)
pvc_min_ip_tx_time_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_min_ip_tx_time_time_intv.setStatus("mandatory")
_Pvc_max_tx_time_intv_Type = Integer32
_Pvc_max_tx_time_intv_Object = MibScalar
pvc_max_tx_time_intv = _Pvc_max_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 29),
    _Pvc_max_tx_time_intv_Type()
)
pvc_max_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_tx_time_intv.setStatus("mandatory")


class _Pvc_max_tx_time_time_intv_Type(DisplayString):
    """Custom type pvc_max_tx_time_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_max_tx_time_time_intv_Type.__name__ = "DisplayString"
_Pvc_max_tx_time_time_intv_Object = MibScalar
pvc_max_tx_time_time_intv = _Pvc_max_tx_time_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 30),
    _Pvc_max_tx_time_time_intv_Type()
)
pvc_max_tx_time_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_tx_time_time_intv.setStatus("mandatory")


class _Pvc_max_user_load_tx_intv_Type(DisplayString):
    """Custom type pvc_max_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_max_user_load_tx_intv_Type.__name__ = "DisplayString"
_Pvc_max_user_load_tx_intv_Object = MibScalar
pvc_max_user_load_tx_intv = _Pvc_max_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 31),
    _Pvc_max_user_load_tx_intv_Type()
)
pvc_max_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_user_load_tx_intv.setStatus("mandatory")


class _Pvc_max_user_load_tx_time_intv_Type(DisplayString):
    """Custom type pvc_max_user_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_max_user_load_tx_time_intv_Type.__name__ = "DisplayString"
_Pvc_max_user_load_tx_time_intv_Object = MibScalar
pvc_max_user_load_tx_time_intv = _Pvc_max_user_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 32),
    _Pvc_max_user_load_tx_time_intv_Type()
)
pvc_max_user_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_user_load_tx_time_intv.setStatus("mandatory")


class _Pvc_max_user_load_rx_intv_Type(DisplayString):
    """Custom type pvc_max_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_max_user_load_rx_intv_Type.__name__ = "DisplayString"
_Pvc_max_user_load_rx_intv_Object = MibScalar
pvc_max_user_load_rx_intv = _Pvc_max_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 33),
    _Pvc_max_user_load_rx_intv_Type()
)
pvc_max_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_user_load_rx_intv.setStatus("mandatory")


class _Pvc_max_user_load_rx_time_intv_Type(DisplayString):
    """Custom type pvc_max_user_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_max_user_load_rx_time_intv_Type.__name__ = "DisplayString"
_Pvc_max_user_load_rx_time_intv_Object = MibScalar
pvc_max_user_load_rx_time_intv = _Pvc_max_user_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 34),
    _Pvc_max_user_load_rx_time_intv_Type()
)
pvc_max_user_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_user_load_rx_time_intv.setStatus("mandatory")


class _Pvc_max_total_load_tx_intv_Type(DisplayString):
    """Custom type pvc_max_total_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_max_total_load_tx_intv_Type.__name__ = "DisplayString"
_Pvc_max_total_load_tx_intv_Object = MibScalar
pvc_max_total_load_tx_intv = _Pvc_max_total_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 35),
    _Pvc_max_total_load_tx_intv_Type()
)
pvc_max_total_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_total_load_tx_intv.setStatus("mandatory")


class _Pvc_max_total_load_tx_time_intv_Type(DisplayString):
    """Custom type pvc_max_total_load_tx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_max_total_load_tx_time_intv_Type.__name__ = "DisplayString"
_Pvc_max_total_load_tx_time_intv_Object = MibScalar
pvc_max_total_load_tx_time_intv = _Pvc_max_total_load_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 36),
    _Pvc_max_total_load_tx_time_intv_Type()
)
pvc_max_total_load_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_total_load_tx_time_intv.setStatus("mandatory")


class _Pvc_max_total_load_rx_intv_Type(DisplayString):
    """Custom type pvc_max_total_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Pvc_max_total_load_rx_intv_Type.__name__ = "DisplayString"
_Pvc_max_total_load_rx_intv_Object = MibScalar
pvc_max_total_load_rx_intv = _Pvc_max_total_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 37),
    _Pvc_max_total_load_rx_intv_Type()
)
pvc_max_total_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_total_load_rx_intv.setStatus("mandatory")


class _Pvc_max_total_load_rx_time_intv_Type(DisplayString):
    """Custom type pvc_max_total_load_rx_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_max_total_load_rx_time_intv_Type.__name__ = "DisplayString"
_Pvc_max_total_load_rx_time_intv_Object = MibScalar
pvc_max_total_load_rx_time_intv = _Pvc_max_total_load_rx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 38),
    _Pvc_max_total_load_rx_time_intv_Type()
)
pvc_max_total_load_rx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_total_load_rx_time_intv.setStatus("mandatory")
_Pvc_max_ip_tx_time_intv_Type = Integer32
_Pvc_max_ip_tx_time_intv_Object = MibScalar
pvc_max_ip_tx_time_intv = _Pvc_max_ip_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 39),
    _Pvc_max_ip_tx_time_intv_Type()
)
pvc_max_ip_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_ip_tx_time_intv.setStatus("mandatory")


class _Pvc_max_ip_tx_time_time_intv_Type(DisplayString):
    """Custom type pvc_max_ip_tx_time_time_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pvc_max_ip_tx_time_time_intv_Type.__name__ = "DisplayString"
_Pvc_max_ip_tx_time_time_intv_Object = MibScalar
pvc_max_ip_tx_time_time_intv = _Pvc_max_ip_tx_time_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 3, 4, 1, 40),
    _Pvc_max_ip_tx_time_time_intv_Type()
)
pvc_max_ip_tx_time_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvc_max_ip_tx_time_time_intv.setStatus("mandatory")
_ProbeTrafficShape_ObjectIdentity = ObjectIdentity
probeTrafficShape = _ProbeTrafficShape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 4)
)
_PvcShapeThresh_ObjectIdentity = ObjectIdentity
pvcShapeThresh = _PvcShapeThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1)
)


class _PvcShapeThreshLevel_1_Type(Integer32):
    """Custom type pvcShapeThreshLevel_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeThreshLevel_1_Type.__name__ = "Integer32"
_PvcShapeThreshLevel_1_Object = MibScalar
pvcShapeThreshLevel_1 = _PvcShapeThreshLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1, 1),
    _PvcShapeThreshLevel_1_Type()
)
pvcShapeThreshLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeThreshLevel_1.setStatus("mandatory")


class _PvcShapeThreshLevel_2_Type(Integer32):
    """Custom type pvcShapeThreshLevel_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeThreshLevel_2_Type.__name__ = "Integer32"
_PvcShapeThreshLevel_2_Object = MibScalar
pvcShapeThreshLevel_2 = _PvcShapeThreshLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1, 2),
    _PvcShapeThreshLevel_2_Type()
)
pvcShapeThreshLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeThreshLevel_2.setStatus("mandatory")


class _PvcShapeThreshLevel_3_Type(Integer32):
    """Custom type pvcShapeThreshLevel_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeThreshLevel_3_Type.__name__ = "Integer32"
_PvcShapeThreshLevel_3_Object = MibScalar
pvcShapeThreshLevel_3 = _PvcShapeThreshLevel_3_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1, 3),
    _PvcShapeThreshLevel_3_Type()
)
pvcShapeThreshLevel_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeThreshLevel_3.setStatus("mandatory")


class _PvcShapeThreshLevel_4_Type(Integer32):
    """Custom type pvcShapeThreshLevel_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeThreshLevel_4_Type.__name__ = "Integer32"
_PvcShapeThreshLevel_4_Object = MibScalar
pvcShapeThreshLevel_4 = _PvcShapeThreshLevel_4_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1, 4),
    _PvcShapeThreshLevel_4_Type()
)
pvcShapeThreshLevel_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeThreshLevel_4.setStatus("mandatory")


class _PvcShapeThreshLevel_5_Type(Integer32):
    """Custom type pvcShapeThreshLevel_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeThreshLevel_5_Type.__name__ = "Integer32"
_PvcShapeThreshLevel_5_Object = MibScalar
pvcShapeThreshLevel_5 = _PvcShapeThreshLevel_5_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1, 5),
    _PvcShapeThreshLevel_5_Type()
)
pvcShapeThreshLevel_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeThreshLevel_5.setStatus("mandatory")


class _PvcShapeThreshLevel_6_Type(Integer32):
    """Custom type pvcShapeThreshLevel_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeThreshLevel_6_Type.__name__ = "Integer32"
_PvcShapeThreshLevel_6_Object = MibScalar
pvcShapeThreshLevel_6 = _PvcShapeThreshLevel_6_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1, 6),
    _PvcShapeThreshLevel_6_Type()
)
pvcShapeThreshLevel_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeThreshLevel_6.setStatus("mandatory")
_PvcShapeThreshLevel_7_Type = Integer32
_PvcShapeThreshLevel_7_Object = MibScalar
pvcShapeThreshLevel_7 = _PvcShapeThreshLevel_7_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 1, 7),
    _PvcShapeThreshLevel_7_Type()
)
pvcShapeThreshLevel_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeThreshLevel_7.setStatus("mandatory")
_PvcShapeCurrToDce_Table_Object = MibTable
pvcShapeCurrToDce_Table = _PvcShapeCurrToDce_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2)
)
if mibBuilder.loadTexts:
    pvcShapeCurrToDce_Table.setStatus("mandatory")
_PvcShapeCurrToDce_Entry_Object = MibTableRow
pvcShapeCurrToDce_Entry = _PvcShapeCurrToDce_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1)
)
pvcShapeCurrToDce_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcShapeCurrToDce-index"),
)
if mibBuilder.loadTexts:
    pvcShapeCurrToDce_Entry.setStatus("mandatory")


class _PvcShapeCurrToDce_index_Type(Integer32):
    """Custom type pvcShapeCurrToDce_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcShapeCurrToDce_index_Type.__name__ = "Integer32"
_PvcShapeCurrToDce_index_Object = MibScalar
pvcShapeCurrToDce_index = _PvcShapeCurrToDce_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 1),
    _PvcShapeCurrToDce_index_Type()
)
pvcShapeCurrToDce_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDce_index.setStatus("mandatory")


class _PvcShapeCurrToDceLevel_1_Type(Integer32):
    """Custom type pvcShapeCurrToDceLevel_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDceLevel_1_Type.__name__ = "Integer32"
_PvcShapeCurrToDceLevel_1_Object = MibScalar
pvcShapeCurrToDceLevel_1 = _PvcShapeCurrToDceLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 2),
    _PvcShapeCurrToDceLevel_1_Type()
)
pvcShapeCurrToDceLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDceLevel_1.setStatus("mandatory")


class _PvcShapeCurrToDceLevel_2_Type(Integer32):
    """Custom type pvcShapeCurrToDceLevel_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDceLevel_2_Type.__name__ = "Integer32"
_PvcShapeCurrToDceLevel_2_Object = MibScalar
pvcShapeCurrToDceLevel_2 = _PvcShapeCurrToDceLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 3),
    _PvcShapeCurrToDceLevel_2_Type()
)
pvcShapeCurrToDceLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDceLevel_2.setStatus("mandatory")


class _PvcShapeCurrToDceLevel_3_Type(Integer32):
    """Custom type pvcShapeCurrToDceLevel_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDceLevel_3_Type.__name__ = "Integer32"
_PvcShapeCurrToDceLevel_3_Object = MibScalar
pvcShapeCurrToDceLevel_3 = _PvcShapeCurrToDceLevel_3_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 4),
    _PvcShapeCurrToDceLevel_3_Type()
)
pvcShapeCurrToDceLevel_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDceLevel_3.setStatus("mandatory")


class _PvcShapeCurrToDceLevel_4_Type(Integer32):
    """Custom type pvcShapeCurrToDceLevel_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDceLevel_4_Type.__name__ = "Integer32"
_PvcShapeCurrToDceLevel_4_Object = MibScalar
pvcShapeCurrToDceLevel_4 = _PvcShapeCurrToDceLevel_4_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 5),
    _PvcShapeCurrToDceLevel_4_Type()
)
pvcShapeCurrToDceLevel_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDceLevel_4.setStatus("mandatory")


class _PvcShapeCurrToDceLevel_5_Type(Integer32):
    """Custom type pvcShapeCurrToDceLevel_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDceLevel_5_Type.__name__ = "Integer32"
_PvcShapeCurrToDceLevel_5_Object = MibScalar
pvcShapeCurrToDceLevel_5 = _PvcShapeCurrToDceLevel_5_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 6),
    _PvcShapeCurrToDceLevel_5_Type()
)
pvcShapeCurrToDceLevel_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDceLevel_5.setStatus("mandatory")


class _PvcShapeCurrToDceLevel_6_Type(Integer32):
    """Custom type pvcShapeCurrToDceLevel_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDceLevel_6_Type.__name__ = "Integer32"
_PvcShapeCurrToDceLevel_6_Object = MibScalar
pvcShapeCurrToDceLevel_6 = _PvcShapeCurrToDceLevel_6_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 7),
    _PvcShapeCurrToDceLevel_6_Type()
)
pvcShapeCurrToDceLevel_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDceLevel_6.setStatus("mandatory")


class _PvcShapeCurrToDceLevel_7_Type(Integer32):
    """Custom type pvcShapeCurrToDceLevel_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDceLevel_7_Type.__name__ = "Integer32"
_PvcShapeCurrToDceLevel_7_Object = MibScalar
pvcShapeCurrToDceLevel_7 = _PvcShapeCurrToDceLevel_7_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 2, 1, 8),
    _PvcShapeCurrToDceLevel_7_Type()
)
pvcShapeCurrToDceLevel_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDceLevel_7.setStatus("mandatory")
_PvcShapeCurrToDte_Table_Object = MibTable
pvcShapeCurrToDte_Table = _PvcShapeCurrToDte_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3)
)
if mibBuilder.loadTexts:
    pvcShapeCurrToDte_Table.setStatus("mandatory")
_PvcShapeCurrToDte_Entry_Object = MibTableRow
pvcShapeCurrToDte_Entry = _PvcShapeCurrToDte_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1)
)
pvcShapeCurrToDte_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcShapeCurrToDte-index"),
)
if mibBuilder.loadTexts:
    pvcShapeCurrToDte_Entry.setStatus("mandatory")


class _PvcShapeCurrToDte_index_Type(Integer32):
    """Custom type pvcShapeCurrToDte_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcShapeCurrToDte_index_Type.__name__ = "Integer32"
_PvcShapeCurrToDte_index_Object = MibScalar
pvcShapeCurrToDte_index = _PvcShapeCurrToDte_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 1),
    _PvcShapeCurrToDte_index_Type()
)
pvcShapeCurrToDte_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDte_index.setStatus("mandatory")


class _PvcShapeCurrToDteLevel_1_Type(Integer32):
    """Custom type pvcShapeCurrToDteLevel_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDteLevel_1_Type.__name__ = "Integer32"
_PvcShapeCurrToDteLevel_1_Object = MibScalar
pvcShapeCurrToDteLevel_1 = _PvcShapeCurrToDteLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 2),
    _PvcShapeCurrToDteLevel_1_Type()
)
pvcShapeCurrToDteLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDteLevel_1.setStatus("mandatory")


class _PvcShapeCurrToDteLevel_2_Type(Integer32):
    """Custom type pvcShapeCurrToDteLevel_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDteLevel_2_Type.__name__ = "Integer32"
_PvcShapeCurrToDteLevel_2_Object = MibScalar
pvcShapeCurrToDteLevel_2 = _PvcShapeCurrToDteLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 3),
    _PvcShapeCurrToDteLevel_2_Type()
)
pvcShapeCurrToDteLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDteLevel_2.setStatus("mandatory")


class _PvcShapeCurrToDteLevel_3_Type(Integer32):
    """Custom type pvcShapeCurrToDteLevel_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDteLevel_3_Type.__name__ = "Integer32"
_PvcShapeCurrToDteLevel_3_Object = MibScalar
pvcShapeCurrToDteLevel_3 = _PvcShapeCurrToDteLevel_3_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 4),
    _PvcShapeCurrToDteLevel_3_Type()
)
pvcShapeCurrToDteLevel_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDteLevel_3.setStatus("mandatory")


class _PvcShapeCurrToDteLevel_4_Type(Integer32):
    """Custom type pvcShapeCurrToDteLevel_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDteLevel_4_Type.__name__ = "Integer32"
_PvcShapeCurrToDteLevel_4_Object = MibScalar
pvcShapeCurrToDteLevel_4 = _PvcShapeCurrToDteLevel_4_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 5),
    _PvcShapeCurrToDteLevel_4_Type()
)
pvcShapeCurrToDteLevel_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDteLevel_4.setStatus("mandatory")


class _PvcShapeCurrToDteLevel_5_Type(Integer32):
    """Custom type pvcShapeCurrToDteLevel_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDteLevel_5_Type.__name__ = "Integer32"
_PvcShapeCurrToDteLevel_5_Object = MibScalar
pvcShapeCurrToDteLevel_5 = _PvcShapeCurrToDteLevel_5_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 6),
    _PvcShapeCurrToDteLevel_5_Type()
)
pvcShapeCurrToDteLevel_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDteLevel_5.setStatus("mandatory")


class _PvcShapeCurrToDteLevel_6_Type(Integer32):
    """Custom type pvcShapeCurrToDteLevel_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDteLevel_6_Type.__name__ = "Integer32"
_PvcShapeCurrToDteLevel_6_Object = MibScalar
pvcShapeCurrToDteLevel_6 = _PvcShapeCurrToDteLevel_6_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 7),
    _PvcShapeCurrToDteLevel_6_Type()
)
pvcShapeCurrToDteLevel_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDteLevel_6.setStatus("mandatory")


class _PvcShapeCurrToDteLevel_7_Type(Integer32):
    """Custom type pvcShapeCurrToDteLevel_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeCurrToDteLevel_7_Type.__name__ = "Integer32"
_PvcShapeCurrToDteLevel_7_Object = MibScalar
pvcShapeCurrToDteLevel_7 = _PvcShapeCurrToDteLevel_7_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 3, 1, 8),
    _PvcShapeCurrToDteLevel_7_Type()
)
pvcShapeCurrToDteLevel_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeCurrToDteLevel_7.setStatus("mandatory")
_PvcShapeIntvToDce_Table_Object = MibTable
pvcShapeIntvToDce_Table = _PvcShapeIntvToDce_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4)
)
if mibBuilder.loadTexts:
    pvcShapeIntvToDce_Table.setStatus("mandatory")
_PvcShapeIntvToDce_Entry_Object = MibTableRow
pvcShapeIntvToDce_Entry = _PvcShapeIntvToDce_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1)
)
pvcShapeIntvToDce_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcShapeIntvToDce-pvcIx"),
    (0, "LINK-PROBE-MIB", "pvcShapeIntvToDce-intvIx"),
)
if mibBuilder.loadTexts:
    pvcShapeIntvToDce_Entry.setStatus("mandatory")


class _PvcShapeIntvToDce_pvcIx_Type(Integer32):
    """Custom type pvcShapeIntvToDce_pvcIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcShapeIntvToDce_pvcIx_Type.__name__ = "Integer32"
_PvcShapeIntvToDce_pvcIx_Object = MibScalar
pvcShapeIntvToDce_pvcIx = _PvcShapeIntvToDce_pvcIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 1),
    _PvcShapeIntvToDce_pvcIx_Type()
)
pvcShapeIntvToDce_pvcIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDce_pvcIx.setStatus("mandatory")


class _PvcShapeIntvToDce_intvIx_Type(Integer32):
    """Custom type pvcShapeIntvToDce_intvIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvcShapeIntvToDce_intvIx_Type.__name__ = "Integer32"
_PvcShapeIntvToDce_intvIx_Object = MibScalar
pvcShapeIntvToDce_intvIx = _PvcShapeIntvToDce_intvIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 2),
    _PvcShapeIntvToDce_intvIx_Type()
)
pvcShapeIntvToDce_intvIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDce_intvIx.setStatus("mandatory")


class _PvcShapeIntvToDceLevel_1_Type(Integer32):
    """Custom type pvcShapeIntvToDceLevel_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDceLevel_1_Type.__name__ = "Integer32"
_PvcShapeIntvToDceLevel_1_Object = MibScalar
pvcShapeIntvToDceLevel_1 = _PvcShapeIntvToDceLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 3),
    _PvcShapeIntvToDceLevel_1_Type()
)
pvcShapeIntvToDceLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDceLevel_1.setStatus("mandatory")


class _PvcShapeIntvToDceLevel_2_Type(Integer32):
    """Custom type pvcShapeIntvToDceLevel_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDceLevel_2_Type.__name__ = "Integer32"
_PvcShapeIntvToDceLevel_2_Object = MibScalar
pvcShapeIntvToDceLevel_2 = _PvcShapeIntvToDceLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 4),
    _PvcShapeIntvToDceLevel_2_Type()
)
pvcShapeIntvToDceLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDceLevel_2.setStatus("mandatory")


class _PvcShapeIntvToDceLevel_3_Type(Integer32):
    """Custom type pvcShapeIntvToDceLevel_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDceLevel_3_Type.__name__ = "Integer32"
_PvcShapeIntvToDceLevel_3_Object = MibScalar
pvcShapeIntvToDceLevel_3 = _PvcShapeIntvToDceLevel_3_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 5),
    _PvcShapeIntvToDceLevel_3_Type()
)
pvcShapeIntvToDceLevel_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDceLevel_3.setStatus("mandatory")


class _PvcShapeIntvToDceLevel_4_Type(Integer32):
    """Custom type pvcShapeIntvToDceLevel_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDceLevel_4_Type.__name__ = "Integer32"
_PvcShapeIntvToDceLevel_4_Object = MibScalar
pvcShapeIntvToDceLevel_4 = _PvcShapeIntvToDceLevel_4_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 6),
    _PvcShapeIntvToDceLevel_4_Type()
)
pvcShapeIntvToDceLevel_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDceLevel_4.setStatus("mandatory")


class _PvcShapeIntvToDceLevel_5_Type(Integer32):
    """Custom type pvcShapeIntvToDceLevel_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDceLevel_5_Type.__name__ = "Integer32"
_PvcShapeIntvToDceLevel_5_Object = MibScalar
pvcShapeIntvToDceLevel_5 = _PvcShapeIntvToDceLevel_5_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 7),
    _PvcShapeIntvToDceLevel_5_Type()
)
pvcShapeIntvToDceLevel_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDceLevel_5.setStatus("mandatory")


class _PvcShapeIntvToDceLevel_6_Type(Integer32):
    """Custom type pvcShapeIntvToDceLevel_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDceLevel_6_Type.__name__ = "Integer32"
_PvcShapeIntvToDceLevel_6_Object = MibScalar
pvcShapeIntvToDceLevel_6 = _PvcShapeIntvToDceLevel_6_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 8),
    _PvcShapeIntvToDceLevel_6_Type()
)
pvcShapeIntvToDceLevel_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDceLevel_6.setStatus("mandatory")


class _PvcShapeIntvToDceLevel_7_Type(Integer32):
    """Custom type pvcShapeIntvToDceLevel_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDceLevel_7_Type.__name__ = "Integer32"
_PvcShapeIntvToDceLevel_7_Object = MibScalar
pvcShapeIntvToDceLevel_7 = _PvcShapeIntvToDceLevel_7_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 4, 1, 9),
    _PvcShapeIntvToDceLevel_7_Type()
)
pvcShapeIntvToDceLevel_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDceLevel_7.setStatus("mandatory")
_PvcShapeIntvToDte_Table_Object = MibTable
pvcShapeIntvToDte_Table = _PvcShapeIntvToDte_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5)
)
if mibBuilder.loadTexts:
    pvcShapeIntvToDte_Table.setStatus("mandatory")
_PvcShapeIntvToDte_Entry_Object = MibTableRow
pvcShapeIntvToDte_Entry = _PvcShapeIntvToDte_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1)
)
pvcShapeIntvToDte_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcShapeIntvToDte-pvcIx"),
    (0, "LINK-PROBE-MIB", "pvcShapeIntvToDte-intvIx"),
)
if mibBuilder.loadTexts:
    pvcShapeIntvToDte_Entry.setStatus("mandatory")


class _PvcShapeIntvToDte_pvcIx_Type(Integer32):
    """Custom type pvcShapeIntvToDte_pvcIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcShapeIntvToDte_pvcIx_Type.__name__ = "Integer32"
_PvcShapeIntvToDte_pvcIx_Object = MibScalar
pvcShapeIntvToDte_pvcIx = _PvcShapeIntvToDte_pvcIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 1),
    _PvcShapeIntvToDte_pvcIx_Type()
)
pvcShapeIntvToDte_pvcIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDte_pvcIx.setStatus("mandatory")


class _PvcShapeIntvToDte_intvIx_Type(Integer32):
    """Custom type pvcShapeIntvToDte_intvIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvcShapeIntvToDte_intvIx_Type.__name__ = "Integer32"
_PvcShapeIntvToDte_intvIx_Object = MibScalar
pvcShapeIntvToDte_intvIx = _PvcShapeIntvToDte_intvIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 2),
    _PvcShapeIntvToDte_intvIx_Type()
)
pvcShapeIntvToDte_intvIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDte_intvIx.setStatus("mandatory")


class _PvcShapeIntvToDteLevel_1_Type(Integer32):
    """Custom type pvcShapeIntvToDteLevel_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDteLevel_1_Type.__name__ = "Integer32"
_PvcShapeIntvToDteLevel_1_Object = MibScalar
pvcShapeIntvToDteLevel_1 = _PvcShapeIntvToDteLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 3),
    _PvcShapeIntvToDteLevel_1_Type()
)
pvcShapeIntvToDteLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDteLevel_1.setStatus("mandatory")


class _PvcShapeIntvToDteLevel_2_Type(Integer32):
    """Custom type pvcShapeIntvToDteLevel_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDteLevel_2_Type.__name__ = "Integer32"
_PvcShapeIntvToDteLevel_2_Object = MibScalar
pvcShapeIntvToDteLevel_2 = _PvcShapeIntvToDteLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 4),
    _PvcShapeIntvToDteLevel_2_Type()
)
pvcShapeIntvToDteLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDteLevel_2.setStatus("mandatory")


class _PvcShapeIntvToDteLevel_3_Type(Integer32):
    """Custom type pvcShapeIntvToDteLevel_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDteLevel_3_Type.__name__ = "Integer32"
_PvcShapeIntvToDteLevel_3_Object = MibScalar
pvcShapeIntvToDteLevel_3 = _PvcShapeIntvToDteLevel_3_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 5),
    _PvcShapeIntvToDteLevel_3_Type()
)
pvcShapeIntvToDteLevel_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDteLevel_3.setStatus("mandatory")


class _PvcShapeIntvToDteLevel_4_Type(Integer32):
    """Custom type pvcShapeIntvToDteLevel_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDteLevel_4_Type.__name__ = "Integer32"
_PvcShapeIntvToDteLevel_4_Object = MibScalar
pvcShapeIntvToDteLevel_4 = _PvcShapeIntvToDteLevel_4_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 6),
    _PvcShapeIntvToDteLevel_4_Type()
)
pvcShapeIntvToDteLevel_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDteLevel_4.setStatus("mandatory")


class _PvcShapeIntvToDteLevel_5_Type(Integer32):
    """Custom type pvcShapeIntvToDteLevel_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDteLevel_5_Type.__name__ = "Integer32"
_PvcShapeIntvToDteLevel_5_Object = MibScalar
pvcShapeIntvToDteLevel_5 = _PvcShapeIntvToDteLevel_5_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 7),
    _PvcShapeIntvToDteLevel_5_Type()
)
pvcShapeIntvToDteLevel_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDteLevel_5.setStatus("mandatory")


class _PvcShapeIntvToDteLevel_6_Type(Integer32):
    """Custom type pvcShapeIntvToDteLevel_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDteLevel_6_Type.__name__ = "Integer32"
_PvcShapeIntvToDteLevel_6_Object = MibScalar
pvcShapeIntvToDteLevel_6 = _PvcShapeIntvToDteLevel_6_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 8),
    _PvcShapeIntvToDteLevel_6_Type()
)
pvcShapeIntvToDteLevel_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDteLevel_6.setStatus("mandatory")


class _PvcShapeIntvToDteLevel_7_Type(Integer32):
    """Custom type pvcShapeIntvToDteLevel_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PvcShapeIntvToDteLevel_7_Type.__name__ = "Integer32"
_PvcShapeIntvToDteLevel_7_Object = MibScalar
pvcShapeIntvToDteLevel_7 = _PvcShapeIntvToDteLevel_7_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 4, 5, 1, 9),
    _PvcShapeIntvToDteLevel_7_Type()
)
pvcShapeIntvToDteLevel_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcShapeIntvToDteLevel_7.setStatus("mandatory")
_ProbeHistorical_ObjectIdentity = ObjectIdentity
probeHistorical = _ProbeHistorical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 5)
)
_HistIntvStartTimeIntv_Table_Object = MibTable
histIntvStartTimeIntv_Table = _HistIntvStartTimeIntv_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 1)
)
if mibBuilder.loadTexts:
    histIntvStartTimeIntv_Table.setStatus("mandatory")
_HistIntvStartTimeIntv_Entry_Object = MibTableRow
histIntvStartTimeIntv_Entry = _HistIntvStartTimeIntv_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 1, 1)
)
histIntvStartTimeIntv_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "histIntvStartTimeIntv-index"),
)
if mibBuilder.loadTexts:
    histIntvStartTimeIntv_Entry.setStatus("mandatory")


class _HistIntvStartTimeIntv_index_Type(Integer32):
    """Custom type histIntvStartTimeIntv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HistIntvStartTimeIntv_index_Type.__name__ = "Integer32"
_HistIntvStartTimeIntv_index_Object = MibScalar
histIntvStartTimeIntv_index = _HistIntvStartTimeIntv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 1, 1, 1),
    _HistIntvStartTimeIntv_index_Type()
)
histIntvStartTimeIntv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histIntvStartTimeIntv_index.setStatus("mandatory")


class _Hist_intv_start_time_Type(DisplayString):
    """Custom type hist_intv_start_time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hist_intv_start_time_Type.__name__ = "DisplayString"
_Hist_intv_start_time_Object = MibScalar
hist_intv_start_time = _Hist_intv_start_time_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 1, 1, 2),
    _Hist_intv_start_time_Type()
)
hist_intv_start_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_intv_start_time.setStatus("mandatory")
_HistChanPerfIntv_Table_Object = MibTable
histChanPerfIntv_Table = _HistChanPerfIntv_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 2)
)
if mibBuilder.loadTexts:
    histChanPerfIntv_Table.setStatus("mandatory")
_HistChanPerfIntv_Entry_Object = MibTableRow
histChanPerfIntv_Entry = _HistChanPerfIntv_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 2, 1)
)
histChanPerfIntv_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "histChanPerfIntv-index"),
)
if mibBuilder.loadTexts:
    histChanPerfIntv_Entry.setStatus("mandatory")


class _HistChanPerfIntv_index_Type(Integer32):
    """Custom type histChanPerfIntv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HistChanPerfIntv_index_Type.__name__ = "Integer32"
_HistChanPerfIntv_index_Object = MibScalar
histChanPerfIntv_index = _HistChanPerfIntv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 2, 1, 1),
    _HistChanPerfIntv_index_Type()
)
histChanPerfIntv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histChanPerfIntv_index.setStatus("mandatory")


class _Hist_chan_unavail_toDte_intv_Type(DisplayString):
    """Custom type hist_chan_unavail_toDte_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_chan_unavail_toDte_intv_Type.__name__ = "DisplayString"
_Hist_chan_unavail_toDte_intv_Object = MibScalar
hist_chan_unavail_toDte_intv = _Hist_chan_unavail_toDte_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 2, 1, 2),
    _Hist_chan_unavail_toDte_intv_Type()
)
hist_chan_unavail_toDte_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_chan_unavail_toDte_intv.setStatus("mandatory")


class _Hist_chan_unavail_toDce_intv_Type(DisplayString):
    """Custom type hist_chan_unavail_toDce_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_chan_unavail_toDce_intv_Type.__name__ = "DisplayString"
_Hist_chan_unavail_toDce_intv_Object = MibScalar
hist_chan_unavail_toDce_intv = _Hist_chan_unavail_toDce_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 2, 1, 3),
    _Hist_chan_unavail_toDce_intv_Type()
)
hist_chan_unavail_toDce_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_chan_unavail_toDce_intv.setStatus("mandatory")


class _Hist_chan_user_load_tx_intv_Type(DisplayString):
    """Custom type hist_chan_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_chan_user_load_tx_intv_Type.__name__ = "DisplayString"
_Hist_chan_user_load_tx_intv_Object = MibScalar
hist_chan_user_load_tx_intv = _Hist_chan_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 2, 1, 4),
    _Hist_chan_user_load_tx_intv_Type()
)
hist_chan_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_chan_user_load_tx_intv.setStatus("mandatory")


class _Hist_chan_user_load_rx_intv_Type(DisplayString):
    """Custom type hist_chan_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_chan_user_load_rx_intv_Type.__name__ = "DisplayString"
_Hist_chan_user_load_rx_intv_Object = MibScalar
hist_chan_user_load_rx_intv = _Hist_chan_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 2, 1, 5),
    _Hist_chan_user_load_rx_intv_Type()
)
hist_chan_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_chan_user_load_rx_intv.setStatus("mandatory")
_HistPvcPerfIntv_Table_Object = MibTable
histPvcPerfIntv_Table = _HistPvcPerfIntv_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3)
)
if mibBuilder.loadTexts:
    histPvcPerfIntv_Table.setStatus("mandatory")
_HistPvcPerfIntv_Entry_Object = MibTableRow
histPvcPerfIntv_Entry = _HistPvcPerfIntv_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1)
)
histPvcPerfIntv_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "histPvcPerfIntv-num-index"),
    (0, "LINK-PROBE-MIB", "histPvcPerf-intv-index"),
)
if mibBuilder.loadTexts:
    histPvcPerfIntv_Entry.setStatus("mandatory")


class _HistPvcPerfIntv_num_index_Type(Integer32):
    """Custom type histPvcPerfIntv_num_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_HistPvcPerfIntv_num_index_Type.__name__ = "Integer32"
_HistPvcPerfIntv_num_index_Object = MibScalar
histPvcPerfIntv_num_index = _HistPvcPerfIntv_num_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 1),
    _HistPvcPerfIntv_num_index_Type()
)
histPvcPerfIntv_num_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcPerfIntv_num_index.setStatus("mandatory")


class _HistPvcPerf_intv_index_Type(Integer32):
    """Custom type histPvcPerf_intv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HistPvcPerf_intv_index_Type.__name__ = "Integer32"
_HistPvcPerf_intv_index_Object = MibScalar
histPvcPerf_intv_index = _HistPvcPerf_intv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 2),
    _HistPvcPerf_intv_index_Type()
)
histPvcPerf_intv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcPerf_intv_index.setStatus("mandatory")
_Hist_pvc_tx_time_intv_Type = Integer32
_Hist_pvc_tx_time_intv_Object = MibScalar
hist_pvc_tx_time_intv = _Hist_pvc_tx_time_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 3),
    _Hist_pvc_tx_time_intv_Type()
)
hist_pvc_tx_time_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_tx_time_intv.setStatus("mandatory")


class _Hist_pvc_unavail_toDte_intv_Type(DisplayString):
    """Custom type hist_pvc_unavail_toDte_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_pvc_unavail_toDte_intv_Type.__name__ = "DisplayString"
_Hist_pvc_unavail_toDte_intv_Object = MibScalar
hist_pvc_unavail_toDte_intv = _Hist_pvc_unavail_toDte_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 4),
    _Hist_pvc_unavail_toDte_intv_Type()
)
hist_pvc_unavail_toDte_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_unavail_toDte_intv.setStatus("mandatory")


class _Hist_pvc_unavail_toDce_intv_Type(DisplayString):
    """Custom type hist_pvc_unavail_toDce_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_pvc_unavail_toDce_intv_Type.__name__ = "DisplayString"
_Hist_pvc_unavail_toDce_intv_Object = MibScalar
hist_pvc_unavail_toDce_intv = _Hist_pvc_unavail_toDce_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 5),
    _Hist_pvc_unavail_toDce_intv_Type()
)
hist_pvc_unavail_toDce_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_unavail_toDce_intv.setStatus("mandatory")


class _Hist_pvc_user_load_tx_intv_Type(DisplayString):
    """Custom type hist_pvc_user_load_tx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_pvc_user_load_tx_intv_Type.__name__ = "DisplayString"
_Hist_pvc_user_load_tx_intv_Object = MibScalar
hist_pvc_user_load_tx_intv = _Hist_pvc_user_load_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 6),
    _Hist_pvc_user_load_tx_intv_Type()
)
hist_pvc_user_load_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_user_load_tx_intv.setStatus("mandatory")


class _Hist_pvc_user_load_rx_intv_Type(DisplayString):
    """Custom type hist_pvc_user_load_rx_intv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_Hist_pvc_user_load_rx_intv_Type.__name__ = "DisplayString"
_Hist_pvc_user_load_rx_intv_Object = MibScalar
hist_pvc_user_load_rx_intv = _Hist_pvc_user_load_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 7),
    _Hist_pvc_user_load_rx_intv_Type()
)
hist_pvc_user_load_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_user_load_rx_intv.setStatus("mandatory")
_Hist_pvc_CIR_toNet_exceed_intv_Type = Integer32
_Hist_pvc_CIR_toNet_exceed_intv_Object = MibScalar
hist_pvc_CIR_toNet_exceed_intv = _Hist_pvc_CIR_toNet_exceed_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 8),
    _Hist_pvc_CIR_toNet_exceed_intv_Type()
)
hist_pvc_CIR_toNet_exceed_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_CIR_toNet_exceed_intv.setStatus("mandatory")


class _Hist_pvc_loss_frame_tx_intv_Type(Integer32):
    """Custom type hist_pvc_loss_frame_tx_intv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no-resp", 254),
          ("not-avail", 255))
    )


_Hist_pvc_loss_frame_tx_intv_Type.__name__ = "Integer32"
_Hist_pvc_loss_frame_tx_intv_Object = MibScalar
hist_pvc_loss_frame_tx_intv = _Hist_pvc_loss_frame_tx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 9),
    _Hist_pvc_loss_frame_tx_intv_Type()
)
hist_pvc_loss_frame_tx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_loss_frame_tx_intv.setStatus("mandatory")


class _Hist_pvc_loss_frame_rx_intv_Type(Integer32):
    """Custom type hist_pvc_loss_frame_rx_intv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no-resp", 254),
          ("not-avail", 255))
    )


_Hist_pvc_loss_frame_rx_intv_Type.__name__ = "Integer32"
_Hist_pvc_loss_frame_rx_intv_Object = MibScalar
hist_pvc_loss_frame_rx_intv = _Hist_pvc_loss_frame_rx_intv_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 3, 1, 10),
    _Hist_pvc_loss_frame_rx_intv_Type()
)
hist_pvc_loss_frame_rx_intv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hist_pvc_loss_frame_rx_intv.setStatus("mandatory")
_HistPvcShapeIntvToDce_Table_Object = MibTable
histPvcShapeIntvToDce_Table = _HistPvcShapeIntvToDce_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4)
)
if mibBuilder.loadTexts:
    histPvcShapeIntvToDce_Table.setStatus("mandatory")
_HistPvcShapeIntvToDce_Entry_Object = MibTableRow
histPvcShapeIntvToDce_Entry = _HistPvcShapeIntvToDce_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1)
)
histPvcShapeIntvToDce_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "histPvcShapeIntvToDce-pvcIx"),
    (0, "LINK-PROBE-MIB", "histPvcShapeIntvToDce-intvIx"),
)
if mibBuilder.loadTexts:
    histPvcShapeIntvToDce_Entry.setStatus("mandatory")


class _HistPvcShapeIntvToDce_pvcIx_Type(Integer32):
    """Custom type histPvcShapeIntvToDce_pvcIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_HistPvcShapeIntvToDce_pvcIx_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDce_pvcIx_Object = MibScalar
histPvcShapeIntvToDce_pvcIx = _HistPvcShapeIntvToDce_pvcIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 1),
    _HistPvcShapeIntvToDce_pvcIx_Type()
)
histPvcShapeIntvToDce_pvcIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDce_pvcIx.setStatus("mandatory")


class _HistPvcShapeIntvToDce_intvIx_Type(Integer32):
    """Custom type histPvcShapeIntvToDce_intvIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HistPvcShapeIntvToDce_intvIx_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDce_intvIx_Object = MibScalar
histPvcShapeIntvToDce_intvIx = _HistPvcShapeIntvToDce_intvIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 2),
    _HistPvcShapeIntvToDce_intvIx_Type()
)
histPvcShapeIntvToDce_intvIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDce_intvIx.setStatus("mandatory")


class _HistPvcShapeIntvToDceLevel_1_Type(Integer32):
    """Custom type histPvcShapeIntvToDceLevel_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDceLevel_1_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDceLevel_1_Object = MibScalar
histPvcShapeIntvToDceLevel_1 = _HistPvcShapeIntvToDceLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 3),
    _HistPvcShapeIntvToDceLevel_1_Type()
)
histPvcShapeIntvToDceLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDceLevel_1.setStatus("mandatory")


class _HistPvcShapeIntvToDceLevel_2_Type(Integer32):
    """Custom type histPvcShapeIntvToDceLevel_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDceLevel_2_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDceLevel_2_Object = MibScalar
histPvcShapeIntvToDceLevel_2 = _HistPvcShapeIntvToDceLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 4),
    _HistPvcShapeIntvToDceLevel_2_Type()
)
histPvcShapeIntvToDceLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDceLevel_2.setStatus("mandatory")


class _HistPvcShapeIntvToDceLevel_3_Type(Integer32):
    """Custom type histPvcShapeIntvToDceLevel_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDceLevel_3_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDceLevel_3_Object = MibScalar
histPvcShapeIntvToDceLevel_3 = _HistPvcShapeIntvToDceLevel_3_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 5),
    _HistPvcShapeIntvToDceLevel_3_Type()
)
histPvcShapeIntvToDceLevel_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDceLevel_3.setStatus("mandatory")


class _HistPvcShapeIntvToDceLevel_4_Type(Integer32):
    """Custom type histPvcShapeIntvToDceLevel_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDceLevel_4_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDceLevel_4_Object = MibScalar
histPvcShapeIntvToDceLevel_4 = _HistPvcShapeIntvToDceLevel_4_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 6),
    _HistPvcShapeIntvToDceLevel_4_Type()
)
histPvcShapeIntvToDceLevel_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDceLevel_4.setStatus("mandatory")


class _HistPvcShapeIntvToDceLevel_5_Type(Integer32):
    """Custom type histPvcShapeIntvToDceLevel_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDceLevel_5_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDceLevel_5_Object = MibScalar
histPvcShapeIntvToDceLevel_5 = _HistPvcShapeIntvToDceLevel_5_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 7),
    _HistPvcShapeIntvToDceLevel_5_Type()
)
histPvcShapeIntvToDceLevel_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDceLevel_5.setStatus("mandatory")


class _HistPvcShapeIntvToDceLevel_6_Type(Integer32):
    """Custom type histPvcShapeIntvToDceLevel_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDceLevel_6_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDceLevel_6_Object = MibScalar
histPvcShapeIntvToDceLevel_6 = _HistPvcShapeIntvToDceLevel_6_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 8),
    _HistPvcShapeIntvToDceLevel_6_Type()
)
histPvcShapeIntvToDceLevel_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDceLevel_6.setStatus("mandatory")


class _HistPvcShapeIntvToDceLevel_7_Type(Integer32):
    """Custom type histPvcShapeIntvToDceLevel_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDceLevel_7_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDceLevel_7_Object = MibScalar
histPvcShapeIntvToDceLevel_7 = _HistPvcShapeIntvToDceLevel_7_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 4, 1, 9),
    _HistPvcShapeIntvToDceLevel_7_Type()
)
histPvcShapeIntvToDceLevel_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDceLevel_7.setStatus("mandatory")
_HistPvcShapeIntvToDte_Table_Object = MibTable
histPvcShapeIntvToDte_Table = _HistPvcShapeIntvToDte_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5)
)
if mibBuilder.loadTexts:
    histPvcShapeIntvToDte_Table.setStatus("mandatory")
_HistPvcShapeIntvToDte_Entry_Object = MibTableRow
histPvcShapeIntvToDte_Entry = _HistPvcShapeIntvToDte_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1)
)
histPvcShapeIntvToDte_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "histPvcShapeIntvToDte-pvcIx"),
    (0, "LINK-PROBE-MIB", "histPvcShapeIntvToDte-intvIx"),
)
if mibBuilder.loadTexts:
    histPvcShapeIntvToDte_Entry.setStatus("mandatory")


class _HistPvcShapeIntvToDte_pvcIx_Type(Integer32):
    """Custom type histPvcShapeIntvToDte_pvcIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_HistPvcShapeIntvToDte_pvcIx_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDte_pvcIx_Object = MibScalar
histPvcShapeIntvToDte_pvcIx = _HistPvcShapeIntvToDte_pvcIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 1),
    _HistPvcShapeIntvToDte_pvcIx_Type()
)
histPvcShapeIntvToDte_pvcIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDte_pvcIx.setStatus("mandatory")


class _HistPvcShapeIntvToDte_intvIx_Type(Integer32):
    """Custom type histPvcShapeIntvToDte_intvIx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HistPvcShapeIntvToDte_intvIx_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDte_intvIx_Object = MibScalar
histPvcShapeIntvToDte_intvIx = _HistPvcShapeIntvToDte_intvIx_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 2),
    _HistPvcShapeIntvToDte_intvIx_Type()
)
histPvcShapeIntvToDte_intvIx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDte_intvIx.setStatus("mandatory")


class _HistPvcShapeIntvToDteLevel_1_Type(Integer32):
    """Custom type histPvcShapeIntvToDteLevel_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDteLevel_1_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDteLevel_1_Object = MibScalar
histPvcShapeIntvToDteLevel_1 = _HistPvcShapeIntvToDteLevel_1_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 3),
    _HistPvcShapeIntvToDteLevel_1_Type()
)
histPvcShapeIntvToDteLevel_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDteLevel_1.setStatus("mandatory")


class _HistPvcShapeIntvToDteLevel_2_Type(Integer32):
    """Custom type histPvcShapeIntvToDteLevel_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDteLevel_2_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDteLevel_2_Object = MibScalar
histPvcShapeIntvToDteLevel_2 = _HistPvcShapeIntvToDteLevel_2_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 4),
    _HistPvcShapeIntvToDteLevel_2_Type()
)
histPvcShapeIntvToDteLevel_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDteLevel_2.setStatus("mandatory")


class _HistPvcShapeIntvToDteLevel_3_Type(Integer32):
    """Custom type histPvcShapeIntvToDteLevel_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDteLevel_3_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDteLevel_3_Object = MibScalar
histPvcShapeIntvToDteLevel_3 = _HistPvcShapeIntvToDteLevel_3_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 5),
    _HistPvcShapeIntvToDteLevel_3_Type()
)
histPvcShapeIntvToDteLevel_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDteLevel_3.setStatus("mandatory")


class _HistPvcShapeIntvToDteLevel_4_Type(Integer32):
    """Custom type histPvcShapeIntvToDteLevel_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDteLevel_4_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDteLevel_4_Object = MibScalar
histPvcShapeIntvToDteLevel_4 = _HistPvcShapeIntvToDteLevel_4_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 6),
    _HistPvcShapeIntvToDteLevel_4_Type()
)
histPvcShapeIntvToDteLevel_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDteLevel_4.setStatus("mandatory")


class _HistPvcShapeIntvToDteLevel_5_Type(Integer32):
    """Custom type histPvcShapeIntvToDteLevel_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDteLevel_5_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDteLevel_5_Object = MibScalar
histPvcShapeIntvToDteLevel_5 = _HistPvcShapeIntvToDteLevel_5_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 7),
    _HistPvcShapeIntvToDteLevel_5_Type()
)
histPvcShapeIntvToDteLevel_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDteLevel_5.setStatus("mandatory")


class _HistPvcShapeIntvToDteLevel_6_Type(Integer32):
    """Custom type histPvcShapeIntvToDteLevel_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDteLevel_6_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDteLevel_6_Object = MibScalar
histPvcShapeIntvToDteLevel_6 = _HistPvcShapeIntvToDteLevel_6_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 8),
    _HistPvcShapeIntvToDteLevel_6_Type()
)
histPvcShapeIntvToDteLevel_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDteLevel_6.setStatus("mandatory")


class _HistPvcShapeIntvToDteLevel_7_Type(Integer32):
    """Custom type histPvcShapeIntvToDteLevel_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HistPvcShapeIntvToDteLevel_7_Type.__name__ = "Integer32"
_HistPvcShapeIntvToDteLevel_7_Object = MibScalar
histPvcShapeIntvToDteLevel_7 = _HistPvcShapeIntvToDteLevel_7_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 5, 5, 1, 9),
    _HistPvcShapeIntvToDteLevel_7_Type()
)
histPvcShapeIntvToDteLevel_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histPvcShapeIntvToDteLevel_7.setStatus("mandatory")
_ProbeIntervalStartTime_ObjectIdentity = ObjectIdentity
probeIntervalStartTime = _ProbeIntervalStartTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 6)
)
_IntvStartTimeIntv_Table_Object = MibTable
intvStartTimeIntv_Table = _IntvStartTimeIntv_Table_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 6, 1)
)
if mibBuilder.loadTexts:
    intvStartTimeIntv_Table.setStatus("mandatory")
_IntvStartTimeIntv_Entry_Object = MibTableRow
intvStartTimeIntv_Entry = _IntvStartTimeIntv_Entry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 6, 1, 1)
)
intvStartTimeIntv_Entry.setIndexNames(
    (0, "LINK-PROBE-MIB", "intvStartTimeIntv-index"),
)
if mibBuilder.loadTexts:
    intvStartTimeIntv_Entry.setStatus("mandatory")


class _IntvStartTimeIntv_index_Type(Integer32):
    """Custom type intvStartTimeIntv_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntvStartTimeIntv_index_Type.__name__ = "Integer32"
_IntvStartTimeIntv_index_Object = MibScalar
intvStartTimeIntv_index = _IntvStartTimeIntv_index_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 6, 1, 1, 1),
    _IntvStartTimeIntv_index_Type()
)
intvStartTimeIntv_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intvStartTimeIntv_index.setStatus("mandatory")


class _Intv_start_time_Type(DisplayString):
    """Custom type intv_start_time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Intv_start_time_Type.__name__ = "DisplayString"
_Intv_start_time_Object = MibScalar
intv_start_time = _Intv_start_time_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 6, 1, 1, 2),
    _Intv_start_time_Type()
)
intv_start_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intv_start_time.setStatus("mandatory")
_DbuConfigGroup_ObjectIdentity = ObjectIdentity
dbuConfigGroup = _DbuConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 7)
)
_DbuPVCTable_Object = MibTable
dbuPVCTable = _DbuPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 1)
)
if mibBuilder.loadTexts:
    dbuPVCTable.setStatus("mandatory")
_DbuPVCEntry_Object = MibTableRow
dbuPVCEntry = _DbuPVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 1, 1)
)
dbuPVCEntry.setIndexNames(
    (0, "LINK-PROBE-MIB", "dbuPVCTableIndex"),
)
if mibBuilder.loadTexts:
    dbuPVCEntry.setStatus("mandatory")


class _DbuPVCTableIndex_Type(Integer32):
    """Custom type dbuPVCTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_DbuPVCTableIndex_Type.__name__ = "Integer32"
_DbuPVCTableIndex_Object = MibTableColumn
dbuPVCTableIndex = _DbuPVCTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 1, 1, 1),
    _DbuPVCTableIndex_Type()
)
dbuPVCTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuPVCTableIndex.setStatus("mandatory")


class _DbuRemotePVCDlci_Type(Integer32):
    """Custom type dbuRemotePVCDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_DbuRemotePVCDlci_Type.__name__ = "Integer32"
_DbuRemotePVCDlci_Object = MibTableColumn
dbuRemotePVCDlci = _DbuRemotePVCDlci_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 1, 1, 2),
    _DbuRemotePVCDlci_Type()
)
dbuRemotePVCDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuRemotePVCDlci.setStatus("mandatory")


class _DbuIsdnAddress_Type(DisplayString):
    """Custom type dbuIsdnAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_DbuIsdnAddress_Type.__name__ = "DisplayString"
_DbuIsdnAddress_Object = MibTableColumn
dbuIsdnAddress = _DbuIsdnAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 1, 1, 3),
    _DbuIsdnAddress_Type()
)
dbuIsdnAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuIsdnAddress.setStatus("mandatory")


class _DbuPvcCir_Type(Integer32):
    """Custom type dbuPvcCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_DbuPvcCir_Type.__name__ = "Integer32"
_DbuPvcCir_Object = MibTableColumn
dbuPvcCir = _DbuPvcCir_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 1, 1, 4),
    _DbuPvcCir_Type()
)
dbuPvcCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuPvcCir.setStatus("mandatory")


class _DbuMasterSlave_Type(Integer32):
    """Custom type dbuMasterSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_DbuMasterSlave_Type.__name__ = "Integer32"
_DbuMasterSlave_Object = MibScalar
dbuMasterSlave = _DbuMasterSlave_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 2),
    _DbuMasterSlave_Type()
)
dbuMasterSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuMasterSlave.setStatus("mandatory")


class _DbuBackupType_Type(Integer32):
    """Custom type dbuBackupType based on Integer32"""
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
        *(("channelDbu", 4),
          ("channelDbu-noProbe", 6),
          ("dte2Dbu1", 2),
          ("dte2Dbu2", 3),
          ("linkProbe", 1),
          ("pvcDbu", 5),
          ("pvcDbu-noProbe", 7))
    )


_DbuBackupType_Type.__name__ = "Integer32"
_DbuBackupType_Object = MibScalar
dbuBackupType = _DbuBackupType_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 3),
    _DbuBackupType_Type()
)
dbuBackupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuBackupType.setStatus("mandatory")


class _DbuPVCAdd_Type(Integer32):
    """Custom type dbuPVCAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_DbuPVCAdd_Type.__name__ = "Integer32"
_DbuPVCAdd_Object = MibScalar
dbuPVCAdd = _DbuPVCAdd_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 4),
    _DbuPVCAdd_Type()
)
dbuPVCAdd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dbuPVCAdd.setStatus("mandatory")


class _DbuPVCDelete_Type(Integer32):
    """Custom type dbuPVCDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_DbuPVCDelete_Type.__name__ = "Integer32"
_DbuPVCDelete_Object = MibScalar
dbuPVCDelete = _DbuPVCDelete_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 5),
    _DbuPVCDelete_Type()
)
dbuPVCDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dbuPVCDelete.setStatus("mandatory")


class _DbuRecoverCount_Type(Integer32):
    """Custom type dbuRecoverCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DbuRecoverCount_Type.__name__ = "Integer32"
_DbuRecoverCount_Object = MibScalar
dbuRecoverCount = _DbuRecoverCount_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 6),
    _DbuRecoverCount_Type()
)
dbuRecoverCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbuRecoverCount.setStatus("mandatory")


class _DbuDialedIsdnAddress_Type(DisplayString):
    """Custom type dbuDialedIsdnAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_DbuDialedIsdnAddress_Type.__name__ = "DisplayString"
_DbuDialedIsdnAddress_Object = MibScalar
dbuDialedIsdnAddress = _DbuDialedIsdnAddress_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 7, 7),
    _DbuDialedIsdnAddress_Type()
)
dbuDialedIsdnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbuDialedIsdnAddress.setStatus("mandatory")
_DeviceStatusGroup_ObjectIdentity = ObjectIdentity
deviceStatusGroup = _DeviceStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 8)
)


class _GlobalStatus_Type(Integer32):
    """Custom type globalStatus based on Integer32"""
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
        *(("connected", 2),
          ("hwFailure", 4),
          ("ready", 1),
          ("test", 3))
    )


_GlobalStatus_Type.__name__ = "Integer32"
_GlobalStatus_Object = MibScalar
globalStatus = _GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 1),
    _GlobalStatus_Type()
)
globalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatus.setStatus("mandatory")
_PvcStatusTable_Object = MibTable
pvcStatusTable = _PvcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 2)
)
if mibBuilder.loadTexts:
    pvcStatusTable.setStatus("mandatory")
_PvcStatusEntry_Object = MibTableRow
pvcStatusEntry = _PvcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 2, 1)
)
pvcStatusEntry.setIndexNames(
    (0, "LINK-PROBE-MIB", "pvcStatusIndex"),
)
if mibBuilder.loadTexts:
    pvcStatusEntry.setStatus("mandatory")


class _PvcStatusIndex_Type(Integer32):
    """Custom type pvcStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcStatusIndex_Type.__name__ = "Integer32"
_PvcStatusIndex_Object = MibTableColumn
pvcStatusIndex = _PvcStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 2, 1, 1),
    _PvcStatusIndex_Type()
)
pvcStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatusIndex.setStatus("mandatory")


class _PvcStatus_Type(Integer32):
    """Custom type pvcStatus based on Integer32"""
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
        *(("pvcActive", 2),
          ("pvcConnected", 3),
          ("pvcInactive", 1),
          ("pvcTest", 4))
    )


_PvcStatus_Type.__name__ = "Integer32"
_PvcStatus_Object = MibTableColumn
pvcStatus = _PvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 2, 1, 2),
    _PvcStatus_Type()
)
pvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcStatus.setStatus("mandatory")


class _EventSubject_Type(Integer32):
    """Custom type eventSubject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("pvc", 2))
    )


_EventSubject_Type.__name__ = "Integer32"
_EventSubject_Object = MibScalar
eventSubject = _EventSubject_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 3),
    _EventSubject_Type()
)
eventSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSubject.setStatus("mandatory")


class _PvcIdentifier_Type(Integer32):
    """Custom type pvcIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcIdentifier_Type.__name__ = "Integer32"
_PvcIdentifier_Object = MibScalar
pvcIdentifier = _PvcIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 4),
    _PvcIdentifier_Type()
)
pvcIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIdentifier.setStatus("mandatory")


class _Cp3000LogCode_Type(DisplayString):
    """Custom type cp3000LogCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Cp3000LogCode_Type.__name__ = "DisplayString"
_Cp3000LogCode_Object = MibScalar
cp3000LogCode = _Cp3000LogCode_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 5),
    _Cp3000LogCode_Type()
)
cp3000LogCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cp3000LogCode.setStatus("mandatory")


class _Cp3000LogSpeed_Type(DisplayString):
    """Custom type cp3000LogSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Cp3000LogSpeed_Type.__name__ = "DisplayString"
_Cp3000LogSpeed_Object = MibScalar
cp3000LogSpeed = _Cp3000LogSpeed_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 6),
    _Cp3000LogSpeed_Type()
)
cp3000LogSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cp3000LogSpeed.setStatus("mandatory")


class _Cp3000LogDate_Type(DisplayString):
    """Custom type cp3000LogDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Cp3000LogDate_Type.__name__ = "DisplayString"
_Cp3000LogDate_Object = MibScalar
cp3000LogDate = _Cp3000LogDate_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 7),
    _Cp3000LogDate_Type()
)
cp3000LogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cp3000LogDate.setStatus("mandatory")


class _Cp3000LogInfo_Type(DisplayString):
    """Custom type cp3000LogInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Cp3000LogInfo_Type.__name__ = "DisplayString"
_Cp3000LogInfo_Object = MibScalar
cp3000LogInfo = _Cp3000LogInfo_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 8, 8),
    _Cp3000LogInfo_Type()
)
cp3000LogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cp3000LogInfo.setStatus("mandatory")
_TrapAcknowledgeGroup_ObjectIdentity = ObjectIdentity
trapAcknowledgeGroup = _TrapAcknowledgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 568, 8, 9)
)


class _TrapAckEnable_Type(Integer32):
    """Custom type trapAckEnable based on Integer32"""
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


_TrapAckEnable_Type.__name__ = "Integer32"
_TrapAckEnable_Object = MibScalar
trapAckEnable = _TrapAckEnable_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 9, 1),
    _TrapAckEnable_Type()
)
trapAckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAckEnable.setStatus("mandatory")


class _TrapAckTimeout_Type(Integer32):
    """Custom type trapAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_TrapAckTimeout_Type.__name__ = "Integer32"
_TrapAckTimeout_Object = MibScalar
trapAckTimeout = _TrapAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 9, 2),
    _TrapAckTimeout_Type()
)
trapAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAckTimeout.setStatus("mandatory")


class _TrapAckFromMngr_Type(Integer32):
    """Custom type trapAckFromMngr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapAcked", 2),
          ("trapNotAcked", 1))
    )


_TrapAckFromMngr_Type.__name__ = "Integer32"
_TrapAckFromMngr_Object = MibScalar
trapAckFromMngr = _TrapAckFromMngr_Object(
    (1, 3, 6, 1, 4, 1, 568, 8, 9, 3),
    _TrapAckFromMngr_Type()
)
trapAckFromMngr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAckFromMngr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pvcNotAvailDCE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 1)
)
pvcNotAvailDCE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_unavail_toDce"),
        ("LINK-PROBE-MIB", "pvcNotAvailThreshDCE"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcNotAvailDCE.setStatus(
        ""
    )

pvcNotAvailDTE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 2)
)
pvcNotAvailDTE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_unavail_toDte"),
        ("LINK-PROBE-MIB", "pvcNotAvailThreshDTE"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcNotAvailDTE.setStatus(
        ""
    )

pvcRTD = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 3)
)
pvcRTD.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvcAveRTDThresh"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcRTD.setStatus(
        ""
    )

frChanUtilizeToDTE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 4)
)
frChanUtilizeToDTE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "frChanUtilizThreshToDTE"),
        ("LINK-PROBE-MIB", "chan_user_load_rx_curr"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    frChanUtilizeToDTE.setStatus(
        ""
    )

frChanUtilizeToDCE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 5)
)
frChanUtilizeToDCE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "frChanUtilizThreshToDCE"),
        ("LINK-PROBE-MIB", "chan_user_load_tx_curr"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    frChanUtilizeToDCE.setStatus(
        ""
    )

pvcBecn = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 6)
)
pvcBecn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvc_number_index_curr"),
        ("LINK-PROBE-MIB", "becn_frames_pvc_curr"),
        ("LINK-PROBE-MIB", "pvcBecnThresh"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcBecn.setStatus(
        ""
    )

pvcFecn = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 7)
)
pvcFecn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvc_number_index_curr"),
        ("LINK-PROBE-MIB", "fecn_frames_pvc_curr"),
        ("LINK-PROBE-MIB", "pvcFecnThresh"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcFecn.setStatus(
        ""
    )

pvcUtilToDTE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 8)
)
pvcUtilToDTE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_user_load_rx_curr"),
        ("LINK-PROBE-MIB", "pvcUtilToDTEThresh"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcUtilToDTE.setStatus(
        ""
    )

pvcUtilToDCE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 9)
)
pvcUtilToDCE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_user_load_tx_curr"),
        ("LINK-PROBE-MIB", "pvcUtilToDCEThresh"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcUtilToDCE.setStatus(
        ""
    )

pvcCIRExceedToDTE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 10)
)
pvcCIRExceedToDTE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_CIR_toNet_exceed_curr"),
        ("LINK-PROBE-MIB", "pvcCirToDTE"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcCIRExceedToDTE.setStatus(
        ""
    )

pvcEIRExceedToDTE = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 11)
)
pvcEIRExceedToDTE.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_EIR_toNet_exceed_curr"),
        ("LINK-PROBE-MIB", "pvcEirToDTE"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcEIRExceedToDTE.setStatus(
        ""
    )

pvcLossFrameTx = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 12)
)
pvcLossFrameTx.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_loss_frame_tx_curr"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcLossFrameTx.setStatus(
        ""
    )

pvcLossFrameRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 13)
)
pvcLossFrameRx.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvc_loss_frame_rx_curr"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcLossFrameRx.setStatus(
        ""
    )

frChanUtilToDTE_exception = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 14)
)
frChanUtilToDTE_exception.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "chanLoadToDTEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    frChanUtilToDTE_exception.setStatus(
        ""
    )

frChanUtilToDCE_exception = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 15)
)
frChanUtilToDCE_exception.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "chanLoadToDCEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    frChanUtilToDCE_exception.setStatus(
        ""
    )

frChanUtilToDTE_endException = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 16)
)
frChanUtilToDTE_endException.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "chanLoadToDTEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    frChanUtilToDTE_endException.setStatus(
        ""
    )

frChanUtilToDCE_endException = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 17)
)
frChanUtilToDCE_endException.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "chanLoadToDTEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    frChanUtilToDCE_endException.setStatus(
        ""
    )

pvcRTD_exception = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 18)
)
pvcRTD_exception.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvcRTDThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcRTD_exception.setStatus(
        ""
    )

pvcRTD_endException = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 19)
)
pvcRTD_endException.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvcRTDThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcRTD_endException.setStatus(
        ""
    )

pvcLoadToDTE_exception = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 20)
)
pvcLoadToDTE_exception.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvcLoadToDTEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcLoadToDTE_exception.setStatus(
        ""
    )

pvcLoadToDCE_exception = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 21)
)
pvcLoadToDCE_exception.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvcLoadToDCEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcLoadToDCE_exception.setStatus(
        ""
    )

pvcLoadToDTE_endException = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 22)
)
pvcLoadToDTE_endException.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvcLoadToDTEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcLoadToDTE_endException.setStatus(
        ""
    )

pvcLoadToDCE_endException = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 23)
)
pvcLoadToDCE_endException.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "pvcLoadToDCEThresh_realTime"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcLoadToDCE_endException.setStatus(
        ""
    )

pvcStatusChangeAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 24)
)
pvcStatusChangeAvail.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcStatusChangeAvail.setStatus(
        ""
    )

pvcStatusChangeUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 25)
)
pvcStatusChangeUnavail.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "pvcPerfCurr_num_index"),
        ("LINK-PROBE-MIB", "current_intv_start_time"))
)
if mibBuilder.loadTexts:
    pvcStatusChangeUnavail.setStatus(
        ""
    )

dbuPvcStatusChangeBackedUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 26)
)
dbuPvcStatusChangeBackedUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "dbuPVCTableIndex"),
        ("LINK-PROBE-MIB", "sys_current_time"))
)
if mibBuilder.loadTexts:
    dbuPvcStatusChangeBackedUp.setStatus(
        ""
    )

dbuPvcStatusChangeNotBackedUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 27)
)
dbuPvcStatusChangeNotBackedUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "dbuPVCTableIndex"),
        ("LINK-PROBE-MIB", "sys_current_time"))
)
if mibBuilder.loadTexts:
    dbuPvcStatusChangeNotBackedUp.setStatus(
        ""
    )

dbuBackupCallActivation = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 28)
)
dbuBackupCallActivation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "dbuDialedIsdnAddress"),
        ("LINK-PROBE-MIB", "sys_current_time"))
)
if mibBuilder.loadTexts:
    dbuBackupCallActivation.setStatus(
        ""
    )

dbuBackupCallDeactivation = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 29)
)
dbuBackupCallDeactivation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "dbuDialedIsdnAddress"),
        ("LINK-PROBE-MIB", "sys_current_time"))
)
if mibBuilder.loadTexts:
    dbuBackupCallDeactivation.setStatus(
        ""
    )

dbuBackupCallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 30)
)
dbuBackupCallFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "dbuDialedIsdnAddress"),
        ("LINK-PROBE-MIB", "sys_current_time"))
)
if mibBuilder.loadTexts:
    dbuBackupCallFailed.setStatus(
        ""
    )

dcdAlarmDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 31)
)
dcdAlarmDetection.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "sys_current_time"))
)
if mibBuilder.loadTexts:
    dcdAlarmDetection.setStatus(
        ""
    )

cp3000Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 32)
)
cp3000Event.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "sys_current_time"),
        ("LINK-PROBE-MIB", "eventSubject"),
        ("LINK-PROBE-MIB", "pvcIdentifier"),
        ("LINK-PROBE-MIB", "cp3000LogCode"),
        ("LINK-PROBE-MIB", "cp3000LogSpeed"),
        ("LINK-PROBE-MIB", "cp3000LogDate"),
        ("LINK-PROBE-MIB", "cp3000LogInfo"))
)
if mibBuilder.loadTexts:
    cp3000Event.setStatus(
        ""
    )

bypassEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 568, 8, 0, 33)
)
bypassEnabled.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LINK-PROBE-MIB", "bypassStatus"),
        ("LINK-PROBE-MIB", "sys_current_time"))
)
if mibBuilder.loadTexts:
    bypassEnabled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINK-PROBE-MIB",
    **{"netQuest": netQuest,
       "link-probe": link_probe,
       "pvcNotAvailDCE": pvcNotAvailDCE,
       "pvcNotAvailDTE": pvcNotAvailDTE,
       "pvcRTD": pvcRTD,
       "frChanUtilizeToDTE": frChanUtilizeToDTE,
       "frChanUtilizeToDCE": frChanUtilizeToDCE,
       "pvcBecn": pvcBecn,
       "pvcFecn": pvcFecn,
       "pvcUtilToDTE": pvcUtilToDTE,
       "pvcUtilToDCE": pvcUtilToDCE,
       "pvcCIRExceedToDTE": pvcCIRExceedToDTE,
       "pvcEIRExceedToDTE": pvcEIRExceedToDTE,
       "pvcLossFrameTx": pvcLossFrameTx,
       "pvcLossFrameRx": pvcLossFrameRx,
       "frChanUtilToDTE-exception": frChanUtilToDTE_exception,
       "frChanUtilToDCE-exception": frChanUtilToDCE_exception,
       "frChanUtilToDTE-endException": frChanUtilToDTE_endException,
       "frChanUtilToDCE-endException": frChanUtilToDCE_endException,
       "pvcRTD-exception": pvcRTD_exception,
       "pvcRTD-endException": pvcRTD_endException,
       "pvcLoadToDTE-exception": pvcLoadToDTE_exception,
       "pvcLoadToDCE-exception": pvcLoadToDCE_exception,
       "pvcLoadToDTE-endException": pvcLoadToDTE_endException,
       "pvcLoadToDCE-endException": pvcLoadToDCE_endException,
       "pvcStatusChangeAvail": pvcStatusChangeAvail,
       "pvcStatusChangeUnavail": pvcStatusChangeUnavail,
       "dbuPvcStatusChangeBackedUp": dbuPvcStatusChangeBackedUp,
       "dbuPvcStatusChangeNotBackedUp": dbuPvcStatusChangeNotBackedUp,
       "dbuBackupCallActivation": dbuBackupCallActivation,
       "dbuBackupCallDeactivation": dbuBackupCallDeactivation,
       "dbuBackupCallFailed": dbuBackupCallFailed,
       "dcdAlarmDetection": dcdAlarmDetection,
       "cp3000Event": cp3000Event,
       "bypassEnabled": bypassEnabled,
       "probeConfig": probeConfig,
       "chan-config": chan_config,
       "lmi-Operation": lmi_Operation,
       "lmi-DLCI": lmi_DLCI,
       "inband-IP-DLCI": inband_IP_DLCI,
       "ip-Encapsu": ip_Encapsu,
       "interface-Speed": interface_Speed,
       "nvram-update": nvram_update,
       "lmi-config": lmi_config,
       "lmi-type": lmi_type,
       "max-Info-Length": max_Info_Length,
       "n391-Counter": n391_Counter,
       "n392-Net-Counter": n392_Net_Counter,
       "n392-User-Counter": n392_User_Counter,
       "n393-Net-Counter": n393_Net_Counter,
       "n393-User-Counter": n393_User_Counter,
       "t391-Timer": t391_Timer,
       "t392-Timer": t392_Timer,
       "lMI-Controller": lMI_Controller,
       "pro-fun-config": pro_fun_config,
       "softwareVersion": softwareVersion,
       "probe-Mode": probe_Mode,
       "poll-Period": poll_Period,
       "sys-current-time": sys_current_time,
       "current-intv-start-time": current_intv_start_time,
       "pvc-Count": pvc_Count,
       "probeTokenSize": probeTokenSize,
       "pvc-add": pvc_add,
       "pvc-delete": pvc_delete,
       "pvc-Table": pvc_Table,
       "pvc-Entry": pvc_Entry,
       "pvc-Table-Index": pvc_Table_Index,
       "pvc-Operation": pvc_Operation,
       "pvc-Remote-IpAddress": pvc_Remote_IpAddress,
       "alternateVersion": alternateVersion,
       "bypassStatus": bypassStatus,
       "trap-config": trap_config,
       "trapCtlGlobal": trapCtlGlobal,
       "trapCtlSpecific": trapCtlSpecific,
       "pvcNotAvailThreshDCE": pvcNotAvailThreshDCE,
       "pvcNotAvailThreshDTE": pvcNotAvailThreshDTE,
       "pvcAveRTDThresh": pvcAveRTDThresh,
       "frChanUtilizThreshToDTE": frChanUtilizThreshToDTE,
       "frChanUtilizThreshToDCE": frChanUtilizThreshToDCE,
       "pvcBecnThresh": pvcBecnThresh,
       "pvcFecnThresh": pvcFecnThresh,
       "pvcUtilToDTEThresh": pvcUtilToDTEThresh,
       "pvcUtilToDCEThresh": pvcUtilToDCEThresh,
       "chanLoadToDTEThresh-realTime": chanLoadToDTEThresh_realTime,
       "chanLoadToDCEThresh-realTime": chanLoadToDCEThresh_realTime,
       "chanLoadThreshToDTE-realTimeRange": chanLoadThreshToDTE_realTimeRange,
       "chanLoadThreshToDCE-realTimeRange": chanLoadThreshToDCE_realTimeRange,
       "pvcRTDThresh-realTime": pvcRTDThresh_realTime,
       "pvcRTDThresh-realTimeRange": pvcRTDThresh_realTimeRange,
       "pvcLoadToDTEThresh-realTime": pvcLoadToDTEThresh_realTime,
       "pvcLoadToDCEThresh-realTime": pvcLoadToDCEThresh_realTime,
       "pvcLoadToDTEThresh-realTimeRange": pvcLoadToDTEThresh_realTimeRange,
       "pvcLoadToDCEThresh-realTimeRange": pvcLoadToDCEThresh_realTimeRange,
       "pvc-config": pvc_config,
       "pvcTC": pvcTC,
       "pvcCirEir-Table": pvcCirEir_Table,
       "pvcCirEir-Entry": pvcCirEir_Entry,
       "pvcCirEir-Table-Index": pvcCirEir_Table_Index,
       "pvcCirToDTE": pvcCirToDTE,
       "pvcCirToDCE": pvcCirToDCE,
       "pvcEirToDTE": pvcEirToDTE,
       "pvcEirToDCE": pvcEirToDCE,
       "file-download-config": file_download_config,
       "sourceIpAddress": sourceIpAddress,
       "sourceFileName": sourceFileName,
       "sourceFileMode": sourceFileMode,
       "tftpAction": tftpAction,
       "changeVersion": changeVersion,
       "softwareReset": softwareReset,
       "tftpState": tftpState,
       "net-management-config": net_management_config,
       "ipInterface": ipInterface,
       "inbandIpAddress": inbandIpAddress,
       "outbandIpAddress": outbandIpAddress,
       "routerIpAddress": routerIpAddress,
       "subnetmaskIpAddress": subnetmaskIpAddress,
       "probeStat": probeStat,
       "chStCurrent": chStCurrent,
       "dte-frames-ch-curr": dte_frames_ch_curr,
       "dce-frames-ch-curr": dce_frames_ch_curr,
       "dte-octets-ch-curr": dte_octets_ch_curr,
       "dce-octets-ch-curr": dce_octets_ch_curr,
       "lmi-enq-tx-ch-curr": lmi_enq_tx_ch_curr,
       "lmi-resp-tx-ch-curr": lmi_resp_tx_ch_curr,
       "lmi-enq-rx-ch-curr": lmi_enq_rx_ch_curr,
       "lmi-resp-rx-ch-curr": lmi_resp_rx_ch_curr,
       "fecn-frames-ch-curr": fecn_frames_ch_curr,
       "becn-frames-ch-curr": becn_frames_ch_curr,
       "ip-tx-ch-curr": ip_tx_ch_curr,
       "ip-rx-ch-curr": ip_rx_ch_curr,
       "poll-tx-ch-curr": poll_tx_ch_curr,
       "resp-tx-ch-curr": resp_tx_ch_curr,
       "poll-rx-ch-curr": poll_rx_ch_curr,
       "resp-rx-ch-curr": resp_rx_ch_curr,
       "chStInterval-Table": chStInterval_Table,
       "chStInterval-Entry": chStInterval_Entry,
       "chStIntv-index": chStIntv_index,
       "dte-frames-ch-intv": dte_frames_ch_intv,
       "dce-frames-ch-intv": dce_frames_ch_intv,
       "dte-octets-ch-intv": dte_octets_ch_intv,
       "dce-octets-ch-intv": dce_octets_ch_intv,
       "lmi-enq-tx-ch-intv": lmi_enq_tx_ch_intv,
       "lmi-resp-tx-ch-intv": lmi_resp_tx_ch_intv,
       "lmi-enq-rx-ch-intv": lmi_enq_rx_ch_intv,
       "lmi-resp-rx-ch-intv": lmi_resp_rx_ch_intv,
       "fecn-frames-ch-intv": fecn_frames_ch_intv,
       "becn-frames-ch-intv": becn_frames_ch_intv,
       "ip-tx-ch-intv": ip_tx_ch_intv,
       "ip-rx-ch-intv": ip_rx_ch_intv,
       "poll-tx-ch-intv": poll_tx_ch_intv,
       "resp-tx-ch-intv": resp_tx_ch_intv,
       "poll-rx-ch-intv": poll_rx_ch_intv,
       "resp-rx-ch-intv": resp_rx_ch_intv,
       "pvcStCurrent-Table": pvcStCurrent_Table,
       "pvcStCurrent-Entry": pvcStCurrent_Entry,
       "pvc-number-index-curr": pvc_number_index_curr,
       "dte-frames-pvc-curr": dte_frames_pvc_curr,
       "dce-frames-pvc-curr": dce_frames_pvc_curr,
       "dte-octets-pvc-curr": dte_octets_pvc_curr,
       "dce-octets-pvc-curr": dce_octets_pvc_curr,
       "dte-frames-with-DE-pvc-curr": dte_frames_with_DE_pvc_curr,
       "dce-frames-with-DE-pvc-curr": dce_frames_with_DE_pvc_curr,
       "fecn-frames-pvc-curr": fecn_frames_pvc_curr,
       "becn-frames-pvc-curr": becn_frames_pvc_curr,
       "poll-tx-pvc-curr": poll_tx_pvc_curr,
       "resp-tx-pvc-curr": resp_tx_pvc_curr,
       "poll-rx-pvc-curr": poll_rx_pvc_curr,
       "resp-rx-pvc-curr": resp_rx_pvc_curr,
       "pvc-loop-curr": pvc_loop_curr,
       "ip-poll-tx-pvc-curr": ip_poll_tx_pvc_curr,
       "ip-resp-tx-pvc-curr": ip_resp_tx_pvc_curr,
       "ip-poll-rx-pvc-curr": ip_poll_rx_pvc_curr,
       "ip-resp-rx-pvc-curr": ip_resp_rx_pvc_curr,
       "ipRtrRxLatTxPvcCurr": ipRtrRxLatTxPvcCurr,
       "ipRtrRxLatRxPvcCurr": ipRtrRxLatRxPvcCurr,
       "ipRtrTxLatTxPvcCurr": ipRtrTxLatTxPvcCurr,
       "ipRtrTxLatRxPvcCurr": ipRtrTxLatRxPvcCurr,
       "pvcStInterval-Table": pvcStInterval_Table,
       "pvcStInterval-Entry": pvcStInterval_Entry,
       "pvc-number-index-intv": pvc_number_index_intv,
       "pvcStIntv-index": pvcStIntv_index,
       "dte-frames-pvc-intv": dte_frames_pvc_intv,
       "dce-frames-pvc-intv": dce_frames_pvc_intv,
       "dte-octets-pvc-intv": dte_octets_pvc_intv,
       "dce-octets-pvc-intv": dce_octets_pvc_intv,
       "dte-frames-with-DE-pvc-intv": dte_frames_with_DE_pvc_intv,
       "dce-frames-with-DE-pvc-intv": dce_frames_with_DE_pvc_intv,
       "fecn-frames-pvc-intv": fecn_frames_pvc_intv,
       "becn-frames-pvc-intv": becn_frames_pvc_intv,
       "poll-tx-pvc-intv": poll_tx_pvc_intv,
       "resp-tx-pvc-intv": resp_tx_pvc_intv,
       "poll-rx-pvc-intv": poll_rx_pvc_intv,
       "resp-rx-pvc-intv": resp_rx_pvc_intv,
       "pvc-loop-intv": pvc_loop_intv,
       "ip-poll-tx-pvc-intv": ip_poll_tx_pvc_intv,
       "ip-resp-tx-pvc-intv": ip_resp_tx_pvc_intv,
       "ip-poll-rx-pvc-intv": ip_poll_rx_pvc_intv,
       "ip-resp-rx-pvc-intv": ip_resp_rx_pvc_intv,
       "ipRtrRxLatTxPvcIntv": ipRtrRxLatTxPvcIntv,
       "ipRtrRxLatRxPvcIntv": ipRtrRxLatRxPvcIntv,
       "ipRtrTxLatTxPvcIntv": ipRtrTxLatTxPvcIntv,
       "ipRtrTxLatRxPvcIntv": ipRtrTxLatRxPvcIntv,
       "probePerform": probePerform,
       "chanPerfCurr": chanPerfCurr,
       "chan-unvail-toDte-curr": chan_unvail_toDte_curr,
       "chan-unavail-toDce-curr": chan_unavail_toDce_curr,
       "chan-user-load-tx-curr": chan_user_load_tx_curr,
       "chan-user-load-rx-curr": chan_user_load_rx_curr,
       "chan-total-load-tx-curr": chan_total_load_tx_curr,
       "chan-total-load-rx-curr": chan_total_load_rx_curr,
       "chanPerfIntv-Table": chanPerfIntv_Table,
       "chanPerfIntv-Entry": chanPerfIntv_Entry,
       "chanPerfIntv-index": chanPerfIntv_index,
       "chan-unavail-toDte-intv": chan_unavail_toDte_intv,
       "chan-unavail-toDce-intv": chan_unavail_toDce_intv,
       "chan-user-load-tx-intv": chan_user_load_tx_intv,
       "chan-user-load-rx-intv": chan_user_load_rx_intv,
       "chan-total-load-tx-intv": chan_total_load_tx_intv,
       "chan-total-load-rx-intv": chan_total_load_rx_intv,
       "chan-min-user-load-tx-intv": chan_min_user_load_tx_intv,
       "chan-min-user-load-tx-time-intv": chan_min_user_load_tx_time_intv,
       "chan-min-user-load-rx-intv": chan_min_user_load_rx_intv,
       "chan-min-user-load-rx-time-intv": chan_min_user_load_rx_time_intv,
       "chan-min-total-load-tx-intv": chan_min_total_load_tx_intv,
       "chan-min-total-load-tx-time-intv": chan_min_total_load_tx_time_intv,
       "chan-min-total-load-rx-intv": chan_min_total_load_rx_intv,
       "chan-min-total-load-rx-time-intv": chan_min_total_load_rx_time_intv,
       "chan-max-user-load-tx-intv": chan_max_user_load_tx_intv,
       "chan-max-user-load-tx-time-intv": chan_max_user_load_tx_time_intv,
       "chan-max-user-load-rx-intv": chan_max_user_load_rx_intv,
       "chan-max-user-load-rx-time-intv": chan_max_user_load_rx_time_intv,
       "chan-max-total-load-tx-intv": chan_max_total_load_tx_intv,
       "chan-max-total-load-tx-time-intv": chan_max_total_load_tx_time_intv,
       "chan-max-total-load-rx-intv": chan_max_total_load_rx_intv,
       "chan-max-total-load-rx-time-intv": chan_max_total_load_rx_time_intv,
       "pvcPerfCurr-Table": pvcPerfCurr_Table,
       "pvcPerfCurr-Entry": pvcPerfCurr_Entry,
       "pvcPerfCurr-num-index": pvcPerfCurr_num_index,
       "pvc-tx-time-curr": pvc_tx_time_curr,
       "pvc-unavail-toDte": pvc_unavail_toDte,
       "pvc-unavail-toDce": pvc_unavail_toDce,
       "pvc-user-load-tx-curr": pvc_user_load_tx_curr,
       "pvc-user-load-rx-curr": pvc_user_load_rx_curr,
       "pvc-total-load-tx-curr": pvc_total_load_tx_curr,
       "pvc-total-load-rx-curr": pvc_total_load_rx_curr,
       "pvc-CIR-toNet-exceed-curr": pvc_CIR_toNet_exceed_curr,
       "pvc-EIR-toNet-exceed-curr": pvc_EIR_toNet_exceed_curr,
       "pvc-loss-frame-tx-curr": pvc_loss_frame_tx_curr,
       "pvc-loss-frame-rx-curr": pvc_loss_frame_rx_curr,
       "pvc-ip-tx-time-curr": pvc_ip_tx_time_curr,
       "pvcIpRtrRxLatTxTimeCurr": pvcIpRtrRxLatTxTimeCurr,
       "pvcIpRtrTxLatTxTimeCurr": pvcIpRtrTxLatTxTimeCurr,
       "pvcPerfIntv-Table": pvcPerfIntv_Table,
       "pvcPerfIntv-Entry": pvcPerfIntv_Entry,
       "pvcPerfIntv-num-index": pvcPerfIntv_num_index,
       "pvcPerf-intv-index": pvcPerf_intv_index,
       "pvc-tx-time-intv": pvc_tx_time_intv,
       "pvc-unavail-toDte-intv": pvc_unavail_toDte_intv,
       "pvc-unavail-toDce-intv": pvc_unavail_toDce_intv,
       "pvc-user-load-tx-intv": pvc_user_load_tx_intv,
       "pvc-user-load-rx-intv": pvc_user_load_rx_intv,
       "pvc-total-load-tx-intv": pvc_total_load_tx_intv,
       "pvc-total-load-rx-intv": pvc_total_load_rx_intv,
       "pvc-CIR-toNet-exceed-intv": pvc_CIR_toNet_exceed_intv,
       "pvc-EIR-toNet-exceed-intv": pvc_EIR_toNet_exceed_intv,
       "pvc-loss-frame-tx-intv": pvc_loss_frame_tx_intv,
       "pvc-loss-frame-rx-intv": pvc_loss_frame_rx_intv,
       "pvc-ip-tx-time-intv": pvc_ip_tx_time_intv,
       "pvcIpRtrRxLatTxTimeIntv": pvcIpRtrRxLatTxTimeIntv,
       "pvcIpRtrTxLatTxTimeIntv": pvcIpRtrTxLatTxTimeIntv,
       "pvc-min-tx-time-intv": pvc_min_tx_time_intv,
       "pvc-min-tx-time-time-intv": pvc_min_tx_time_time_intv,
       "pvc-min-user-load-tx-intv": pvc_min_user_load_tx_intv,
       "pvc-min-user-load-tx-time-intv": pvc_min_user_load_tx_time_intv,
       "pvc-min-user-load-rx-intv": pvc_min_user_load_rx_intv,
       "pvc-min-user-load-rx-time-intv": pvc_min_user_load_rx_time_intv,
       "pvc-min-total-load-tx-intv": pvc_min_total_load_tx_intv,
       "pvc-min-total-load-tx-time-intv": pvc_min_total_load_tx_time_intv,
       "pvc-min-total-load-rx-intv": pvc_min_total_load_rx_intv,
       "pvc-min-total-load-rx-time-intv": pvc_min_total_load_rx_time_intv,
       "pvc-min-ip-tx-time-intv": pvc_min_ip_tx_time_intv,
       "pvc-min-ip-tx-time-time-intv": pvc_min_ip_tx_time_time_intv,
       "pvc-max-tx-time-intv": pvc_max_tx_time_intv,
       "pvc-max-tx-time-time-intv": pvc_max_tx_time_time_intv,
       "pvc-max-user-load-tx-intv": pvc_max_user_load_tx_intv,
       "pvc-max-user-load-tx-time-intv": pvc_max_user_load_tx_time_intv,
       "pvc-max-user-load-rx-intv": pvc_max_user_load_rx_intv,
       "pvc-max-user-load-rx-time-intv": pvc_max_user_load_rx_time_intv,
       "pvc-max-total-load-tx-intv": pvc_max_total_load_tx_intv,
       "pvc-max-total-load-tx-time-intv": pvc_max_total_load_tx_time_intv,
       "pvc-max-total-load-rx-intv": pvc_max_total_load_rx_intv,
       "pvc-max-total-load-rx-time-intv": pvc_max_total_load_rx_time_intv,
       "pvc-max-ip-tx-time-intv": pvc_max_ip_tx_time_intv,
       "pvc-max-ip-tx-time-time-intv": pvc_max_ip_tx_time_time_intv,
       "probeTrafficShape": probeTrafficShape,
       "pvcShapeThresh": pvcShapeThresh,
       "pvcShapeThreshLevel-1": pvcShapeThreshLevel_1,
       "pvcShapeThreshLevel-2": pvcShapeThreshLevel_2,
       "pvcShapeThreshLevel-3": pvcShapeThreshLevel_3,
       "pvcShapeThreshLevel-4": pvcShapeThreshLevel_4,
       "pvcShapeThreshLevel-5": pvcShapeThreshLevel_5,
       "pvcShapeThreshLevel-6": pvcShapeThreshLevel_6,
       "pvcShapeThreshLevel-7": pvcShapeThreshLevel_7,
       "pvcShapeCurrToDce-Table": pvcShapeCurrToDce_Table,
       "pvcShapeCurrToDce-Entry": pvcShapeCurrToDce_Entry,
       "pvcShapeCurrToDce-index": pvcShapeCurrToDce_index,
       "pvcShapeCurrToDceLevel-1": pvcShapeCurrToDceLevel_1,
       "pvcShapeCurrToDceLevel-2": pvcShapeCurrToDceLevel_2,
       "pvcShapeCurrToDceLevel-3": pvcShapeCurrToDceLevel_3,
       "pvcShapeCurrToDceLevel-4": pvcShapeCurrToDceLevel_4,
       "pvcShapeCurrToDceLevel-5": pvcShapeCurrToDceLevel_5,
       "pvcShapeCurrToDceLevel-6": pvcShapeCurrToDceLevel_6,
       "pvcShapeCurrToDceLevel-7": pvcShapeCurrToDceLevel_7,
       "pvcShapeCurrToDte-Table": pvcShapeCurrToDte_Table,
       "pvcShapeCurrToDte-Entry": pvcShapeCurrToDte_Entry,
       "pvcShapeCurrToDte-index": pvcShapeCurrToDte_index,
       "pvcShapeCurrToDteLevel-1": pvcShapeCurrToDteLevel_1,
       "pvcShapeCurrToDteLevel-2": pvcShapeCurrToDteLevel_2,
       "pvcShapeCurrToDteLevel-3": pvcShapeCurrToDteLevel_3,
       "pvcShapeCurrToDteLevel-4": pvcShapeCurrToDteLevel_4,
       "pvcShapeCurrToDteLevel-5": pvcShapeCurrToDteLevel_5,
       "pvcShapeCurrToDteLevel-6": pvcShapeCurrToDteLevel_6,
       "pvcShapeCurrToDteLevel-7": pvcShapeCurrToDteLevel_7,
       "pvcShapeIntvToDce-Table": pvcShapeIntvToDce_Table,
       "pvcShapeIntvToDce-Entry": pvcShapeIntvToDce_Entry,
       "pvcShapeIntvToDce-pvcIx": pvcShapeIntvToDce_pvcIx,
       "pvcShapeIntvToDce-intvIx": pvcShapeIntvToDce_intvIx,
       "pvcShapeIntvToDceLevel-1": pvcShapeIntvToDceLevel_1,
       "pvcShapeIntvToDceLevel-2": pvcShapeIntvToDceLevel_2,
       "pvcShapeIntvToDceLevel-3": pvcShapeIntvToDceLevel_3,
       "pvcShapeIntvToDceLevel-4": pvcShapeIntvToDceLevel_4,
       "pvcShapeIntvToDceLevel-5": pvcShapeIntvToDceLevel_5,
       "pvcShapeIntvToDceLevel-6": pvcShapeIntvToDceLevel_6,
       "pvcShapeIntvToDceLevel-7": pvcShapeIntvToDceLevel_7,
       "pvcShapeIntvToDte-Table": pvcShapeIntvToDte_Table,
       "pvcShapeIntvToDte-Entry": pvcShapeIntvToDte_Entry,
       "pvcShapeIntvToDte-pvcIx": pvcShapeIntvToDte_pvcIx,
       "pvcShapeIntvToDte-intvIx": pvcShapeIntvToDte_intvIx,
       "pvcShapeIntvToDteLevel-1": pvcShapeIntvToDteLevel_1,
       "pvcShapeIntvToDteLevel-2": pvcShapeIntvToDteLevel_2,
       "pvcShapeIntvToDteLevel-3": pvcShapeIntvToDteLevel_3,
       "pvcShapeIntvToDteLevel-4": pvcShapeIntvToDteLevel_4,
       "pvcShapeIntvToDteLevel-5": pvcShapeIntvToDteLevel_5,
       "pvcShapeIntvToDteLevel-6": pvcShapeIntvToDteLevel_6,
       "pvcShapeIntvToDteLevel-7": pvcShapeIntvToDteLevel_7,
       "probeHistorical": probeHistorical,
       "histIntvStartTimeIntv-Table": histIntvStartTimeIntv_Table,
       "histIntvStartTimeIntv-Entry": histIntvStartTimeIntv_Entry,
       "histIntvStartTimeIntv-index": histIntvStartTimeIntv_index,
       "hist-intv-start-time": hist_intv_start_time,
       "histChanPerfIntv-Table": histChanPerfIntv_Table,
       "histChanPerfIntv-Entry": histChanPerfIntv_Entry,
       "histChanPerfIntv-index": histChanPerfIntv_index,
       "hist-chan-unavail-toDte-intv": hist_chan_unavail_toDte_intv,
       "hist-chan-unavail-toDce-intv": hist_chan_unavail_toDce_intv,
       "hist-chan-user-load-tx-intv": hist_chan_user_load_tx_intv,
       "hist-chan-user-load-rx-intv": hist_chan_user_load_rx_intv,
       "histPvcPerfIntv-Table": histPvcPerfIntv_Table,
       "histPvcPerfIntv-Entry": histPvcPerfIntv_Entry,
       "histPvcPerfIntv-num-index": histPvcPerfIntv_num_index,
       "histPvcPerf-intv-index": histPvcPerf_intv_index,
       "hist-pvc-tx-time-intv": hist_pvc_tx_time_intv,
       "hist-pvc-unavail-toDte-intv": hist_pvc_unavail_toDte_intv,
       "hist-pvc-unavail-toDce-intv": hist_pvc_unavail_toDce_intv,
       "hist-pvc-user-load-tx-intv": hist_pvc_user_load_tx_intv,
       "hist-pvc-user-load-rx-intv": hist_pvc_user_load_rx_intv,
       "hist-pvc-CIR-toNet-exceed-intv": hist_pvc_CIR_toNet_exceed_intv,
       "hist-pvc-loss-frame-tx-intv": hist_pvc_loss_frame_tx_intv,
       "hist-pvc-loss-frame-rx-intv": hist_pvc_loss_frame_rx_intv,
       "histPvcShapeIntvToDce-Table": histPvcShapeIntvToDce_Table,
       "histPvcShapeIntvToDce-Entry": histPvcShapeIntvToDce_Entry,
       "histPvcShapeIntvToDce-pvcIx": histPvcShapeIntvToDce_pvcIx,
       "histPvcShapeIntvToDce-intvIx": histPvcShapeIntvToDce_intvIx,
       "histPvcShapeIntvToDceLevel-1": histPvcShapeIntvToDceLevel_1,
       "histPvcShapeIntvToDceLevel-2": histPvcShapeIntvToDceLevel_2,
       "histPvcShapeIntvToDceLevel-3": histPvcShapeIntvToDceLevel_3,
       "histPvcShapeIntvToDceLevel-4": histPvcShapeIntvToDceLevel_4,
       "histPvcShapeIntvToDceLevel-5": histPvcShapeIntvToDceLevel_5,
       "histPvcShapeIntvToDceLevel-6": histPvcShapeIntvToDceLevel_6,
       "histPvcShapeIntvToDceLevel-7": histPvcShapeIntvToDceLevel_7,
       "histPvcShapeIntvToDte-Table": histPvcShapeIntvToDte_Table,
       "histPvcShapeIntvToDte-Entry": histPvcShapeIntvToDte_Entry,
       "histPvcShapeIntvToDte-pvcIx": histPvcShapeIntvToDte_pvcIx,
       "histPvcShapeIntvToDte-intvIx": histPvcShapeIntvToDte_intvIx,
       "histPvcShapeIntvToDteLevel-1": histPvcShapeIntvToDteLevel_1,
       "histPvcShapeIntvToDteLevel-2": histPvcShapeIntvToDteLevel_2,
       "histPvcShapeIntvToDteLevel-3": histPvcShapeIntvToDteLevel_3,
       "histPvcShapeIntvToDteLevel-4": histPvcShapeIntvToDteLevel_4,
       "histPvcShapeIntvToDteLevel-5": histPvcShapeIntvToDteLevel_5,
       "histPvcShapeIntvToDteLevel-6": histPvcShapeIntvToDteLevel_6,
       "histPvcShapeIntvToDteLevel-7": histPvcShapeIntvToDteLevel_7,
       "probeIntervalStartTime": probeIntervalStartTime,
       "intvStartTimeIntv-Table": intvStartTimeIntv_Table,
       "intvStartTimeIntv-Entry": intvStartTimeIntv_Entry,
       "intvStartTimeIntv-index": intvStartTimeIntv_index,
       "intv-start-time": intv_start_time,
       "dbuConfigGroup": dbuConfigGroup,
       "dbuPVCTable": dbuPVCTable,
       "dbuPVCEntry": dbuPVCEntry,
       "dbuPVCTableIndex": dbuPVCTableIndex,
       "dbuRemotePVCDlci": dbuRemotePVCDlci,
       "dbuIsdnAddress": dbuIsdnAddress,
       "dbuPvcCir": dbuPvcCir,
       "dbuMasterSlave": dbuMasterSlave,
       "dbuBackupType": dbuBackupType,
       "dbuPVCAdd": dbuPVCAdd,
       "dbuPVCDelete": dbuPVCDelete,
       "dbuRecoverCount": dbuRecoverCount,
       "dbuDialedIsdnAddress": dbuDialedIsdnAddress,
       "deviceStatusGroup": deviceStatusGroup,
       "globalStatus": globalStatus,
       "pvcStatusTable": pvcStatusTable,
       "pvcStatusEntry": pvcStatusEntry,
       "pvcStatusIndex": pvcStatusIndex,
       "pvcStatus": pvcStatus,
       "eventSubject": eventSubject,
       "pvcIdentifier": pvcIdentifier,
       "cp3000LogCode": cp3000LogCode,
       "cp3000LogSpeed": cp3000LogSpeed,
       "cp3000LogDate": cp3000LogDate,
       "cp3000LogInfo": cp3000LogInfo,
       "trapAcknowledgeGroup": trapAcknowledgeGroup,
       "trapAckEnable": trapAckEnable,
       "trapAckTimeout": trapAckTimeout,
       "trapAckFromMngr": trapAckFromMngr}
)
