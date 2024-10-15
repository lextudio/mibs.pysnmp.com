# SNMP MIB module (ISG-NSD-COMMON-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISG-NSD-COMMON-TRAPS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:46 2024
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

(cdx6500SNMPLastTrap,) = mibBuilder.importSymbols(
    "CDX-6500-COMMON-MIB",
    "cdx6500SNMPLastTrap")

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



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class Counter8(Integer32):
    """Custom type Counter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




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

# Managed Objects groups


# Notification objects

code_power_supply_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1000)
)
code_power_supply_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_power_supply_down.setStatus(
        ""
    )

code_power_supply_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1001)
)
code_power_supply_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_power_supply_up.setStatus(
        ""
    )

code_fan_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1002)
)
code_fan_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_fan_failed.setStatus(
        ""
    )

code_flash_checksum_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1003)
)
code_flash_checksum_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_flash_checksum_error.setStatus(
        ""
    )

code_flash_checksum_ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1004)
)
code_flash_checksum_ok.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_flash_checksum_ok.setStatus(
        ""
    )

code_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1005)
)
code_error_detected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_error_detected.setStatus(
        ""
    )

code1006_dram_code_c = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1006)
)
code1006_dram_code_c.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code1006_dram_code_c.setStatus(
        ""
    )

code1007_dram_code_c = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1007)
)
code1007_dram_code_c.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code1007_dram_code_c.setStatus(
        ""
    )

code_dram_idata_c = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1008)
)
code_dram_idata_c.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_dram_idata_c.setStatus(
        ""
    )

code_dram_idata_reload_success = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1009)
)
code_dram_idata_reload_success.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_dram_idata_reload_success.setStatus(
        ""
    )

code_dram_idata_reload_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1010)
)
code_dram_idata_reload_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_dram_idata_reload_failure.setStatus(
        ""
    )

code_dram_idata_sig_array = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 1011)
)
code_dram_idata_sig_array.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_dram_idata_sig_array.setStatus(
        ""
    )

port_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2000)
)
port_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    port_boot_complete.setStatus(
        ""
    )

port_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2001)
)
port_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    port_boot_failure.setStatus(
        ""
    )

channel_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2002)
)
channel_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    channel_boot_complete.setStatus(
        ""
    )

channel_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2003)
)
channel_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    channel_boot_failure.setStatus(
        ""
    )

code_port_boot_to_new_port_failu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2004)
)
code_port_boot_to_new_port_failu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_port_boot_to_new_port_failu.setStatus(
        ""
    )

code_port_insufficient_dynamic_m = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2005)
)
code_port_insufficient_dynamic_m.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_port_insufficient_dynamic_m.setStatus(
        ""
    )

code2006_port_dynami = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2006)
)
code2006_port_dynami.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code2006_port_dynami.setStatus(
        ""
    )

code2007_port_dynami = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2007)
)
code2007_port_dynami.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code2007_port_dynami.setStatus(
        ""
    )

code2008_port_dynami = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2008)
)
code2008_port_dynami.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code2008_port_dynami.setStatus(
        ""
    )

code2009_port_failur = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 2009)
)
code2009_port_failur.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code2009_port_failur.setStatus(
        ""
    )

buff_pool_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 3000)
)
buff_pool_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    buff_pool_util_exceeded.setStatus(
        ""
    )

lib_lan_congestion_start = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 3001)
)
lib_lan_congestion_start.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lib_lan_congestion_start.setStatus(
        ""
    )

lib_lan_congestion_end = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 3002)
)
lib_lan_congestion_end.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lib_lan_congestion_end.setStatus(
        ""
    )

cmem_corrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 4000)
)
cmem_corrupted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cmem_corrupted.setStatus(
        ""
    )

cmem_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 4001)
)
cmem_recovered.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cmem_recovered.setStatus(
        ""
    )

cmem_compression_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 4002)
)
cmem_compression_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cmem_compression_fail.setStatus(
        ""
    )

code_no_memory_tftp_upload_to_sc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 4003)
)
code_no_memory_tftp_upload_to_sc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_no_memory_tftp_upload_to_sc.setStatus(
        ""
    )

ctp_wrong_task_level = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 5000)
)
ctp_wrong_task_level.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ctp_wrong_task_level.setStatus(
        ""
    )

ctp_help_msg_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 5001)
)
ctp_help_msg_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ctp_help_msg_overflow.setStatus(
        ""
    )

eiaPort_handshake_incomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6001)
)
eiaPort_handshake_incomplete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eiaPort_handshake_incomplete.setStatus(
        ""
    )

eiaPort_handshake_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6002)
)
eiaPort_handshake_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eiaPort_handshake_complete.setStatus(
        ""
    )

v25bis_proto_mismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6003)
)
v25bis_proto_mismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    v25bis_proto_mismatch.setStatus(
        ""
    )

v25bis_call_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6004)
)
v25bis_call_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    v25bis_call_fail.setStatus(
        ""
    )

v25bis_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6005)
)
v25bis_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    v25bis_error.setStatus(
        ""
    )

v25bis_unknown_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6006)
)
v25bis_unknown_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    v25bis_unknown_error.setStatus(
        ""
    )

sw56k_calling = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6007)
)
sw56k_calling.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_calling.setStatus(
        ""
    )

sw56k_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6008)
)
sw56k_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_connected.setStatus(
        ""
    )

sw56k_call_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6009)
)
sw56k_call_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_call_fail.setStatus(
        ""
    )

sw56k_incall_answered = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6010)
)
sw56k_incall_answered.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_incall_answered.setStatus(
        ""
    )

sw56k_no_phone_num = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6011)
)
sw56k_no_phone_num.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_no_phone_num.setStatus(
        ""
    )

sw56k_incall_ignored = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6012)
)
sw56k_incall_ignored.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_incall_ignored.setStatus(
        ""
    )

sw56k_disconnect_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6013)
)
sw56k_disconnect_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_disconnect_fail.setStatus(
        ""
    )

sw56k_line_out_of_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6014)
)
sw56k_line_out_of_service.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_line_out_of_service.setStatus(
        ""
    )

sw56k_line_in_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6015)
)
sw56k_line_in_service.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_line_in_service.setStatus(
        ""
    )

sw56k_call_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6016)
)
sw56k_call_disconnected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_call_disconnected.setStatus(
        ""
    )

sw56k_in_channel_loopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6017)
)
sw56k_in_channel_loopback.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_in_channel_loopback.setStatus(
        ""
    )

sw56k_in_dsu_loopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6018)
)
sw56k_in_dsu_loopback.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sw56k_in_dsu_loopback.setStatus(
        ""
    )

x32_dial_in_not_allowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6019)
)
x32_dial_in_not_allowed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32_dial_in_not_allowed.setStatus(
        ""
    )

x32_dial_out_not_allowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6020)
)
x32_dial_out_not_allowed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32_dial_out_not_allowed.setStatus(
        ""
    )

x32_modem_faulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6021)
)
x32_modem_faulty.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32_modem_faulty.setStatus(
        ""
    )

x32_phone_num_busy = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6022)
)
x32_phone_num_busy.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32_phone_num_busy.setStatus(
        ""
    )

x32_phone_line_busy = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6023)
)
x32_phone_line_busy.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32_phone_line_busy.setStatus(
        ""
    )

x32_incompat_destination = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6024)
)
x32_incompat_destination.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32_incompat_destination.setStatus(
        ""
    )

eia6025_port_dial_nu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6025)
)
eia6025_port_dial_nu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eia6025_port_dial_nu.setStatus(
        ""
    )

eia6026_port_modem_f = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6026)
)
eia6026_port_modem_f.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eia6026_port_modem_f.setStatus(
        ""
    )

eia6027_port_modem_f = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6027)
)
eia6027_port_modem_f.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eia6027_port_modem_f.setStatus(
        ""
    )

eia6028_port_modem_f = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6028)
)
eia6028_port_modem_f.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eia6028_port_modem_f.setStatus(
        ""
    )

eia6029_port_incomin = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6029)
)
eia6029_port_incomin.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eia6029_port_incomin.setStatus(
        ""
    )

eia6030_port_no_dial = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6030)
)
eia6030_port_no_dial.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eia6030_port_no_dial.setStatus(
        ""
    )

eia6031_port_could_n = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 6031)
)
eia6031_port_could_n.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    eia6031_port_could_n.setStatus(
        ""
    )

code_software_failure_logged = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 9000)
)
code_software_failure_logged.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_software_failure_logged.setStatus(
        ""
    )

code9001_task_rescue = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 9001)
)
code9001_task_rescue.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code9001_task_rescue.setStatus(
        ""
    )

code9002_rescued_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 9002)
)
code9002_rescued_msg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code9002_rescued_msg.setStatus(
        ""
    )

code9003_rescued_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 9003)
)
code9003_rescued_msg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code9003_rescued_msg.setStatus(
        ""
    )

reports_lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 15000)
)
reports_lost.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    reports_lost.setStatus(
        ""
    )

report_log_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 15001)
)
report_log_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    report_log_cleared.setStatus(
        ""
    )

vc_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16000)
)
vc_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vc_connected.setStatus(
        ""
    )

vc_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16001)
)
vc_disconnected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vc_disconnected.setStatus(
        ""
    )

pvc_duplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16002)
)
pvc_duplication.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pvc_duplication.setStatus(
        ""
    )

pvc_not_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16003)
)
pvc_not_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pvc_not_connected.setStatus(
        ""
    )

node_boot_for_rout_tables = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16004)
)
node_boot_for_rout_tables.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_boot_for_rout_tables.setStatus(
        ""
    )

node_boot_for_pvc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16005)
)
node_boot_for_pvc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_boot_for_pvc.setStatus(
        ""
    )

rout_call_from_to_cleared_by_rou = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16006)
)
rout_call_from_to_cleared_by_rou.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout_call_from_to_cleared_by_rou.setStatus(
        ""
    )

rout16007_routproclb_ss_rout_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16007)
)
rout16007_routproclb_ss_rout_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16007_routproclb_ss_rout_down.setStatus(
        ""
    )

rout16008_routproclb_rout_not_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16008)
)
rout16008_routproclb_rout_not_found.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16008_routproclb_rout_not_found.setStatus(
        ""
    )

rout16009_routproclb_forwarding_call_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16009)
)
rout16009_routproclb_forwarding_call_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16009_routproclb_forwarding_call_req.setStatus(
        ""
    )

rout16010_routproclb_ss_rout_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16010)
)
rout16010_routproclb_ss_rout_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16010_routproclb_ss_rout_up.setStatus(
        ""
    )

rout16011_routproclb_retry_calls = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16011)
)
rout16011_routproclb_retry_calls.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16011_routproclb_retry_calls.setStatus(
        ""
    )

rout16012_rout_old_call_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16012)
)
rout16012_rout_old_call_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16012_rout_old_call_req.setStatus(
        ""
    )

rout16013_rout_call_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16013)
)
rout16013_rout_call_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16013_rout_call_req.setStatus(
        ""
    )

rout16014_rout_call_acc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16014)
)
rout16014_rout_call_acc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16014_rout_call_acc.setStatus(
        ""
    )

rout16015_rout_local_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16015)
)
rout16015_rout_local_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16015_rout_local_clear.setStatus(
        ""
    )

rout16016_rout_clear_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16016)
)
rout16016_rout_clear_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16016_rout_clear_req.setStatus(
        ""
    )

rout16017_rout_clear_call_accept = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16017)
)
rout16017_rout_clear_call_accept.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16017_rout_clear_call_accept.setStatus(
        ""
    )

rout16018_routclearcr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16018)
)
rout16018_routclearcr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16018_routclearcr.setStatus(
        ""
    )

rout16019_rout_main = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16019)
)
rout16019_rout_main.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16019_rout_main.setStatus(
        ""
    )

rout16020_rout_socksel = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16020)
)
rout16020_rout_socksel.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16020_rout_socksel.setStatus(
        ""
    )

rout16021_call_routi = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16021)
)
rout16021_call_routi.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16021_call_routi.setStatus(
        ""
    )

rout16022_routmain_p = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16022)
)
rout16022_routmain_p.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16022_routmain_p.setStatus(
        ""
    )

rout16023_packet_poi = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 16023)
)
rout16023_packet_poi.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rout16023_packet_poi.setStatus(
        ""
    )

port_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 17000)
)
port_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    port_util_exceeded.setStatus(
        ""
    )

port_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 17001)
)
port_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    port_err_count_exceeded.setStatus(
        ""
    )

cpu_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 17002)
)
cpu_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cpu_util_exceeded.setStatus(
        ""
    )

node_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19000)
)
node_reset.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_reset.setStatus(
        ""
    )

watchdog_timeout_node_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19001)
)
watchdog_timeout_node_reset.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    watchdog_timeout_node_reset.setStatus(
        ""
    )

node_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19002)
)
node_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_boot.setStatus(
        ""
    )

crash_node_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19003)
)
crash_node_reset.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    crash_node_reset.setStatus(
        ""
    )

debug_node_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19004)
)
debug_node_reset.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    debug_node_reset.setStatus(
        ""
    )

node_coldstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19005)
)
node_coldstart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_coldstart.setStatus(
        ""
    )

node_warmstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19006)
)
node_warmstart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_warmstart.setStatus(
        ""
    )

mboard_diag_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19007)
)
mboard_diag_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mboard_diag_fail.setStatus(
        ""
    )

board_diag_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19008)
)
board_diag_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    board_diag_fail.setStatus(
        ""
    )

port_diag_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19009)
)
port_diag_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    port_diag_fail.setStatus(
        ""
    )

missing_dim = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19010)
)
missing_dim.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    missing_dim.setStatus(
        ""
    )

flash_simm_diag_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19011)
)
flash_simm_diag_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    flash_simm_diag_fail.setStatus(
        ""
    )

insufficient_ram = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19012)
)
insufficient_ram.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    insufficient_ram.setStatus(
        ""
    )

port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19013)
)
port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    port_boot_fail.setStatus(
        ""
    )

local_dram_exhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19014)
)
local_dram_exhausted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    local_dram_exhausted.setStatus(
        ""
    )

bad_cmem_battery = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19015)
)
bad_cmem_battery.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bad_cmem_battery.setStatus(
        ""
    )

unexpected_interrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19016)
)
unexpected_interrupt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    unexpected_interrupt.setStatus(
        ""
    )

code_port_insuffficient_dynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19017)
)
code_port_insuffficient_dynamic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_port_insuffficient_dynamic.setStatus(
        ""
    )

code_node_reset_with_default_pas = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19018)
)
code_node_reset_with_default_pas.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_node_reset_with_default_pas.setStatus(
        ""
    )

cougar_reset_with_default_pas = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19019)
)
cougar_reset_with_default_pas.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cougar_reset_with_default_pas.setStatus(
        ""
    )

code19020_ctp_pad_setting_overridden = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 19020)
)
code19020_ctp_pad_setting_overridden.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code19020_ctp_pad_setting_overridden.setStatus(
        ""
    )

node_boot_for_mnem = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 21000)
)
node_boot_for_mnem.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_boot_for_mnem.setStatus(
        ""
    )

software_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 25000)
)
software_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    software_failure.setStatus(
        ""
    )

billing_records_lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 32000)
)
billing_records_lost.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    billing_records_lost.setStatus(
        ""
    )

dl_attempting_download = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33000)
)
dl_attempting_download.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_attempting_download.setStatus(
        ""
    )

dl_recvd_invalid_rec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33001)
)
dl_recvd_invalid_rec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_recvd_invalid_rec.setStatus(
        ""
    )

dl_recvd_no_rec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33002)
)
dl_recvd_no_rec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_recvd_no_rec.setStatus(
        ""
    )

dl_recvd_invalid_len_rec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33003)
)
dl_recvd_invalid_len_rec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_recvd_invalid_len_rec.setStatus(
        ""
    )

dl_recvd_invalid_chksum_rec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33004)
)
dl_recvd_invalid_chksum_rec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_recvd_invalid_chksum_rec.setStatus(
        ""
    )

dl_download_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33005)
)
dl_download_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_download_complete.setStatus(
        ""
    )

ds_conn_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33006)
)
ds_conn_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_conn_timeout.setStatus(
        ""
    )

dl_invl_address = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33007)
)
dl_invl_address.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_invl_address.setStatus(
        ""
    )

ds_download_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33008)
)
ds_download_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_download_complete.setStatus(
        ""
    )

ds_loading = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33009)
)
ds_loading.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_loading.setStatus(
        ""
    )

ds_incompat_cpu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33010)
)
ds_incompat_cpu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_incompat_cpu.setStatus(
        ""
    )

dl_invl_image_addr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33011)
)
dl_invl_image_addr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_invl_image_addr.setStatus(
        ""
    )

dl_flash_erase_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33012)
)
dl_flash_erase_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_flash_erase_fail.setStatus(
        ""
    )

dl_no_conf_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33013)
)
dl_no_conf_server.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_no_conf_server.setStatus(
        ""
    )

dl_flash_write_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33014)
)
dl_flash_write_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_flash_write_fail.setStatus(
        ""
    )

ds_flash_read_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33015)
)
ds_flash_read_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_flash_read_fail.setStatus(
        ""
    )

dl_software_copy_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33016)
)
dl_software_copy_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_software_copy_fail.setStatus(
        ""
    )

ds_software_send_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33017)
)
ds_software_send_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_software_send_fail.setStatus(
        ""
    )

dl_download_in_progress_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33018)
)
dl_download_in_progress_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_download_in_progress_err.setStatus(
        ""
    )

ds_flash_bank_unavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33019)
)
ds_flash_bank_unavail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_flash_bank_unavail.setStatus(
        ""
    )

ds_download_in_progress_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33020)
)
ds_download_in_progress_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_download_in_progress_err.setStatus(
        ""
    )

dl_copying_to_flash = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33021)
)
dl_copying_to_flash.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dl_copying_to_flash.setStatus(
        ""
    )

ds_no_mnemonic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33022)
)
ds_no_mnemonic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ds_no_mnemonic.setStatus(
        ""
    )

dlsv_flash_has_been_corrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 33023)
)
dlsv_flash_has_been_corrupted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dlsv_flash_has_been_corrupted.setStatus(
        ""
    )

nullPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 39000)
)
nullPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nullPort_boot.setStatus(
        ""
    )

nullPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 39001)
)
nullPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nullPort_boot_fail.setStatus(
        ""
    )

nullPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 39002)
)
nullPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nullPort_disable.setStatus(
        ""
    )

nullPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 39003)
)
nullPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nullPort_enable.setStatus(
        ""
    )

async_iodrivers_port_error_thres = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 40000)
)
async_iodrivers_port_error_thres.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async_iodrivers_port_error_thres.setStatus(
        ""
    )

async_iodrivers_unsupported_speed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 40001)
)
async_iodrivers_unsupported_speed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async_iodrivers_unsupported_speed.setStatus(
        ""
    )

bop_iodrivers_port_error_count_thres = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 41000)
)
bop_iodrivers_port_error_count_thres.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop_iodrivers_port_error_count_thres.setStatus(
        ""
    )

bop_iodrivers_unsupported_speed_oper = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 41001)
)
bop_iodrivers_unsupported_speed_oper.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop_iodrivers_unsupported_speed_oper.setStatus(
        ""
    )

lapb_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42000)
)
lapb_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_link_down.setStatus(
        ""
    )

lapb_disc_received = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42001)
)
lapb_disc_received.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_disc_received.setStatus(
        ""
    )

lapb_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42002)
)
lapb_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_bad_frame_type.setStatus(
        ""
    )

lapb_address_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42003)
)
lapb_address_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_address_error.setStatus(
        ""
    )

lapb_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42004)
)
lapb_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_bad_frame_len.setStatus(
        ""
    )

lapb_extend_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42005)
)
lapb_extend_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_extend_seq_frmr.setStatus(
        ""
    )

lapb_norm_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42006)
)
lapb_norm_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_norm_seq_frmr.setStatus(
        ""
    )

lapb_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42007)
)
lapb_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_link_up.setStatus(
        ""
    )

lapb_link_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42008)
)
lapb_link_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_link_blocked.setStatus(
        ""
    )

lapb_bad_n_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42009)
)
lapb_bad_n_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_bad_n_r.setStatus(
        ""
    )

lapb_backup_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42010)
)
lapb_backup_activated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_backup_activated.setStatus(
        ""
    )

lapb_extend_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42011)
)
lapb_extend_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_extend_bad_frame_type.setStatus(
        ""
    )

lapb_access_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42012)
)
lapb_access_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_access_link_down.setStatus(
        ""
    )

lapb_access_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42013)
)
lapb_access_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_access_link_up.setStatus(
        ""
    )

lapb_ovsize_frame = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 42014)
)
lapb_ovsize_frame.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lapb_ovsize_frame.setStatus(
        ""
    )

hdlc_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43000)
)
hdlc_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_link_down.setStatus(
        ""
    )

hdlc_disc_received = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43001)
)
hdlc_disc_received.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_disc_received.setStatus(
        ""
    )

hdlc_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43002)
)
hdlc_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_bad_frame_type.setStatus(
        ""
    )

hdlc_address_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43003)
)
hdlc_address_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_address_error.setStatus(
        ""
    )

hdlc_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43004)
)
hdlc_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_bad_frame_len.setStatus(
        ""
    )

hdlc_extend_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43005)
)
hdlc_extend_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_extend_seq_frmr.setStatus(
        ""
    )

hdlc_norm_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43006)
)
hdlc_norm_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_norm_seq_frmr.setStatus(
        ""
    )

hdlc_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43007)
)
hdlc_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_link_up.setStatus(
        ""
    )

hdlc_line_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43008)
)
hdlc_line_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_line_blocked.setStatus(
        ""
    )

hdlc_bad_n_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43009)
)
hdlc_bad_n_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_bad_n_r.setStatus(
        ""
    )

hdlc_backup_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43010)
)
hdlc_backup_activated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_backup_activated.setStatus(
        ""
    )

hdlc_extend_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43011)
)
hdlc_extend_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_extend_bad_frame_type.setStatus(
        ""
    )

hdlc_access_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43012)
)
hdlc_access_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_access_link_down.setStatus(
        ""
    )

hdlc_access_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43013)
)
hdlc_access_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_access_link_up.setStatus(
        ""
    )

hdlc_ovsize_frame = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 43014)
)
hdlc_ovsize_frame.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdlc_ovsize_frame.setStatus(
        ""
    )

apad_input_buf_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44000)
)
apad_input_buf_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apad_input_buf_overrun.setStatus(
        ""
    )

apad_hpEnqack_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44002)
)
apad_hpEnqack_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apad_hpEnqack_timeout.setStatus(
        ""
    )

apad_bcst_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44003)
)
apad_bcst_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apad_bcst_overrun.setStatus(
        ""
    )

apad_unauth_polled_async = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44004)
)
apad_unauth_polled_async.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apad_unauth_polled_async.setStatus(
        ""
    )

apad_x28_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44005)
)
apad_x28_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apad_x28_overrun.setStatus(
        ""
    )

apad_outputbuf_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44006)
)
apad_outputbuf_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apad_outputbuf_overrun.setStatus(
        ""
    )

apad_stpa_frame_dropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44007)
)
apad_stpa_frame_dropped.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apad_stpa_frame_dropped.setStatus(
        ""
    )

pad_violations_port_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44008)
)
pad_violations_port_disconnected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pad_violations_port_disconnected.setStatus(
        ""
    )

pad_violations_port_locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44009)
)
pad_violations_port_locked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pad_violations_port_locked.setStatus(
        ""
    )

pad_violations_port_degraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44010)
)
pad_violations_port_degraded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pad_violations_port_degraded.setStatus(
        ""
    )

pad_violations_no_action = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 44011)
)
pad_violations_no_action.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pad_violations_no_action.setStatus(
        ""
    )

x25L3_pkt_lvl_restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46000)
)
x25L3_pkt_lvl_restart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_pkt_lvl_restart.setStatus(
        ""
    )

x25L3_no_response = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46001)
)
x25L3_no_response.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_no_response.setStatus(
        ""
    )

x25L3_channel_reset_recv = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46002)
)
x25L3_channel_reset_recv.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_channel_reset_recv.setStatus(
        ""
    )

x25L3_rept_bad_p_k = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46003)
)
x25L3_rept_bad_p_k.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_rept_bad_p_k.setStatus(
        ""
    )

x25L3_bad_p_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46004)
)
x25L3_bad_p_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_bad_p_r.setStatus(
        ""
    )

x25L3_bad_p_s = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46005)
)
x25L3_bad_p_s.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_bad_p_s.setStatus(
        ""
    )

x25L3_pvc_not_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46006)
)
x25L3_pvc_not_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_pvc_not_connected.setStatus(
        ""
    )

x25L3_unassigned_lcn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46007)
)
x25L3_unassigned_lcn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_unassigned_lcn.setStatus(
        ""
    )

x25L3_bad_pkt_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46008)
)
x25L3_bad_pkt_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_bad_pkt_len.setStatus(
        ""
    )

x25L3_bad_pkt_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46009)
)
x25L3_bad_pkt_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_bad_pkt_type.setStatus(
        ""
    )

x25L3_bcst_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46010)
)
x25L3_bcst_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_bcst_overrun.setStatus(
        ""
    )

x25L3_input_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46011)
)
x25L3_input_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_input_overrun.setStatus(
        ""
    )

x25L3_tp_lvl_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46012)
)
x25L3_tp_lvl_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_tp_lvl_blocked.setStatus(
        ""
    )

x25L3_tp_all_lvls_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46013)
)
x25L3_tp_all_lvls_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_tp_all_lvls_blocked.setStatus(
        ""
    )

x25L3_insuff_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46014)
)
x25L3_insuff_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_insuff_memory.setStatus(
        ""
    )

x25L3_output_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46015)
)
x25L3_output_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25L3_output_overrun.setStatus(
        ""
    )

x2546016_bad_ccbptr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 46016)
)
x2546016_bad_ccbptr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x2546016_bad_ccbptr.setStatus(
        ""
    )

padPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 49000)
)
padPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    padPort_boot.setStatus(
        ""
    )

padPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 49001)
)
padPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    padPort_boot_fail.setStatus(
        ""
    )

padPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 49002)
)
padPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    padPort_disable.setStatus(
        ""
    )

padPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 49003)
)
padPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    padPort_enable.setStatus(
        ""
    )

padPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 49004)
)
padPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    padPort_util_exceeded.setStatus(
        ""
    )

padPort_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 49005)
)
padPort_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    padPort_err_count_exceeded.setStatus(
        ""
    )

padPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 49006)
)
padPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    padPort_warn_status.setStatus(
        ""
    )

x25Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 51000)
)
x25Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25Port_boot.setStatus(
        ""
    )

x25Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 51001)
)
x25Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25Port_boot_fail.setStatus(
        ""
    )

x25Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 51002)
)
x25Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25Port_disable.setStatus(
        ""
    )

x25Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 51003)
)
x25Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25Port_enable.setStatus(
        ""
    )

x25Port_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 51004)
)
x25Port_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25Port_util_exceeded.setStatus(
        ""
    )

x25Port_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 51005)
)
x25Port_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25Port_warn_status.setStatus(
        ""
    )

x25Port_pkt_size_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 51006)
)
x25Port_pkt_size_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25Port_pkt_size_warning.setStatus(
        ""
    )

bsc2780Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56000)
)
bsc2780Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_boot.setStatus(
        ""
    )

bsc2780Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56001)
)
bsc2780Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_boot_fail.setStatus(
        ""
    )

bsc2780Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56002)
)
bsc2780Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_disable.setStatus(
        ""
    )

bsc2780Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56003)
)
bsc2780Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_enable.setStatus(
        ""
    )

bsc2780Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56004)
)
bsc2780Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_enable_fail.setStatus(
        ""
    )

bsc2780Port_ses_rej = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56005)
)
bsc2780Port_ses_rej.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_ses_rej.setStatus(
        ""
    )

bsc2780Port_line_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56006)
)
bsc2780Port_line_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_line_error.setStatus(
        ""
    )

bsc2780Port_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56007)
)
bsc2780Port_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_util_exceeded.setStatus(
        ""
    )

bsc2780Port_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 56008)
)
bsc2780Port_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc2780Port_warn_status.setStatus(
        ""
    )

bsc3270Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57000)
)
bsc3270Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_boot.setStatus(
        ""
    )

bsc3270Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57001)
)
bsc3270Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_boot_fail.setStatus(
        ""
    )

bsc3270Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57002)
)
bsc3270Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_disable.setStatus(
        ""
    )

bsc3270Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57003)
)
bsc3270Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_enable.setStatus(
        ""
    )

bsc3270Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57004)
)
bsc3270Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_enable_fail.setStatus(
        ""
    )

bsc3270Port_inbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57005)
)
bsc3270Port_inbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_inbound_err.setStatus(
        ""
    )

bsc3270Port_outbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57006)
)
bsc3270Port_outbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_outbound_err.setStatus(
        ""
    )

bsc3270Port_line_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57007)
)
bsc3270Port_line_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_line_down.setStatus(
        ""
    )

bsc3270Port_line_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57008)
)
bsc3270Port_line_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_line_up.setStatus(
        ""
    )

bsc3270Port_dev_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57009)
)
bsc3270Port_dev_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_dev_down.setStatus(
        ""
    )

bsc3270Port_dev_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57010)
)
bsc3270Port_dev_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_dev_up.setStatus(
        ""
    )

bsc3270Port_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57011)
)
bsc3270Port_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270Port_warn_status.setStatus(
        ""
    )

bsc3270_device_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57012)
)
bsc3270_device_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270_device_enabled.setStatus(
        ""
    )

bsc3270_device_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57013)
)
bsc3270_device_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270_device_disabled.setStatus(
        ""
    )

bsc3270_device_enable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57014)
)
bsc3270_device_enable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270_device_enable_failure.setStatus(
        ""
    )

bsc3270_device_disable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57015)
)
bsc3270_device_disable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc3270_device_disable_failure.setStatus(
        ""
    )

bsc327057016_device = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57016)
)
bsc327057016_device.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc327057016_device.setStatus(
        ""
    )

bsc327057017_device = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 57017)
)
bsc327057017_device.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bsc327057017_device.setStatus(
        ""
    )

dsp3270_possible_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 59000)
)
dsp3270_possible_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dsp3270_possible_data_loss.setStatus(
        ""
    )

cop_iodrivers_port_error_thres = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 61000)
)
cop_iodrivers_port_error_thres.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cop_iodrivers_port_error_thres.setStatus(
        ""
    )

disk_bytes_loaded_from_nso_disk = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 65000)
)
disk_bytes_loaded_from_nso_disk.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    disk_bytes_loaded_from_nso_disk.setStatus(
        ""
    )

disk_cannot_read_from_nso_slot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 65001)
)
disk_cannot_read_from_nso_slot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    disk_cannot_read_from_nso_slot.setStatus(
        ""
    )

mx25L2_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68001)
)
mx25L2_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_stn_up.setStatus(
        ""
    )

mx25L2_multiple_masters = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68002)
)
mx25L2_multiple_masters.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_multiple_masters.setStatus(
        ""
    )

mx25L2_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68003)
)
mx25L2_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_bad_frame_type.setStatus(
        ""
    )

mx25L2_norm_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68004)
)
mx25L2_norm_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_norm_seq_frmr.setStatus(
        ""
    )

mx25L2_addr_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68005)
)
mx25L2_addr_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_addr_error.setStatus(
        ""
    )

mx25L2_master_polled_early = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68006)
)
mx25L2_master_polled_early.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_master_polled_early.setStatus(
        ""
    )

mx25L2_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68007)
)
mx25L2_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_link_up.setStatus(
        ""
    )

mx25L2_bad_n_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68008)
)
mx25L2_bad_n_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_bad_n_r.setStatus(
        ""
    )

mx25L2_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68009)
)
mx25L2_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_bad_frame_len.setStatus(
        ""
    )

mx25L2_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68010)
)
mx25L2_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_stn_down.setStatus(
        ""
    )

mx25L2_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 68011)
)
mx25L2_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25L2_link_down.setStatus(
        ""
    )

mx25Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69000)
)
mx25Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_boot.setStatus(
        ""
    )

mx25Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69001)
)
mx25Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_disable.setStatus(
        ""
    )

mx25Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69002)
)
mx25Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_enable.setStatus(
        ""
    )

mx25Port_stn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69003)
)
mx25Port_stn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_boot.setStatus(
        ""
    )

mx25Port_stn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69004)
)
mx25Port_stn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_disable.setStatus(
        ""
    )

mx25Port_stn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69005)
)
mx25Port_stn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_enable.setStatus(
        ""
    )

mx25Port_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69006)
)
mx25Port_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_util_exceeded.setStatus(
        ""
    )

mx25Port_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69007)
)
mx25Port_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_err_count_exceeded.setStatus(
        ""
    )

mx25Port_stn_addr_dupl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69008)
)
mx25Port_stn_addr_dupl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_addr_dupl.setStatus(
        ""
    )

mx25Port_stn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69009)
)
mx25Port_stn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_boot_fail.setStatus(
        ""
    )

mx25Port_stn_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69010)
)
mx25Port_stn_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_enable_fail.setStatus(
        ""
    )

mx25Port_stn_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69011)
)
mx25Port_stn_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_disable_fail.setStatus(
        ""
    )

mx25Port_stn_bsyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69012)
)
mx25Port_stn_bsyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_bsyout_fail.setStatus(
        ""
    )

mx25Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69013)
)
mx25Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_boot_fail.setStatus(
        ""
    )

mx25Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69014)
)
mx25Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_enable_fail.setStatus(
        ""
    )

mx25Port_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69015)
)
mx25Port_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_disable_fail.setStatus(
        ""
    )

mx25Port_busyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69016)
)
mx25Port_busyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_busyout_fail.setStatus(
        ""
    )

mx25Port_stn_bsyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69017)
)
mx25Port_stn_bsyout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_stn_bsyout.setStatus(
        ""
    )

mx25Port_busyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69018)
)
mx25Port_busyout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_busyout.setStatus(
        ""
    )

mx25Port_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 69019)
)
mx25Port_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mx25Port_warn_status.setStatus(
        ""
    )

sdlcPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74000)
)
sdlcPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_boot.setStatus(
        ""
    )

sdlcPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74001)
)
sdlcPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_boot_fail.setStatus(
        ""
    )

sdlcPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74002)
)
sdlcPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_disable.setStatus(
        ""
    )

sdlcPort_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74003)
)
sdlcPort_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_disable_fail.setStatus(
        ""
    )

sdlcPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74004)
)
sdlcPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_enable.setStatus(
        ""
    )

sdlcPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74005)
)
sdlcPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_enable_fail.setStatus(
        ""
    )

sdlcPort_stn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74006)
)
sdlcPort_stn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_boot.setStatus(
        ""
    )

sdlcPort_stn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74007)
)
sdlcPort_stn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_boot_fail.setStatus(
        ""
    )

sdlcPort_stn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74008)
)
sdlcPort_stn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_disable.setStatus(
        ""
    )

sdlcPort_stn_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74009)
)
sdlcPort_stn_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_disable_fail.setStatus(
        ""
    )

sdlcPort_stn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74010)
)
sdlcPort_stn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_enable.setStatus(
        ""
    )

sdlcPort_stn_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74011)
)
sdlcPort_stn_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_enable_fail.setStatus(
        ""
    )

sdlcPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74012)
)
sdlcPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_util_exceeded.setStatus(
        ""
    )

sdlcPort_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74013)
)
sdlcPort_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_err_count_exceeded.setStatus(
        ""
    )

sdlcPort_busyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74014)
)
sdlcPort_busyout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_busyout.setStatus(
        ""
    )

sdlcPort_busyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74015)
)
sdlcPort_busyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_busyout_fail.setStatus(
        ""
    )

sdlcPort_stn_busy_out = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74016)
)
sdlcPort_stn_busy_out.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_busy_out.setStatus(
        ""
    )

sdlcPort_stn_busyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74017)
)
sdlcPort_stn_busyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_stn_busyout_fail.setStatus(
        ""
    )

sdlcPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74018)
)
sdlcPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_warn_status.setStatus(
        ""
    )

sdlcPort_insuff_mem = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74019)
)
sdlcPort_insuff_mem.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_insuff_mem.setStatus(
        ""
    )

sdlcPort_unsup_frm_size = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74020)
)
sdlcPort_unsup_frm_size.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcPort_unsup_frm_size.setStatus(
        ""
    )

sna74021_sdlc_s_dyna = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74021)
)
sna74021_sdlc_s_dyna.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sna74021_sdlc_s_dyna.setStatus(
        ""
    )

sna74022_sdlc_s_dyna = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74022)
)
sna74022_sdlc_s_dyna.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sna74022_sdlc_s_dyna.setStatus(
        ""
    )

sna74023_sdlc_s_dyna = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 74023)
)
sna74023_sdlc_s_dyna.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sna74023_sdlc_s_dyna.setStatus(
        ""
    )

sdlcL2_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75001)
)
sdlcL2_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_bad_frame_len.setStatus(
        ""
    )

sdlcL2_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75002)
)
sdlcL2_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_bad_frame_type.setStatus(
        ""
    )

sdlcL2_bad_n_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75003)
)
sdlcL2_bad_n_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_bad_n_r.setStatus(
        ""
    )

sdlcL2_master_polled_early = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75004)
)
sdlcL2_master_polled_early.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_master_polled_early.setStatus(
        ""
    )

sdlcL2_norm_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75005)
)
sdlcL2_norm_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_norm_seq_frmr.setStatus(
        ""
    )

sdlcL2_stn_disconn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75006)
)
sdlcL2_stn_disconn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_stn_disconn.setStatus(
        ""
    )

sdlcL2_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75007)
)
sdlcL2_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_stn_down.setStatus(
        ""
    )

sdlcL2_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75008)
)
sdlcL2_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_stn_up.setStatus(
        ""
    )

sdlcL2_addr_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75009)
)
sdlcL2_addr_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_addr_error.setStatus(
        ""
    )

sdlcL2_hpad_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75010)
)
sdlcL2_hpad_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_hpad_stn_down.setStatus(
        ""
    )

sdlcL2_hpad_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75011)
)
sdlcL2_hpad_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_hpad_stn_up.setStatus(
        ""
    )

sdlcL2_hpad_stn_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75012)
)
sdlcL2_hpad_stn_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_hpad_stn_active.setStatus(
        ""
    )

sdlcL2_hpad_stn_inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75013)
)
sdlcL2_hpad_stn_inactive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_hpad_stn_inactive.setStatus(
        ""
    )

sdlcL2_tpad_stn_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75014)
)
sdlcL2_tpad_stn_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_tpad_stn_active.setStatus(
        ""
    )

sdlcL2_tpad_stn_inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75015)
)
sdlcL2_tpad_stn_inactive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_tpad_stn_inactive.setStatus(
        ""
    )

sdlcL2_ovsize_frame = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 75016)
)
sdlcL2_ovsize_frame.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sdlcL2_ovsize_frame.setStatus(
        ""
    )

qllc_proto_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76000)
)
qllc_proto_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_proto_error.setStatus(
        ""
    )

qllc_bad_pkt_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76001)
)
qllc_bad_pkt_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_bad_pkt_len.setStatus(
        ""
    )

qllc_illegal_pkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76002)
)
qllc_illegal_pkt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_illegal_pkt.setStatus(
        ""
    )

qllc_qfrmr_receive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76003)
)
qllc_qfrmr_receive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_qfrmr_receive.setStatus(
        ""
    )

qllc_tpad_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76004)
)
qllc_tpad_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_tpad_stn_up.setStatus(
        ""
    )

qllc_tpad_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76005)
)
qllc_tpad_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_tpad_stn_down.setStatus(
        ""
    )

qllc_net_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76006)
)
qllc_net_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_net_link_up.setStatus(
        ""
    )

qllc_net_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 76007)
)
qllc_net_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qllc_net_link_down.setStatus(
        ""
    )

ncrbscPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86000)
)
ncrbscPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_boot.setStatus(
        ""
    )

ncrbscPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86001)
)
ncrbscPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_boot_fail.setStatus(
        ""
    )

ncrbscPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86002)
)
ncrbscPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_disable.setStatus(
        ""
    )

ncrbscPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86003)
)
ncrbscPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_enable.setStatus(
        ""
    )

ncrbscPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86004)
)
ncrbscPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_enable_fail.setStatus(
        ""
    )

ncrbscPort_inbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86005)
)
ncrbscPort_inbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_inbound_err.setStatus(
        ""
    )

ncrbscPort_outbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86006)
)
ncrbscPort_outbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_outbound_err.setStatus(
        ""
    )

ncrbscPort_line_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86007)
)
ncrbscPort_line_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_line_down.setStatus(
        ""
    )

ncrbscPort_line_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86008)
)
ncrbscPort_line_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_line_up.setStatus(
        ""
    )

ncrbscPort_dev_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86009)
)
ncrbscPort_dev_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_dev_down.setStatus(
        ""
    )

ncrbscPort_dev_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86010)
)
ncrbscPort_dev_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_dev_up.setStatus(
        ""
    )

ncrbscPort_dev_unavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86011)
)
ncrbscPort_dev_unavail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbscPort_dev_unavail.setStatus(
        ""
    )

ncrbsc_list_is_empty = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86012)
)
ncrbsc_list_is_empty.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbsc_list_is_empty.setStatus(
        ""
    )

ncrbsc_list_is_not_empty = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 86013)
)
ncrbsc_list_is_not_empty.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ncrbsc_list_is_not_empty.setStatus(
        ""
    )

friL2_unconfigured_dlci = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87000)
)
friL2_unconfigured_dlci.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_unconfigured_dlci.setStatus(
        ""
    )

friL2_pkt_for_disable_stn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87001)
)
friL2_pkt_for_disable_stn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_pkt_for_disable_stn.setStatus(
        ""
    )

friL2_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87002)
)
friL2_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_bad_frame_len.setStatus(
        ""
    )

friL2_annexd_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87003)
)
friL2_annexd_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_annexd_error.setStatus(
        ""
    )

friL2_lmi_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87004)
)
friL2_lmi_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_lmi_error.setStatus(
        ""
    )

friL2_bypass_stn_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87005)
)
friL2_bypass_stn_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_bypass_stn_link_up.setStatus(
        ""
    )

friL2_bypass_stn_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87006)
)
friL2_bypass_stn_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_bypass_stn_link_down.setStatus(
        ""
    )

friL2_annexa_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87007)
)
friL2_annexa_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_annexa_error.setStatus(
        ""
    )

friL2_unused_net_dlci = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87008)
)
friL2_unused_net_dlci.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friL2_unused_net_dlci.setStatus(
        ""
    )

fri_prot_detect_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87009)
)
fri_prot_detect_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_prot_detect_timeout.setStatus(
        ""
    )

fri_prot_change = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87010)
)
fri_prot_change.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_prot_change.setStatus(
        ""
    )

fri_frm_seg_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87011)
)
fri_frm_seg_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_frm_seg_down.setStatus(
        ""
    )

fri_frm_seg_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87012)
)
fri_frm_seg_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_frm_seg_up.setStatus(
        ""
    )

fri_rx_lmi_status_update_contain = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87013)
)
fri_rx_lmi_status_update_contain.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_rx_lmi_status_update_contain.setStatus(
        ""
    )

fri_frame_received_invalid_addre = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87014)
)
fri_frame_received_invalid_addre.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_frame_received_invalid_addre.setStatus(
        ""
    )

fri_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87015)
)
fri_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_link_up.setStatus(
        ""
    )

fri_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87016)
)
fri_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_link_down.setStatus(
        ""
    )

fri_protocol_error_threshold_rea = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87017)
)
fri_protocol_error_threshold_rea.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_protocol_error_threshold_rea.setStatus(
        ""
    )

fri87018_uni_segment = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87018)
)
fri87018_uni_segment.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri87018_uni_segment.setStatus(
        ""
    )

fri87019_uni_segment = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 87019)
)
fri87019_uni_segment.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri87019_uni_segment.setStatus(
        ""
    )

friPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88000)
)
friPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_boot.setStatus(
        ""
    )

friPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88001)
)
friPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_boot_fail.setStatus(
        ""
    )

friPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88002)
)
friPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_disable.setStatus(
        ""
    )

friPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88003)
)
friPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_enable.setStatus(
        ""
    )

friPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88004)
)
friPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_util_exceeded.setStatus(
        ""
    )

friPort_stn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88005)
)
friPort_stn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_stn_disable.setStatus(
        ""
    )

friPort_stn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88006)
)
friPort_stn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_stn_enable.setStatus(
        ""
    )

friPort_stn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88007)
)
friPort_stn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_stn_boot.setStatus(
        ""
    )

friPort_stn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88008)
)
friPort_stn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_stn_boot_fail.setStatus(
        ""
    )

friPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88009)
)
friPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    friPort_warn_status.setStatus(
        ""
    )

fripPort_boot_Stn_novbd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88010)
)
fripPort_boot_Stn_novbd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fripPort_boot_Stn_novbd.setStatus(
        ""
    )

fripPort_boot_Stn_novoice = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88011)
)
fripPort_boot_Stn_novoice.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fripPort_boot_Stn_novoice.setStatus(
        ""
    )

fripPort_boot_vbd_noseg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88012)
)
fripPort_boot_vbd_noseg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fripPort_boot_vbd_noseg.setStatus(
        ""
    )

frip_Port_boot_seg_novbd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88013)
)
frip_Port_boot_seg_novbd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    frip_Port_boot_seg_novbd.setStatus(
        ""
    )

fri_suspicious_configuration_fra = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88014)
)
fri_suspicious_configuration_fra.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_suspicious_configuration_fra.setStatus(
        ""
    )

fri_rfc1315_ifindexdlcifrcircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88015)
)
fri_rfc1315_ifindexdlcifrcircuit.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_rfc1315_ifindexdlcifrcircuit.setStatus(
        ""
    )

fri_port_update_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88016)
)
fri_port_update_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_port_update_complete.setStatus(
        ""
    )

fri_out_of_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 88017)
)
fri_out_of_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fri_out_of_memory.setStatus(
        ""
    )

dcp_fsm_call_termination = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 90000)
)
dcp_fsm_call_termination.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_fsm_call_termination.setStatus(
        ""
    )

dcp_na_fac_set_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91000)
)
dcp_na_fac_set_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_fac_set_fail.setStatus(
        ""
    )

dcp_na_fac_get_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91001)
)
dcp_na_fac_get_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_fac_get_fail.setStatus(
        ""
    )

dcp_na_null_ptr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91002)
)
dcp_na_null_ptr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_null_ptr.setStatus(
        ""
    )

dcp_na_invalid_cr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91003)
)
dcp_na_invalid_cr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_invalid_cr.setStatus(
        ""
    )

dcp_na_invalid_cc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91004)
)
dcp_na_invalid_cc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_invalid_cc.setStatus(
        ""
    )

dcp_na_invalid_pkt_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91005)
)
dcp_na_invalid_pkt_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_invalid_pkt_type.setStatus(
        ""
    )

dcp_na_invalid_tpdu_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91006)
)
dcp_na_invalid_tpdu_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_invalid_tpdu_len.setStatus(
        ""
    )

dcp_na_invalid_tpdu_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 91007)
)
dcp_na_invalid_tpdu_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_na_invalid_tpdu_type.setStatus(
        ""
    )

dcp_pa_invalid_pkt_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 92000)
)
dcp_pa_invalid_pkt_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_pa_invalid_pkt_type.setStatus(
        ""
    )

dcp_pa_null_ptr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 92001)
)
dcp_pa_null_ptr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dcp_pa_null_ptr.setStatus(
        ""
    )

dsdPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 94000)
)
dsdPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dsdPort_boot.setStatus(
        ""
    )

dsdPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 94001)
)
dsdPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dsdPort_boot_fail.setStatus(
        ""
    )

rs366Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 97000)
)
rs366Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rs366Port_boot.setStatus(
        ""
    )

rs366Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 97001)
)
rs366Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rs366Port_boot_fail.setStatus(
        ""
    )

rs366Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 97002)
)
rs366Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rs366Port_disable.setStatus(
        ""
    )

rs366Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 97003)
)
rs366Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rs366Port_enable.setStatus(
        ""
    )

rs366Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 97004)
)
rs366Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rs366Port_enable_fail.setStatus(
        ""
    )

rs366Port_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 97005)
)
rs366Port_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    rs366Port_disable_fail.setStatus(
        ""
    )

flash_cannot_read_from_memory_sl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 104000)
)
flash_cannot_read_from_memory_sl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    flash_cannot_read_from_memory_sl.setStatus(
        ""
    )

software_copying_to_flash = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105000)
)
software_copying_to_flash.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    software_copying_to_flash.setStatus(
        ""
    )

num_bytes_copied_to_flash = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105001)
)
num_bytes_copied_to_flash.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    num_bytes_copied_to_flash.setStatus(
        ""
    )

copy_to_flash_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105002)
)
copy_to_flash_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    copy_to_flash_complete.setStatus(
        ""
    )

copy_to_flash_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105003)
)
copy_to_flash_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    copy_to_flash_fail.setStatus(
        ""
    )

updating_software = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105004)
)
updating_software.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    updating_software.setStatus(
        ""
    )

software_update_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105005)
)
software_update_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    software_update_complete.setStatus(
        ""
    )

software_update_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105006)
)
software_update_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    software_update_fail.setStatus(
        ""
    )

flash_checksum_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105007)
)
flash_checksum_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    flash_checksum_err.setStatus(
        ""
    )

flash_erase_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105008)
)
flash_erase_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    flash_erase_fail.setStatus(
        ""
    )

flash_write_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105009)
)
flash_write_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    flash_write_fail.setStatus(
        ""
    )

lfash_copying = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105010)
)
lfash_copying.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lfash_copying.setStatus(
        ""
    )

lflash_copy = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105011)
)
lflash_copy.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lflash_copy.setStatus(
        ""
    )

lflash_copy_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105012)
)
lflash_copy_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lflash_copy_fail.setStatus(
        ""
    )

sd_copying_software_from_local_f = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105013)
)
sd_copying_software_from_local_f.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sd_copying_software_from_local_f.setStatus(
        ""
    )

sd_local_flash_copy_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105014)
)
sd_local_flash_copy_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sd_local_flash_copy_complete.setStatus(
        ""
    )

sd_local_flash_copy_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 105015)
)
sd_local_flash_copy_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sd_local_flash_copy_failed.setStatus(
        ""
    )

cmem_simm_init = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 106000)
)
cmem_simm_init.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cmem_simm_init.setStatus(
        ""
    )

alt_flash_software_load = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 106001)
)
alt_flash_software_load.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alt_flash_software_load.setStatus(
        ""
    )

unknown_card_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 106002)
)
unknown_card_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    unknown_card_type.setStatus(
        ""
    )

mboard_lab_strap_install = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 106003)
)
mboard_lab_strap_install.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mboard_lab_strap_install.setStatus(
        ""
    )

async302_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 107000)
)
async302_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async302_err_count_exceeded.setStatus(
        ""
    )

async302_dbits_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 107001)
)
async302_dbits_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async302_dbits_unsupp.setStatus(
        ""
    )

async302_baud_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 107002)
)
async302_baud_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async302_baud_unsupp.setStatus(
        ""
    )

async302_parity_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 107003)
)
async302_parity_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async302_parity_unsupp.setStatus(
        ""
    )

bop302_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 108000)
)
bop302_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop302_err_count_exceeded.setStatus(
        ""
    )

bop302_unsupp_speed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 108001)
)
bop302_unsupp_speed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop302_unsupp_speed.setStatus(
        ""
    )

bop302_rx_byte_count_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 108002)
)
bop302_rx_byte_count_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop302_rx_byte_count_err.setStatus(
        ""
    )

bop302_erroneous_bool = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 108003)
)
bop302_erroneous_bool.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop302_erroneous_bool.setStatus(
        ""
    )

bop302_clk_override = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 108004)
)
bop302_clk_override.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop302_clk_override.setStatus(
        ""
    )

bop302_tx_sanity_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 108005)
)
bop302_tx_sanity_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop302_tx_sanity_timeout.setStatus(
        ""
    )

iodrivers108006_corr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 108006)
)
iodrivers108006_corr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers108006_corr.setStatus(
        ""
    )

cop302_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 109000)
)
cop302_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cop302_err_count_exceeded.setStatus(
        ""
    )

bstdPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110000)
)
bstdPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_boot.setStatus(
        ""
    )

bstdPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110001)
)
bstdPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_boot_fail.setStatus(
        ""
    )

bstdPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110002)
)
bstdPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_disable.setStatus(
        ""
    )

bstdPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110003)
)
bstdPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_enable.setStatus(
        ""
    )

bstdPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110004)
)
bstdPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_enable_fail.setStatus(
        ""
    )

bstdPort_inbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110005)
)
bstdPort_inbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_inbound_err.setStatus(
        ""
    )

bstdPort_outbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110006)
)
bstdPort_outbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_outbound_err.setStatus(
        ""
    )

bstdPort_line_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110007)
)
bstdPort_line_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_line_down.setStatus(
        ""
    )

bstdPort_line_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110008)
)
bstdPort_line_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_line_up.setStatus(
        ""
    )

bstdPort_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110009)
)
bstdPort_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_stn_down.setStatus(
        ""
    )

bstdPort_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110010)
)
bstdPort_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_stn_up.setStatus(
        ""
    )

bstdPort_address_conflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110011)
)
bstdPort_address_conflict.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_address_conflict.setStatus(
        ""
    )

bstdPort_possible_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110012)
)
bstdPort_possible_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_possible_data_loss.setStatus(
        ""
    )

bstdPort_cont_tgrp_conflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110013)
)
bstdPort_cont_tgrp_conflict.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_cont_tgrp_conflict.setStatus(
        ""
    )

bstdPort_hpad_tgrp_conflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110014)
)
bstdPort_hpad_tgrp_conflict.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstdPort_hpad_tgrp_conflict.setStatus(
        ""
    )

bstd_station_inhibited_no_dsp_co = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110015)
)
bstd_station_inhibited_no_dsp_co.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstd_station_inhibited_no_dsp_co.setStatus(
        ""
    )

bstd_initialization_failed_softw = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 110016)
)
bstd_initialization_failed_softw.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bstd_initialization_failed_softw.setStatus(
        ""
    )

xdlcL2_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111001)
)
xdlcL2_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_bad_frame_len.setStatus(
        ""
    )

xdlcL2_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111002)
)
xdlcL2_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_bad_frame_type.setStatus(
        ""
    )

xdlcL2_bad_n_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111003)
)
xdlcL2_bad_n_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_bad_n_r.setStatus(
        ""
    )

xdlcL2_addr_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111004)
)
xdlcL2_addr_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_addr_error.setStatus(
        ""
    )

xdlcL2_norm_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111005)
)
xdlcL2_norm_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_norm_seq_frmr.setStatus(
        ""
    )

xdlcL2_stn_disconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111006)
)
xdlcL2_stn_disconnect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_stn_disconnect.setStatus(
        ""
    )

xdlcL2_mx25_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111007)
)
xdlcL2_mx25_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_mx25_stn_down.setStatus(
        ""
    )

xdlcL2_mx25_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111008)
)
xdlcL2_mx25_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_mx25_stn_up.setStatus(
        ""
    )

xdlcL2_multiple_masters = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111009)
)
xdlcL2_multiple_masters.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_multiple_masters.setStatus(
        ""
    )

xdlcL2_stat_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111010)
)
xdlcL2_stat_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_stat_overflow.setStatus(
        ""
    )

xdlcL2_tpad_stn_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111011)
)
xdlcL2_tpad_stn_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_tpad_stn_active.setStatus(
        ""
    )

xdlcL2_tpad_stn_inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111012)
)
xdlcL2_tpad_stn_inactive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_tpad_stn_inactive.setStatus(
        ""
    )

xdlcL2_ovsize_frame = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 111013)
)
xdlcL2_ovsize_frame.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcL2_ovsize_frame.setStatus(
        ""
    )

xdlcPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112000)
)
xdlcPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_boot.setStatus(
        ""
    )

xdlcPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112001)
)
xdlcPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_boot_fail.setStatus(
        ""
    )

xdlcPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112002)
)
xdlcPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_disable.setStatus(
        ""
    )

xdlcPort_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112003)
)
xdlcPort_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_disable_fail.setStatus(
        ""
    )

xdlcPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112004)
)
xdlcPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_enable.setStatus(
        ""
    )

xdlcPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112005)
)
xdlcPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_enable_fail.setStatus(
        ""
    )

xdlcPort_stn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112006)
)
xdlcPort_stn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_boot.setStatus(
        ""
    )

xdlcPort_stn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112007)
)
xdlcPort_stn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_boot_fail.setStatus(
        ""
    )

xdlcPort_stn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112008)
)
xdlcPort_stn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_disable.setStatus(
        ""
    )

xdlcPort_stn_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112009)
)
xdlcPort_stn_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_disable_fail.setStatus(
        ""
    )

xdlcPort_stn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112010)
)
xdlcPort_stn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_enable.setStatus(
        ""
    )

xdlcPort_stn_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112011)
)
xdlcPort_stn_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_enable_fail.setStatus(
        ""
    )

xdlcPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112012)
)
xdlcPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_util_exceeded.setStatus(
        ""
    )

xdlcPort_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112013)
)
xdlcPort_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_err_count_exceeded.setStatus(
        ""
    )

xdlcPort_stn_addr_dupl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112014)
)
xdlcPort_stn_addr_dupl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_addr_dupl.setStatus(
        ""
    )

xdlcPort_stat_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112015)
)
xdlcPort_stat_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stat_overflow.setStatus(
        ""
    )

xdlcPort_stn_stat_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112016)
)
xdlcPort_stn_stat_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_stn_stat_overflow.setStatus(
        ""
    )

xdlcPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112017)
)
xdlcPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_warn_status.setStatus(
        ""
    )

xdlcPort_unsupport_frm_size = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112018)
)
xdlcPort_unsupport_frm_size.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlcPort_unsupport_frm_size.setStatus(
        ""
    )

xdlc_insufficient_memory_to_prot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112019)
)
xdlc_insufficient_memory_to_prot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlc_insufficient_memory_to_prot.setStatus(
        ""
    )

xdlc112020_xdlc_s_dy = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112020)
)
xdlc112020_xdlc_s_dy.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlc112020_xdlc_s_dy.setStatus(
        ""
    )

xdlc112021_xdlc_s_dy = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112021)
)
xdlc112021_xdlc_s_dy.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlc112021_xdlc_s_dy.setStatus(
        ""
    )

xdlc112022_xdlc_s_dy = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112022)
)
xdlc112022_xdlc_s_dy.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlc112022_xdlc_s_dy.setStatus(
        ""
    )

xdlc112023_insuffici = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 112023)
)
xdlc112023_insuffici.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xdlc112023_insuffici.setStatus(
        ""
    )

nccpDpad_unknown_device = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115000)
)
nccpDpad_unknown_device.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_unknown_device.setStatus(
        ""
    )

nccpDpad_crc_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115001)
)
nccpDpad_crc_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_crc_error.setStatus(
        ""
    )

nccpDpad_streaming_device = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115002)
)
nccpDpad_streaming_device.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_streaming_device.setStatus(
        ""
    )

nccpDpad_stream_device_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115003)
)
nccpDpad_stream_device_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_stream_device_clear.setStatus(
        ""
    )

nccpDpad_main_chan_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115004)
)
nccpDpad_main_chan_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_main_chan_fail.setStatus(
        ""
    )

nccpDpad_main_chan_connect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115005)
)
nccpDpad_main_chan_connect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_main_chan_connect.setStatus(
        ""
    )

nccpDpad_main_chan_disconn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115006)
)
nccpDpad_main_chan_disconn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_main_chan_disconn.setStatus(
        ""
    )

nccpDpad_state_search_abort = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 115007)
)
nccpDpad_state_search_abort.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpDpad_state_search_abort.setStatus(
        ""
    )

nccpMpad_not_responding = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 116000)
)
nccpMpad_not_responding.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpMpad_not_responding.setStatus(
        ""
    )

nccpMpad_device_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 116001)
)
nccpMpad_device_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpMpad_device_status.setStatus(
        ""
    )

nccpMpad_dupl_device = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 116002)
)
nccpMpad_dupl_device.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpMpad_dupl_device.setStatus(
        ""
    )

nccpMpad_chan_conn_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 116003)
)
nccpMpad_chan_conn_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpMpad_chan_conn_fail.setStatus(
        ""
    )

nccpMpad_chan_conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 116004)
)
nccpMpad_chan_conn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpMpad_chan_conn.setStatus(
        ""
    )

nccpMpad_chan_disconn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 116005)
)
nccpMpad_chan_disconn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpMpad_chan_disconn.setStatus(
        ""
    )

nccpMpad_proto_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 116006)
)
nccpMpad_proto_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    nccpMpad_proto_err.setStatus(
        ""
    )

ibm2260Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125000)
)
ibm2260Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_boot.setStatus(
        ""
    )

ibm2260Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125001)
)
ibm2260Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_boot_fail.setStatus(
        ""
    )

ibm2260Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125002)
)
ibm2260Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_disable.setStatus(
        ""
    )

ibm2260Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125003)
)
ibm2260Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_enable.setStatus(
        ""
    )

ibm2260Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125004)
)
ibm2260Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_enable_fail.setStatus(
        ""
    )

ibm2260Port_inbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125005)
)
ibm2260Port_inbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_inbound_err.setStatus(
        ""
    )

ibm2260Port_outbound_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125006)
)
ibm2260Port_outbound_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_outbound_err.setStatus(
        ""
    )

ibm2260Port_line_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125007)
)
ibm2260Port_line_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_line_down.setStatus(
        ""
    )

ibm2260Port_line_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125008)
)
ibm2260Port_line_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_line_up.setStatus(
        ""
    )

ibm2260Port_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125009)
)
ibm2260Port_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_stn_down.setStatus(
        ""
    )

ibm2260Port_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125010)
)
ibm2260Port_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_stn_up.setStatus(
        ""
    )

ibm2260Port_addr_conflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125011)
)
ibm2260Port_addr_conflict.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_addr_conflict.setStatus(
        ""
    )

ibm2260Port_poss_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 125012)
)
ibm2260Port_poss_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ibm2260Port_poss_data_loss.setStatus(
        ""
    )

tbopPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126000)
)
tbopPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_boot.setStatus(
        ""
    )

tbopPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126001)
)
tbopPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_boot_fail.setStatus(
        ""
    )

tbopPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126002)
)
tbopPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_disable.setStatus(
        ""
    )

tbopPort_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126003)
)
tbopPort_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_disable_fail.setStatus(
        ""
    )

tbopPort_Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126004)
)
tbopPort_Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_Port_enable.setStatus(
        ""
    )

tbopPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126005)
)
tbopPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_enable_fail.setStatus(
        ""
    )

tbopPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126006)
)
tbopPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_util_exceeded.setStatus(
        ""
    )

tbopPort_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126007)
)
tbopPort_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_err_count_exceeded.setStatus(
        ""
    )

tbopPort_busyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126008)
)
tbopPort_busyout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_busyout.setStatus(
        ""
    )

tbopPort_busyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126009)
)
tbopPort_busyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopPort_busyout_fail.setStatus(
        ""
    )

tbop_port_status_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 126010)
)
tbop_port_status_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbop_port_status_warning.setStatus(
        ""
    )

tbopL2_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 127001)
)
tbopL2_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tbopL2_bad_frame_len.setStatus(
        ""
    )

tcop_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129000)
)
tcop_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_boot.setStatus(
        ""
    )

tcop_Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129001)
)
tcop_Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_boot_fail.setStatus(
        ""
    )

tcop_Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129002)
)
tcop_Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_disable.setStatus(
        ""
    )

tcop_Port_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129003)
)
tcop_Port_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_disable_fail.setStatus(
        ""
    )

tcop_Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129004)
)
tcop_Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_enable.setStatus(
        ""
    )

tcop_Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129005)
)
tcop_Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_enable_fail.setStatus(
        ""
    )

tcop_Port_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129006)
)
tcop_Port_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_util_exceeded.setStatus(
        ""
    )

tcop_Port_error_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129007)
)
tcop_Port_error_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_error_exceeded.setStatus(
        ""
    )

tcop_Port_busy_out = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129008)
)
tcop_Port_busy_out.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_busy_out.setStatus(
        ""
    )

tcop_Port_busy_out_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129009)
)
tcop_Port_busy_out_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_busy_out_fail.setStatus(
        ""
    )

tcop_Port_subtype_notsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 129010)
)
tcop_Port_subtype_notsupported.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_Port_subtype_notsupported.setStatus(
        ""
    )

tcop_rx_queue_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 130001)
)
tcop_rx_queue_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_rx_queue_overflow.setStatus(
        ""
    )

tcop_tx_queue_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 130002)
)
tcop_tx_queue_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_tx_queue_overflow.setStatus(
        ""
    )

tcop_tx_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 130003)
)
tcop_tx_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_tx_timeout.setStatus(
        ""
    )

tcop_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 130004)
)
tcop_threshold.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcop_threshold.setStatus(
        ""
    )

bridge_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134000)
)
bridge_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_init_fail.setStatus(
        ""
    )

bridge_link_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134001)
)
bridge_link_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_link_boot.setStatus(
        ""
    )

bridge_link_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134002)
)
bridge_link_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_link_boot_fail.setStatus(
        ""
    )

bridge_link_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134003)
)
bridge_link_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_link_enabled.setStatus(
        ""
    )

bridge_link_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134004)
)
bridge_link_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_link_disabled.setStatus(
        ""
    )

bridge_param_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134005)
)
bridge_param_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_param_boot.setStatus(
        ""
    )

bridge_param_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134006)
)
bridge_param_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_param_boot_fail.setStatus(
        ""
    )

bridge_link_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 134007)
)
bridge_link_out_of_range.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bridge_link_out_of_range.setStatus(
        ""
    )

sr_ring_num_mismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 136000)
)
sr_ring_num_mismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sr_ring_num_mismatch.setStatus(
        ""
    )

sr_bridge_id_mismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 136001)
)
sr_bridge_id_mismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sr_bridge_id_mismatch.setStatus(
        ""
    )

sr_dupl_rbr_triplet = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 136002)
)
sr_dupl_rbr_triplet.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sr_dupl_rbr_triplet.setStatus(
        ""
    )

sr_incompat_link_mode = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 136003)
)
sr_incompat_link_mode.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sr_incompat_link_mode.setStatus(
        ""
    )

include_br_one_trans_link_allowe = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 136004)
)
include_br_one_trans_link_allowe.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    include_br_one_trans_link_allowe.setStatus(
        ""
    )

sr_duplicate_token_ring = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 136005)
)
sr_duplicate_token_ring.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sr_duplicate_token_ring.setStatus(
        ""
    )

stp_unknown_bpdu_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 137000)
)
stp_unknown_bpdu_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    stp_unknown_bpdu_type.setStatus(
        ""
    )

stp_bridge_is_root = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 137001)
)
stp_bridge_is_root.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    stp_bridge_is_root.setStatus(
        ""
    )

stp_bridge_is_not_root = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 137002)
)
stp_bridge_is_not_root.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    stp_bridge_is_not_root.setStatus(
        ""
    )

stp_topo_unstable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 137003)
)
stp_topo_unstable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    stp_topo_unstable.setStatus(
        ""
    )

stp_topo_stable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 137004)
)
stp_topo_stable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    stp_topo_stable.setStatus(
        ""
    )

stp_config_buff_not_avail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 137005)
)
stp_config_buff_not_avail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    stp_config_buff_not_avail.setStatus(
        ""
    )

stp_tcn_buff_not_avail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 137006)
)
stp_tcn_buff_not_avail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    stp_tcn_buff_not_avail.setStatus(
        ""
    )

trPort_reset_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138000)
)
trPort_reset_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_reset_fail.setStatus(
        ""
    )

trPort_chip_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138001)
)
trPort_chip_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_chip_init_fail.setStatus(
        ""
    )

trPort_open_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138002)
)
trPort_open_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_open_fail.setStatus(
        ""
    )

trPort_Port_init = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138003)
)
trPort_Port_init.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_Port_init.setStatus(
        ""
    )

trPort_rx_cmd_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138004)
)
trPort_rx_cmd_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_rx_cmd_timeout.setStatus(
        ""
    )

trPort_tx_cmd_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138005)
)
trPort_tx_cmd_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_tx_cmd_timeout.setStatus(
        ""
    )

trPort_loss_of_signal = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138006)
)
trPort_loss_of_signal.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_loss_of_signal.setStatus(
        ""
    )

trPort_loss_of_signal_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138007)
)
trPort_loss_of_signal_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_loss_of_signal_clear.setStatus(
        ""
    )

trPort_beacon = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138008)
)
trPort_beacon.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_beacon.setStatus(
        ""
    )

trPort_beacon_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138009)
)
trPort_beacon_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_beacon_clear.setStatus(
        ""
    )

trPort_tx_beacon = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138010)
)
trPort_tx_beacon.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_tx_beacon.setStatus(
        ""
    )

trPort_tx_beacon_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138011)
)
trPort_tx_beacon_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_tx_beacon_clear.setStatus(
        ""
    )

trPort_tx_halted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138012)
)
trPort_tx_halted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_tx_halted.setStatus(
        ""
    )

trPort_cmd_reject = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138013)
)
trPort_cmd_reject.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_cmd_reject.setStatus(
        ""
    )

trPort_lobe_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138014)
)
trPort_lobe_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_lobe_error.setStatus(
        ""
    )

trPort_auto_remove_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138015)
)
trPort_auto_remove_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_auto_remove_err.setStatus(
        ""
    )

trPort_remove_rcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138016)
)
trPort_remove_rcvd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_remove_rcvd.setStatus(
        ""
    )

trPort_not_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138017)
)
trPort_not_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_not_disabled.setStatus(
        ""
    )

trPort_cmd_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138018)
)
trPort_cmd_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_cmd_timeout.setStatus(
        ""
    )

trPort_fatal_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138019)
)
trPort_fatal_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_fatal_err.setStatus(
        ""
    )

trPort_single_stn_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138020)
)
trPort_single_stn_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_single_stn_err.setStatus(
        ""
    )

trPort_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138021)
)
trPort_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_up.setStatus(
        ""
    )

trPort_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138022)
)
trPort_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_down.setStatus(
        ""
    )

trPort_trans_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138023)
)
trPort_trans_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_trans_err.setStatus(
        ""
    )

trPort_unkn_trans_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138024)
)
trPort_unkn_trans_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_unkn_trans_err.setStatus(
        ""
    )

trPort_diag_check = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138025)
)
trPort_diag_check.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_diag_check.setStatus(
        ""
    )

trd_tr_diagnostic_check_cb = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 138026)
)
trd_tr_diagnostic_check_cb.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trd_tr_diagnostic_check_cb.setStatus(
        ""
    )

trPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 139000)
)
trPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_boot.setStatus(
        ""
    )

trPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 139001)
)
trPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_boot_fail.setStatus(
        ""
    )

trPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 139002)
)
trPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_enable.setStatus(
        ""
    )

trPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 139003)
)
trPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_disable.setStatus(
        ""
    )

trPort_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 139004)
)
trPort_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_init_fail.setStatus(
        ""
    )

trPort_ring_num_cfg_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 139005)
)
trPort_ring_num_cfg_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    trPort_ring_num_cfg_err.setStatus(
        ""
    )

hdwareAccel_comm_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 141000)
)
hdwareAccel_comm_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdwareAccel_comm_fail.setStatus(
        ""
    )

hdwareAccel_ha_warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 141001)
)
hdwareAccel_ha_warn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdwareAccel_ha_warn.setStatus(
        ""
    )

hdwareAccel_test = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 141002)
)
hdwareAccel_test.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hdwareAccel_test.setStatus(
        ""
    )

agent_coldstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151000)
)
agent_coldstart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_coldstart.setStatus(
        ""
    )

agent_warmstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151001)
)
agent_warmstart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_warmstart.setStatus(
        ""
    )

agent_chan_conn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151002)
)
agent_chan_conn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_chan_conn_up.setStatus(
        ""
    )

agent_chan_conn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151003)
)
agent_chan_conn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_chan_conn_down.setStatus(
        ""
    )

agent_missing_module = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151004)
)
agent_missing_module.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_missing_module.setStatus(
        ""
    )

agent_missing_aaf = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151005)
)
agent_missing_aaf.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_missing_aaf.setStatus(
        ""
    )

agent_auth_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151006)
)
agent_auth_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_auth_fail.setStatus(
        ""
    )

agent_wrong_pointer = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 151007)
)
agent_wrong_pointer.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    agent_wrong_pointer.setStatus(
        ""
    )

snmpmgr_snmp_manager_is_restarti = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 152000)
)
snmpmgr_snmp_manager_is_restarti.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpmgr_snmp_manager_is_restarti.setStatus(
        ""
    )

snmpmgr_failed_main_channel_conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 152001)
)
snmpmgr_failed_main_channel_conn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpmgr_failed_main_channel_conn.setStatus(
        ""
    )

snmpmgr_connected_to_main_channe = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 152002)
)
snmpmgr_connected_to_main_channe.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpmgr_connected_to_main_channe.setStatus(
        ""
    )

snmpmgr_lost_main_channel_connec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 152003)
)
snmpmgr_lost_main_channel_connec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpmgr_lost_main_channel_connec.setStatus(
        ""
    )

snmpmgr_connected_to_pms_channel = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 152004)
)
snmpmgr_connected_to_pms_channel.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpmgr_connected_to_pms_channel.setStatus(
        ""
    )

snmpmgr_lost_pms_channel_connect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 152005)
)
snmpmgr_lost_pms_channel_connect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpmgr_lost_pms_channel_connect.setStatus(
        ""
    )

snmpconn_snmp_connection_is_rest = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 153000)
)
snmpconn_snmp_connection_is_rest.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpconn_snmp_connection_is_rest.setStatus(
        ""
    )

snmpconn_cannot_get_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 153001)
)
snmpconn_cannot_get_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpconn_cannot_get_memory.setStatus(
        ""
    )

snmpconn_cannot_get_iorb = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 153002)
)
snmpconn_cannot_get_iorb.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpconn_cannot_get_iorb.setStatus(
        ""
    )

snmpconn_cannot_get_dbuffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 153003)
)
snmpconn_cannot_get_dbuffer.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snmpconn_cannot_get_dbuffer.setStatus(
        ""
    )

ret_high_priority_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 154000)
)
ret_high_priority_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ret_high_priority_traps.setStatus(
        ""
    )

ret_med_priority_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 154001)
)
ret_med_priority_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ret_med_priority_traps.setStatus(
        ""
    )

ret_low_priority_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 154002)
)
ret_low_priority_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ret_low_priority_traps.setStatus(
        ""
    )

lclTermi_invalid_frame = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 155000)
)
lclTermi_invalid_frame.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTermi_invalid_frame.setStatus(
        ""
    )

lclTermi_ssn_not_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 155001)
)
lclTermi_ssn_not_started.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTermi_ssn_not_started.setStatus(
        ""
    )

lclTermi_ssn_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 155002)
)
lclTermi_ssn_started.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTermi_ssn_started.setStatus(
        ""
    )

lclTermi_ssn_terminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 155003)
)
lclTermi_ssn_terminated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTermi_ssn_terminated.setStatus(
        ""
    )

lcon_config_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156000)
)
lcon_config_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_config_err.setStatus(
        ""
    )

lcon_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156001)
)
lcon_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_disabled.setStatus(
        ""
    )

lcon_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156002)
)
lcon_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_enabled.setStatus(
        ""
    )

lcon_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156003)
)
lcon_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_disable_fail.setStatus(
        ""
    )

lcon_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156004)
)
lcon_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_enable_fail.setStatus(
        ""
    )

lcon_booted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156005)
)
lcon_booted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_booted.setStatus(
        ""
    )

lcon_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156006)
)
lcon_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_boot_fail.setStatus(
        ""
    )

lcon_create_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156007)
)
lcon_create_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_create_fail.setStatus(
        ""
    )

lcon_group_config_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156008)
)
lcon_group_config_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_group_config_error.setStatus(
        ""
    )

lcon_nexthop_config_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156009)
)
lcon_nexthop_config_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_nexthop_config_err.setStatus(
        ""
    )

lcon_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156010)
)
lcon_out_of_range.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_out_of_range.setStatus(
        ""
    )

wa_protocol_priority_profile_ent = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156011)
)
wa_protocol_priority_profile_ent.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wa_protocol_priority_profile_ent.setStatus(
        ""
    )

wa_precedence_array_assignments = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 156012)
)
wa_precedence_array_assignments.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wa_precedence_array_assignments.setStatus(
        ""
    )

wsl_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 157000)
)
wsl_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wsl_Port_boot.setStatus(
        ""
    )

lcon_creation_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 157001)
)
lcon_creation_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_creation_fail.setStatus(
        ""
    )

wsl_not_monitored = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 157002)
)
wsl_not_monitored.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wsl_not_monitored.setStatus(
        ""
    )

lcon_bad_hello_thresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 159000)
)
lcon_bad_hello_thresh.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_bad_hello_thresh.setStatus(
        ""
    )

lcon_invalid_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 159001)
)
lcon_invalid_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_invalid_id.setStatus(
        ""
    )

sram_high_prior_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 162000)
)
sram_high_prior_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sram_high_prior_traps.setStatus(
        ""
    )

sram_med_prior_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 162001)
)
sram_med_prior_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sram_med_prior_traps.setStatus(
        ""
    )

sram_low_prior_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 162002)
)
sram_low_prior_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sram_low_prior_traps.setStatus(
        ""
    )

node_record_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 173000)
)
node_record_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    node_record_boot_fail.setStatus(
        ""
    )

ethPort_no_throttle_timers = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174000)
)
ethPort_no_throttle_timers.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_no_throttle_timers.setStatus(
        ""
    )

ethPort_no_initialization = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174001)
)
ethPort_no_initialization.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_no_initialization.setStatus(
        ""
    )

ethPort_config_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174002)
)
ethPort_config_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_config_fail.setStatus(
        ""
    )

ethPort_ia_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174003)
)
ethPort_ia_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_ia_fail.setStatus(
        ""
    )

ethPort_configuration_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174004)
)
ethPort_configuration_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_configuration_timeout.setStatus(
        ""
    )

ethPort_no_suspension = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174005)
)
ethPort_no_suspension.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_no_suspension.setStatus(
        ""
    )

ethPort_tx_put_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174006)
)
ethPort_tx_put_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_tx_put_fail.setStatus(
        ""
    )

ethPort_excess_tx_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174007)
)
ethPort_excess_tx_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_excess_tx_err.setStatus(
        ""
    )

ethPort_loc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174008)
)
ethPort_loc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_loc.setStatus(
        ""
    )

ethPort_excess_rx_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174009)
)
ethPort_excess_rx_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_excess_rx_err.setStatus(
        ""
    )

ethPort_excess_tx_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174010)
)
ethPort_excess_tx_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_excess_tx_clear.setStatus(
        ""
    )

ethPort_loc_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174011)
)
ethPort_loc_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_loc_clear.setStatus(
        ""
    )

ethPort_excessive_rx_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174012)
)
ethPort_excessive_rx_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_excessive_rx_clear.setStatus(
        ""
    )

ethPort_invalid_state_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174013)
)
ethPort_invalid_state_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_invalid_state_enabled.setStatus(
        ""
    )

ethPort_inval_state_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174014)
)
ethPort_inval_state_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_inval_state_disable.setStatus(
        ""
    )

ethPort_loopback_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174015)
)
ethPort_loopback_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_loopback_fail.setStatus(
        ""
    )

ethPort_tdr_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174016)
)
ethPort_tdr_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_tdr_fail.setStatus(
        ""
    )

ethPort_ca_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174017)
)
ethPort_ca_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_ca_fail.setStatus(
        ""
    )

ethPort_rx_list_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174018)
)
ethPort_rx_list_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_rx_list_err.setStatus(
        ""
    )

ethPort_tx_list_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174019)
)
ethPort_tx_list_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_tx_list_err.setStatus(
        ""
    )

ethPort_lockup_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 174020)
)
ethPort_lockup_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_lockup_err.setStatus(
        ""
    )

alcPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 176000)
)
alcPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alcPort_boot.setStatus(
        ""
    )

alcPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 176001)
)
alcPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alcPort_boot_fail.setStatus(
        ""
    )

alcPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 176002)
)
alcPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alcPort_disable.setStatus(
        ""
    )

alcPort_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 176003)
)
alcPort_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alcPort_disable_fail.setStatus(
        ""
    )

alcPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 176004)
)
alcPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alcPort_enable.setStatus(
        ""
    )

alcPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 176005)
)
alcPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alcPort_enable_fail.setStatus(
        ""
    )

alcPort_nomodule = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 176006)
)
alcPort_nomodule.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alcPort_nomodule.setStatus(
        ""
    )

alch_al_line_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177000)
)
alch_al_line_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_line_down.setStatus(
        ""
    )

alch_al_line_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177001)
)
alch_al_line_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_line_up.setStatus(
        ""
    )

alch_al_flow_ctl_imp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177002)
)
alch_al_flow_ctl_imp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_flow_ctl_imp.setStatus(
        ""
    )

alch_al_flow_ctl_rel = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177003)
)
alch_al_flow_ctl_rel.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_flow_ctl_rel.setStatus(
        ""
    )

alch_al_ia_fast_poll = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177004)
)
alch_al_ia_fast_poll.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_ia_fast_poll.setStatus(
        ""
    )

alch_al_ia_slow_poll = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177005)
)
alch_al_ia_slow_poll.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_ia_slow_poll.setStatus(
        ""
    )

alch_al_ia_stop_poll = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177006)
)
alch_al_ia_stop_poll.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_ia_stop_poll.setStatus(
        ""
    )

alch_al_reset_disc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177007)
)
alch_al_reset_disc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_reset_disc.setStatus(
        ""
    )

alch_al_T1_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177008)
)
alch_al_T1_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_T1_timeout.setStatus(
        ""
    )

alch_al_T2_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177009)
)
alch_al_T2_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_T2_timeout.setStatus(
        ""
    )

alch_al_bad_ccc_rec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177010)
)
alch_al_bad_ccc_rec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_bad_ccc_rec.setStatus(
        ""
    )

alch_al_host_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177011)
)
alch_al_host_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_host_timeout.setStatus(
        ""
    )

alch_al_host_start_poll = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177012)
)
alch_al_host_start_poll.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_host_start_poll.setStatus(
        ""
    )

alch_al_msg_dis_no_conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 177013)
)
alch_al_msg_dis_no_conn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alch_al_msg_dis_no_conn.setStatus(
        ""
    )

alp_al_buff_disc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 178000)
)
alp_al_buff_disc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alp_al_buff_disc.setStatus(
        ""
    )

apl_al_call_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 178001)
)
apl_al_call_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    apl_al_call_fail.setStatus(
        ""
    )

alp_al_lost_msgs = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 178002)
)
alp_al_lost_msgs.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alp_al_lost_msgs.setStatus(
        ""
    )

alp_al_SIP_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 178003)
)
alp_al_SIP_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alp_al_SIP_error.setStatus(
        ""
    )

alp_al_SIP_nexist = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 178004)
)
alp_al_SIP_nexist.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alp_al_SIP_nexist.setStatus(
        ""
    )

alp_al_src_IP_rqd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 178005)
)
alp_al_src_IP_rqd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    alp_al_src_IP_rqd.setStatus(
        ""
    )

fraPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186000)
)
fraPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_boot.setStatus(
        ""
    )

fraPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186001)
)
fraPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_boot_fail.setStatus(
        ""
    )

fraPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186002)
)
fraPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_disable.setStatus(
        ""
    )

fraPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186003)
)
fraPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_enable.setStatus(
        ""
    )

fraPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186004)
)
fraPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_util_exceeded.setStatus(
        ""
    )

fraPort_stn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186005)
)
fraPort_stn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_stn_disable.setStatus(
        ""
    )

fraPort_stn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186006)
)
fraPort_stn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_stn_enable.setStatus(
        ""
    )

fraPort_stn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186007)
)
fraPort_stn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_stn_boot.setStatus(
        ""
    )

fraPort_stn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186008)
)
fraPort_stn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_stn_boot_fail.setStatus(
        ""
    )

fraPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186009)
)
fraPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraPort_warn_status.setStatus(
        ""
    )

fra_port_update_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186010)
)
fra_port_update_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fra_port_update_complete.setStatus(
        ""
    )

fra_out_of_memory_some_stations = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 186011)
)
fra_out_of_memory_some_stations.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fra_out_of_memory_some_stations.setStatus(
        ""
    )

fraL2_unconfig_dlci = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187000)
)
fraL2_unconfig_dlci.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_unconfig_dlci.setStatus(
        ""
    )

fraL2_dsbl_stn_pack = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187001)
)
fraL2_dsbl_stn_pack.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_dsbl_stn_pack.setStatus(
        ""
    )

fraL2_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187002)
)
fraL2_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_bad_frame_len.setStatus(
        ""
    )

fraL2_annexd_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187003)
)
fraL2_annexd_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_annexd_err.setStatus(
        ""
    )

fraL2_lmi_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187004)
)
fraL2_lmi_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_lmi_err.setStatus(
        ""
    )

fraL2_fsm_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187005)
)
fraL2_fsm_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_fsm_err.setStatus(
        ""
    )

fraL2_invalid_addr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187006)
)
fraL2_invalid_addr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_invalid_addr.setStatus(
        ""
    )

fraL2_net_congested = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187007)
)
fraL2_net_congested.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_net_congested.setStatus(
        ""
    )

fraL2_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187008)
)
fraL2_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_link_up.setStatus(
        ""
    )

fraL2_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187009)
)
fraL2_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_link_down.setStatus(
        ""
    )

fraL2_annexa_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187010)
)
fraL2_annexa_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fraL2_annexa_err.setStatus(
        ""
    )

fra_station_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187011)
)
fra_station_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fra_station_up.setStatus(
        ""
    )

fra_station_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 187012)
)
fra_station_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    fra_station_down.setStatus(
        ""
    )

lcon_invalid_proto_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 188000)
)
lcon_invalid_proto_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_invalid_proto_id.setStatus(
        ""
    )

lcon_invalid_forward_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 188001)
)
lcon_invalid_forward_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_invalid_forward_id.setStatus(
        ""
    )

lcon_rx_no_route_discard = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 188002)
)
lcon_rx_no_route_discard.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_rx_no_route_discard.setStatus(
        ""
    )

lcon_rx_no_hop_discard = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 188003)
)
lcon_rx_no_hop_discard.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_rx_no_hop_discard.setStatus(
        ""
    )

lcon_tx_bad_hop_discard = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 188004)
)
lcon_tx_bad_hop_discard.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_tx_bad_hop_discard.setStatus(
        ""
    )

lcon_svc_creation_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 189000)
)
lcon_svc_creation_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_svc_creation_fail.setStatus(
        ""
    )

lcon_1294_invalid_encap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 191000)
)
lcon_1294_invalid_encap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_1294_invalid_encap.setStatus(
        ""
    )

tb_forwarding_table_full = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 192000)
)
tb_forwarding_table_full.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tb_forwarding_table_full.setStatus(
        ""
    )

ethPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 193000)
)
ethPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_boot.setStatus(
        ""
    )

ethPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 193001)
)
ethPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_boot_fail.setStatus(
        ""
    )

ethPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 193002)
)
ethPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_enable.setStatus(
        ""
    )

ethPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 193003)
)
ethPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_disable.setStatus(
        ""
    )

ethPort_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 193004)
)
ethPort_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethPort_init_fail.setStatus(
        ""
    )

shdlc_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195000)
)
shdlc_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_link_down.setStatus(
        ""
    )

shdlc_disc_recv = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195001)
)
shdlc_disc_recv.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_disc_recv.setStatus(
        ""
    )

shdlc_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195002)
)
shdlc_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_bad_frame_type.setStatus(
        ""
    )

shdlc_address_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195003)
)
shdlc_address_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_address_err.setStatus(
        ""
    )

shdlc_bad_frame_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195004)
)
shdlc_bad_frame_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_bad_frame_len.setStatus(
        ""
    )

shdlc_extend_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195005)
)
shdlc_extend_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_extend_seq_frmr.setStatus(
        ""
    )

shdlc_norm_seq_frmr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195006)
)
shdlc_norm_seq_frmr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_norm_seq_frmr.setStatus(
        ""
    )

shdlc_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195007)
)
shdlc_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_link_up.setStatus(
        ""
    )

shdlc_link_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195008)
)
shdlc_link_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_link_blocked.setStatus(
        ""
    )

shdlc_bad_n_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195009)
)
shdlc_bad_n_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_bad_n_r.setStatus(
        ""
    )

shdlc_backup_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195010)
)
shdlc_backup_activated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_backup_activated.setStatus(
        ""
    )

shdlc_extend_bad_frame_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195011)
)
shdlc_extend_bad_frame_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_extend_bad_frame_type.setStatus(
        ""
    )

shdlc_access_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195012)
)
shdlc_access_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_access_link_down.setStatus(
        ""
    )

shdlc_access_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195013)
)
shdlc_access_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_access_link_up.setStatus(
        ""
    )

shdlc_ovsize_frame = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 195014)
)
shdlc_ovsize_frame.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_ovsize_frame.setStatus(
        ""
    )

shdlc_port_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 196000)
)
shdlc_port_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_port_boot_complete.setStatus(
        ""
    )

shdlc_port_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 196001)
)
shdlc_port_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_port_boot_failure.setStatus(
        ""
    )

shdlc_port_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 196002)
)
shdlc_port_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_port_disabled.setStatus(
        ""
    )

shdlc_port_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 196003)
)
shdlc_port_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_port_enabled.setStatus(
        ""
    )

shdlc_port_utilization_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 196004)
)
shdlc_port_utilization_threshold.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_port_utilization_threshold.setStatus(
        ""
    )

shdlc_port_status_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 196005)
)
shdlc_port_status_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_port_status_warning.setStatus(
        ""
    )

shdlc_unsupported_frame_size_ope = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 196006)
)
shdlc_unsupported_frame_size_ope.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    shdlc_unsupported_frame_size_ope.setStatus(
        ""
    )

tftp_op_success = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198000)
)
tftp_op_success.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_op_success.setStatus(
        ""
    )

tftp_cmem_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198001)
)
tftp_cmem_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_cmem_fail.setStatus(
        ""
    )

tftp_local_transfer_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198002)
)
tftp_local_transfer_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_local_transfer_fail.setStatus(
        ""
    )

tftp_remote_transfer_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198003)
)
tftp_remote_transfer_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_remote_transfer_fail.setStatus(
        ""
    )

tftp_system_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198004)
)
tftp_system_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_system_fail.setStatus(
        ""
    )

tftp_udp_reg_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198005)
)
tftp_udp_reg_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_udp_reg_fail.setStatus(
        ""
    )

tftp_dl_in_progress = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198006)
)
tftp_dl_in_progress.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_dl_in_progress.setStatus(
        ""
    )

tftp_sw_image_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198007)
)
tftp_sw_image_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_sw_image_err.setStatus(
        ""
    )

tftp_flash_erase_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198008)
)
tftp_flash_erase_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_flash_erase_fail.setStatus(
        ""
    )

tftp_flash_write_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198009)
)
tftp_flash_write_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_flash_write_fail.setStatus(
        ""
    )

tftp_tftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198010)
)
tftp_tftp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_tftp.setStatus(
        ""
    )

tftp_partial_success = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198011)
)
tftp_partial_success.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_partial_success.setStatus(
        ""
    )

tftp_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 198012)
)
tftp_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tftp_failure.setStatus(
        ""
    )

ipx_multiple_paths = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 202000)
)
ipx_multiple_paths.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipx_multiple_paths.setStatus(
        ""
    )

ipx_net_unreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 202001)
)
ipx_net_unreachable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipx_net_unreachable.setStatus(
        ""
    )

router_ipx_disabled_memory_alloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 202002)
)
router_ipx_disabled_memory_alloc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_ipx_disabled_memory_alloc.setStatus(
        ""
    )

router_no_memory_for_table = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 202006)
)
router_no_memory_for_table.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_no_memory_for_table.setStatus(
        ""
    )

router_no_memory_for_record = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 202007)
)
router_no_memory_for_record.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_no_memory_for_record.setStatus(
        ""
    )

router_record_attempt_to_add_dup = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 202008)
)
router_record_attempt_to_add_dup.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_record_attempt_to_add_dup.setStatus(
        ""
    )

dscope_user_message_lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 206000)
)
dscope_user_message_lost.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dscope_user_message_lost.setStatus(
        ""
    )

dscope_subaddress_incorrect_leng = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 206001)
)
dscope_subaddress_incorrect_leng.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dscope_subaddress_incorrect_leng.setStatus(
        ""
    )

ipx_high_priority_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 210000)
)
ipx_high_priority_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipx_high_priority_traps.setStatus(
        ""
    )

ipx_med_priority_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 210001)
)
ipx_med_priority_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipx_med_priority_traps.setStatus(
        ""
    )

ipx_low_priority_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 210002)
)
ipx_low_priority_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipx_low_priority_traps.setStatus(
        ""
    )

ipx_max_interf_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 210003)
)
ipx_max_interf_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipx_max_interf_exceeded.setStatus(
        ""
    )

router_record_attempt_to_add_dup2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 210004)
)
router_record_attempt_to_add_dup2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_record_attempt_to_add_dup2.setStatus(
        ""
    )

code_bytes_loaded_from_extended = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 211000)
)
code_bytes_loaded_from_extended.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_bytes_loaded_from_extended.setStatus(
        ""
    )

cougar_code_loaded_from_extended = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 211001)
)
cougar_code_loaded_from_extended.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cougar_code_loaded_from_extended.setStatus(
        ""
    )

code_extended_software_load_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 211002)
)
code_extended_software_load_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_extended_software_load_fail.setStatus(
        ""
    )

code_master_failed_to_copy_exten = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 211003)
)
code_master_failed_to_copy_exten.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_master_failed_to_copy_exten.setStatus(
        ""
    )

code_extended_checksum_error_slo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 211004)
)
code_extended_checksum_error_slo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    code_extended_checksum_error_slo.setStatus(
        ""
    )

asyncModem_speed_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 212000)
)
asyncModem_speed_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    asyncModem_speed_unsupp.setStatus(
        ""
    )

asyncModem_databits_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 212001)
)
asyncModem_databits_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    asyncModem_databits_unsupp.setStatus(
        ""
    )

asyncModem_connection = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 212002)
)
asyncModem_connection.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    asyncModem_connection.setStatus(
        ""
    )

t3pos_fat_timer_expired_line_dis = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215000)
)
t3pos_fat_timer_expired_line_dis.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_fat_timer_expired_line_dis.setStatus(
        ""
    )

t3pos_connection_towards_host_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215001)
)
t3pos_connection_towards_host_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_connection_towards_host_in.setStatus(
        ""
    )

t3pos_dleeot_received_call_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215002)
)
t3pos_dleeot_received_call_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_dleeot_received_call_clear.setStatus(
        ""
    )

t3pos_invalid_frame_from_pos_cal = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215003)
)
t3pos_invalid_frame_from_pos_cal.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_invalid_frame_from_pos_cal.setStatus(
        ""
    )

t3pos_dle_eot_timeout_call_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215004)
)
t3pos_dle_eot_timeout_call_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_dle_eot_timeout_call_clear.setStatus(
        ""
    )

t3pos_line_failure_line_disconne = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215005)
)
t3pos_line_failure_line_disconne.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_line_failure_line_disconne.setStatus(
        ""
    )

t3pos_output_queue_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215006)
)
t3pos_output_queue_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_output_queue_overrun.setStatus(
        ""
    )

t3pos_input_queue_overrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215007)
)
t3pos_input_queue_overrun.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_input_queue_overrun.setStatus(
        ""
    )

t3pos_call_cleared_by_host = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215008)
)
t3pos_call_cleared_by_host.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_call_cleared_by_host.setStatus(
        ""
    )

t3pos_call_rejected_by_level3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215009)
)
t3pos_call_rejected_by_level3.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_call_rejected_by_level3.setStatus(
        ""
    )

t3pos_invalid_mss_from_pos_call = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215010)
)
t3pos_invalid_mss_from_pos_call.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_invalid_mss_from_pos_call.setStatus(
        ""
    )

t3pos_invalid_mss_from_host_call = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215011)
)
t3pos_invalid_mss_from_host_call.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_invalid_mss_from_host_call.setStatus(
        ""
    )

t3pos_dial_out_not_supported_cal = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215012)
)
t3pos_dial_out_not_supported_cal.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_dial_out_not_supported_cal.setStatus(
        ""
    )

t3pos_host_frame_size_exceeded_c = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215013)
)
t3pos_host_frame_size_exceeded_c.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_host_frame_size_exceeded_c.setStatus(
        ""
    )

t3pos_control_frame_from_host_ca = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215014)
)
t3pos_control_frame_from_host_ca.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_control_frame_from_host_ca.setStatus(
        ""
    )

t3pos_retry_exceeded_line_discon = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215015)
)
t3pos_retry_exceeded_line_discon.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_retry_exceeded_line_discon.setStatus(
        ""
    )

t3pos_retry_exceeded_call_cleare = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215016)
)
t3pos_retry_exceeded_call_cleare.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_retry_exceeded_call_cleare.setStatus(
        ""
    )

t3pos_virtual_retry_exceeded_cal = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215017)
)
t3pos_virtual_retry_exceeded_cal.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_virtual_retry_exceeded_cal.setStatus(
        ""
    )

t3pos_virtual_call_retry_exceede = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215018)
)
t3pos_virtual_call_retry_exceede.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_virtual_call_retry_exceede.setStatus(
        ""
    )

t3pos_invitation_to_clear_from_h = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215019)
)
t3pos_invitation_to_clear_from_h.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_invitation_to_clear_from_h.setStatus(
        ""
    )

t3pos_invalid_control_field_call = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215020)
)
t3pos_invalid_control_field_call.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_invalid_control_field_call.setStatus(
        ""
    )

t3pos_port_stat_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215021)
)
t3pos_port_stat_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_stat_overflow.setStatus(
        ""
    )

t3pos_connected_to_host = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215022)
)
t3pos_connected_to_host.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_connected_to_host.setStatus(
        ""
    )

t3pos_control_field_empty_call_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 215023)
)
t3pos_control_field_empty_call_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_control_field_empty_call_r.setStatus(
        ""
    )

t3pos_port_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216000)
)
t3pos_port_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_boot_complete.setStatus(
        ""
    )

t3pos_portbootfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216001)
)
t3pos_portbootfailure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_portbootfailure.setStatus(
        ""
    )

t3pos_port_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216002)
)
t3pos_port_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_disabled.setStatus(
        ""
    )

t3pos_port_disable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216003)
)
t3pos_port_disable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_disable_failure.setStatus(
        ""
    )

t3pos_port_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216004)
)
t3pos_port_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_enabled.setStatus(
        ""
    )

t3pos_port_enable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216005)
)
t3pos_port_enable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_enable_failure.setStatus(
        ""
    )

t3pos_port_connection_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216006)
)
t3pos_port_connection_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_connection_cleared.setStatus(
        ""
    )

t3pos_port_utilization_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 216007)
)
t3pos_port_utilization_threshold.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t3pos_port_utilization_threshold.setStatus(
        ""
    )

atpad_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 218000)
)
atpad_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpad_data_loss.setStatus(
        ""
    )

atpad_data_loss_cmd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 218001)
)
atpad_data_loss_cmd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpad_data_loss_cmd.setStatus(
        ""
    )

atpadPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 219000)
)
atpadPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpadPort_boot.setStatus(
        ""
    )

atpadPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 219001)
)
atpadPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpadPort_boot_fail.setStatus(
        ""
    )

atpadPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 219002)
)
atpadPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpadPort_disable.setStatus(
        ""
    )

atpadPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 219003)
)
atpadPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpadPort_enable.setStatus(
        ""
    )

atpadPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 219004)
)
atpadPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpadPort_util_exceeded.setStatus(
        ""
    )

atpadPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 219005)
)
atpadPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpadPort_warn_status.setStatus(
        ""
    )

atpadPort_errcnt_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 219006)
)
atpadPort_errcnt_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    atpadPort_errcnt_exceeded.setStatus(
        ""
    )

lclTerm_stn_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 222000)
)
lclTerm_stn_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTerm_stn_up.setStatus(
        ""
    )

lclTerm_stn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 222001)
)
lclTerm_stn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTerm_stn_down.setStatus(
        ""
    )

lclTerm_stn_timed_out = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 222002)
)
lclTerm_stn_timed_out.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTerm_stn_timed_out.setStatus(
        ""
    )

lclTerm_remote_disconn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 222003)
)
lclTerm_remote_disconn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTerm_remote_disconn.setStatus(
        ""
    )

lclTerm_remote_conn_estab = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 222004)
)
lclTerm_remote_conn_estab.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTerm_remote_conn_estab.setStatus(
        ""
    )

lclTerm_remote_call_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 222005)
)
lclTerm_remote_call_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lclTerm_remote_call_up.setStatus(
        ""
    )

ethltm_station_frame_type_does_n = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 224000)
)
ethltm_station_frame_type_does_n.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethltm_station_frame_type_does_n.setStatus(
        ""
    )

ethltm_remote_call_established = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 224001)
)
ethltm_remote_call_established.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ethltm_remote_call_established.setStatus(
        ""
    )

frltm_fri_dlci_disconn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 225001)
)
frltm_fri_dlci_disconn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    frltm_fri_dlci_disconn.setStatus(
        ""
    )

lctTerm_stn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226000)
)
lctTerm_stn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lctTerm_stn_boot.setStatus(
        ""
    )

lctTerm_stn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226001)
)
lctTerm_stn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lctTerm_stn_boot_fail.setStatus(
        ""
    )

lctTerm_stn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226002)
)
lctTerm_stn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lctTerm_stn_disable.setStatus(
        ""
    )

lctTerm_stn_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226003)
)
lctTerm_stn_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lctTerm_stn_disable_fail.setStatus(
        ""
    )

lctTerm_stn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226004)
)
lctTerm_stn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lctTerm_stn_enable.setStatus(
        ""
    )

lctTerm_stn_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226005)
)
lctTerm_stn_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lctTerm_stn_enable_fail.setStatus(
        ""
    )

lctTerm_port_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226006)
)
lctTerm_port_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lctTerm_port_warn_status.setStatus(
        ""
    )

slaccm_insufficient_memory_to_pr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226007)
)
slaccm_insufficient_memory_to_pr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm_insufficient_memory_to_pr.setStatus(
        ""
    )

slaccm_insufficient_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226008)
)
slaccm_insufficient_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm_insufficient_memory.setStatus(
        ""
    )

slaccm226009_dynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226009)
)
slaccm226009_dynamic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226009_dynamic.setStatus(
        ""
    )

slaccm226010_dynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226010)
)
slaccm226010_dynamic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226010_dynamic.setStatus(
        ""
    )

slaccm226011_dynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226011)
)
slaccm226011_dynamic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226011_dynamic.setStatus(
        ""
    )

slaccm226012_dynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226012)
)
slaccm226012_dynamic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226012_dynamic.setStatus(
        ""
    )

slaccm226013_dynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226013)
)
slaccm226013_dynamic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226013_dynamic.setStatus(
        ""
    )

slaccm226014_dynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226014)
)
slaccm226014_dynamic.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226014_dynamic.setStatus(
        ""
    )

slaccm226015_insuffi = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226015)
)
slaccm226015_insuffi.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226015_insuffi.setStatus(
        ""
    )

slaccm226016_no_stat = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226016)
)
slaccm226016_no_stat.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226016_no_stat.setStatus(
        ""
    )

slaccm226017_all_sta = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226017)
)
slaccm226017_all_sta.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226017_all_sta.setStatus(
        ""
    )

slaccm226018_will_re = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226018)
)
slaccm226018_will_re.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226018_will_re.setStatus(
        ""
    )

slaccm226019_err_sla = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 226019)
)
slaccm226019_err_sla.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slaccm226019_err_sla.setStatus(
        ""
    )

tnpplp_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227000)
)
tnpplp_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_link_down.setStatus(
        ""
    )

tnpplp_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227001)
)
tnpplp_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_link_up.setStatus(
        ""
    )

tnpplp_protocol_errors = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227002)
)
tnpplp_protocol_errors.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_protocol_errors.setStatus(
        ""
    )

tnpplp_frame_discarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227003)
)
tnpplp_frame_discarded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_frame_discarded.setStatus(
        ""
    )

tnpplp_rempad_connprogress = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227004)
)
tnpplp_rempad_connprogress.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_rempad_connprogress.setStatus(
        ""
    )

tnpplp_autocalltry_exhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227005)
)
tnpplp_autocalltry_exhaust.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_autocalltry_exhaust.setStatus(
        ""
    )

tnpplp_remdevice_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227006)
)
tnpplp_remdevice_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_remdevice_down.setStatus(
        ""
    )

tnpplp_rempad_callclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227007)
)
tnpplp_rempad_callclear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_rempad_callclear.setStatus(
        ""
    )

tnpplp_level3_callreject = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227008)
)
tnpplp_level3_callreject.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_level3_callreject.setStatus(
        ""
    )

tnpplp_mnemonic_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227009)
)
tnpplp_mnemonic_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_mnemonic_error.setStatus(
        ""
    )

tnpplp_remdevice_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227010)
)
tnpplp_remdevice_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_remdevice_up.setStatus(
        ""
    )

tnpplp_x25call_reject = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227011)
)
tnpplp_x25call_reject.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_x25call_reject.setStatus(
        ""
    )

tnpplp_network_callclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227012)
)
tnpplp_network_callclear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_network_callclear.setStatus(
        ""
    )

tnpplp_rempad_mismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227013)
)
tnpplp_rempad_mismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_rempad_mismatch.setStatus(
        ""
    )

tnpplp_x25_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 227014)
)
tnpplp_x25_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnpplp_x25_up.setStatus(
        ""
    )

tnppPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228000)
)
tnppPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_boot.setStatus(
        ""
    )

tnppPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228001)
)
tnppPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_boot_fail.setStatus(
        ""
    )

tnppPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228002)
)
tnppPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_disable.setStatus(
        ""
    )

tnppPort_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228003)
)
tnppPort_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_disable_fail.setStatus(
        ""
    )

tnppPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228004)
)
tnppPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_enable.setStatus(
        ""
    )

tnppPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228005)
)
tnppPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_enable_fail.setStatus(
        ""
    )

tnppPort_connection_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228006)
)
tnppPort_connection_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_connection_cleared.setStatus(
        ""
    )

tnppPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228007)
)
tnppPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_util_exceeded.setStatus(
        ""
    )

tnppPort_status_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 228008)
)
tnppPort_status_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnppPort_status_warning.setStatus(
        ""
    )

netSvcs_param_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 229000)
)
netSvcs_param_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    netSvcs_param_err.setStatus(
        ""
    )

netSvcs_no_features = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 229001)
)
netSvcs_no_features.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    netSvcs_no_features.setStatus(
        ""
    )

netSvcs_data_struct_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 229002)
)
netSvcs_data_struct_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    netSvcs_data_struct_err.setStatus(
        ""
    )

netSvcs_unav_chans = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 229003)
)
netSvcs_unav_chans.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    netSvcs_unav_chans.setStatus(
        ""
    )

netSvcs_rereg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 229004)
)
netSvcs_rereg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    netSvcs_rereg.setStatus(
        ""
    )

netSvcs_invalid_config = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 229005)
)
netSvcs_invalid_config.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    netSvcs_invalid_config.setStatus(
        ""
    )

bod_I_lead_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230000)
)
bod_I_lead_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_I_lead_up.setStatus(
        ""
    )

bod_I_lead_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230001)
)
bod_I_lead_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_I_lead_down.setStatus(
        ""
    )

bod_I_leased_line_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230002)
)
bod_I_leased_line_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_I_leased_line_down.setStatus(
        ""
    )

bod_I_leased_line_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230003)
)
bod_I_leased_line_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_I_leased_line_up.setStatus(
        ""
    )

bod_tow_switch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230004)
)
bod_tow_switch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_tow_switch.setStatus(
        ""
    )

bod_tow_disabling = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230005)
)
bod_tow_disabling.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_tow_disabling.setStatus(
        ""
    )

bod_tow_enabling = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230006)
)
bod_tow_enabling.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_tow_enabling.setStatus(
        ""
    )

bod_isdn_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230007)
)
bod_isdn_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_isdn_down.setStatus(
        ""
    )

bod_user_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230008)
)
bod_user_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_user_disable.setStatus(
        ""
    )

bod_Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230009)
)
bod_Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_Port_disable.setStatus(
        ""
    )

bod_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 230010)
)
bod_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bod_Port_boot.setStatus(
        ""
    )

slipPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 231000)
)
slipPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipPort_boot.setStatus(
        ""
    )

slipPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 231001)
)
slipPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipPort_boot_fail.setStatus(
        ""
    )

slipPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 231002)
)
slipPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipPort_disable.setStatus(
        ""
    )

slipPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 231003)
)
slipPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipPort_enable.setStatus(
        ""
    )

slipPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 231004)
)
slipPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipPort_util_exceeded.setStatus(
        ""
    )

slipPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 231005)
)
slipPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipPort_warn_status.setStatus(
        ""
    )

slipPort_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 231006)
)
slipPort_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipPort_err_count_exceeded.setStatus(
        ""
    )

slipProto_inb_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 232000)
)
slipProto_inb_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipProto_inb_data_loss.setStatus(
        ""
    )

slipProto_outb_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 233000)
)
slipProto_outb_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipProto_outb_data_loss.setStatus(
        ""
    )

slipProto_invalid_encaps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 233001)
)
slipProto_invalid_encaps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    slipProto_invalid_encaps.setStatus(
        ""
    )

lcon_877_unsup_proto_rcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 234000)
)
lcon_877_unsup_proto_rcvd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lcon_877_unsup_proto_rcvd.setStatus(
        ""
    )

appleTalk_bad_param = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236000)
)
appleTalk_bad_param.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_bad_param.setStatus(
        ""
    )

appleTalk_no_mem = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236001)
)
appleTalk_no_mem.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_no_mem.setStatus(
        ""
    )

appleTalk_low_prior_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236002)
)
appleTalk_low_prior_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_low_prior_traps.setStatus(
        ""
    )

appleTalk_med_prior_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236003)
)
appleTalk_med_prior_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_med_prior_traps.setStatus(
        ""
    )

appleTalk_high_prior_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236004)
)
appleTalk_high_prior_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_high_prior_traps.setStatus(
        ""
    )

appleTalk_verbose = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236005)
)
appleTalk_verbose.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_verbose.setStatus(
        ""
    )

appleTalk_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236006)
)
appleTalk_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_warning.setStatus(
        ""
    )

appleTalk_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236007)
)
appleTalk_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_err.setStatus(
        ""
    )

appleTalk_fatal_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236008)
)
appleTalk_fatal_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_fatal_err.setStatus(
        ""
    )

appleTalk_unknown_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236009)
)
appleTalk_unknown_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_unknown_err.setStatus(
        ""
    )

appleTalk_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 236010)
)
appleTalk_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appleTalk_failure.setStatus(
        ""
    )

sip_restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 237000)
)
sip_restart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_restart.setStatus(
        ""
    )

sip_lan_restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 238000)
)
sip_lan_restart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_lan_restart.setStatus(
        ""
    )

sip_lan_connect_client = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 238001)
)
sip_lan_connect_client.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_lan_connect_client.setStatus(
        ""
    )

sip_lan_disconnect_client = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 238002)
)
sip_lan_disconnect_client.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_lan_disconnect_client.setStatus(
        ""
    )

sip_wan_restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239000)
)
sip_wan_restart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_restart.setStatus(
        ""
    )

sip_wan_lan_disconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239001)
)
sip_wan_lan_disconnect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_lan_disconnect.setStatus(
        ""
    )

sip_wan_lan_restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239002)
)
sip_wan_lan_restart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_lan_restart.setStatus(
        ""
    )

sip_wan_lan_connect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239003)
)
sip_wan_lan_connect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_lan_connect.setStatus(
        ""
    )

sip_wan_lan_disc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239004)
)
sip_wan_lan_disc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_lan_disc.setStatus(
        ""
    )

sip_wan_wan_connect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239005)
)
sip_wan_wan_connect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_wan_connect.setStatus(
        ""
    )

sip_wan_wan_disconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239006)
)
sip_wan_wan_disconnect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_wan_disconnect.setStatus(
        ""
    )

sip_wan_wan_interrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 239007)
)
sip_wan_wan_interrupted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sip_wan_wan_interrupted.setStatus(
        ""
    )

bop_bri_no_report = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241000)
)
bop_bri_no_report.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop_bri_no_report.setStatus(
        ""
    )

briPort_call_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241001)
)
briPort_call_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_call_up.setStatus(
        ""
    )

briPort_call_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241002)
)
briPort_call_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_call_down.setStatus(
        ""
    )

briPort_tx_setup_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241003)
)
briPort_tx_setup_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_tx_setup_fail.setStatus(
        ""
    )

briPort_rx_setup_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241004)
)
briPort_rx_setup_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_rx_setup_fail.setStatus(
        ""
    )

briPort_disconn_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241005)
)
briPort_disconn_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_disconn_fail.setStatus(
        ""
    )

briPort_tx_call_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241006)
)
briPort_tx_call_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_tx_call_fail.setStatus(
        ""
    )

briPort_rx_call_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241007)
)
briPort_rx_call_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_rx_call_fail.setStatus(
        ""
    )

briPort_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241008)
)
briPort_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_init_fail.setStatus(
        ""
    )

briPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241009)
)
briPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_boot_fail.setStatus(
        ""
    )

briPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241010)
)
briPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_boot.setStatus(
        ""
    )

briPort_buff_congested = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241011)
)
briPort_buff_congested.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_buff_congested.setStatus(
        ""
    )

briPort_dchan_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241012)
)
briPort_dchan_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_dchan_err.setStatus(
        ""
    )

briPort_card_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241013)
)
briPort_card_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_card_fail.setStatus(
        ""
    )

briPort_dchan_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241014)
)
briPort_dchan_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_dchan_link_down.setStatus(
        ""
    )

bopbri_bri_internal_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241015)
)
bopbri_bri_internal_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bopbri_bri_internal_error.setStatus(
        ""
    )

bopbri241062_channel = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 241062)
)
bopbri241062_channel.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bopbri241062_channel.setStatus(
        ""
    )

swServ_link_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242000)
)
swServ_link_activated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_link_activated.setStatus(
        ""
    )

swServ_link_deactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242001)
)
swServ_link_deactivated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_link_deactivated.setStatus(
        ""
    )

swServ_invalid_entry = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242002)
)
swServ_invalid_entry.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_invalid_entry.setStatus(
        ""
    )

swServ_serving_multi_ports = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242003)
)
swServ_serving_multi_ports.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_serving_multi_ports.setStatus(
        ""
    )

swServ_param_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242004)
)
swServ_param_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_param_error.setStatus(
        ""
    )

swServ_already_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242005)
)
swServ_already_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_already_active.setStatus(
        ""
    )

swServ_num_entries_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242006)
)
swServ_num_entries_changed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_num_entries_changed.setStatus(
        ""
    )

swServ_dest_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242007)
)
swServ_dest_changed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_dest_changed.setStatus(
        ""
    )

swServ_monitored_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242008)
)
swServ_monitored_changed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_monitored_changed.setStatus(
        ""
    )

swServ_backup_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242009)
)
swServ_backup_changed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    swServ_backup_changed.setStatus(
        ""
    )

ss_number_of_max_entries_in_node = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242010)
)
ss_number_of_max_entries_in_node.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss_number_of_max_entries_in_node.setStatus(
        ""
    )

ss242011_process_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242011)
)
ss242011_process_msg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242011_process_msg.setStatus(
        ""
    )

ss242012_ss_dynamic_rte = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242012)
)
ss242012_ss_dynamic_rte.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242012_ss_dynamic_rte.setStatus(
        ""
    )

ss242013_select_dest = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242013)
)
ss242013_select_dest.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242013_select_dest.setStatus(
        ""
    )

ss242014_select_cond = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242014)
)
ss242014_select_cond.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242014_select_cond.setStatus(
        ""
    )

ss242015_process_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242015)
)
ss242015_process_msg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242015_process_msg.setStatus(
        ""
    )

ss242016_cmem_compre = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242016)
)
ss242016_cmem_compre.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242016_cmem_compre.setStatus(
        ""
    )

ss242017_cmem_decomp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242017)
)
ss242017_cmem_decomp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242017_cmem_decomp.setStatus(
        ""
    )

ss242018_ss_max_retries = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242018)
)
ss242018_ss_max_retries.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242018_ss_max_retries.setStatus(
        ""
    )

ss242019_max_callid = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242019)
)
ss242019_max_callid.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242019_max_callid.setStatus(
        ""
    )

ss242020_possible_ra = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 242020)
)
ss242020_possible_ra.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ss242020_possible_ra.setStatus(
        ""
    )

hubPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 243000)
)
hubPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hubPort_boot.setStatus(
        ""
    )

hubPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 243001)
)
hubPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hubPort_boot_fail.setStatus(
        ""
    )

hubPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 243002)
)
hubPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hubPort_disable.setStatus(
        ""
    )

hubPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 243003)
)
hubPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hubPort_enable.setStatus(
        ""
    )

hubPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 243004)
)
hubPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    hubPort_warn_status.setStatus(
        ""
    )

briPort_chan_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245000)
)
briPort_chan_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_chan_boot.setStatus(
        ""
    )

briPort_chan_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245001)
)
briPort_chan_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_chan_boot_fail.setStatus(
        ""
    )

bri_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245002)
)
bri_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bri_Port_boot.setStatus(
        ""
    )

briPort_invalid_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245003)
)
briPort_invalid_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_invalid_boot.setStatus(
        ""
    )

briPort_chan_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245004)
)
briPort_chan_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_chan_disable.setStatus(
        ""
    )

briPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245005)
)
briPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_disable.setStatus(
        ""
    )

briPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245006)
)
briPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_warn_status.setStatus(
        ""
    )

briPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245007)
)
briPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_util_exceeded.setStatus(
        ""
    )

briPort_chan_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245008)
)
briPort_chan_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_chan_warn_status.setStatus(
        ""
    )

briPort_chan_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245009)
)
briPort_chan_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_chan_enable.setStatus(
        ""
    )

briPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245010)
)
briPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_enable.setStatus(
        ""
    )

briPort_chan_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245011)
)
briPort_chan_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_chan_util_exceeded.setStatus(
        ""
    )

briPort_no_chans = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245012)
)
briPort_no_chans.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_no_chans.setStatus(
        ""
    )

briPort_protocol_mismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245013)
)
briPort_protocol_mismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_protocol_mismatch.setStatus(
        ""
    )

bri245014_card_failu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245014)
)
bri245014_card_failu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bri245014_card_failu.setStatus(
        ""
    )

bri245015_port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245015)
)
bri245015_port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bri245015_port_boot.setStatus(
        ""
    )

bri245016_auto_recov = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 245016)
)
bri245016_auto_recov.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bri245016_auto_recov.setStatus(
        ""
    )

briPort_pkt_lvl_restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 246000)
)
briPort_pkt_lvl_restart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    briPort_pkt_lvl_restart.setStatus(
        ""
    )

dc_dsp_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248000)
)
dc_dsp_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dsp_disabled.setStatus(
        ""
    )

dc_dsp_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248001)
)
dc_dsp_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dsp_fail.setStatus(
        ""
    )

dc_no_ram = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248002)
)
dc_no_ram.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_no_ram.setStatus(
        ""
    )

dc_insuff_ram = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248003)
)
dc_insuff_ram.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_insuff_ram.setStatus(
        ""
    )

dc_no_channels = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248004)
)
dc_no_channels.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_no_channels.setStatus(
        ""
    )

dc_rcvd_neg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248005)
)
dc_rcvd_neg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_rcvd_neg.setStatus(
        ""
    )

dc_mis_configure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248006)
)
dc_mis_configure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_mis_configure.setStatus(
        ""
    )

dc_abnorm_clr_flush = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248007)
)
dc_abnorm_clr_flush.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_abnorm_clr_flush.setStatus(
        ""
    )

dc_lost_clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248008)
)
dc_lost_clr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_lost_clr.setStatus(
        ""
    )

dc_ap_to_ap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248009)
)
dc_ap_to_ap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_ap_to_ap.setStatus(
        ""
    )

dc_no_chan_for_pvc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248010)
)
dc_no_chan_for_pvc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_no_chan_for_pvc.setStatus(
        ""
    )

dc_src_config_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248011)
)
dc_src_config_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_src_config_err.setStatus(
        ""
    )

dc_corrupt_control_blk = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248012)
)
dc_corrupt_control_blk.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_corrupt_control_blk.setStatus(
        ""
    )

dc_abnorm_cmd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248013)
)
dc_abnorm_cmd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_abnorm_cmd.setStatus(
        ""
    )

dc_dsp_download_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248014)
)
dc_dsp_download_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dsp_download_err.setStatus(
        ""
    )

dc_incorrect_config = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248015)
)
dc_incorrect_config.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_incorrect_config.setStatus(
        ""
    )

dc_hdr_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248016)
)
dc_hdr_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_hdr_err.setStatus(
        ""
    )

dc_max_dc_chan = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248017)
)
dc_max_dc_chan.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_max_dc_chan.setStatus(
        ""
    )

dc_gen_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248018)
)
dc_gen_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_gen_init_fail.setStatus(
        ""
    )

dc_dbg_sem_locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248019)
)
dc_dbg_sem_locked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_sem_locked.setStatus(
        ""
    )

dc_dbg_ca_no_cr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248020)
)
dc_dbg_ca_no_cr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_ca_no_cr.setStatus(
        ""
    )

dc_dbg_no_config = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248021)
)
dc_dbg_no_config.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_no_config.setStatus(
        ""
    )

dc_dbg_dealloc_no_cb = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248022)
)
dc_dbg_dealloc_no_cb.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_dealloc_no_cb.setStatus(
        ""
    )

dc_dbg_dch_ch_stat_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248023)
)
dc_dbg_dch_ch_stat_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_dch_ch_stat_fail.setStatus(
        ""
    )

dc_dbg_lost_buffs = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248024)
)
dc_dbg_lost_buffs.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_lost_buffs.setStatus(
        ""
    )

dc_dbg_abnorm_fsm_event = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248025)
)
dc_dbg_abnorm_fsm_event.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_abnorm_fsm_event.setStatus(
        ""
    )

dc_dbg_zero_out_desc_cnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248026)
)
dc_dbg_zero_out_desc_cnt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_zero_out_desc_cnt.setStatus(
        ""
    )

dc_dbg_dch_func_status_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248027)
)
dc_dbg_dch_func_status_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_dch_func_status_fail.setStatus(
        ""
    )

dc_dbg_dch_ch_prov_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248028)
)
dc_dbg_dch_ch_prov_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_dch_ch_prov_fail.setStatus(
        ""
    )

dc_dbg_dch_ch_pop_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248029)
)
dc_dbg_dch_ch_pop_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_dch_ch_pop_fail.setStatus(
        ""
    )

dc_dbg_dch_ch_free_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248030)
)
dc_dbg_dch_ch_free_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_dch_ch_free_fail.setStatus(
        ""
    )

dc_dbg_bad_compress = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248031)
)
dc_dbg_bad_compress.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_bad_compress.setStatus(
        ""
    )

dc_dbg_func_type_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248032)
)
dc_dbg_func_type_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_func_type_fail.setStatus(
        ""
    )

dc_dbg_chan_num_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248033)
)
dc_dbg_chan_num_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_chan_num_fail.setStatus(
        ""
    )

dc_dbg_chan_stat_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248034)
)
dc_dbg_chan_stat_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_chan_stat_fail.setStatus(
        ""
    )

dc_dbg_chan_reset_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248035)
)
dc_dbg_chan_reset_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_chan_reset_fail.setStatus(
        ""
    )

dc_dbg_frm_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248036)
)
dc_dbg_frm_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_frm_error.setStatus(
        ""
    )

dc_dbg_qpck_cnt_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248037)
)
dc_dbg_qpck_cnt_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_qpck_cnt_error.setStatus(
        ""
    )

dc_dbg_dch_ch_nb_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248038)
)
dc_dbg_dch_ch_nb_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_dch_ch_nb_fail.setStatus(
        ""
    )

dc_dbg_reset_stat_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248039)
)
dc_dbg_reset_stat_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_reset_stat_fail.setStatus(
        ""
    )

dc_dbg_chan_status_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248040)
)
dc_dbg_chan_status_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_chan_status_fail.setStatus(
        ""
    )

dc_dbg_param_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248041)
)
dc_dbg_param_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_param_error.setStatus(
        ""
    )

dc_dbg_hw_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 248042)
)
dc_dbg_hw_missing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dc_dbg_hw_missing.setStatus(
        ""
    )

x32Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250000)
)
x32Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_boot.setStatus(
        ""
    )

x32Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250001)
)
x32Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_boot_fail.setStatus(
        ""
    )

x32Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250002)
)
x32Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_disable.setStatus(
        ""
    )

x32Port_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250003)
)
x32Port_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_disable_fail.setStatus(
        ""
    )

x32Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250004)
)
x32Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_enable.setStatus(
        ""
    )

x32Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250005)
)
x32Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_enable_fail.setStatus(
        ""
    )

x32Port_conn_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250006)
)
x32Port_conn_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_conn_clear.setStatus(
        ""
    )

x32Port_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250007)
)
x32Port_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_util_exceeded.setStatus(
        ""
    )

x32Port_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250008)
)
x32Port_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_warn_status.setStatus(
        ""
    )

x32Port_call_thresh_exceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250009)
)
x32Port_call_thresh_exceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_call_thresh_exceed.setStatus(
        ""
    )

x32Port_unsucc_call_exceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250010)
)
x32Port_unsucc_call_exceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_unsucc_call_exceed.setStatus(
        ""
    )

x32Port_t14_timer_expiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 250011)
)
x32Port_t14_timer_expiry.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x32Port_t14_timer_expiry.setStatus(
        ""
    )

cnui_port_disconn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 251000)
)
cnui_port_disconn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cnui_port_disconn.setStatus(
        ""
    )

cnui_port_locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 251001)
)
cnui_port_locked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cnui_port_locked.setStatus(
        ""
    )

cnui_port_degraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 251002)
)
cnui_port_degraded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cnui_port_degraded.setStatus(
        ""
    )

cnui_no_action = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 251003)
)
cnui_no_action.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cnui_no_action.setStatus(
        ""
    )

dor_agt_tbl_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 252000)
)
dor_agt_tbl_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_agt_tbl_overflow.setStatus(
        ""
    )

dor_agt_config_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 252001)
)
dor_agt_config_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_agt_config_err.setStatus(
        ""
    )

dor_unknown_call = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 252002)
)
dor_unknown_call.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_unknown_call.setStatus(
        ""
    )

dor_comm_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 252003)
)
dor_comm_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_comm_error.setStatus(
        ""
    )

dor_agt_req_abandoned = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 252004)
)
dor_agt_req_abandoned.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_agt_req_abandoned.setStatus(
        ""
    )

dor_stat_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 252005)
)
dor_stat_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_stat_overflow.setStatus(
        ""
    )

dor_mgr_config_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 253000)
)
dor_mgr_config_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_mgr_config_err.setStatus(
        ""
    )

dor_link_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 253001)
)
dor_link_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_link_fail.setStatus(
        ""
    )

dor_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 253002)
)
dor_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_link_up.setStatus(
        ""
    )

dor_mgr_req_abandoned = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 253003)
)
dor_mgr_req_abandoned.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_mgr_req_abandoned.setStatus(
        ""
    )

dor_agent_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 253004)
)
dor_agent_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_agent_fail.setStatus(
        ""
    )

dor_mgr_tbl_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 253005)
)
dor_mgr_tbl_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dor_mgr_tbl_overflow.setStatus(
        ""
    )

cnui_rrt_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 255000)
)
cnui_rrt_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cnui_rrt_boot.setStatus(
        ""
    )

cnui_rrt_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 255001)
)
cnui_rrt_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cnui_rrt_boot_fail.setStatus(
        ""
    )

cnui_rrt_util_thres_exceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 255002)
)
cnui_rrt_util_thres_exceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cnui_rrt_util_thres_exceed.setStatus(
        ""
    )

tcp_checksum_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256000)
)
tcp_checksum_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_checksum_error.setStatus(
        ""
    )

tcp_pkt_for_invalid_conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256001)
)
tcp_pkt_for_invalid_conn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_pkt_for_invalid_conn.setStatus(
        ""
    )

tcp_active_open_sccful = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256002)
)
tcp_active_open_sccful.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_active_open_sccful.setStatus(
        ""
    )

tcp_rcvd_invld_syn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256003)
)
tcp_rcvd_invld_syn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_invld_syn.setStatus(
        ""
    )

tcp_rcvd_old_syn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256004)
)
tcp_rcvd_old_syn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_old_syn.setStatus(
        ""
    )

tcp_rcvd_out_of_wdow_seg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256005)
)
tcp_rcvd_out_of_wdow_seg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_out_of_wdow_seg.setStatus(
        ""
    )

tcp_dropping_seg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256006)
)
tcp_dropping_seg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_dropping_seg.setStatus(
        ""
    )

tcp_rcvd_old_seg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256007)
)
tcp_rcvd_old_seg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_old_seg.setStatus(
        ""
    )

tcp_rcvd_rst_in_listen = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256008)
)
tcp_rcvd_rst_in_listen.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_rst_in_listen.setStatus(
        ""
    )

tcp_rcvd_rst_in_synrcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256009)
)
tcp_rcvd_rst_in_synrcvd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_rst_in_synrcvd.setStatus(
        ""
    )

tcp_rcvd_rst_so_aborting = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256010)
)
tcp_rcvd_rst_so_aborting.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_rst_so_aborting.setStatus(
        ""
    )

tcp_no_ack_so_dropping = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256011)
)
tcp_no_ack_so_dropping.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_no_ack_so_dropping.setStatus(
        ""
    )

tcp_invld_ack_dropping = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256012)
)
tcp_invld_ack_dropping.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_invld_ack_dropping.setStatus(
        ""
    )

tcp_rcvd_fin_in_estab = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256013)
)
tcp_rcvd_fin_in_estab.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_fin_in_estab.setStatus(
        ""
    )

tcp_rcvd_push = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256014)
)
tcp_rcvd_push.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_push.setStatus(
        ""
    )

tcp_entering_estab = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256015)
)
tcp_entering_estab.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_entering_estab.setStatus(
        ""
    )

tcp_rcvd_fin_in_listen = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256016)
)
tcp_rcvd_fin_in_listen.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_fin_in_listen.setStatus(
        ""
    )

tcp_add_hole_at_end = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256017)
)
tcp_add_hole_at_end.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_add_hole_at_end.setStatus(
        ""
    )

tcp_add_hole_at_beg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256018)
)
tcp_add_hole_at_beg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_add_hole_at_beg.setStatus(
        ""
    )

tcp_fill_beg_hole = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256019)
)
tcp_fill_beg_hole.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_fill_beg_hole.setStatus(
        ""
    )

tcp_fill_end_hole = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256020)
)
tcp_fill_end_hole.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_fill_end_hole.setStatus(
        ""
    )

tcp_remove_hole = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256021)
)
tcp_remove_hole.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_remove_hole.setStatus(
        ""
    )

tcp_too_big_for_rcv_buff = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256022)
)
tcp_too_big_for_rcv_buff.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_too_big_for_rcv_buff.setStatus(
        ""
    )

tcp_fin_in_invld_state = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256023)
)
tcp_fin_in_invld_state.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_fin_in_invld_state.setStatus(
        ""
    )

tcp_fin_in_valid_state = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256024)
)
tcp_fin_in_valid_state.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_fin_in_valid_state.setStatus(
        ""
    )

tcp_appln_rcv_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256025)
)
tcp_appln_rcv_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_appln_rcv_timeout.setStatus(
        ""
    )

tcp_illgl_clos_frgn_wndw = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256026)
)
tcp_illgl_clos_frgn_wndw.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_illgl_clos_frgn_wndw.setStatus(
        ""
    )

tcp_state_to_synrcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256027)
)
tcp_state_to_synrcvd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_state_to_synrcvd.setStatus(
        ""
    )

tcp_state_to_estab = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256028)
)
tcp_state_to_estab.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_state_to_estab.setStatus(
        ""
    )

tcp_rcvd_tcp_pkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256029)
)
tcp_rcvd_tcp_pkt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_tcp_pkt.setStatus(
        ""
    )

tcp_data_given_to_appln = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256030)
)
tcp_data_given_to_appln.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_data_given_to_appln.setStatus(
        ""
    )

tcp_excessive_retries = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256031)
)
tcp_excessive_retries.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_excessive_retries.setStatus(
        ""
    )

tcp_sending_control_seg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256032)
)
tcp_sending_control_seg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_sending_control_seg.setStatus(
        ""
    )

tcp_retransmitting = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256033)
)
tcp_retransmitting.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_retransmitting.setStatus(
        ""
    )

tcp_transmitting = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256034)
)
tcp_transmitting.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_transmitting.setStatus(
        ""
    )

tcp_illgl_optn_in_syn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256035)
)
tcp_illgl_optn_in_syn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_illgl_optn_in_syn.setStatus(
        ""
    )

tcp_zero_wndw_probe = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256036)
)
tcp_zero_wndw_probe.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_zero_wndw_probe.setStatus(
        ""
    )

tcp_bad_ack_in_synrcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256037)
)
tcp_bad_ack_in_synrcvd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_bad_ack_in_synrcvd.setStatus(
        ""
    )

tcp_rcvd_ack_in_listen = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256038)
)
tcp_rcvd_ack_in_listen.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_ack_in_listen.setStatus(
        ""
    )

tcp_sending_rst = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256039)
)
tcp_sending_rst.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_sending_rst.setStatus(
        ""
    )

tcp_connection_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256040)
)
tcp_connection_closed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_connection_closed.setStatus(
        ""
    )

tcp_firing_tcb_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256041)
)
tcp_firing_tcb_1.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_firing_tcb_1.setStatus(
        ""
    )

tcp_firing_tcb_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256042)
)
tcp_firing_tcb_2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_firing_tcb_2.setStatus(
        ""
    )

tcp_idle_tmr_fires = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256043)
)
tcp_idle_tmr_fires.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_idle_tmr_fires.setStatus(
        ""
    )

tcp_retransmit_tmr_fires = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256044)
)
tcp_retransmit_tmr_fires.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_retransmit_tmr_fires.setStatus(
        ""
    )

tcp_estab_to_finwait = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256045)
)
tcp_estab_to_finwait.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_estab_to_finwait.setStatus(
        ""
    )

tcp_state_to_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256046)
)
tcp_state_to_closed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_state_to_closed.setStatus(
        ""
    )

tcp_rcvd_data_aftr_close = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256047)
)
tcp_rcvd_data_aftr_close.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_data_aftr_close.setStatus(
        ""
    )

tcp_received_nack = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256048)
)
tcp_received_nack.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_received_nack.setStatus(
        ""
    )

tcp_rcvd_ack_keepalive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256049)
)
tcp_rcvd_ack_keepalive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_rcvd_ack_keepalive.setStatus(
        ""
    )

tcp_local_wndw_zero = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256050)
)
tcp_local_wndw_zero.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_local_wndw_zero.setStatus(
        ""
    )

tcp_sending_fin = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256051)
)
tcp_sending_fin.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_sending_fin.setStatus(
        ""
    )

tcp_no_buf_to_send_pkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256052)
)
tcp_no_buf_to_send_pkt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_no_buf_to_send_pkt.setStatus(
        ""
    )

tcp_transmit_buf_clipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256053)
)
tcp_transmit_buf_clipped.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_transmit_buf_clipped.setStatus(
        ""
    )

tcp_recv_buf_clipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256054)
)
tcp_recv_buf_clipped.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_recv_buf_clipped.setStatus(
        ""
    )

tcp_restarting = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256055)
)
tcp_restarting.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_restarting.setStatus(
        ""
    )

tcp_mot_high_prty_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256056)
)
tcp_mot_high_prty_trap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_mot_high_prty_trap.setStatus(
        ""
    )

tcp_mot_med_prty_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256057)
)
tcp_mot_med_prty_trap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_mot_med_prty_trap.setStatus(
        ""
    )

tcp_mot_low_prty_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 256058)
)
tcp_mot_low_prty_trap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcp_mot_low_prty_trap.setStatus(
        ""
    )

telnet_internal_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 257000)
)
telnet_internal_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    telnet_internal_err.setStatus(
        ""
    )

telnet_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 257001)
)
telnet_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    telnet_err.setStatus(
        ""
    )

async360_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 259000)
)
async360_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async360_err_count_exceeded.setStatus(
        ""
    )

async360_dbits_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 259001)
)
async360_dbits_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async360_dbits_unsupp.setStatus(
        ""
    )

async360_baud_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 259002)
)
async360_baud_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async360_baud_unsupp.setStatus(
        ""
    )

async360_parity_unsupp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 259003)
)
async360_parity_unsupp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    async360_parity_unsupp.setStatus(
        ""
    )

bop360_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 260000)
)
bop360_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop360_err_count_exceeded.setStatus(
        ""
    )

bop360_unsupp_speed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 260001)
)
bop360_unsupp_speed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop360_unsupp_speed.setStatus(
        ""
    )

bop360_rx_byte_count_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 260002)
)
bop360_rx_byte_count_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop360_rx_byte_count_err.setStatus(
        ""
    )

bop360_erroneous_bool = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 260003)
)
bop360_erroneous_bool.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop360_erroneous_bool.setStatus(
        ""
    )

bop360_clk_override = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 260004)
)
bop360_clk_override.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop360_clk_override.setStatus(
        ""
    )

bop360_tx_sanity_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 260005)
)
bop360_tx_sanity_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    bop360_tx_sanity_timeout.setStatus(
        ""
    )

iodrivers260006_corr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 260006)
)
iodrivers260006_corr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers260006_corr.setStatus(
        ""
    )

cop360_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 261000)
)
cop360_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    cop360_err_count_exceeded.setStatus(
        ""
    )

mc68302drvr_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 262000)
)
mc68302drvr_trap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mc68302drvr_trap.setStatus(
        ""
    )

mc68360drvr_traps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 264000)
)
mc68360drvr_traps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    mc68360drvr_traps.setStatus(
        ""
    )

iodrivers_sgnothrottletimer = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265000)
)
iodrivers_sgnothrottletimer.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgnothrottletimer.setStatus(
        ""
    )

iodrivers_sgnoinitializatio = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265001)
)
iodrivers_sgnoinitializatio.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgnoinitializatio.setStatus(
        ""
    )

iodrivers_sgconfigurationfaile = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265002)
)
iodrivers_sgconfigurationfaile.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgconfigurationfaile.setStatus(
        ""
    )

iodrivers_sgiafaile = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265003)
)
iodrivers_sgiafaile.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgiafaile.setStatus(
        ""
    )

iodrivers_sgconfigurationtimedout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265004)
)
iodrivers_sgconfigurationtimedout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgconfigurationtimedout.setStatus(
        ""
    )

iodrivers_sgnosuspensio = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265005)
)
iodrivers_sgnosuspensio.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgnosuspensio.setStatus(
        ""
    )

iodrivers_sgtxlistputfaile = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265006)
)
iodrivers_sgtxlistputfaile.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgtxlistputfaile.setStatus(
        ""
    )

iodrivers_sgexcessivetxerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265007)
)
iodrivers_sgexcessivetxerror.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgexcessivetxerror.setStatus(
        ""
    )

iodrivers_sglossofcarrie = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265008)
)
iodrivers_sglossofcarrie.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sglossofcarrie.setStatus(
        ""
    )

iodrivers_sgexcessiverxerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265009)
)
iodrivers_sgexcessiverxerror.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgexcessiverxerror.setStatus(
        ""
    )

iodrivers_sgexcessivetxclea = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265010)
)
iodrivers_sgexcessivetxclea.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgexcessivetxclea.setStatus(
        ""
    )

iodrivers_sglossofcarrierclea = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265011)
)
iodrivers_sglossofcarrierclea.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sglossofcarrierclea.setStatus(
        ""
    )

iodrivers_sgexcessiverxclea = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265012)
)
iodrivers_sgexcessiverxclea.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgexcessiverxclea.setStatus(
        ""
    )

iodrivers_sginvalidstateenable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265013)
)
iodrivers_sginvalidstateenable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sginvalidstateenable.setStatus(
        ""
    )

iodrivers_sginvalidstatedisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265014)
)
iodrivers_sginvalidstatedisable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sginvalidstatedisable.setStatus(
        ""
    )

iodrivers_sgloopbackfaile = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265015)
)
iodrivers_sgloopbackfaile.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgloopbackfaile.setStatus(
        ""
    )

iodrivers_sgtdrfaile = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 265016)
)
iodrivers_sgtdrfaile.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers_sgtdrfaile.setStatus(
        ""
    )

pppPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268000)
)
pppPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppPort_boot.setStatus(
        ""
    )

pppPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268001)
)
pppPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppPort_boot_fail.setStatus(
        ""
    )

pppPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268002)
)
pppPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppPort_disable.setStatus(
        ""
    )

pppPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268003)
)
pppPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppPort_enable.setStatus(
        ""
    )

pppPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268004)
)
pppPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppPort_util_exceeded.setStatus(
        ""
    )

pppPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268005)
)
pppPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppPort_warn_status.setStatus(
        ""
    )

pppPort_err_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268006)
)
pppPort_err_count_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppPort_err_count_exceeded.setStatus(
        ""
    )

ppp_allocated_bytes_for_tracing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268007)
)
ppp_allocated_bytes_for_tracing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_allocated_bytes_for_tracing.setStatus(
        ""
    )

ppp_port_initialization_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 268008)
)
ppp_port_initialization_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_port_initialization_failed.setStatus(
        ""
    )

pppL2_out_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 269000)
)
pppL2_out_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_out_data_loss.setStatus(
        ""
    )

pppL2_frame_reject = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 269001)
)
pppL2_frame_reject.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_frame_reject.setStatus(
        ""
    )

pppL2_unsupp_proto = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270000)
)
pppL2_unsupp_proto.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_unsupp_proto.setStatus(
        ""
    )

pppL2_vj_comp_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270001)
)
pppL2_vj_comp_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_vj_comp_fail.setStatus(
        ""
    )

pppL2_login_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270002)
)
pppL2_login_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_login_fail.setStatus(
        ""
    )

pppL2_login_ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270003)
)
pppL2_login_ok.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_login_ok.setStatus(
        ""
    )

ppp_proto_compneg_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270004)
)
ppp_proto_compneg_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_proto_compneg_failed.setStatus(
        ""
    )

ppp_proto_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270005)
)
ppp_proto_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_proto_data_loss.setStatus(
        ""
    )

ppp_dedicated_link_not_configure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270006)
)
ppp_dedicated_link_not_configure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_dedicated_link_not_configure.setStatus(
        ""
    )

ppp_dedicated_link_already_alloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270007)
)
ppp_dedicated_link_already_alloc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_dedicated_link_already_alloc.setStatus(
        ""
    )

ppp_discarding_frames = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270008)
)
ppp_discarding_frames.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_discarding_frames.setStatus(
        ""
    )

ppp_received_multilink_frame_wit = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270009)
)
ppp_received_multilink_frame_wit.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_received_multilink_frame_wit.setStatus(
        ""
    )

ppp_remote_is_silent = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270010)
)
ppp_remote_is_silent.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_remote_is_silent.setStatus(
        ""
    )

ppp_no_profile_available_for_s = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270011)
)
ppp_no_profile_available_for_s.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_no_profile_available_for_s.setStatus(
        ""
    )

ppp_inconsistent_link_negotiatio = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270012)
)
ppp_inconsistent_link_negotiatio.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_inconsistent_link_negotiatio.setStatus(
        ""
    )

ppp_no_bundles_available = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270013)
)
ppp_no_bundles_available.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_no_bundles_available.setStatus(
        ""
    )

ppp_the_peers_name_exceeds_16_ch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270014)
)
ppp_the_peers_name_exceeds_16_ch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_the_peers_name_exceeds_16_ch.setStatus(
        ""
    )

ppp_authentication_was_rejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270015)
)
ppp_authentication_was_rejected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_authentication_was_rejected.setStatus(
        ""
    )

ppp_link_is_looped_back = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270016)
)
ppp_link_is_looped_back.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_link_is_looped_back.setStatus(
        ""
    )

ppp_exceeds_maximum_number_of_li = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270017)
)
ppp_exceeds_maximum_number_of_li.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_exceeds_maximum_number_of_li.setStatus(
        ""
    )

ppp_permanent_links_must_configu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 270018)
)
ppp_permanent_links_must_configu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ppp_permanent_links_must_configu.setStatus(
        ""
    )

pppL2_in_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 271000)
)
pppL2_in_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_in_data_loss.setStatus(
        ""
    )

pppL2_invalid_encaps = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 271001)
)
pppL2_invalid_encaps.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pppL2_invalid_encaps.setStatus(
        ""
    )

isdn_lapd_fseq_override = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 275000)
)
isdn_lapd_fseq_override.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_lapd_fseq_override.setStatus(
        ""
    )

isdn_line_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278000)
)
isdn_line_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_line_active.setStatus(
        ""
    )

isdn_line_inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278001)
)
isdn_line_inactive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_line_inactive.setStatus(
        ""
    )

isdn_loop_test = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278002)
)
isdn_loop_test.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_loop_test.setStatus(
        ""
    )

isdn_incompatible_detect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278003)
)
isdn_incompatible_detect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_incompatible_detect.setStatus(
        ""
    )

isdn_terminal_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278004)
)
isdn_terminal_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_terminal_init_fail.setStatus(
        ""
    )

isdn_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278005)
)
isdn_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_Port_boot.setStatus(
        ""
    )

isdn_debug_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278006)
)
isdn_debug_info.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_debug_info.setStatus(
        ""
    )

isdn_illegal_port_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278007)
)
isdn_illegal_port_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_illegal_port_type.setStatus(
        ""
    )

isdn_Port_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278008)
)
isdn_Port_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_Port_connected.setStatus(
        ""
    )

isdn_Port_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278009)
)
isdn_Port_disconnected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_Port_disconnected.setStatus(
        ""
    )

isdn_switch_override = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278010)
)
isdn_switch_override.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_switch_override.setStatus(
        ""
    )

isdn_terminal_init = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278011)
)
isdn_terminal_init.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_terminal_init.setStatus(
        ""
    )

isdn_dialing_to_on_bri_int_chann = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278012)
)
isdn_dialing_to_on_bri_int_chann.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_dialing_to_on_bri_int_chann.setStatus(
        ""
    )

isdn_incoming_call_on_bri_int_chan = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278013)
)
isdn_incoming_call_on_bri_int_chan.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_incoming_call_on_bri_int_chan.setStatus(
        ""
    )

isdn_bri_int_boot_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278014)
)
isdn_bri_int_boot_completed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_bri_int_boot_completed.setStatus(
        ""
    )

isdn_duplicate_fix_tei_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278015)
)
isdn_duplicate_fix_tei_detected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_duplicate_fix_tei_detected.setStatus(
        ""
    )

isdn_dial_number_contention = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278016)
)
isdn_dial_number_contention.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_dial_number_contention.setStatus(
        ""
    )

isdn278017_disconnec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278017)
)
isdn278017_disconnec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278017_disconnec.setStatus(
        ""
    )

isdn278018_false_dis = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278018)
)
isdn278018_false_dis.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278018_false_dis.setStatus(
        ""
    )

isdn278019_isdn_pri = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278019)
)
isdn278019_isdn_pri.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278019_isdn_pri.setStatus(
        ""
    )

isdn278020_isdn_pri = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278020)
)
isdn278020_isdn_pri.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278020_isdn_pri.setStatus(
        ""
    )

isdn278023_isdn_bri = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278023)
)
isdn278023_isdn_bri.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278023_isdn_bri.setStatus(
        ""
    )

isdn278025_qsig_erro = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278025)
)
isdn278025_qsig_erro.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278025_qsig_erro.setStatus(
        ""
    )

isdn278026_invalid_q = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278026)
)
isdn278026_invalid_q.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278026_invalid_q.setStatus(
        ""
    )

isdn278027_isdn_bri = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278027)
)
isdn278027_isdn_bri.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278027_isdn_bri.setStatus(
        ""
    )

isdn278030_isdn_bri = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278030)
)
isdn278030_isdn_bri.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278030_isdn_bri.setStatus(
        ""
    )

isdn278031_isdn_bri = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 278031)
)
isdn278031_isdn_bri.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn278031_isdn_bri.setStatus(
        ""
    )

isdn_lif_packet = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 279000)
)
isdn_lif_packet.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_lif_packet.setStatus(
        ""
    )

voice_hw_board_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280000)
)
voice_hw_board_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_hw_board_fail.setStatus(
        ""
    )

voice_Port_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280001)
)
voice_Port_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_fail.setStatus(
        ""
    )

voice_Port_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280002)
)
voice_Port_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_init_fail.setStatus(
        ""
    )

voice_Port_not_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280003)
)
voice_Port_not_started.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_not_started.setStatus(
        ""
    )

voice_Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280004)
)
voice_Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_boot_fail.setStatus(
        ""
    )

voice_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280005)
)
voice_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_boot.setStatus(
        ""
    )

voice_Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280006)
)
voice_Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_disable.setStatus(
        ""
    )

voice_Port_busyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280007)
)
voice_Port_busyout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_busyout.setStatus(
        ""
    )

voice_Port_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280008)
)
voice_Port_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_disable_fail.setStatus(
        ""
    )

voice_Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280009)
)
voice_Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_enable.setStatus(
        ""
    )

voice_Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280010)
)
voice_Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_enable_fail.setStatus(
        ""
    )

voice_Port_busyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280011)
)
voice_Port_busyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    voice_Port_busyout_fail.setStatus(
        ""
    )

vport_virtual_mapping_error_caus = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280012)
)
vport_virtual_mapping_error_caus.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_virtual_mapping_error_caus.setStatus(
        ""
    )

vport_virtual_mapping_error_caus2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280013)
)
vport_virtual_mapping_error_caus2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_virtual_mapping_error_caus2.setStatus(
        ""
    )

vport_voice_record_conversion_co = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280014)
)
vport_voice_record_conversion_co.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_voice_record_conversion_co.setStatus(
        ""
    )

vport_voice_record_conversion_fa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280015)
)
vport_voice_record_conversion_fa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_voice_record_conversion_fa.setStatus(
        ""
    )

vport_voice_record_conversion_vs = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 280016)
)
vport_voice_record_conversion_vs.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_voice_record_conversion_vs.setStatus(
        ""
    )

vdcdm_hw_board_failure_cause_bac = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281000)
)
vdcdm_hw_board_failure_cause_bac.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_hw_board_failure_cause_bac.setStatus(
        ""
    )

vdcdm_board_boot_cause_watchdog = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281001)
)
vdcdm_board_boot_cause_watchdog.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_board_boot_cause_watchdog.setStatus(
        ""
    )

vdcdm_port_failure_cause_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281002)
)
vdcdm_port_failure_cause_missing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_port_failure_cause_missing.setStatus(
        ""
    )

vdcdm_port_failure_cause_missing2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281003)
)
vdcdm_port_failure_cause_missing2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_port_failure_cause_missing2.setStatus(
        ""
    )

vdcdm_dspm_software_download_com = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281004)
)
vdcdm_dspm_software_download_com.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_dspm_software_download_com.setStatus(
        ""
    )

vdcdm_dspm_software_download_fai = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281005)
)
vdcdm_dspm_software_download_fai.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_dspm_software_download_fai.setStatus(
        ""
    )

vdcdm_voice_signaling_trace = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281006)
)
vdcdm_voice_signaling_trace.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_voice_signaling_trace.setStatus(
        ""
    )

vdcdm_error_on_channel_cause = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281007)
)
vdcdm_error_on_channel_cause.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_error_on_channel_cause.setStatus(
        ""
    )

vdcdm_dspm_crash_reason_pc_add = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281008)
)
vdcdm_dspm_crash_reason_pc_add.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_dspm_crash_reason_pc_add.setStatus(
        ""
    )

vdcdm_dspm_first_recovery_succes = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281009)
)
vdcdm_dspm_first_recovery_succes.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_dspm_first_recovery_succes.setStatus(
        ""
    )

vdcdm_dspm_second_recovery_succe = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281010)
)
vdcdm_dspm_second_recovery_succe.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_dspm_second_recovery_succe.setStatus(
        ""
    )

vdcdm_dspm_protocol_initializati = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281011)
)
vdcdm_dspm_protocol_initializati.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_dspm_protocol_initializati.setStatus(
        ""
    )

vdcdm_voice_call_calling_called = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281012)
)
vdcdm_voice_call_calling_called.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_voice_call_calling_called.setStatus(
        ""
    )

vdcdm_voice_vsm_command_eid_3d_o = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281013)
)
vdcdm_voice_vsm_command_eid_3d_o.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_voice_vsm_command_eid_3d_o.setStatus(
        ""
    )

vdcdm_voice_vsm_response_eid_3d = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281014)
)
vdcdm_voice_vsm_response_eid_3d.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm_voice_vsm_response_eid_3d.setStatus(
        ""
    )

vdcdm281015_voice_trace = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281015)
)
vdcdm281015_voice_trace.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm281015_voice_trace.setStatus(
        ""
    )

vdcdm281016_voice_ca = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281016)
)
vdcdm281016_voice_ca.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm281016_voice_ca.setStatus(
        ""
    )

vdcdm281017_voice = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281017)
)
vdcdm281017_voice.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm281017_voice.setStatus(
        ""
    )

vdcdm281018_dsp_last = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281018)
)
vdcdm281018_dsp_last.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm281018_dsp_last.setStatus(
        ""
    )

vdcdm281019_voice = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 281019)
)
vdcdm281019_voice.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vdcdm281019_voice.setStatus(
        ""
    )

t1e1_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 282000)
)
t1e1_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_Port_boot.setStatus(
        ""
    )

t1e1_Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 282001)
)
t1e1_Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_Port_boot_fail.setStatus(
        ""
    )

t1e1_Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 282002)
)
t1e1_Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_Port_disable.setStatus(
        ""
    )

t1e1_Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 282003)
)
t1e1_Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_Port_enable.setStatus(
        ""
    )

t1e1_Port_not_init = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 282004)
)
t1e1_Port_not_init.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_Port_not_init.setStatus(
        ""
    )

t1e1_Port_vmt_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 282005)
)
t1e1_Port_vmt_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_Port_vmt_error.setStatus(
        ""
    )

t1e1_putmsg_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283000)
)
t1e1_putmsg_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_putmsg_failed.setStatus(
        ""
    )

t1e1_comm_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283001)
)
t1e1_comm_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_comm_error.setStatus(
        ""
    )

t1e1_fatal_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283002)
)
t1e1_fatal_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_fatal_error.setStatus(
        ""
    )

t1e1_dload_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283003)
)
t1e1_dload_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_dload_failed.setStatus(
        ""
    )

t1e1_threshold_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283004)
)
t1e1_threshold_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_threshold_exceeded.setStatus(
        ""
    )

t1e1_t1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283005)
)
t1e1_t1_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_t1_alarm.setStatus(
        ""
    )

t1e1_e1_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283006)
)
t1e1_e1_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_e1_alarm.setStatus(
        ""
    )

t1e1_background_diag = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283007)
)
t1e1_background_diag.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_background_diag.setStatus(
        ""
    )

t1e1_watchdog_expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283008)
)
t1e1_watchdog_expired.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_watchdog_expired.setStatus(
        ""
    )

t1e1_illegal_clocking = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283009)
)
t1e1_illegal_clocking.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_illegal_clocking.setStatus(
        ""
    )

t1e1_invalid_message = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283010)
)
t1e1_invalid_message.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_invalid_message.setStatus(
        ""
    )

t1e1_pri_b_incoming_call_to_from = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283011)
)
t1e1_pri_b_incoming_call_to_from.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_b_incoming_call_to_from.setStatus(
        ""
    )

t1e1_pri_b_outgoing_call_to_conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283012)
)
t1e1_pri_b_outgoing_call_to_conn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_b_outgoing_call_to_conn.setStatus(
        ""
    )

t1e1_pri_call_on_port_disconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283013)
)
t1e1_pri_call_on_port_disconnect.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_call_on_port_disconnect.setStatus(
        ""
    )

t1e1_pri_call_on_port_disconnect2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283014)
)
t1e1_pri_call_on_port_disconnect2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_call_on_port_disconnect2.setStatus(
        ""
    )

t1e1_pri_incoming_call_to_from_f = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283015)
)
t1e1_pri_incoming_call_to_from_f.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_incoming_call_to_from_f.setStatus(
        ""
    )

t1e1_pri_outgoing_call_to_from_f = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283016)
)
t1e1_pri_outgoing_call_to_from_f.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_outgoing_call_to_from_f.setStatus(
        ""
    )

t1e1_pri_incoming_call_to_from_f2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283017)
)
t1e1_pri_incoming_call_to_from_f2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_incoming_call_to_from_f2.setStatus(
        ""
    )

t1e1_pri_d_channel_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283018)
)
t1e1_pri_d_channel_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_d_channel_up.setStatus(
        ""
    )

t1e1_pri_d_channel_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283019)
)
t1e1_pri_d_channel_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_d_channel_down.setStatus(
        ""
    )

t1e1_pri_b_b_channel_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283020)
)
t1e1_pri_b_b_channel_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_b_b_channel_up.setStatus(
        ""
    )

t1e1_pri_b_b_channel_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283021)
)
t1e1_pri_b_b_channel_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_b_b_channel_down.setStatus(
        ""
    )

t1e1_virtual_port_config_does_no = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283022)
)
t1e1_virtual_port_config_does_no.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_virtual_port_config_does_no.setStatus(
        ""
    )

t1e1_isdn_signaling_message_rece = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283023)
)
t1e1_isdn_signaling_message_rece.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_isdn_signaling_message_rece.setStatus(
        ""
    )

t1e1_pri_d_channel_establishing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283024)
)
t1e1_pri_d_channel_establishing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_d_channel_establishing.setStatus(
        ""
    )

t1e1_pri_b_incoming_call_to_from2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283025)
)
t1e1_pri_b_incoming_call_to_from2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_b_incoming_call_to_from2.setStatus(
        ""
    )

t1e1_function_name_sigstate = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283026)
)
t1e1_function_name_sigstate.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_function_name_sigstate.setStatus(
        ""
    )

t1e1_t1e1drv_invalid_execution_l = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283027)
)
t1e1_t1e1drv_invalid_execution_l.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_t1e1drv_invalid_execution_l.setStatus(
        ""
    )

t1e1_pri_d_channel_restarted_all = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283028)
)
t1e1_pri_d_channel_restarted_all.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_d_channel_restarted_all.setStatus(
        ""
    )

t1e1_invalid_pri_signalling_port = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283029)
)
t1e1_invalid_pri_signalling_port.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_invalid_pri_signalling_port.setStatus(
        ""
    )

t1e1_virtual_port_t1e1_card_does = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283030)
)
t1e1_virtual_port_t1e1_card_does.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_virtual_port_t1e1_card_does.setStatus(
        ""
    )

t1e1_virtual_port_no_hdlc_channe = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283031)
)
t1e1_virtual_port_no_hdlc_channe.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_virtual_port_no_hdlc_channe.setStatus(
        ""
    )

t1e1_virtual_port_no_t1e1_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283032)
)
t1e1_virtual_port_no_t1e1_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_virtual_port_no_t1e1_memory.setStatus(
        ""
    )

t1e1_pri_call_on_port_disconnect22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 283033)
)
t1e1_pri_call_on_port_disconnect22.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1_pri_call_on_port_disconnect22.setStatus(
        ""
    )

spfm_pvc_connection_failed_on = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285001)
)
spfm_pvc_connection_failed_on.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_pvc_connection_failed_on.setStatus(
        ""
    )

spfm_pvc_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285002)
)
spfm_pvc_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_pvc_connected.setStatus(
        ""
    )

spfm_disabled_duplicate_slot_on = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285003)
)
spfm_disabled_duplicate_slot_on.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_disabled_duplicate_slot_on.setStatus(
        ""
    )

spfm_disabled_misconfigured_opti = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285004)
)
spfm_disabled_misconfigured_opti.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_disabled_misconfigured_opti.setStatus(
        ""
    )

spfm_connection_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285005)
)
spfm_connection_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_connection_active.setStatus(
        ""
    )

spfm_connection_inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285006)
)
spfm_connection_inactive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_connection_inactive.setStatus(
        ""
    )

spfm_rx_data_on_unknown_dlci_slo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285007)
)
spfm_rx_data_on_unknown_dlci_slo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_rx_data_on_unknown_dlci_slo.setStatus(
        ""
    )

spfm_header_format_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285008)
)
spfm_header_format_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_header_format_error.setStatus(
        ""
    )

spfm_configuration_mismatch_on_r = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 285009)
)
spfm_configuration_mismatch_on_r.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_configuration_mismatch_on_r.setStatus(
        ""
    )

spfm_entry_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 286001)
)
spfm_entry_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_entry_boot_complete.setStatus(
        ""
    )

spfm_entry_boot_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 286002)
)
spfm_entry_boot_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spfm_entry_boot_failed.setStatus(
        ""
    )

smds_stn_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 289000)
)
smds_stn_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    smds_stn_data_loss.setStatus(
        ""
    )

smds_stn_invalid_encap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 289001)
)
smds_stn_invalid_encap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    smds_stn_invalid_encap.setStatus(
        ""
    )

smds_stn_masked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 289002)
)
smds_stn_masked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    smds_stn_masked.setStatus(
        ""
    )

smds_sni_data_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 290000)
)
smds_sni_data_loss.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    smds_sni_data_loss.setStatus(
        ""
    )

smds_sni_invalid_encap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 290001)
)
smds_sni_invalid_encap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    smds_sni_invalid_encap.setStatus(
        ""
    )

smds_sni_no_station = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 290002)
)
smds_sni_no_station.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    smds_sni_no_station.setStatus(
        ""
    )

dxi_port_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 291000)
)
dxi_port_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_port_boot_complete.setStatus(
        ""
    )

dxi_port_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 291001)
)
dxi_port_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_port_boot_failure.setStatus(
        ""
    )

dxi_port_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 291002)
)
dxi_port_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_port_disabled.setStatus(
        ""
    )

dxi_port_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 291003)
)
dxi_port_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_port_enabled.setStatus(
        ""
    )

dxi_port_utilization_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 291004)
)
dxi_port_utilization_threshold.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_port_utilization_threshold.setStatus(
        ""
    )

dxi_port_status_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 291005)
)
dxi_port_status_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_port_status_warning.setStatus(
        ""
    )

dxi_data_lost_from_rx_data_queue = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 292000)
)
dxi_data_lost_from_rx_data_queue.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_data_lost_from_rx_data_queue.setStatus(
        ""
    )

dxi_data_lost_from_tx_data_queue = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 292001)
)
dxi_data_lost_from_tx_data_queue.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_data_lost_from_tx_data_queue.setStatus(
        ""
    )

dxi_no_heartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 292002)
)
dxi_no_heartbeat.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dxi_no_heartbeat.setStatus(
        ""
    )

ipxwan_null_rfcm_cb = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293000)
)
ipxwan_null_rfcm_cb.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_null_rfcm_cb.setStatus(
        ""
    )

ipxwan_not_enough_ram = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293001)
)
ipxwan_not_enough_ram.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_not_enough_ram.setStatus(
        ""
    )

ipxwan_alloc_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293002)
)
ipxwan_alloc_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_alloc_failed.setStatus(
        ""
    )

ipxwan_module_not_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293003)
)
ipxwan_module_not_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_module_not_active.setStatus(
        ""
    )

ipxwan_ipx_not_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293004)
)
ipxwan_ipx_not_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_ipx_not_active.setStatus(
        ""
    )

ipxwan_called_for_lan = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293005)
)
ipxwan_called_for_lan.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_called_for_lan.setStatus(
        ""
    )

ipxwan_nul_ipxwancb = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293006)
)
ipxwan_nul_ipxwancb.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_nul_ipxwancb.setStatus(
        ""
    )

ipxwan_dropping_packet = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293007)
)
ipxwan_dropping_packet.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_dropping_packet.setStatus(
        ""
    )

ipxwan_bad_format = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293008)
)
ipxwan_bad_format.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_bad_format.setStatus(
        ""
    )

ipxwan_rcvd_tmr_req_opt_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293009)
)
ipxwan_rcvd_tmr_req_opt_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_req_opt_len.setStatus(
        ""
    )

ipxwan_rcvd_tmr_req_wnode_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293010)
)
ipxwan_rcvd_tmr_req_wnode_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_req_wnode_id.setStatus(
        ""
    )

ipxwan_rcvd_tmr_req_ext_node = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293011)
)
ipxwan_rcvd_tmr_req_ext_node.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_req_ext_node.setStatus(
        ""
    )

ipxwan_tmr_req_cfg_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293012)
)
ipxwan_tmr_req_cfg_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_tmr_req_cfg_error.setStatus(
        ""
    )

ipxwan_rcvd_tmr_req_no_common_routing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293013)
)
ipxwan_rcvd_tmr_req_no_common_routing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_req_no_common_routing.setStatus(
        ""
    )

ipxwan_rcvd_tmr_resp_wnode_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293014)
)
ipxwan_rcvd_tmr_resp_wnode_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_resp_wnode_id.setStatus(
        ""
    )

ipxwan_rcvd_tmr_resp_multiple_routing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293015)
)
ipxwan_rcvd_tmr_resp_multiple_routing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_resp_multiple_routing.setStatus(
        ""
    )

ipxwan_rcvd_tmr_resp_routing_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293016)
)
ipxwan_rcvd_tmr_resp_routing_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_resp_routing_type.setStatus(
        ""
    )

ipxwan_rcvd_tmr_resp_not_supported = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293017)
)
ipxwan_rcvd_tmr_resp_not_supported.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_resp_not_supported.setStatus(
        ""
    )

ipxwan_rcvd_tmr_resp_opt_len = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293018)
)
ipxwan_rcvd_tmr_resp_opt_len.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_resp_opt_len.setStatus(
        ""
    )

ipxwan_rcvd_tmr_resp_header_comp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293019)
)
ipxwan_rcvd_tmr_resp_header_comp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_resp_header_comp.setStatus(
        ""
    )

ipxwan_rcvd_tmr_resp_no_routing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293020)
)
ipxwan_rcvd_tmr_resp_no_routing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_tmr_resp_no_routing.setStatus(
        ""
    )

ipxwan_rcvd_info_req_wnode_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293021)
)
ipxwan_rcvd_info_req_wnode_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_req_wnode_id.setStatus(
        ""
    )

ipxwan_rcvd_info_info_exchg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293022)
)
ipxwan_rcvd_info_info_exchg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_info_exchg.setStatus(
        ""
    )

ipxwan_rcvd_info_no_info_exchg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293023)
)
ipxwan_rcvd_info_no_info_exchg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_no_info_exchg.setStatus(
        ""
    )

ipxwan_rcvd_info_netno_zero = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293024)
)
ipxwan_rcvd_info_netno_zero.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_netno_zero.setStatus(
        ""
    )

ipxwan_rcvd_info_netno_nonzero = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293025)
)
ipxwan_rcvd_info_netno_nonzero.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_netno_nonzero.setStatus(
        ""
    )

ipxwan_rcvd_info_conflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293026)
)
ipxwan_rcvd_info_conflict.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_conflict.setStatus(
        ""
    )

ipxwan_rcvd_info_resp_wnode_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293027)
)
ipxwan_rcvd_info_resp_wnode_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_resp_wnode_id.setStatus(
        ""
    )

ipxwan_rcvd_info_resp_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293028)
)
ipxwan_rcvd_info_resp_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_resp_active.setStatus(
        ""
    )

ipxwan_rcvd_info_resp_setting = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293029)
)
ipxwan_rcvd_info_resp_setting.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_rcvd_info_resp_setting.setStatus(
        ""
    )

ipxwan_getbuf_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293030)
)
ipxwan_getbuf_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_getbuf_failed.setStatus(
        ""
    )

ipxwan_unsupported_event = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293031)
)
ipxwan_unsupported_event.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_unsupported_event.setStatus(
        ""
    )

ipxwan_state_machine = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293032)
)
ipxwan_state_machine.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_state_machine.setStatus(
        ""
    )

ipxwan_internal_buffer_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 293033)
)
ipxwan_internal_buffer_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ipxwan_internal_buffer_overflow.setStatus(
        ""
    )

tow_report_no_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 294000)
)
tow_report_no_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tow_report_no_memory.setStatus(
        ""
    )

tow_report_not_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 294001)
)
tow_report_not_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tow_report_not_active.setStatus(
        ""
    )

tow_report_default_entry = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 294002)
)
tow_report_default_entry.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tow_report_default_entry.setStatus(
        ""
    )

tow_report_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 294003)
)
tow_report_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tow_report_active.setStatus(
        ""
    )

vx_stn_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 295000)
)
vx_stn_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vx_stn_boot_complete.setStatus(
        ""
    )

vx_stn_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 295001)
)
vx_stn_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vx_stn_boot_failure.setStatus(
        ""
    )

vx_stn_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 295002)
)
vx_stn_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vx_stn_disabled.setStatus(
        ""
    )

vx_stn_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 295003)
)
vx_stn_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vx_stn_enabled.setStatus(
        ""
    )

vx_no_config_for_stn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 295004)
)
vx_no_config_for_stn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vx_no_config_for_stn.setStatus(
        ""
    )

pnef_tfr_insufficient_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298000)
)
pnef_tfr_insufficient_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_insufficient_memory.setStatus(
        ""
    )

pnef_tfr_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298001)
)
pnef_tfr_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_boot_failure.setStatus(
        ""
    )

pnef_tfr_connection_established = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298002)
)
pnef_tfr_connection_established.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_connection_established.setStatus(
        ""
    )

pnef_tfr_connection_failure_with = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298003)
)
pnef_tfr_connection_failure_with.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_connection_failure_with.setStatus(
        ""
    )

pnef_tfr_unknown_caller = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298004)
)
pnef_tfr_unknown_caller.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_unknown_caller.setStatus(
        ""
    )

pnef_tfr_frame_discarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298005)
)
pnef_tfr_frame_discarded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_frame_discarded.setStatus(
        ""
    )

pnef_tfr_queue_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298006)
)
pnef_tfr_queue_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_queue_overflow.setStatus(
        ""
    )

pnef_tfr_received_incomplete_fra = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 298007)
)
pnef_tfr_received_incomplete_fra.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfr_received_incomplete_fra.setStatus(
        ""
    )

pnef_tfri_insufficient_memory_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 299000)
)
pnef_tfri_insufficient_memory_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfri_insufficient_memory_in.setStatus(
        ""
    )

pnef_tfri_insufficient_memory_in2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 299001)
)
pnef_tfri_insufficient_memory_in2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfri_insufficient_memory_in2.setStatus(
        ""
    )

pnef_tfri_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 299002)
)
pnef_tfri_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfri_boot_failure.setStatus(
        ""
    )

pnef_tfri_connection_established = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 299003)
)
pnef_tfri_connection_established.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfri_connection_established.setStatus(
        ""
    )

pnef_tfri_connection_failure_wit = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 299004)
)
pnef_tfri_connection_failure_wit.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfri_connection_failure_wit.setStatus(
        ""
    )

pnef_tfri_frame_discarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 299005)
)
pnef_tfri_frame_discarded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfri_frame_discarded.setStatus(
        ""
    )

pnef_tfri_socket_registration_fa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 299006)
)
pnef_tfri_socket_registration_fa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pnef_tfri_socket_registration_fa.setStatus(
        ""
    )

tdlcPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 300000)
)
tdlcPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdlcPort_boot.setStatus(
        ""
    )

tdlcPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 300001)
)
tdlcPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdlcPort_disable.setStatus(
        ""
    )

tdlcPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 300002)
)
tdlcPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdlcPort_enable.setStatus(
        ""
    )

tdlcPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 300003)
)
tdlcPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdlcPort_util_exceeded.setStatus(
        ""
    )

tdlcPort_statuswarn_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 300004)
)
tdlcPort_statuswarn_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdlcPort_statuswarn_disabled.setStatus(
        ""
    )

tdlcPort_utilexceed_pagingTerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 300005)
)
tdlcPort_utilexceed_pagingTerm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdlcPort_utilexceed_pagingTerm.setStatus(
        ""
    )

vport_voice_switching_record_fai = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 304000)
)
vport_voice_switching_record_fai.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_voice_switching_record_fai.setStatus(
        ""
    )

vport_voice_switching_record_con = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 304001)
)
vport_voice_switching_record_con.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_voice_switching_record_con.setStatus(
        ""
    )

iso3201_Port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306000)
)
iso3201_Port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Port_boot.setStatus(
        ""
    )

iso3201_Port_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306001)
)
iso3201_Port_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Port_boot_fail.setStatus(
        ""
    )

iso3201_Port_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306002)
)
iso3201_Port_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Port_disable.setStatus(
        ""
    )

iso3201_Port_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306003)
)
iso3201_Port_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Port_disable_fail.setStatus(
        ""
    )

iso3201_Port_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306004)
)
iso3201_Port_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Port_enable.setStatus(
        ""
    )

iso3201_Port_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306005)
)
iso3201_Port_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Port_enable_fail.setStatus(
        ""
    )

iso3201_Port_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306006)
)
iso3201_Port_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Port_warn_status.setStatus(
        ""
    )

iso3201_Stn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306007)
)
iso3201_Stn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_boot.setStatus(
        ""
    )

iso3201_Stn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306008)
)
iso3201_Stn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_boot_fail.setStatus(
        ""
    )

iso3201_Stn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306009)
)
iso3201_Stn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_disable.setStatus(
        ""
    )

iso3201_Stn_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306010)
)
iso3201_Stn_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_disable_fail.setStatus(
        ""
    )

iso3201_Stn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306011)
)
iso3201_Stn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_enable.setStatus(
        ""
    )

iso3201_Stn_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306012)
)
iso3201_Stn_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_enable_fail.setStatus(
        ""
    )

iso3201_Stn_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306013)
)
iso3201_Stn_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_warn_status.setStatus(
        ""
    )

iso3201_Stn_inhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306014)
)
iso3201_Stn_inhibited.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_inhibited.setStatus(
        ""
    )

iso3201_Stn_poll_suspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306015)
)
iso3201_Stn_poll_suspended.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_poll_suspended.setStatus(
        ""
    )

iso3201_Stn_poll_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306016)
)
iso3201_Stn_poll_resumed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_poll_resumed.setStatus(
        ""
    )

iso3201_Stn_mnem_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306017)
)
iso3201_Stn_mnem_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_mnem_error.setStatus(
        ""
    )

iso3201_Stn_acall_exceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306018)
)
iso3201_Stn_acall_exceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_Stn_acall_exceed.setStatus(
        ""
    )

iso3201_local_commn_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306019)
)
iso3201_local_commn_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_local_commn_error.setStatus(
        ""
    )

iso3201_line_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306020)
)
iso3201_line_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_line_status.setStatus(
        ""
    )

iso3201_dq_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306021)
)
iso3201_dq_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_dq_error.setStatus(
        ""
    )

iso3201_data_mesg_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306022)
)
iso3201_data_mesg_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_data_mesg_error.setStatus(
        ""
    )

iso3201_poll_error_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306023)
)
iso3201_poll_error_clear.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_poll_error_clear.setStatus(
        ""
    )

iso3201_recd_error_mesg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306024)
)
iso3201_recd_error_mesg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_recd_error_mesg.setStatus(
        ""
    )

iso3201_station_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 306025)
)
iso3201_station_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iso3201_station_down.setStatus(
        ""
    )

gscPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308000)
)
gscPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_boot.setStatus(
        ""
    )

gscPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308001)
)
gscPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_boot_fail.setStatus(
        ""
    )

gscPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308002)
)
gscPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_disable.setStatus(
        ""
    )

gscPort_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308003)
)
gscPort_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_disable_fail.setStatus(
        ""
    )

gscPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308004)
)
gscPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_enable.setStatus(
        ""
    )

gscPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308005)
)
gscPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_enable_fail.setStatus(
        ""
    )

gscStn_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308006)
)
gscStn_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStn_boot.setStatus(
        ""
    )

gscStn_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308007)
)
gscStn_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStn_boot_fail.setStatus(
        ""
    )

gscStn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308008)
)
gscStn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStn_disable.setStatus(
        ""
    )

gscStn_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308009)
)
gscStn_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStn_disable_fail.setStatus(
        ""
    )

gscStn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308010)
)
gscStn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStn_enable.setStatus(
        ""
    )

gscStn_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308011)
)
gscStn_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStn_enable_fail.setStatus(
        ""
    )

gscPort_util_gt_thres = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308012)
)
gscPort_util_gt_thres.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_util_gt_thres.setStatus(
        ""
    )

gscPort_error_thres_exceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308013)
)
gscPort_error_thres_exceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_error_thres_exceed.setStatus(
        ""
    )

gscPort_busyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308014)
)
gscPort_busyout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_busyout.setStatus(
        ""
    )

gscPort_busyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308015)
)
gscPort_busyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_busyout_fail.setStatus(
        ""
    )

gscStnBusyout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308016)
)
gscStnBusyout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStnBusyout.setStatus(
        ""
    )

gscStn_busyout_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308017)
)
gscStn_busyout_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscStn_busyout_fail.setStatus(
        ""
    )

gscPort_status_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308018)
)
gscPort_status_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_status_warning.setStatus(
        ""
    )

gscPort_no_broadcast_stns = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308019)
)
gscPort_no_broadcast_stns.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gscPort_no_broadcast_stns.setStatus(
        ""
    )

gsc_memory_allocation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308020)
)
gsc_memory_allocation_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_memory_allocation_failed.setStatus(
        ""
    )

gsc_inter_character_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308021)
)
gsc_inter_character_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_inter_character_timeout.setStatus(
        ""
    )

gsc_checksum_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308022)
)
gsc_checksum_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_checksum_error.setStatus(
        ""
    )

gsc_frame_too_long = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308023)
)
gsc_frame_too_long.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_frame_too_long.setStatus(
        ""
    )

gsc_unescaped_char_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308024)
)
gsc_unescaped_char_found.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_unescaped_char_found.setStatus(
        ""
    )

gsc_unexpected_frame = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308025)
)
gsc_unexpected_frame.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_unexpected_frame.setStatus(
        ""
    )

gsc_frame_dropped_after_max_retr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308031)
)
gsc_frame_dropped_after_max_retr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_frame_dropped_after_max_retr.setStatus(
        ""
    )

gsc_device_not_responding = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308032)
)
gsc_device_not_responding.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_device_not_responding.setStatus(
        ""
    )

gsc_messages_lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308033)
)
gsc_messages_lost.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_messages_lost.setStatus(
        ""
    )

gsc_device_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308034)
)
gsc_device_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_device_active.setStatus(
        ""
    )

gsc_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308035)
)
gsc_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_link_up.setStatus(
        ""
    )

gsc_invalid_device_responding = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308036)
)
gsc_invalid_device_responding.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_invalid_device_responding.setStatus(
        ""
    )

gsc_solicit_abort = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308037)
)
gsc_solicit_abort.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_solicit_abort.setStatus(
        ""
    )

gsc_fsm_internal_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308038)
)
gsc_fsm_internal_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_fsm_internal_error.setStatus(
        ""
    )

gsc_wrong_message_address = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308039)
)
gsc_wrong_message_address.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_wrong_message_address.setStatus(
        ""
    )

gsc_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308040)
)
gsc_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_link_down.setStatus(
        ""
    )

gsc_autocall_retries_exhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308041)
)
gsc_autocall_retries_exhausted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_autocall_retries_exhausted.setStatus(
        ""
    )

gsc_station_not_configured = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308042)
)
gsc_station_not_configured.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_station_not_configured.setStatus(
        ""
    )

gsc_can_not_forward_station_disa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308043)
)
gsc_can_not_forward_station_disa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_can_not_forward_station_disa.setStatus(
        ""
    )

gsc_inactivity_time_out = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308044)
)
gsc_inactivity_time_out.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_inactivity_time_out.setStatus(
        ""
    )

gsc_inbound_link_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308045)
)
gsc_inbound_link_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_inbound_link_blocked.setStatus(
        ""
    )

gsc_inbound_link_unblocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308046)
)
gsc_inbound_link_unblocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_inbound_link_unblocked.setStatus(
        ""
    )

gsc_outbound_link_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308047)
)
gsc_outbound_link_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_outbound_link_blocked.setStatus(
        ""
    )

gsc_outbound_link_unblocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 308048)
)
gsc_outbound_link_unblocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    gsc_outbound_link_unblocked.setStatus(
        ""
    )

tpa_connection_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315000)
)
tpa_connection_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_up.setStatus(
        ""
    )

tpa_connection_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315001)
)
tpa_connection_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_down.setStatus(
        ""
    )

tpa_clearing_call_unexpected_q_b = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315002)
)
tpa_clearing_call_unexpected_q_b.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_clearing_call_unexpected_q_b.setStatus(
        ""
    )

tpa_sdlc_not_enough_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315003)
)
tpa_sdlc_not_enough_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_sdlc_not_enough_memory.setStatus(
        ""
    )

tpa_sdlc_idcm_or_tgo_does_not_ex = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315004)
)
tpa_sdlc_idcm_or_tgo_does_not_ex.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_sdlc_idcm_or_tgo_does_not_ex.setStatus(
        ""
    )

tpa_sdlc_idcm_not_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315005)
)
tpa_sdlc_idcm_not_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_sdlc_idcm_not_up.setStatus(
        ""
    )

tpa_clearing_call_bad_or_no_resp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315006)
)
tpa_clearing_call_bad_or_no_resp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_clearing_call_bad_or_no_resp.setStatus(
        ""
    )

tpa_received_ve_responsesense_da = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315007)
)
tpa_received_ve_responsesense_da.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_received_ve_responsesense_da.setStatus(
        ""
    )

tpa_retry_exceeded_for_sna_messa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315008)
)
tpa_retry_exceeded_for_sna_messa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_retry_exceeded_for_sna_messa.setStatus(
        ""
    )

tpa_lu_lu_session_cleared_cleari = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315009)
)
tpa_lu_lu_session_cleared_cleari.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_lu_lu_session_cleared_cleari.setStatus(
        ""
    )

tpa_pu_session_cleared_clearing = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315010)
)
tpa_pu_session_cleared_clearing.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_pu_session_cleared_clearing.setStatus(
        ""
    )

tpa_pu_session_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315011)
)
tpa_pu_session_activated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_pu_session_activated.setStatus(
        ""
    )

tpa_lu_session_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315012)
)
tpa_lu_session_activated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_lu_session_activated.setStatus(
        ""
    )

tpa_invalid_cp_packet_ru_th_rh = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315013)
)
tpa_invalid_cp_packet_ru_th_rh.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_invalid_cp_packet_ru_th_rh.setStatus(
        ""
    )

tpa_invalid_lu_packet_ru_th_rh = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315014)
)
tpa_invalid_lu_packet_ru_th_rh.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_invalid_lu_packet_ru_th_rh.setStatus(
        ""
    )

tpa_out_of_sequence_packet_event = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315015)
)
tpa_out_of_sequence_packet_event.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_out_of_sequence_packet_event.setStatus(
        ""
    )

tpa_retries_over_for_sending_bin = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 315016)
)
tpa_retries_over_for_sending_bin.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_retries_over_for_sending_bin.setStatus(
        ""
    )

tpa_tpa3270_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 316000)
)
tpa_tpa3270_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpa3270_connected.setStatus(
        ""
    )

tpa_tpa3270_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 316001)
)
tpa_tpa3270_disconnected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpa3270_disconnected.setStatus(
        ""
    )

tpdu_tpr_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317000)
)
tpdu_tpr_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_boot_complete.setStatus(
        ""
    )

tpdu_tpr_slot_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317001)
)
tpdu_tpr_slot_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_slot_boot_complete.setStatus(
        ""
    )

tpdu_tpr_boot_failure_number_of = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317002)
)
tpdu_tpr_boot_failure_number_of.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_boot_failure_number_of.setStatus(
        ""
    )

tpdu_tpr_slot_no_boot_failure_sl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317003)
)
tpdu_tpr_slot_no_boot_failure_sl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_slot_no_boot_failure_sl.setStatus(
        ""
    )

tpdu_tpr_init_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317004)
)
tpdu_tpr_init_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_init_failed.setStatus(
        ""
    )

tpdu_tpr_initslot_tpa_module_doe = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317005)
)
tpdu_tpr_initslot_tpa_module_doe.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_initslot_tpa_module_doe.setStatus(
        ""
    )

tpdu_tpr_initslot_tpa_module_ini = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317006)
)
tpdu_tpr_initslot_tpa_module_ini.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_initslot_tpa_module_ini.setStatus(
        ""
    )

tpdu_tpr_slot_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317007)
)
tpdu_tpr_slot_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_slot_enabled.setStatus(
        ""
    )

tpdu_tpr_slot_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317008)
)
tpdu_tpr_slot_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_slot_disabled.setStatus(
        ""
    )

tpdu_tpr_fwd_packet_for_dead_slo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317009)
)
tpdu_tpr_fwd_packet_for_dead_slo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_tpr_fwd_packet_for_dead_slo.setStatus(
        ""
    )

tpdu_session_is_in_progress_with = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317010)
)
tpdu_session_is_in_progress_with.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_is_in_progress_with.setStatus(
        ""
    )

tpdu_invalid_session_message_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317011)
)
tpdu_invalid_session_message_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_invalid_session_message_in.setStatus(
        ""
    )

tpdu_session_aborted_invalid_ses = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317012)
)
tpdu_session_aborted_invalid_ses.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_invalid_ses.setStatus(
        ""
    )

tpdu_session_aborted_got_session = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317013)
)
tpdu_session_aborted_got_session.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_got_session.setStatus(
        ""
    )

tpdu_session_aborted_got_invitat = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317014)
)
tpdu_session_aborted_got_invitat.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_got_invitat.setStatus(
        ""
    )

tpdu_session_aborted_got_illegal = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317015)
)
tpdu_session_aborted_got_illegal.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_got_illegal.setStatus(
        ""
    )

tpdu_session_aborted_data_when_o = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317016)
)
tpdu_session_aborted_data_when_o.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_data_when_o.setStatus(
        ""
    )

tpdu_session_aborted_got_call_cl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317017)
)
tpdu_session_aborted_got_call_cl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_got_call_cl.setStatus(
        ""
    )

tpdu_session_aborted_got_call_re = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317018)
)
tpdu_session_aborted_got_call_re.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_got_call_re.setStatus(
        ""
    )

tpdu_session_aborted_got_call_ac = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317019)
)
tpdu_session_aborted_got_call_ac.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_got_call_ac.setStatus(
        ""
    )

tpdu_session_aborted_got_data_fr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317020)
)
tpdu_session_aborted_got_data_fr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_aborted_got_data_fr.setStatus(
        ""
    )

tpdu_session_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317021)
)
tpdu_session_closed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_closed.setStatus(
        ""
    )

tpdu_session_established_with_sl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317022)
)
tpdu_session_established_with_sl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_established_with_sl.setStatus(
        ""
    )

tpdu_data_in_idle_state_from_slo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317023)
)
tpdu_data_in_idle_state_from_slo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_data_in_idle_state_from_slo.setStatus(
        ""
    )

tpdu_session_closed_got_call_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317024)
)
tpdu_session_closed_got_call_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_closed_got_call_req.setStatus(
        ""
    )

tpdu_session_closed_got_call_acc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317025)
)
tpdu_session_closed_got_call_acc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_closed_got_call_acc.setStatus(
        ""
    )

tpdu_session_closed_got_illegal = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317026)
)
tpdu_session_closed_got_illegal.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_closed_got_illegal.setStatus(
        ""
    )

tpdu_packet_allocation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317027)
)
tpdu_packet_allocation_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_packet_allocation_failed.setStatus(
        ""
    )

tpdu_not_enough_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317028)
)
tpdu_not_enough_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_not_enough_memory.setStatus(
        ""
    )

tpdu_session_closed_got_invalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317029)
)
tpdu_session_closed_got_invalid.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_closed_got_invalid.setStatus(
        ""
    )

tpdu_discarded_session_message_f = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317030)
)
tpdu_discarded_session_message_f.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_discarded_session_message_f.setStatus(
        ""
    )

tpdu_session_stataus_message_cou = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 317031)
)
tpdu_session_stataus_message_cou.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpdu_session_stataus_message_cou.setStatus(
        ""
    )

sppPort_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318000)
)
sppPort_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_boot.setStatus(
        ""
    )

sppPort_boot_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318001)
)
sppPort_boot_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_boot_fail.setStatus(
        ""
    )

sppPort_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318002)
)
sppPort_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_disable.setStatus(
        ""
    )

sppPort_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318003)
)
sppPort_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_disable_fail.setStatus(
        ""
    )

sppPort_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318004)
)
sppPort_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_enable.setStatus(
        ""
    )

sppPort_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318005)
)
sppPort_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_enable_fail.setStatus(
        ""
    )

sppStn_disable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318006)
)
sppStn_disable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppStn_disable.setStatus(
        ""
    )

sppStn_disable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318007)
)
sppStn_disable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppStn_disable_fail.setStatus(
        ""
    )

sppStn_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318008)
)
sppStn_enable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppStn_enable.setStatus(
        ""
    )

sppStn_enable_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318009)
)
sppStn_enable_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppStn_enable_fail.setStatus(
        ""
    )

sppPort_util_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318010)
)
sppPort_util_exceeded.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_util_exceeded.setStatus(
        ""
    )

sppPort_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318011)
)
sppPort_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_warn_status.setStatus(
        ""
    )

sppPort_bad_tid = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318012)
)
sppPort_bad_tid.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_bad_tid.setStatus(
        ""
    )

sppPort_bad_pid = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318013)
)
sppPort_bad_pid.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sppPort_bad_pid.setStatus(
        ""
    )

spp_stn_warn_status = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 318014)
)
spp_stn_warn_status.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    spp_stn_warn_status.setStatus(
        ""
    )

xlb_insufficient_memory_for_tran = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 321000)
)
xlb_insufficient_memory_for_tran.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xlb_insufficient_memory_for_tran.setStatus(
        ""
    )

xlb_module_initialized = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 321001)
)
xlb_module_initialized.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    xlb_module_initialized.setStatus(
        ""
    )

tpa_x25_not_enough_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 324000)
)
tpa_x25_not_enough_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_x25_not_enough_memory.setStatus(
        ""
    )

tpa_connection_up2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 324001)
)
tpa_connection_up2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_up2.setStatus(
        ""
    )

tpa_connection_down2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 324002)
)
tpa_connection_down2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_down2.setStatus(
        ""
    )

tpa_connection_is_in_progress = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 324003)
)
tpa_connection_is_in_progress.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_is_in_progress.setStatus(
        ""
    )

tpa_x25_idcm_or_tgo_does_not_exi = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 324004)
)
tpa_x25_idcm_or_tgo_does_not_exi.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_x25_idcm_or_tgo_does_not_exi.setStatus(
        ""
    )

tpa_x25_idcm_not_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 324005)
)
tpa_x25_idcm_not_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_x25_idcm_not_up.setStatus(
        ""
    )

tpa_maximum_autocall_attempts_fa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 324006)
)
tpa_maximum_autocall_attempts_fa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_maximum_autocall_attempts_fa.setStatus(
        ""
    )

igmp_1_rfcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327000)
)
igmp_1_rfcm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_1_rfcm.setStatus(
        ""
    )

igmp_2_igmp_module = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327001)
)
igmp_2_igmp_module.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_2_igmp_module.setStatus(
        ""
    )

igmp_3_mem_alloc_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327002)
)
igmp_3_mem_alloc_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_3_mem_alloc_failed.setStatus(
        ""
    )

igmp_4_module_not_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327003)
)
igmp_4_module_not_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_4_module_not_up.setStatus(
        ""
    )

igmp_5_packet_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327004)
)
igmp_5_packet_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_5_packet_error.setStatus(
        ""
    )

igmp_6_buffer_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327005)
)
igmp_6_buffer_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_6_buffer_failure.setStatus(
        ""
    )

igmp_7_group_insert_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327006)
)
igmp_7_group_insert_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_7_group_insert_fail.setStatus(
        ""
    )

igmp_8_debug_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327007)
)
igmp_8_debug_trap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_8_debug_trap.setStatus(
        ""
    )

igmp_9_packet_dropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327008)
)
igmp_9_packet_dropped.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_9_packet_dropped.setStatus(
        ""
    )

igmp_10_multicast_not_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327009)
)
igmp_10_multicast_not_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_10_multicast_not_enabled.setStatus(
        ""
    )

igmp_11_debug_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327010)
)
igmp_11_debug_trap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_11_debug_trap.setStatus(
        ""
    )

igmp_12_debug_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327011)
)
igmp_12_debug_trap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_12_debug_trap.setStatus(
        ""
    )

igmp_13_null_context_block = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327012)
)
igmp_13_null_context_block.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_13_null_context_block.setStatus(
        ""
    )

igmp_14_packet_received = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327013)
)
igmp_14_packet_received.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_14_packet_received.setStatus(
        ""
    )

igmp_15_membership_query = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327014)
)
igmp_15_membership_query.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_15_membership_query.setStatus(
        ""
    )

igmp_16_membership_report = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327015)
)
igmp_16_membership_report.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_16_membership_report.setStatus(
        ""
    )

igmp_17_membership_report_ver2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327016)
)
igmp_17_membership_report_ver2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_17_membership_report_ver2.setStatus(
        ""
    )

igmp_18_membership_leave_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327017)
)
igmp_18_membership_leave_msg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_18_membership_leave_msg.setStatus(
        ""
    )

igmp_19_unknown_group_member = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327018)
)
igmp_19_unknown_group_member.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_19_unknown_group_member.setStatus(
        ""
    )

igmp_20_unknown_packet = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327019)
)
igmp_20_unknown_packet.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_20_unknown_packet.setStatus(
        ""
    )

igmp_21_group_membership_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 327020)
)
igmp_21_group_membership_timeout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    igmp_21_group_membership_timeout.setStatus(
        ""
    )

router_dvmrp1_dvmrpinit_called_w = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 328000)
)
router_dvmrp1_dvmrpinit_called_w.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_dvmrp1_dvmrpinit_called_w.setStatus(
        ""
    )

router_dvmrp2_dvmrp_module_abort = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 328001)
)
router_dvmrp2_dvmrp_module_abort.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_dvmrp2_dvmrp_module_abort.setStatus(
        ""
    )

tpa_tcp_not_enough_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329000)
)
tpa_tcp_not_enough_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tcp_not_enough_memory.setStatus(
        ""
    )

tpa_connection_down22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329001)
)
tpa_connection_down22.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_down22.setStatus(
        ""
    )

tpa_tcp_tcp_does_not_exist = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329002)
)
tpa_tcp_tcp_does_not_exist.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tcp_tcp_does_not_exist.setStatus(
        ""
    )

tpa_tpatcpqueue_fullpacket_dropp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329003)
)
tpa_tpatcpqueue_fullpacket_dropp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcpqueue_fullpacket_dropp.setStatus(
        ""
    )

tpa_tpatcptcp_send_failed_connec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329004)
)
tpa_tpatcptcp_send_failed_connec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcptcp_send_failed_connec.setStatus(
        ""
    )

tpa_tpatcppacket_allocation_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329005)
)
tpa_tpatcppacket_allocation_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcppacket_allocation_fail.setStatus(
        ""
    )

tpa_tpatcpconnection_retries_ove = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329006)
)
tpa_tpatcpconnection_retries_ove.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcpconnection_retries_ove.setStatus(
        ""
    )

tpa_tpatcptcp_listen_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329007)
)
tpa_tpatcptcp_listen_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcptcp_listen_failed.setStatus(
        ""
    )

tpa_tpatcptcp_active_open_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329008)
)
tpa_tpatcptcp_active_open_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcptcp_active_open_failed.setStatus(
        ""
    )

tpa_tpatcppacket_with_m_bit_from = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329009)
)
tpa_tpatcppacket_with_m_bit_from.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcppacket_with_m_bit_from.setStatus(
        ""
    )

tpa_connection_up22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329010)
)
tpa_connection_up22.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_up22.setStatus(
        ""
    )

tpa_timeout_from_tcp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329011)
)
tpa_timeout_from_tcp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_timeout_from_tcp.setStatus(
        ""
    )

tpa_tpatcptcp_timeout_discarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 329012)
)
tpa_tpatcptcp_timeout_discarding.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpatcptcp_timeout_discarding.setStatus(
        ""
    )

tpa_connection_down222 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 330000)
)
tpa_connection_down222.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_down222.setStatus(
        ""
    )

tpa_udp_not_enough_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 330001)
)
tpa_udp_not_enough_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_udp_not_enough_memory.setStatus(
        ""
    )

tpa_udp_udp_does_not_exist = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 330002)
)
tpa_udp_udp_does_not_exist.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_udp_udp_does_not_exist.setStatus(
        ""
    )

tpa_udp_registration_with_udp_fa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 330003)
)
tpa_udp_registration_with_udp_fa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_udp_registration_with_udp_fa.setStatus(
        ""
    )

tpa_udp_registration_with_sip_fa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 330004)
)
tpa_udp_registration_with_sip_fa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_udp_registration_with_sip_fa.setStatus(
        ""
    )

sotcp_init_failed_insufficient_m = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331000)
)
sotcp_init_failed_insufficient_m.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_init_failed_insufficient_m.setStatus(
        ""
    )

sotcp_init_failed_software_absen = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331001)
)
sotcp_init_failed_software_absen.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_init_failed_software_absen.setStatus(
        ""
    )

sotcp_no_more_tcp_sessions = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331002)
)
sotcp_no_more_tcp_sessions.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_no_more_tcp_sessions.setStatus(
        ""
    )

sotcp_tcp_listen_failed_trying_a = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331003)
)
sotcp_tcp_listen_failed_trying_a.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_tcp_listen_failed_trying_a.setStatus(
        ""
    )

sotcp_tcp_receive_failed_session = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331004)
)
sotcp_tcp_receive_failed_session.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_tcp_receive_failed_session.setStatus(
        ""
    )

sotcp_invalid_packet = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331005)
)
sotcp_invalid_packet.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_invalid_packet.setStatus(
        ""
    )

sotcp_tcp_active_open_failed_wit = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331006)
)
sotcp_tcp_active_open_failed_wit.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_tcp_active_open_failed_wit.setStatus(
        ""
    )

sotcp_tcp_session_established_wi = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331007)
)
sotcp_tcp_session_established_wi.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_tcp_session_established_wi.setStatus(
        ""
    )

sotcp_memory_allocation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331008)
)
sotcp_memory_allocation_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_memory_allocation_failed.setStatus(
        ""
    )

sotcp_no_more_connections = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331009)
)
sotcp_no_more_connections.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_no_more_connections.setStatus(
        ""
    )

sotcp_tcp_session_timed_out_with = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331010)
)
sotcp_tcp_session_timed_out_with.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_tcp_session_timed_out_with.setStatus(
        ""
    )

sotcp_tcp_session_closed_by_the = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331011)
)
sotcp_tcp_session_closed_by_the.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_tcp_session_closed_by_the.setStatus(
        ""
    )

sotcp_session_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331012)
)
sotcp_session_closed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_session_closed.setStatus(
        ""
    )

sotcp_new_connection_with_connec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331013)
)
sotcp_new_connection_with_connec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_new_connection_with_connec.setStatus(
        ""
    )

sotcp_c_packet_allocation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331014)
)
sotcp_c_packet_allocation_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_c_packet_allocation_failed.setStatus(
        ""
    )

sotcp_c_serial_protocol_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331015)
)
sotcp_c_serial_protocol_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_c_serial_protocol_blocked.setStatus(
        ""
    )

sotcp_no_matching_ip_peer_for = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331016)
)
sotcp_no_matching_ip_peer_for.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_no_matching_ip_peer_for.setStatus(
        ""
    )

sotcp_queue_toward_tcp_blocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331017)
)
sotcp_queue_toward_tcp_blocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_queue_toward_tcp_blocked.setStatus(
        ""
    )

sotcp_queue_toward_tcp_unblocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331018)
)
sotcp_queue_toward_tcp_unblocked.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_queue_toward_tcp_unblocked.setStatus(
        ""
    )

sotcp_c_data_loss_due_to_queue_o = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331019)
)
sotcp_c_data_loss_due_to_queue_o.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_c_data_loss_due_to_queue_o.setStatus(
        ""
    )

sotcp_udp_registration_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331020)
)
sotcp_udp_registration_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_udp_registration_failure.setStatus(
        ""
    )

sotcp_c_remote_does_not_support = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331021)
)
sotcp_c_remote_does_not_support.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_c_remote_does_not_support.setStatus(
        ""
    )

sotcp_init_failed_idcm_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331022)
)
sotcp_init_failed_idcm_init_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_init_failed_idcm_init_fail.setStatus(
        ""
    )

sotcp_udp_module_absent_voice = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331023)
)
sotcp_udp_module_absent_voice.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp_udp_module_absent_voice.setStatus(
        ""
    )

sotcp331024_sotcp_ma = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331024)
)
sotcp331024_sotcp_ma.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp331024_sotcp_ma.setStatus(
        ""
    )

sotcp331025_sotcp_c = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331025)
)
sotcp331025_sotcp_c.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp331025_sotcp_c.setStatus(
        ""
    )

sotcp331026_sotcp_cr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 331026)
)
sotcp331026_sotcp_cr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    sotcp331026_sotcp_cr.setStatus(
        ""
    )

flash_multi_config_request = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 332000)
)
flash_multi_config_request.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    flash_multi_config_request.setStatus(
        ""
    )

vconfig_voice_port_failed_to_dow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 335000)
)
vconfig_voice_port_failed_to_dow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vconfig_voice_port_failed_to_dow.setStatus(
        ""
    )

vconfig_voice_port_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 335001)
)
vconfig_voice_port_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vconfig_voice_port_boot_complete.setStatus(
        ""
    )

vr_download_failed_insuf_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 339000)
)
vr_download_failed_insuf_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vr_download_failed_insuf_memory.setStatus(
        ""
    )

vr_download_failed_vsmio = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 339001)
)
vr_download_failed_vsmio.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vr_download_failed_vsmio.setStatus(
        ""
    )

vr339002_download_fa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 339002)
)
vr339002_download_fa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vr339002_download_fa.setStatus(
        ""
    )

vhardware340000_vhwv = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 340000)
)
vhardware340000_vhwv.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vhardware340000_vhwv.setStatus(
        ""
    )

idim_port_i430_dim_installed_on = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 341000)
)
idim_port_i430_dim_installed_on.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    idim_port_i430_dim_installed_on.setStatus(
        ""
    )

idim_i430_dim_in_sync = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 341001)
)
idim_i430_dim_in_sync.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    idim_i430_dim_in_sync.setStatus(
        ""
    )

idim_i430_dim_out_of_sync = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 341002)
)
idim_i430_dim_out_of_sync.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    idim_i430_dim_out_of_sync.setStatus(
        ""
    )

h323_internal_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342000)
)
h323_internal_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_internal_error.setStatus(
        ""
    )

h323_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342001)
)
h323_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_error.setStatus(
        ""
    )

h323_ip_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342002)
)
h323_ip_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_ip_error.setStatus(
        ""
    )

h323_h323 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342003)
)
h323_h323.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_h323.setStatus(
        ""
    )

h323_not_hdld_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342004)
)
h323_not_hdld_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_not_hdld_in.setStatus(
        ""
    )

h323_qsig_msg_not_handled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342005)
)
h323_qsig_msg_not_handled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_qsig_msg_not_handled.setStatus(
        ""
    )

h323_tcp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342006)
)
h323_tcp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_tcp.setStatus(
        ""
    )

h323_msd_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342007)
)
h323_msd_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_msd_error.setStatus(
        ""
    )

h323_rtp_discard = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342008)
)
h323_rtp_discard.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_rtp_discard.setStatus(
        ""
    )

h323_unknown_rtp_payload_type = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342009)
)
h323_unknown_rtp_payload_type.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_unknown_rtp_payload_type.setStatus(
        ""
    )

h323_sequence_numbers = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342010)
)
h323_sequence_numbers.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_sequence_numbers.setStatus(
        ""
    )

h323_ssrc_mismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342011)
)
h323_ssrc_mismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323_ssrc_mismatch.setStatus(
        ""
    )

h323342012_h323_unhandled_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342012)
)
h323342012_h323_unhandled_msg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323342012_h323_unhandled_msg.setStatus(
        ""
    )

h323342014_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 342014)
)
h323342014_info.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323342014_info.setStatus(
        ""
    )

tpa_tpa2780_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 343000)
)
tpa_tpa2780_connected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpa2780_connected.setStatus(
        ""
    )

tpa_tpa2780_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 343001)
)
tpa_tpa2780_disconnected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_tpa2780_disconnected.setStatus(
        ""
    )

tpa_connection_up222 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344000)
)
tpa_connection_up222.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_up222.setStatus(
        ""
    )

tpa_connection_down2222 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344001)
)
tpa_connection_down2222.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_down2222.setStatus(
        ""
    )

tpa_connection_is_in_progress2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344002)
)
tpa_connection_is_in_progress2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_connection_is_in_progress2.setStatus(
        ""
    )

tpa_clearing_call_remote_station = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344003)
)
tpa_clearing_call_remote_station.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_clearing_call_remote_station.setStatus(
        ""
    )

tpa_fra_not_enough_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344004)
)
tpa_fra_not_enough_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_fra_not_enough_memory.setStatus(
        ""
    )

tpa_fra_idcm_or_tgo_does_not_exi = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344005)
)
tpa_fra_idcm_or_tgo_does_not_exi.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_fra_idcm_or_tgo_does_not_exi.setStatus(
        ""
    )

tpa_fra_idcm_not_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344006)
)
tpa_fra_idcm_not_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_fra_idcm_not_up.setStatus(
        ""
    )

tpa_clearing_call_bad_response = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 344007)
)
tpa_clearing_call_bad_response.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tpa_clearing_call_bad_response.setStatus(
        ""
    )

router_udp_registration_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 347000)
)
router_udp_registration_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_udp_registration_failure.setStatus(
        ""
    )

router_proxy_ignoredip_interface = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 347001)
)
router_proxy_ignoredip_interface.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_proxy_ignoredip_interface.setStatus(
        ""
    )

router_proxy_ignored_has_duplica = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 347002)
)
router_proxy_ignored_has_duplica.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_proxy_ignored_has_duplica.setStatus(
        ""
    )

router_proxy_specifying_interfac = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 347003)
)
router_proxy_specifying_interfac.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_proxy_specifying_interfac.setStatus(
        ""
    )

router_proxies_restarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 347004)
)
router_proxies_restarted.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_proxies_restarted.setStatus(
        ""
    )

router_proxy_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 347005)
)
router_proxy_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_proxy_enabled.setStatus(
        ""
    )

router_proxy_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 347006)
)
router_proxy_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router_proxy_disabled.setStatus(
        ""
    )

ac100_port_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351000)
)
ac100_port_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_port_boot_complete.setStatus(
        ""
    )

ac100_port_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351001)
)
ac100_port_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_port_boot_failure.setStatus(
        ""
    )

ac100_port_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351002)
)
ac100_port_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_port_disabled.setStatus(
        ""
    )

ac100_port_disable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351003)
)
ac100_port_disable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_port_disable_failure.setStatus(
        ""
    )

ac100_port_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351004)
)
ac100_port_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_port_enabled.setStatus(
        ""
    )

ac100_port_enable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351005)
)
ac100_port_enable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_port_enable_failure.setStatus(
        ""
    )

ac100_port_status_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351006)
)
ac100_port_status_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_port_status_warning.setStatus(
        ""
    )

ac100_site_boot_complete = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351007)
)
ac100_site_boot_complete.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_boot_complete.setStatus(
        ""
    )

ac100_site_boot_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351008)
)
ac100_site_boot_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_boot_failure.setStatus(
        ""
    )

ac100_site_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351009)
)
ac100_site_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_disabled.setStatus(
        ""
    )

ac100_site_disable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351010)
)
ac100_site_disable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_disable_failure.setStatus(
        ""
    )

ac100_site_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351011)
)
ac100_site_enabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_enabled.setStatus(
        ""
    )

ac100_site_enable_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351012)
)
ac100_site_enable_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_enable_failure.setStatus(
        ""
    )

ac100_site_alive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351013)
)
ac100_site_alive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_alive.setStatus(
        ""
    )

ac100_site_dead = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351014)
)
ac100_site_dead.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_site_dead.setStatus(
        ""
    )

ac100_data_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351015)
)
ac100_data_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_data_error.setStatus(
        ""
    )

ac100_errmesg = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351016)
)
ac100_errmesg.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_errmesg.setStatus(
        ""
    )

ac100_duplicate_site_address = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 351017)
)
ac100_duplicate_site_address.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ac100_duplicate_site_address.setStatus(
        ""
    )

x25_bcug_table_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 352000)
)
x25_bcug_table_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25_bcug_table_overflow.setStatus(
        ""
    )

x25_bcug_duplicate_bcug_entries = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 352001)
)
x25_bcug_duplicate_bcug_entries.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    x25_bcug_duplicate_bcug_entries.setStatus(
        ""
    )

ccs_line_is_active007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 354000)
)
ccs_line_is_active007.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_line_is_active007.setStatus(
        ""
    )

ccs_line_is_inactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 354001)
)
ccs_line_is_inactive.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_line_is_inactive.setStatus(
        ""
    )

ccs_incompatible_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 354002)
)
ccs_incompatible_detected.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_incompatible_detected.setStatus(
        ""
    )

ccs_boot_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 354003)
)
ccs_boot_completed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_boot_completed.setStatus(
        ""
    )

ccs_connected_to_port = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 354005)
)
ccs_connected_to_port.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_connected_to_port.setStatus(
        ""
    )

ccs_disconnected_from_port_cause = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 354006)
)
ccs_disconnected_from_port_cause.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_disconnected_from_port_cause.setStatus(
        ""
    )

ccs_frame_sequencing_override = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 357000)
)
ccs_frame_sequencing_override.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_frame_sequencing_override.setStatus(
        ""
    )

ns360000_null_address = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 360000)
)
ns360000_null_address.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns360000_null_address.setStatus(
        ""
    )

ns360001_failed_to_map = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 360001)
)
ns360001_failed_to_map.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns360001_failed_to_map.setStatus(
        ""
    )

ns360002_get_add_map = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 360002)
)
ns360002_get_add_map.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns360002_get_add_map.setStatus(
        ""
    )

ns361000_x25_rch_tbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361000)
)
ns361000_x25_rch_tbl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361000_x25_rch_tbl.setStatus(
        ""
    )

ns361001_inccalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361001)
)
ns361001_inccalls.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361001_inccalls.setStatus(
        ""
    )

ns361002_deleted_link = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361002)
)
ns361002_deleted_link.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361002_deleted_link.setStatus(
        ""
    )

ns361003_entry_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361003)
)
ns361003_entry_created.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361003_entry_created.setStatus(
        ""
    )

ns361004_nos_apce_to_create_entry = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361004)
)
ns361004_nos_apce_to_create_entry.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361004_nos_apce_to_create_entry.setStatus(
        ""
    )

ns361005_duplicate_entry = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361005)
)
ns361005_duplicate_entry.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361005_duplicate_entry.setStatus(
        ""
    )

ns361006_getlink_found_conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361006)
)
ns361006_getlink_found_conn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361006_getlink_found_conn.setStatus(
        ""
    )

ns361007_statechange = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361007)
)
ns361007_statechange.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361007_statechange.setStatus(
        ""
    )

ns361008_deccalls_cleared_link = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361008)
)
ns361008_deccalls_cleared_link.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361008_deccalls_cleared_link.setStatus(
        ""
    )

ns361009_deccalls_one = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361009)
)
ns361009_deccalls_one.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361009_deccalls_one.setStatus(
        ""
    )

ns361010_deccalls_last_call = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361010)
)
ns361010_deccalls_last_call.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361010_deccalls_last_call.setStatus(
        ""
    )

ns361011_statechange_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 361011)
)
ns361011_statechange_fail.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ns361011_statechange_fail.setStatus(
        ""
    )

vbcst_state_not_found_for = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 364000)
)
vbcst_state_not_found_for.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vbcst_state_not_found_for.setStatus(
        ""
    )

vbcst_state_table_not_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 364001)
)
vbcst_state_table_not_found.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vbcst_state_table_not_found.setStatus(
        ""
    )

vbcst_no_entry_for_event_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 364002)
)
vbcst_no_entry_for_event_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vbcst_no_entry_for_event_in.setStatus(
        ""
    )

vbcst_process_event_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 364003)
)
vbcst_process_event_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vbcst_process_event_in.setStatus(
        ""
    )

vbcst_10_loops_for_event_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 364004)
)
vbcst_10_loops_for_event_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vbcst_10_loops_for_event_in.setStatus(
        ""
    )

vbcst_call_cleared_incompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 364005)
)
vbcst_call_cleared_incompatible.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vbcst_call_cleared_incompatible.setStatus(
        ""
    )

vbcst_call_cleared_incompatible_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 364006)
)
vbcst_call_cleared_incompatible_2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vbcst_call_cleared_incompatible_2.setStatus(
        ""
    )

t1e1vg_remote_loopback_in_progre = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 371001)
)
t1e1vg_remote_loopback_in_progre.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_remote_loopback_in_progre.setStatus(
        ""
    )

t1e1vg_remote_loopback_ended = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 371002)
)
t1e1vg_remote_loopback_ended.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_remote_loopback_ended.setStatus(
        ""
    )

vport_cvs_module_failed_initiali = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373001)
)
vport_cvs_module_failed_initiali.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_module_failed_initiali.setStatus(
        ""
    )

vport_cvs_no_digit_string_matchi = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373002)
)
vport_cvs_no_digit_string_matchi.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_no_digit_string_matchi.setStatus(
        ""
    )

vport_cvs_connection_to_terminat = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373003)
)
vport_cvs_connection_to_terminat.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_connection_to_terminat.setStatus(
        ""
    )

vport_cvs_invalid_execution_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373004)
)
vport_cvs_invalid_execution_line.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_invalid_execution_line.setStatus(
        ""
    )

vport_cvs_centralized_voice_swit = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373005)
)
vport_cvs_centralized_voice_swit.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_centralized_voice_swit.setStatus(
        ""
    )

vport_cvs_centralized_voice_swit2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373006)
)
vport_cvs_centralized_voice_swit2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_centralized_voice_swit2.setStatus(
        ""
    )

vport_cvs = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373007)
)
vport_cvs.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs.setStatus(
        ""
    )

vport_cvs_cvs_table_copy_complet = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373008)
)
vport_cvs_cvs_table_copy_complet.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_cvs_table_copy_complet.setStatus(
        ""
    )

vport_cvs_state_event_new_state = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 373009)
)
vport_cvs_state_event_new_state.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vport_cvs_state_event_new_state.setStatus(
        ""
    )

ccs_lapf_ctl_protocol_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 374000)
)
ccs_lapf_ctl_protocol_link_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_lapf_ctl_protocol_link_up.setStatus(
        ""
    )

ccs_lapf_ctl_protocol_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 374001)
)
ccs_lapf_ctl_protocol_link_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_lapf_ctl_protocol_link_down.setStatus(
        ""
    )

ccs_svc_station_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 374002)
)
ccs_svc_station_activated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_svc_station_activated.setStatus(
        ""
    )

ccs_svc_station_deactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 374003)
)
ccs_svc_station_deactivated.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ccs_svc_station_deactivated.setStatus(
        ""
    )

encrypt_simm_is_defective = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379000)
)
encrypt_simm_is_defective.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_simm_is_defective.setStatus(
        ""
    )

encrypt_insufficient_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379001)
)
encrypt_insufficient_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_insufficient_memory.setStatus(
        ""
    )

encrypt_established_session = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379002)
)
encrypt_established_session.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_established_session.setStatus(
        ""
    )

encrypt_cannot_create_session = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379003)
)
encrypt_cannot_create_session.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_cannot_create_session.setStatus(
        ""
    )

encrypt_failed_key_exchange = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379004)
)
encrypt_failed_key_exchange.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_failed_key_exchange.setStatus(
        ""
    )

encrypt_failed_key_exchange_no_response = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379005)
)
encrypt_failed_key_exchange_no_response.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_failed_key_exchange_no_response.setStatus(
        ""
    )

encrypt_node_key_not_configured = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379006)
)
encrypt_node_key_not_configured.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_node_key_not_configured.setStatus(
        ""
    )

encrypt_bad_base_keys_in_cmem = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379007)
)
encrypt_bad_base_keys_in_cmem.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_bad_base_keys_in_cmem.setStatus(
        ""
    )

encrypt_abnormal_ns_command = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379008)
)
encrypt_abnormal_ns_command.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_abnormal_ns_command.setStatus(
        ""
    )

encrypt_configuring_more_channels_than_hw_can_support = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379009)
)
encrypt_configuring_more_channels_than_hw_can_support.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_configuring_more_channels_than_hw_can_support.setStatus(
        ""
    )

encrypt_node_key_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379010)
)
encrypt_node_key_changed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_node_key_changed.setStatus(
        ""
    )

encrypt_base_key_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379011)
)
encrypt_base_key_changed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_base_key_changed.setStatus(
        ""
    )

encrypt_good_base_key_in_cmem = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379012)
)
encrypt_good_base_key_in_cmem.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_good_base_key_in_cmem.setStatus(
        ""
    )

encrypt_remote_reset_from_remote_encryption_peer = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379013)
)
encrypt_remote_reset_from_remote_encryption_peer.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_remote_reset_from_remote_encryption_peer.setStatus(
        ""
    )

encrypt_test_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379014)
)
encrypt_test_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_test_error.setStatus(
        ""
    )

encrypt_mis_configured = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379015)
)
encrypt_mis_configured.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_mis_configured.setStatus(
        ""
    )

encrypt_invalid_attempt_to_connect_ap_to_ap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379016)
)
encrypt_invalid_attempt_to_connect_ap_to_ap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_invalid_attempt_to_connect_ap_to_ap.setStatus(
        ""
    )

encrypt_booted_encryption_key = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379017)
)
encrypt_booted_encryption_key.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_booted_encryption_key.setStatus(
        ""
    )

encrypt_booted_encryption_profile = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379018)
)
encrypt_booted_encryption_profile.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_booted_encryption_profile.setStatus(
        ""
    )

encrypt_deleted_all_encryption_keys = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379019)
)
encrypt_deleted_all_encryption_keys.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_deleted_all_encryption_keys.setStatus(
        ""
    )

encrypt_data_encryption_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379020)
)
encrypt_data_encryption_disabled.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_data_encryption_disabled.setStatus(
        ""
    )

encrypt_IV_usage_forced_by_remote_peer = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379021)
)
encrypt_IV_usage_forced_by_remote_peer.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_IV_usage_forced_by_remote_peer.setStatus(
        ""
    )

encrypt_simm_bad_or_not_installed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 379022)
)
encrypt_simm_bad_or_not_installed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    encrypt_simm_bad_or_not_installed.setStatus(
        ""
    )

crc_last_two_chars = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 380000)
)
crc_last_two_chars.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    crc_last_two_chars.setStatus(
        ""
    )

tcpdriver_tcp_listen_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 381000)
)
tcpdriver_tcp_listen_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcpdriver_tcp_listen_failed.setStatus(
        ""
    )

tcpdriver_session_established = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 381001)
)
tcpdriver_session_established.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcpdriver_session_established.setStatus(
        ""
    )

tcpdriver_session_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 381002)
)
tcpdriver_session_closed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcpdriver_session_closed.setStatus(
        ""
    )

tcpdriver_l2_packet_size_exceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 381003)
)
tcpdriver_l2_packet_size_exceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcpdriver_l2_packet_size_exceed.setStatus(
        ""
    )

tcpdriver_tcp_packet_size_exceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 381004)
)
tcpdriver_tcp_packet_size_exceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcpdriver_tcp_packet_size_exceed.setStatus(
        ""
    )

tcpdriver_list_full = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 381005)
)
tcpdriver_list_full.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcpdriver_list_full.setStatus(
        ""
    )

tcpdriver_tcp_send_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 381006)
)
tcpdriver_tcp_send_failed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tcpdriver_tcp_send_failed.setStatus(
        ""
    )

dlcm_syserr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 382000)
)
dlcm_syserr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    dlcm_syserr.setStatus(
        ""
    )

appncm_appn_cm_syserr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 383000)
)
appncm_appn_cm_syserr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appncm_appn_cm_syserr.setStatus(
        ""
    )

appncm_insufficient_memory = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 383001)
)
appncm_insufficient_memory.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    appncm_insufficient_memory.setStatus(
        ""
    )

snap_syserr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384000)
)
snap_syserr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_syserr.setStatus(
        ""
    )

snap_snap = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384001)
)
snap_snap.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_snap.setStatus(
        ""
    )

snap_tp_started_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384002)
)
snap_tp_started_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_tp_started_req.setStatus(
        ""
    )

snap_rcv_alloc_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384003)
)
snap_rcv_alloc_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_rcv_alloc_req.setStatus(
        ""
    )

snap_tp_started_rsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384004)
)
snap_tp_started_rsp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_tp_started_rsp.setStatus(
        ""
    )

snap_rcv_alloc_rsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384005)
)
snap_rcv_alloc_rsp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_rcv_alloc_rsp.setStatus(
        ""
    )

snap_tp_ended_req = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384006)
)
snap_tp_ended_req.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_tp_ended_req.setStatus(
        ""
    )

snap_tp_ended_rsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 384007)
)
snap_tp_ended_rsp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    snap_tp_ended_rsp.setStatus(
        ""
    )

lu62map_error_in_appc_verb_resp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385000)
)
lu62map_error_in_appc_verb_resp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_error_in_appc_verb_resp.setStatus(
        ""
    )

lu62map_5494_retry_limit_reached = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385001)
)
lu62map_5494_retry_limit_reached.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_5494_retry_limit_reached.setStatus(
        ""
    )

lu62map_event_in_wrong_state = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385002)
)
lu62map_event_in_wrong_state.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_event_in_wrong_state.setStatus(
        ""
    )

lu62map_null_pointer_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385003)
)
lu62map_null_pointer_on_line.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_null_pointer_on_line.setStatus(
        ""
    )

lu62map_failed_to_get_snap_sock = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385004)
)
lu62map_failed_to_get_snap_sock.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_failed_to_get_snap_sock.setStatus(
        ""
    )

lu62map_received_unknown_sna_ev = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385005)
)
lu62map_received_unknown_sna_ev.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_unknown_sna_ev.setStatus(
        ""
    )

lu62map_failure_returned = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385006)
)
lu62map_failure_returned.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_failure_returned.setStatus(
        ""
    )

lu62map_incorrect_header = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385007)
)
lu62map_incorrect_header.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_incorrect_header.setStatus(
        ""
    )

lu62map_received_unknown_resp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385008)
)
lu62map_received_unknown_resp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_unknown_resp.setStatus(
        ""
    )

lu62map_5494_controller_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385009)
)
lu62map_5494_controller_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_5494_controller_up.setStatus(
        ""
    )

lu62map_5494_controller_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385010)
)
lu62map_5494_controller_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_5494_controller_down.setStatus(
        ""
    )

lu62map_received_unexpected_mess = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385011)
)
lu62map_received_unexpected_mess.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_unexpected_mess.setStatus(
        ""
    )

lu62map_received_unknown_tpid = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385012)
)
lu62map_received_unknown_tpid.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_unknown_tpid.setStatus(
        ""
    )

lu62map_received_too_many_recv = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385013)
)
lu62map_received_too_many_recv.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_too_many_recv.setStatus(
        ""
    )

lu62map_received_unknown_lu4lu7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385014)
)
lu62map_received_unknown_lu4lu7.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_unknown_lu4lu7.setStatus(
        ""
    )

lu62map_lu4lu7_incorrect_header = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385015)
)
lu62map_lu4lu7_incorrect_header.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_lu4lu7_incorrect_header.setStatus(
        ""
    )

lu62map_5494_workstation_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385016)
)
lu62map_5494_workstation_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_5494_workstation_down.setStatus(
        ""
    )

lu62map_5494_workstation_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385017)
)
lu62map_5494_workstation_up.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_5494_workstation_up.setStatus(
        ""
    )

lu62map_lu62map = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385018)
)
lu62map_lu62map.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_lu62map.setStatus(
        ""
    )

lu62map_dactlu_in_unexpected_state = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385019)
)
lu62map_dactlu_in_unexpected_state.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_dactlu_in_unexpected_state.setStatus(
        ""
    )

lu62map_received_lustat = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385020)
)
lu62map_received_lustat.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_lustat.setStatus(
        ""
    )

lu62map_received_actlu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385021)
)
lu62map_received_actlu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_actlu.setStatus(
        ""
    )

lu62map_bad_struct_id = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385022)
)
lu62map_bad_struct_id.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_bad_struct_id.setStatus(
        ""
    )

lu62map_received_nonpip_alloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385023)
)
lu62map_received_nonpip_alloc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_nonpip_alloc.setStatus(
        ""
    )

lu62map_received_data_from_qllc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385024)
)
lu62map_received_data_from_qllc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_received_data_from_qllc.setStatus(
        ""
    )

lu62map_null_pointer_on_line2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385025)
)
lu62map_null_pointer_on_line2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_null_pointer_on_line2.setStatus(
        ""
    )

lu62map_event_in_wrong_state2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385026)
)
lu62map_event_in_wrong_state2.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_event_in_wrong_state2.setStatus(
        ""
    )

lu62map_unknown_lu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385027)
)
lu62map_unknown_lu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map_unknown_lu.setStatus(
        ""
    )

lu62map385028_5494_station = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385028)
)
lu62map385028_5494_station.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385028_5494_station.setStatus(
        ""
    )

lu62map385029_5494_remote_conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385029)
)
lu62map385029_5494_remote_conn.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385029_5494_remote_conn.setStatus(
        ""
    )

lu62map385030_5494_remote_call = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385030)
)
lu62map385030_5494_remote_call.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385030_5494_remote_call.setStatus(
        ""
    )

lu62map385031_qllcpa = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385031)
)
lu62map385031_qllcpa.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385031_qllcpa.setStatus(
        ""
    )

lu62map385032_handle = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385032)
)
lu62map385032_handle.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385032_handle.setStatus(
        ""
    )

lu62map385033_sendou = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385033)
)
lu62map385033_sendou.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385033_sendou.setStatus(
        ""
    )

lu62map385034_purgeq = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385034)
)
lu62map385034_purgeq.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385034_purgeq.setStatus(
        ""
    )

lu62map385035_sendqu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385035)
)
lu62map385035_sendqu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385035_sendqu.setStatus(
        ""
    )

lu62map385036_sendup = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 385036)
)
lu62map385036_sendup.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    lu62map385036_sendup.setStatus(
        ""
    )

qos_not_operational = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 387000)
)
qos_not_operational.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qos_not_operational.setStatus(
        ""
    )

qos_memory_allocation_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 388000)
)
qos_memory_allocation_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qos_memory_allocation_failure.setStatus(
        ""
    )

qos_total_percentage_exceeds_100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 389000)
)
qos_total_percentage_exceeds_100.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qos_total_percentage_exceeds_100.setStatus(
        ""
    )

qos_total_percentage_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 389001)
)
qos_total_percentage_changed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qos_total_percentage_changed.setStatus(
        ""
    )

h323392000_h323_node = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 392000)
)
h323392000_h323_node.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323392000_h323_node.setStatus(
        ""
    )

h323392001_h323_node = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 392001)
)
h323392001_h323_node.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323392001_h323_node.setStatus(
        ""
    )

h323392002_no_h323_n = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 392002)
)
h323392002_no_h323_n.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    h323392002_no_h323_n.setStatus(
        ""
    )

iodrivers396000_port = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 396000)
)
iodrivers396000_port.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers396000_port.setStatus(
        ""
    )

iodrivers396001_unsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 396001)
)
iodrivers396001_unsu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers396001_unsu.setStatus(
        ""
    )

iodrivers396002_unsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 396002)
)
iodrivers396002_unsu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers396002_unsu.setStatus(
        ""
    )

iodrivers396003_erro = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 396003)
)
iodrivers396003_erro.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers396003_erro.setStatus(
        ""
    )

iodrivers396004_cloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 396004)
)
iodrivers396004_cloc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers396004_cloc.setStatus(
        ""
    )

iodrivers396005_tx_s = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 396005)
)
iodrivers396005_tx_s.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers396005_tx_s.setStatus(
        ""
    )

iodrivers396006_corr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 396006)
)
iodrivers396006_corr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers396006_corr.setStatus(
        ""
    )

qoskit400000_qos_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 400000)
)
qoskit400000_qos_failure.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qoskit400000_qos_failure.setStatus(
        ""
    )

qoskit400001_qos_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 400001)
)
qoskit400001_qos_warning.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qoskit400001_qos_warning.setStatus(
        ""
    )

qoskit402000_qos_sched_be = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 402000)
)
qoskit402000_qos_sched_be.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    qoskit402000_qos_sched_be.setStatus(
        ""
    )

pbr_rept_space_unavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403000)
)
pbr_rept_space_unavailable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_space_unavailable.setStatus(
        ""
    )

pbr_rept_ctp_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403001)
)
pbr_rept_ctp_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_ctp_error.setStatus(
        ""
    )

pbr_rept_flow_active = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403002)
)
pbr_rept_flow_active.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_flow_active.setStatus(
        ""
    )

pbr_rept_flow_dropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403003)
)
pbr_rept_flow_dropped.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_flow_dropped.setStatus(
        ""
    )

pbr_rept_flow_expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403004)
)
pbr_rept_flow_expired.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_flow_expired.setStatus(
        ""
    )

pbr_rept_flow_out_of_tow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403005)
)
pbr_rept_flow_out_of_tow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_flow_out_of_tow.setStatus(
        ""
    )

pbr_rept_flow_nxthop_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403006)
)
pbr_rept_flow_nxthop_down.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_flow_nxthop_down.setStatus(
        ""
    )

pbr_rept_flow_revert_to_primary = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403007)
)
pbr_rept_flow_revert_to_primary.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_flow_revert_to_primary.setStatus(
        ""
    )

pbr_rept_cache_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403008)
)
pbr_rept_cache_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_cache_cleared.setStatus(
        ""
    )

pbr_rept_cache_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 403009)
)
pbr_rept_cache_overflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    pbr_rept_cache_overflow.setStatus(
        ""
    )

ruihc_rept_nomem = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404000)
)
ruihc_rept_nomem.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_nomem.setStatus(
        ""
    )

ruihc_rept_ctxtoverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404001)
)
ruihc_rept_ctxtoverflow.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_ctxtoverflow.setStatus(
        ""
    )

ruihc_rept_newentryinctxt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404002)
)
ruihc_rept_newentryinctxt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_newentryinctxt.setStatus(
        ""
    )

ruihc_rept_compressionstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404003)
)
ruihc_rept_compressionstart.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_compressionstart.setStatus(
        ""
    )

ruihc_rept_ctxtentry_tmout = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404004)
)
ruihc_rept_ctxtentry_tmout.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_ctxtentry_tmout.setStatus(
        ""
    )

ruihc_rept_movetonegcache = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404005)
)
ruihc_rept_movetonegcache.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_movetonegcache.setStatus(
        ""
    )

ruihc_rept_ctxtstpktrcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404006)
)
ruihc_rept_ctxtstpktrcvd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_ctxtstpktrcvd.setStatus(
        ""
    )

ruihc_rept_ctxtnoexist = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404007)
)
ruihc_rept_ctxtnoexist.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_ctxtnoexist.setStatus(
        ""
    )

ruihc_rept_ctxtidmismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404008)
)
ruihc_rept_ctxtidmismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_ctxtidmismatch.setStatus(
        ""
    )

ruihc_rept_nomem4newpkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404009)
)
ruihc_rept_nomem4newpkt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_nomem4newpkt.setStatus(
        ""
    )

ruihc_rept_conntypmismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404010)
)
ruihc_rept_conntypmismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_conntypmismatch.setStatus(
        ""
    )

ruihc_rept_decompctxtnoexist = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404011)
)
ruihc_rept_decompctxtnoexist.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    ruihc_rept_decompctxtnoexist.setStatus(
        ""
    )

t1e1vg_HardwareFailed_OS = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404012)
)
t1e1vg_HardwareFailed_OS.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_HardwareFailed_OS.setStatus(
        ""
    )

t1e1vg_HardwareFailed_DRV = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404013)
)
t1e1vg_HardwareFailed_DRV.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_HardwareFailed_DRV.setStatus(
        ""
    )

t1e1vg_HardwareFailed_ME = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404014)
)
t1e1vg_HardwareFailed_ME.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_HardwareFailed_ME.setStatus(
        ""
    )

t1e1vg_HardwareFailed_DSL = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404015)
)
t1e1vg_HardwareFailed_DSL.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_HardwareFailed_DSL.setStatus(
        ""
    )

t1e1vg_ConfigurationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404016)
)
t1e1vg_ConfigurationMismatch.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_ConfigurationMismatch.setStatus(
        ""
    )

t1e1vg_CMEM_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404017)
)
t1e1vg_CMEM_error.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_CMEM_error.setStatus(
        ""
    )

t1e1vg_RemoteLoopback_InProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404018)
)
t1e1vg_RemoteLoopback_InProgress.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_RemoteLoopback_InProgress.setStatus(
        ""
    )

t1e1vg_RemoteLoopback_End = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404019)
)
t1e1vg_RemoteLoopback_End.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_RemoteLoopback_End.setStatus(
        ""
    )

t1e1vg_RAI_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404020)
)
t1e1vg_RAI_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_RAI_cleared.setStatus(
        ""
    )

t1e1vg_LOF_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404021)
)
t1e1vg_LOF_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_LOF_cleared.setStatus(
        ""
    )

t1e1vg_LOS_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404022)
)
t1e1vg_LOS_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_LOS_cleared.setStatus(
        ""
    )

t1e1vg_AIS_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404023)
)
t1e1vg_AIS_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_AIS_cleared.setStatus(
        ""
    )

t1e1vg_RAI_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404024)
)
t1e1vg_RAI_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_RAI_alarm.setStatus(
        ""
    )

t1e1vg_LOF_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404025)
)
t1e1vg_LOF_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_LOF_alarm.setStatus(
        ""
    )

t1e1vg_LOS_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404026)
)
t1e1vg_LOS_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_LOS_alarm.setStatus(
        ""
    )

t1e1vg_AIS_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404027)
)
t1e1vg_AIS_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_AIS_alarm.setStatus(
        ""
    )

t1e1vg_YELLOW_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404028)
)
t1e1vg_YELLOW_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_YELLOW_cleared.setStatus(
        ""
    )

t1e1vg_RED_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404029)
)
t1e1vg_RED_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_RED_cleared.setStatus(
        ""
    )

t1e1vg_BLUE_cleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404030)
)
t1e1vg_BLUE_cleared.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_BLUE_cleared.setStatus(
        ""
    )

t1e1vg_YELLOW_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404031)
)
t1e1vg_YELLOW_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_YELLOW_alarm.setStatus(
        ""
    )

t1e1vg_RED_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404032)
)
t1e1vg_RED_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_RED_alarm.setStatus(
        ""
    )

t1e1vg_BLUE_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404033)
)
t1e1vg_BLUE_alarm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_BLUE_alarm.setStatus(
        ""
    )

t1e1vg_LES_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404034)
)
t1e1vg_LES_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_LES_thresholdExceed.setStatus(
        ""
    )

t1e1vg_LCV_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404035)
)
t1e1vg_LCV_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_LCV_thresholdExceed.setStatus(
        ""
    )

t1e1vg_PCV_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404036)
)
t1e1vg_PCV_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_PCV_thresholdExceed.setStatus(
        ""
    )

t1e1vg_CSS_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404037)
)
t1e1vg_CSS_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_CSS_thresholdExceed.setStatus(
        ""
    )

t1e1vg_ES_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404038)
)
t1e1vg_ES_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_ES_thresholdExceed.setStatus(
        ""
    )

t1e1vg_BES_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404039)
)
t1e1vg_BES_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_BES_thresholdExceed.setStatus(
        ""
    )

t1e1vg_SES_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404040)
)
t1e1vg_SES_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_SES_thresholdExceed.setStatus(
        ""
    )

t1e1vg_SEFS_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404041)
)
t1e1vg_SEFS_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_SEFS_thresholdExceed.setStatus(
        ""
    )

t1e1vg_UAS_thresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404042)
)
t1e1vg_UAS_thresholdExceed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    t1e1vg_UAS_thresholdExceed.setStatus(
        ""
    )

tdm_clk_ModuleFail_OS = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404043)
)
tdm_clk_ModuleFail_OS.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdm_clk_ModuleFail_OS.setStatus(
        ""
    )

tdm_clk_NetworkClock_lost = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404044)
)
tdm_clk_NetworkClock_lost.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdm_clk_NetworkClock_lost.setStatus(
        ""
    )

tdm_clk_NetworkClock_dedrives = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404045)
)
tdm_clk_NetworkClock_dedrives.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdm_clk_NetworkClock_dedrives.setStatus(
        ""
    )

vpmt_ModuleFail_OS = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404046)
)
vpmt_ModuleFail_OS.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vpmt_ModuleFail_OS.setStatus(
        ""
    )

vpmt_ModuleFail_VPMT = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404047)
)
vpmt_ModuleFail_VPMT.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vpmt_ModuleFail_VPMT.setStatus(
        ""
    )

vpmt_ModuleFail_VPMT_CB = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404048)
)
vpmt_ModuleFail_VPMT_CB.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    vpmt_ModuleFail_VPMT_CB.setStatus(
        ""
    )

isdn_isdn_pri_ACTIVE = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404049)
)
isdn_isdn_pri_ACTIVE.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_isdn_pri_ACTIVE.setStatus(
        ""
    )

isdn_isdn_pri_INACTIVE = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404050)
)
isdn_isdn_pri_INACTIVE.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_isdn_pri_INACTIVE.setStatus(
        ""
    )

isdn_isdn_pri_CALL_IN_FROM_NUM = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404051)
)
isdn_isdn_pri_CALL_IN_FROM_NUM.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_isdn_pri_CALL_IN_FROM_NUM.setStatus(
        ""
    )

isdn_isdn_pri_CALL_IN_FROM_UNKNOWN = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404052)
)
isdn_isdn_pri_CALL_IN_FROM_UNKNOWN.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_isdn_pri_CALL_IN_FROM_UNKNOWN.setStatus(
        ""
    )

isdn_isdn_pri_CALL_OUT = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 404053)
)
isdn_isdn_pri_CALL_OUT.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    isdn_isdn_pri_CALL_OUT.setStatus(
        ""
    )

aam405000_port_boot = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405000)
)
aam405000_port_boot.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405000_port_boot.setStatus(
        ""
    )

aam405001_port_disab = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405001)
)
aam405001_port_disab.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405001_port_disab.setStatus(
        ""
    )

aam405002_port_enabl = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405002)
)
aam405002_port_enabl.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405002_port_enabl.setStatus(
        ""
    )

aam405003_port_utili = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405003)
)
aam405003_port_utili.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405003_port_utili.setStatus(
        ""
    )

aam405004_station_di = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405004)
)
aam405004_station_di.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405004_station_di.setStatus(
        ""
    )

aam405005_station_en = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405005)
)
aam405005_station_en.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405005_station_en.setStatus(
        ""
    )

aam405006_station_bo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405006)
)
aam405006_station_bo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405006_station_bo.setStatus(
        ""
    )

aam405007_port_statu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405007)
)
aam405007_port_statu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405007_port_statu.setStatus(
        ""
    )

aam405008_out_of_mem = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 405008)
)
aam405008_out_of_mem.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aam405008_out_of_mem.setStatus(
        ""
    )

aamsar407000_port_er = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407000)
)
aamsar407000_port_er.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407000_port_er.setStatus(
        ""
    )

aamsar407001_vcc_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407001)
)
aamsar407001_vcc_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407001_vcc_err.setStatus(
        ""
    )

aamsar407002_wrong_a = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407002)
)
aamsar407002_wrong_a.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407002_wrong_a.setStatus(
        ""
    )

aamsar407003_data_fr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407003)
)
aamsar407003_data_fr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407003_data_fr.setStatus(
        ""
    )

aamsar407004_aal5_cp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407004)
)
aamsar407004_aal5_cp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407004_aal5_cp.setStatus(
        ""
    )

aamsar407005_aal5_cp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407005)
)
aamsar407005_aal5_cp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407005_aal5_cp.setStatus(
        ""
    )

aamsar407006_aal5_cp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407006)
)
aamsar407006_aal5_cp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407006_aal5_cp.setStatus(
        ""
    )

aamsar407007_aal5_cp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407007)
)
aamsar407007_aal5_cp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407007_aal5_cp.setStatus(
        ""
    )

aamsar407008_port_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407008)
)
aamsar407008_port_in.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407008_port_in.setStatus(
        ""
    )

aamsar407009_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407009)
)
aamsar407009_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407009_unable.setStatus(
        ""
    )

aamsar407010_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407010)
)
aamsar407010_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407010_unable.setStatus(
        ""
    )

aamsar407011_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407011)
)
aamsar407011_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407011_unable.setStatus(
        ""
    )

aamsar407012_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407012)
)
aamsar407012_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407012_unable.setStatus(
        ""
    )

aamsar407013_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407013)
)
aamsar407013_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407013_unable.setStatus(
        ""
    )

aamsar407014_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407014)
)
aamsar407014_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407014_unable.setStatus(
        ""
    )

aamsar407015_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407015)
)
aamsar407015_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407015_unable.setStatus(
        ""
    )

aamsar407016_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407016)
)
aamsar407016_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407016_unable.setStatus(
        ""
    )

aamsar407017_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407017)
)
aamsar407017_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407017_unable.setStatus(
        ""
    )

aamsar407018_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407018)
)
aamsar407018_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407018_unable.setStatus(
        ""
    )

aamsar407019_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407019)
)
aamsar407019_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407019_unable.setStatus(
        ""
    )

aamsar407020_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407020)
)
aamsar407020_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407020_unable.setStatus(
        ""
    )

aamsar407021_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407021)
)
aamsar407021_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407021_unable.setStatus(
        ""
    )

aamsar407022_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407022)
)
aamsar407022_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407022_unable.setStatus(
        ""
    )

aamsar407023_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407023)
)
aamsar407023_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407023_unable.setStatus(
        ""
    )

aamsar407024_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407024)
)
aamsar407024_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407024_unable.setStatus(
        ""
    )

aamsar407025_vcc_ava = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407025)
)
aamsar407025_vcc_ava.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407025_vcc_ava.setStatus(
        ""
    )

aamsar407026_error_w = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407026)
)
aamsar407026_error_w.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407026_error_w.setStatus(
        ""
    )

aamsar407027_error_w = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407027)
)
aamsar407027_error_w.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407027_error_w.setStatus(
        ""
    )

aamsar407028_error_w = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407028)
)
aamsar407028_error_w.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407028_error_w.setStatus(
        ""
    )

aamsar407029_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407029)
)
aamsar407029_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407029_unable.setStatus(
        ""
    )

aamsar407030_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407030)
)
aamsar407030_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407030_unable.setStatus(
        ""
    )

aamsar407031_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407031)
)
aamsar407031_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407031_unable.setStatus(
        ""
    )

aamsar407032_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407032)
)
aamsar407032_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407032_unable.setStatus(
        ""
    )

aamsar407033_unable = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407033)
)
aamsar407033_unable.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407033_unable.setStatus(
        ""
    )

aamsar407034_wrong_p = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407034)
)
aamsar407034_wrong_p.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407034_wrong_p.setStatus(
        ""
    )

aamsar407035_wrong_v = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 407035)
)
aamsar407035_wrong_v.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    aamsar407035_wrong_v.setStatus(
        ""
    )

iodrivers411000_port = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 411000)
)
iodrivers411000_port.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers411000_port.setStatus(
        ""
    )

iodrivers411001_unsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 411001)
)
iodrivers411001_unsu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers411001_unsu.setStatus(
        ""
    )

iodrivers411002_unsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 411002)
)
iodrivers411002_unsu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers411002_unsu.setStatus(
        ""
    )

iodrivers411003_erro = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 411003)
)
iodrivers411003_erro.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers411003_erro.setStatus(
        ""
    )

iodrivers411004_cloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 411004)
)
iodrivers411004_cloc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers411004_cloc.setStatus(
        ""
    )

iodrivers411005_tx_s = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 411005)
)
iodrivers411005_tx_s.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers411005_tx_s.setStatus(
        ""
    )

iodrivers412000_port = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 412000)
)
iodrivers412000_port.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers412000_port.setStatus(
        ""
    )

iodrivers412001_unsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 412001)
)
iodrivers412001_unsu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers412001_unsu.setStatus(
        ""
    )

iodrivers412002_unsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 412002)
)
iodrivers412002_unsu.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers412002_unsu.setStatus(
        ""
    )

iodrivers412003_erro = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 412003)
)
iodrivers412003_erro.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers412003_erro.setStatus(
        ""
    )

iodrivers412004_cloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 412004)
)
iodrivers412004_cloc.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers412004_cloc.setStatus(
        ""
    )

iodrivers412005_tx_s = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 412005)
)
iodrivers412005_tx_s.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers412005_tx_s.setStatus(
        ""
    )

iodrivers413000_sgno = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413000)
)
iodrivers413000_sgno.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413000_sgno.setStatus(
        ""
    )

iodrivers413001_sgno = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413001)
)
iodrivers413001_sgno.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413001_sgno.setStatus(
        ""
    )

iodrivers413002_sgco = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413002)
)
iodrivers413002_sgco.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413002_sgco.setStatus(
        ""
    )

iodrivers413003_sgia = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413003)
)
iodrivers413003_sgia.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413003_sgia.setStatus(
        ""
    )

iodrivers413004_sgco = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413004)
)
iodrivers413004_sgco.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413004_sgco.setStatus(
        ""
    )

iodrivers413005_sgno = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413005)
)
iodrivers413005_sgno.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413005_sgno.setStatus(
        ""
    )

iodrivers413006_sgtx = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413006)
)
iodrivers413006_sgtx.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413006_sgtx.setStatus(
        ""
    )

iodrivers413007_sgex = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413007)
)
iodrivers413007_sgex.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413007_sgex.setStatus(
        ""
    )

iodrivers413008_sglo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413008)
)
iodrivers413008_sglo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413008_sglo.setStatus(
        ""
    )

iodrivers413009_sgex = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413009)
)
iodrivers413009_sgex.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413009_sgex.setStatus(
        ""
    )

iodrivers413010_sgex = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413010)
)
iodrivers413010_sgex.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413010_sgex.setStatus(
        ""
    )

iodrivers413011_sglo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413011)
)
iodrivers413011_sglo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413011_sglo.setStatus(
        ""
    )

iodrivers413012_sgex = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413012)
)
iodrivers413012_sgex.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413012_sgex.setStatus(
        ""
    )

iodrivers413013_sgin = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413013)
)
iodrivers413013_sgin.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413013_sgin.setStatus(
        ""
    )

iodrivers413014_sgin = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413014)
)
iodrivers413014_sgin.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413014_sgin.setStatus(
        ""
    )

iodrivers413015_sglo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413015)
)
iodrivers413015_sglo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413015_sglo.setStatus(
        ""
    )

iodrivers413016_sgtd = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413016)
)
iodrivers413016_sgtd.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413016_sgtd.setStatus(
        ""
    )

iodrivers413017_sgca = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413017)
)
iodrivers413017_sgca.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413017_sgca.setStatus(
        ""
    )

iodrivers413018_sgrx = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413018)
)
iodrivers413018_sgrx.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413018_sgrx.setStatus(
        ""
    )

iodrivers413019_sgtx = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413019)
)
iodrivers413019_sgtx.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413019_sgtx.setStatus(
        ""
    )

iodrivers413020_sglo = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413020)
)
iodrivers413020_sglo.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413020_sglo.setStatus(
        ""
    )

iodrivers413021_sgfp = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 413021)
)
iodrivers413021_sgfp.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    iodrivers413021_sgfp.setStatus(
        ""
    )

tdmclk415000_tdmclk = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 415000)
)
tdmclk415000_tdmclk.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tdmclk415000_tdmclk.setStatus(
        ""
    )

router417000_nat_pkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 417000)
)
router417000_nat_pkt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router417000_nat_pkt.setStatus(
        ""
    )

router417001_nat_add = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 417001)
)
router417001_nat_add.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router417001_nat_add.setStatus(
        ""
    )

router417002_nat_act = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 417002)
)
router417002_nat_act.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router417002_nat_act.setStatus(
        ""
    )

router417003_nat_pkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 417003)
)
router417003_nat_pkt.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router417003_nat_pkt.setStatus(
        ""
    )

wa421000_not_enough = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 421000)
)
wa421000_not_enough.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wa421000_not_enough.setStatus(
        ""
    )

wa421001_unsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 421001)
)
wa421001_unsupported.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wa421001_unsupported.setStatus(
        ""
    )

wa421002_unsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 421002)
)
wa421002_unsupported.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wa421002_unsupported.setStatus(
        ""
    )

wa421003_unsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 421003)
)
wa421003_unsupported.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wa421003_unsupported.setStatus(
        ""
    )

wa421004_bridged_or = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 421004)
)
wa421004_bridged_or.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    wa421004_bridged_or.setStatus(
        ""
    )

router422000_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422000)
)
router422000_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422000_ipoatm.setStatus(
        ""
    )

router422001_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422001)
)
router422001_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422001_ipoatm.setStatus(
        ""
    )

router422002_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422002)
)
router422002_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422002_ipoatm.setStatus(
        ""
    )

router422003_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422003)
)
router422003_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422003_ipoatm.setStatus(
        ""
    )

router422004_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422004)
)
router422004_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422004_ipoatm.setStatus(
        ""
    )

router422005_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422005)
)
router422005_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422005_ipoatm.setStatus(
        ""
    )

router422006_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422006)
)
router422006_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422006_ipoatm.setStatus(
        ""
    )

router422007_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422007)
)
router422007_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422007_ipoatm.setStatus(
        ""
    )

router422008_ipoatm = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 422008)
)
router422008_ipoatm.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    router422008_ipoatm.setStatus(
        ""
    )

tnl_nomem_rec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426000)
)
tnl_nomem_rec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_nomem_rec.setStatus(
        ""
    )

tnl_duplicate_rec = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426001)
)
tnl_duplicate_rec.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_duplicate_rec.setStatus(
        ""
    )

tnl_improper_config = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426002)
)
tnl_improper_config.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_improper_config.setStatus(
        ""
    )

tnl_pck = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426003)
)
tnl_pck.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_pck.setStatus(
        ""
    )

tnl_chan_open = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426004)
)
tnl_chan_open.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_chan_open.setStatus(
        ""
    )

tnl_chan_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426005)
)
tnl_chan_closed.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_chan_closed.setStatus(
        ""
    )

tnl_encr_pck = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426006)
)
tnl_encr_pck.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_encr_pck.setStatus(
        ""
    )

tnl_decr_pck = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426007)
)
tnl_decr_pck.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_decr_pck.setStatus(
        ""
    )

tnl_queue_full = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426008)
)
tnl_queue_full.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_queue_full.setStatus(
        ""
    )

tnl_wrong_encrpck = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426009)
)
tnl_wrong_encrpck.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_wrong_encrpck.setStatus(
        ""
    )

tnl_queue_flush = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426010)
)
tnl_queue_flush.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_queue_flush.setStatus(
        ""
    )

tnl_cache_del = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426011)
)
tnl_cache_del.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_cache_del.setStatus(
        ""
    )

tnl_cache_clr = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426012)
)
tnl_cache_clr.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_cache_clr.setStatus(
        ""
    )

tnl_cache_garbage = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426013)
)
tnl_cache_garbage.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_cache_garbage.setStatus(
        ""
    )

tnl_gen = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426014)
)
tnl_gen.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_gen.setStatus(
        ""
    )

tnl_cache_notim = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426015)
)
tnl_cache_notim.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_cache_notim.setStatus(
        ""
    )

tnl_brdg_mod_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426016)
)
tnl_brdg_mod_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_brdg_mod_err.setStatus(
        ""
    )

tnl_seq_no_debug = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426017)
)
tnl_seq_no_debug.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_seq_no_debug.setStatus(
        ""
    )

tnl_ruihc_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426018)
)
tnl_ruihc_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_ruihc_err.setStatus(
        ""
    )

tnl_encr_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 0, 426019)
)
tnl_encr_err.setObjects(
    ("CDX-6500-COMMON-MIB", "cdx6500SNMPLastTrap")
)
if mibBuilder.loadTexts:
    tnl_encr_err.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISG-NSD-COMMON-TRAPS",
    **{"Counter16": Counter16,
       "Counter8": Counter8,
       "MacAddress": MacAddress,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "code-power-supply-down": code_power_supply_down,
       "code-power-supply-up": code_power_supply_up,
       "code-fan-failed": code_fan_failed,
       "code-flash-checksum-error": code_flash_checksum_error,
       "code-flash-checksum-ok": code_flash_checksum_ok,
       "code-error-detected": code_error_detected,
       "code1006-dram-code-c": code1006_dram_code_c,
       "code1007-dram-code-c": code1007_dram_code_c,
       "code-dram-idata-c": code_dram_idata_c,
       "code-dram-idata-reload-success": code_dram_idata_reload_success,
       "code-dram-idata-reload-failure": code_dram_idata_reload_failure,
       "code-dram-idata-sig-array": code_dram_idata_sig_array,
       "port-boot-complete": port_boot_complete,
       "port-boot-failure": port_boot_failure,
       "channel-boot-complete": channel_boot_complete,
       "channel-boot-failure": channel_boot_failure,
       "code-port-boot-to-new-port-failu": code_port_boot_to_new_port_failu,
       "code-port-insufficient-dynamic-m": code_port_insufficient_dynamic_m,
       "code2006-port-dynami": code2006_port_dynami,
       "code2007-port-dynami": code2007_port_dynami,
       "code2008-port-dynami": code2008_port_dynami,
       "code2009-port-failur": code2009_port_failur,
       "buff-pool-util-exceeded": buff_pool_util_exceeded,
       "lib-lan-congestion-start": lib_lan_congestion_start,
       "lib-lan-congestion-end": lib_lan_congestion_end,
       "cmem-corrupted": cmem_corrupted,
       "cmem-recovered": cmem_recovered,
       "cmem-compression-fail": cmem_compression_fail,
       "code-no-memory-tftp-upload-to-sc": code_no_memory_tftp_upload_to_sc,
       "ctp-wrong-task-level": ctp_wrong_task_level,
       "ctp-help-msg-overflow": ctp_help_msg_overflow,
       "eiaPort-handshake-incomplete": eiaPort_handshake_incomplete,
       "eiaPort-handshake-complete": eiaPort_handshake_complete,
       "v25bis-proto-mismatch": v25bis_proto_mismatch,
       "v25bis-call-fail": v25bis_call_fail,
       "v25bis-error": v25bis_error,
       "v25bis-unknown-error": v25bis_unknown_error,
       "sw56k-calling": sw56k_calling,
       "sw56k-connected": sw56k_connected,
       "sw56k-call-fail": sw56k_call_fail,
       "sw56k-incall-answered": sw56k_incall_answered,
       "sw56k-no-phone-num": sw56k_no_phone_num,
       "sw56k-incall-ignored": sw56k_incall_ignored,
       "sw56k-disconnect-fail": sw56k_disconnect_fail,
       "sw56k-line-out-of-service": sw56k_line_out_of_service,
       "sw56k-line-in-service": sw56k_line_in_service,
       "sw56k-call-disconnected": sw56k_call_disconnected,
       "sw56k-in-channel-loopback": sw56k_in_channel_loopback,
       "sw56k-in-dsu-loopback": sw56k_in_dsu_loopback,
       "x32-dial-in-not-allowed": x32_dial_in_not_allowed,
       "x32-dial-out-not-allowed": x32_dial_out_not_allowed,
       "x32-modem-faulty": x32_modem_faulty,
       "x32-phone-num-busy": x32_phone_num_busy,
       "x32-phone-line-busy": x32_phone_line_busy,
       "x32-incompat-destination": x32_incompat_destination,
       "eia6025-port-dial-nu": eia6025_port_dial_nu,
       "eia6026-port-modem-f": eia6026_port_modem_f,
       "eia6027-port-modem-f": eia6027_port_modem_f,
       "eia6028-port-modem-f": eia6028_port_modem_f,
       "eia6029-port-incomin": eia6029_port_incomin,
       "eia6030-port-no-dial": eia6030_port_no_dial,
       "eia6031-port-could-n": eia6031_port_could_n,
       "code-software-failure-logged": code_software_failure_logged,
       "code9001-task-rescue": code9001_task_rescue,
       "code9002-rescued-msg": code9002_rescued_msg,
       "code9003-rescued-msg": code9003_rescued_msg,
       "reports-lost": reports_lost,
       "report-log-cleared": report_log_cleared,
       "vc-connected": vc_connected,
       "vc-disconnected": vc_disconnected,
       "pvc-duplication": pvc_duplication,
       "pvc-not-connected": pvc_not_connected,
       "node-boot-for-rout-tables": node_boot_for_rout_tables,
       "node-boot-for-pvc": node_boot_for_pvc,
       "rout-call-from-to-cleared-by-rou": rout_call_from_to_cleared_by_rou,
       "rout16007-routproclb-ss-rout-down": rout16007_routproclb_ss_rout_down,
       "rout16008-routproclb-rout-not-found": rout16008_routproclb_rout_not_found,
       "rout16009-routproclb-forwarding-call-req": rout16009_routproclb_forwarding_call_req,
       "rout16010-routproclb-ss-rout-up": rout16010_routproclb_ss_rout_up,
       "rout16011-routproclb-retry-calls": rout16011_routproclb_retry_calls,
       "rout16012-rout-old-call-req": rout16012_rout_old_call_req,
       "rout16013-rout-call-req": rout16013_rout_call_req,
       "rout16014-rout-call-acc": rout16014_rout_call_acc,
       "rout16015-rout-local-clear": rout16015_rout_local_clear,
       "rout16016-rout-clear-req": rout16016_rout_clear_req,
       "rout16017-rout-clear-call-accept": rout16017_rout_clear_call_accept,
       "rout16018-routclearcr": rout16018_routclearcr,
       "rout16019-rout-main": rout16019_rout_main,
       "rout16020-rout-socksel": rout16020_rout_socksel,
       "rout16021-call-routi": rout16021_call_routi,
       "rout16022-routmain-p": rout16022_routmain_p,
       "rout16023-packet-poi": rout16023_packet_poi,
       "port-util-exceeded": port_util_exceeded,
       "port-err-count-exceeded": port_err_count_exceeded,
       "cpu-util-exceeded": cpu_util_exceeded,
       "node-reset": node_reset,
       "watchdog-timeout-node-reset": watchdog_timeout_node_reset,
       "node-boot": node_boot,
       "crash-node-reset": crash_node_reset,
       "debug-node-reset": debug_node_reset,
       "node-coldstart": node_coldstart,
       "node-warmstart": node_warmstart,
       "mboard-diag-fail": mboard_diag_fail,
       "board-diag-fail": board_diag_fail,
       "port-diag-fail": port_diag_fail,
       "missing-dim": missing_dim,
       "flash-simm-diag-fail": flash_simm_diag_fail,
       "insufficient-ram": insufficient_ram,
       "port-boot-fail": port_boot_fail,
       "local-dram-exhausted": local_dram_exhausted,
       "bad-cmem-battery": bad_cmem_battery,
       "unexpected-interrupt": unexpected_interrupt,
       "code-port-insuffficient-dynamic": code_port_insuffficient_dynamic,
       "code-node-reset-with-default-pas": code_node_reset_with_default_pas,
       "cougar-reset-with-default-pas": cougar_reset_with_default_pas,
       "code19020-ctp-pad-setting-overridden": code19020_ctp_pad_setting_overridden,
       "node-boot-for-mnem": node_boot_for_mnem,
       "software-failure": software_failure,
       "billing-records-lost": billing_records_lost,
       "dl-attempting-download": dl_attempting_download,
       "dl-recvd-invalid-rec": dl_recvd_invalid_rec,
       "dl-recvd-no-rec": dl_recvd_no_rec,
       "dl-recvd-invalid-len-rec": dl_recvd_invalid_len_rec,
       "dl-recvd-invalid-chksum-rec": dl_recvd_invalid_chksum_rec,
       "dl-download-complete": dl_download_complete,
       "ds-conn-timeout": ds_conn_timeout,
       "dl-invl-address": dl_invl_address,
       "ds-download-complete": ds_download_complete,
       "ds-loading": ds_loading,
       "ds-incompat-cpu": ds_incompat_cpu,
       "dl-invl-image-addr": dl_invl_image_addr,
       "dl-flash-erase-fail": dl_flash_erase_fail,
       "dl-no-conf-server": dl_no_conf_server,
       "dl-flash-write-fail": dl_flash_write_fail,
       "ds-flash-read-fail": ds_flash_read_fail,
       "dl-software-copy-fail": dl_software_copy_fail,
       "ds-software-send-fail": ds_software_send_fail,
       "dl-download-in-progress-err": dl_download_in_progress_err,
       "ds-flash-bank-unavail": ds_flash_bank_unavail,
       "ds-download-in-progress-err": ds_download_in_progress_err,
       "dl-copying-to-flash": dl_copying_to_flash,
       "ds-no-mnemonic": ds_no_mnemonic,
       "dlsv-flash-has-been-corrupted": dlsv_flash_has_been_corrupted,
       "nullPort-boot": nullPort_boot,
       "nullPort-boot-fail": nullPort_boot_fail,
       "nullPort-disable": nullPort_disable,
       "nullPort-enable": nullPort_enable,
       "async-iodrivers-port-error-thres": async_iodrivers_port_error_thres,
       "async-iodrivers-unsupported-speed": async_iodrivers_unsupported_speed,
       "bop-iodrivers-port-error-count-thres": bop_iodrivers_port_error_count_thres,
       "bop-iodrivers-unsupported-speed-oper": bop_iodrivers_unsupported_speed_oper,
       "lapb-link-down": lapb_link_down,
       "lapb-disc-received": lapb_disc_received,
       "lapb-bad-frame-type": lapb_bad_frame_type,
       "lapb-address-error": lapb_address_error,
       "lapb-bad-frame-len": lapb_bad_frame_len,
       "lapb-extend-seq-frmr": lapb_extend_seq_frmr,
       "lapb-norm-seq-frmr": lapb_norm_seq_frmr,
       "lapb-link-up": lapb_link_up,
       "lapb-link-blocked": lapb_link_blocked,
       "lapb-bad-n-r": lapb_bad_n_r,
       "lapb-backup-activated": lapb_backup_activated,
       "lapb-extend-bad-frame-type": lapb_extend_bad_frame_type,
       "lapb-access-link-down": lapb_access_link_down,
       "lapb-access-link-up": lapb_access_link_up,
       "lapb-ovsize-frame": lapb_ovsize_frame,
       "hdlc-link-down": hdlc_link_down,
       "hdlc-disc-received": hdlc_disc_received,
       "hdlc-bad-frame-type": hdlc_bad_frame_type,
       "hdlc-address-error": hdlc_address_error,
       "hdlc-bad-frame-len": hdlc_bad_frame_len,
       "hdlc-extend-seq-frmr": hdlc_extend_seq_frmr,
       "hdlc-norm-seq-frmr": hdlc_norm_seq_frmr,
       "hdlc-link-up": hdlc_link_up,
       "hdlc-line-blocked": hdlc_line_blocked,
       "hdlc-bad-n-r": hdlc_bad_n_r,
       "hdlc-backup-activated": hdlc_backup_activated,
       "hdlc-extend-bad-frame-type": hdlc_extend_bad_frame_type,
       "hdlc-access-link-down": hdlc_access_link_down,
       "hdlc-access-link-up": hdlc_access_link_up,
       "hdlc-ovsize-frame": hdlc_ovsize_frame,
       "apad-input-buf-overrun": apad_input_buf_overrun,
       "apad-hpEnqack-timeout": apad_hpEnqack_timeout,
       "apad-bcst-overrun": apad_bcst_overrun,
       "apad-unauth-polled-async": apad_unauth_polled_async,
       "apad-x28-overrun": apad_x28_overrun,
       "apad-outputbuf-overrun": apad_outputbuf_overrun,
       "apad-stpa-frame-dropped": apad_stpa_frame_dropped,
       "pad-violations-port-disconnected": pad_violations_port_disconnected,
       "pad-violations-port-locked": pad_violations_port_locked,
       "pad-violations-port-degraded": pad_violations_port_degraded,
       "pad-violations-no-action": pad_violations_no_action,
       "x25L3-pkt-lvl-restart": x25L3_pkt_lvl_restart,
       "x25L3-no-response": x25L3_no_response,
       "x25L3-channel-reset-recv": x25L3_channel_reset_recv,
       "x25L3-rept-bad-p-k": x25L3_rept_bad_p_k,
       "x25L3-bad-p-r": x25L3_bad_p_r,
       "x25L3-bad-p-s": x25L3_bad_p_s,
       "x25L3-pvc-not-connected": x25L3_pvc_not_connected,
       "x25L3-unassigned-lcn": x25L3_unassigned_lcn,
       "x25L3-bad-pkt-len": x25L3_bad_pkt_len,
       "x25L3-bad-pkt-type": x25L3_bad_pkt_type,
       "x25L3-bcst-overrun": x25L3_bcst_overrun,
       "x25L3-input-overrun": x25L3_input_overrun,
       "x25L3-tp-lvl-blocked": x25L3_tp_lvl_blocked,
       "x25L3-tp-all-lvls-blocked": x25L3_tp_all_lvls_blocked,
       "x25L3-insuff-memory": x25L3_insuff_memory,
       "x25L3-output-overrun": x25L3_output_overrun,
       "x2546016-bad-ccbptr": x2546016_bad_ccbptr,
       "padPort-boot": padPort_boot,
       "padPort-boot-fail": padPort_boot_fail,
       "padPort-disable": padPort_disable,
       "padPort-enable": padPort_enable,
       "padPort-util-exceeded": padPort_util_exceeded,
       "padPort-err-count-exceeded": padPort_err_count_exceeded,
       "padPort-warn-status": padPort_warn_status,
       "x25Port-boot": x25Port_boot,
       "x25Port-boot-fail": x25Port_boot_fail,
       "x25Port-disable": x25Port_disable,
       "x25Port-enable": x25Port_enable,
       "x25Port-util-exceeded": x25Port_util_exceeded,
       "x25Port-warn-status": x25Port_warn_status,
       "x25Port-pkt-size-warning": x25Port_pkt_size_warning,
       "bsc2780Port-boot": bsc2780Port_boot,
       "bsc2780Port-boot-fail": bsc2780Port_boot_fail,
       "bsc2780Port-disable": bsc2780Port_disable,
       "bsc2780Port-enable": bsc2780Port_enable,
       "bsc2780Port-enable-fail": bsc2780Port_enable_fail,
       "bsc2780Port-ses-rej": bsc2780Port_ses_rej,
       "bsc2780Port-line-error": bsc2780Port_line_error,
       "bsc2780Port-util-exceeded": bsc2780Port_util_exceeded,
       "bsc2780Port-warn-status": bsc2780Port_warn_status,
       "bsc3270Port-boot": bsc3270Port_boot,
       "bsc3270Port-boot-fail": bsc3270Port_boot_fail,
       "bsc3270Port-disable": bsc3270Port_disable,
       "bsc3270Port-enable": bsc3270Port_enable,
       "bsc3270Port-enable-fail": bsc3270Port_enable_fail,
       "bsc3270Port-inbound-err": bsc3270Port_inbound_err,
       "bsc3270Port-outbound-err": bsc3270Port_outbound_err,
       "bsc3270Port-line-down": bsc3270Port_line_down,
       "bsc3270Port-line-up": bsc3270Port_line_up,
       "bsc3270Port-dev-down": bsc3270Port_dev_down,
       "bsc3270Port-dev-up": bsc3270Port_dev_up,
       "bsc3270Port-warn-status": bsc3270Port_warn_status,
       "bsc3270-device-enabled": bsc3270_device_enabled,
       "bsc3270-device-disabled": bsc3270_device_disabled,
       "bsc3270-device-enable-failure": bsc3270_device_enable_failure,
       "bsc3270-device-disable-failure": bsc3270_device_disable_failure,
       "bsc327057016-device": bsc327057016_device,
       "bsc327057017-device": bsc327057017_device,
       "dsp3270-possible-data-loss": dsp3270_possible_data_loss,
       "cop-iodrivers-port-error-thres": cop_iodrivers_port_error_thres,
       "disk-bytes-loaded-from-nso-disk": disk_bytes_loaded_from_nso_disk,
       "disk-cannot-read-from-nso-slot": disk_cannot_read_from_nso_slot,
       "mx25L2-stn-up": mx25L2_stn_up,
       "mx25L2-multiple-masters": mx25L2_multiple_masters,
       "mx25L2-bad-frame-type": mx25L2_bad_frame_type,
       "mx25L2-norm-seq-frmr": mx25L2_norm_seq_frmr,
       "mx25L2-addr-error": mx25L2_addr_error,
       "mx25L2-master-polled-early": mx25L2_master_polled_early,
       "mx25L2-link-up": mx25L2_link_up,
       "mx25L2-bad-n-r": mx25L2_bad_n_r,
       "mx25L2-bad-frame-len": mx25L2_bad_frame_len,
       "mx25L2-stn-down": mx25L2_stn_down,
       "mx25L2-link-down": mx25L2_link_down,
       "mx25Port-boot": mx25Port_boot,
       "mx25Port-disable": mx25Port_disable,
       "mx25Port-enable": mx25Port_enable,
       "mx25Port-stn-boot": mx25Port_stn_boot,
       "mx25Port-stn-disable": mx25Port_stn_disable,
       "mx25Port-stn-enable": mx25Port_stn_enable,
       "mx25Port-util-exceeded": mx25Port_util_exceeded,
       "mx25Port-err-count-exceeded": mx25Port_err_count_exceeded,
       "mx25Port-stn-addr-dupl": mx25Port_stn_addr_dupl,
       "mx25Port-stn-boot-fail": mx25Port_stn_boot_fail,
       "mx25Port-stn-enable-fail": mx25Port_stn_enable_fail,
       "mx25Port-stn-disable-fail": mx25Port_stn_disable_fail,
       "mx25Port-stn-bsyout-fail": mx25Port_stn_bsyout_fail,
       "mx25Port-boot-fail": mx25Port_boot_fail,
       "mx25Port-enable-fail": mx25Port_enable_fail,
       "mx25Port-disable-fail": mx25Port_disable_fail,
       "mx25Port-busyout-fail": mx25Port_busyout_fail,
       "mx25Port-stn-bsyout": mx25Port_stn_bsyout,
       "mx25Port-busyout": mx25Port_busyout,
       "mx25Port-warn-status": mx25Port_warn_status,
       "sdlcPort-boot": sdlcPort_boot,
       "sdlcPort-boot-fail": sdlcPort_boot_fail,
       "sdlcPort-disable": sdlcPort_disable,
       "sdlcPort-disable-fail": sdlcPort_disable_fail,
       "sdlcPort-enable": sdlcPort_enable,
       "sdlcPort-enable-fail": sdlcPort_enable_fail,
       "sdlcPort-stn-boot": sdlcPort_stn_boot,
       "sdlcPort-stn-boot-fail": sdlcPort_stn_boot_fail,
       "sdlcPort-stn-disable": sdlcPort_stn_disable,
       "sdlcPort-stn-disable-fail": sdlcPort_stn_disable_fail,
       "sdlcPort-stn-enable": sdlcPort_stn_enable,
       "sdlcPort-stn-enable-fail": sdlcPort_stn_enable_fail,
       "sdlcPort-util-exceeded": sdlcPort_util_exceeded,
       "sdlcPort-err-count-exceeded": sdlcPort_err_count_exceeded,
       "sdlcPort-busyout": sdlcPort_busyout,
       "sdlcPort-busyout-fail": sdlcPort_busyout_fail,
       "sdlcPort-stn-busy-out": sdlcPort_stn_busy_out,
       "sdlcPort-stn-busyout-fail": sdlcPort_stn_busyout_fail,
       "sdlcPort-warn-status": sdlcPort_warn_status,
       "sdlcPort-insuff-mem": sdlcPort_insuff_mem,
       "sdlcPort-unsup-frm-size": sdlcPort_unsup_frm_size,
       "sna74021-sdlc-s-dyna": sna74021_sdlc_s_dyna,
       "sna74022-sdlc-s-dyna": sna74022_sdlc_s_dyna,
       "sna74023-sdlc-s-dyna": sna74023_sdlc_s_dyna,
       "sdlcL2-bad-frame-len": sdlcL2_bad_frame_len,
       "sdlcL2-bad-frame-type": sdlcL2_bad_frame_type,
       "sdlcL2-bad-n-r": sdlcL2_bad_n_r,
       "sdlcL2-master-polled-early": sdlcL2_master_polled_early,
       "sdlcL2-norm-seq-frmr": sdlcL2_norm_seq_frmr,
       "sdlcL2-stn-disconn": sdlcL2_stn_disconn,
       "sdlcL2-stn-down": sdlcL2_stn_down,
       "sdlcL2-stn-up": sdlcL2_stn_up,
       "sdlcL2-addr-error": sdlcL2_addr_error,
       "sdlcL2-hpad-stn-down": sdlcL2_hpad_stn_down,
       "sdlcL2-hpad-stn-up": sdlcL2_hpad_stn_up,
       "sdlcL2-hpad-stn-active": sdlcL2_hpad_stn_active,
       "sdlcL2-hpad-stn-inactive": sdlcL2_hpad_stn_inactive,
       "sdlcL2-tpad-stn-active": sdlcL2_tpad_stn_active,
       "sdlcL2-tpad-stn-inactive": sdlcL2_tpad_stn_inactive,
       "sdlcL2-ovsize-frame": sdlcL2_ovsize_frame,
       "qllc-proto-error": qllc_proto_error,
       "qllc-bad-pkt-len": qllc_bad_pkt_len,
       "qllc-illegal-pkt": qllc_illegal_pkt,
       "qllc-qfrmr-receive": qllc_qfrmr_receive,
       "qllc-tpad-stn-up": qllc_tpad_stn_up,
       "qllc-tpad-stn-down": qllc_tpad_stn_down,
       "qllc-net-link-up": qllc_net_link_up,
       "qllc-net-link-down": qllc_net_link_down,
       "ncrbscPort-boot": ncrbscPort_boot,
       "ncrbscPort-boot-fail": ncrbscPort_boot_fail,
       "ncrbscPort-disable": ncrbscPort_disable,
       "ncrbscPort-enable": ncrbscPort_enable,
       "ncrbscPort-enable-fail": ncrbscPort_enable_fail,
       "ncrbscPort-inbound-err": ncrbscPort_inbound_err,
       "ncrbscPort-outbound-err": ncrbscPort_outbound_err,
       "ncrbscPort-line-down": ncrbscPort_line_down,
       "ncrbscPort-line-up": ncrbscPort_line_up,
       "ncrbscPort-dev-down": ncrbscPort_dev_down,
       "ncrbscPort-dev-up": ncrbscPort_dev_up,
       "ncrbscPort-dev-unavail": ncrbscPort_dev_unavail,
       "ncrbsc-list-is-empty": ncrbsc_list_is_empty,
       "ncrbsc-list-is-not-empty": ncrbsc_list_is_not_empty,
       "friL2-unconfigured-dlci": friL2_unconfigured_dlci,
       "friL2-pkt-for-disable-stn": friL2_pkt_for_disable_stn,
       "friL2-bad-frame-len": friL2_bad_frame_len,
       "friL2-annexd-error": friL2_annexd_error,
       "friL2-lmi-error": friL2_lmi_error,
       "friL2-bypass-stn-link-up": friL2_bypass_stn_link_up,
       "friL2-bypass-stn-link-down": friL2_bypass_stn_link_down,
       "friL2-annexa-error": friL2_annexa_error,
       "friL2-unused-net-dlci": friL2_unused_net_dlci,
       "fri-prot-detect-timeout": fri_prot_detect_timeout,
       "fri-prot-change": fri_prot_change,
       "fri-frm-seg-down": fri_frm_seg_down,
       "fri-frm-seg-up": fri_frm_seg_up,
       "fri-rx-lmi-status-update-contain": fri_rx_lmi_status_update_contain,
       "fri-frame-received-invalid-addre": fri_frame_received_invalid_addre,
       "fri-link-up": fri_link_up,
       "fri-link-down": fri_link_down,
       "fri-protocol-error-threshold-rea": fri_protocol_error_threshold_rea,
       "fri87018-uni-segment": fri87018_uni_segment,
       "fri87019-uni-segment": fri87019_uni_segment,
       "friPort-boot": friPort_boot,
       "friPort-boot-fail": friPort_boot_fail,
       "friPort-disable": friPort_disable,
       "friPort-enable": friPort_enable,
       "friPort-util-exceeded": friPort_util_exceeded,
       "friPort-stn-disable": friPort_stn_disable,
       "friPort-stn-enable": friPort_stn_enable,
       "friPort-stn-boot": friPort_stn_boot,
       "friPort-stn-boot-fail": friPort_stn_boot_fail,
       "friPort-warn-status": friPort_warn_status,
       "fripPort-boot-Stn-novbd": fripPort_boot_Stn_novbd,
       "fripPort-boot-Stn-novoice": fripPort_boot_Stn_novoice,
       "fripPort-boot-vbd-noseg": fripPort_boot_vbd_noseg,
       "frip-Port-boot-seg-novbd": frip_Port_boot_seg_novbd,
       "fri-suspicious-configuration-fra": fri_suspicious_configuration_fra,
       "fri-rfc1315-ifindexdlcifrcircuit": fri_rfc1315_ifindexdlcifrcircuit,
       "fri-port-update-complete": fri_port_update_complete,
       "fri-out-of-memory": fri_out_of_memory,
       "dcp-fsm-call-termination": dcp_fsm_call_termination,
       "dcp-na-fac-set-fail": dcp_na_fac_set_fail,
       "dcp-na-fac-get-fail": dcp_na_fac_get_fail,
       "dcp-na-null-ptr": dcp_na_null_ptr,
       "dcp-na-invalid-cr": dcp_na_invalid_cr,
       "dcp-na-invalid-cc": dcp_na_invalid_cc,
       "dcp-na-invalid-pkt-type": dcp_na_invalid_pkt_type,
       "dcp-na-invalid-tpdu-len": dcp_na_invalid_tpdu_len,
       "dcp-na-invalid-tpdu-type": dcp_na_invalid_tpdu_type,
       "dcp-pa-invalid-pkt-type": dcp_pa_invalid_pkt_type,
       "dcp-pa-null-ptr": dcp_pa_null_ptr,
       "dsdPort-boot": dsdPort_boot,
       "dsdPort-boot-fail": dsdPort_boot_fail,
       "rs366Port-boot": rs366Port_boot,
       "rs366Port-boot-fail": rs366Port_boot_fail,
       "rs366Port-disable": rs366Port_disable,
       "rs366Port-enable": rs366Port_enable,
       "rs366Port-enable-fail": rs366Port_enable_fail,
       "rs366Port-disable-fail": rs366Port_disable_fail,
       "flash-cannot-read-from-memory-sl": flash_cannot_read_from_memory_sl,
       "software-copying-to-flash": software_copying_to_flash,
       "num-bytes-copied-to-flash": num_bytes_copied_to_flash,
       "copy-to-flash-complete": copy_to_flash_complete,
       "copy-to-flash-fail": copy_to_flash_fail,
       "updating-software": updating_software,
       "software-update-complete": software_update_complete,
       "software-update-fail": software_update_fail,
       "flash-checksum-err": flash_checksum_err,
       "flash-erase-fail": flash_erase_fail,
       "flash-write-fail": flash_write_fail,
       "lfash-copying": lfash_copying,
       "lflash-copy": lflash_copy,
       "lflash-copy-fail": lflash_copy_fail,
       "sd-copying-software-from-local-f": sd_copying_software_from_local_f,
       "sd-local-flash-copy-complete": sd_local_flash_copy_complete,
       "sd-local-flash-copy-failed": sd_local_flash_copy_failed,
       "cmem-simm-init": cmem_simm_init,
       "alt-flash-software-load": alt_flash_software_load,
       "unknown-card-type": unknown_card_type,
       "mboard-lab-strap-install": mboard_lab_strap_install,
       "async302-err-count-exceeded": async302_err_count_exceeded,
       "async302-dbits-unsupp": async302_dbits_unsupp,
       "async302-baud-unsupp": async302_baud_unsupp,
       "async302-parity-unsupp": async302_parity_unsupp,
       "bop302-err-count-exceeded": bop302_err_count_exceeded,
       "bop302-unsupp-speed": bop302_unsupp_speed,
       "bop302-rx-byte-count-err": bop302_rx_byte_count_err,
       "bop302-erroneous-bool": bop302_erroneous_bool,
       "bop302-clk-override": bop302_clk_override,
       "bop302-tx-sanity-timeout": bop302_tx_sanity_timeout,
       "iodrivers108006-corr": iodrivers108006_corr,
       "cop302-err-count-exceeded": cop302_err_count_exceeded,
       "bstdPort-boot": bstdPort_boot,
       "bstdPort-boot-fail": bstdPort_boot_fail,
       "bstdPort-disable": bstdPort_disable,
       "bstdPort-enable": bstdPort_enable,
       "bstdPort-enable-fail": bstdPort_enable_fail,
       "bstdPort-inbound-err": bstdPort_inbound_err,
       "bstdPort-outbound-err": bstdPort_outbound_err,
       "bstdPort-line-down": bstdPort_line_down,
       "bstdPort-line-up": bstdPort_line_up,
       "bstdPort-stn-down": bstdPort_stn_down,
       "bstdPort-stn-up": bstdPort_stn_up,
       "bstdPort-address-conflict": bstdPort_address_conflict,
       "bstdPort-possible-data-loss": bstdPort_possible_data_loss,
       "bstdPort-cont-tgrp-conflict": bstdPort_cont_tgrp_conflict,
       "bstdPort-hpad-tgrp-conflict": bstdPort_hpad_tgrp_conflict,
       "bstd-station-inhibited-no-dsp-co": bstd_station_inhibited_no_dsp_co,
       "bstd-initialization-failed-softw": bstd_initialization_failed_softw,
       "xdlcL2-bad-frame-len": xdlcL2_bad_frame_len,
       "xdlcL2-bad-frame-type": xdlcL2_bad_frame_type,
       "xdlcL2-bad-n-r": xdlcL2_bad_n_r,
       "xdlcL2-addr-error": xdlcL2_addr_error,
       "xdlcL2-norm-seq-frmr": xdlcL2_norm_seq_frmr,
       "xdlcL2-stn-disconnect": xdlcL2_stn_disconnect,
       "xdlcL2-mx25-stn-down": xdlcL2_mx25_stn_down,
       "xdlcL2-mx25-stn-up": xdlcL2_mx25_stn_up,
       "xdlcL2-multiple-masters": xdlcL2_multiple_masters,
       "xdlcL2-stat-overflow": xdlcL2_stat_overflow,
       "xdlcL2-tpad-stn-active": xdlcL2_tpad_stn_active,
       "xdlcL2-tpad-stn-inactive": xdlcL2_tpad_stn_inactive,
       "xdlcL2-ovsize-frame": xdlcL2_ovsize_frame,
       "xdlcPort-boot": xdlcPort_boot,
       "xdlcPort-boot-fail": xdlcPort_boot_fail,
       "xdlcPort-disable": xdlcPort_disable,
       "xdlcPort-disable-fail": xdlcPort_disable_fail,
       "xdlcPort-enable": xdlcPort_enable,
       "xdlcPort-enable-fail": xdlcPort_enable_fail,
       "xdlcPort-stn-boot": xdlcPort_stn_boot,
       "xdlcPort-stn-boot-fail": xdlcPort_stn_boot_fail,
       "xdlcPort-stn-disable": xdlcPort_stn_disable,
       "xdlcPort-stn-disable-fail": xdlcPort_stn_disable_fail,
       "xdlcPort-stn-enable": xdlcPort_stn_enable,
       "xdlcPort-stn-enable-fail": xdlcPort_stn_enable_fail,
       "xdlcPort-util-exceeded": xdlcPort_util_exceeded,
       "xdlcPort-err-count-exceeded": xdlcPort_err_count_exceeded,
       "xdlcPort-stn-addr-dupl": xdlcPort_stn_addr_dupl,
       "xdlcPort-stat-overflow": xdlcPort_stat_overflow,
       "xdlcPort-stn-stat-overflow": xdlcPort_stn_stat_overflow,
       "xdlcPort-warn-status": xdlcPort_warn_status,
       "xdlcPort-unsupport-frm-size": xdlcPort_unsupport_frm_size,
       "xdlc-insufficient-memory-to-prot": xdlc_insufficient_memory_to_prot,
       "xdlc112020-xdlc-s-dy": xdlc112020_xdlc_s_dy,
       "xdlc112021-xdlc-s-dy": xdlc112021_xdlc_s_dy,
       "xdlc112022-xdlc-s-dy": xdlc112022_xdlc_s_dy,
       "xdlc112023-insuffici": xdlc112023_insuffici,
       "nccpDpad-unknown-device": nccpDpad_unknown_device,
       "nccpDpad-crc-error": nccpDpad_crc_error,
       "nccpDpad-streaming-device": nccpDpad_streaming_device,
       "nccpDpad-stream-device-clear": nccpDpad_stream_device_clear,
       "nccpDpad-main-chan-fail": nccpDpad_main_chan_fail,
       "nccpDpad-main-chan-connect": nccpDpad_main_chan_connect,
       "nccpDpad-main-chan-disconn": nccpDpad_main_chan_disconn,
       "nccpDpad-state-search-abort": nccpDpad_state_search_abort,
       "nccpMpad-not-responding": nccpMpad_not_responding,
       "nccpMpad-device-status": nccpMpad_device_status,
       "nccpMpad-dupl-device": nccpMpad_dupl_device,
       "nccpMpad-chan-conn-fail": nccpMpad_chan_conn_fail,
       "nccpMpad-chan-conn": nccpMpad_chan_conn,
       "nccpMpad-chan-disconn": nccpMpad_chan_disconn,
       "nccpMpad-proto-err": nccpMpad_proto_err,
       "ibm2260Port-boot": ibm2260Port_boot,
       "ibm2260Port-boot-fail": ibm2260Port_boot_fail,
       "ibm2260Port-disable": ibm2260Port_disable,
       "ibm2260Port-enable": ibm2260Port_enable,
       "ibm2260Port-enable-fail": ibm2260Port_enable_fail,
       "ibm2260Port-inbound-err": ibm2260Port_inbound_err,
       "ibm2260Port-outbound-err": ibm2260Port_outbound_err,
       "ibm2260Port-line-down": ibm2260Port_line_down,
       "ibm2260Port-line-up": ibm2260Port_line_up,
       "ibm2260Port-stn-down": ibm2260Port_stn_down,
       "ibm2260Port-stn-up": ibm2260Port_stn_up,
       "ibm2260Port-addr-conflict": ibm2260Port_addr_conflict,
       "ibm2260Port-poss-data-loss": ibm2260Port_poss_data_loss,
       "tbopPort-boot": tbopPort_boot,
       "tbopPort-boot-fail": tbopPort_boot_fail,
       "tbopPort-disable": tbopPort_disable,
       "tbopPort-disable-fail": tbopPort_disable_fail,
       "tbopPort-Port-enable": tbopPort_Port_enable,
       "tbopPort-enable-fail": tbopPort_enable_fail,
       "tbopPort-util-exceeded": tbopPort_util_exceeded,
       "tbopPort-err-count-exceeded": tbopPort_err_count_exceeded,
       "tbopPort-busyout": tbopPort_busyout,
       "tbopPort-busyout-fail": tbopPort_busyout_fail,
       "tbop-port-status-warning": tbop_port_status_warning,
       "tbopL2-bad-frame-len": tbopL2_bad_frame_len,
       "tcop-Port-boot": tcop_Port_boot,
       "tcop-Port-boot-fail": tcop_Port_boot_fail,
       "tcop-Port-disable": tcop_Port_disable,
       "tcop-Port-disable-fail": tcop_Port_disable_fail,
       "tcop-Port-enable": tcop_Port_enable,
       "tcop-Port-enable-fail": tcop_Port_enable_fail,
       "tcop-Port-util-exceeded": tcop_Port_util_exceeded,
       "tcop-Port-error-exceeded": tcop_Port_error_exceeded,
       "tcop-Port-busy-out": tcop_Port_busy_out,
       "tcop-Port-busy-out-fail": tcop_Port_busy_out_fail,
       "tcop-Port-subtype-notsupported": tcop_Port_subtype_notsupported,
       "tcop-rx-queue-overflow": tcop_rx_queue_overflow,
       "tcop-tx-queue-overflow": tcop_tx_queue_overflow,
       "tcop-tx-timeout": tcop_tx_timeout,
       "tcop-threshold": tcop_threshold,
       "bridge-init-fail": bridge_init_fail,
       "bridge-link-boot": bridge_link_boot,
       "bridge-link-boot-fail": bridge_link_boot_fail,
       "bridge-link-enabled": bridge_link_enabled,
       "bridge-link-disabled": bridge_link_disabled,
       "bridge-param-boot": bridge_param_boot,
       "bridge-param-boot-fail": bridge_param_boot_fail,
       "bridge-link-out-of-range": bridge_link_out_of_range,
       "sr-ring-num-mismatch": sr_ring_num_mismatch,
       "sr-bridge-id-mismatch": sr_bridge_id_mismatch,
       "sr-dupl-rbr-triplet": sr_dupl_rbr_triplet,
       "sr-incompat-link-mode": sr_incompat_link_mode,
       "include-br-one-trans-link-allowe": include_br_one_trans_link_allowe,
       "sr-duplicate-token-ring": sr_duplicate_token_ring,
       "stp-unknown-bpdu-type": stp_unknown_bpdu_type,
       "stp-bridge-is-root": stp_bridge_is_root,
       "stp-bridge-is-not-root": stp_bridge_is_not_root,
       "stp-topo-unstable": stp_topo_unstable,
       "stp-topo-stable": stp_topo_stable,
       "stp-config-buff-not-avail": stp_config_buff_not_avail,
       "stp-tcn-buff-not-avail": stp_tcn_buff_not_avail,
       "trPort-reset-fail": trPort_reset_fail,
       "trPort-chip-init-fail": trPort_chip_init_fail,
       "trPort-open-fail": trPort_open_fail,
       "trPort-Port-init": trPort_Port_init,
       "trPort-rx-cmd-timeout": trPort_rx_cmd_timeout,
       "trPort-tx-cmd-timeout": trPort_tx_cmd_timeout,
       "trPort-loss-of-signal": trPort_loss_of_signal,
       "trPort-loss-of-signal-clear": trPort_loss_of_signal_clear,
       "trPort-beacon": trPort_beacon,
       "trPort-beacon-clear": trPort_beacon_clear,
       "trPort-tx-beacon": trPort_tx_beacon,
       "trPort-tx-beacon-clear": trPort_tx_beacon_clear,
       "trPort-tx-halted": trPort_tx_halted,
       "trPort-cmd-reject": trPort_cmd_reject,
       "trPort-lobe-error": trPort_lobe_error,
       "trPort-auto-remove-err": trPort_auto_remove_err,
       "trPort-remove-rcvd": trPort_remove_rcvd,
       "trPort-not-disabled": trPort_not_disabled,
       "trPort-cmd-timeout": trPort_cmd_timeout,
       "trPort-fatal-err": trPort_fatal_err,
       "trPort-single-stn-err": trPort_single_stn_err,
       "trPort-up": trPort_up,
       "trPort-down": trPort_down,
       "trPort-trans-err": trPort_trans_err,
       "trPort-unkn-trans-err": trPort_unkn_trans_err,
       "trPort-diag-check": trPort_diag_check,
       "trd-tr-diagnostic-check-cb": trd_tr_diagnostic_check_cb,
       "trPort-boot": trPort_boot,
       "trPort-boot-fail": trPort_boot_fail,
       "trPort-enable": trPort_enable,
       "trPort-disable": trPort_disable,
       "trPort-init-fail": trPort_init_fail,
       "trPort-ring-num-cfg-err": trPort_ring_num_cfg_err,
       "hdwareAccel-comm-fail": hdwareAccel_comm_fail,
       "hdwareAccel-ha-warn": hdwareAccel_ha_warn,
       "hdwareAccel-test": hdwareAccel_test,
       "agent-coldstart": agent_coldstart,
       "agent-warmstart": agent_warmstart,
       "agent-chan-conn-up": agent_chan_conn_up,
       "agent-chan-conn-down": agent_chan_conn_down,
       "agent-missing-module": agent_missing_module,
       "agent-missing-aaf": agent_missing_aaf,
       "agent-auth-fail": agent_auth_fail,
       "agent-wrong-pointer": agent_wrong_pointer,
       "snmpmgr-snmp-manager-is-restarti": snmpmgr_snmp_manager_is_restarti,
       "snmpmgr-failed-main-channel-conn": snmpmgr_failed_main_channel_conn,
       "snmpmgr-connected-to-main-channe": snmpmgr_connected_to_main_channe,
       "snmpmgr-lost-main-channel-connec": snmpmgr_lost_main_channel_connec,
       "snmpmgr-connected-to-pms-channel": snmpmgr_connected_to_pms_channel,
       "snmpmgr-lost-pms-channel-connect": snmpmgr_lost_pms_channel_connect,
       "snmpconn-snmp-connection-is-rest": snmpconn_snmp_connection_is_rest,
       "snmpconn-cannot-get-memory": snmpconn_cannot_get_memory,
       "snmpconn-cannot-get-iorb": snmpconn_cannot_get_iorb,
       "snmpconn-cannot-get-dbuffer": snmpconn_cannot_get_dbuffer,
       "ret-high-priority-traps": ret_high_priority_traps,
       "ret-med-priority-traps": ret_med_priority_traps,
       "ret-low-priority-traps": ret_low_priority_traps,
       "lclTermi-invalid-frame": lclTermi_invalid_frame,
       "lclTermi-ssn-not-started": lclTermi_ssn_not_started,
       "lclTermi-ssn-started": lclTermi_ssn_started,
       "lclTermi-ssn-terminated": lclTermi_ssn_terminated,
       "lcon-config-err": lcon_config_err,
       "lcon-disabled": lcon_disabled,
       "lcon-enabled": lcon_enabled,
       "lcon-disable-fail": lcon_disable_fail,
       "lcon-enable-fail": lcon_enable_fail,
       "lcon-booted": lcon_booted,
       "lcon-boot-fail": lcon_boot_fail,
       "lcon-create-fail": lcon_create_fail,
       "lcon-group-config-error": lcon_group_config_error,
       "lcon-nexthop-config-err": lcon_nexthop_config_err,
       "lcon-out-of-range": lcon_out_of_range,
       "wa-protocol-priority-profile-ent": wa_protocol_priority_profile_ent,
       "wa-precedence-array-assignments": wa_precedence_array_assignments,
       "wsl-Port-boot": wsl_Port_boot,
       "lcon-creation-fail": lcon_creation_fail,
       "wsl-not-monitored": wsl_not_monitored,
       "lcon-bad-hello-thresh": lcon_bad_hello_thresh,
       "lcon-invalid-id": lcon_invalid_id,
       "sram-high-prior-traps": sram_high_prior_traps,
       "sram-med-prior-traps": sram_med_prior_traps,
       "sram-low-prior-traps": sram_low_prior_traps,
       "node-record-boot-fail": node_record_boot_fail,
       "ethPort-no-throttle-timers": ethPort_no_throttle_timers,
       "ethPort-no-initialization": ethPort_no_initialization,
       "ethPort-config-fail": ethPort_config_fail,
       "ethPort-ia-fail": ethPort_ia_fail,
       "ethPort-configuration-timeout": ethPort_configuration_timeout,
       "ethPort-no-suspension": ethPort_no_suspension,
       "ethPort-tx-put-fail": ethPort_tx_put_fail,
       "ethPort-excess-tx-err": ethPort_excess_tx_err,
       "ethPort-loc": ethPort_loc,
       "ethPort-excess-rx-err": ethPort_excess_rx_err,
       "ethPort-excess-tx-clear": ethPort_excess_tx_clear,
       "ethPort-loc-clear": ethPort_loc_clear,
       "ethPort-excessive-rx-clear": ethPort_excessive_rx_clear,
       "ethPort-invalid-state-enabled": ethPort_invalid_state_enabled,
       "ethPort-inval-state-disable": ethPort_inval_state_disable,
       "ethPort-loopback-fail": ethPort_loopback_fail,
       "ethPort-tdr-fail": ethPort_tdr_fail,
       "ethPort-ca-fail": ethPort_ca_fail,
       "ethPort-rx-list-err": ethPort_rx_list_err,
       "ethPort-tx-list-err": ethPort_tx_list_err,
       "ethPort-lockup-err": ethPort_lockup_err,
       "alcPort-boot": alcPort_boot,
       "alcPort-boot-fail": alcPort_boot_fail,
       "alcPort-disable": alcPort_disable,
       "alcPort-disable-fail": alcPort_disable_fail,
       "alcPort-enable": alcPort_enable,
       "alcPort-enable-fail": alcPort_enable_fail,
       "alcPort-nomodule": alcPort_nomodule,
       "alch-al-line-down": alch_al_line_down,
       "alch-al-line-up": alch_al_line_up,
       "alch-al-flow-ctl-imp": alch_al_flow_ctl_imp,
       "alch-al-flow-ctl-rel": alch_al_flow_ctl_rel,
       "alch-al-ia-fast-poll": alch_al_ia_fast_poll,
       "alch-al-ia-slow-poll": alch_al_ia_slow_poll,
       "alch-al-ia-stop-poll": alch_al_ia_stop_poll,
       "alch-al-reset-disc": alch_al_reset_disc,
       "alch-al-T1-timeout": alch_al_T1_timeout,
       "alch-al-T2-timeout": alch_al_T2_timeout,
       "alch-al-bad-ccc-rec": alch_al_bad_ccc_rec,
       "alch-al-host-timeout": alch_al_host_timeout,
       "alch-al-host-start-poll": alch_al_host_start_poll,
       "alch-al-msg-dis-no-conn": alch_al_msg_dis_no_conn,
       "alp-al-buff-disc": alp_al_buff_disc,
       "apl-al-call-fail": apl_al_call_fail,
       "alp-al-lost-msgs": alp_al_lost_msgs,
       "alp-al-SIP-error": alp_al_SIP_error,
       "alp-al-SIP-nexist": alp_al_SIP_nexist,
       "alp-al-src-IP-rqd": alp_al_src_IP_rqd,
       "fraPort-boot": fraPort_boot,
       "fraPort-boot-fail": fraPort_boot_fail,
       "fraPort-disable": fraPort_disable,
       "fraPort-enable": fraPort_enable,
       "fraPort-util-exceeded": fraPort_util_exceeded,
       "fraPort-stn-disable": fraPort_stn_disable,
       "fraPort-stn-enable": fraPort_stn_enable,
       "fraPort-stn-boot": fraPort_stn_boot,
       "fraPort-stn-boot-fail": fraPort_stn_boot_fail,
       "fraPort-warn-status": fraPort_warn_status,
       "fra-port-update-complete": fra_port_update_complete,
       "fra-out-of-memory-some-stations": fra_out_of_memory_some_stations,
       "fraL2-unconfig-dlci": fraL2_unconfig_dlci,
       "fraL2-dsbl-stn-pack": fraL2_dsbl_stn_pack,
       "fraL2-bad-frame-len": fraL2_bad_frame_len,
       "fraL2-annexd-err": fraL2_annexd_err,
       "fraL2-lmi-err": fraL2_lmi_err,
       "fraL2-fsm-err": fraL2_fsm_err,
       "fraL2-invalid-addr": fraL2_invalid_addr,
       "fraL2-net-congested": fraL2_net_congested,
       "fraL2-link-up": fraL2_link_up,
       "fraL2-link-down": fraL2_link_down,
       "fraL2-annexa-err": fraL2_annexa_err,
       "fra-station-up": fra_station_up,
       "fra-station-down": fra_station_down,
       "lcon-invalid-proto-id": lcon_invalid_proto_id,
       "lcon-invalid-forward-id": lcon_invalid_forward_id,
       "lcon-rx-no-route-discard": lcon_rx_no_route_discard,
       "lcon-rx-no-hop-discard": lcon_rx_no_hop_discard,
       "lcon-tx-bad-hop-discard": lcon_tx_bad_hop_discard,
       "lcon-svc-creation-fail": lcon_svc_creation_fail,
       "lcon-1294-invalid-encap": lcon_1294_invalid_encap,
       "tb-forwarding-table-full": tb_forwarding_table_full,
       "ethPort-boot": ethPort_boot,
       "ethPort-boot-fail": ethPort_boot_fail,
       "ethPort-enable": ethPort_enable,
       "ethPort-disable": ethPort_disable,
       "ethPort-init-fail": ethPort_init_fail,
       "shdlc-link-down": shdlc_link_down,
       "shdlc-disc-recv": shdlc_disc_recv,
       "shdlc-bad-frame-type": shdlc_bad_frame_type,
       "shdlc-address-err": shdlc_address_err,
       "shdlc-bad-frame-len": shdlc_bad_frame_len,
       "shdlc-extend-seq-frmr": shdlc_extend_seq_frmr,
       "shdlc-norm-seq-frmr": shdlc_norm_seq_frmr,
       "shdlc-link-up": shdlc_link_up,
       "shdlc-link-blocked": shdlc_link_blocked,
       "shdlc-bad-n-r": shdlc_bad_n_r,
       "shdlc-backup-activated": shdlc_backup_activated,
       "shdlc-extend-bad-frame-type": shdlc_extend_bad_frame_type,
       "shdlc-access-link-down": shdlc_access_link_down,
       "shdlc-access-link-up": shdlc_access_link_up,
       "shdlc-ovsize-frame": shdlc_ovsize_frame,
       "shdlc-port-boot-complete": shdlc_port_boot_complete,
       "shdlc-port-boot-failure": shdlc_port_boot_failure,
       "shdlc-port-disabled": shdlc_port_disabled,
       "shdlc-port-enabled": shdlc_port_enabled,
       "shdlc-port-utilization-threshold": shdlc_port_utilization_threshold,
       "shdlc-port-status-warning": shdlc_port_status_warning,
       "shdlc-unsupported-frame-size-ope": shdlc_unsupported_frame_size_ope,
       "tftp-op-success": tftp_op_success,
       "tftp-cmem-fail": tftp_cmem_fail,
       "tftp-local-transfer-fail": tftp_local_transfer_fail,
       "tftp-remote-transfer-fail": tftp_remote_transfer_fail,
       "tftp-system-fail": tftp_system_fail,
       "tftp-udp-reg-fail": tftp_udp_reg_fail,
       "tftp-dl-in-progress": tftp_dl_in_progress,
       "tftp-sw-image-err": tftp_sw_image_err,
       "tftp-flash-erase-fail": tftp_flash_erase_fail,
       "tftp-flash-write-fail": tftp_flash_write_fail,
       "tftp-tftp": tftp_tftp,
       "tftp-partial-success": tftp_partial_success,
       "tftp-failure": tftp_failure,
       "ipx-multiple-paths": ipx_multiple_paths,
       "ipx-net-unreachable": ipx_net_unreachable,
       "router-ipx-disabled-memory-alloc": router_ipx_disabled_memory_alloc,
       "router-no-memory-for-table": router_no_memory_for_table,
       "router-no-memory-for-record": router_no_memory_for_record,
       "router-record-attempt-to-add-dup": router_record_attempt_to_add_dup,
       "dscope-user-message-lost": dscope_user_message_lost,
       "dscope-subaddress-incorrect-leng": dscope_subaddress_incorrect_leng,
       "ipx-high-priority-traps": ipx_high_priority_traps,
       "ipx-med-priority-traps": ipx_med_priority_traps,
       "ipx-low-priority-traps": ipx_low_priority_traps,
       "ipx-max-interf-exceeded": ipx_max_interf_exceeded,
       "router-record-attempt-to-add-dup2": router_record_attempt_to_add_dup2,
       "code-bytes-loaded-from-extended": code_bytes_loaded_from_extended,
       "cougar-code-loaded-from-extended": cougar_code_loaded_from_extended,
       "code-extended-software-load-fail": code_extended_software_load_fail,
       "code-master-failed-to-copy-exten": code_master_failed_to_copy_exten,
       "code-extended-checksum-error-slo": code_extended_checksum_error_slo,
       "asyncModem-speed-unsupp": asyncModem_speed_unsupp,
       "asyncModem-databits-unsupp": asyncModem_databits_unsupp,
       "asyncModem-connection": asyncModem_connection,
       "t3pos-fat-timer-expired-line-dis": t3pos_fat_timer_expired_line_dis,
       "t3pos-connection-towards-host-in": t3pos_connection_towards_host_in,
       "t3pos-dleeot-received-call-clear": t3pos_dleeot_received_call_clear,
       "t3pos-invalid-frame-from-pos-cal": t3pos_invalid_frame_from_pos_cal,
       "t3pos-dle-eot-timeout-call-clear": t3pos_dle_eot_timeout_call_clear,
       "t3pos-line-failure-line-disconne": t3pos_line_failure_line_disconne,
       "t3pos-output-queue-overrun": t3pos_output_queue_overrun,
       "t3pos-input-queue-overrun": t3pos_input_queue_overrun,
       "t3pos-call-cleared-by-host": t3pos_call_cleared_by_host,
       "t3pos-call-rejected-by-level3": t3pos_call_rejected_by_level3,
       "t3pos-invalid-mss-from-pos-call": t3pos_invalid_mss_from_pos_call,
       "t3pos-invalid-mss-from-host-call": t3pos_invalid_mss_from_host_call,
       "t3pos-dial-out-not-supported-cal": t3pos_dial_out_not_supported_cal,
       "t3pos-host-frame-size-exceeded-c": t3pos_host_frame_size_exceeded_c,
       "t3pos-control-frame-from-host-ca": t3pos_control_frame_from_host_ca,
       "t3pos-retry-exceeded-line-discon": t3pos_retry_exceeded_line_discon,
       "t3pos-retry-exceeded-call-cleare": t3pos_retry_exceeded_call_cleare,
       "t3pos-virtual-retry-exceeded-cal": t3pos_virtual_retry_exceeded_cal,
       "t3pos-virtual-call-retry-exceede": t3pos_virtual_call_retry_exceede,
       "t3pos-invitation-to-clear-from-h": t3pos_invitation_to_clear_from_h,
       "t3pos-invalid-control-field-call": t3pos_invalid_control_field_call,
       "t3pos-port-stat-overflow": t3pos_port_stat_overflow,
       "t3pos-connected-to-host": t3pos_connected_to_host,
       "t3pos-control-field-empty-call-r": t3pos_control_field_empty_call_r,
       "t3pos-port-boot-complete": t3pos_port_boot_complete,
       "t3pos-portbootfailure": t3pos_portbootfailure,
       "t3pos-port-disabled": t3pos_port_disabled,
       "t3pos-port-disable-failure": t3pos_port_disable_failure,
       "t3pos-port-enabled": t3pos_port_enabled,
       "t3pos-port-enable-failure": t3pos_port_enable_failure,
       "t3pos-port-connection-cleared": t3pos_port_connection_cleared,
       "t3pos-port-utilization-threshold": t3pos_port_utilization_threshold,
       "atpad-data-loss": atpad_data_loss,
       "atpad-data-loss-cmd": atpad_data_loss_cmd,
       "atpadPort-boot": atpadPort_boot,
       "atpadPort-boot-fail": atpadPort_boot_fail,
       "atpadPort-disable": atpadPort_disable,
       "atpadPort-enable": atpadPort_enable,
       "atpadPort-util-exceeded": atpadPort_util_exceeded,
       "atpadPort-warn-status": atpadPort_warn_status,
       "atpadPort-errcnt-exceeded": atpadPort_errcnt_exceeded,
       "lclTerm-stn-up": lclTerm_stn_up,
       "lclTerm-stn-down": lclTerm_stn_down,
       "lclTerm-stn-timed-out": lclTerm_stn_timed_out,
       "lclTerm-remote-disconn": lclTerm_remote_disconn,
       "lclTerm-remote-conn-estab": lclTerm_remote_conn_estab,
       "lclTerm-remote-call-up": lclTerm_remote_call_up,
       "ethltm-station-frame-type-does-n": ethltm_station_frame_type_does_n,
       "ethltm-remote-call-established": ethltm_remote_call_established,
       "frltm-fri-dlci-disconn": frltm_fri_dlci_disconn,
       "lctTerm-stn-boot": lctTerm_stn_boot,
       "lctTerm-stn-boot-fail": lctTerm_stn_boot_fail,
       "lctTerm-stn-disable": lctTerm_stn_disable,
       "lctTerm-stn-disable-fail": lctTerm_stn_disable_fail,
       "lctTerm-stn-enable": lctTerm_stn_enable,
       "lctTerm-stn-enable-fail": lctTerm_stn_enable_fail,
       "lctTerm-port-warn-status": lctTerm_port_warn_status,
       "slaccm-insufficient-memory-to-pr": slaccm_insufficient_memory_to_pr,
       "slaccm-insufficient-memory": slaccm_insufficient_memory,
       "slaccm226009-dynamic": slaccm226009_dynamic,
       "slaccm226010-dynamic": slaccm226010_dynamic,
       "slaccm226011-dynamic": slaccm226011_dynamic,
       "slaccm226012-dynamic": slaccm226012_dynamic,
       "slaccm226013-dynamic": slaccm226013_dynamic,
       "slaccm226014-dynamic": slaccm226014_dynamic,
       "slaccm226015-insuffi": slaccm226015_insuffi,
       "slaccm226016-no-stat": slaccm226016_no_stat,
       "slaccm226017-all-sta": slaccm226017_all_sta,
       "slaccm226018-will-re": slaccm226018_will_re,
       "slaccm226019-err-sla": slaccm226019_err_sla,
       "tnpplp-link-down": tnpplp_link_down,
       "tnpplp-link-up": tnpplp_link_up,
       "tnpplp-protocol-errors": tnpplp_protocol_errors,
       "tnpplp-frame-discarded": tnpplp_frame_discarded,
       "tnpplp-rempad-connprogress": tnpplp_rempad_connprogress,
       "tnpplp-autocalltry-exhaust": tnpplp_autocalltry_exhaust,
       "tnpplp-remdevice-down": tnpplp_remdevice_down,
       "tnpplp-rempad-callclear": tnpplp_rempad_callclear,
       "tnpplp-level3-callreject": tnpplp_level3_callreject,
       "tnpplp-mnemonic-error": tnpplp_mnemonic_error,
       "tnpplp-remdevice-up": tnpplp_remdevice_up,
       "tnpplp-x25call-reject": tnpplp_x25call_reject,
       "tnpplp-network-callclear": tnpplp_network_callclear,
       "tnpplp-rempad-mismatch": tnpplp_rempad_mismatch,
       "tnpplp-x25-up": tnpplp_x25_up,
       "tnppPort-boot": tnppPort_boot,
       "tnppPort-boot-fail": tnppPort_boot_fail,
       "tnppPort-disable": tnppPort_disable,
       "tnppPort-disable-fail": tnppPort_disable_fail,
       "tnppPort-enable": tnppPort_enable,
       "tnppPort-enable-fail": tnppPort_enable_fail,
       "tnppPort-connection-cleared": tnppPort_connection_cleared,
       "tnppPort-util-exceeded": tnppPort_util_exceeded,
       "tnppPort-status-warning": tnppPort_status_warning,
       "netSvcs-param-err": netSvcs_param_err,
       "netSvcs-no-features": netSvcs_no_features,
       "netSvcs-data-struct-err": netSvcs_data_struct_err,
       "netSvcs-unav-chans": netSvcs_unav_chans,
       "netSvcs-rereg": netSvcs_rereg,
       "netSvcs-invalid-config": netSvcs_invalid_config,
       "bod-I-lead-up": bod_I_lead_up,
       "bod-I-lead-down": bod_I_lead_down,
       "bod-I-leased-line-down": bod_I_leased_line_down,
       "bod-I-leased-line-up": bod_I_leased_line_up,
       "bod-tow-switch": bod_tow_switch,
       "bod-tow-disabling": bod_tow_disabling,
       "bod-tow-enabling": bod_tow_enabling,
       "bod-isdn-down": bod_isdn_down,
       "bod-user-disable": bod_user_disable,
       "bod-Port-disable": bod_Port_disable,
       "bod-Port-boot": bod_Port_boot,
       "slipPort-boot": slipPort_boot,
       "slipPort-boot-fail": slipPort_boot_fail,
       "slipPort-disable": slipPort_disable,
       "slipPort-enable": slipPort_enable,
       "slipPort-util-exceeded": slipPort_util_exceeded,
       "slipPort-warn-status": slipPort_warn_status,
       "slipPort-err-count-exceeded": slipPort_err_count_exceeded,
       "slipProto-inb-data-loss": slipProto_inb_data_loss,
       "slipProto-outb-data-loss": slipProto_outb_data_loss,
       "slipProto-invalid-encaps": slipProto_invalid_encaps,
       "lcon-877-unsup-proto-rcvd": lcon_877_unsup_proto_rcvd,
       "appleTalk-bad-param": appleTalk_bad_param,
       "appleTalk-no-mem": appleTalk_no_mem,
       "appleTalk-low-prior-traps": appleTalk_low_prior_traps,
       "appleTalk-med-prior-traps": appleTalk_med_prior_traps,
       "appleTalk-high-prior-traps": appleTalk_high_prior_traps,
       "appleTalk-verbose": appleTalk_verbose,
       "appleTalk-warning": appleTalk_warning,
       "appleTalk-err": appleTalk_err,
       "appleTalk-fatal-err": appleTalk_fatal_err,
       "appleTalk-unknown-err": appleTalk_unknown_err,
       "appleTalk-failure": appleTalk_failure,
       "sip-restart": sip_restart,
       "sip-lan-restart": sip_lan_restart,
       "sip-lan-connect-client": sip_lan_connect_client,
       "sip-lan-disconnect-client": sip_lan_disconnect_client,
       "sip-wan-restart": sip_wan_restart,
       "sip-wan-lan-disconnect": sip_wan_lan_disconnect,
       "sip-wan-lan-restart": sip_wan_lan_restart,
       "sip-wan-lan-connect": sip_wan_lan_connect,
       "sip-wan-lan-disc": sip_wan_lan_disc,
       "sip-wan-wan-connect": sip_wan_wan_connect,
       "sip-wan-wan-disconnect": sip_wan_wan_disconnect,
       "sip-wan-wan-interrupted": sip_wan_wan_interrupted,
       "bop-bri-no-report": bop_bri_no_report,
       "briPort-call-up": briPort_call_up,
       "briPort-call-down": briPort_call_down,
       "briPort-tx-setup-fail": briPort_tx_setup_fail,
       "briPort-rx-setup-fail": briPort_rx_setup_fail,
       "briPort-disconn-fail": briPort_disconn_fail,
       "briPort-tx-call-fail": briPort_tx_call_fail,
       "briPort-rx-call-fail": briPort_rx_call_fail,
       "briPort-init-fail": briPort_init_fail,
       "briPort-boot-fail": briPort_boot_fail,
       "briPort-boot": briPort_boot,
       "briPort-buff-congested": briPort_buff_congested,
       "briPort-dchan-err": briPort_dchan_err,
       "briPort-card-fail": briPort_card_fail,
       "briPort-dchan-link-down": briPort_dchan_link_down,
       "bopbri-bri-internal-error": bopbri_bri_internal_error,
       "bopbri241062-channel": bopbri241062_channel,
       "swServ-link-activated": swServ_link_activated,
       "swServ-link-deactivated": swServ_link_deactivated,
       "swServ-invalid-entry": swServ_invalid_entry,
       "swServ-serving-multi-ports": swServ_serving_multi_ports,
       "swServ-param-error": swServ_param_error,
       "swServ-already-active": swServ_already_active,
       "swServ-num-entries-changed": swServ_num_entries_changed,
       "swServ-dest-changed": swServ_dest_changed,
       "swServ-monitored-changed": swServ_monitored_changed,
       "swServ-backup-changed": swServ_backup_changed,
       "ss-number-of-max-entries-in-node": ss_number_of_max_entries_in_node,
       "ss242011-process-msg": ss242011_process_msg,
       "ss242012-ss-dynamic-rte": ss242012_ss_dynamic_rte,
       "ss242013-select-dest": ss242013_select_dest,
       "ss242014-select-cond": ss242014_select_cond,
       "ss242015-process-msg": ss242015_process_msg,
       "ss242016-cmem-compre": ss242016_cmem_compre,
       "ss242017-cmem-decomp": ss242017_cmem_decomp,
       "ss242018-ss-max-retries": ss242018_ss_max_retries,
       "ss242019-max-callid": ss242019_max_callid,
       "ss242020-possible-ra": ss242020_possible_ra,
       "hubPort-boot": hubPort_boot,
       "hubPort-boot-fail": hubPort_boot_fail,
       "hubPort-disable": hubPort_disable,
       "hubPort-enable": hubPort_enable,
       "hubPort-warn-status": hubPort_warn_status,
       "briPort-chan-boot": briPort_chan_boot,
       "briPort-chan-boot-fail": briPort_chan_boot_fail,
       "bri-Port-boot": bri_Port_boot,
       "briPort-invalid-boot": briPort_invalid_boot,
       "briPort-chan-disable": briPort_chan_disable,
       "briPort-disable": briPort_disable,
       "briPort-warn-status": briPort_warn_status,
       "briPort-util-exceeded": briPort_util_exceeded,
       "briPort-chan-warn-status": briPort_chan_warn_status,
       "briPort-chan-enable": briPort_chan_enable,
       "briPort-enable": briPort_enable,
       "briPort-chan-util-exceeded": briPort_chan_util_exceeded,
       "briPort-no-chans": briPort_no_chans,
       "briPort-protocol-mismatch": briPort_protocol_mismatch,
       "bri245014-card-failu": bri245014_card_failu,
       "bri245015-port-boot": bri245015_port_boot,
       "bri245016-auto-recov": bri245016_auto_recov,
       "briPort-pkt-lvl-restart": briPort_pkt_lvl_restart,
       "dc-dsp-disabled": dc_dsp_disabled,
       "dc-dsp-fail": dc_dsp_fail,
       "dc-no-ram": dc_no_ram,
       "dc-insuff-ram": dc_insuff_ram,
       "dc-no-channels": dc_no_channels,
       "dc-rcvd-neg": dc_rcvd_neg,
       "dc-mis-configure": dc_mis_configure,
       "dc-abnorm-clr-flush": dc_abnorm_clr_flush,
       "dc-lost-clr": dc_lost_clr,
       "dc-ap-to-ap": dc_ap_to_ap,
       "dc-no-chan-for-pvc": dc_no_chan_for_pvc,
       "dc-src-config-err": dc_src_config_err,
       "dc-corrupt-control-blk": dc_corrupt_control_blk,
       "dc-abnorm-cmd": dc_abnorm_cmd,
       "dc-dsp-download-err": dc_dsp_download_err,
       "dc-incorrect-config": dc_incorrect_config,
       "dc-hdr-err": dc_hdr_err,
       "dc-max-dc-chan": dc_max_dc_chan,
       "dc-gen-init-fail": dc_gen_init_fail,
       "dc-dbg-sem-locked": dc_dbg_sem_locked,
       "dc-dbg-ca-no-cr": dc_dbg_ca_no_cr,
       "dc-dbg-no-config": dc_dbg_no_config,
       "dc-dbg-dealloc-no-cb": dc_dbg_dealloc_no_cb,
       "dc-dbg-dch-ch-stat-fail": dc_dbg_dch_ch_stat_fail,
       "dc-dbg-lost-buffs": dc_dbg_lost_buffs,
       "dc-dbg-abnorm-fsm-event": dc_dbg_abnorm_fsm_event,
       "dc-dbg-zero-out-desc-cnt": dc_dbg_zero_out_desc_cnt,
       "dc-dbg-dch-func-status-fail": dc_dbg_dch_func_status_fail,
       "dc-dbg-dch-ch-prov-fail": dc_dbg_dch_ch_prov_fail,
       "dc-dbg-dch-ch-pop-fail": dc_dbg_dch_ch_pop_fail,
       "dc-dbg-dch-ch-free-fail": dc_dbg_dch_ch_free_fail,
       "dc-dbg-bad-compress": dc_dbg_bad_compress,
       "dc-dbg-func-type-fail": dc_dbg_func_type_fail,
       "dc-dbg-chan-num-fail": dc_dbg_chan_num_fail,
       "dc-dbg-chan-stat-fail": dc_dbg_chan_stat_fail,
       "dc-dbg-chan-reset-fail": dc_dbg_chan_reset_fail,
       "dc-dbg-frm-error": dc_dbg_frm_error,
       "dc-dbg-qpck-cnt-error": dc_dbg_qpck_cnt_error,
       "dc-dbg-dch-ch-nb-fail": dc_dbg_dch_ch_nb_fail,
       "dc-dbg-reset-stat-fail": dc_dbg_reset_stat_fail,
       "dc-dbg-chan-status-fail": dc_dbg_chan_status_fail,
       "dc-dbg-param-error": dc_dbg_param_error,
       "dc-dbg-hw-missing": dc_dbg_hw_missing,
       "x32Port-boot": x32Port_boot,
       "x32Port-boot-fail": x32Port_boot_fail,
       "x32Port-disable": x32Port_disable,
       "x32Port-disable-fail": x32Port_disable_fail,
       "x32Port-enable": x32Port_enable,
       "x32Port-enable-fail": x32Port_enable_fail,
       "x32Port-conn-clear": x32Port_conn_clear,
       "x32Port-util-exceeded": x32Port_util_exceeded,
       "x32Port-warn-status": x32Port_warn_status,
       "x32Port-call-thresh-exceed": x32Port_call_thresh_exceed,
       "x32Port-unsucc-call-exceed": x32Port_unsucc_call_exceed,
       "x32Port-t14-timer-expiry": x32Port_t14_timer_expiry,
       "cnui-port-disconn": cnui_port_disconn,
       "cnui-port-locked": cnui_port_locked,
       "cnui-port-degraded": cnui_port_degraded,
       "cnui-no-action": cnui_no_action,
       "dor-agt-tbl-overflow": dor_agt_tbl_overflow,
       "dor-agt-config-err": dor_agt_config_err,
       "dor-unknown-call": dor_unknown_call,
       "dor-comm-error": dor_comm_error,
       "dor-agt-req-abandoned": dor_agt_req_abandoned,
       "dor-stat-overflow": dor_stat_overflow,
       "dor-mgr-config-err": dor_mgr_config_err,
       "dor-link-fail": dor_link_fail,
       "dor-link-up": dor_link_up,
       "dor-mgr-req-abandoned": dor_mgr_req_abandoned,
       "dor-agent-fail": dor_agent_fail,
       "dor-mgr-tbl-overflow": dor_mgr_tbl_overflow,
       "cnui-rrt-boot": cnui_rrt_boot,
       "cnui-rrt-boot-fail": cnui_rrt_boot_fail,
       "cnui-rrt-util-thres-exceed": cnui_rrt_util_thres_exceed,
       "tcp-checksum-error": tcp_checksum_error,
       "tcp-pkt-for-invalid-conn": tcp_pkt_for_invalid_conn,
       "tcp-active-open-sccful": tcp_active_open_sccful,
       "tcp-rcvd-invld-syn": tcp_rcvd_invld_syn,
       "tcp-rcvd-old-syn": tcp_rcvd_old_syn,
       "tcp-rcvd-out-of-wdow-seg": tcp_rcvd_out_of_wdow_seg,
       "tcp-dropping-seg": tcp_dropping_seg,
       "tcp-rcvd-old-seg": tcp_rcvd_old_seg,
       "tcp-rcvd-rst-in-listen": tcp_rcvd_rst_in_listen,
       "tcp-rcvd-rst-in-synrcvd": tcp_rcvd_rst_in_synrcvd,
       "tcp-rcvd-rst-so-aborting": tcp_rcvd_rst_so_aborting,
       "tcp-no-ack-so-dropping": tcp_no_ack_so_dropping,
       "tcp-invld-ack-dropping": tcp_invld_ack_dropping,
       "tcp-rcvd-fin-in-estab": tcp_rcvd_fin_in_estab,
       "tcp-rcvd-push": tcp_rcvd_push,
       "tcp-entering-estab": tcp_entering_estab,
       "tcp-rcvd-fin-in-listen": tcp_rcvd_fin_in_listen,
       "tcp-add-hole-at-end": tcp_add_hole_at_end,
       "tcp-add-hole-at-beg": tcp_add_hole_at_beg,
       "tcp-fill-beg-hole": tcp_fill_beg_hole,
       "tcp-fill-end-hole": tcp_fill_end_hole,
       "tcp-remove-hole": tcp_remove_hole,
       "tcp-too-big-for-rcv-buff": tcp_too_big_for_rcv_buff,
       "tcp-fin-in-invld-state": tcp_fin_in_invld_state,
       "tcp-fin-in-valid-state": tcp_fin_in_valid_state,
       "tcp-appln-rcv-timeout": tcp_appln_rcv_timeout,
       "tcp-illgl-clos-frgn-wndw": tcp_illgl_clos_frgn_wndw,
       "tcp-state-to-synrcvd": tcp_state_to_synrcvd,
       "tcp-state-to-estab": tcp_state_to_estab,
       "tcp-rcvd-tcp-pkt": tcp_rcvd_tcp_pkt,
       "tcp-data-given-to-appln": tcp_data_given_to_appln,
       "tcp-excessive-retries": tcp_excessive_retries,
       "tcp-sending-control-seg": tcp_sending_control_seg,
       "tcp-retransmitting": tcp_retransmitting,
       "tcp-transmitting": tcp_transmitting,
       "tcp-illgl-optn-in-syn": tcp_illgl_optn_in_syn,
       "tcp-zero-wndw-probe": tcp_zero_wndw_probe,
       "tcp-bad-ack-in-synrcvd": tcp_bad_ack_in_synrcvd,
       "tcp-rcvd-ack-in-listen": tcp_rcvd_ack_in_listen,
       "tcp-sending-rst": tcp_sending_rst,
       "tcp-connection-closed": tcp_connection_closed,
       "tcp-firing-tcb-1": tcp_firing_tcb_1,
       "tcp-firing-tcb-2": tcp_firing_tcb_2,
       "tcp-idle-tmr-fires": tcp_idle_tmr_fires,
       "tcp-retransmit-tmr-fires": tcp_retransmit_tmr_fires,
       "tcp-estab-to-finwait": tcp_estab_to_finwait,
       "tcp-state-to-closed": tcp_state_to_closed,
       "tcp-rcvd-data-aftr-close": tcp_rcvd_data_aftr_close,
       "tcp-received-nack": tcp_received_nack,
       "tcp-rcvd-ack-keepalive": tcp_rcvd_ack_keepalive,
       "tcp-local-wndw-zero": tcp_local_wndw_zero,
       "tcp-sending-fin": tcp_sending_fin,
       "tcp-no-buf-to-send-pkt": tcp_no_buf_to_send_pkt,
       "tcp-transmit-buf-clipped": tcp_transmit_buf_clipped,
       "tcp-recv-buf-clipped": tcp_recv_buf_clipped,
       "tcp-restarting": tcp_restarting,
       "tcp-mot-high-prty-trap": tcp_mot_high_prty_trap,
       "tcp-mot-med-prty-trap": tcp_mot_med_prty_trap,
       "tcp-mot-low-prty-trap": tcp_mot_low_prty_trap,
       "telnet-internal-err": telnet_internal_err,
       "telnet-err": telnet_err,
       "async360-err-count-exceeded": async360_err_count_exceeded,
       "async360-dbits-unsupp": async360_dbits_unsupp,
       "async360-baud-unsupp": async360_baud_unsupp,
       "async360-parity-unsupp": async360_parity_unsupp,
       "bop360-err-count-exceeded": bop360_err_count_exceeded,
       "bop360-unsupp-speed": bop360_unsupp_speed,
       "bop360-rx-byte-count-err": bop360_rx_byte_count_err,
       "bop360-erroneous-bool": bop360_erroneous_bool,
       "bop360-clk-override": bop360_clk_override,
       "bop360-tx-sanity-timeout": bop360_tx_sanity_timeout,
       "iodrivers260006-corr": iodrivers260006_corr,
       "cop360-err-count-exceeded": cop360_err_count_exceeded,
       "mc68302drvr-trap": mc68302drvr_trap,
       "mc68360drvr-traps": mc68360drvr_traps,
       "iodrivers-sgnothrottletimer": iodrivers_sgnothrottletimer,
       "iodrivers-sgnoinitializatio": iodrivers_sgnoinitializatio,
       "iodrivers-sgconfigurationfaile": iodrivers_sgconfigurationfaile,
       "iodrivers-sgiafaile": iodrivers_sgiafaile,
       "iodrivers-sgconfigurationtimedout": iodrivers_sgconfigurationtimedout,
       "iodrivers-sgnosuspensio": iodrivers_sgnosuspensio,
       "iodrivers-sgtxlistputfaile": iodrivers_sgtxlistputfaile,
       "iodrivers-sgexcessivetxerror": iodrivers_sgexcessivetxerror,
       "iodrivers-sglossofcarrie": iodrivers_sglossofcarrie,
       "iodrivers-sgexcessiverxerror": iodrivers_sgexcessiverxerror,
       "iodrivers-sgexcessivetxclea": iodrivers_sgexcessivetxclea,
       "iodrivers-sglossofcarrierclea": iodrivers_sglossofcarrierclea,
       "iodrivers-sgexcessiverxclea": iodrivers_sgexcessiverxclea,
       "iodrivers-sginvalidstateenable": iodrivers_sginvalidstateenable,
       "iodrivers-sginvalidstatedisable": iodrivers_sginvalidstatedisable,
       "iodrivers-sgloopbackfaile": iodrivers_sgloopbackfaile,
       "iodrivers-sgtdrfaile": iodrivers_sgtdrfaile,
       "pppPort-boot": pppPort_boot,
       "pppPort-boot-fail": pppPort_boot_fail,
       "pppPort-disable": pppPort_disable,
       "pppPort-enable": pppPort_enable,
       "pppPort-util-exceeded": pppPort_util_exceeded,
       "pppPort-warn-status": pppPort_warn_status,
       "pppPort-err-count-exceeded": pppPort_err_count_exceeded,
       "ppp-allocated-bytes-for-tracing": ppp_allocated_bytes_for_tracing,
       "ppp-port-initialization-failed": ppp_port_initialization_failed,
       "pppL2-out-data-loss": pppL2_out_data_loss,
       "pppL2-frame-reject": pppL2_frame_reject,
       "pppL2-unsupp-proto": pppL2_unsupp_proto,
       "pppL2-vj-comp-fail": pppL2_vj_comp_fail,
       "pppL2-login-fail": pppL2_login_fail,
       "pppL2-login-ok": pppL2_login_ok,
       "ppp-proto-compneg-failed": ppp_proto_compneg_failed,
       "ppp-proto-data-loss": ppp_proto_data_loss,
       "ppp-dedicated-link-not-configure": ppp_dedicated_link_not_configure,
       "ppp-dedicated-link-already-alloc": ppp_dedicated_link_already_alloc,
       "ppp-discarding-frames": ppp_discarding_frames,
       "ppp-received-multilink-frame-wit": ppp_received_multilink_frame_wit,
       "ppp-remote-is-silent": ppp_remote_is_silent,
       "ppp-no-profile-available-for-s": ppp_no_profile_available_for_s,
       "ppp-inconsistent-link-negotiatio": ppp_inconsistent_link_negotiatio,
       "ppp-no-bundles-available": ppp_no_bundles_available,
       "ppp-the-peers-name-exceeds-16-ch": ppp_the_peers_name_exceeds_16_ch,
       "ppp-authentication-was-rejected": ppp_authentication_was_rejected,
       "ppp-link-is-looped-back": ppp_link_is_looped_back,
       "ppp-exceeds-maximum-number-of-li": ppp_exceeds_maximum_number_of_li,
       "ppp-permanent-links-must-configu": ppp_permanent_links_must_configu,
       "pppL2-in-data-loss": pppL2_in_data_loss,
       "pppL2-invalid-encaps": pppL2_invalid_encaps,
       "isdn-lapd-fseq-override": isdn_lapd_fseq_override,
       "isdn-line-active": isdn_line_active,
       "isdn-line-inactive": isdn_line_inactive,
       "isdn-loop-test": isdn_loop_test,
       "isdn-incompatible-detect": isdn_incompatible_detect,
       "isdn-terminal-init-fail": isdn_terminal_init_fail,
       "isdn-Port-boot": isdn_Port_boot,
       "isdn-debug-info": isdn_debug_info,
       "isdn-illegal-port-type": isdn_illegal_port_type,
       "isdn-Port-connected": isdn_Port_connected,
       "isdn-Port-disconnected": isdn_Port_disconnected,
       "isdn-switch-override": isdn_switch_override,
       "isdn-terminal-init": isdn_terminal_init,
       "isdn-dialing-to-on-bri-int-chann": isdn_dialing_to_on_bri_int_chann,
       "isdn-incoming-call-on-bri-int-chan": isdn_incoming_call_on_bri_int_chan,
       "isdn-bri-int-boot-completed": isdn_bri_int_boot_completed,
       "isdn-duplicate-fix-tei-detected": isdn_duplicate_fix_tei_detected,
       "isdn-dial-number-contention": isdn_dial_number_contention,
       "isdn278017-disconnec": isdn278017_disconnec,
       "isdn278018-false-dis": isdn278018_false_dis,
       "isdn278019-isdn-pri": isdn278019_isdn_pri,
       "isdn278020-isdn-pri": isdn278020_isdn_pri,
       "isdn278023-isdn-bri": isdn278023_isdn_bri,
       "isdn278025-qsig-erro": isdn278025_qsig_erro,
       "isdn278026-invalid-q": isdn278026_invalid_q,
       "isdn278027-isdn-bri": isdn278027_isdn_bri,
       "isdn278030-isdn-bri": isdn278030_isdn_bri,
       "isdn278031-isdn-bri": isdn278031_isdn_bri,
       "isdn-lif-packet": isdn_lif_packet,
       "voice-hw-board-fail": voice_hw_board_fail,
       "voice-Port-fail": voice_Port_fail,
       "voice-Port-init-fail": voice_Port_init_fail,
       "voice-Port-not-started": voice_Port_not_started,
       "voice-Port-boot-fail": voice_Port_boot_fail,
       "voice-Port-boot": voice_Port_boot,
       "voice-Port-disable": voice_Port_disable,
       "voice-Port-busyout": voice_Port_busyout,
       "voice-Port-disable-fail": voice_Port_disable_fail,
       "voice-Port-enable": voice_Port_enable,
       "voice-Port-enable-fail": voice_Port_enable_fail,
       "voice-Port-busyout-fail": voice_Port_busyout_fail,
       "vport-virtual-mapping-error-caus": vport_virtual_mapping_error_caus,
       "vport-virtual-mapping-error-caus2": vport_virtual_mapping_error_caus2,
       "vport-voice-record-conversion-co": vport_voice_record_conversion_co,
       "vport-voice-record-conversion-fa": vport_voice_record_conversion_fa,
       "vport-voice-record-conversion-vs": vport_voice_record_conversion_vs,
       "vdcdm-hw-board-failure-cause-bac": vdcdm_hw_board_failure_cause_bac,
       "vdcdm-board-boot-cause-watchdog": vdcdm_board_boot_cause_watchdog,
       "vdcdm-port-failure-cause-missing": vdcdm_port_failure_cause_missing,
       "vdcdm-port-failure-cause-missing2": vdcdm_port_failure_cause_missing2,
       "vdcdm-dspm-software-download-com": vdcdm_dspm_software_download_com,
       "vdcdm-dspm-software-download-fai": vdcdm_dspm_software_download_fai,
       "vdcdm-voice-signaling-trace": vdcdm_voice_signaling_trace,
       "vdcdm-error-on-channel-cause": vdcdm_error_on_channel_cause,
       "vdcdm-dspm-crash-reason-pc-add": vdcdm_dspm_crash_reason_pc_add,
       "vdcdm-dspm-first-recovery-succes": vdcdm_dspm_first_recovery_succes,
       "vdcdm-dspm-second-recovery-succe": vdcdm_dspm_second_recovery_succe,
       "vdcdm-dspm-protocol-initializati": vdcdm_dspm_protocol_initializati,
       "vdcdm-voice-call-calling-called": vdcdm_voice_call_calling_called,
       "vdcdm-voice-vsm-command-eid-3d-o": vdcdm_voice_vsm_command_eid_3d_o,
       "vdcdm-voice-vsm-response-eid-3d": vdcdm_voice_vsm_response_eid_3d,
       "vdcdm281015-voice-trace": vdcdm281015_voice_trace,
       "vdcdm281016-voice-ca": vdcdm281016_voice_ca,
       "vdcdm281017-voice": vdcdm281017_voice,
       "vdcdm281018-dsp-last": vdcdm281018_dsp_last,
       "vdcdm281019-voice": vdcdm281019_voice,
       "t1e1-Port-boot": t1e1_Port_boot,
       "t1e1-Port-boot-fail": t1e1_Port_boot_fail,
       "t1e1-Port-disable": t1e1_Port_disable,
       "t1e1-Port-enable": t1e1_Port_enable,
       "t1e1-Port-not-init": t1e1_Port_not_init,
       "t1e1-Port-vmt-error": t1e1_Port_vmt_error,
       "t1e1-putmsg-failed": t1e1_putmsg_failed,
       "t1e1-comm-error": t1e1_comm_error,
       "t1e1-fatal-error": t1e1_fatal_error,
       "t1e1-dload-failed": t1e1_dload_failed,
       "t1e1-threshold-exceeded": t1e1_threshold_exceeded,
       "t1e1-t1-alarm": t1e1_t1_alarm,
       "t1e1-e1-alarm": t1e1_e1_alarm,
       "t1e1-background-diag": t1e1_background_diag,
       "t1e1-watchdog-expired": t1e1_watchdog_expired,
       "t1e1-illegal-clocking": t1e1_illegal_clocking,
       "t1e1-invalid-message": t1e1_invalid_message,
       "t1e1-pri-b-incoming-call-to-from": t1e1_pri_b_incoming_call_to_from,
       "t1e1-pri-b-outgoing-call-to-conn": t1e1_pri_b_outgoing_call_to_conn,
       "t1e1-pri-call-on-port-disconnect": t1e1_pri_call_on_port_disconnect,
       "t1e1-pri-call-on-port-disconnect2": t1e1_pri_call_on_port_disconnect2,
       "t1e1-pri-incoming-call-to-from-f": t1e1_pri_incoming_call_to_from_f,
       "t1e1-pri-outgoing-call-to-from-f": t1e1_pri_outgoing_call_to_from_f,
       "t1e1-pri-incoming-call-to-from-f2": t1e1_pri_incoming_call_to_from_f2,
       "t1e1-pri-d-channel-up": t1e1_pri_d_channel_up,
       "t1e1-pri-d-channel-down": t1e1_pri_d_channel_down,
       "t1e1-pri-b-b-channel-up": t1e1_pri_b_b_channel_up,
       "t1e1-pri-b-b-channel-down": t1e1_pri_b_b_channel_down,
       "t1e1-virtual-port-config-does-no": t1e1_virtual_port_config_does_no,
       "t1e1-isdn-signaling-message-rece": t1e1_isdn_signaling_message_rece,
       "t1e1-pri-d-channel-establishing": t1e1_pri_d_channel_establishing,
       "t1e1-pri-b-incoming-call-to-from2": t1e1_pri_b_incoming_call_to_from2,
       "t1e1-function-name-sigstate": t1e1_function_name_sigstate,
       "t1e1-t1e1drv-invalid-execution-l": t1e1_t1e1drv_invalid_execution_l,
       "t1e1-pri-d-channel-restarted-all": t1e1_pri_d_channel_restarted_all,
       "t1e1-invalid-pri-signalling-port": t1e1_invalid_pri_signalling_port,
       "t1e1-virtual-port-t1e1-card-does": t1e1_virtual_port_t1e1_card_does,
       "t1e1-virtual-port-no-hdlc-channe": t1e1_virtual_port_no_hdlc_channe,
       "t1e1-virtual-port-no-t1e1-memory": t1e1_virtual_port_no_t1e1_memory,
       "t1e1-pri-call-on-port-disconnect22": t1e1_pri_call_on_port_disconnect22,
       "spfm-pvc-connection-failed-on": spfm_pvc_connection_failed_on,
       "spfm-pvc-connected": spfm_pvc_connected,
       "spfm-disabled-duplicate-slot-on": spfm_disabled_duplicate_slot_on,
       "spfm-disabled-misconfigured-opti": spfm_disabled_misconfigured_opti,
       "spfm-connection-active": spfm_connection_active,
       "spfm-connection-inactive": spfm_connection_inactive,
       "spfm-rx-data-on-unknown-dlci-slo": spfm_rx_data_on_unknown_dlci_slo,
       "spfm-header-format-error": spfm_header_format_error,
       "spfm-configuration-mismatch-on-r": spfm_configuration_mismatch_on_r,
       "spfm-entry-boot-complete": spfm_entry_boot_complete,
       "spfm-entry-boot-failed": spfm_entry_boot_failed,
       "smds-stn-data-loss": smds_stn_data_loss,
       "smds-stn-invalid-encap": smds_stn_invalid_encap,
       "smds-stn-masked": smds_stn_masked,
       "smds-sni-data-loss": smds_sni_data_loss,
       "smds-sni-invalid-encap": smds_sni_invalid_encap,
       "smds-sni-no-station": smds_sni_no_station,
       "dxi-port-boot-complete": dxi_port_boot_complete,
       "dxi-port-boot-failure": dxi_port_boot_failure,
       "dxi-port-disabled": dxi_port_disabled,
       "dxi-port-enabled": dxi_port_enabled,
       "dxi-port-utilization-threshold": dxi_port_utilization_threshold,
       "dxi-port-status-warning": dxi_port_status_warning,
       "dxi-data-lost-from-rx-data-queue": dxi_data_lost_from_rx_data_queue,
       "dxi-data-lost-from-tx-data-queue": dxi_data_lost_from_tx_data_queue,
       "dxi-no-heartbeat": dxi_no_heartbeat,
       "ipxwan-null-rfcm-cb": ipxwan_null_rfcm_cb,
       "ipxwan-not-enough-ram": ipxwan_not_enough_ram,
       "ipxwan-alloc-failed": ipxwan_alloc_failed,
       "ipxwan-module-not-active": ipxwan_module_not_active,
       "ipxwan-ipx-not-active": ipxwan_ipx_not_active,
       "ipxwan-called-for-lan": ipxwan_called_for_lan,
       "ipxwan-nul-ipxwancb": ipxwan_nul_ipxwancb,
       "ipxwan-dropping-packet": ipxwan_dropping_packet,
       "ipxwan-bad-format": ipxwan_bad_format,
       "ipxwan-rcvd-tmr-req-opt-len": ipxwan_rcvd_tmr_req_opt_len,
       "ipxwan-rcvd-tmr-req-wnode-id": ipxwan_rcvd_tmr_req_wnode_id,
       "ipxwan-rcvd-tmr-req-ext-node": ipxwan_rcvd_tmr_req_ext_node,
       "ipxwan-tmr-req-cfg-error": ipxwan_tmr_req_cfg_error,
       "ipxwan-rcvd-tmr-req-no-common-routing": ipxwan_rcvd_tmr_req_no_common_routing,
       "ipxwan-rcvd-tmr-resp-wnode-id": ipxwan_rcvd_tmr_resp_wnode_id,
       "ipxwan-rcvd-tmr-resp-multiple-routing": ipxwan_rcvd_tmr_resp_multiple_routing,
       "ipxwan-rcvd-tmr-resp-routing-type": ipxwan_rcvd_tmr_resp_routing_type,
       "ipxwan-rcvd-tmr-resp-not-supported": ipxwan_rcvd_tmr_resp_not_supported,
       "ipxwan-rcvd-tmr-resp-opt-len": ipxwan_rcvd_tmr_resp_opt_len,
       "ipxwan-rcvd-tmr-resp-header-comp": ipxwan_rcvd_tmr_resp_header_comp,
       "ipxwan-rcvd-tmr-resp-no-routing": ipxwan_rcvd_tmr_resp_no_routing,
       "ipxwan-rcvd-info-req-wnode-id": ipxwan_rcvd_info_req_wnode_id,
       "ipxwan-rcvd-info-info-exchg": ipxwan_rcvd_info_info_exchg,
       "ipxwan-rcvd-info-no-info-exchg": ipxwan_rcvd_info_no_info_exchg,
       "ipxwan-rcvd-info-netno-zero": ipxwan_rcvd_info_netno_zero,
       "ipxwan-rcvd-info-netno-nonzero": ipxwan_rcvd_info_netno_nonzero,
       "ipxwan-rcvd-info-conflict": ipxwan_rcvd_info_conflict,
       "ipxwan-rcvd-info-resp-wnode-id": ipxwan_rcvd_info_resp_wnode_id,
       "ipxwan-rcvd-info-resp-active": ipxwan_rcvd_info_resp_active,
       "ipxwan-rcvd-info-resp-setting": ipxwan_rcvd_info_resp_setting,
       "ipxwan-getbuf-failed": ipxwan_getbuf_failed,
       "ipxwan-unsupported-event": ipxwan_unsupported_event,
       "ipxwan-state-machine": ipxwan_state_machine,
       "ipxwan-internal-buffer-overflow": ipxwan_internal_buffer_overflow,
       "tow-report-no-memory": tow_report_no_memory,
       "tow-report-not-active": tow_report_not_active,
       "tow-report-default-entry": tow_report_default_entry,
       "tow-report-active": tow_report_active,
       "vx-stn-boot-complete": vx_stn_boot_complete,
       "vx-stn-boot-failure": vx_stn_boot_failure,
       "vx-stn-disabled": vx_stn_disabled,
       "vx-stn-enabled": vx_stn_enabled,
       "vx-no-config-for-stn": vx_no_config_for_stn,
       "pnef-tfr-insufficient-memory": pnef_tfr_insufficient_memory,
       "pnef-tfr-boot-failure": pnef_tfr_boot_failure,
       "pnef-tfr-connection-established": pnef_tfr_connection_established,
       "pnef-tfr-connection-failure-with": pnef_tfr_connection_failure_with,
       "pnef-tfr-unknown-caller": pnef_tfr_unknown_caller,
       "pnef-tfr-frame-discarded": pnef_tfr_frame_discarded,
       "pnef-tfr-queue-overflow": pnef_tfr_queue_overflow,
       "pnef-tfr-received-incomplete-fra": pnef_tfr_received_incomplete_fra,
       "pnef-tfri-insufficient-memory-in": pnef_tfri_insufficient_memory_in,
       "pnef-tfri-insufficient-memory-in2": pnef_tfri_insufficient_memory_in2,
       "pnef-tfri-boot-failure": pnef_tfri_boot_failure,
       "pnef-tfri-connection-established": pnef_tfri_connection_established,
       "pnef-tfri-connection-failure-wit": pnef_tfri_connection_failure_wit,
       "pnef-tfri-frame-discarded": pnef_tfri_frame_discarded,
       "pnef-tfri-socket-registration-fa": pnef_tfri_socket_registration_fa,
       "tdlcPort-boot": tdlcPort_boot,
       "tdlcPort-disable": tdlcPort_disable,
       "tdlcPort-enable": tdlcPort_enable,
       "tdlcPort-util-exceeded": tdlcPort_util_exceeded,
       "tdlcPort-statuswarn-disabled": tdlcPort_statuswarn_disabled,
       "tdlcPort-utilexceed-pagingTerm": tdlcPort_utilexceed_pagingTerm,
       "vport-voice-switching-record-fai": vport_voice_switching_record_fai,
       "vport-voice-switching-record-con": vport_voice_switching_record_con,
       "iso3201-Port-boot": iso3201_Port_boot,
       "iso3201-Port-boot-fail": iso3201_Port_boot_fail,
       "iso3201-Port-disable": iso3201_Port_disable,
       "iso3201-Port-disable-fail": iso3201_Port_disable_fail,
       "iso3201-Port-enable": iso3201_Port_enable,
       "iso3201-Port-enable-fail": iso3201_Port_enable_fail,
       "iso3201-Port-warn-status": iso3201_Port_warn_status,
       "iso3201-Stn-boot": iso3201_Stn_boot,
       "iso3201-Stn-boot-fail": iso3201_Stn_boot_fail,
       "iso3201-Stn-disable": iso3201_Stn_disable,
       "iso3201-Stn-disable-fail": iso3201_Stn_disable_fail,
       "iso3201-Stn-enable": iso3201_Stn_enable,
       "iso3201-Stn-enable-fail": iso3201_Stn_enable_fail,
       "iso3201-Stn-warn-status": iso3201_Stn_warn_status,
       "iso3201-Stn-inhibited": iso3201_Stn_inhibited,
       "iso3201-Stn-poll-suspended": iso3201_Stn_poll_suspended,
       "iso3201-Stn-poll-resumed": iso3201_Stn_poll_resumed,
       "iso3201-Stn-mnem-error": iso3201_Stn_mnem_error,
       "iso3201-Stn-acall-exceed": iso3201_Stn_acall_exceed,
       "iso3201-local-commn-error": iso3201_local_commn_error,
       "iso3201-line-status": iso3201_line_status,
       "iso3201-dq-error": iso3201_dq_error,
       "iso3201-data-mesg-error": iso3201_data_mesg_error,
       "iso3201-poll-error-clear": iso3201_poll_error_clear,
       "iso3201-recd-error-mesg": iso3201_recd_error_mesg,
       "iso3201-station-down": iso3201_station_down,
       "gscPort-boot": gscPort_boot,
       "gscPort-boot-fail": gscPort_boot_fail,
       "gscPort-disable": gscPort_disable,
       "gscPort-disable-fail": gscPort_disable_fail,
       "gscPort-enable": gscPort_enable,
       "gscPort-enable-fail": gscPort_enable_fail,
       "gscStn-boot": gscStn_boot,
       "gscStn-boot-fail": gscStn_boot_fail,
       "gscStn-disable": gscStn_disable,
       "gscStn-disable-fail": gscStn_disable_fail,
       "gscStn-enable": gscStn_enable,
       "gscStn-enable-fail": gscStn_enable_fail,
       "gscPort-util-gt-thres": gscPort_util_gt_thres,
       "gscPort-error-thres-exceed": gscPort_error_thres_exceed,
       "gscPort-busyout": gscPort_busyout,
       "gscPort-busyout-fail": gscPort_busyout_fail,
       "gscStnBusyout": gscStnBusyout,
       "gscStn-busyout-fail": gscStn_busyout_fail,
       "gscPort-status-warning": gscPort_status_warning,
       "gscPort-no-broadcast-stns": gscPort_no_broadcast_stns,
       "gsc-memory-allocation-failed": gsc_memory_allocation_failed,
       "gsc-inter-character-timeout": gsc_inter_character_timeout,
       "gsc-checksum-error": gsc_checksum_error,
       "gsc-frame-too-long": gsc_frame_too_long,
       "gsc-unescaped-char-found": gsc_unescaped_char_found,
       "gsc-unexpected-frame": gsc_unexpected_frame,
       "gsc-frame-dropped-after-max-retr": gsc_frame_dropped_after_max_retr,
       "gsc-device-not-responding": gsc_device_not_responding,
       "gsc-messages-lost": gsc_messages_lost,
       "gsc-device-active": gsc_device_active,
       "gsc-link-up": gsc_link_up,
       "gsc-invalid-device-responding": gsc_invalid_device_responding,
       "gsc-solicit-abort": gsc_solicit_abort,
       "gsc-fsm-internal-error": gsc_fsm_internal_error,
       "gsc-wrong-message-address": gsc_wrong_message_address,
       "gsc-link-down": gsc_link_down,
       "gsc-autocall-retries-exhausted": gsc_autocall_retries_exhausted,
       "gsc-station-not-configured": gsc_station_not_configured,
       "gsc-can-not-forward-station-disa": gsc_can_not_forward_station_disa,
       "gsc-inactivity-time-out": gsc_inactivity_time_out,
       "gsc-inbound-link-blocked": gsc_inbound_link_blocked,
       "gsc-inbound-link-unblocked": gsc_inbound_link_unblocked,
       "gsc-outbound-link-blocked": gsc_outbound_link_blocked,
       "gsc-outbound-link-unblocked": gsc_outbound_link_unblocked,
       "tpa-connection-up": tpa_connection_up,
       "tpa-connection-down": tpa_connection_down,
       "tpa-clearing-call-unexpected-q-b": tpa_clearing_call_unexpected_q_b,
       "tpa-sdlc-not-enough-memory": tpa_sdlc_not_enough_memory,
       "tpa-sdlc-idcm-or-tgo-does-not-ex": tpa_sdlc_idcm_or_tgo_does_not_ex,
       "tpa-sdlc-idcm-not-up": tpa_sdlc_idcm_not_up,
       "tpa-clearing-call-bad-or-no-resp": tpa_clearing_call_bad_or_no_resp,
       "tpa-received-ve-responsesense-da": tpa_received_ve_responsesense_da,
       "tpa-retry-exceeded-for-sna-messa": tpa_retry_exceeded_for_sna_messa,
       "tpa-lu-lu-session-cleared-cleari": tpa_lu_lu_session_cleared_cleari,
       "tpa-pu-session-cleared-clearing": tpa_pu_session_cleared_clearing,
       "tpa-pu-session-activated": tpa_pu_session_activated,
       "tpa-lu-session-activated": tpa_lu_session_activated,
       "tpa-invalid-cp-packet-ru-th-rh": tpa_invalid_cp_packet_ru_th_rh,
       "tpa-invalid-lu-packet-ru-th-rh": tpa_invalid_lu_packet_ru_th_rh,
       "tpa-out-of-sequence-packet-event": tpa_out_of_sequence_packet_event,
       "tpa-retries-over-for-sending-bin": tpa_retries_over_for_sending_bin,
       "tpa-tpa3270-connected": tpa_tpa3270_connected,
       "tpa-tpa3270-disconnected": tpa_tpa3270_disconnected,
       "tpdu-tpr-boot-complete": tpdu_tpr_boot_complete,
       "tpdu-tpr-slot-boot-complete": tpdu_tpr_slot_boot_complete,
       "tpdu-tpr-boot-failure-number-of": tpdu_tpr_boot_failure_number_of,
       "tpdu-tpr-slot-no-boot-failure-sl": tpdu_tpr_slot_no_boot_failure_sl,
       "tpdu-tpr-init-failed": tpdu_tpr_init_failed,
       "tpdu-tpr-initslot-tpa-module-doe": tpdu_tpr_initslot_tpa_module_doe,
       "tpdu-tpr-initslot-tpa-module-ini": tpdu_tpr_initslot_tpa_module_ini,
       "tpdu-tpr-slot-enabled": tpdu_tpr_slot_enabled,
       "tpdu-tpr-slot-disabled": tpdu_tpr_slot_disabled,
       "tpdu-tpr-fwd-packet-for-dead-slo": tpdu_tpr_fwd_packet_for_dead_slo,
       "tpdu-session-is-in-progress-with": tpdu_session_is_in_progress_with,
       "tpdu-invalid-session-message-in": tpdu_invalid_session_message_in,
       "tpdu-session-aborted-invalid-ses": tpdu_session_aborted_invalid_ses,
       "tpdu-session-aborted-got-session": tpdu_session_aborted_got_session,
       "tpdu-session-aborted-got-invitat": tpdu_session_aborted_got_invitat,
       "tpdu-session-aborted-got-illegal": tpdu_session_aborted_got_illegal,
       "tpdu-session-aborted-data-when-o": tpdu_session_aborted_data_when_o,
       "tpdu-session-aborted-got-call-cl": tpdu_session_aborted_got_call_cl,
       "tpdu-session-aborted-got-call-re": tpdu_session_aborted_got_call_re,
       "tpdu-session-aborted-got-call-ac": tpdu_session_aborted_got_call_ac,
       "tpdu-session-aborted-got-data-fr": tpdu_session_aborted_got_data_fr,
       "tpdu-session-closed": tpdu_session_closed,
       "tpdu-session-established-with-sl": tpdu_session_established_with_sl,
       "tpdu-data-in-idle-state-from-slo": tpdu_data_in_idle_state_from_slo,
       "tpdu-session-closed-got-call-req": tpdu_session_closed_got_call_req,
       "tpdu-session-closed-got-call-acc": tpdu_session_closed_got_call_acc,
       "tpdu-session-closed-got-illegal": tpdu_session_closed_got_illegal,
       "tpdu-packet-allocation-failed": tpdu_packet_allocation_failed,
       "tpdu-not-enough-memory": tpdu_not_enough_memory,
       "tpdu-session-closed-got-invalid": tpdu_session_closed_got_invalid,
       "tpdu-discarded-session-message-f": tpdu_discarded_session_message_f,
       "tpdu-session-stataus-message-cou": tpdu_session_stataus_message_cou,
       "sppPort-boot": sppPort_boot,
       "sppPort-boot-fail": sppPort_boot_fail,
       "sppPort-disable": sppPort_disable,
       "sppPort-disable-fail": sppPort_disable_fail,
       "sppPort-enable": sppPort_enable,
       "sppPort-enable-fail": sppPort_enable_fail,
       "sppStn-disable": sppStn_disable,
       "sppStn-disable-fail": sppStn_disable_fail,
       "sppStn-enable": sppStn_enable,
       "sppStn-enable-fail": sppStn_enable_fail,
       "sppPort-util-exceeded": sppPort_util_exceeded,
       "sppPort-warn-status": sppPort_warn_status,
       "sppPort-bad-tid": sppPort_bad_tid,
       "sppPort-bad-pid": sppPort_bad_pid,
       "spp-stn-warn-status": spp_stn_warn_status,
       "xlb-insufficient-memory-for-tran": xlb_insufficient_memory_for_tran,
       "xlb-module-initialized": xlb_module_initialized,
       "tpa-x25-not-enough-memory": tpa_x25_not_enough_memory,
       "tpa-connection-up2": tpa_connection_up2,
       "tpa-connection-down2": tpa_connection_down2,
       "tpa-connection-is-in-progress": tpa_connection_is_in_progress,
       "tpa-x25-idcm-or-tgo-does-not-exi": tpa_x25_idcm_or_tgo_does_not_exi,
       "tpa-x25-idcm-not-up": tpa_x25_idcm_not_up,
       "tpa-maximum-autocall-attempts-fa": tpa_maximum_autocall_attempts_fa,
       "igmp-1-rfcm": igmp_1_rfcm,
       "igmp-2-igmp-module": igmp_2_igmp_module,
       "igmp-3-mem-alloc-failed": igmp_3_mem_alloc_failed,
       "igmp-4-module-not-up": igmp_4_module_not_up,
       "igmp-5-packet-error": igmp_5_packet_error,
       "igmp-6-buffer-failure": igmp_6_buffer_failure,
       "igmp-7-group-insert-fail": igmp_7_group_insert_fail,
       "igmp-8-debug-trap": igmp_8_debug_trap,
       "igmp-9-packet-dropped": igmp_9_packet_dropped,
       "igmp-10-multicast-not-enabled": igmp_10_multicast_not_enabled,
       "igmp-11-debug-trap": igmp_11_debug_trap,
       "igmp-12-debug-trap": igmp_12_debug_trap,
       "igmp-13-null-context-block": igmp_13_null_context_block,
       "igmp-14-packet-received": igmp_14_packet_received,
       "igmp-15-membership-query": igmp_15_membership_query,
       "igmp-16-membership-report": igmp_16_membership_report,
       "igmp-17-membership-report-ver2": igmp_17_membership_report_ver2,
       "igmp-18-membership-leave-msg": igmp_18_membership_leave_msg,
       "igmp-19-unknown-group-member": igmp_19_unknown_group_member,
       "igmp-20-unknown-packet": igmp_20_unknown_packet,
       "igmp-21-group-membership-timeout": igmp_21_group_membership_timeout,
       "router-dvmrp1-dvmrpinit-called-w": router_dvmrp1_dvmrpinit_called_w,
       "router-dvmrp2-dvmrp-module-abort": router_dvmrp2_dvmrp_module_abort,
       "tpa-tcp-not-enough-memory": tpa_tcp_not_enough_memory,
       "tpa-connection-down22": tpa_connection_down22,
       "tpa-tcp-tcp-does-not-exist": tpa_tcp_tcp_does_not_exist,
       "tpa-tpatcpqueue-fullpacket-dropp": tpa_tpatcpqueue_fullpacket_dropp,
       "tpa-tpatcptcp-send-failed-connec": tpa_tpatcptcp_send_failed_connec,
       "tpa-tpatcppacket-allocation-fail": tpa_tpatcppacket_allocation_fail,
       "tpa-tpatcpconnection-retries-ove": tpa_tpatcpconnection_retries_ove,
       "tpa-tpatcptcp-listen-failed": tpa_tpatcptcp_listen_failed,
       "tpa-tpatcptcp-active-open-failed": tpa_tpatcptcp_active_open_failed,
       "tpa-tpatcppacket-with-m-bit-from": tpa_tpatcppacket_with_m_bit_from,
       "tpa-connection-up22": tpa_connection_up22,
       "tpa-timeout-from-tcp": tpa_timeout_from_tcp,
       "tpa-tpatcptcp-timeout-discarding": tpa_tpatcptcp_timeout_discarding,
       "tpa-connection-down222": tpa_connection_down222,
       "tpa-udp-not-enough-memory": tpa_udp_not_enough_memory,
       "tpa-udp-udp-does-not-exist": tpa_udp_udp_does_not_exist,
       "tpa-udp-registration-with-udp-fa": tpa_udp_registration_with_udp_fa,
       "tpa-udp-registration-with-sip-fa": tpa_udp_registration_with_sip_fa,
       "sotcp-init-failed-insufficient-m": sotcp_init_failed_insufficient_m,
       "sotcp-init-failed-software-absen": sotcp_init_failed_software_absen,
       "sotcp-no-more-tcp-sessions": sotcp_no_more_tcp_sessions,
       "sotcp-tcp-listen-failed-trying-a": sotcp_tcp_listen_failed_trying_a,
       "sotcp-tcp-receive-failed-session": sotcp_tcp_receive_failed_session,
       "sotcp-invalid-packet": sotcp_invalid_packet,
       "sotcp-tcp-active-open-failed-wit": sotcp_tcp_active_open_failed_wit,
       "sotcp-tcp-session-established-wi": sotcp_tcp_session_established_wi,
       "sotcp-memory-allocation-failed": sotcp_memory_allocation_failed,
       "sotcp-no-more-connections": sotcp_no_more_connections,
       "sotcp-tcp-session-timed-out-with": sotcp_tcp_session_timed_out_with,
       "sotcp-tcp-session-closed-by-the": sotcp_tcp_session_closed_by_the,
       "sotcp-session-closed": sotcp_session_closed,
       "sotcp-new-connection-with-connec": sotcp_new_connection_with_connec,
       "sotcp-c-packet-allocation-failed": sotcp_c_packet_allocation_failed,
       "sotcp-c-serial-protocol-blocked": sotcp_c_serial_protocol_blocked,
       "sotcp-no-matching-ip-peer-for": sotcp_no_matching_ip_peer_for,
       "sotcp-queue-toward-tcp-blocked": sotcp_queue_toward_tcp_blocked,
       "sotcp-queue-toward-tcp-unblocked": sotcp_queue_toward_tcp_unblocked,
       "sotcp-c-data-loss-due-to-queue-o": sotcp_c_data_loss_due_to_queue_o,
       "sotcp-udp-registration-failure": sotcp_udp_registration_failure,
       "sotcp-c-remote-does-not-support": sotcp_c_remote_does_not_support,
       "sotcp-init-failed-idcm-init-fail": sotcp_init_failed_idcm_init_fail,
       "sotcp-udp-module-absent-voice": sotcp_udp_module_absent_voice,
       "sotcp331024-sotcp-ma": sotcp331024_sotcp_ma,
       "sotcp331025-sotcp-c": sotcp331025_sotcp_c,
       "sotcp331026-sotcp-cr": sotcp331026_sotcp_cr,
       "flash-multi-config-request": flash_multi_config_request,
       "vconfig-voice-port-failed-to-dow": vconfig_voice_port_failed_to_dow,
       "vconfig-voice-port-boot-complete": vconfig_voice_port_boot_complete,
       "vr-download-failed-insuf-memory": vr_download_failed_insuf_memory,
       "vr-download-failed-vsmio": vr_download_failed_vsmio,
       "vr339002-download-fa": vr339002_download_fa,
       "vhardware340000-vhwv": vhardware340000_vhwv,
       "idim-port-i430-dim-installed-on": idim_port_i430_dim_installed_on,
       "idim-i430-dim-in-sync": idim_i430_dim_in_sync,
       "idim-i430-dim-out-of-sync": idim_i430_dim_out_of_sync,
       "h323-internal-error": h323_internal_error,
       "h323-error": h323_error,
       "h323-ip-error": h323_ip_error,
       "h323-h323": h323_h323,
       "h323-not-hdld-in": h323_not_hdld_in,
       "h323-qsig-msg-not-handled": h323_qsig_msg_not_handled,
       "h323-tcp": h323_tcp,
       "h323-msd-error": h323_msd_error,
       "h323-rtp-discard": h323_rtp_discard,
       "h323-unknown-rtp-payload-type": h323_unknown_rtp_payload_type,
       "h323-sequence-numbers": h323_sequence_numbers,
       "h323-ssrc-mismatch": h323_ssrc_mismatch,
       "h323342012-h323-unhandled-msg": h323342012_h323_unhandled_msg,
       "h323342014-info": h323342014_info,
       "tpa-tpa2780-connected": tpa_tpa2780_connected,
       "tpa-tpa2780-disconnected": tpa_tpa2780_disconnected,
       "tpa-connection-up222": tpa_connection_up222,
       "tpa-connection-down2222": tpa_connection_down2222,
       "tpa-connection-is-in-progress2": tpa_connection_is_in_progress2,
       "tpa-clearing-call-remote-station": tpa_clearing_call_remote_station,
       "tpa-fra-not-enough-memory": tpa_fra_not_enough_memory,
       "tpa-fra-idcm-or-tgo-does-not-exi": tpa_fra_idcm_or_tgo_does_not_exi,
       "tpa-fra-idcm-not-up": tpa_fra_idcm_not_up,
       "tpa-clearing-call-bad-response": tpa_clearing_call_bad_response,
       "router-udp-registration-failure": router_udp_registration_failure,
       "router-proxy-ignoredip-interface": router_proxy_ignoredip_interface,
       "router-proxy-ignored-has-duplica": router_proxy_ignored_has_duplica,
       "router-proxy-specifying-interfac": router_proxy_specifying_interfac,
       "router-proxies-restarted": router_proxies_restarted,
       "router-proxy-enabled": router_proxy_enabled,
       "router-proxy-disabled": router_proxy_disabled,
       "ac100-port-boot-complete": ac100_port_boot_complete,
       "ac100-port-boot-failure": ac100_port_boot_failure,
       "ac100-port-disabled": ac100_port_disabled,
       "ac100-port-disable-failure": ac100_port_disable_failure,
       "ac100-port-enabled": ac100_port_enabled,
       "ac100-port-enable-failure": ac100_port_enable_failure,
       "ac100-port-status-warning": ac100_port_status_warning,
       "ac100-site-boot-complete": ac100_site_boot_complete,
       "ac100-site-boot-failure": ac100_site_boot_failure,
       "ac100-site-disabled": ac100_site_disabled,
       "ac100-site-disable-failure": ac100_site_disable_failure,
       "ac100-site-enabled": ac100_site_enabled,
       "ac100-site-enable-failure": ac100_site_enable_failure,
       "ac100-site-alive": ac100_site_alive,
       "ac100-site-dead": ac100_site_dead,
       "ac100-data-error": ac100_data_error,
       "ac100-errmesg": ac100_errmesg,
       "ac100-duplicate-site-address": ac100_duplicate_site_address,
       "x25-bcug-table-overflow": x25_bcug_table_overflow,
       "x25-bcug-duplicate-bcug-entries": x25_bcug_duplicate_bcug_entries,
       "ccs-line-is-active007": ccs_line_is_active007,
       "ccs-line-is-inactive": ccs_line_is_inactive,
       "ccs-incompatible-detected": ccs_incompatible_detected,
       "ccs-boot-completed": ccs_boot_completed,
       "ccs-connected-to-port": ccs_connected_to_port,
       "ccs-disconnected-from-port-cause": ccs_disconnected_from_port_cause,
       "ccs-frame-sequencing-override": ccs_frame_sequencing_override,
       "ns360000-null-address": ns360000_null_address,
       "ns360001-failed-to-map": ns360001_failed_to_map,
       "ns360002-get-add-map": ns360002_get_add_map,
       "ns361000-x25-rch-tbl": ns361000_x25_rch_tbl,
       "ns361001-inccalls": ns361001_inccalls,
       "ns361002-deleted-link": ns361002_deleted_link,
       "ns361003-entry-created": ns361003_entry_created,
       "ns361004-nos-apce-to-create-entry": ns361004_nos_apce_to_create_entry,
       "ns361005-duplicate-entry": ns361005_duplicate_entry,
       "ns361006-getlink-found-conn": ns361006_getlink_found_conn,
       "ns361007-statechange": ns361007_statechange,
       "ns361008-deccalls-cleared-link": ns361008_deccalls_cleared_link,
       "ns361009-deccalls-one": ns361009_deccalls_one,
       "ns361010-deccalls-last-call": ns361010_deccalls_last_call,
       "ns361011-statechange-fail": ns361011_statechange_fail,
       "vbcst-state-not-found-for": vbcst_state_not_found_for,
       "vbcst-state-table-not-found": vbcst_state_table_not_found,
       "vbcst-no-entry-for-event-in": vbcst_no_entry_for_event_in,
       "vbcst-process-event-in": vbcst_process_event_in,
       "vbcst-10-loops-for-event-in": vbcst_10_loops_for_event_in,
       "vbcst-call-cleared-incompatible": vbcst_call_cleared_incompatible,
       "vbcst-call-cleared-incompatible-2": vbcst_call_cleared_incompatible_2,
       "t1e1vg-remote-loopback-in-progre": t1e1vg_remote_loopback_in_progre,
       "t1e1vg-remote-loopback-ended": t1e1vg_remote_loopback_ended,
       "vport-cvs-module-failed-initiali": vport_cvs_module_failed_initiali,
       "vport-cvs-no-digit-string-matchi": vport_cvs_no_digit_string_matchi,
       "vport-cvs-connection-to-terminat": vport_cvs_connection_to_terminat,
       "vport-cvs-invalid-execution-line": vport_cvs_invalid_execution_line,
       "vport-cvs-centralized-voice-swit": vport_cvs_centralized_voice_swit,
       "vport-cvs-centralized-voice-swit2": vport_cvs_centralized_voice_swit2,
       "vport-cvs": vport_cvs,
       "vport-cvs-cvs-table-copy-complet": vport_cvs_cvs_table_copy_complet,
       "vport-cvs-state-event-new-state": vport_cvs_state_event_new_state,
       "ccs-lapf-ctl-protocol-link-up": ccs_lapf_ctl_protocol_link_up,
       "ccs-lapf-ctl-protocol-link-down": ccs_lapf_ctl_protocol_link_down,
       "ccs-svc-station-activated": ccs_svc_station_activated,
       "ccs-svc-station-deactivated": ccs_svc_station_deactivated,
       "encrypt-simm-is-defective": encrypt_simm_is_defective,
       "encrypt-insufficient-memory": encrypt_insufficient_memory,
       "encrypt-established-session": encrypt_established_session,
       "encrypt-cannot-create-session": encrypt_cannot_create_session,
       "encrypt-failed-key-exchange": encrypt_failed_key_exchange,
       "encrypt-failed-key-exchange-no-response": encrypt_failed_key_exchange_no_response,
       "encrypt-node-key-not-configured": encrypt_node_key_not_configured,
       "encrypt-bad-base-keys-in-cmem": encrypt_bad_base_keys_in_cmem,
       "encrypt-abnormal-ns-command": encrypt_abnormal_ns_command,
       "encrypt-configuring-more-channels-than-hw-can-support": encrypt_configuring_more_channels_than_hw_can_support,
       "encrypt-node-key-changed": encrypt_node_key_changed,
       "encrypt-base-key-changed": encrypt_base_key_changed,
       "encrypt-good-base-key-in-cmem": encrypt_good_base_key_in_cmem,
       "encrypt-remote-reset-from-remote-encryption-peer": encrypt_remote_reset_from_remote_encryption_peer,
       "encrypt-test-error": encrypt_test_error,
       "encrypt-mis-configured": encrypt_mis_configured,
       "encrypt-invalid-attempt-to-connect-ap-to-ap": encrypt_invalid_attempt_to_connect_ap_to_ap,
       "encrypt-booted-encryption-key": encrypt_booted_encryption_key,
       "encrypt-booted-encryption-profile": encrypt_booted_encryption_profile,
       "encrypt-deleted-all-encryption-keys": encrypt_deleted_all_encryption_keys,
       "encrypt-data-encryption-disabled": encrypt_data_encryption_disabled,
       "encrypt-IV-usage-forced-by-remote-peer": encrypt_IV_usage_forced_by_remote_peer,
       "encrypt-simm-bad-or-not-installed": encrypt_simm_bad_or_not_installed,
       "crc-last-two-chars": crc_last_two_chars,
       "tcpdriver-tcp-listen-failed": tcpdriver_tcp_listen_failed,
       "tcpdriver-session-established": tcpdriver_session_established,
       "tcpdriver-session-closed": tcpdriver_session_closed,
       "tcpdriver-l2-packet-size-exceed": tcpdriver_l2_packet_size_exceed,
       "tcpdriver-tcp-packet-size-exceed": tcpdriver_tcp_packet_size_exceed,
       "tcpdriver-list-full": tcpdriver_list_full,
       "tcpdriver-tcp-send-failed": tcpdriver_tcp_send_failed,
       "dlcm-syserr": dlcm_syserr,
       "appncm-appn-cm-syserr": appncm_appn_cm_syserr,
       "appncm-insufficient-memory": appncm_insufficient_memory,
       "snap-syserr": snap_syserr,
       "snap-snap": snap_snap,
       "snap-tp-started-req": snap_tp_started_req,
       "snap-rcv-alloc-req": snap_rcv_alloc_req,
       "snap-tp-started-rsp": snap_tp_started_rsp,
       "snap-rcv-alloc-rsp": snap_rcv_alloc_rsp,
       "snap-tp-ended-req": snap_tp_ended_req,
       "snap-tp-ended-rsp": snap_tp_ended_rsp,
       "lu62map-error-in-appc-verb-resp": lu62map_error_in_appc_verb_resp,
       "lu62map-5494-retry-limit-reached": lu62map_5494_retry_limit_reached,
       "lu62map-event-in-wrong-state": lu62map_event_in_wrong_state,
       "lu62map-null-pointer-on-line": lu62map_null_pointer_on_line,
       "lu62map-failed-to-get-snap-sock": lu62map_failed_to_get_snap_sock,
       "lu62map-received-unknown-sna-ev": lu62map_received_unknown_sna_ev,
       "lu62map-failure-returned": lu62map_failure_returned,
       "lu62map-incorrect-header": lu62map_incorrect_header,
       "lu62map-received-unknown-resp": lu62map_received_unknown_resp,
       "lu62map-5494-controller-up": lu62map_5494_controller_up,
       "lu62map-5494-controller-down": lu62map_5494_controller_down,
       "lu62map-received-unexpected-mess": lu62map_received_unexpected_mess,
       "lu62map-received-unknown-tpid": lu62map_received_unknown_tpid,
       "lu62map-received-too-many-recv": lu62map_received_too_many_recv,
       "lu62map-received-unknown-lu4lu7": lu62map_received_unknown_lu4lu7,
       "lu62map-lu4lu7-incorrect-header": lu62map_lu4lu7_incorrect_header,
       "lu62map-5494-workstation-down": lu62map_5494_workstation_down,
       "lu62map-5494-workstation-up": lu62map_5494_workstation_up,
       "lu62map-lu62map": lu62map_lu62map,
       "lu62map-dactlu-in-unexpected-state": lu62map_dactlu_in_unexpected_state,
       "lu62map-received-lustat": lu62map_received_lustat,
       "lu62map-received-actlu": lu62map_received_actlu,
       "lu62map-bad-struct-id": lu62map_bad_struct_id,
       "lu62map-received-nonpip-alloc": lu62map_received_nonpip_alloc,
       "lu62map-received-data-from-qllc": lu62map_received_data_from_qllc,
       "lu62map-null-pointer-on-line2": lu62map_null_pointer_on_line2,
       "lu62map-event-in-wrong-state2": lu62map_event_in_wrong_state2,
       "lu62map-unknown-lu": lu62map_unknown_lu,
       "lu62map385028-5494-station": lu62map385028_5494_station,
       "lu62map385029-5494-remote-conn": lu62map385029_5494_remote_conn,
       "lu62map385030-5494-remote-call": lu62map385030_5494_remote_call,
       "lu62map385031-qllcpa": lu62map385031_qllcpa,
       "lu62map385032-handle": lu62map385032_handle,
       "lu62map385033-sendou": lu62map385033_sendou,
       "lu62map385034-purgeq": lu62map385034_purgeq,
       "lu62map385035-sendqu": lu62map385035_sendqu,
       "lu62map385036-sendup": lu62map385036_sendup,
       "qos-not-operational": qos_not_operational,
       "qos-memory-allocation-failure": qos_memory_allocation_failure,
       "qos-total-percentage-exceeds-100": qos_total_percentage_exceeds_100,
       "qos-total-percentage-changed": qos_total_percentage_changed,
       "h323392000-h323-node": h323392000_h323_node,
       "h323392001-h323-node": h323392001_h323_node,
       "h323392002-no-h323-n": h323392002_no_h323_n,
       "iodrivers396000-port": iodrivers396000_port,
       "iodrivers396001-unsu": iodrivers396001_unsu,
       "iodrivers396002-unsu": iodrivers396002_unsu,
       "iodrivers396003-erro": iodrivers396003_erro,
       "iodrivers396004-cloc": iodrivers396004_cloc,
       "iodrivers396005-tx-s": iodrivers396005_tx_s,
       "iodrivers396006-corr": iodrivers396006_corr,
       "qoskit400000-qos-failure": qoskit400000_qos_failure,
       "qoskit400001-qos-warning": qoskit400001_qos_warning,
       "qoskit402000-qos-sched-be": qoskit402000_qos_sched_be,
       "pbr-rept-space-unavailable": pbr_rept_space_unavailable,
       "pbr-rept-ctp-error": pbr_rept_ctp_error,
       "pbr-rept-flow-active": pbr_rept_flow_active,
       "pbr-rept-flow-dropped": pbr_rept_flow_dropped,
       "pbr-rept-flow-expired": pbr_rept_flow_expired,
       "pbr-rept-flow-out-of-tow": pbr_rept_flow_out_of_tow,
       "pbr-rept-flow-nxthop-down": pbr_rept_flow_nxthop_down,
       "pbr-rept-flow-revert-to-primary": pbr_rept_flow_revert_to_primary,
       "pbr-rept-cache-cleared": pbr_rept_cache_cleared,
       "pbr-rept-cache-overflow": pbr_rept_cache_overflow,
       "ruihc-rept-nomem": ruihc_rept_nomem,
       "ruihc-rept-ctxtoverflow": ruihc_rept_ctxtoverflow,
       "ruihc-rept-newentryinctxt": ruihc_rept_newentryinctxt,
       "ruihc-rept-compressionstart": ruihc_rept_compressionstart,
       "ruihc-rept-ctxtentry-tmout": ruihc_rept_ctxtentry_tmout,
       "ruihc-rept-movetonegcache": ruihc_rept_movetonegcache,
       "ruihc-rept-ctxtstpktrcvd": ruihc_rept_ctxtstpktrcvd,
       "ruihc-rept-ctxtnoexist": ruihc_rept_ctxtnoexist,
       "ruihc-rept-ctxtidmismatch": ruihc_rept_ctxtidmismatch,
       "ruihc-rept-nomem4newpkt": ruihc_rept_nomem4newpkt,
       "ruihc-rept-conntypmismatch": ruihc_rept_conntypmismatch,
       "ruihc-rept-decompctxtnoexist": ruihc_rept_decompctxtnoexist,
       "t1e1vg-HardwareFailed-OS": t1e1vg_HardwareFailed_OS,
       "t1e1vg-HardwareFailed-DRV": t1e1vg_HardwareFailed_DRV,
       "t1e1vg-HardwareFailed-ME": t1e1vg_HardwareFailed_ME,
       "t1e1vg-HardwareFailed-DSL": t1e1vg_HardwareFailed_DSL,
       "t1e1vg-ConfigurationMismatch": t1e1vg_ConfigurationMismatch,
       "t1e1vg-CMEM-error": t1e1vg_CMEM_error,
       "t1e1vg-RemoteLoopback-InProgress": t1e1vg_RemoteLoopback_InProgress,
       "t1e1vg-RemoteLoopback-End": t1e1vg_RemoteLoopback_End,
       "t1e1vg-RAI-cleared": t1e1vg_RAI_cleared,
       "t1e1vg-LOF-cleared": t1e1vg_LOF_cleared,
       "t1e1vg-LOS-cleared": t1e1vg_LOS_cleared,
       "t1e1vg-AIS-cleared": t1e1vg_AIS_cleared,
       "t1e1vg-RAI-alarm": t1e1vg_RAI_alarm,
       "t1e1vg-LOF-alarm": t1e1vg_LOF_alarm,
       "t1e1vg-LOS-alarm": t1e1vg_LOS_alarm,
       "t1e1vg-AIS-alarm": t1e1vg_AIS_alarm,
       "t1e1vg-YELLOW-cleared": t1e1vg_YELLOW_cleared,
       "t1e1vg-RED-cleared": t1e1vg_RED_cleared,
       "t1e1vg-BLUE-cleared": t1e1vg_BLUE_cleared,
       "t1e1vg-YELLOW-alarm": t1e1vg_YELLOW_alarm,
       "t1e1vg-RED-alarm": t1e1vg_RED_alarm,
       "t1e1vg-BLUE-alarm": t1e1vg_BLUE_alarm,
       "t1e1vg-LES-thresholdExceed": t1e1vg_LES_thresholdExceed,
       "t1e1vg-LCV-thresholdExceed": t1e1vg_LCV_thresholdExceed,
       "t1e1vg-PCV-thresholdExceed": t1e1vg_PCV_thresholdExceed,
       "t1e1vg-CSS-thresholdExceed": t1e1vg_CSS_thresholdExceed,
       "t1e1vg-ES-thresholdExceed": t1e1vg_ES_thresholdExceed,
       "t1e1vg-BES-thresholdExceed": t1e1vg_BES_thresholdExceed,
       "t1e1vg-SES-thresholdExceed": t1e1vg_SES_thresholdExceed,
       "t1e1vg-SEFS-thresholdExceed": t1e1vg_SEFS_thresholdExceed,
       "t1e1vg-UAS-thresholdExceed": t1e1vg_UAS_thresholdExceed,
       "tdm-clk-ModuleFail-OS": tdm_clk_ModuleFail_OS,
       "tdm-clk-NetworkClock-lost": tdm_clk_NetworkClock_lost,
       "tdm-clk-NetworkClock-dedrives": tdm_clk_NetworkClock_dedrives,
       "vpmt-ModuleFail-OS": vpmt_ModuleFail_OS,
       "vpmt-ModuleFail-VPMT": vpmt_ModuleFail_VPMT,
       "vpmt-ModuleFail-VPMT-CB": vpmt_ModuleFail_VPMT_CB,
       "isdn-isdn-pri-ACTIVE": isdn_isdn_pri_ACTIVE,
       "isdn-isdn-pri-INACTIVE": isdn_isdn_pri_INACTIVE,
       "isdn-isdn-pri-CALL-IN-FROM-NUM": isdn_isdn_pri_CALL_IN_FROM_NUM,
       "isdn-isdn-pri-CALL-IN-FROM-UNKNOWN": isdn_isdn_pri_CALL_IN_FROM_UNKNOWN,
       "isdn-isdn-pri-CALL-OUT": isdn_isdn_pri_CALL_OUT,
       "aam405000-port-boot": aam405000_port_boot,
       "aam405001-port-disab": aam405001_port_disab,
       "aam405002-port-enabl": aam405002_port_enabl,
       "aam405003-port-utili": aam405003_port_utili,
       "aam405004-station-di": aam405004_station_di,
       "aam405005-station-en": aam405005_station_en,
       "aam405006-station-bo": aam405006_station_bo,
       "aam405007-port-statu": aam405007_port_statu,
       "aam405008-out-of-mem": aam405008_out_of_mem,
       "aamsar407000-port-er": aamsar407000_port_er,
       "aamsar407001-vcc-err": aamsar407001_vcc_err,
       "aamsar407002-wrong-a": aamsar407002_wrong_a,
       "aamsar407003-data-fr": aamsar407003_data_fr,
       "aamsar407004-aal5-cp": aamsar407004_aal5_cp,
       "aamsar407005-aal5-cp": aamsar407005_aal5_cp,
       "aamsar407006-aal5-cp": aamsar407006_aal5_cp,
       "aamsar407007-aal5-cp": aamsar407007_aal5_cp,
       "aamsar407008-port-in": aamsar407008_port_in,
       "aamsar407009-unable": aamsar407009_unable,
       "aamsar407010-unable": aamsar407010_unable,
       "aamsar407011-unable": aamsar407011_unable,
       "aamsar407012-unable": aamsar407012_unable,
       "aamsar407013-unable": aamsar407013_unable,
       "aamsar407014-unable": aamsar407014_unable,
       "aamsar407015-unable": aamsar407015_unable,
       "aamsar407016-unable": aamsar407016_unable,
       "aamsar407017-unable": aamsar407017_unable,
       "aamsar407018-unable": aamsar407018_unable,
       "aamsar407019-unable": aamsar407019_unable,
       "aamsar407020-unable": aamsar407020_unable,
       "aamsar407021-unable": aamsar407021_unable,
       "aamsar407022-unable": aamsar407022_unable,
       "aamsar407023-unable": aamsar407023_unable,
       "aamsar407024-unable": aamsar407024_unable,
       "aamsar407025-vcc-ava": aamsar407025_vcc_ava,
       "aamsar407026-error-w": aamsar407026_error_w,
       "aamsar407027-error-w": aamsar407027_error_w,
       "aamsar407028-error-w": aamsar407028_error_w,
       "aamsar407029-unable": aamsar407029_unable,
       "aamsar407030-unable": aamsar407030_unable,
       "aamsar407031-unable": aamsar407031_unable,
       "aamsar407032-unable": aamsar407032_unable,
       "aamsar407033-unable": aamsar407033_unable,
       "aamsar407034-wrong-p": aamsar407034_wrong_p,
       "aamsar407035-wrong-v": aamsar407035_wrong_v,
       "iodrivers411000-port": iodrivers411000_port,
       "iodrivers411001-unsu": iodrivers411001_unsu,
       "iodrivers411002-unsu": iodrivers411002_unsu,
       "iodrivers411003-erro": iodrivers411003_erro,
       "iodrivers411004-cloc": iodrivers411004_cloc,
       "iodrivers411005-tx-s": iodrivers411005_tx_s,
       "iodrivers412000-port": iodrivers412000_port,
       "iodrivers412001-unsu": iodrivers412001_unsu,
       "iodrivers412002-unsu": iodrivers412002_unsu,
       "iodrivers412003-erro": iodrivers412003_erro,
       "iodrivers412004-cloc": iodrivers412004_cloc,
       "iodrivers412005-tx-s": iodrivers412005_tx_s,
       "iodrivers413000-sgno": iodrivers413000_sgno,
       "iodrivers413001-sgno": iodrivers413001_sgno,
       "iodrivers413002-sgco": iodrivers413002_sgco,
       "iodrivers413003-sgia": iodrivers413003_sgia,
       "iodrivers413004-sgco": iodrivers413004_sgco,
       "iodrivers413005-sgno": iodrivers413005_sgno,
       "iodrivers413006-sgtx": iodrivers413006_sgtx,
       "iodrivers413007-sgex": iodrivers413007_sgex,
       "iodrivers413008-sglo": iodrivers413008_sglo,
       "iodrivers413009-sgex": iodrivers413009_sgex,
       "iodrivers413010-sgex": iodrivers413010_sgex,
       "iodrivers413011-sglo": iodrivers413011_sglo,
       "iodrivers413012-sgex": iodrivers413012_sgex,
       "iodrivers413013-sgin": iodrivers413013_sgin,
       "iodrivers413014-sgin": iodrivers413014_sgin,
       "iodrivers413015-sglo": iodrivers413015_sglo,
       "iodrivers413016-sgtd": iodrivers413016_sgtd,
       "iodrivers413017-sgca": iodrivers413017_sgca,
       "iodrivers413018-sgrx": iodrivers413018_sgrx,
       "iodrivers413019-sgtx": iodrivers413019_sgtx,
       "iodrivers413020-sglo": iodrivers413020_sglo,
       "iodrivers413021-sgfp": iodrivers413021_sgfp,
       "tdmclk415000-tdmclk": tdmclk415000_tdmclk,
       "router417000-nat-pkt": router417000_nat_pkt,
       "router417001-nat-add": router417001_nat_add,
       "router417002-nat-act": router417002_nat_act,
       "router417003-nat-pkt": router417003_nat_pkt,
       "wa421000-not-enough": wa421000_not_enough,
       "wa421001-unsupported": wa421001_unsupported,
       "wa421002-unsupported": wa421002_unsupported,
       "wa421003-unsupported": wa421003_unsupported,
       "wa421004-bridged-or": wa421004_bridged_or,
       "router422000-ipoatm": router422000_ipoatm,
       "router422001-ipoatm": router422001_ipoatm,
       "router422002-ipoatm": router422002_ipoatm,
       "router422003-ipoatm": router422003_ipoatm,
       "router422004-ipoatm": router422004_ipoatm,
       "router422005-ipoatm": router422005_ipoatm,
       "router422006-ipoatm": router422006_ipoatm,
       "router422007-ipoatm": router422007_ipoatm,
       "router422008-ipoatm": router422008_ipoatm,
       "tnl-nomem-rec": tnl_nomem_rec,
       "tnl-duplicate-rec": tnl_duplicate_rec,
       "tnl-improper-config": tnl_improper_config,
       "tnl-pck": tnl_pck,
       "tnl-chan-open": tnl_chan_open,
       "tnl-chan-closed": tnl_chan_closed,
       "tnl-encr-pck": tnl_encr_pck,
       "tnl-decr-pck": tnl_decr_pck,
       "tnl-queue-full": tnl_queue_full,
       "tnl-wrong-encrpck": tnl_wrong_encrpck,
       "tnl-queue-flush": tnl_queue_flush,
       "tnl-cache-del": tnl_cache_del,
       "tnl-cache-clr": tnl_cache_clr,
       "tnl-cache-garbage": tnl_cache_garbage,
       "tnl-gen": tnl_gen,
       "tnl-cache-notim": tnl_cache_notim,
       "tnl-brdg-mod-err": tnl_brdg_mod_err,
       "tnl-seq-no-debug": tnl_seq_no_debug,
       "tnl-ruihc-err": tnl_ruihc_err,
       "tnl-encr-err": tnl_encr_err}
)
